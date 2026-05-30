--- 
title: cdn_network_analytics_adaptive_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - cdn_network_analytics_adaptive_groups
  - cache
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


Creates, updates, deletes, gets or lists a <code>cdn_network_analytics_adaptive_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cdn_network_analytics_adaptive_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cache.cdn_network_analytics_adaptive_groups" /></td></tr>
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
    <td><CopyableCode code="ip_protocol_name" /></td>
    <td><code>string</code></td>
    <td>Name of the L4 protocol (TCP / UDP / ICMP / GRE / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="bits" /></td>
    <td><code>integer</code></td>
    <td>Sum of bits received.</td>
</tr>
<tr>
    <td><CopyableCode code="colo_code" /></td>
    <td><code>string</code></td>
    <td>IATA code of the receiving Cloudflare datacenter.</td>
</tr>
<tr>
    <td><CopyableCode code="colo_country" /></td>
    <td><code>string</code></td>
    <td>Country of the receiving datacenter.</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="destination_country" /></td>
    <td><code>string</code></td>
    <td>Country of the destination IP.</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Packet direction relative to the customer network.</td>
</tr>
<tr>
    <td><CopyableCode code="packets" /></td>
    <td><code>integer</code></td>
    <td>Sum of packets received.</td>
</tr>
<tr>
    <td><CopyableCode code="source_country" /></td>
    <td><code>string</code></td>
    <td>Country of the source IP.</td>
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
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-until"><code>until</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a></td>
    <td>Cloudflare CDN edge network-layer analytics for an account, grouped by colo, source/destination country, packet direction, and IP protocol. Per-tuple totals for bits and packets received at the edge.</td>
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
<tr id="parameter-account_tag">
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>Cloudflare account ID (the 32-char hex tag).</td>
</tr>
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

Cloudflare CDN edge network-layer analytics for an account, grouped by colo, source/destination country, packet direction, and IP protocol. Per-tuple totals for bits and packets received at the edge.

```sql
SELECT
ip_protocol_name,
bits,
colo_code,
colo_country,
datetime,
destination_country,
direction,
packets,
source_country
FROM cloudflare.cache.cdn_network_analytics_adaptive_groups
WHERE account_tag = '{{ account_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
