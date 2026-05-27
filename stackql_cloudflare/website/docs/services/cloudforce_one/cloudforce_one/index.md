--- 
title: cloudforce_one
hide_title: false
hide_table_of_contents: false
keywords:
  - cloudforce_one
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

Creates, updates, deletes, gets or lists a <code>cloudforce_one</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloudforce_one" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.cloudforce_one" /></td></tr>
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
    <td><a href="#create_requests"><CopyableCode code="create_requests" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td></td>
    <td>Lists Cloudforce One intelligence requests with filtering and pagination.</td>
</tr>
<tr>
    <td><a href="#generate_v2"><CopyableCode code="generate_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-templateId"><code>templateId</code></a>, <a href="#parameter-fields"><code>fields</code></a></td>
    <td></td>
    <td>Generate a takedown letter from a template. Returns V4 JSON for text format or a PDF binary for pdf format.</td>
</tr>
<tr>
    <td><a href="#search_v2"><CopyableCode code="search_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-image_data"><code>image_data</code></a></td>
    <td><a href="#parameter-showHistoric"><code>showHistoric</code></a>, <a href="#parameter-download"><code>download</code></a></td>
    <td>Submit an image and find the n closest matches from the scanned images index without creating any match records. Returns similarity scores and metadata for each match.</td>
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
<tr id="parameter-download">
    <td><CopyableCode code="download" /></td>
    <td><code>string</code></td>
    <td>If true, include base64-encoded image data in the response</td>
</tr>
<tr id="parameter-showHistoric">
    <td><CopyableCode code="showHistoric" /></td>
    <td><code>string</code></td>
    <td>Include scanned images without domain metadata (historic data). Default: false (only show images with domain)</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="create_requests"
    values={[
        { label: 'create_requests', value: 'create_requests' },
        { label: 'generate_v2', value: 'generate_v2' },
        { label: 'search_v2', value: 'search_v2' }
    ]}
>
<TabItem value="create_requests">

Lists Cloudforce One intelligence requests with filtering and pagination.

```sql
EXEC cloudflare.cloudforce_one.cloudforce_one.create_requests 
@account_id='{{ account_id }}' --required 
@@json=
'{
"completed_after": "{{ completed_after }}", 
"completed_before": "{{ completed_before }}", 
"created_after": "{{ created_after }}", 
"created_before": "{{ created_before }}", 
"page": {{ page }}, 
"per_page": {{ per_page }}, 
"request_type": "{{ request_type }}", 
"sort_by": "{{ sort_by }}", 
"sort_order": "{{ sort_order }}", 
"status": "{{ status }}"
}'
;
```
</TabItem>
<TabItem value="generate_v2">

Generate a takedown letter from a template. Returns V4 JSON for text format or a PDF binary for pdf format.

```sql
EXEC cloudflare.cloudforce_one.cloudforce_one.generate_v2 
@account_id='{{ account_id }}' --required 
@@json=
'{
"fields": "{{ fields }}", 
"format": "{{ format }}", 
"templateId": "{{ templateId }}"
}'
;
```
</TabItem>
<TabItem value="search_v2">

Submit an image and find the n closest matches from the scanned images index without creating any match records. Returns similarity scores and metadata for each match.

```sql
EXEC cloudflare.cloudforce_one.cloudforce_one.search_v2 
@account_id='{{ account_id }}' --required, 
@showHistoric='{{ showHistoric }}', 
@download='{{ download }}' 
@@json=
'{
"image_data": "{{ image_data }}", 
"score_threshold": {{ score_threshold }}, 
"top_k": {{ top_k }}
}'
;
```
</TabItem>
</Tabs>
