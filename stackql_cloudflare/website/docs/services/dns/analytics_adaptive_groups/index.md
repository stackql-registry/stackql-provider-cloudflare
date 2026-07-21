--- 
title: analytics_adaptive_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - analytics_adaptive_groups
  - dns
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


Creates, updates, deletes, gets or lists an <code>analytics_adaptive_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analytics_adaptive_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.analytics_adaptive_groups" /></td></tr>
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
    <td><CopyableCode code="colo_name" /></td>
    <td><code>string</code></td>
    <td>IATA code of the Cloudflare colo.</td>
</tr>
<tr>
    <td><CopyableCode code="query_name" /></td>
    <td><code>string</code></td>
    <td>DNS query name (no trailing dot).</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ip_version" /></td>
    <td><code>string</code></td>
    <td>IPv4 / IPv6.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>Transport protocol (UDP / TCP / DoH / DoT).</td>
</tr>
<tr>
    <td><CopyableCode code="queries" /></td>
    <td><code>integer</code></td>
    <td>Total DNS queries for this dimension tuple.</td>
</tr>
<tr>
    <td><CopyableCode code="queries_not_cached_not_stale" /></td>
    <td><code>integer</code></td>
    <td>Queries served fresh (not cache</td>
</tr>
<tr>
    <td><CopyableCode code="queries_stale" /></td>
    <td><code>integer</code></td>
    <td>Queries served from stale cache.</td>
</tr>
<tr>
    <td><CopyableCode code="query_type" /></td>
    <td><code>string</code></td>
    <td>DNS query type (A</td>
</tr>
<tr>
    <td><CopyableCode code="response_cached" /></td>
    <td><code>string</code></td>
    <td>Whether the response was served from cache.</td>
</tr>
<tr>
    <td><CopyableCode code="response_code" /></td>
    <td><code>string</code></td>
    <td>DNS response code (NOERROR</td>
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
    <td>DNS query analytics for a zone, grouped by query name, type, response code, cache status, and serving colo. Replaces the deprecated REST endpoints /zones/&#123;zone_id&#125;/dns_analytics/* (hard EOL 2026-12-01).</td>
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
    <td>Lower bound (inclusive). RFC3339.</td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string (date-time)</code></td>
    <td>Upper bound (exclusive). RFC3339.</td>
</tr>
<tr id="parameter-zone_tag">
    <td><CopyableCode code="zone_tag" /></td>
    <td><code>string</code></td>
    <td>Cloudflare zone ID (the 32-char hex tag).</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Maximum dimension-tuple rows per call.</td>
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

DNS query analytics for a zone, grouped by query name, type, response code, cache status, and serving colo. Replaces the deprecated REST endpoints /zones/&#123;zone_id&#125;/dns_analytics/* (hard EOL 2026-12-01).

```sql
SELECT
colo_name,
query_name,
datetime,
ip_version,
protocol,
queries,
queries_not_cached_not_stale,
queries_stale,
query_type,
response_cached,
response_code
FROM cloudflare.dns.analytics_adaptive_groups
WHERE zone_tag = '{{ zone_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
