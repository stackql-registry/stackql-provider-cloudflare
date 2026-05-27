--- 
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - r2_data_catalog
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2_data_catalog.namespaces" /></td></tr>
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

List of namespaces retrieved successfully.

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
    <td><CopyableCode code="details" /></td>
    <td><code>array</code></td>
    <td>Contains detailed metadata for each namespace when return_details is true. Each object includes the namespace, UUID, and timestamps.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace_uuids" /></td>
    <td><code>array</code></td>
    <td>Contains UUIDs for each namespace when return_uuids is true. The order corresponds to the namespaces array.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaces" /></td>
    <td><code>array</code></td>
    <td>Lists namespaces in the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="next_page_token" /></td>
    <td><code>string</code></td>
    <td>Use this opaque token to fetch the next page of results. A null or absent value indicates the last page. (example: MSYxNzU5NzU1NTc4NTA0MTk0JjAxOTliOTliLTJjODgtNzNiMy04ZGJiLTQyMWUwZThmMjc1Nw)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-return_uuids"><code>return_uuids</code></a>, <a href="#parameter-return_details"><code>return_details</code></a></td>
    <td>Returns a list of namespaces in the specified R2 catalog. Supports hierarchical filtering and pagination for efficient traversal of large namespace hierarchies.</td>
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
<tr id="parameter-bucket_name">
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>The R2 bucket name.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of namespaces to return per page. Defaults to 100, maximum 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from a previous response. Use this to fetch the next page of results.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent namespace to filter by. Only returns direct children of this namespace. For nested namespaces, use %1F as separator (e.g., "bronze%1Fanalytics"). Omit this parameter to list top-level namespaces.</td>
</tr>
<tr id="parameter-return_details">
    <td><CopyableCode code="return_details" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include additional metadata (timestamps). When true, response includes created_at and updated_at arrays.</td>
</tr>
<tr id="parameter-return_uuids">
    <td><CopyableCode code="return_uuids" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include namespace UUIDs in the response. Set to true to receive the namespace_uuids array.</td>
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

Returns a list of namespaces in the specified R2 catalog. Supports hierarchical filtering and pagination for efficient traversal of large namespace hierarchies.

```sql
SELECT
details,
namespace_uuids,
namespaces,
next_page_token
FROM cloudflare.r2_data_catalog.namespaces
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND page_token = '{{ page_token }}'
AND page_size = '{{ page_size }}'
AND parent = '{{ parent }}'
AND return_uuids = '{{ return_uuids }}'
AND return_details = '{{ return_details }}'
;
```
</TabItem>
</Tabs>
