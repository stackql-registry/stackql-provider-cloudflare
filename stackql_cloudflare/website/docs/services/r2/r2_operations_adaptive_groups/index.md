--- 
title: r2_operations_adaptive_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - r2_operations_adaptive_groups
  - r2
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


Creates, updates, deletes, gets or lists a <code>r2_operations_adaptive_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="r2_operations_adaptive_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.r2_operations_adaptive_groups" /></td></tr>
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
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>R2 bucket name.</td>
</tr>
<tr>
    <td><CopyableCode code="action_status" /></td>
    <td><code>string</code></td>
    <td>Operation result (success / failure / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="action_type" /></td>
    <td><code>string</code></td>
    <td>R2 operation (GetObject / PutObject / ListObjects / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="eyeball_region" /></td>
    <td><code>string</code></td>
    <td>Region of the requesting eyeball (WNAM / ENAM / WEU / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>integer</code></td>
    <td>Request count for the tuple.</td>
</tr>
<tr>
    <td><CopyableCode code="response_bytes" /></td>
    <td><code>integer</code></td>
    <td>Total retrieved bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="response_object_size" /></td>
    <td><code>integer</code></td>
    <td>Total response object sizes.</td>
</tr>
<tr>
    <td><CopyableCode code="response_status_code" /></td>
    <td><code>integer</code></td>
    <td>HTTP status returned.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_class" /></td>
    <td><code>string</code></td>
    <td>Storage class (Standard / InfrequentAccess).</td>
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
    <td>Cloudflare R2 storage operation analytics for an account, grouped by bucket, operation type, region, and HTTP status. Per-tuple totals for request count, response bytes, and object size.</td>
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

Cloudflare R2 storage operation analytics for an account, grouped by bucket, operation type, region, and HTTP status. Per-tuple totals for request count, response bytes, and object size.

```sql
SELECT
bucket_name,
action_status,
action_type,
datetime,
eyeball_region,
requests,
response_bytes,
response_object_size,
response_status_code,
storage_class
FROM cloudflare.r2.r2_operations_adaptive_groups
WHERE account_tag = '{{ account_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
