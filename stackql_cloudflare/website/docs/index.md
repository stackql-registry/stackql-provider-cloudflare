---
title: cloudflare
hide_title: false
hide_table_of_contents: false
keywords:
  - cloudflare
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Cloudflare resources using SQL
custom_edit_url: null
image: /img/stackql-cloudflare-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

The connectivity cloud - DNS, CDN, Zero Trust, Workers, and more.


:::info[Provider Summary] 

total services: __108__  
total resources: __1235__  

:::

See also:
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * *

## Installation

To pull the latest version of the `cloudflare` provider, run the following command:

```bash
REGISTRY PULL cloudflare;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).

## Authentication

The following system environment variable is used for authentication by default:

- <CopyableCode code="CLOUDFLARE_API_TOKEN" /> - A Cloudflare API token (see <a href="https://developers.cloudflare.com/fundamentals/api/get-started/create-token/">Create a token</a>)

This variable is sourced at runtime (from the local machine or as a CI variable/secret).

<details>

<summary>Using a different environment variable</summary>

To use a different environment variable (instead of the default), use the `--auth` flag of the `stackql` program. For example:

```bash

AUTH='{ "cloudflare": { "type": "bearer", "credentialsenvvar": "YOUR_CLOUDFLARE_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:

```powershell

$Auth = "{ 'cloudflare': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_CLOUDFLARE_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Example Queries

Try the following queries using `stackql shell`, or run them from a script or CI pipeline with `stackql exec`.

### Accounts

Accounts the token has access to, with the IDs the other queries take as `account_id`:

```sql
SELECT id, name, type, created_on
FROM cloudflare.accounts.accounts
ORDER BY name;
```

### Zones by status and plan

Every zone visible to the token, with its status, plan and owning account read from the nested `plan` and `account` columns:

```sql
SELECT name, status, paused, type,
       json_extract(plan, '$.name') AS plan_name,
       json_extract(account, '$.name') AS account_name
FROM cloudflare.zones.zones
ORDER BY account_name, name;
```

### DNS records of one type in a zone

A records in a zone, with the `type` filter passed through to the API:

```sql
SELECT name, content, proxied, ttl, comment
FROM cloudflare.dns.zones_dns_records
WHERE zone_id = '{{ zone_id }}' AND type = 'A'
ORDER BY name;
```

### DNS records across every zone

All records in every zone, resolved from the zone list with one request per zone:

```sql
SELECT z.name AS zone, r.name AS record, r.type, r.content, r.proxied, r.ttl
FROM cloudflare.zones.zones z
JOIN cloudflare.dns.zones_dns_records r ON r.zone_id = z.id
ORDER BY zone, r.type, record;
```

### Workers scripts

Scripts deployed in an account (`id` is the script name), most recently modified first:

```sql
SELECT id, modified_on, compatibility_date, usage_model, has_modules, logpush
FROM cloudflare.workers.scripts
WHERE account_id = '{{ account_id }}'
ORDER BY modified_on DESC;
```

### KV namespaces and R2 buckets

Workers KV namespaces and R2 buckets in an account as one storage inventory:

```sql
SELECT 'kv' AS store, title AS name, NULL AS location, NULL AS storage_class
FROM cloudflare.kv.namespaces
WHERE account_id = '{{ account_id }}'
UNION ALL
SELECT 'r2', name, location, storage_class
FROM cloudflare.r2.buckets
WHERE account_id = '{{ account_id }}';
```

### Rulesets for a zone

WAF, rate limiting and other rulesets deployed to a zone, ordered by phase:

```sql
SELECT name, phase, kind, version, last_updated
FROM cloudflare.rulesets.rulesets
WHERE zone_id = '{{ zone_id }}'
ORDER BY phase, name;
```

### Cloudflare Tunnels by health

Tunnels in an account with their health status and the time they last had an active connection:

```sql
SELECT name, status, tun_type, config_src, conns_active_at, created_at
FROM cloudflare.zero_trust.tunnels
WHERE account_id = '{{ account_id }}'
ORDER BY status, name;
```

### Workers invocations over a time window

Invocations, errors and CPU time per script over a window, from the GraphQL analytics resource (the token needs Analytics Read on the account, and `account_tag` takes the account ID):

```sql
SELECT script_name, status,
       SUM(requests) AS invocations,
       SUM(errors) AS errors,
       SUM(cpu_time_us) AS cpu_time_us
