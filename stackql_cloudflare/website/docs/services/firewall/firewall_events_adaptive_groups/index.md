--- 
title: firewall_events_adaptive_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_events_adaptive_groups
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


Creates, updates, deletes, gets or lists a <code>firewall_events_adaptive_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_events_adaptive_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.firewall_events_adaptive_groups" /></td></tr>
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
    <td>Product-specific rule ID triggered by this event.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleset_id" /></td>
    <td><code>string</code></td>
    <td>Product-specific ruleset ID triggered by this event.</td>
</tr>
<tr>
    <td><CopyableCode code="client_country_name" /></td>
    <td><code>string</code></td>
    <td>ISO-3166 alpha-2 country code derived from client IP.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>First-class action taken by the firewall (block, challenge, jschallenge, log, allow, etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="client_asn_description" /></td>
    <td><code>string</code></td>
    <td>Visitor ASN as a string (e.g. AS15169 Google LLC).</td>
</tr>
<tr>
    <td><CopyableCode code="client_ip" /></td>
    <td><code>string</code></td>
    <td>Visitor IP address (IPv4 or IPv6).</td>
</tr>
<tr>
    <td><CopyableCode code="client_request_http_host" /></td>
    <td><code>string</code></td>
    <td>Hostname component of the client request.</td>
</tr>
<tr>
    <td><CopyableCode code="client_request_path" /></td>
    <td><code>string</code></td>
    <td>Path component of the client request.</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minute-bucketed timestamp (RFC3339).</td>
</tr>
<tr>
    <td><CopyableCode code="edge_response_status" /></td>
    <td><code>integer</code></td>
    <td>HTTP status returned to the client.</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>integer</code></td>
    <td>Number of firewall events contributing to this dimension tuple.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Cloudflare security product that triggered the event (waf, firewallrules, ratelimit, etc.).</td>
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
    <td>Firewall event analytics for a zone, with adaptive sampling, grouped by action / source / rule / country / status. Each row aggregates the count of firewall events for one dimension tuple over the requested time window. Useful for surfacing top blocking rules, top blocked countries, top targeted paths.</td>
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
    <td>Lower bound (inclusive) of the time range. RFC3339 (e.g. 2026-05-29T00:00:00Z).</td>
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
    <td>Maximum number of dimension-tuple rows to return per call.</td>
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

Firewall event analytics for a zone, with adaptive sampling, grouped by action / source / rule / country / status. Each row aggregates the count of firewall events for one dimension tuple over the requested time window. Useful for surfacing top blocking rules, top blocked countries, top targeted paths.

```sql
SELECT
rule_id,
ruleset_id,
client_country_name,
action,
client_asn_description,
client_ip,
client_request_http_host,
client_request_path,
datetime,
edge_response_status,
events,
source
FROM cloudflare.firewall.firewall_events_adaptive_groups
WHERE zone_tag = '{{ zone_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
