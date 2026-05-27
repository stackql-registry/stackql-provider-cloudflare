--- 
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
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

Creates, updates, deletes, gets or lists a <code>permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.permissions" /></td></tr>
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

Returns the list of permissions.

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
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource ID this permission applies to account_id or group_id</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td> (dataset)</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td> (read, write)</td>
</tr>
<tr>
    <td><CopyableCode code="subjectId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="subjectType" /></td>
    <td><code>string</code></td>
    <td> (account, group)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td>List permissions</td>
</tr>
<tr>
    <td><a href="#post_permission_create"><CopyableCode code="post_permission_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-subjectType"><code>subjectType</code></a>, <a href="#parameter-subjectId"><code>subjectId</code></a>, <a href="#parameter-role"><code>role</code></a></td>
    <td></td>
    <td>Create a permission</td>
</tr>
<tr>
    <td><a href="#put_permission_update"><CopyableCode code="put_permission_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-grant_id"><code>grant_id</code></a>, <a href="#parameter-role"><code>role</code></a></td>
    <td></td>
    <td>Update a permission</td>
</tr>
<tr>
    <td><a href="#delete_permission_delete"><CopyableCode code="delete_permission_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-grant_id"><code>grant_id</code></a></td>
    <td></td>
    <td>Delete a permission</td>
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
<tr id="parameter-dataset_id">
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>The dataset ID.</td>
</tr>
<tr id="parameter-grant_id">
    <td><CopyableCode code="grant_id" /></td>
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

List permissions

```sql
SELECT
createdAt,
resourceId,
resourceType,
role,
subjectId,
subjectType,
updatedAt,
uuid
FROM cloudflare.cloudforce_one.permissions
WHERE account_id = '{{ account_id }}' -- required
AND dataset_id = '{{ dataset_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_permission_create"
    values={[
        { label: 'post_permission_create', value: 'post_permission_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_permission_create">

Create a permission

```sql
INSERT INTO cloudflare.cloudforce_one.permissions (
role,
subjectId,
subjectType,
account_id,
dataset_id
)
SELECT 
'{{ role }}' /* required */,
'{{ subjectId }}' /* required */,
'{{ subjectType }}' /* required */,
'{{ account_id }}',
'{{ dataset_id }}'
RETURNING
createdAt,
resourceId,
resourceType,
role,
subjectId,
subjectType,
updatedAt,
uuid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: permissions
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the permissions resource.
    - name: dataset_id
      value: "{{ dataset_id }}"
      description: Required parameter for the permissions resource.
    - name: role
      value: "{{ role }}"
      valid_values: ['read', 'write']
    - name: subjectId
      value: "{{ subjectId }}"
    - name: subjectType
      value: "{{ subjectType }}"
      valid_values: ['account', 'group']
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_permission_update"
    values={[
        { label: 'put_permission_update', value: 'put_permission_update' }
    ]}
>
<TabItem value="put_permission_update">

Update a permission

```sql
REPLACE cloudflare.cloudforce_one.permissions
SET 
role = '{{ role }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
AND grant_id = '{{ grant_id }}' --required
AND role = '{{ role }}' --required
RETURNING
message,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_permission_delete"
    values={[
        { label: 'delete_permission_delete', value: 'delete_permission_delete' }
    ]}
>
<TabItem value="delete_permission_delete">

Delete a permission

```sql
DELETE FROM cloudflare.cloudforce_one.permissions
WHERE account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
AND grant_id = '{{ grant_id }}' --required
;
```
</TabItem>
</Tabs>
