--- 
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - pipelines
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pipelines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pipelines.pipelines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>[DEPRECATED] Update an existing pipeline. Use the new /pipelines/v1/pipelines endpoint instead.</td>
</tr>
<tr>
    <td><a href="#delete_v1"><CopyableCode code="delete_v1" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pipeline_id"><code>pipeline_id</code></a></td>
    <td></td>
    <td>Delete Pipeline in Account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Delete a pipeline. Use the new /pipelines/v1/pipelines endpoint instead.</td>
</tr>
<tr>
    <td><a href="#validate_sql_v1"><CopyableCode code="validate_sql_v1" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sql"><code>sql</code></a></td>
    <td></td>
    <td>Validate Arroyo SQL.</td>
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
<tr id="parameter-pipeline_id">
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-pipeline_name">
    <td><CopyableCode code="pipeline_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

[DEPRECATED] Update an existing pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

```sql
REPLACE cloudflare.pipelines.pipelines
SET 
destination = '{{ destination }}',
name = '{{ name }}',
source = '{{ source }}'
WHERE 
account_id = '{{ account_id }}' --required
AND pipeline_name = '{{ pipeline_name }}' --required
AND name = '{{ name }}' --required
AND source = '{{ source }}' --required
AND destination = '{{ destination }}' --required
RETURNING
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_v1"
    values={[
        { label: 'delete_v1', value: 'delete_v1' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_v1">

Delete Pipeline in Account.

```sql
DELETE FROM cloudflare.pipelines.pipelines
WHERE account_id = '{{ account_id }}' --required
AND pipeline_id = '{{ pipeline_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

[DEPRECATED] Delete a pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

```sql
DELETE FROM cloudflare.pipelines.pipelines
WHERE account_id = '{{ account_id }}' --required
AND pipeline_name = '{{ pipeline_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_sql_v1"
    values={[
        { label: 'validate_sql_v1', value: 'validate_sql_v1' }
    ]}
>
<TabItem value="validate_sql_v1">

Validate Arroyo SQL.

```sql
EXEC cloudflare.pipelines.pipelines.validate_sql_v1 
@account_id='{{ account_id }}' --required 
@@json=
'{
"sql": "{{ sql }}"
}'
;
```
</TabItem>
</Tabs>
