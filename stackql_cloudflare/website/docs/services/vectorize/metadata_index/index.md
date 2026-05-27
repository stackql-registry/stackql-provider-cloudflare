--- 
title: metadata_index
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_index
  - vectorize
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

Creates, updates, deletes, gets or lists a <code>metadata_index</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="metadata_index" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.vectorize.metadata_index" /></td></tr>
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

List Metadata Index Response

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
    <td><CopyableCode code="indexType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of indexed metadata property. (string, number, boolean)</td>
</tr>
<tr>
    <td><CopyableCode code="propertyName" /></td>
    <td><code>string</code></td>
    <td>Specifies the indexed metadata property. (example: random_metadata_property)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>List Metadata Indexes for the specified Vectorize Index.</td>
</tr>
<tr>
    <td><a href="#create_v2"><CopyableCode code="create_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-propertyName"><code>propertyName</code></a>, <a href="#parameter-indexType"><code>indexType</code></a></td>
    <td></td>
    <td>Enable metadata filtering based on metadata property. Limited to 10 properties.</td>
</tr>
<tr>
    <td><a href="#create_delete_v2"><CopyableCode code="create_delete_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-propertyName"><code>propertyName</code></a></td>
    <td></td>
    <td>Allow Vectorize to delete the specified metadata index.</td>
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
<tr id="parameter-index_name">
    <td><CopyableCode code="index_name" /></td>
    <td><code>string</code></td>
    <td>The Vectorize index name.</td>
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

List Metadata Indexes for the specified Vectorize Index.

```sql
SELECT
indexType,
propertyName
FROM cloudflare.vectorize.metadata_index
WHERE account_id = '{{ account_id }}' -- required
AND index_name = '{{ index_name }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_v2"
    values={[
        { label: 'create_v2', value: 'create_v2' },
        { label: 'create_delete_v2', value: 'create_delete_v2' }
    ]}
>
<TabItem value="create_v2">

Enable metadata filtering based on metadata property. Limited to 10 properties.

```sql
EXEC cloudflare.vectorize.metadata_index.create_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"indexType": "{{ indexType }}", 
"propertyName": "{{ propertyName }}"
}'
;
```
</TabItem>
<TabItem value="create_delete_v2">

Allow Vectorize to delete the specified metadata index.

```sql
EXEC cloudflare.vectorize.metadata_index.create_delete_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"propertyName": "{{ propertyName }}"
}'
;
```
</TabItem>
</Tabs>
