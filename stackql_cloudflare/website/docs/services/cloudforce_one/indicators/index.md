--- 
title: indicators
hide_title: false
hide_table_of_contents: false
keywords:
  - indicators
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

Creates, updates, deletes, gets or lists an <code>indicators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indicators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.indicators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the indicator.

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
    <td><CopyableCode code="datasetId" /></td>
    <td><code>string</code></td>
    <td>The dataset ID this indicator belongs to. Included in list responses.</td>
</tr>
<tr>
    <td><CopyableCode code="indicatorType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="relatedEvents" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
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
<tr>
    <td><CopyableCode code="value" /></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-indicator_id"><code>indicator_id</code></a></td>
    <td></td>
    <td>Retrieves a specific indicator by its UUID.</td>
</tr>
<tr>
    <td><a href="#patch_indicator_update"><CopyableCode code="patch_indicator_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-indicator_id"><code>indicator_id</code></a></td>
    <td></td>
    <td>Updates an existing indicator's properties.</td>
</tr>
<tr>
    <td><a href="#delete_indicator_delete"><CopyableCode code="delete_indicator_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-indicator_id"><code>indicator_id</code></a></td>
    <td></td>
    <td>Deletes a specific indicator by its UUID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-indicatorType"><code>indicatorType</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Creates a new indicator with the specified type and related datasets.</td>
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
<tr id="parameter-indicator_id">
    <td><CopyableCode code="indicator_id" /></td>
    <td><code>string</code></td>
    <td>Indicator UUID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieves a specific indicator by its UUID.

```sql
SELECT
createdAt,
datasetId,
indicatorType,
relatedEvents,
tags,
updatedAt,
uuid,
value
FROM cloudflare.cloudforce_one.indicators
WHERE account_id = '{{ account_id }}' -- required
AND dataset_id = '{{ dataset_id }}' -- required
AND indicator_id = '{{ indicator_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="patch_indicator_update"
    values={[
        { label: 'patch_indicator_update', value: 'patch_indicator_update' }
    ]}
>
<TabItem value="patch_indicator_update">

Updates an existing indicator's properties.

```sql
UPDATE cloudflare.cloudforce_one.indicators
SET 
indicatorType = '{{ indicatorType }}',
relatedEvents = '{{ relatedEvents }}',
tags = '{{ tags }}',
value = '{{ value }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
AND indicator_id = '{{ indicator_id }}' --required
RETURNING
createdAt,
datasetId,
indicatorType,
relatedEvents,
tags,
updatedAt,
uuid,
value;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_indicator_delete"
    values={[
        { label: 'delete_indicator_delete', value: 'delete_indicator_delete' }
    ]}
>
<TabItem value="delete_indicator_delete">

Deletes a specific indicator by its UUID.

```sql
DELETE FROM cloudflare.cloudforce_one.indicators
WHERE account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
AND indicator_id = '{{ indicator_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' }
    ]}
>
<TabItem value="create">

Creates a new indicator with the specified type and related datasets.

```sql
EXEC cloudflare.cloudforce_one.indicators.create 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required 
@@json=
'{
"autoCreateType": {{ autoCreateType }}, 
"indicatorType": "{{ indicatorType }}", 
"relatedEvents": "{{ relatedEvents }}", 
"tags": "{{ tags }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
</Tabs>
