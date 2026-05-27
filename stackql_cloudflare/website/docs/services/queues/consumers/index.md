--- 
title: consumers
hide_title: false
hide_table_of_contents: false
keywords:
  - consumers
  - queues
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

Creates, updates, deletes, gets or lists a <code>consumers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="consumers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.queues.consumers" /></td></tr>
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

Get Queue Consumer response.

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
    <td><CopyableCode code="consumer_id" /></td>
    <td><code>string</code></td>
    <td>A Resource identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="queue_name" /></td>
    <td><code>string</code></td>
    <td> (example: example-queue)</td>
</tr>
<tr>
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>Name of a Worker (example: my-consumer-worker)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dead_letter_queue" /></td>
    <td><code>string</code></td>
    <td>Name of the dead letter queue, or empty string if not configured</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (worker)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

All consumers attached to this Queue

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
    <td><CopyableCode code="consumer_id" /></td>
    <td><code>string</code></td>
    <td>A Resource identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="queue_name" /></td>
    <td><code>string</code></td>
    <td> (example: example-queue)</td>
</tr>
<tr>
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>Name of a Worker (example: my-consumer-worker)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dead_letter_queue" /></td>
    <td><code>string</code></td>
    <td>Name of the dead letter queue, or empty string if not configured</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (worker)</td>
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
    <td><a href="#parameter-consumer_id"><code>consumer_id</code></a>, <a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the consumer for a queue by consumer id</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns the consumers for a Queue</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Creates a new consumer for a Queue</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-consumer_id"><code>consumer_id</code></a>, <a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates the consumer for a queue, or creates one if it does not exist.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-consumer_id"><code>consumer_id</code></a>, <a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes the consumer for a queue.</td>
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
<tr id="parameter-consumer_id">
    <td><CopyableCode code="consumer_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-queue_id">
    <td><CopyableCode code="queue_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare Queue ID.</td>
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

Fetches the consumer for a queue by consumer id

```sql
SELECT
consumer_id,
queue_name,
script_name,
created_on,
dead_letter_queue,
settings,
type
FROM cloudflare.queues.consumers
WHERE consumer_id = '{{ consumer_id }}' -- required
AND queue_id = '{{ queue_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns the consumers for a Queue

```sql
SELECT
consumer_id,
queue_name,
script_name,
created_on,
dead_letter_queue,
settings,
type
FROM cloudflare.queues.consumers
WHERE queue_id = '{{ queue_id }}' -- required
AND account_id = '{{ account_id }}' -- required
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

Creates a new consumer for a Queue

```sql
INSERT INTO cloudflare.queues.consumers (
dead_letter_queue,
script_name,
settings,
type,
queue_id,
account_id
)
SELECT 
'{{ dead_letter_queue }}',
'{{ script_name }}',
'{{ settings }}',
'{{ type }}' /* required */,
'{{ queue_id }}',
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
- name: consumers
  props:
    - name: queue_id
      value: "{{ queue_id }}"
      description: Required parameter for the consumers resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the consumers resource.
    - name: dead_letter_queue
      value: "{{ dead_letter_queue }}"
    - name: script_name
      value: "{{ script_name }}"
      description: |
        Name of a Worker
    - name: settings
      value:
        batch_size: {{ batch_size }}
        max_concurrency: {{ max_concurrency }}
        max_retries: {{ max_retries }}
        max_wait_time_ms: {{ max_wait_time_ms }}
        retry_delay: {{ retry_delay }}
    - name: type
      value: "{{ type }}"
      valid_values: ['worker']
`}</CodeBlock>

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

Updates the consumer for a queue, or creates one if it does not exist.

```sql
REPLACE cloudflare.queues.consumers
SET 
dead_letter_queue = '{{ dead_letter_queue }}',
script_name = '{{ script_name }}',
settings = '{{ settings }}',
type = '{{ type }}'
WHERE 
consumer_id = '{{ consumer_id }}' --required
AND queue_id = '{{ queue_id }}' --required
AND account_id = '{{ account_id }}' --required
AND type = '{{ type }}' --required
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

Deletes the consumer for a queue.

```sql
DELETE FROM cloudflare.queues.consumers
WHERE consumer_id = '{{ consumer_id }}' --required
AND queue_id = '{{ queue_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
