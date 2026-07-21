# StackQL Cloudflare Provider

This directory contains the tooling and source artefacts needed to generate the StackQL provider for Cloudflare from the upstream [Cloudflare Python SDK](https://github.com/cloudflare/cloudflare-python) and its source OpenAPI specification.

The service hierarchy mirrors the Python SDK's `src/cloudflare/resources/` layout (109+ services such as `zones`, `dns`, `workers`, `zero_trust`, `accounts`).

## Quick start - make all

The whole generate -> test -> docs chain is wrapped in a `Makefile`. Run from the `stackql_cloudflare/` directory on Linux, macOS, or WSL (the server lifecycle scripts need a POSIX shell with `pgrep`/`ps`).

One-time setup (Python 3.10+, Node 18+; the Cloudflare Python SDK source must be present in the parent `src/cloudflare/` directory, which it is in this repo):

```bash
pip install pyyaml
npm install          # .npmrc configures the JSR registry needed by a transitive dep
```

Then:

```bash
make all
```

`make all` runs the following targets in order, stopping on the first failure:

| Target      | Step | Wraps                                                          | Description                                                                                                             |
| ----------- | ---- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `specs`     | 1    | `npm run generate-specs -- --clean`                            | Upstream OpenAPI -> `provider-dev/source/*.yaml` (cached download; `make specs-refresh` re-pulls the spec first).       |
| `mappings`  | 2    | `assign_resource_names --strict`                               | Refresh `all_services.csv`. **Fails if any operation has no existing mapping row** - curate the defaulted rows, re-run. |
| `provider`  | 3    | `npm run generate-provider`                                    | Generate the provider tree plus all post-gen passes.                                                                    |
| `meta-test` | 4    | `start-server` -> `test-meta-routes` -> `stop-server`          | Go/no-go gate: walk every SHOW/DESCRIBE meta route. Non-zero exit stops the build. No API token needed.                 |
| `docs`      | 6    | `npm run generate-docs`                                        | Generate Docusaurus markdown plus the sanitize, octet-stream example, and AI page enhancement post-passes.              |

Live smoke tests are deliberately NOT part of `make all` - they execute against `api.cloudflare.com` and need credentials. Run them separately after `make all` passes:

```bash
export CLOUDFLARE_API_TOKEN=...     # account-level "Workers KV Storage:Edit"
export CLOUDFLARE_ACCOUNT_ID=...
make smoke-test-kv                  # wraps server start -> bin/smoke-test-kv.cjs -> server stop
```

Step 5 (manual live UAT + smoke tests) and step 7 (publish PRs) remain human-driven so the gates can actually do their job. `make help` lists every target; each can be run individually (`make provider`, `make meta-test`, ...).

## Table of contents

- [Quick start - make all](#quick-start---make-all)
- [Pipeline steps](#pipeline-steps)
  - [Step 1 - Generate OpenAPI specs](#step-1---generate_openapi_specs) (`make specs`)
  - [Step 2 - Assign resource names](#step-2---assign_resource_names) (`make mappings`)
  - [Step 3 - Generate provider](#step-3---generate_provider) (`make provider`)
  - [Step 4 - Meta route test](#step-4---meta_route_test) (`make meta-test`)
  - [Step 5 - Live smoke / UAT](#step-5---live_smoke_uat) (manual + `make smoke-test-kv`)
  - [Step 6 - Generate web docs](#step-6---generate_webdocs) (`make docs`)
  - [Step 7a - Publish provider](#step-7a---publish_provider-stackql-provider-registry) (manual PR flow)
  - [Step 7b - Publish docs](#step-7b---publish_docs-netlify) (manual PR flow)
- [Analytics resources](#analytics-resources) - notes on the 10 GraphQL-backed analytics resources.
- [Updating to a new upstream spec](#updating-to-a-new-upstream-spec) - what to do when Cloudflare bumps the SDK.
- [Design notes](#design-notes) - the "why" behind the non-obvious decisions.
- [Addendum - upstream sync + regeneration](#addendum---upstream-sync--regeneration) - syncing this fork from `cloudflare/cloudflare-python`, plus the `gh` workflow that sidesteps the fork-network PR enumeration.

## Pipeline steps

The pipeline is seven steps: four code-generation steps (1, 2, 3, 6), two test/UAT gates (4, 5), and a final publish stage with two independent sub-targets (7a provider registry, 7b docs microsite). Each step is idempotent and can be re-run as the upstream spec evolves. Steps 1-4 and 6 are automated end-to-end by [`make all`](#quick-start---make-all).

### Step 1 - GENERATE_OPENAPI_SPECS

Download the upstream Cloudflare OpenAPI spec, normalize polymorphism, and split it into per-service yamls under `provider-dev/source/`.

```bash
make specs             # or: make specs-refresh (re-downloads the upstream spec first)
```

Underlying command:

```bash
npm run generate-specs -- --clean
# = python -m stackql_cloudflare_provider.generate_specs --clean
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

Walk the source yamls and write/refresh `provider-dev/config/all_services.csv`, mapping every operation to a stackql resource / method / verb / object key.

```bash
make mappings          # runs with --strict: fails on any unmapped operation
```

Underlying command:

```bash
npm run assign-resource-names
# = python -m stackql_cloudflare_provider.assign_resource_names
# make adds --strict (see below)
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

Use `--strict` (what `make mappings` runs) to turn "new op found" into a hard failure: the command exits non-zero if any operation had no existing mapping row, or if any row carries a hash-suffixed resource/method name (the collision-disambiguation fallback - never an acceptable end state). The default rows ARE still written, so the workflow is: review the new rows in the CSV, tighten resource/method/verb where the defaults are wrong, rename any hashed names semantically, and re-run.

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

Run `@stackql/provider-utils` to emit the final provider tree (`provider.yaml` + per-service yamls with `x-stackQL-resources` blocks), then apply all post-gen passes.

```bash
make provider
```

Underlying command:

```bash
npm run generate-provider
# = node ./bin/generate-provider.mjs (plus the post-passes listed below)
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

`generate-provider` then runs five post-passes automatically (each is idempotent and can also be run standalone via `python -m stackql_cloudflare_provider.<module>`):

1. `binary_responses` - wraps non-JSON success responses (PDFs, images, raw text, octet-stream) into a `{contents: string}` shape with a `response.transform`, so binary-download endpoints are SELECT-able as a `contents` column.
2. `request_body_transforms` - attaches a `request.transform` to write methods whose JSON body has array/object properties (the naive translator would string-wrap them on the wire).
3. `octet_stream_requests` - rewrites the handful of write methods whose request body is `application/octet-stream` (KV value PUT, Workers AI binary-input models, DLP dataset uploads). For these methods ONLY, the naive `requestBodyTranslate` is dropped; an injected `stackql*Body` wrapper schema exposes a single required `value` column via `request.schema_override`, and a `request.transform` sends it verbatim as the raw body. Callers MUST use the `data__` prefix for these methods, e.g. `REPLACE cloudflare.kv.values SET data__value = '...' WHERE ...`.
4. `ai_task_families` - collapses the ~93 per-model Workers AI run resources into 9 task-family SELECT resources (`ai.text_generation`, `ai.text_embeddings`, `ai.text_to_image`, ...) riding the generic `POST /ai/run/{model_name}` operation with `model_name` as the discriminator. WHERE params bind to body properties with unprefixed names (`WHERE model_name = '@cf/meta/llama-3.2-1b-instruct' AND prompt = '...'`), and each SELECT executes (and bills) an inference call. Config: `provider-dev/config/ai_task_families.yaml`. The generic `ai.run` resource remains as the select-only escape hatch for unlisted models, and also carries the 5 octet-stream-input models (whisper x2, resnet x2, detr) as exec methods with the `data__value` raw-body path (folded via `all_services.csv` - binary input cannot be a SELECT WHERE param).
5. `select_response_fixes` - fixes response shapes for resources whose SELECT would return no columns (untyped `result.items`, scalar arrays, raw text bodies, dynamic objects): typed item schemas for the ai model catalog, scalar-array-to-rows transforms, and `contents` wraps. Config: `provider-dev/config/select_response_fixes.yaml`.

(A final post-pass, `graphql_merge`, shims the hand-authored GraphQL operations from `provider-dev/source-graphql/` into the matching service yamls.)

### Step 4 - META_ROUTE_TEST

Go/no-go gate. Start a local stackql server backed by the freshly-built registry, then walk every documented service / resource through `SHOW METHODS / DESCRIBE`. Surfaces spec issues that only show up at SQL plan time.

```bash
make meta-test         # server start -> test -> server stop, exit status preserved
```

Underlying commands (run from Linux, macOS, or WSL - the bash scripts assume `pgrep` / `ps` and a POSIX shell):

```bash
npm run start-server                # Starts stackql on tcp/5444 with this registry mounted
npm run server-status               # Check it's up
npm run test-meta-routes            # Walk every SHOW METHODS / DESCRIBE route
npm run stop-server                 # Tear it down
```

Step 4 does NOT need a Cloudflare API token - meta routes are answered from the registry, not from a live API call.

### Step 5 - LIVE_SMOKE_UAT

Confirms the generated provider actually executes against `api.cloudflare.com`. Deliberately NOT part of `make all` - it needs live credentials. Two parts: the manual UAT queries below, and the automated full-cycle KV smoke test (`make smoke-test-kv`).

The manual part requires a Cloudflare API token scoped to whatever endpoints you want to hit (the four canned queries below need `Account Settings:Read`, `Zone:Read`, `Pages:Read`, `Workers Scripts:Read`).

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

#### Automated full-cycle KV smoke test

In addition to the manual UAT queries, `smoke-test-kv.cjs` exercises a complete create/write/read/delete lifecycle against the live API - including the `application/octet-stream` request-body path (`data__value`) on `cloudflare.kv.values`:

```bash
export CLOUDFLARE_API_TOKEN=...     # Account-level "Workers KV Storage:Edit"
export CLOUDFLARE_ACCOUNT_ID=...    # Or pass --account
make smoke-test-kv                  # Wraps server start -> test -> server stop
```

Or with the server lifecycle managed by hand:

```bash
npm run start-server
npm run smoke-test-kv
npm run stop-server
```

The token needs account-level `Workers KV Storage:Edit`. The test creates a scratch namespace (`stackql-smoke-<runid>`), REPLACEs a value via `data__value`, reads it back and asserts the round-trip, lists keys, deletes the value, confirms it is gone, and deletes the namespace (cleanup runs even on failure; `--keep` skips it). Non-zero exit on any failure.

### Step 6 - GENERATE_WEBDOCS

Generate Docusaurus markdown under `website/docs/` plus three post-passes (MDX sanitize, octet-stream `data__` examples, Workers AI page enhancement), then build and eyeball the site locally before raising the docs PR.

```bash
make docs
```

Underlying command:

```bash
npm run generate-docs
# = node ./bin/generate-docs.mjs (plus the post-passes listed below)
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

A second post-step then runs automatically:

```bash
python -m stackql_cloudflare_provider.octet_stream_docs
```

This finds every resource method carrying `request.mediaType: application/octet-stream` in the generated provider yamls (attached by the `octet_stream_requests` post-pass in step 3, so the two can't drift) and rewrites that method's SQL example on the matching docs page to show the body column `data__`-prefixed (`SET data__value = '{{ value }}'`, or `data__value` first in the INSERT column list). Naive body translation is off for those methods, so the unprefixed form docgen emits would not execute. Only the matched method's sql block is touched. Idempotent.

A third post-step, `ai_docs_enhance`, then rewrites the Workers AI task-family pages plus the generic `run` page: a `Supported models` admonition listing every valid `model_name` as copyable code (grouped by family on the run page), and runnable SELECT examples with the family's typed result columns and the model input WHERE params (prompt, text, audio, ...) that docgen cannot derive from `request.schema_override`. Driven by `provider-dev/config/ai_task_families.yaml`. Idempotent.

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

## Analytics resources

The provider exposes a curated set of 10 analytics resources covering HTTP request rollups, DNS query analytics, firewall events, Workers invocations, R2 / D1 / CDN-network metrics, and more. They require a broader API token scope than the typical REST endpoints (`Account -> Analytics -> Read`) and take a mandatory `since` / `until` time window. Example queries are in [examples/analytics/](examples/analytics/); maintainer-facing detail on the underlying dispatch is in [GRAPHQL.md](GRAPHQL.md).

## Updating to a new upstream spec

When the Cloudflare Python SDK is bumped, walk the full 7-step [pipeline](#pipeline-steps) above with two adjustments at the front end:

1. `git pull` the new SDK into `src/cloudflare/` (the parent repo).
2. Run step 1 with `--refresh` to re-download the upstream OpenAPI: `make specs-refresh` (or `npm run generate-specs -- --refresh --clean`).
3. Run step 2: `make mappings` - preserves your manual CSV edits and fails on any newly-discovered operation so you can curate the auto-defaulted rows before proceeding.
4. Review the diff in `provider-dev/source/` and `provider-dev/config/all_services.csv`, then re-run `make all` (skips nothing - specs are regenerated from the now-refreshed cache and the strict gate re-checks the CSV).
5. Continue with steps 5-7 (live UAT + smoke tests -> docs pre-flight -> publish provider + docs).

## Design notes

**Why mirror the Python SDK hierarchy rather than the upstream OpenAPI tags?**
The upstream spec declares 441 distinct tags, many of them granular (e.g. `AI Gateway Datasets`, `AI Gateway Dynamic Routes`). The SDK collapses these into 109 cohesive services. The SDK's hierarchy is the one we want StackQL users to query.

**Why pre-normalize polymorphism in the Python step instead of leaving it to `provider-utils.normalize`?**
StackQL projects schemas onto a relational model. We want tight control over how `allOf` / `oneOf` / `anyOf` collapse so we can guarantee a stable, side-effect-free superset of fields per resource. The Python normalizer does the flattening once, in-place, so the generated source/ files are already flat - downstream tooling never sees polymorphism and never has to guess.

**Why a per-service `x-stackQL-config.pagination` block instead of provider-level?**
Pagination semantics are a service-level concern in any-sdk (some Cloudflare services use cursors, others use page numbers). Setting it at the service level via `serviceConfig` in the generate wrapper keeps the option open to override on a per-service basis - just edit the generated `provider-dev/openapi/src/cloudflare/v00.00.00000/services/<service>.yaml` after step 3 if a service uses a different scheme.

## Addendum - upstream sync + regeneration

This repository is a fork of [`cloudflare/cloudflare-python`](https://github.com/cloudflare/cloudflare-python) (the official Cloudflare Python SDK, generated by Stainless). The stackql provider work all lives under `stackql_cloudflare/`, and the default branch on the fork is `stackql-provider` - not `main`. `main` exists in the fork so it can track upstream cleanly.

Branch model:

```
cloudflare/cloudflare-python:main   (upstream - Stainless auto-publishes here)
            |
            v  (periodic sync)
stackql-registry/stackql-provider-cloudflare:main
            |
            v  (merge into provider branch when ready to regenerate)
stackql-registry/stackql-provider-cloudflare:stackql-provider   (default branch)
            |
            v  (feature branches for individual changes)
feature/...
```

The sync brings in three things that drive a regeneration:

- A new upstream OpenAPI spec URL in the repo-root `.stats.yml` (`openapi_spec_url`). Step 1 reads this to download the spec.
- New / changed Python SDK source under `src/cloudflare/`. Step 1 reads this to assign upstream paths to services.
- Occasional changes to Stainless-managed root files (`pyproject.toml`, `Brewfile`, etc.). These do not affect the generator but should be merged through cleanly.

### One-time setup

Add the upstream Cloudflare repo as a remote (only needed if you'll sync from the CLI rather than the GitHub "Sync fork" button):

```bash
git remote add upstream https://github.com/cloudflare/cloudflare-python.git
git remote -v   # confirm: origin = fork, upstream = cloudflare/cloudflare-python
```

Tell `gh` to default all PR commands in this clone to the fork repo. This is the cure for the slow fork-network enumeration in the GitHub web UI when you click "New pull request" - `gh` skips the dropdowns entirely:

```bash
gh repo set-default stackql-registry/stackql-provider-cloudflare
```

The setting lives in `.git/config` per-clone.

### Syncing upstream into the fork

With the `upstream` remote configured (one-time setup above), the sync is three git commands:

```bash
git fetch upstream
git checkout main
git merge --ff-only upstream/main    # fast-forward only; bail if upstream force-pushed
git push origin main
```

That's it. No GitHub UI dance needed. If the `--ff-only` merge fails (rare - means Stainless force-pushed upstream `main`, or you've committed to `main` locally by mistake), investigate before reaching for `--no-ff` or `reset --hard`.

(`gh repo sync stackql-registry/stackql-provider-cloudflare --branch main` is a thin wrapper around the same fetch/merge if you prefer it.)

Cadence: typically quarterly, or whenever an upstream Cloudflare feature you want to expose lands in the SDK. There's no automated trigger - skim the upstream changelog and bump when relevant.

### Promoting upstream changes into `stackql-provider`

Once `main` is current, merge into the provider branch on a feature branch so the regeneration diff stays reviewable:

```bash
git checkout stackql-provider
git pull
git checkout -b feature/upstream-sync-<date>
git merge main
# Resolve any conflicts - typically only .stats.yml and src/cloudflare/ touch points; stackql_cloudflare/ should be conflict-free unless you've hand-edited generated artefacts.
```

Then run steps 1-6 of the [pipeline](#pipeline-steps) on the feature branch (`make all` covers steps 1-4 and 6). Step 2 (`make mappings`) fails on every newly-discovered upstream operation; curate the auto-defaulted CSV rows if any landed on the wrong stackql resource / method / verb, then re-run. See [Updating to a new upstream spec](#updating-to-a-new-upstream-spec) for the short form.

### Raising the PR back to `stackql-provider`

With `gh repo set-default` configured (above), the PR command collapses to:

```bash
git push -u origin feature/upstream-sync-<date>
gh pr create --base stackql-provider --title "upstream sync <date>" --body "..."
# or
gh pr create --base stackql-provider --fill   # title/body from last commit
```

`--base stackql-provider` is explicit even though it's the fork's default branch, because `gh` will otherwise sometimes guess based on what looks closest. No `--repo` flag needed (covered by `set-default`).

If you really want to use the web UI instead, bookmark the pre-filled compare URL - it skips the dropdowns:

```
https://github.com/stackql-registry/stackql-provider-cloudflare/compare/stackql-provider...<your-branch>
```

A tiny git alias makes it one command:

```bash
git config alias.pr-url '!f() { echo "https://github.com/stackql-registry/stackql-provider-cloudflare/compare/stackql-provider...$(git branch --show-current)"; }; f'
git pr-url   # prints the URL to click
```

Once the upstream-sync PR merges into `stackql-provider`, continue with step 7 of the [pipeline](#pipeline-steps) (publish provider + docs).
