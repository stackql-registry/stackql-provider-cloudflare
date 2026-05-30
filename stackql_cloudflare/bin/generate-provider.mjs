#!/usr/bin/env node
// Wraps @stackql/provider-utils providerdev.generate to build the Cloudflare
// StackQL provider from the per-service yamls under provider-dev/source/
// plus the resource mapping in provider-dev/config/all_services.csv.
//
// Output: provider-dev/openapi/src/cloudflare/v00.00.00000/{provider.yaml,services/*.yaml}
//
// Usage:
//   node bin/generate-provider.mjs               # generate all services
//   node bin/generate-provider.mjs --verbose
//   node bin/generate-provider.mjs --overwrite

import { providerdev } from '@stackql/provider-utils';
import { spawnSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BASE_DIR = path.resolve(__dirname, '..');

const argv = process.argv.slice(2);
const verbose = argv.includes('--verbose') || argv.includes('-v');
const overwrite = argv.includes('--overwrite');

const inputDir   = path.join(BASE_DIR, 'provider-dev', 'source');
// Generator writes <outputDir>/<version>/{provider.yaml,services/}, but the
// provider.yaml's $refs point at `cloudflare/<version>/services/...`. So we
// nest the outputDir under a `cloudflare/` directory to make the refs resolve
// when the stackql server's registry root is `provider-dev/openapi/src/`.
const outputDir  = path.join(BASE_DIR, 'provider-dev', 'openapi', 'src', 'cloudflare');
const configPath = path.join(BASE_DIR, 'provider-dev', 'config', 'all_services.csv');

// Cloudflare wraps list responses in `{ "result": [...], "result_info": { ... } }`
// with page-based pagination via `page` and `per_page` query params, and an
// optional cursor for newer APIs.
const providerConfig = JSON.stringify({
  auth: {
    type: 'bearer',
    credentialsenvvar: 'CLOUDFLARE_API_TOKEN',
  },
});

// Pagination is parked. Cloudflare's V4 API uses `page` request +
// `result_info.{page,total_pages}` response, but any-sdk's token-based
// pagination model can't express the "stop when page >= total_pages"
// termination - it just echoes `result_info.page` back as `?page=1` and
// loops forever on the same response. See the any-sdk issue tracking
// page-number+total-pages support. Until that lands, ship without
// pagination - the first page (default 20 rows) returns cleanly.
const serviceConfig = null;

// provider-utils' generate expects servers as a JSON string.
const servers = JSON.stringify([
  { url: 'https://api.cloudflare.com/client/v4' },
]);

console.log(`[generate-provider] input:   ${inputDir}`);
console.log(`[generate-provider] output:  ${outputDir}`);
console.log(`[generate-provider] config:  ${configPath}`);

// Pre-process: strip upstream REST endpoints that have been superseded
// by hand-authored GraphQL operations (read from the source-graphql
// manifest's `replaces_rest` blocks). Targets are removed from the
// source yamls AND from all_services.csv so the downstream provider +
// docs do not surface dead / sunset endpoints (e.g. /zones/{id}/
// analytics/dashboard, which returns code 1015). Idempotent.
const pythonBin = process.env.PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
console.log(`[generate-provider] stripping REST endpoints superseded by source-graphql/manifest.yaml...`);
const strip = spawnSync(pythonBin, ['-m', 'stackql_cloudflare_provider.strip_superseded_rest'], {
  cwd: BASE_DIR,
  stdio: 'inherit',
});
if (strip.status !== 0) {
  console.error(`[generate-provider] strip_superseded_rest failed with exit ${strip.status}`);
  process.exit(strip.status ?? 1);
}

const result = await providerdev.generate({
  inputDir,
  outputDir,
  configPath,
  providerId: 'cloudflare',
  servers,
  providerConfig,
  serviceConfig,
  // Attach `config.requestBodyTranslate.algorithm = naive` to every
  // POST/PUT/PATCH method that has a request body. Effect: callers can
  // write `INSERT INTO ... SELECT name, type, unit` instead of
  // `... SELECT data__name, data__type, data__unit`. The `data__` prefix
  // is only needed to avoid clashes between body-param names and response
  // properties - Cloudflare's surface doesn't have those clashes.
  naiveReqBodyTranslate: true,
  overwrite,
  verbose,
});

if (result === false) {
  console.error('[generate-provider] generation failed - see errors above');
  process.exit(1);
}

console.log(`[generate-provider] done. services=${result.serviceCount} resources=${result.resourceCount} methods=${result.methodCount}`);
console.log(`[generate-provider] wrote to ${result.outputDirectory}`);

// Post-process: wrap non-JSON success responses (PDFs, images, raw text,
// application/octet-stream, etc.) into a `{contents: string}` JSON shape
// and attach a stackql response.transform to each resource method that
// references them. Result: those endpoints become SELECT-able as a
// one-row table with a `contents` column.
console.log(`[generate-provider] wrapping binary / non-JSON responses with contents column transform...`);
const bin = spawnSync(pythonBin, ['-m', 'stackql_cloudflare_provider.binary_responses'], {
  cwd: BASE_DIR,
  stdio: 'inherit',
});
if (bin.status !== 0) {
  console.error(`[generate-provider] binary_responses failed with exit ${bin.status}`);
  process.exit(bin.status ?? 1);
}

// Post-process: attach `request.transform` blocks to write methods whose
// body schemas have array- or object-typed properties. Under stackql's
// `naive` requestBodyTranslate, those values arrive as Go strings and
// get string-wrapped on the wire (e.g. `{"rules": "[{...}]"}`), which
// Cloudflare rejects. The transform re-emits the body with `kindOf`-based
// branching: parsed slice/map -> toJson; raw string -> splat verbatim.
console.log(`[generate-provider] attaching request.transform for array/object body properties...`);
const reqtx = spawnSync(pythonBin, ['-m', 'stackql_cloudflare_provider.request_body_transforms'], {
  cwd: BASE_DIR,
  stdio: 'inherit',
});
if (reqtx.status !== 0) {
  console.error(`[generate-provider] request_body_transforms failed with exit ${reqtx.status}`);
  process.exit(reqtx.status ?? 1);
}

// Post-process: shim hand-authored Cloudflare GraphQL operations into
// the matching service yamls. Source manifest + per-op specs live under
// provider-dev/source-graphql/. The merge script is idempotent and only
// touches services referenced by the manifest, so REST-only services
// are untouched.
console.log(`[generate-provider] shimming GraphQL operations from provider-dev/source-graphql/...`);
const gql = spawnSync(pythonBin, ['-m', 'stackql_cloudflare_provider.graphql_merge'], {
  cwd: BASE_DIR,
  stdio: 'inherit',
});
if (gql.status !== 0) {
  console.error(`[generate-provider] graphql_merge failed with exit ${gql.status}`);
  process.exit(gql.status ?? 1);
}
