# StackQL Cloudflare Provider

This directory contains the tooling and source artefacts needed to generate the StackQL provider for Cloudflare from the upstream [Cloudflare Python SDK](https://github.com/cloudflare/cloudflare-python) and its source OpenAPI specification.

The service hierarchy mirrors the Python SDK's `src/cloudflare/resources/` layout (109+ services such as `zones`, `dns`, `workers`, `zero_trust`, `accounts`).

## Table of contents

- [Layout](#layout) - directory + file tour of the generator + outputs.
- [Prerequisites](#prerequisites) - Python, Node, SDK checkout.
- [End-to-end - path to production](#end-to-end---path-to-production) - the 7-step pipeline (table below).
- [One-liner](#one-liner) - codegen-only chain for steps 1-3.
- [Analytics resources](#analytics-resources) - notes on the 10 GraphQL-backed analytics resources.
- [Updating to a new upstream spec](#updating-to-a-new-upstream-spec) - what to do when Cloudflare bumps the SDK.
- [Design notes](#design-notes) - the "why" behind the non-obvious decisions.

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

## End-to-end - path to production

Run from the directory `stackql_cloudflare/`. The pipeline is seven steps: four code-generation steps (1, 2, 3, 6), two test/UAT gates (4, 5), and a final publish stage with two independent sub-targets (7a provider registry, 7b docs microsite). Each step is idempotent and can be re-run as the upstream spec evolves.

| #  | Summary                                                            | Description                                                                                                                                                |
| -- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | [OpenAPI gen](#step-1---generate_openapi_specs)                    | Download upstream Cloudflare OpenAPI, normalize polymorphism, split into per-service yamls under `provider-dev/source/`.                                   |
| 2  | [Route assignment](#step-2---assign_resource_names)                | Walk the source yamls and write/refresh `provider-dev/config/all_services.csv` mapping every operation to a stackql resource / method / verb / object key. |
| 3  | [Provider gen](#step-3---generate_provider)                        | Run `@stackql/provider-utils` to emit the final provider tree (`provider.yaml` + per-service yamls with `x-stackQL-resources` blocks).                     |
| 4  | [Meta route test](#step-4---meta_route_test)                       | Start local stackql server and walk every `SHOW METHODS / DESCRIBE` route - catches spec issues that only surface at SQL plan time. No API token needed.   |
| 5  | [Live smoke / UAT](#step-5---live_smoke_uat)                       | Open `stackql shell` against the local registry, export `CLOUDFLARE_API_TOKEN`, run the canned UAT queries to confirm real API calls succeed.              |
| 6  | [Doc gen + pre-flight](#step-6---generate_webdocs)                 | Generate Docusaurus markdown under `website/docs/`, then `yarn build` + `yarn serve` from `website/` to confirm the site compiles and pages look right.    |
| 7a | [Publish provider](#step-7a---publish_provider-stackql-provider-registry) | Copy the generated provider tree to `stackql-provider-registry/providers/src/cloudflare/`, PR to `dev`, smoke-test against `registry-dev.stackql.app`, then PR `dev` -> `main` to promote to the prod registry. |
| 7b | [Publish docs](#step-7b---publish_docs-netlify)                    | PR to `main` in this repo - Netlify builds a preview deploy on the PR; merging publishes to `https://cloudflare-provider.stackql.io/`.                     |

### Step 1 - GENERATE_OPENAPI_SPECS

```bash
npm run generate-specs -- --clean
```

(equivalent to `python -m stackql_cloudflare_provider.generate_specs --clean`)

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
npm run assign-resource-names
```

(equivalent to `python -m stackql_cloudflare_provider.assign_resource_names`)

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

### Step 4 - META_ROUTE_TEST

Start a local stackql server backed by the freshly-built registry, then walk every documented service / resource through `SHOW METHODS / DESCRIBE`. Surfaces spec issues that only show up at SQL plan time.

Run from Linux, macOS, or WSL (the bash scripts assume `pgrep` / `ps` and a POSIX shell):

```bash
npm run start-server                # Starts stackql on tcp/5444 with this registry mounted
npm run server-status               # Check it's up
npm run test-meta-routes            # Walk every SHOW METHODS / DESCRIBE route
npm run stop-server                 # Tear it down
```

Step 4 does NOT need a Cloudflare API token - meta routes are answered from the registry, not from a live API call.

### Step 5 - LIVE_SMOKE_UAT

Manual. Confirms the generated provider actually executes against `api.cloudflare.com`. Requires a Cloudflare API token scoped to whatever endpoints you want to hit (the four canned queries below need `Account Settings:Read`, `Zone:Read`, `Pages:Read`, `Workers Scripts:Read`).

```bash
export CLOUDFLARE_API_TOKEN=...
```

Then open an interactive `stackql shell` against the local registry (no server needed - point `--registry` at the directory containing `src/`). Run from the provider root so `$PWD` resolves correctly:

```bash
REG_ROOT="$(pwd)/provider-dev/openapi"
REG="{\"url\":\"file://${REG_ROOT}\",\"localDocRoot\":\"${REG_ROOT}\",\"verifyConfig\":{\"nopVerify\":true}}"
./stackql --registry="${REG}" shell
```

Sanity-check the registry shape first:

```sql
SHOW PROVIDERS;
SHOW SERVICES IN cloudflare;
SHOW RESOURCES IN cloudflare.zones;
```

Then run the UAT queries (substitute your own account ID where shown):

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
SELECT id, name, JSON_EXTRACT(canonical_deployment, '$.aliases[0]') as alias, JSON_EXTRACT(source, '$.url') as url FROM cloudflare.pages.projects WHERE account_id = '<your-account-id>';

-- 4. List workers in an account
SELECT id, name FROM cloudflare.workers.workers WHERE account_id = '<your-account-id>';
```

If anything errors or returns an unexpected shape, fix at the source (steps 1-3) and re-run before moving on.

### Step 6 - GENERATE_WEBDOCS

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

#### Pre-flight - build and serve the site locally

Before opening the docs PR (step 7b) you should compile the site and eyeball it. These are NOT wired into `generate-docs` - run them after by hand. They catch (a) MDX/markdown errors that would fail the Netlify build and (b) visually-broken pages that pass the build but read wrong:

```bash
cd website
yarn build       # Compile the site - fails loudly on MDX issues
yarn serve       # Serve the build at http://localhost:3000
```

Click through the resources you touched, plus the landing page. Stop the server with Ctrl+C. If `yarn build` fails, the Netlify PR build will also fail - fix locally first.

### Step 7a - PUBLISH_PROVIDER (stackql-provider-registry)

The generated provider tree lives at `stackql_cloudflare/provider-dev/openapi/src/cloudflare/`. Publishing it is a two-stage PR flow through the `stackql/stackql-provider-registry` repo: `dev` first for live testing against the dev registry, then `dev` -> `main` for promotion to production.

1. **Clone the registry repo locally** (or update your existing checkout):
   ```bash
   git clone https://github.com/stackql/stackql-provider-registry.git
   cd stackql-provider-registry
   git checkout dev
   git pull
   ```

2. **Copy the generated provider tree into `providers/src/`**:
   ```bash
   rsync -av --delete \
     /path/to/stackql_cloudflare/provider-dev/openapi/src/cloudflare/ \
     providers/src/cloudflare/
   ```
   (Lands as `providers/src/cloudflare/v00.00.00000/{provider.yaml,services/*.yaml}`.)

3. **Branch, commit, push, raise a PR targeting `dev`**:
   ```bash
   git checkout -b cloudflare-<release-tag>
   git add providers/src/cloudflare
   git commit -m "cloudflare: <summary of changes>"
   git push -u origin cloudflare-<release-tag>
   gh pr create --base dev --title "cloudflare: <summary>" --body "..."
   ```

4. **Wait for the PR to merge into `dev`**, then live-test against the dev registry:
   ```bash
   export CLOUDFLARE_API_TOKEN=...
   export DEV_REG="{ \"url\": \"https://registry-dev.stackql.app/providers\" }"
   ./stackql --registry="${DEV_REG}" shell
   ```
   Re-run the step-5 UAT queries against the dev registry to confirm the published artefact works end-to-end.

5. **Promote to production** by raising a PR from `dev` to `main` in `stackql-provider-registry`. Merging that PR is the path-to-production checkpoint - the public prod registry picks up the change automatically once it lands on `main`.

### Step 7b - PUBLISH_DOCS (Netlify)

The docs microsite at `https://cloudflare-provider.stackql.io/` is built by Netlify from the `website/` directory of this repo on every PR to `main`.

1. **Branch, commit, and push the regenerated `website/docs/` tree** (along with any other in-repo changes from this run - `provider-dev/source/`, `provider-dev/openapi/`, `provider-dev/config/all_services.csv`, etc.):
   ```bash
   git checkout -b cloudflare-docs-<release-tag>
   git add stackql_cloudflare/
   git commit -m "cloudflare: regenerate docs + provider for <summary>"
   git push -u origin cloudflare-docs-<release-tag>
   ```

2. **Raise a PR to `main`** of this repo. Netlify will build a preview deploy and post the URL on the PR. Click through the preview the same way you did for the local pre-flight in step 6 - confirm the pages you touched render correctly and the site builds without warnings.

3. **Merge the PR** once the Netlify preview passes review. The merge triggers a production deploy to `https://cloudflare-provider.stackql.io/`.

Steps 7a and 7b are independent and can be raised in either order - the provider works without the docs, and the docs work against either the dev or prod registry.

## One-liner

The first three steps (pure codegen, no I/O against external systems) can be chained:

```bash
npm run generate-specs -- --clean \
  && npm run assign-resource-names \
  && npm run generate-provider
```

Steps 4-7 should be run individually so the gates (meta route test, live UAT, docs pre-flight, PR reviews) can actually do their job.

## Analytics resources

The provider exposes a curated set of 10 analytics resources covering HTTP request rollups, DNS query analytics, firewall events, Workers invocations, R2 / D1 / CDN-network metrics, and more. They require a broader API token scope than the typical REST endpoints (`Account -> Analytics -> Read`) and take a mandatory `since` / `until` time window. Example queries are in [examples/analytics/](examples/analytics/); maintainer-facing detail on the underlying dispatch is in [GRAPHQL.md](GRAPHQL.md).

## Updating to a new upstream spec

When the Cloudflare Python SDK is bumped, walk the full 7-step path-to-production above with two adjustments at the front end:

1. `git pull` the new SDK into `src/cloudflare/` (the parent repo).
2. Run step 1 with `--refresh` to re-download the upstream OpenAPI: `npm run generate-specs -- --refresh --clean`.
3. Run step 2: `npm run assign-resource-names` - preserves your manual CSV edits and logs any newly-discovered operations so you can spot-check them.
4. Review the diff in `provider-dev/source/` and `provider-dev/config/all_services.csv` before proceeding.
5. Continue with steps 3-7 (provider gen -> meta route test -> live UAT -> doc gen + pre-flight -> publish provider + docs).

## Design notes

**Why mirror the Python SDK hierarchy rather than the upstream OpenAPI tags?**
The upstream spec declares 441 distinct tags, many of them granular (e.g. `AI Gateway Datasets`, `AI Gateway Dynamic Routes`). The SDK collapses these into 109 cohesive services. The SDK's hierarchy is the one we want StackQL users to query.

**Why pre-normalize polymorphism in the Python step instead of leaving it to `provider-utils.normalize`?**
StackQL projects schemas onto a relational model. We want tight control over how `allOf` / `oneOf` / `anyOf` collapse so we can guarantee a stable, side-effect-free superset of fields per resource. The Python normalizer does the flattening once, in-place, so the generated source/ files are already flat - downstream tooling never sees polymorphism and never has to guess.

**Why a per-service `x-stackQL-config.pagination` block instead of provider-level?**
Pagination semantics are a service-level concern in any-sdk (some Cloudflare services use cursors, others use page numbers). Setting it at the service level via `serviceConfig` in the generate wrapper keeps the option open to override on a per-service basis - just edit the generated `provider-dev/openapi/src/cloudflare/v00.00.00000/services/<service>.yaml` after step 3 if a service uses a different scheme.
