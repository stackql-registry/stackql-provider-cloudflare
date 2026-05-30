--- 
title: workers
hide_title: false
hide_table_of_contents: false
keywords:
  - workers
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

Creates, updates, deletes, gets or lists a <code>workers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.workers" /></td></tr>
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

Get Worker success.

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
    <td>Immutable ID of the Worker. (example: e8f70fdbc8b1fb0b8ddb1af166186758)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the Worker. (example: my-worker)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Worker was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deployed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Worker's most recent deployment was created. `null` if the Worker has never been deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="logpush" /></td>
    <td><code>boolean</code></td>
    <td>Whether logpush is enabled for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="observability" /></td>
    <td><code>object</code></td>
    <td>Observability settings for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="references" /></td>
    <td><code>object</code></td>
    <td>Other resources that reference the Worker and depend on it existing.</td>
</tr>
<tr>
    <td><CopyableCode code="subdomain" /></td>
    <td><code>object</code></td>
    <td>Subdomain settings for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Tags associated with the Worker. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="tail_consumers" /></td>
    <td><code>array</code></td>
    <td>Other Workers that should consume logs from the Worker. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Worker was most recently updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Workers success.

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
    <td>Immutable ID of the Worker. (example: e8f70fdbc8b1fb0b8ddb1af166186758)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the Worker. (example: my-worker)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Worker was created.</td>
</tr>
<tr>
    <td><CopyableCode code="deployed_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Worker's most recent deployment was created. `null` if the Worker has never been deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="logpush" /></td>
    <td><code>boolean</code></td>
    <td>Whether logpush is enabled for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="observability" /></td>
    <td><code>object</code></td>
    <td>Observability settings for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="references" /></td>
    <td><code>object</code></td>
    <td>Other resources that reference the Worker and depend on it existing.</td>
</tr>
<tr>
    <td><CopyableCode code="subdomain" /></td>
    <td><code>object</code></td>
    <td>Subdomain settings for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Tags associated with the Worker. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="tail_consumers" /></td>
    <td><code>array</code></td>
    <td>Other Workers that should consume logs from the Worker. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Worker was most recently updated.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a></td>
    <td></td>
    <td>Get details about a specific Worker.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>List all Workers for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-subdomain"><code>subdomain</code></a>, <a href="#parameter-observability"><code>observability</code></a>, <a href="#parameter-logpush"><code>logpush</code></a>, <a href="#parameter-tail_consumers"><code>tail_consumers</code></a></td>
    <td></td>
    <td>Create a new Worker.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-subdomain"><code>subdomain</code></a>, <a href="#parameter-observability"><code>observability</code></a>, <a href="#parameter-logpush"><code>logpush</code></a>, <a href="#parameter-tail_consumers"><code>tail_consumers</code></a></td>
    <td></td>
    <td>Perform a partial update on a Worker, where omitted properties are left unchanged from their current values.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-subdomain"><code>subdomain</code></a>, <a href="#parameter-observability"><code>observability</code></a>, <a href="#parameter-logpush"><code>logpush</code></a>, <a href="#parameter-tail_consumers"><code>tail_consumers</code></a></td>
    <td></td>
    <td>Perform a complete replacement of a Worker, where omitted properties are set to their default values. This is the exact same as the Create Worker endpoint, but operates on an existing Worker. To perform a partial update instead, use the Edit Worker endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a></td>
    <td></td>
    <td>Delete a Worker and all its associated resources (versions, deployments, etc.).</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-base64"><code>base64</code></a></td>
    <td>Upload assets ahead of creating a Worker version. To learn more about the direct uploads of assets, see https://developers.cloudflare.com/workers/static-assets/direct-upload/.</td>
</tr>
<tr>
    <td><a href="#create_keys"><CopyableCode code="create_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all the keys in your telemetry events.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-queryId"><code>queryId</code></a>, <a href="#parameter-timeframe"><code>timeframe</code></a></td>
    <td></td>
    <td>Run a temporary or saved query.</td>
</tr>
<tr>
    <td><a href="#create_values"><CopyableCode code="create_values" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-timeframe"><code>timeframe</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-datasets"><code>datasets</code></a></td>
    <td></td>
    <td>List unique values found in your events.</td>
</tr>
<tr>
    <td><a href="#delete_versions"><CopyableCode code="delete_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a></td>
    <td></td>
    <td>Delete a version.</td>
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
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-worker_id">
    <td><CopyableCode code="worker_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-base64">
    <td><CopyableCode code="base64" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort direction.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>Property to sort results by.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Current page.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Items per-page.</td>
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

Get details about a specific Worker.

```sql
SELECT
id,
name,
created_on,
deployed_on,
logpush,
observability,
references,
subdomain,
tags,
tail_consumers,
updated_on
FROM cloudflare.workers.workers
WHERE account_id = '{{ account_id }}' -- required
AND worker_id = '{{ worker_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Workers for an account.

```sql
SELECT
id,
name,
created_on,
deployed_on,
logpush,
observability,
references,
subdomain,
tags,
tail_consumers,
updated_on
FROM cloudflare.workers.workers
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order_by = '{{ order_by }}'
AND order = '{{ order }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new Worker.

