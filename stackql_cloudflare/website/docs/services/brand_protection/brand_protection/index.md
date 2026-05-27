--- 
title: brand_protection
hide_title: false
hide_table_of_contents: false
keywords:
  - brand_protection
  - brand_protection
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

Creates, updates, deletes, gets or lists a <code>brand_protection</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="brand_protection" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.brand_protection.brand_protection" /></td></tr>
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
    <td><a href="#create_queries"><CopyableCode code="create_queries" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-tag"><code>tag</code></a>, <a href="#parameter-scan"><code>scan</code></a></td>
    <td>Return a success message after creating new saved string queries</td>
</tr>
<tr>
    <td><a href="#submit"><CopyableCode code="submit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Return new URL submissions</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-scan">
    <td><CopyableCode code="scan" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-tag">
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="create_queries"
    values={[
        { label: 'create_queries', value: 'create_queries' },
        { label: 'submit', value: 'submit' }
    ]}
>
<TabItem value="create_queries">

Return a success message after creating new saved string queries

```sql
EXEC cloudflare.brand_protection.brand_protection.create_queries 
@account_id='{{ account_id }}' --required, 
@id='{{ id }}', 
@tag='{{ tag }}', 
@scan={{ scan }} 
@@json=
'{
"max_time": "{{ max_time }}", 
"min_time": "{{ min_time }}", 
"scan": {{ scan }}, 
"string_matches": "{{ string_matches }}", 
"tag": "{{ tag }}"
}'
;
```
</TabItem>
<TabItem value="submit">

Return new URL submissions

```sql
EXEC cloudflare.brand_protection.brand_protection.submit 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
