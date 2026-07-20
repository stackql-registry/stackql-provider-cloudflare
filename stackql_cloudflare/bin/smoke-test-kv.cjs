#!/usr/bin/env node
// Full-cycle KV smoke test against a running local stackql server.
//
// Exercises the complete Workers KV lifecycle through stackql, including
// the application/octet-stream request-body handling for kv.values
// (see stackql_cloudflare_provider/octet_stream_requests.py - the value
// PUT sends the raw body, addressed as the required `data__value` column):
//
//   1. INSERT   cloudflare.kv.namespaces  (create a scratch namespace)
//   2. REPLACE  cloudflare.kv.values      (write a value - octet-stream body)
//   3. SELECT   cloudflare.kv.values      (read it back, assert round-trip)
//   4. SELECT   cloudflare.kv.keys        (assert the key is listed)
//   5. DELETE   cloudflare.kv.values      (delete the key)
//   6. SELECT   cloudflare.kv.values      (assert it is gone)
//   7. DELETE   cloudflare.kv.namespaces  (delete the scratch namespace)
//
// Prerequisites:
//   - local server running (npm run start-server) with CLOUDFLARE_API_TOKEN
//     set to a token carrying "Workers KV Storage: Edit" on the account
//   - CLOUDFLARE_ACCOUNT_ID set in the environment (or pass --account)
//
// Usage:
//   node bin/smoke-test-kv.cjs [--port 5444] [--account <account_id>] [--verbose] [--keep]

const { runQuery } = require('@stackql/pgwire-lite');

const args = process.argv.slice(2);
let port = 5444;
let verbose = false;
let keep = false;
let accountId = process.env.CLOUDFLARE_ACCOUNT_ID || '';

for (let i = 0; i < args.length; i++) {
  switch (args[i]) {
    case '--port':
      port = parseInt(args[++i], 10);
      break;
    case '--account':
      accountId = args[++i];
      break;
    case '--verbose':
      verbose = true;
      break;
    case '--keep':
      keep = true;
      break;
    case '--help':
      console.log('Usage: smoke-test-kv.cjs [--port PORT] [--account ACCOUNT_ID] [--verbose] [--keep]');
      process.exit(0);
      break;
    default:
      console.error(`Error: Unknown option "${args[i]}"`);
      process.exit(1);
  }
}

if (!accountId) {
  console.error('Error: account id required - set CLOUDFLARE_ACCOUNT_ID or pass --account');
  process.exit(1);
}

const connectionOptions = {
  user: 'stackql',
  database: 'stackql',
  host: 'localhost',
  port,
  debug: false,
};

const runId = Date.now().toString(36);
const nsTitle = `stackql-smoke-${runId}`;
const keyName = 'stackql_smoke_key';
const keyValue = `stackql-smoke-value-${runId}`;

// Mutations (REPLACE / DELETE without RETURNING) legitimately produce no
// result set - pgwire-lite surfaces that as an error we treat as success.
const NO_RESULT = "didn't produce a result";

async function query(sql, description, { allowNoResult = false, allowError = null } = {}) {
  if (verbose) {
    console.log(`\n-- ${description}\n${sql}`);
  } else {
    process.stdout.write(`${description}... `);
  }
  try {
    const result = await runQuery(connectionOptions, sql);
    const rows = result.data || [];
    if (!verbose) console.log(`ok (${rows.length} rows)`);
    else console.log(rows);
    return rows;
  } catch (error) {
    const msg = error.message || '';
    if (allowNoResult && msg.includes(NO_RESULT)) {
      if (!verbose) console.log('ok');
      return [];
    }
    if (allowError && allowError.test(msg)) {
      if (!verbose) console.log(`ok (expected error: ${msg.trim()})`);
      return null;
    }
    if (!verbose) console.log('FAILED');
    throw new Error(`${description} failed: ${msg}`);
  }
}

function fail(message) {
  console.error(`\nSMOKE TEST FAILED: ${message}`);
  process.exitCode = 1;
}

async function findNamespaceIdByTitle(title) {
  // Pagination is disabled provider-wide (first page only), so a busy
  // account may not list the scratch namespace - RETURNING is the
  // primary id source, this is the fallback.
  const rows = await query(
    `SELECT id, title FROM cloudflare.kv.namespaces WHERE account_id = '${accountId}'`,
    'Listing namespaces (fallback id lookup)'
  );
  const match = (rows || []).find(r => r.title === title);
  return match ? match.id : null;
}

