--- 
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - cloudforce_one
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.groups" /></td></tr>
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

Return the group.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns the list of groups.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Read a group for an account</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List groups for an account</td>
</tr>
<tr>
    <td><a href="#post_group_create"><CopyableCode code="post_group_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-description"><code>description</code></a></td>
    <td></td>
    <td>Create a group</td>
</tr>
<tr>
    <td><a href="#put_group_update"><CopyableCode code="put_group_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-description"><code>description</code></a></td>
    <td></td>
    <td>Update a group</td>
</tr>
<tr>
    <td><a href="#delete_group_delete"><CopyableCode code="delete_group_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Delete a group for an account</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The Access group ID.</td>
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

Read a group for an account

```sql
SELECT
name,
createdAt,
description,
members,
updatedAt,
uuid
FROM cloudflare.cloudforce_one.groups
WHERE account_id = '{{ account_id }}' -- required
AND group_id = '{{ group_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List groups for an account

```sql
SELECT
name,
createdAt,
description,
updatedAt,
uuid
FROM cloudflare.cloudforce_one.groups
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_group_create"
    values={[
        { label: 'post_group_create', value: 'post_group_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_group_create">

Create a group

```sql
INSERT INTO cloudflare.cloudforce_one.groups (
description,
name,
account_id
)
SELECT 
'{{ description }}' /* required */,
'{{ name }}' /* required */,
'{{ account_id }}'
RETURNING
name,
createdAt,
description,
updatedAt,
uuid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the groups resource.
    - name: description
      value: "{{ description }}"
    - name: name
      value: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_group_update"
    values={[
        { label: 'put_group_update', value: 'put_group_update' }
    ]}
>
<TabItem value="put_group_update">

Update a group

```sql
REPLACE cloudflare.cloudforce_one.groups
SET 
description = '{{ description }}',
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
AND name = '{{ name }}' --required
AND description = '{{ description }}' --required
RETURNING
name,
createdAt,
description,
updatedAt,
uuid;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_group_delete"
    values={[
        { label: 'delete_group_delete', value: 'delete_group_delete' }
    ]}
>
<TabItem value="delete_group_delete">

Delete a group for an account

```sql
DELETE FROM cloudflare.cloudforce_one.groups
WHERE account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
;
```
</TabItem>
</Tabs>
