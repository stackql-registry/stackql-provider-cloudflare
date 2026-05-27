--- 
title: r2_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - r2_catalog
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

Creates, updates, deletes, gets or lists a <code>r2_catalog</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="r2_catalog" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2_data_catalog.r2_catalog" /></td></tr>
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

R2 catalog details.

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
    <td><code>string (uuid)</code></td>
    <td>Use this to uniquely identify the catalog. (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the catalog name (generated from account and bucket name). (example: account123_my-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="bucket" /></td>
    <td><code>string</code></td>
    <td>Specifies the associated R2 bucket name. (example: my-data-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="credential_status" /></td>
    <td><code>string</code></td>
    <td>Shows the credential configuration status. (present, absent) (example: present)</td>
</tr>
<tr>
    <td><CopyableCode code="maintenance_config" /></td>
    <td><code>object</code></td>
    <td>Configures maintenance for the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Indicates the status of the catalog. (active, inactive) (example: active)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of R2 catalogs.

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
    <td><code>string (uuid)</code></td>
    <td>Use this to uniquely identify the catalog. (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specifies the catalog name (generated from account and bucket name). (example: account123_my-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="bucket" /></td>
    <td><code>string</code></td>
    <td>Specifies the associated R2 bucket name. (example: my-data-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="credential_status" /></td>
    <td><code>string</code></td>
    <td>Shows the credential configuration status. (present, absent) (example: present)</td>
</tr>
<tr>
    <td><CopyableCode code="maintenance_config" /></td>
    <td><code>object</code></td>
    <td>Configures maintenance for the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Indicates the status of the catalog. (active, inactive) (example: active)</td>
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
    <td></td>
    <td>Retrieve detailed information about a specific R2 catalog by bucket name. Returns catalog status, maintenance configuration, and credential status.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns a list of R2 buckets that have been enabled as Apache Iceberg catalogs for the specified account. Each catalog represents an R2 bucket configured to store Iceberg metadata and data files.</td>
</tr>
<tr>
    <td><a href="#create_credential"><CopyableCode code="create_credential" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-token"><code>token</code></a></td>
    <td></td>
    <td>Store authentication credentials for a catalog. These credentials are used to authenticate with R2 storage when performing catalog operations.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a></td>
    <td></td>
    <td>Disable an R2 bucket as a catalog. This operation deactivates the catalog but preserves existing metadata and data files. The catalog can be re-enabled later.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a></td>
    <td></td>
    <td>Enable an R2 bucket as an Apache Iceberg catalog. This operation creates the necessary catalog infrastructure and activates the bucket for storing Iceberg metadata and data files.</td>
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

Retrieve detailed information about a specific R2 catalog by bucket name. Returns catalog status, maintenance configuration, and credential status.

```sql
SELECT
id,
name,
bucket,
credential_status,
maintenance_config,
status
FROM cloudflare.r2_data_catalog.r2_catalog
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of R2 buckets that have been enabled as Apache Iceberg catalogs for the specified account. Each catalog represents an R2 bucket configured to store Iceberg metadata and data files.

```sql
SELECT
id,
name,
bucket,
credential_status,
maintenance_config,
status
FROM cloudflare.r2_data_catalog.r2_catalog
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_credential"
    values={[
        { label: 'create_credential', value: 'create_credential' },
        { label: 'disable', value: 'disable' },
        { label: 'enable', value: 'enable' }
    ]}
>
<TabItem value="create_credential">

Store authentication credentials for a catalog. These credentials are used to authenticate with R2 storage when performing catalog operations.

```sql
EXEC cloudflare.r2_data_catalog.r2_catalog.create_credential 
@account_id='{{ account_id }}' --required, 
@bucket_name='{{ bucket_name }}' --required 
@@json=
'{
"token": "{{ token }}"
}'
;
```
</TabItem>
<TabItem value="disable">

Disable an R2 bucket as a catalog. This operation deactivates the catalog but preserves existing metadata and data files. The catalog can be re-enabled later.

```sql
EXEC cloudflare.r2_data_catalog.r2_catalog.disable 
@account_id='{{ account_id }}' --required, 
@bucket_name='{{ bucket_name }}' --required
;
```
</TabItem>
<TabItem value="enable">

Enable an R2 bucket as an Apache Iceberg catalog. This operation creates the necessary catalog infrastructure and activates the bucket for storing Iceberg metadata and data files.

```sql
EXEC cloudflare.r2_data_catalog.r2_catalog.enable 
@account_id='{{ account_id }}' --required, 
@bucket_name='{{ bucket_name }}' --required
;
```
</TabItem>
</Tabs>
