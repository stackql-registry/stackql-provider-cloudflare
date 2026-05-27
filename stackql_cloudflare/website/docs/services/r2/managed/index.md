--- 
title: managed
hide_title: false
hide_table_of_contents: false
keywords:
  - managed
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

Creates, updates, deletes, gets or lists a <code>managed</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.managed" /></td></tr>
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

Get Managed Subdomain response.

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
    <td><CopyableCode code="bucketId" /></td>
    <td><code>string</code></td>
    <td>Bucket ID.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain name of the bucket's r2.dev domain.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether this bucket is publicly accessible at the r2.dev domain.</td>
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
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Gets state of public access over the bucket's R2-managed (r2.dev) domain.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Updates state of public access over the bucket's R2-managed (r2.dev) domain.</td>
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

Gets state of public access over the bucket's R2-managed (r2.dev) domain.

```sql
SELECT
bucketId,
domain,
enabled
FROM cloudflare.r2.managed
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
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

Updates state of public access over the bucket's R2-managed (r2.dev) domain.

```sql
REPLACE cloudflare.r2.managed
SET 
enabled = {{ enabled }}
WHERE 
account_id = '{{ account_id }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND enabled = {{ enabled }} --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
