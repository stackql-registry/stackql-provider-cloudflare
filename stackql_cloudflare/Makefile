# StackQL Cloudflare provider - build pipeline.
#
# `make all` runs the full generate -> gate -> docs chain:
#
#   specs      Step 1: download/transform upstream OpenAPI into per-service
#              yamls under provider-dev/source/ (uses the cached download;
#              use `make specs-refresh` to re-pull the upstream spec)
#   mappings   Step 2: refresh provider-dev/config/all_services.csv in
#              --strict mode - FAILS if any operation has no existing
#              mapping row. Default rows are still written for the new
#              operations; review/curate them in the CSV, then re-run.
#   provider   Step 3: generate the provider tree + ALL post-passes
#              (strip_superseded_rest, binary_responses,
#              request_body_transforms, octet_stream_requests,
#              ai_task_families, select_response_fixes, graphql_merge -
#              wired inside bin/generate-provider.mjs)
#   meta-test  Step 4 gate (go/no-go): start a local server, walk every
#              SHOW/DESCRIBE meta route, stop the server. Non-zero exit
#              stops the build. No API token needed.
#   docs       Step 6: generate Docusaurus markdown + post-passes
#              (sanitize_docs, octet_stream_docs, ai_docs_enhance -
#              wired inside bin/generate-docs.mjs)
#
# Live smoke tests are deliberately NOT part of `all` (they hit
# api.cloudflare.com and need credentials). Run them separately:
#
#   export CLOUDFLARE_API_TOKEN=...     # account-level "Workers KV Storage:Edit"
#   export CLOUDFLARE_ACCOUNT_ID=...
#   make smoke-test-kv
#
# Run from Linux, macOS, or WSL (server lifecycle scripts need a POSIX
# shell with pgrep/ps).

SHELL := /bin/bash
# python on Windows/Git Bash, python3 on WSL/Linux/macOS - override with PYTHON=...
PYTHON ?= $(shell command -v python >/dev/null 2>&1 && echo python || echo python3)
PORT ?= 5444

.PHONY: all specs specs-refresh mappings provider meta-test docs smoke-test-kv start-server stop-server help

all: specs mappings provider meta-test docs
	@echo ""
	@echo "make all complete: provider + docs generated, meta-route gate passed."
	@echo "Live smoke tests are run separately - see 'make help'."

help:
	@echo "Targets:"
	@echo "  all            specs -> mappings -> provider -> meta-test -> docs"
	@echo "  specs          Step 1: upstream OpenAPI -> provider-dev/source/*.yaml (cached download)"
	@echo "  specs-refresh  Step 1 with --refresh: re-download the upstream spec first"
	@echo "  mappings       Step 2: refresh all_services.csv (--strict: fails on unmapped operations)"
	@echo "  provider       Step 3: generate provider + all post-gen passes (binary/octet/AI families/response fixes/graphql)"
	@echo "  meta-test      Step 4 gate: SHOW/DESCRIBE walk via local server (no token needed)"
	@echo "  docs           Step 6: generate docs + sanitize/octet-example/AI-page post-passes"
	@echo "  smoke-test-kv  Live full-cycle KV test - needs CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID"
	@echo "  start-server / stop-server   Local stackql server lifecycle (PORT=$(PORT))"

specs:
	$(PYTHON) -m stackql_cloudflare_provider.generate_specs --clean

specs-refresh:
	$(PYTHON) -m stackql_cloudflare_provider.generate_specs --refresh --clean

mappings:
	$(PYTHON) -m stackql_cloudflare_provider.assign_resource_names --strict

provider:
	npm run generate-provider

# Go/no-go gate: the server is always torn down, and the meta-test's
# exit status is preserved so a failure stops `make all`.
meta-test:
	bash bin/start-server.sh --port $(PORT)
	node bin/test-meta-routes.cjs cloudflare --port $(PORT); status=$$?; bash bin/stop-server.sh --port $(PORT); exit $$status

docs:
	npm run generate-docs

# Live smoke test - NOT part of `all`. Requires:
#   CLOUDFLARE_API_TOKEN   token with account-level "Workers KV Storage:Edit"
#   CLOUDFLARE_ACCOUNT_ID  target account (or pass --account via ARGS)
smoke-test-kv:
	bash bin/start-server.sh --port $(PORT)
	node bin/smoke-test-kv.cjs --port $(PORT) $(ARGS); status=$$?; bash bin/stop-server.sh --port $(PORT); exit $$status

start-server:
	bash bin/start-server.sh --port $(PORT)

stop-server:
	bash bin/stop-server.sh --port $(PORT)
