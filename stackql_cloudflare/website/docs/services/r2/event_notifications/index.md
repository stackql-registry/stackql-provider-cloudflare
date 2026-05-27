--- 
title: event_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - event_notifications
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

Creates, updates, deletes, gets or lists an <code>event_notifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="event_notifications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.event_notifications" /></td></tr>
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

Read Configuration response.

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
    <td><CopyableCode code="queueId" /></td>
    <td><code>string</code></td>
    <td>Queue ID. (example: 11111aa1-11aa-111a-a1a1-a1a111a11a11)</td>
</tr>
<tr>
    <td><CopyableCode code="queueName" /></td>
    <td><code>string</code></td>
    <td>Name of the queue. (example: first-queue)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Read Configuration response.

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
    <td><CopyableCode code="bucketName" /></td>
    <td><code>string</code></td>
    <td>Name of the bucket.</td>
</tr>
<tr>
    <td><CopyableCode code="queues" /></td>
    <td><code>array</code></td>
    <td>List of queues associated with the bucket.</td>
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
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Get a single event notification rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>List all event notification rules for a bucket.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-rules"><code>rules</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Create event notification rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-queue_id"><code>queue_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Delete an event notification rule. **If no body is provided, all rules for specified queue will be deleted**.</td>
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
<tr id="parameter-bucket_name">
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>The R2 bucket name.</td>
</tr>
<tr id="parameter-queue_id">
    <td><CopyableCode code="queue_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare Queue ID.</td>
</tr>
<tr id="parameter-cf-r2-jurisdiction">
    <td><CopyableCode code="cf-r2-jurisdiction" /></td>
    <td><code>string</code></td>
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

Get a single event notification rule.

```sql
SELECT
queueId,
queueName,
rules
FROM cloudflare.r2.event_notifications
WHERE queue_id = '{{ queue_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND account_id = '{{ account_id }}' -- required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
<TabItem value="list">

List all event notification rules for a bucket.

```sql
SELECT
bucketName,
queues
FROM cloudflare.r2.event_notifications
WHERE bucket_name = '{{ bucket_name }}' -- required
AND account_id = '{{ account_id }}' -- required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
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

Create event notification rule.

```sql
REPLACE cloudflare.r2.event_notifications
SET 
rules = '{{ rules }}'
WHERE 
queue_id = '{{ queue_id }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND rules = '{{ rules }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction}}'
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

Delete an event notification rule. **If no body is provided, all rules for specified queue will be deleted**.

```sql
DELETE FROM cloudflare.r2.event_notifications
WHERE queue_id = '{{ queue_id }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
</Tabs>
