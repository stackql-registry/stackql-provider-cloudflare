--- 
title: lifecycle
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle
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

Creates, updates, deletes, gets or lists a <code>lifecycle</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.lifecycle" /></td></tr>
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

Success Response.

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
    <td>Unique identifier for this rule. (example: Expire all objects older than 24 hours)</td>
</tr>
<tr>
    <td><CopyableCode code="abortMultipartUploadsTransition" /></td>
    <td><code>object</code></td>
    <td>Transition to abort ongoing multipart uploads.</td>
</tr>
<tr>
    <td><CopyableCode code="conditions" /></td>
    <td><code>object</code></td>
    <td>Conditions that apply to all transitions of this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="deleteObjectsTransition" /></td>
    <td><code>object</code></td>
    <td>Transition to delete objects.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this rule is in effect.</td>
</tr>
<tr>
    <td><CopyableCode code="storageClassTransitions" /></td>
    <td><code>array</code></td>
    <td>Transitions to change the storage class of objects.</td>
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
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Get object lifecycle rules for a bucket.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Set the object lifecycle rules for a bucket.</td>
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
<tr id="parameter-cf-r2-jurisdiction">
    <td><CopyableCode code="cf-r2-jurisdiction" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get object lifecycle rules for a bucket.

```sql
SELECT
id,
abortMultipartUploadsTransition,
conditions,
deleteObjectsTransition,
enabled,
storageClassTransitions
FROM cloudflare.r2.lifecycle
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

Set the object lifecycle rules for a bucket.

```sql
REPLACE cloudflare.r2.lifecycle
SET 
rules = '{{ rules }}'
WHERE 
bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
