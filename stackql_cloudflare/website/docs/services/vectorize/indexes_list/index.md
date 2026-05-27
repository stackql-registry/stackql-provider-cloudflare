--- 
title: indexes_list
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes_list
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

Creates, updates, deletes, gets or lists an <code>indexes_list</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indexes_list" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.vectorize.indexes_list" /></td></tr>
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

List Vectors Response

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
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Number of vectors returned in this response</td>
</tr>
<tr>
    <td><CopyableCode code="cursorExpirationTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the cursor expires as an ISO8601 string (example: 2025-08-12T20:32:52.469144957+00:00)</td>
</tr>
<tr>
    <td><CopyableCode code="isTruncated" /></td>
    <td><code>boolean</code></td>
    <td>Whether there are more vectors available beyond this response</td>
</tr>
<tr>
    <td><CopyableCode code="nextCursor" /></td>
    <td><code>string</code></td>
    <td>Cursor for the next page of results (example: suUTaDY5PFUiRweVccnzyt9n75suNPbXHPshvCzue5mHjtj7Letjvzlza9eGj099)</td>
</tr>
<tr>
    <td><CopyableCode code="totalCount" /></td>
    <td><code>integer</code></td>
    <td>Total number of vectors in the index</td>
</tr>
<tr>
    <td><CopyableCode code="vectors" /></td>
    <td><code>array</code></td>
    <td>Array of vector items</td>
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
    <td><a href="#parameter-count"><code>count</code></a>, <a href="#parameter-cursor"><code>cursor</code></a></td>
    <td>Returns a paginated list of vector identifiers from the specified index.</td>
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
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
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

Returns a paginated list of vector identifiers from the specified index.

```sql
SELECT
count,
cursorExpirationTimestamp,
isTruncated,
nextCursor,
totalCount,
vectors
FROM cloudflare.vectorize.indexes_list
WHERE account_id = '{{ account_id }}' -- required
AND index_name = '{{ index_name }}' -- required
AND count = '{{ count }}'
AND cursor = '{{ cursor }}'
;
```
</TabItem>
</Tabs>
