--- 
title: workers_invocations
hide_title: false
hide_table_of_contents: false
keywords:
  - workers_invocations
  - workers
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


Creates, updates, deletes, gets or lists a <code>workers_invocations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workers_invocations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.workers_invocations" /></td></tr>
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
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>Worker script name.</td>
</tr>
<tr>
    <td><CopyableCode code="colo_code" /></td>
    <td><code>string</code></td>
    <td>IATA airport code of the serving colo.</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_us" /></td>
    <td><code>integer</code></td>
    <td>Total CPU time in microseconds.</td>
</tr>
<tr>
    <td><CopyableCode code="datetime" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="duration_gb_s" /></td>
    <td><code>integer</code></td>
    <td>Billable duration (GB*s units).</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>integer</code></td>
    <td>Errored invocations.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>integer</code></td>
    <td>Invocation count.</td>
</tr>
<tr>
    <td><CopyableCode code="response_body_size" /></td>
    <td><code>integer</code></td>
    <td>Total response body bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Invocation status (success / clientDisconnected / scriptError / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="subrequests" /></td>
    <td><code>integer</code></td>
    <td>Subrequest count.</td>
</tr>
<tr>
    <td><CopyableCode code="usage_model" /></td>
    <td><code>string</code></td>
    <td>Usage model (bundled / unbound / etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="wall_time_us" /></td>
    <td><code>integer</code></td>
    <td>Total wall time in microseconds.</td>
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
    <td>Cloudflare Workers invocation analytics for an account, grouped by script, status, and serving colo. Per-tuple totals for requests, errors, CPU time, duration (GB-s), subrequests, and response bytes.</td>
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

Cloudflare Workers invocation analytics for an account, grouped by script, status, and serving colo. Per-tuple totals for requests, errors, CPU time, duration (GB-s), subrequests, and response bytes.

```sql
SELECT
script_name,
colo_code,
cpu_time_us,
datetime,
duration_gb_s,
errors,
requests,
response_body_size,
status,
subrequests,
usage_model,
wall_time_us
FROM cloudflare.workers.workers_invocations
WHERE account_tag = '{{ account_tag }}' -- required
AND since = '{{ since }}' -- required
AND until = '{{ until }}' -- required
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
