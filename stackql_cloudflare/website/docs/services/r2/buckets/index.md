--- 
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
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

Creates, updates, deletes, gets or lists a <code>buckets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="buckets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.buckets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get Bucket response.

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
    <td>Name of the bucket. (example: example-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="creation_date" /></td>
    <td><code>string</code></td>
    <td>Creation timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="jurisdiction" /></td>
    <td><code>string</code></td>
    <td>Jurisdiction where objects in this bucket are guaranteed to be stored. (default, eu, fedramp) (default: default, x-stainless-param: jurisdiction)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the bucket. (apac, eeur, enam, weur, wnam, oc) (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="storage_class" /></td>
    <td><code>string</code></td>
    <td>Storage class for newly uploaded objects, unless specified otherwise. (Standard, InfrequentAccess) (default: Standard)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Buckets response.

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
    <td>Name of the bucket. (example: example-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="creation_date" /></td>
    <td><code>string</code></td>
    <td>Creation timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="jurisdiction" /></td>
    <td><code>string</code></td>
    <td>Jurisdiction where objects in this bucket are guaranteed to be stored. (default, eu, fedramp) (default: default, x-stainless-param: jurisdiction)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location of the bucket. (apac, eeur, enam, weur, wnam, oc) (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="storage_class" /></td>
    <td><code>string</code></td>
    <td>Storage class for newly uploaded objects, unless specified otherwise. (Standard, InfrequentAccess) (default: Standard)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Gets properties of an existing R2 bucket.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-name_contains"><code>name_contains</code></a>, <a href="#parameter-start_after"><code>start_after</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Lists all R2 buckets on your account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Creates a new R2 bucket.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a>, <a href="#parameter-cf-r2-storage-class"><code>cf-r2-storage-class</code></a></td>
    <td>Updates properties of an existing R2 bucket.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Deletes an existing R2 bucket.</td>
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
<tr id="parameter-cf-r2-storage-class">
    <td><CopyableCode code="cf-r2-storage-class" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name_contains">
    <td><CopyableCode code="name_contains" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-start_after">
    <td><CopyableCode code="start_after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets properties of an existing R2 bucket.

```sql
SELECT
name,
creation_date,
jurisdiction,
location,
storage_class
FROM cloudflare.r2.buckets
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
<TabItem value="list">

Lists all R2 buckets on your account.

```sql
SELECT
name,
creation_date,
jurisdiction,
location,
storage_class
FROM cloudflare.r2.buckets
WHERE account_id = '{{ account_id }}' -- required
AND name_contains = '{{ name_contains }}'
AND start_after = '{{ start_after }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND cursor = '{{ cursor }}'
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
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

Creates a new R2 bucket.

```sql
INSERT INTO cloudflare.r2.buckets (
locationHint,
name,
storageClass,
account_id,
cf-r2-jurisdiction
)
SELECT 
'{{ locationHint }}',
'{{ name }}' /* required */,
'{{ storageClass }}',
'{{ account_id }}',
'{{ cf-r2-jurisdiction }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: buckets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the buckets resource.
    - name: locationHint
      value: "{{ locationHint }}"
      description: |
        Location of the bucket.
      valid_values: ['apac', 'eeur', 'enam', 'weur', 'wnam', 'oc']
    - name: name
      value: "{{ name }}"
      description: |
        Name of the bucket.
    - name: storageClass
      value: "{{ storageClass }}"
      description: |
        Storage class for newly uploaded objects, unless specified otherwise.
      valid_values: ['Standard', 'InfrequentAccess']
      default: Standard
    - name: cf-r2-jurisdiction
      value: "{{ cf-r2-jurisdiction }}"
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

Updates properties of an existing R2 bucket.

```sql
UPDATE cloudflare.r2.buckets
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction}}'
AND cf-r2-storage-class = '{{ cf-r2-storage-class}}'
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

Deletes an existing R2 bucket.

```sql
DELETE FROM cloudflare.r2.buckets
WHERE bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
</Tabs>
