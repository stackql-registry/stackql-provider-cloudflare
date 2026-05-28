--- 
title: http_requests_1h_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - http_requests_1h_groups
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


Creates, updates, deletes, gets or lists a <code>http_requests_1h_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="http_requests_1h_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.http_requests_1h_groups" /></td></tr>
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
    <td><CopyableCode code="bytes" /></td>
    <td><code>integer</code></td>
    <td>Total bytes served from the edge for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="cached_bytes" /></td>
    <td><code>integer</code></td>
    <td>Bytes served from cache for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="cached_requests" /></td>
    <td><code>integer</code></td>
    <td>Requests served from cache for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="date" /></td>
    <td><code>string (date)</code></td>
    <td>Date component of the hour bucket (YYYY-MM-DD).</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Hour-bucketed timestamp (RFC3339).</td>
</tr>
<tr>
    <td><CopyableCode code="edge_request_bytes" /></td>
    <td><code>integer</code></td>
    <td>Bytes received from the client over the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="encrypted_bytes" /></td>
    <td><code>integer</code></td>
    <td>Bytes served over TLS for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="encrypted_requests" /></td>
    <td><code>integer</code></td>
    <td>Requests served over TLS for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="page_views" /></td>
    <td><code>integer</code></td>
    <td>Successful HTML content requests for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>integer</code></td>
    <td>Total request count for the hour.</td>
</tr>
<tr>
    <td><CopyableCode code="threats" /></td>
    <td><code>integer</code></td>
    <td>Requests classified as threats for the hour.</td>
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
    <td>Hourly-bucketed HTTP request totals for a zone. One row per hour with totals for requests, bytes, threats, page views, cache hits/bytes, encrypted requests/bytes, and edge request bytes. Use for last-N-hours traffic dashboards and trend visualisations.</td>
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
    <td>Maximum hourly rows to return per call. Default 168 (one week of hourly buckets).</td>
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

Hourly-bucketed HTTP request totals for a zone. One row per hour with totals for requests, bytes, threats, page views, cache hits/bytes, encrypted requests/bytes, and edge request bytes. Use for last-N-hours traffic dashboards and trend visualisations.

```sql
SELECT
bytes,
cached_bytes,
cached_requests,
date,
datetime,
edge_request_bytes,
encrypted_bytes,
encrypted_requests,
page_views,
requests,
threats
FROM cloudflare.zones.http_requests_1h_groups
WHERE zone_tag = '{{ zone_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
