#!/usr/bin/env node
// Wraps @stackql/provider-utils docgen.generateDocs to produce the Docusaurus
// website content under website/docs/cloudflare-docs/.
//
// Usage:
//   node bin/generate-docs.mjs                # generate all docs
//   node bin/generate-docs.mjs --verbose

import { docgen } from '@stackql/provider-utils';
import { spawnSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BASE_DIR = path.resolve(__dirname, '..');

const argv = process.argv.slice(2);
const verbose = argv.includes('--verbose') || argv.includes('-v');

const providerDir     = path.join(BASE_DIR, 'provider-dev', 'openapi', 'src', 'cloudflare', 'v00.00.00000');
// generateDocs appends "docs/" to outputDir then a {providerName}-docs/
// folder underneath. Point it at website/ so the final hierarchy lands as
// website/docs/...
const outputDir       = path.join(BASE_DIR, 'website');
const providerDataDir = path.join(BASE_DIR, 'provider-dev', 'docgen', 'provider-data');

console.log(`[generate-docs] provider:    ${providerDir}`);
console.log(`[generate-docs] providerData:${providerDataDir}`);
console.log(`[generate-docs] output:      ${outputDir}`);

const result = await docgen.generateDocs({
  providerName: 'cloudflare',
  providerDir,
  outputDir,
  providerDataDir,
  // Let docgen run SwaggerParser.dereference + flattenAllOf. Cloudflare's
  // upstream `{accounts_or_zones}` paths (which used to crash the
  // dereferencer) are now fanned out into concrete /accounts/ and /zones/
  // paths by our generator, so SwaggerParser is happy.
  dereferenced: false,
  verbose,
});

console.log(`[generate-docs] done. services=${result.totalServices} resources=${result.totalResources}`);
console.log(`[generate-docs] wrote to ${result.outputPath}`);

// Post-process: scrub MDX-hostile characters (angle brackets, tildes) out
// of <code>...</code> blocks in the generated markdown. Cloudflare API
// parameter names like `meta.<field>[<operator>]` and `issue_class~neq`
// would otherwise be parsed as JSX tags / strikethrough markers and break
// the docusaurus build.
console.log(`[generate-docs] sanitising MDX-hostile characters in <code> blocks...`);
const pythonBin = process.env.PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
const sanitize = spawnSync(pythonBin, ['-m', 'stackql_cloudflare_provider.sanitize_docs'], {
  cwd: BASE_DIR,
  stdio: 'inherit',
});
if (sanitize.status !== 0) {
  console.error(`[generate-docs] sanitize_docs failed with exit ${sanitize.status}`);
  process.exit(sanitize.status ?? 1);
}
