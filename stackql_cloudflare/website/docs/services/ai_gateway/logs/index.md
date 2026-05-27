--- 
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
  - ai_gateway
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

Creates, updates, deletes, gets or lists a <code>logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="logs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai_gateway.logs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns the log details

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cached" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cost" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_cost" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_content_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_head" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_head_complete" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="response_content_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="response_head" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="response_head_complete" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="response_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status_code" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="step" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokens_in" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokens_out" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns a list of Gateway Logs

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cached" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cost" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_cost" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_content_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="request_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="response_content_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status_code" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="step" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokens_in" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokens_out" /></td>
    <td><code>integer</code></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves detailed information for a specific AI Gateway log entry.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a></td>
    <td><a href="#parameter-search"><code>search</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-order_by_direction"><code>order_by_direction</code></a>, <a href="#parameter-filters"><code>filters</code></a>, <a href="#parameter-meta_info"><code>meta_info</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-start_date"><code>start_date</code></a>, <a href="#parameter-end_date"><code>end_date</code></a>, <a href="#parameter-min_cost"><code>min_cost</code></a>, <a href="#parameter-max_cost"><code>max_cost</code></a>, <a href="#parameter-min_tokens_in"><code>min_tokens_in</code></a>, <a href="#parameter-max_tokens_in"><code>max_tokens_in</code></a>, <a href="#parameter-min_tokens_out"><code>min_tokens_out</code></a>, <a href="#parameter-max_tokens_out"><code>max_tokens_out</code></a>, <a href="#parameter-min_total_tokens"><code>min_total_tokens</code></a>, <a href="#parameter-max_total_tokens"><code>max_total_tokens</code></a>, <a href="#parameter-min_duration"><code>min_duration</code></a>, <a href="#parameter-max_duration"><code>max_duration</code></a>, <a href="#parameter-feedback"><code>feedback</code></a>, <a href="#parameter-success"><code>success</code></a>, <a href="#parameter-cached"><code>cached</code></a>, <a href="#parameter-model"><code>model</code></a>, <a href="#parameter-model_type"><code>model_type</code></a>, <a href="#parameter-provider"><code>provider</code></a>, <a href="#parameter-request_content_type"><code>request_content_type</code></a>, <a href="#parameter-response_content_type"><code>response_content_type</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates metadata for an AI Gateway log entry.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a></td>
    <td><a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-order_by_direction"><code>order_by_direction</code></a>, <a href="#parameter-filters"><code>filters</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list_logs_request"><CopyableCode code="list_logs_request" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves the original request payload for an AI Gateway log entry.</td>
</tr>
<tr>
    <td><a href="#list_logs_response"><CopyableCode code="list_logs_response" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves the response payload for an AI Gateway log entry.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account ID.</td>
</tr>
<tr id="parameter-gateway_id">
    <td><CopyableCode code="gateway_id" /></td>
    <td><code>string</code></td>
    <td>The AI Gateway ID.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr id="parameter-cached">
    <td><CopyableCode code="cached" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-end_date">
    <td><CopyableCode code="end_date" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-feedback">
    <td><CopyableCode code="feedback" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-filters">
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-max_cost">
    <td><CopyableCode code="max_cost" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-max_duration">
    <td><CopyableCode code="max_duration" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-max_tokens_in">
    <td><CopyableCode code="max_tokens_in" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-max_tokens_out">
    <td><CopyableCode code="max_tokens_out" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-max_total_tokens">
    <td><CopyableCode code="max_total_tokens" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-meta_info">
    <td><CopyableCode code="meta_info" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-min_cost">
    <td><CopyableCode code="min_cost" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-min_duration">
    <td><CopyableCode code="min_duration" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-min_tokens_in">
    <td><CopyableCode code="min_tokens_in" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-min_tokens_out">
    <td><CopyableCode code="min_tokens_out" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-min_total_tokens">
    <td><CopyableCode code="min_total_tokens" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-model">
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-model_type">
    <td><CopyableCode code="model_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order_by_direction">
    <td><CopyableCode code="order_by_direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-provider">
    <td><CopyableCode code="provider" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-request_content_type">
    <td><CopyableCode code="request_content_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-response_content_type">
    <td><CopyableCode code="response_content_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-start_date">
    <td><CopyableCode code="start_date" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-success">
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves detailed information for a specific AI Gateway log entry.

```sql
SELECT
id,
cached,
cost,
created_at,
custom_cost,
duration,
metadata,
model,
model_type,
path,
provider,
request_content_type,
request_head,
request_head_complete,
request_size,
request_type,
response_content_type,
response_head,
response_head_complete,
response_size,
status_code,
step,
success,
tokens_in,
tokens_out
FROM cloudflare.ai_gateway.logs
WHERE id = '{{ id }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of Gateway Logs

```sql
SELECT
id,
cached,
cost,
created_at,
custom_cost,
duration,
metadata,
model,
model_type,
path,
provider,
request_content_type,
request_type,
response_content_type,
status_code,
step,
success,
tokens_in,
tokens_out
FROM cloudflare.ai_gateway.logs
WHERE account_id = '{{ account_id }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
AND search = '{{ search }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order_by = '{{ order_by }}'
AND order_by_direction = '{{ order_by_direction }}'
AND filters = '{{ filters }}'
AND meta_info = '{{ meta_info }}'
AND direction = '{{ direction }}'
AND start_date = '{{ start_date }}'
AND end_date = '{{ end_date }}'
AND min_cost = '{{ min_cost }}'
AND max_cost = '{{ max_cost }}'
AND min_tokens_in = '{{ min_tokens_in }}'
AND max_tokens_in = '{{ max_tokens_in }}'
AND min_tokens_out = '{{ min_tokens_out }}'
AND max_tokens_out = '{{ max_tokens_out }}'
AND min_total_tokens = '{{ min_total_tokens }}'
AND max_total_tokens = '{{ max_total_tokens }}'
AND min_duration = '{{ min_duration }}'
AND max_duration = '{{ max_duration }}'
AND feedback = '{{ feedback }}'
AND success = '{{ success }}'
AND cached = '{{ cached }}'
AND model = '{{ model }}'
AND model_type = '{{ model_type }}'
AND provider = '{{ provider }}'
AND request_content_type = '{{ request_content_type }}'
AND response_content_type = '{{ response_content_type }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Updates metadata for an AI Gateway log entry.

```sql
UPDATE cloudflare.ai_gateway.logs
SET 
feedback = {{ feedback }},
metadata = '{{ metadata }}',
score = {{ score }}
WHERE 
id = '{{ id }}' --required
AND gateway_id = '{{ gateway_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

No description available.

```sql
DELETE FROM cloudflare.ai_gateway.logs
WHERE account_id = '{{ account_id }}' --required
AND gateway_id = '{{ gateway_id }}' --required
AND order_by = '{{ order_by }}'
AND order_by_direction = '{{ order_by_direction }}'
AND filters = '{{ filters }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_logs_request"
    values={[
        { label: 'list_logs_request', value: 'list_logs_request' },
        { label: 'list_logs_response', value: 'list_logs_response' }
    ]}
>
<TabItem value="list_logs_request">

Retrieves the original request payload for an AI Gateway log entry.

```sql
EXEC cloudflare.ai_gateway.logs.list_logs_request 
@id='{{ id }}' --required, 
@gateway_id='{{ gateway_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="list_logs_response">

Retrieves the response payload for an AI Gateway log entry.

```sql
EXEC cloudflare.ai_gateway.logs.list_logs_response 
@id='{{ id }}' --required, 
@gateway_id='{{ gateway_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
