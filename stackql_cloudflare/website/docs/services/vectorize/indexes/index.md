--- 
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
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

Creates, updates, deletes, gets or lists an <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.vectorize.indexes" /></td></tr>
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
    <td><a href="#create_delete_by_ids"><CopyableCode code="create_delete_by_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>Delete a set of vectors from an index by their vector identifiers.</td>
</tr>
<tr>
    <td><a href="#get_by_ids"><CopyableCode code="get_by_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>Get a set of vectors from an index by their vector identifiers.</td>
</tr>
<tr>
    <td><a href="#create_insert"><CopyableCode code="create_insert" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>Inserts vectors into the specified index and returns the count of the vectors successfully inserted.</td>
</tr>
<tr>
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-vector"><code>vector</code></a></td>
    <td></td>
    <td>Finds vectors closest to a given vector in an index.</td>
</tr>
<tr>
    <td><a href="#upsert"><CopyableCode code="upsert" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>Upserts vectors into the specified index, creating them if they do not exist and returns the count of values and ids successfully inserted.</td>
</tr>
<tr>
    <td><a href="#create_delete_by_ids_v2"><CopyableCode code="create_delete_by_ids_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>Delete a set of vectors from an index by their vector identifiers.</td>
</tr>
<tr>
    <td><a href="#get_by_ids_v2"><CopyableCode code="get_by_ids_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td></td>
    <td>Get a set of vectors from an index by their vector identifiers.</td>
</tr>
<tr>
    <td><a href="#create_insert_v2"><CopyableCode code="create_insert_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td><a href="#parameter-unparsable-behavior"><code>unparsable-behavior</code></a></td>
    <td>Inserts vectors into the specified index and returns a mutation id corresponding to the vectors enqueued for insertion.</td>
</tr>
<tr>
    <td><a href="#query_v2"><CopyableCode code="query_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a>, <a href="#parameter-vector"><code>vector</code></a></td>
    <td></td>
    <td>Finds vectors closest to a given vector in an index.</td>
</tr>
<tr>
    <td><a href="#upsert_v2"><CopyableCode code="upsert_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-index_name"><code>index_name</code></a></td>
    <td><a href="#parameter-unparsable-behavior"><code>unparsable-behavior</code></a></td>
    <td>Upserts vectors into the specified index, creating them if they do not exist and returns a mutation id corresponding to the vectors enqueued for upsertion.</td>
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
<tr id="parameter-unparsable-behavior">
    <td><CopyableCode code="unparsable-behavior" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="create_delete_by_ids"
    values={[
        { label: 'create_delete_by_ids', value: 'create_delete_by_ids' },
        { label: 'get_by_ids', value: 'get_by_ids' },
        { label: 'create_insert', value: 'create_insert' },
        { label: 'query', value: 'query' },
        { label: 'upsert', value: 'upsert' },
        { label: 'create_delete_by_ids_v2', value: 'create_delete_by_ids_v2' },
        { label: 'get_by_ids_v2', value: 'get_by_ids_v2' },
        { label: 'create_insert_v2', value: 'create_insert_v2' },
        { label: 'query_v2', value: 'query_v2' },
        { label: 'upsert_v2', value: 'upsert_v2' }
    ]}
>
<TabItem value="create_delete_by_ids">

Delete a set of vectors from an index by their vector identifiers.

```sql
EXEC cloudflare.vectorize.indexes.create_delete_by_ids 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="get_by_ids">

Get a set of vectors from an index by their vector identifiers.

```sql
EXEC cloudflare.vectorize.indexes.get_by_ids 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="create_insert">

Inserts vectors into the specified index and returns the count of the vectors successfully inserted.

```sql
EXEC cloudflare.vectorize.indexes.create_insert 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required
;
```
</TabItem>
<TabItem value="query">

Finds vectors closest to a given vector in an index.

```sql
EXEC cloudflare.vectorize.indexes.query 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"filter": "{{ filter }}", 
"returnMetadata": {{ returnMetadata }}, 
"returnValues": {{ returnValues }}, 
"topK": {{ topK }}, 
"vector": "{{ vector }}"
}'
;
```
</TabItem>
<TabItem value="upsert">

Upserts vectors into the specified index, creating them if they do not exist and returns the count of values and ids successfully inserted.

```sql
EXEC cloudflare.vectorize.indexes.upsert 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required
;
```
</TabItem>
<TabItem value="create_delete_by_ids_v2">

Delete a set of vectors from an index by their vector identifiers.

```sql
EXEC cloudflare.vectorize.indexes.create_delete_by_ids_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="get_by_ids_v2">

Get a set of vectors from an index by their vector identifiers.

```sql
EXEC cloudflare.vectorize.indexes.get_by_ids_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="create_insert_v2">

Inserts vectors into the specified index and returns a mutation id corresponding to the vectors enqueued for insertion.

```sql
EXEC cloudflare.vectorize.indexes.create_insert_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required, 
@unparsable-behavior='{{ unparsable-behavior }}'
;
```
</TabItem>
<TabItem value="query_v2">

Finds vectors closest to a given vector in an index.

```sql
EXEC cloudflare.vectorize.indexes.query_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required 
@@json=
'{
"filter": "{{ filter }}", 
"returnMetadata": "{{ returnMetadata }}", 
"returnValues": {{ returnValues }}, 
"topK": {{ topK }}, 
"vector": "{{ vector }}"
}'
;
```
</TabItem>
<TabItem value="upsert_v2">

Upserts vectors into the specified index, creating them if they do not exist and returns a mutation id corresponding to the vectors enqueued for upsertion.

```sql
EXEC cloudflare.vectorize.indexes.upsert_v2 
@account_id='{{ account_id }}' --required, 
@index_name='{{ index_name }}' --required, 
@unparsable-behavior='{{ unparsable-behavior }}'
;
```
</TabItem>
</Tabs>
