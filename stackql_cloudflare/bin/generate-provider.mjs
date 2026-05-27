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
const pythonBin = process.env.PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
const bin = spawnSync(pythonBin, ['-m', 'stackql_cloudflare_provider.binary_responses'], {
  cwd: BASE_DIR,
  stdio: 'inherit',
});
if (bin.status !== 0) {
  console.error(`[generate-provider] binary_responses failed with exit ${bin.status}`);
  process.exit(bin.status ?? 1);
}
