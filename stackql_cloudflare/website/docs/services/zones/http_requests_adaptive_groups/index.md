--- 
title: http_requests_adaptive_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - http_requests_adaptive_groups
  - zones
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


Creates, updates, deletes, gets or lists a <code>http_requests_adaptive_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="http_requests_adaptive_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.http_requests_adaptive_groups" /></td></tr>
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
    <td><CopyableCode code="client_country_name" /></td>
    <td><code>string</code></td>
    <td>ISO-3166 alpha-2 country code derived from client IP.</td>
</tr>
<tr>
    <td><CopyableCode code="client_request_http_method_name" /></td>
    <td><code>string</code></td>
    <td>HTTP method (GET, POST, etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer</code></td>
    <td>Total bytes served to the client from the edge.</td>
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
    <td><CopyableCode code="requests" /></td>
    <td><code>integer</code></td>
    <td>Total request count for this dimension tuple.</td>
</tr>
<tr>
    <td><CopyableCode code="visits" /></td>
    <td><code>integer</code></td>
    <td>Requests by end-users that were initiated from a different website (i.e. the HTTP Referer header does not match the host in the HTTP Host header). A coarse "human visitor" heuristic.</td>
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
    <td>HTTP request analytics for a zone with adaptive sampling, grouped by minute, client country, edge response status, and HTTP method. Replaces the sunset REST endpoint /zones/&#123;zone_id&#125;/analytics/dashboard. Each row aggregates request count, byte volume, cache hits, and threat counts for one dimension tuple over the requested time window.</td>
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
    <td>Lower bound (inclusive) of the time range. RFC3339 (e.g. 2026-05-28T00:00:00Z).</td>
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

HTTP request analytics for a zone with adaptive sampling, grouped by minute, client country, edge response status, and HTTP method. Replaces the sunset REST endpoint /zones/&#123;zone_id&#125;/analytics/dashboard. Each row aggregates request count, byte volume, cache hits, and threat counts for one dimension tuple over the requested time window.

```sql
SELECT
client_country_name,
client_request_http_method_name,
bytes,
datetime,
edge_response_status,
requests,
visits
FROM cloudflare.zones.http_requests_adaptive_groups
WHERE zone_tag = '{{ zone_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
