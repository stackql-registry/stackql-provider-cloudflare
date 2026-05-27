--- 
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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

Creates, updates, deletes, gets or lists an <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.assets" /></td></tr>
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

Get request asset response.

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
    <td><code>integer</code></td>
    <td>Asset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Asset name. (example: example.docx)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Defines the asset creation time. (example: 2022-04-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Asset description. (example: example description)</td>
</tr>
<tr>
    <td><CopyableCode code="file_type" /></td>
    <td><code>string</code></td>
    <td>Asset file type. (example: docx)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-asset_id"><code>asset_id</code></a></td>
    <td></td>
    <td>Retrieves an asset attached to a Cloudforce One intelligence request.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-asset_id"><code>asset_id</code></a></td>
    <td></td>
    <td>Updates an asset in a Cloudforce One intelligence request.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-asset_id"><code>asset_id</code></a></td>
    <td></td>
    <td>Removes an asset from a Cloudforce One intelligence request.</td>
</tr>
<tr>
    <td><a href="#new"><CopyableCode code="new" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a></td>
    <td></td>
    <td>Uploads a new asset to a Cloudforce One intelligence request.</td>
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
<tr id="parameter-asset_id">
    <td><CopyableCode code="asset_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Retrieves an asset attached to a Cloudforce One intelligence request.

```sql
SELECT
id,
name,
created,
description,
file_type
FROM cloudflare.cloudforce_one.assets
WHERE account_id = '{{ account_id }}' -- required
AND request_id = '{{ request_id }}' -- required
AND asset_id = '{{ asset_id }}' -- required
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

Updates an asset in a Cloudforce One intelligence request.

```sql
REPLACE cloudflare.cloudforce_one.assets
SET 
source = '{{ source }}'
WHERE 
account_id = '{{ account_id }}' --required
AND request_id = '{{ request_id }}' --required
AND asset_id = '{{ asset_id }}' --required
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

Removes an asset from a Cloudforce One intelligence request.

```sql
DELETE FROM cloudflare.cloudforce_one.assets
WHERE account_id = '{{ account_id }}' --required
AND request_id = '{{ request_id }}' --required
AND asset_id = '{{ asset_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="new"
    values={[
        { label: 'new', value: 'new' }
    ]}
>
<TabItem value="new">

Uploads a new asset to a Cloudforce One intelligence request.

```sql
EXEC cloudflare.cloudforce_one.assets.new 
@account_id='{{ account_id }}' --required, 
@request_id='{{ request_id }}' --required 
@@json=
'{
"source": "{{ source }}"
}'
;
```
</TabItem>
</Tabs>
