--- 
title: ownership
hide_title: false
hide_table_of_contents: false
keywords:
  - ownership
  - magic_transit
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

Creates, updates, deletes, gets or lists an <code>ownership</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ownership" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.ownership" /></td></tr>
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

List PCAPs Bucket Ownership response.

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
    <td>The bucket ID associated with the packet captures API. (example: 9883874ecac311ec8475433579a6bf5f)</td>
</tr>
<tr>
    <td><CopyableCode code="destination_conf" /></td>
    <td><code>string</code></td>
    <td>The full URI for the bucket. This field only applies to `full` packet captures. (example: s3://pcaps-bucket?region=us-east-1)</td>
</tr>
<tr>
    <td><CopyableCode code="filename" /></td>
    <td><code>string</code></td>
    <td>The ownership challenge filename stored in the bucket. (example: ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the ownership challenge. Can be pending, success or failed. (pending, success, failed) (example: success)</td>
</tr>
<tr>
    <td><CopyableCode code="submitted" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp when the bucket was added to packet captures API. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="validated" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp when the bucket was validated. (example: 2020-01-01T08:00:00Z)</td>
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
    <td></td>
    <td>List all buckets configured for use with PCAPs API.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-ownership_id"><code>ownership_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes buckets added to the packet captures API.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a>, <a href="#parameter-ownership_challenge"><code>ownership_challenge</code></a></td>
    <td></td>
    <td>Validates buckets added to the packet captures API.</td>
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
<tr id="parameter-ownership_id">
    <td><CopyableCode code="ownership_id" /></td>
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

List all buckets configured for use with PCAPs API.

```sql
SELECT
id,
destination_conf,
filename,
status,
submitted,
validated
FROM cloudflare.magic_transit.ownership
WHERE account_id = '{{ account_id }}' -- required
;
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

Deletes buckets added to the packet captures API.

```sql
DELETE FROM cloudflare.magic_transit.ownership
WHERE ownership_id = '{{ ownership_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate"
    values={[
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="validate">

Validates buckets added to the packet captures API.

```sql
EXEC cloudflare.magic_transit.ownership.validate 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}", 
"ownership_challenge": "{{ ownership_challenge }}"
}'
;
```
</TabItem>
</Tabs>
