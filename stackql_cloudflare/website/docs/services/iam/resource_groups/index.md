--- 
title: resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_groups
  - iam
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

Creates, updates, deletes, gets or lists a <code>resource_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.iam.resource_groups" /></td></tr>
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

Resource Group Details response

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
    <td>Identifier of the resource group. (example: 6d7f2f5f5b1d4a0e9081fdc98d432fd1)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. (example: com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4)</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Attributes associated to the resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>array</code></td>
    <td>The scope associated to the resource group</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Resource Groups response

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
    <td>Identifier of the resource group. (example: 6d7f2f5f5b1d4a0e9081fdc98d432fd1)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group. (example: com.cloudflare.api.account.eb78d65290b24279ba6f44721b3ea3c4)</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Attributes associated to the resource group.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>array</code></td>
    <td>The scope associated to the resource group</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-resource_group_id"><code>resource_group_id</code></a></td>
    <td></td>
    <td>Get information about a specific resource group in an account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td>List all the resource groups for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Create a new Resource Group under the specified account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-resource_group_id"><code>resource_group_id</code></a></td>
    <td></td>
    <td>Modify an existing resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-resource_group_id"><code>resource_group_id</code></a></td>
    <td></td>
    <td>Remove a resource group from an account.</td>
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
<tr id="parameter-resource_group_id">
    <td><CopyableCode code="resource_group_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
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

Get information about a specific resource group in an account.

```sql
SELECT
id,
name,
meta,
scope
FROM cloudflare.iam.resource_groups
WHERE account_id = '{{ account_id }}' -- required
AND resource_group_id = '{{ resource_group_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all the resource groups for an account.

```sql
SELECT
id,
name,
meta,
scope
FROM cloudflare.iam.resource_groups
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}'
AND name = '{{ name }}'
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

Create a new Resource Group under the specified account.

```sql
INSERT INTO cloudflare.iam.resource_groups (
name,
scope,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ scope }}' /* required */,
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
- name: resource_groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the resource_groups resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the resource group
    - name: scope
      description: |
        A scope is a combination of scope objects which provides additional context.
      value:
        key: "{{ key }}"
        objects:
          - key: "{{ key }}"
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

Modify an existing resource group.

```sql
REPLACE cloudflare.iam.resource_groups
SET 
name = '{{ name }}',
scope = '{{ scope }}'
WHERE 
account_id = '{{ account_id }}' --required
AND resource_group_id = '{{ resource_group_id }}' --required
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

Remove a resource group from an account.

```sql
DELETE FROM cloudflare.iam.resource_groups
WHERE account_id = '{{ account_id }}' --required
AND resource_group_id = '{{ resource_group_id }}' --required
;
```
</TabItem>
</Tabs>
