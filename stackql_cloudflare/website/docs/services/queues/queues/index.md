--- 
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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

Creates, updates, deletes, gets or lists a <code>queues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queues" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.queues.queues" /></td></tr>
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

Details of the requested Queue

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
    <td><CopyableCode code="queue_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="queue_name" /></td>
    <td><code>string</code></td>
    <td> (example: example-queue)</td>
</tr>
<tr>
    <td><CopyableCode code="consumers" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="consumers_total_count" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="producers" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="producers_total_count" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of all Queues that belong to this account

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
    <td><CopyableCode code="queue_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="queue_name" /></td>
    <td><code>string</code></td>
    <td> (example: example-queue)</td>
</tr>
<tr>
    <td><CopyableCode code="consumers" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="consumers_total_count" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="producers" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="producers_total_count" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
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
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get details about a specific queue.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns the queues owned by an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-queue_name"><code>queue_name</code></a></td>
    <td></td>
    <td>Create a new queue</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates a Queue.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates a Queue. Note that this endpoint does not support partial updates. If successful, the Queue's configuration is overwritten with the supplied configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a queue</td>
</tr>
<tr>
    <td><a href="#create_messages"><CopyableCode code="create_messages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Push a message to a Queue</td>
</tr>
<tr>
    <td><a href="#batch"><CopyableCode code="batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Push a batch of message to a Queue</td>
</tr>
<tr>
    <td><a href="#preview"><CopyableCode code="preview" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Preview messages from a Queue without leasing them. Messages remain available for subsequent preview or pull operations.</td>
</tr>
<tr>
    <td><a href="#pull"><CopyableCode code="pull" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Pull a batch of messages from a Queue</td>
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

Get details about a specific queue.

```sql
SELECT
queue_id,
queue_name,
consumers,
consumers_total_count,
created_on,
modified_on,
producers,
producers_total_count,
settings
FROM cloudflare.queues.queues
WHERE queue_id = '{{ queue_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns the queues owned by an account.

```sql
SELECT
queue_id,
queue_name,
consumers,
consumers_total_count,
created_on,
modified_on,
producers,
producers_total_count,
settings
FROM cloudflare.queues.queues
WHERE account_id = '{{ account_id }}' -- required
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

Create a new queue

```sql
INSERT INTO cloudflare.queues.queues (
queue_name,
account_id
)
SELECT 
'{{ queue_name }}' /* required */,
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
- name: queues
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the queues resource.
    - name: queue_name
      value: "{{ queue_name }}"
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

Updates a Queue.

```sql
UPDATE cloudflare.queues.queues
SET 
queue_name = '{{ queue_name }}',
settings = '{{ settings }}'
WHERE 
queue_id = '{{ queue_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Updates a Queue. Note that this endpoint does not support partial updates. If successful, the Queue's configuration is overwritten with the supplied configuration.

```sql
REPLACE cloudflare.queues.queues
SET 
queue_name = '{{ queue_name }}',
settings = '{{ settings }}'
WHERE 
queue_id = '{{ queue_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Deletes a queue

```sql
DELETE FROM cloudflare.queues.queues
WHERE queue_id = '{{ queue_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_messages"
    values={[
        { label: 'create_messages', value: 'create_messages' },
        { label: 'batch', value: 'batch' },
        { label: 'preview', value: 'preview' },
        { label: 'pull', value: 'pull' }
    ]}
>
<TabItem value="create_messages">

Push a message to a Queue

```sql
EXEC cloudflare.queues.queues.create_messages 
@queue_id='{{ queue_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"delay_seconds": {{ delay_seconds }}, 
"body": "{{ body }}", 
"content_type": "{{ content_type }}"
}'
;
```
</TabItem>
<TabItem value="batch">

Push a batch of message to a Queue

```sql
EXEC cloudflare.queues.queues.batch 
@queue_id='{{ queue_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"delay_seconds": {{ delay_seconds }}, 
"messages": "{{ messages }}"
}'
;
```
</TabItem>
<TabItem value="preview">

Preview messages from a Queue without leasing them. Messages remain available for subsequent preview or pull operations.

```sql
EXEC cloudflare.queues.queues.preview 
@queue_id='{{ queue_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"batch_size": {{ batch_size }}
}'
;
```
</TabItem>
<TabItem value="pull">

Pull a batch of messages from a Queue

```sql
EXEC cloudflare.queues.queues.pull 
@queue_id='{{ queue_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"batch_size": {{ batch_size }}, 
"visibility_timeout_ms": {{ visibility_timeout_ms }}
}'
;
```
</TabItem>
</Tabs>
