--- 
title: firewall_events
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_events
  - firewall
  - cloudflare
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage cloudflare resources using SQL
custom_edit_url: null
image: /img/stackql-cloudflare-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::info[Analytics resource]

This is a time-bounded analytics resource. Queries against it differ from typical CRUD resources in a few ways:

- **`since` and `until` are required.** Both are RFC3339 timestamps and define the analytics window (e.g. `since = '2026-05-28T00:00:00Z'`, `until = '2026-05-29T00:00:00Z'`). Queries without them will fail.
- **Row cap via `limit`.** The `limit` parameter (default `100`) bounds the response. Widen the time window or raise `limit` to return more rows.
- **Token scope.** Cloudflare's analytics endpoints require an API token with **Account -> Analytics -> Read** permission, which is broader than typical zone-scoped tokens. A token without it will return empty results.

:::


Creates, updates, deletes, gets or lists a <code>firewall_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.firewall_events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Response

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td>Product-specific rule ID.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleset_id" /></td>
    <td><code>string</code></td>
    <td>Product-specific ruleset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="client_country_name" /></td>
    <td><code>string</code></td>
    <td>ISO-3166 alpha-2 country code.</td>
</tr>
<tr>
    <td><CopyableCode code="client_request_http_method_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="edge_colo_name" /></td>
    <td><code>string</code></td>
    <td>IATA code of the Cloudflare colo that served the request.</td>
</tr>
<tr>
    <td><CopyableCode code="ray_name" /></td>
    <td><code>string</code></td>
    <td>Cloudflare Ray ID.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>First-class action (block / challenge / allow / log / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="client_asn" /></td>
    <td><code>integer</code></td>
    <td>Visitor ASN.</td>
</tr>
<tr>
    <td><CopyableCode code="client_asn_description" /></td>
    <td><code>string</code></td>
    <td>Visitor ASN description.</td>
</tr>
<tr>
    <td><CopyableCode code="client_ip" /></td>
    <td><code>string</code></td>
    <td>Visitor IP (v4 or v6).</td>
</tr>
<tr>
    <td><CopyableCode code="client_request_http_host" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="client_request_path" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Event timestamp (RFC3339).</td>
</tr>
<tr>
    <td><CopyableCode code="edge_response_status" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="origin_response_status" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ref" /></td>
    <td><code>string</code></td>
    <td>User-defined rule ref tag.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Security product that fired (waf / firewallrules / ratelimit / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="user_agent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_tag"><code>zone_tag</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-until"><code>until</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a></td>
    <td>Raw firewall event stream for a zone. One row per event with attacker context (IP, ASN, country) and rule context (action, source, ruleId). Use for incident drill-down rather than rollups.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date-time)</code></td>
    <td>Lower bound (inclusive) of the time range. RFC3339.</td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string (date-time)</code></td>
    <td>Upper bound (exclusive) of the time range. RFC3339.</td>
</tr>
<tr id="parameter-zone_tag">
    <td><CopyableCode code="zone_tag" /></td>
    <td><code>string</code></td>
    <td>Cloudflare zone ID (the 32-char hex tag).</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of events to return per call.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Raw firewall event stream for a zone. One row per event with attacker context (IP, ASN, country) and rule context (action, source, ruleId). Use for incident drill-down rather than rollups.

```sql
SELECT
rule_id,
ruleset_id,
client_country_name,
client_request_http_method_name,
edge_colo_name,
ray_name,
action,
client_asn,
client_asn_description,
client_ip,
client_request_http_host,
client_request_path,
datetime,
edge_response_status,
origin_response_status,
ref,
source,
user_agent
FROM cloudflare.firewall.firewall_events
WHERE zone_tag = '{{ zone_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