async function main() {
  console.log(`\nKV full-cycle smoke test (account ${accountId}, namespace title ${nsTitle})\n`);
  let namespaceId = null;

  try {
    // 1. create scratch namespace
    let rows;
    try {
      rows = await query(
        `INSERT INTO cloudflare.kv.namespaces (title, account_id) SELECT '${nsTitle}', '${accountId}' RETURNING result`,
        'Creating scratch namespace'
      );
    } catch (e) {
      if ((e.message || '').includes(NO_RESULT)) {
        rows = [];
      } else {
        throw e;
      }
    }
    if (rows.length) {
      const raw = rows[0].result;
      try {
        const parsed = typeof raw === 'string' ? JSON.parse(raw) : raw;
        namespaceId = parsed && parsed.id;
      } catch {
        namespaceId = null;
      }
    }
    if (!namespaceId) {
      namespaceId = await findNamespaceIdByTitle(nsTitle);
    }
    if (!namespaceId) {
      throw new Error('could not determine created namespace id');
    }
    console.log(`   namespace id: ${namespaceId}`);

    // 2. write a value - the octet-stream request body path. data__value
    // is mandatory here: naive requestBodyTranslate is disabled for this
    // method and the transform splats data__value verbatim as the raw body.
    await query(
      `REPLACE cloudflare.kv.values SET data__value = '${keyValue}' ` +
      `WHERE account_id = '${accountId}' AND namespace_id = '${namespaceId}' AND key_name = '${keyName}'`,
      'Writing value (REPLACE with data__value)',
      { allowNoResult: true }
    );

    // 3. read it back
    const got = await query(
      `SELECT contents FROM cloudflare.kv.values ` +
      `WHERE account_id = '${accountId}' AND namespace_id = '${namespaceId}' AND key_name = '${keyName}'`,
      'Reading value back'
    );
    if (!got.length || got[0].contents !== keyValue) {
      throw new Error(`round-trip mismatch: expected '${keyValue}', got '${got.length ? got[0].contents : '<no rows>'}'`);
    }
    console.log('   round-trip value matches');

    // 4. key shows up in the key listing
    const keys = await query(
      `SELECT name FROM cloudflare.kv.keys WHERE account_id = '${accountId}' AND namespace_id = '${namespaceId}'`,
      'Listing keys'
    );
    if (!(keys || []).some(k => k.name === keyName)) {
      throw new Error(`key '${keyName}' not present in key listing`);
    }

    // 5. delete the key
    await query(
      `DELETE FROM cloudflare.kv.values ` +
      `WHERE account_id = '${accountId}' AND namespace_id = '${namespaceId}' AND key_name = '${keyName}'`,
      'Deleting value',
      { allowNoResult: true }
    );

    // 6. confirm it is gone (Cloudflare 404s - stackql surfaces an error
    // or an empty result depending on version; both count as deleted)
    const after = await query(
      `SELECT contents FROM cloudflare.kv.values ` +
      `WHERE account_id = '${accountId}' AND namespace_id = '${namespaceId}' AND key_name = '${keyName}'`,
      'Confirming value deleted',
      { allowError: /404|not found|key not found/i }
    );
    if (after && after.length && after[0].contents === keyValue) {
      throw new Error('value still readable after DELETE');
    }

    console.log('\nKV full cycle PASSED');
  } catch (error) {
    fail(error.message);
  } finally {
    // 7. always try to remove the scratch namespace
    if (namespaceId && !keep) {
      try {
        await query(
          `DELETE FROM cloudflare.kv.namespaces ` +
          `WHERE namespace_id = '${namespaceId}' AND account_id = '${accountId}'`,
          'Deleting scratch namespace',
          { allowNoResult: true }
        );
      } catch (error) {
        fail(`cleanup failed - namespace '${nsTitle}' (${namespaceId}) may need manual deletion: ${error.message}`);
      }
    } else if (namespaceId && keep) {
      console.log(`--keep set: leaving namespace '${nsTitle}' (${namespaceId}) in place`);
    }
  }
}

main();
