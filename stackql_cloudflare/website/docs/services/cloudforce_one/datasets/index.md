--- 
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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

Creates, updates, deletes, gets or lists a <code>datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="datasets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.datasets" /></td></tr>
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

Returns a list of dataset in an account.

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
    <td><CopyableCode code="isPublic" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-isPublic"><code>isPublic</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-isPublic"><code>isPublic</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#copy"><CopyableCode code="copy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-destDatasetId"><code>destDatasetId</code></a>, <a href="#parameter-eventIds"><code>eventIds</code></a></td>
    <td><a href="#parameter-keepRawData"><code>keepRawData</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#move"><CopyableCode code="move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-destDatasetId"><code>destDatasetId</code></a>, <a href="#parameter-eventIds"><code>eventIds</code></a></td>
    <td><a href="#parameter-keepRawData"><code>keepRawData</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#populate"><CopyableCode code="populate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-keepRawData">
    <td><CopyableCode code="keepRawData" /></td>
    <td><code>boolean</code></td>
    <td>If true, copies raw data to the destination dataset. Default is false (raw data is stripped/not copied). Raw data is always deleted from the source.</td>
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

Returns a list of dataset in an account.

```sql
SELECT
name,
isPublic,
uuid
FROM cloudflare.cloudforce_one.datasets
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

No description available.

```sql
INSERT INTO cloudflare.cloudforce_one.datasets (
isPublic,
name,
account_id
)
SELECT 
{{ isPublic }} /* required */,
'{{ name }}' /* required */,
'{{ account_id }}'
RETURNING
name,
isPublic,
uuid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: datasets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the datasets resource.
    - name: isPublic
      value: {{ isPublic }}
      description: |
        If true, then anyone can search the dataset. If false, then its limited to the account.
    - name: name
      value: "{{ name }}"
      description: |
        Used to describe the dataset within the account context.
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

No description available.

```sql
UPDATE cloudflare.cloudforce_one.datasets
SET 
isPublic = {{ isPublic }},
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
AND name = '{{ name }}' --required
AND isPublic = {{ isPublic }} --required
RETURNING
name,
isPublic,
uuid;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="copy"
    values={[
        { label: 'copy', value: 'copy' },
        { label: 'move', value: 'move' },
        { label: 'populate', value: 'populate' }
    ]}
>
<TabItem value="copy">

Returns the number of copied events

```sql
EXEC cloudflare.cloudforce_one.datasets.copy 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required, 
@keepRawData={{ keepRawData }} 
@@json=
'{
"destDatasetId": "{{ destDatasetId }}", 
"eventIds": "{{ eventIds }}"
}'
;
```
</TabItem>
<TabItem value="move">

Returns the number of moved events

```sql
EXEC cloudflare.cloudforce_one.datasets.move 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required, 
@keepRawData={{ keepRawData }} 
@@json=
'{
"destDatasetId": "{{ destDatasetId }}", 
"eventIds": "{{ eventIds }}"
}'
;
```
</TabItem>
<TabItem value="populate">

Returns population results with counts and any errors

```sql
EXEC cloudflare.cloudforce_one.datasets.populate 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