FROM cloudflare.workers.invocations
WHERE account_tag = '{{ account_id }}'
  AND since = '2026-09-16T00:00:00Z'
  AND until = '2026-09-17T00:00:00Z'
GROUP BY script_name, status
ORDER BY invocations DESC;
```

### KV namespace lifecycle

Create a namespace (`RETURNING result` returns the new namespace with its `id`), rename it, then delete it:

```sql
INSERT INTO cloudflare.kv.namespaces (title, account_id)
SELECT 'stackql-demo', '{{ account_id }}'
RETURNING result;

REPLACE cloudflare.kv.namespaces
SET title = 'stackql-demo-renamed'
WHERE namespace_id = '{{ namespace_id }}' AND account_id = '{{ account_id }}';

DELETE FROM cloudflare.kv.namespaces
WHERE namespace_id = '{{ namespace_id }}' AND account_id = '{{ account_id }}';
```


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/abuse_reports/">abuse_reports</a><br />
<a href="/services/accounts/">accounts</a><br />
<a href="/services/acm/">acm</a><br />
<a href="/services/addressing/">addressing</a><br />
<a href="/services/ai/">ai</a><br />
<a href="/services/ai_gateway/">ai_gateway</a><br />
<a href="/services/ai_search/">ai_search</a><br />
<a href="/services/alerting/">alerting</a><br />
<a href="/services/api_gateway/">api_gateway</a><br />
<a href="/services/argo/">argo</a><br />
<a href="/services/audit_logs/">audit_logs</a><br />
<a href="/services/billing/">billing</a><br />
<a href="/services/bot_management/">bot_management</a><br />
<a href="/services/botnet_feed/">botnet_feed</a><br />
<a href="/services/brand_protection/">brand_protection</a><br />
<a href="/services/browser_rendering/">browser_rendering</a><br />
<a href="/services/cache/">cache</a><br />
<a href="/services/calls/">calls</a><br />
<a href="/services/certificate_authorities/">certificate_authorities</a><br />
<a href="/services/client_certificates/">client_certificates</a><br />
<a href="/services/cloud_connector/">cloud_connector</a><br />
<a href="/services/cloudforce_one/">cloudforce_one</a><br />
<a href="/services/connectivity/">connectivity</a><br />
<a href="/services/content_scanning/">content_scanning</a><br />
<a href="/services/custom_certificates/">custom_certificates</a><br />
<a href="/services/custom_hostnames/">custom_hostnames</a><br />
<a href="/services/custom_nameservers/">custom_nameservers</a><br />
<a href="/services/custom_pages/">custom_pages</a><br />
<a href="/services/d1/">d1</a><br />
<a href="/services/dcv_delegation/">dcv_delegation</a><br />
<a href="/services/ddos_protection/">ddos_protection</a><br />
<a href="/services/diagnostics/">diagnostics</a><br />
<a href="/services/dns/">dns</a><br />
<a href="/services/dns_firewall/">dns_firewall</a><br />
<a href="/services/durable_objects/">durable_objects</a><br />
<a href="/services/email_routing/">email_routing</a><br />
<a href="/services/email_security/">email_security</a><br />
<a href="/services/email_sending/">email_sending</a><br />
<a href="/services/filters/">filters</a><br />
<a href="/services/firewall/">firewall</a><br />
<a href="/services/fraud/">fraud</a><br />
<a href="/services/google_tag_gateway/">google_tag_gateway</a><br />
<a href="/services/healthchecks/">healthchecks</a><br />
<a href="/services/hostnames/">hostnames</a><br />
<a href="/services/hyperdrive/">hyperdrive</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/images/">images</a><br />
<a href="/services/intel/">intel</a><br />
<a href="/services/ips/">ips</a><br />
<a href="/services/keyless_certificates/">keyless_certificates</a><br />
<a href="/services/kv/">kv</a><br />
<a href="/services/leaked_credential_checks/">leaked_credential_checks</a><br />
<a href="/services/load_balancers/">load_balancers</a><br />
<a href="/services/logpush/">logpush</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/logs/">logs</a><br />
<a href="/services/magic_cloud_networking/">magic_cloud_networking</a><br />
<a href="/services/magic_network_monitoring/">magic_network_monitoring</a><br />
<a href="/services/magic_transit/">magic_transit</a><br />
<a href="/services/managed_transforms/">managed_transforms</a><br />
<a href="/services/memberships/">memberships</a><br />
<a href="/services/mtls_certificates/">mtls_certificates</a><br />
<a href="/services/network_interconnects/">network_interconnects</a><br />
<a href="/services/organizations/">organizations</a><br />
<a href="/services/origin_ca_certificates/">origin_ca_certificates</a><br />
<a href="/services/origin_post_quantum_encryption/">origin_post_quantum_encryption</a><br />
<a href="/services/origin_tls_client_auth/">origin_tls_client_auth</a><br />
<a href="/services/page_rules/">page_rules</a><br />
<a href="/services/page_shield/">page_shield</a><br />
<a href="/services/pages/">pages</a><br />
<a href="/services/pipelines/">pipelines</a><br />
<a href="/services/queues/">queues</a><br />
<a href="/services/r2/">r2</a><br />
<a href="/services/r2_data_catalog/">r2_data_catalog</a><br />
<a href="/services/radar/">radar</a><br />
<a href="/services/rate_limits/">rate_limits</a><br />
<a href="/services/realtime_kit/">realtime_kit</a><br />
<a href="/services/registrar/">registrar</a><br />
<a href="/services/request_tracers/">request_tracers</a><br />
<a href="/services/resource_sharing/">resource_sharing</a><br />
<a href="/services/resource_tagging/">resource_tagging</a><br />
<a href="/services/rules/">rules</a><br />
<a href="/services/rulesets/">rulesets</a><br />
<a href="/services/rum/">rum</a><br />
<a href="/services/schema_validation/">schema_validation</a><br />
<a href="/services/secrets_store/">secrets_store</a><br />
<a href="/services/security_center/">security_center</a><br />
<a href="/services/security_txt/">security_txt</a><br />
<a href="/services/snippets/">snippets</a><br />
<a href="/services/spectrum/">spectrum</a><br />
<a href="/services/speed/">speed</a><br />
<a href="/services/ssl/">ssl</a><br />
<a href="/services/streams/">streams</a><br />
<a href="/services/tenants/">tenants</a><br />
<a href="/services/token_validation/">token_validation</a><br />
<a href="/services/turnstile/">turnstile</a><br />
<a href="/services/url_normalization/">url_normalization</a><br />
<a href="/services/url_scanner/">url_scanner</a><br />
<a href="/services/user/">user</a><br />
<a href="/services/vectorize/">vectorize</a><br />
<a href="/services/vulnerability_scanner/">vulnerability_scanner</a><br />
<a href="/services/waiting_rooms/">waiting_rooms</a><br />
<a href="/services/web3/">web3</a><br />
<a href="/services/workers/">workers</a><br />
<a href="/services/workers_for_platforms/">workers_for_platforms</a><br />
<a href="/services/workflows/">workflows</a><br />
<a href="/services/zaraz/">zaraz</a><br />
<a href="/services/zero_trust/">zero_trust</a><br />
<a href="/services/zones/">zones</a><br />
</div>
</div>
