# StackQL Cloudflare Provider

This directory contains the tooling and source artefacts needed to generate the StackQL provider for Cloudflare from the upstream [Cloudflare Python SDK](https://github.com/cloudflare/cloudflare-python) and its source OpenAPI specification.

The service hierarchy mirrors the Python SDK's `src/cloudflare/resources/` layout (109+ services such as `zones`, `dns`, `workers`, `zero_trust`, `accounts`).

## Layout

```
stackql_cloudflare/
├── stackql_cloudflare_provider/      # Python package - spec generation
│   ├── generate_specs.py             # Step 1: pull upstream OpenAPI, normalize, split per service
│   ├── assign_resource_names.py     # Step 2: write/update all_services.csv
│   ├── binary_responses.py           # Step 3 post-pass: wrap non-JSON responses (PDFs, images, raw text) with a `contents` column transform
│   ├── sanitize_docs.py              # Step 4 post-pass: scrub MDX-hostile chars + rewrite Cloudflare-relative links
│   ├── sdk_index.py                  # Walks src/cloudflare/resources/ -> (verb, path) -> service map
│   ├── split.py                      # Service splitter + path -> service resolver
│   ├── fanout.py                     # Explode dual-scope /{accounts_or_zones}/... paths
│   ├── rename.py                     # Schema -> camelCase + path params -> snake_case
│   ├── canonical_params.py           # Standardise common path-param definitions (account_id, zone_id, ...)
│   ├── normalize.py                  # Schema normalizer (kills allOf/oneOf/anyOf/additionalProperties)
│   └── fold_singletons.py            # One-shot CSV mutation: fold singleton non-SELECT resources into sibling parents as exec methods
├── bin/
│   ├── generate-provider.mjs         # Step 3: provider-utils.generate wrapper
│   ├── generate-docs.mjs             # Step 4: provider-utils.generateDocs wrapper
│   ├── start-server.sh               # Starts a local stackql server against the generated registry
│   ├── stop-server.sh
│   ├── server-status.sh
│   └── test-meta-routes.cjs          # Smoke-test all SHOW/DESCRIBE routes
├── provider-dev/
│   ├── downloads/                    # Cached upstream OpenAPI spec (~17 MB)
│   ├── source/                       # Per-service yamls (step 1 output)
│   ├── config/all_services.csv       # Resource/method/verb assignments (step 2 output)
│   ├── docgen/provider-data/         # headerContent1.txt + headerContent2.txt for the website
│   └── openapi/src/cloudflare/v00.00.00000/  # Final provider (step 3 output)
└── website/docs/                     # Docusaurus markdown (step 4 output)
```

## Prerequisites

- Python 3.10+
  ```bash
  pip install pyyaml
  ```
- Node.js 18+
  ```bash
  npm install
  ```
  (The `.npmrc` configures the JSR registry needed by a transitive dep.)
- The Cloudflare Python SDK source must be present in the parent `src/cloudflare/` directory of this repository (it already is in this repo).

## End-to-end generation

Run the four steps from the directory `stackql_cloudflare/`. Each step is idempotent and can be re-run as the upstream spec evolves.

### Step 1 - GENERATE_OPENAPI_SPECS

```bash
python -m stackql_cloudflare_provider.generate_specs --clean
```

This:

1. Downloads the upstream Cloudflare OpenAPI spec (URL is sourced from the repo-root `.stats.yml`) and caches it under `provider-dev/downloads/`.
2. Normalizes the schemas in-place:
   - `allOf` -> property union (with `required` unioned).
   - `oneOf` / `anyOf` -> property union with dedup (with `required` intersected across branches).
   - `additionalProperties` and `discriminator` are stripped.
3. Walks the Python SDK at `src/cloudflare/resources/` and indexes every `self._get(...) / self._post(...) / self._get_api_list(...)` etc. call by `(verb, path)`. That index assigns each upstream OpenAPI path to its SDK top-level service.
4. For each service, builds a self-contained OpenAPI document containing only the paths assigned to it and the schemas they transitively reference, and writes it to `provider-dev/source/<service>.yaml`.

Flags:

- `--clean` - wipe `provider-dev/source/*.yaml` before regenerating.
- `--refresh` - re-download the upstream spec (ignored if the cache is missing).
- `-s <service>` - regenerate a single service only.
- `-v` - verbose logging.

### Step 2 - ASSIGN_RESOURCE_NAMES

```bash
python -m stackql_cloudflare_provider.assign_resource_names
```

Walks every `provider-dev/source/*.yaml` and ensures every operation has a row in `provider-dev/config/all_services.csv` with sensible default StackQL resource/method/verb/object_key values.

The identity key is `filename::path::verb`. If a row already exists for an operation, the user's edits to the four `stackql_*` columns are preserved verbatim - rerun this command any time you regenerate the source specs.

On subsequent runs (e.g. after refreshing the upstream spec):

- **Existing rows** keep their user-edited `stackql_*` values verbatim.
- **New operations** are auto-defaulted via the heuristics below and logged so you can spot them:
  ```
  new op found accounts.yaml POST /accounts/{account_id}/foo -> resource=foos method=create verb=insert
  ```
  Skim the logs after each spec refresh and tighten the defaults in the CSV if any new row was misclassified.
- **Operations that vanished upstream** are dropped, with a warning per row (capped at 10 shown).
- The final summary line reports the counts: `Wrote N rows to ... (new=A preserved=P reset=U dropped=D)`.

Use `--reset` to discard all user edits and re-default the entire CSV from scratch (rare; useful only when the defaulter logic itself has changed and you want to re-baseline).

CSV columns:

| Column                  | Purpose                                                                 |
| ----------------------- | ----------------------------------------------------------------------- |
| `filename`              | Source yaml (e.g. `zones.yaml`).                                        |
| `path`                  | REST API path.                                                          |
| `operationId`           | Upstream operationId (may be empty for some paths).                     |
| `formatted_op_id`       | Snake-cased + sanitised operationId, synthesized if missing upstream.   |
| `verb`                  | HTTP verb (`get` / `post` / `put` / `patch` / `delete`).                |
| `response_object`       | Component schema referenced by the 2xx response.                        |
| `tags`                  | Upstream OpenAPI tags.                                                  |
| `formatted_tags`        | Snake-cased tags.                                                       |
| `stackql_resource_name` | StackQL resource name (defaults from the SDK sub-resource).             |
| `stackql_method_name`   | StackQL method name (defaults from the SDK method name).                |
| `stackql_verb`          | StackQL verb: `select`, `insert`, `update`, `replace`, `delete`, `exec`.|
| `stackql_object_key`    | JSON path to the response array - typically `$.result`.                 |
| `op_description`        | Operation summary.                                                      |

Default heuristics:

- GET ending in a path param -> `get` (single). GET ending in a static segment -> `list`.
- POST, PUT, PATCH are mapped to `exec` whenever any of these is true (lifecycle / RPC operations):
  - The SDK method name is an action verb (`start`, `stop`, `cancel`, `purge`, `revoke`, `trigger`, `run`, `clear`, `refresh`, etc.).
  - Any static path segment is a known action word (`/purge_cache`, `/activation_check`, `/move`, `/ai/run/...`).
  - The path's leaf is a `{path_param}` (POST into an explicit ID is treated as RPC, not a relational `INSERT`).
- POST whose path leaf is a noun (no action signal) -> `insert`.
- PUT (no action signal) -> `replace`; if the SDK method is `update`, -> `update`.
- PATCH (no action signal) -> `update`.
- DELETE -> `delete`.
- Cloudflare wraps array responses in `{ "result": [...] }`, so the object key for list methods is `$.result`.

After populating defaults, a disambiguation pass renames any `(resource, method)` collision within a service by prefixing the parent path segment(s) into the resource name (e.g. `radar.summary` -> `bots_summary`, `ai_inference_summary`).

Flags:

- `--reset` - discard manual edits and re-default every row.

### Step 3 - GENERATE_PROVIDER

```bash
npm run generate-provider
```

Wraps `@stackql/provider-utils` `providerdev.generate`. Reads `provider-dev/source/` plus the CSV mapping and writes the StackQL provider tree to:

```
provider-dev/openapi/src/cloudflare/v00.00.00000/
├── provider.yaml
└── services/
    ├── zones.yaml
    ├── dns.yaml
    └── ...
```

Provider config injected:

- `auth.type: bearer` with `credentialsenvvar: CLOUDFLARE_API_TOKEN`.
- A service-level pagination block (`x-stackQL-config.pagination`) using Cloudflare's V4 page-based scheme (`page` query param, `result_info.page` response key).
- `servers: [ { url: https://api.cloudflare.com/client/v4 } ]`.

When multiple HTTP operations are exposed under the same SQL verb (e.g. `SELECT` can dispatch to either `get` on `/zones/{zone_id}` or `list` on `/zones`), `provider-utils.generate` sorts each `sqlVerbs.<verb>` list by required path-param count descending so the most-specific method is picked first. That's sufficient for the Cloudflare API - no extra sort step is needed.

### Step 4 - GENERATE_WEBDOCS

```bash
npm run generate-docs
```

Wraps `@stackql/provider-utils` `docgen.generateDocs` and emits Docusaurus markdown under `website/docs/`. Header content for the provider landing page comes from `provider-dev/docgen/provider-data/headerContent{1,2}.txt`.

The wrapper passes `dereferenced: true` so the docgen treats our specs as already-flat (we did the polymorphism flattening in step 1).

After the docs are generated, `bin/generate-docs.mjs` automatically runs a sanitisation post-step:

```bash
python -m stackql_cloudflare_provider.sanitize_docs
```

This walks every `website/docs/**/*.md` file and HTML-entity-escapes the characters `<`, `>` and `~` *inside* `<code>...</code>` blocks only. Cloudflare's API has parameter names like `meta.<field>[<operator>]` and `issue_class~neq` that MDX would otherwise parse as JSX tags or strikethrough markers, breaking the docusaurus build. Rendered output is visually identical to the originals because the substitution happens inside `<code>` already.

Re-run the sanitiser by itself any time you edit the generated markdown by hand:

```bash
python -m stackql_cloudflare_provider.sanitize_docs --verbose
```

## One-liner

```bash
python -m stackql_cloudflare_provider.generate_specs --clean \
  && python -m stackql_cloudflare_provider.assign_resource_names \
  && npm run generate-provider \
  && npm run generate-docs
```

## Local UAT - start a stackql server and run queries

After generation, set your API token and start a local stackql server backed by the freshly-built registry. Run these from Linux, macOS, or WSL (the bash scripts assume `pgrep` / `ps` and a POSIX shell):

```bash
export CLOUDFLARE_API_TOKEN=...

npm run start-server                # Starts stackql on tcp/5444 with this registry mounted
npm run server-status               # Check it's up
```

### Smoke test - meta routes

```bash
npm run test-meta-routes
```

This walks every documented service / resource and runs the `SHOW METHODS / DESCRIBE` route against the live server, surfacing any spec issues that only show up at SQL plan time.

```bash
npm run stop-server                 # Tear it down
npm run server-status               # Check it's down
```

### Interactive shell against the local registry

To poke around with `stackql shell` directly (no server, no psql client needed), point `--registry` at the directory containing `src/`. Run from the provider root so `$PWD` resolves to the right place:

```bash
REG_ROOT="$(pwd)/provider-dev/openapi"
REG="{\"url\":\"file://${REG_ROOT}\",\"localDocRoot\":\"${REG_ROOT}\",\"verifyConfig\":{\"nopVerify\":true}}"
./stackql --registry="${REG}" shell
```

Once in the shell:

```sql
SHOW PROVIDERS;
SHOW SERVICES IN cloudflare;
SHOW RESOURCES IN cloudflare.zones;
```

### UAT queries

```sql
-- 1. Show account info
SELECT id, name, type, created_on FROM cloudflare.accounts.accounts;

-- 2. Cloudflare-wide IP ranges (no auth required)
SELECT 'ipv4' AS ip_version, j.value AS cidr, etag
FROM cloudflare.ips.ips, JSON_EACH(ipv4_cidrs) j
UNION ALL
SELECT 'ipv6' AS ip_version, j.value AS cidr, etag
FROM cloudflare.ips.ips, JSON_EACH(ipv6_cidrs) j;

-- 3. List projects in an account
SELECT id, name, JSON_EXTRACT(canonical_deployment, '$.aliases[0]') as alias, JSON_EXTRACT(source, '$.url') as url FROM cloudflare.pages.projects WHERE account_id = '7dcc2c02e3445ee046a699f2e89e9285';

-- 4. List workers in an account
SELECT id, name FROM cloudflare.workers.workers WHERE account_id = '7dcc2c02e3445ee046a699f2e89e9285';
```

To stop the local server:

```bash
npm run stop-server
```

## Updating to a new upstream spec

When the Cloudflare Python SDK is bumped:

1. `git pull` the new SDK into `src/cloudflare/` (the parent repo).
2. `python -m stackql_cloudflare_provider.generate_specs --refresh --clean`
3. `python -m stackql_cloudflare_provider.assign_resource_names` (preserves your manual CSV edits).
4. `npm run generate-provider`
5. `npm run generate-docs`
6. Review the diff in `provider-dev/source/` and `provider-dev/config/all_services.csv`.
7. Commit.

## Design notes

**Why mirror the Python SDK hierarchy rather than the upstream OpenAPI tags?**
The upstream spec declares 441 distinct tags, many of them granular (e.g. `AI Gateway Datasets`, `AI Gateway Dynamic Routes`). The SDK collapses these into 109 cohesive services. The SDK's hierarchy is the one we want StackQL users to query.

**Why pre-normalize polymorphism in the Python step instead of leaving it to `provider-utils.normalize`?**
StackQL projects schemas onto a relational model. We want tight control over how `allOf` / `oneOf` / `anyOf` collapse so we can guarantee a stable, side-effect-free superset of fields per resource. The Python normalizer does the flattening once, in-place, so the generated source/ files are already flat - downstream tooling never sees polymorphism and never has to guess.

**Why a per-service `x-stackQL-config.pagination` block instead of provider-level?**
Pagination semantics are a service-level concern in any-sdk (some Cloudflare services use cursors, others use page numbers). Setting it at the service level via `serviceConfig` in the generate wrapper keeps the option open to override on a per-service basis - just edit the generated `provider-dev/openapi/src/cloudflare/v00.00.00000/services/<service>.yaml` after step 3 if a service uses a different scheme.