```sql
INSERT INTO cloudflare.workers.workers (
logpush,
name,
observability,
subdomain,
tags,
tail_consumers,
account_id
)
SELECT 
{{ logpush }} /* required */,
'{{ name }}' /* required */,
'{{ observability }}' /* required */,
'{{ subdomain }}' /* required */,
'{{ tags }}' /* required */,
'{{ tail_consumers }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workers
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the workers resource.
    - name: logpush
      value: {{ logpush }}
      description: |
        Whether logpush is enabled for the Worker.
      default: false
    - name: name
      value: "{{ name }}"
      description: |
        Name of the Worker.
    - name: observability
      description: |
        Observability settings for the Worker.
      value:
        enabled: {{ enabled }}
        head_sampling_rate: {{ head_sampling_rate }}
        logs:
          destinations:
            - "{{ destinations }}"
          enabled: {{ enabled }}
          head_sampling_rate: {{ head_sampling_rate }}
          invocation_logs: {{ invocation_logs }}
          persist: {{ persist }}
        traces:
          destinations:
            - "{{ destinations }}"
          enabled: {{ enabled }}
          head_sampling_rate: {{ head_sampling_rate }}
          persist: {{ persist }}
    - name: subdomain
      description: |
        Subdomain settings for the Worker.
      value:
        enabled: {{ enabled }}
        previews_enabled: {{ previews_enabled }}
    - name: tags
      value:
        - "{{ tags }}"
      description: |
        Tags associated with the Worker.
      default: 
    - name: tail_consumers
      description: |
        Other Workers that should consume logs from the Worker.
      value:
        - name: "{{ name }}"
      default: 
`}</CodeBlock>

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

Perform a partial update on a Worker, where omitted properties are left unchanged from their current values.

```sql
UPDATE cloudflare.workers.workers
SET 
logpush = {{ logpush }},
name = '{{ name }}',
observability = '{{ observability }}',
subdomain = '{{ subdomain }}',
tags = '{{ tags }}',
tail_consumers = '{{ tail_consumers }}'
WHERE 
account_id = '{{ account_id }}' --required
AND worker_id = '{{ worker_id }}' --required
AND name = '{{ name }}' --required
AND tags = '{{ tags }}' --required
AND subdomain = '{{ subdomain }}' --required
AND observability = '{{ observability }}' --required
AND logpush = {{ logpush }} --required
AND tail_consumers = '{{ tail_consumers }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Perform a complete replacement of a Worker, where omitted properties are set to their default values. This is the exact same as the Create Worker endpoint, but operates on an existing Worker. To perform a partial update instead, use the Edit Worker endpoint.

```sql
REPLACE cloudflare.workers.workers
SET 
logpush = {{ logpush }},
name = '{{ name }}',
observability = '{{ observability }}',
subdomain = '{{ subdomain }}',
tags = '{{ tags }}',
tail_consumers = '{{ tail_consumers }}'
WHERE 
account_id = '{{ account_id }}' --required
AND worker_id = '{{ worker_id }}' --required
AND name = '{{ name }}' --required
AND tags = '{{ tags }}' --required
AND subdomain = '{{ subdomain }}' --required
AND observability = '{{ observability }}' --required
AND logpush = {{ logpush }} --required
AND tail_consumers = '{{ tail_consumers }}' --required
RETURNING
errors,
messages,
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

Delete a Worker and all its associated resources (versions, deployments, etc.).

```sql
DELETE FROM cloudflare.workers.workers
WHERE account_id = '{{ account_id }}' --required
AND worker_id = '{{ worker_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upload"
    values={[
        { label: 'upload', value: 'upload' },
        { label: 'create_keys', value: 'create_keys' },
        { label: 'query', value: 'query' },
        { label: 'create_values', value: 'create_values' },
        { label: 'delete_versions', value: 'delete_versions' }
    ]}
>
<TabItem value="upload">

Upload assets ahead of creating a Worker version. To learn more about the direct uploads of assets, see https://developers.cloudflare.com/workers/static-assets/direct-upload/.

```sql
EXEC cloudflare.workers.workers.upload 
@account_id='{{ account_id }}' --required, 
@base64={{ base64 }}
;
```
</TabItem>
<TabItem value="create_keys">

List all the keys in your telemetry events.

```sql
EXEC cloudflare.workers.workers.create_keys 
@account_id='{{ account_id }}' --required 
@@json=
'{
"datasets": "{{ datasets }}", 
"filters": "{{ filters }}", 
"from": {{ from }}, 
"keyNeedle": "{{ keyNeedle }}", 
"limit": {{ limit }}, 
"needle": "{{ needle }}", 
"to": {{ to }}
}'
;
```
</TabItem>
<TabItem value="query">

Run a temporary or saved query.

```sql
EXEC cloudflare.workers.workers.query 
@account_id='{{ account_id }}' --required 
@@json=
'{
"chart": {{ chart }}, 
"compare": {{ compare }}, 
"dry": {{ dry }}, 
"granularity": {{ granularity }}, 
"ignoreSeries": {{ ignoreSeries }}, 
"limit": {{ limit }}, 
"offset": "{{ offset }}", 
"offsetBy": {{ offsetBy }}, 
"offsetDirection": "{{ offsetDirection }}", 
"parameters": "{{ parameters }}", 
"queryId": "{{ queryId }}", 
"timeframe": "{{ timeframe }}", 
"view": "{{ view }}"
}'
;
```
</TabItem>
<TabItem value="create_values">

List unique values found in your events.

```sql
EXEC cloudflare.workers.workers.create_values 
@account_id='{{ account_id }}' --required 
@@json=
'{
"datasets": "{{ datasets }}", 
"filters": "{{ filters }}", 
"key": "{{ key }}", 
"limit": {{ limit }}, 
"needle": "{{ needle }}", 
"timeframe": "{{ timeframe }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
<TabItem value="delete_versions">

Delete a version.

```sql
EXEC cloudflare.workers.workers.delete_versions 
@account_id='{{ account_id }}' --required, 
@worker_id='{{ worker_id }}' --required, 
@version_id='{{ version_id }}' --required
;
```
</TabItem>
</Tabs>
