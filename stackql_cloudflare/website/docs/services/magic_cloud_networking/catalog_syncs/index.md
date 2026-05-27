--- 
title: catalog_syncs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog_syncs
  - magic_cloud_networking
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

Creates, updates, deletes, gets or lists a <code>catalog_syncs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="catalog_syncs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_cloud_networking.catalog_syncs" /></td></tr>
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

OK.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="destination_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="destination_type" /></td>
    <td><code>string</code></td>
    <td> (NONE, ZERO_TRUST_LIST)</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="includes_discoveries_until" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_attempted_update_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_successful_update_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_user_update_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="policy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="update_mode" /></td>
    <td><code>string</code></td>
    <td> (AUTO, MANUAL)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

OK.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="destination_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="destination_type" /></td>
    <td><code>string</code></td>
    <td> (NONE, ZERO_TRUST_LIST)</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="includes_discoveries_until" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_attempted_update_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_successful_update_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_user_update_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="policy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="update_mode" /></td>
    <td><code>string</code></td>
    <td> (AUTO, MANUAL)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sync_id"><code>sync_id</code></a></td>
    <td></td>
    <td>Read a Catalog Sync (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List Catalog Syncs (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mode"><code>update_mode</code></a>, <a href="#parameter-destination_type"><code>destination_type</code></a></td>
    <td><a href="#parameter-forwarded"><code>forwarded</code></a></td>
    <td>Create a new Catalog Sync (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sync_id"><code>sync_id</code></a></td>
    <td></td>
    <td>Update a Catalog Sync (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sync_id"><code>sync_id</code></a></td>
    <td></td>
    <td>Update a Catalog Sync (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sync_id"><code>sync_id</code></a></td>
    <td><a href="#parameter-delete_destination"><code>delete_destination</code></a></td>
    <td>Delete a Catalog Sync (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sync_id"><code>sync_id</code></a></td>
    <td></td>
    <td>Refresh a Catalog Sync's destination by running the sync policy against latest resource catalog (Closed Beta).</td>
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
<tr id="parameter-sync_id">
    <td><CopyableCode code="sync_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-delete_destination">
    <td><CopyableCode code="delete_destination" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-forwarded">
    <td><CopyableCode code="forwarded" /></td>
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

Read a Catalog Sync (Closed Beta).

```sql
SELECT
id,
name,
destination_id,
description,
destination_type,
errors,
includes_discoveries_until,
last_attempted_update_at,
last_successful_update_at,
last_user_update_at,
policy,
update_mode
FROM cloudflare.magic_cloud_networking.catalog_syncs
WHERE account_id = '{{ account_id }}' -- required
AND sync_id = '{{ sync_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Catalog Syncs (Closed Beta).

```sql
SELECT
id,
name,
destination_id,
description,
destination_type,
errors,
includes_discoveries_until,
last_attempted_update_at,
last_successful_update_at,
last_user_update_at,
policy,
update_mode
FROM cloudflare.magic_cloud_networking.catalog_syncs
WHERE account_id = '{{ account_id }}' -- required
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

Create a new Catalog Sync (Closed Beta).

```sql
INSERT INTO cloudflare.magic_cloud_networking.catalog_syncs (
description,
destination_type,
name,
policy,
update_mode,
account_id,
forwarded
)
SELECT 
'{{ description }}',
'{{ destination_type }}' /* required */,
'{{ name }}' /* required */,
'{{ policy }}',
'{{ update_mode }}' /* required */,
'{{ account_id }}',
'{{ forwarded }}'
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
- name: catalog_syncs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the catalog_syncs resource.
    - name: description
      value: "{{ description }}"
    - name: destination_type
      value: "{{ destination_type }}"
      valid_values: ['NONE', 'ZERO_TRUST_LIST']
    - name: name
      value: "{{ name }}"
    - name: policy
      value: "{{ policy }}"
    - name: update_mode
      value: "{{ update_mode }}"
      valid_values: ['AUTO', 'MANUAL']
    - name: forwarded
      value: "{{ forwarded }}"
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

Update a Catalog Sync (Closed Beta).

```sql
UPDATE cloudflare.magic_cloud_networking.catalog_syncs
SET 
description = '{{ description }}',
name = '{{ name }}',
policy = '{{ policy }}',
update_mode = '{{ update_mode }}'
WHERE 
account_id = '{{ account_id }}' --required
AND sync_id = '{{ sync_id }}' --required
RETURNING
errors,
messages,
result,
success;
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

Update a Catalog Sync (Closed Beta).

```sql
REPLACE cloudflare.magic_cloud_networking.catalog_syncs
SET 
description = '{{ description }}',
name = '{{ name }}',
policy = '{{ policy }}',
update_mode = '{{ update_mode }}'
WHERE 
account_id = '{{ account_id }}' --required
AND sync_id = '{{ sync_id }}' --required
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

Delete a Catalog Sync (Closed Beta).

```sql
DELETE FROM cloudflare.magic_cloud_networking.catalog_syncs
WHERE account_id = '{{ account_id }}' --required
AND sync_id = '{{ sync_id }}' --required
AND delete_destination = '{{ delete_destination }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh"
    values={[
        { label: 'refresh', value: 'refresh' }
    ]}
>
<TabItem value="refresh">

Refresh a Catalog Sync's destination by running the sync policy against latest resource catalog (Closed Beta).

```sql
EXEC cloudflare.magic_cloud_networking.catalog_syncs.refresh 
@account_id='{{ account_id }}' --required, 
@sync_id='{{ sync_id }}' --required
;
```
</TabItem>
</Tabs>
