--- 
title: v2
hide_title: false
hide_table_of_contents: false
keywords:
  - v2
  - images
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

Creates, updates, deletes, gets or lists a <code>v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="v2" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.images.v2" /></td></tr>
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

List images response

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
    <td><CopyableCode code="continuation_token" /></td>
    <td><code>string</code></td>
    <td>Continuation token to fetch next page. Passed as a query param when requesting List V2 api endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="images" /></td>
    <td><code>array</code></td>
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
    <td><a href="#parameter-continuation_token"><code>continuation_token</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-creator"><code>creator</code></a>, <a href="#parameter-meta.<field>[<operator>]"><code>meta.&lt;field&gt;[&lt;operator&gt;]</code></a></td>
    <td>List up to 10000 images with up to 1000 results per page. Use the optional parameters below to get a specific range of images. Pagination is supported via continuation_token. **Metadata Filtering (Optional):** You can optionally filter images by custom metadata fields using the `meta.<field>[<operator>]=<value>` syntax. **Supported Operators:** - `eq` / `eq:string` / `eq:number` / `eq:boolean` - Exact match - `in` / `in:string` / `in:number` - Match any value in list (pipe-separated) **Metadata Filter Constraints:** - Maximum 5 metadata filters per request - Maximum 5 levels of nesting (e.g., `meta.first.second.third.fourth.fifth`) - Maximum 10 elements for list operators (`in`) - Supports string, number, and boolean value types **Examples:** ``` **List all images:** /images/v2 **Filter by metadata [eq]:** /images/v2?meta.status[eq:string]=active **Filter by metadata [in]:** /images/v2?meta.status[in]=pending|deleted|flagged **Filter by metadata [in:number]:** /images/v2?meta.ratings[in:number]=4|5 **Filter by nested metadata:** /images/v2?meta.region.name[eq]=eu-west **Combine metadata filters with creator:** /images/v2?meta.status[eq]=active&creator=user123 **Multiple metadata filters (AND logic):** /images/v2?meta.status[eq]=active&meta.priority[eq:number]=5 ```</td>
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
<tr id="parameter-continuation_token">
    <td><CopyableCode code="continuation_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-creator">
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-meta.<field>[<operator>]">
    <td><CopyableCode code="meta.<field>[<operator>]" /></td>
    <td><code>string</code></td>
    <td>Optional metadata filter(s). Multiple filters can be combined with AND logic. **Operators:** - `eq`, `eq:string`, `eq:number`, `eq:boolean` - Exact match - `in`, `in:string`, `in:number` - Match any value in pipe-separated list **Examples:** - `meta.status[eq]=active` - `meta.priority[eq:number]=5` - `meta.enabled[eq:boolean]=true` - `meta.region[in]=us-east|us-west|eu-west`</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
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

List up to 10000 images with up to 1000 results per page. Use the optional parameters below to get a specific range of images. Pagination is supported via continuation_token. **Metadata Filtering (Optional):** You can optionally filter images by custom metadata fields using the `meta.<field>[<operator>]=<value>` syntax. **Supported Operators:** - `eq` / `eq:string` / `eq:number` / `eq:boolean` - Exact match - `in` / `in:string` / `in:number` - Match any value in list (pipe-separated) **Metadata Filter Constraints:** - Maximum 5 metadata filters per request - Maximum 5 levels of nesting (e.g., `meta.first.second.third.fourth.fifth`) - Maximum 10 elements for list operators (`in`) - Supports string, number, and boolean value types **Examples:** ``` **List all images:** /images/v2 **Filter by metadata [eq]:** /images/v2?meta.status[eq:string]=active **Filter by metadata [in]:** /images/v2?meta.status[in]=pending|deleted|flagged **Filter by metadata [in:number]:** /images/v2?meta.ratings[in:number]=4|5 **Filter by nested metadata:** /images/v2?meta.region.name[eq]=eu-west **Combine metadata filters with creator:** /images/v2?meta.status[eq]=active&creator=user123 **Multiple metadata filters (AND logic):** /images/v2?meta.status[eq]=active&meta.priority[eq:number]=5 ```

```sql
SELECT
continuation_token,
images
FROM cloudflare.images.v2
WHERE account_id = '{{ account_id }}' -- required
AND continuation_token = '{{ continuation_token }}'
AND per_page = '{{ per_page }}'
AND sort_order = '{{ sort_order }}'
AND creator = '{{ creator }}'
AND meta.<field>[<operator>] = '{{ meta.<field>[<operator>] }}'
;
```
</TabItem>
</Tabs>
