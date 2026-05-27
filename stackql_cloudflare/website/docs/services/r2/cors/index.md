--- 
title: cors
hide_title: false
hide_table_of_contents: false
keywords:
  - cors
  - r2
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

Creates, updates, deletes, gets or lists a <code>cors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.cors" /></td></tr>
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

Success Response.

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
    <td><code>string</code></td>
    <td>Identifier for this rule. (example: Allow Local Development)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed" /></td>
    <td><code>object</code></td>
    <td>Object specifying allowed origins, methods and headers for this CORS rule.</td>
</tr>
<tr>
    <td><CopyableCode code="exposeHeaders" /></td>
    <td><code>array</code></td>
    <td>Specifies the headers that can be exposed back, and accessed by, the JavaScript making the cross-origin request. If you need to access headers beyond the safelisted response headers, such as Content-Encoding or cf-cache-status, you must specify it here.</td>
</tr>
<tr>
    <td><CopyableCode code="maxAgeSeconds" /></td>
    <td><code>number</code></td>
    <td>Specifies the amount of time (in seconds) browsers are allowed to cache CORS preflight responses. Browsers may limit this to 2 hours or less, even if the maximum value (86400) is specified.</td>
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
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Get the CORS policy for a bucket.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Set the CORS policy for a bucket.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Delete the CORS policy for a bucket.</td>
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
<tr id="parameter-cf-r2-jurisdiction">
    <td><CopyableCode code="cf-r2-jurisdiction" /></td>
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

Get the CORS policy for a bucket.

```sql
SELECT
id,
allowed,
exposeHeaders,
maxAgeSeconds
FROM cloudflare.r2.cors
WHERE bucket_name = '{{ bucket_name }}' -- required
AND account_id = '{{ account_id }}' -- required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
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

Set the CORS policy for a bucket.

```sql
REPLACE cloudflare.r2.cors
SET 
rules = '{{ rules }}'
WHERE 
bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction}}'
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

Delete the CORS policy for a bucket.

```sql
DELETE FROM cloudflare.r2.cors
WHERE bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
</Tabs>
