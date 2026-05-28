# GraphQL operations in the Cloudflare stackql provider

Cloudflare's REST API does not cover every analytics surface. Several first-class endpoints are GraphQL-only - most notably the Zone Analytics API (REST `/zones/{id}/analytics/dashboard` is sunset and returns `code 1015: "Zone Analytics API is sunset and replaced by GraphQL API"`).

The provider shims a curated set of Cloudflare GraphQL operations into the relevant service yamls. Users querying `cloudflare.<service>.<resource>` do not need to know whether dispatch is REST or GraphQL - the abstraction is transparent.

## What's shimmed in

| Resource | Scope | Description | Supersedes |
|---|---|---|---|
| `cloudflare.zones.http_requests_adaptive_groups` | zone | HTTP request analytics with adaptive sampling, per (minute, country, status, method) | `GET /zones/{id}/analytics/dashboard` (sunset, code 1015) |
| `cloudflare.zones.http_requests_1h_groups` | zone | Hourly HTTP request rollups (requests, bytes, cache, threats, page views, etc.) | - |
| `cloudflare.zones.http_requests_overview_adaptive_groups` | zone | HTTP request overview by (country, status, content type, browser) | `GET /zones/{id}/analytics/colos` (deprecated, EOL 2026-12-01) |
| `cloudflare.dns.dns_analytics_adaptive_groups` | zone | DNS query analytics by (query name, type, code, colo) | `GET /zones/{id}/dns_analytics/*` (deprecated, EOL 2026-12-01) |
| `cloudflare.firewall.firewall_events_adaptive_groups` | zone | Firewall event rollups by (action, source, rule, country) | - |
| `cloudflare.firewall.firewall_events` | zone | Raw firewall event stream (one row per event) | - |
| `cloudflare.workers.workers_invocations` | account | Workers invocation analytics by (script, status, colo) | - |
| `cloudflare.r2.r2_operations_adaptive_groups` | account | R2 operation analytics by (bucket, action, status) | - |
| `cloudflare.d1.d1_analytics_adaptive_groups` | account | D1 query analytics by (database, role, region) | - |
| `cloudflare.cache.cdn_network_analytics_adaptive_groups` | account | Edge L3/L4 network analytics by (colo, direction, protocol) | - |

A wider inventory of Cloudflare's ~250 GraphQL nodes is in [GRAPHQL_OPS_INVENTORY.md](GRAPHQL_OPS_INVENTORY.md) - additions follow the same pattern (one manifest entry + one ops spec file) and can be incremental.

## Token scope

GraphQL Analytics requires an API token with **Account -> Analytics -> Read** permission. This is broader than the typical zone-scoped tokens you might use for REST CRUD - a zone-only token will receive a `403` from the GraphQL endpoint.

Configure the token in `CLOUDFLARE_API_TOKEN` (the same env var the REST methods use):

```bash
export CLOUDFLARE_API_TOKEN='<token-with-account-analytics-read>'
```

Some account-scoped GraphQL fields are also plan-gated (e.g. `crossZoneSubrequests` requires Enterprise). The provider does not expose plan-gated fields by default - if you need them, fork the relevant op spec under `provider-dev/source-graphql/ops/` and re-merge.

## How the protocol abstraction works

Each GraphQL operation looks like a normal REST resource from the user's perspective:

```sql
SHOW METHODS IN cloudflare.zones.http_requests_adaptive_groups;
DESCRIBE cloudflare.zones.http_requests_adaptive_groups;
SELECT datetime, requests, bytes FROM cloudflare.zones.http_requests_adaptive_groups
WHERE zone_tag = '...' AND since = '...' AND until = '...';
```

Under the hood, each shimmed operation has:

- A synthetic OpenAPI path key `/graphql/<resource>` with a POST verb (lets multiple GraphQL ops coexist in one service file).
- An `x-stackQL-graphQL` extension carrying the wire URL (`https://api.cloudflare.com/client/v4/graphql`), the GraphQL query template, and the response selection jsonpath. This is the any-sdk hook that routes the operation through the GraphQL acquire path instead of REST.
- A `response.transform` (golang_template_json_v0.3.0) that flattens Cloudflare's nested `dimensions / sum / count` row shape into flat snake_case columns. Users get a relational result set; they never see GraphQL.
- A `x-stackql-protocol: graphql` marker on the resource method block - used for introspection / grep and by the docgen post-pass to identify GraphQL methods.

The protocol marker is the only externally visible hint that GraphQL is involved.

## Example queries

Demo `.iql` files live under [examples/analytics/](examples/analytics/). Each file is parameterised with `<ZONE_TAG>` or `<ACCOUNT_TAG>` plus RFC3339 time bounds - substitute and run via:

```bash
./stackql --registry="${REG}" exec -i examples/analytics/http_requests_adaptive.iql --output json
```

Files:

- [http_requests_adaptive.iql](examples/analytics/http_requests_adaptive.iql) - replaces the sunset analytics dashboard endpoint.
- [dns_analytics.iql](examples/analytics/dns_analytics.iql) - DNS query rollup.
- [firewall_events.iql](examples/analytics/firewall_events.iql) - top firewall actions.
- [workers_invocations.iql](examples/analytics/workers_invocations.iql) - top Workers scripts by invocation count.

## Caveats

- **SELECT-only.** Cloudflare's GraphQL API has no mutations. `INSERT / UPDATE / DELETE` on these resources is not supported and will not be added (would require upstream any-sdk changes).
- **Single-page today.** Cloudflare's GraphQL pagination is filter-comparator keyset-based (not cursor-based), which does not match any-sdk's current cursor-after iteration model. All ops run as a single page bounded by the `limit` parameter (default 100). To return more rows, widen `since`/`until` or raise `limit` in the WHERE clause. Multi-page support waits on upstream any-sdk work.
- **Errors are surfaced by the transform when the response shape is unexpected.** When Cloudflare returns `{"data": null, "errors": [...]}` (auth failure, malformed query, missing permissions), the defensive transform skips the row walk and you'll see an empty result set rather than the underlying error message. Use `--http.log.enabled` to surface the processed response and inspect the raw upstream payload via curl when debugging.
- **Token scope mismatch is the most common failure mode.** A 403 from the GraphQL endpoint manifests as empty results; if rows are unexpectedly empty, verify your token has `Account -> Analytics -> Read`.

## Adding new GraphQL operations

Two-file change:

1. Add an entry to [provider-dev/source-graphql/manifest.yaml](provider-dev/source-graphql/manifest.yaml):
   ```yaml
   - field: yourGraphQLFieldName
     scope: zone               # or account
     service: <service>        # must match an existing provider-dev/openapi/.../services/<service>.yaml
     resource: <resource_name>
     method: list
     spec: ops/<spec_filename>.yaml
   ```
2. Create the spec file at `provider-dev/source-graphql/ops/<spec_filename>.yaml` mirroring the shape of existing specs. Required keys: `description`, `parameters`, `query` (template), `transform` (with the defensive null-guard pattern), `row_schema`.

Re-run `npm run generate-provider` (or just the post-pass: `python -m stackql_cloudflare_provider.graphql_merge`) to shim the new op into the matching service yaml. The merge is idempotent.
