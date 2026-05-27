--- 
title: indexes_info
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes_info
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

Creates, updates, deletes, gets or lists an <code>indexes_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexes_info" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.vectorize.indexes_info" /></td></tr>
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

Get Vectorize Index Info Response

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
    <td><CopyableCode code="dimensions" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of dimensions for the index</td>
</tr>
<tr>
    <td><CopyableCode code="processedUpToDatetime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the timestamp the last mutation batch was processed as an ISO8601 string. (example: 2024-07-22T18:25:44.442097Z)</td>
</tr>
<tr>
    <td><CopyableCode code="processedUpToMutation" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the async mutation operation containing the changeset. (example: 0000aaaa-11bb-22cc-33dd-444444eeeeee)</td>
</tr>
<tr>
    <td><CopyableCode code="vectorCount" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of vectors present in the index</td>
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
    <td>Get information about a vectorize index.</td>
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

Get information about a vectorize index.

```sql
SELECT
dimensions,
processedUpToDatetime,
processedUpToMutation,
vectorCount
FROM cloudflare.vectorize.indexes_info
WHERE account_id = '{{ account_id }}' -- required
AND index_name = '{{ index_name }}' -- required
;
```
</TabItem>
</Tabs>
