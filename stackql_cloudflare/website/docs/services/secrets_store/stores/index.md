--- 
title: stores
hide_title: false
hide_table_of_contents: false
keywords:
  - stores
  - secrets_store
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

Creates, updates, deletes, gets or lists a <code>stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="stores" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.secrets_store.stores" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_system', value: 'get_by_system' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_system', value: 'list_by_system' }
    ]}
>
<TabItem value="get_by_account">

store details

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
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the store (example: service_x_keys)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account Identifier (example: 985e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Whenthe secret was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the secret was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_system">

Store details

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
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the store (example: service_x_keys)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account Identifier (example: 985e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Whenthe secret was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the secret was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List account stores response

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
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the store (example: service_x_keys)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account Identifier (example: 985e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Whenthe secret was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the secret was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_system">

List account stores response

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
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the store (example: service_x_keys)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account Identifier (example: 985e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Whenthe secret was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the secret was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Returns details of a single store</td>
</tr>
<tr>
    <td><a href="#get_by_system"><CopyableCode code="get_by_system" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Returns details of a single store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>Lists all the stores in an account</td>
</tr>
<tr>
    <td><a href="#list_by_system"><CopyableCode code="list_by_system" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a></td>
    <td><a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>Lists all stores in an account that are managed by the calling service. Only returns stores where managed_by matches the authenticated service.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a store in the account</td>
</tr>
<tr>
    <td><a href="#secrets_store_system_create"><CopyableCode code="secrets_store_system_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a store in the account on behalf of the calling service. The store will be marked as managed by the authenticated service. Requires account_id in the request body.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Deletes a single store</td>
</tr>
<tr>
    <td><a href="#secrets_store_system_delete_by_id"><CopyableCode code="secrets_store_system_delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Deletes a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
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
<tr id="parameter-account_tag">
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>Account tag identifier (e.g., '12a6ed19f349896cfbd6694ba3de8d31'). This is the account's external tag identifier, not the numeric account ID.</td>
</tr>
<tr id="parameter-store_id">
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td>The secrets store ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Direction to sort objects</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Order secrets by values in the given field</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of objects to return per page</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_system', value: 'get_by_system' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_system', value: 'list_by_system' }
    ]}
>
<TabItem value="get_by_account">

Returns details of a single store

```sql
SELECT
id,
name,
account_id,
created,
modified
FROM cloudflare.secrets_store.stores
WHERE account_id = '{{ account_id }}' -- required
AND store_id = '{{ store_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_system">

Returns details of a single store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
SELECT
id,
name,
account_id,
created,
modified
FROM cloudflare.secrets_store.stores
WHERE account_tag = '{{ account_tag }}' -- required
AND store_id = '{{ store_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Lists all the stores in an account

```sql
SELECT
id,
name,
account_id,
created,
modified
FROM cloudflare.secrets_store.stores
WHERE account_id = '{{ account_id }}' -- required
AND direction = '{{ direction }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
;
```
</TabItem>
<TabItem value="list_by_system">

Lists all stores in an account that are managed by the calling service. Only returns stores where managed_by matches the authenticated service.

```sql
SELECT
id,
name,
account_id,
created,
modified
FROM cloudflare.secrets_store.stores
WHERE account_tag = '{{ account_tag }}' -- required
AND direction = '{{ direction }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'secrets_store_system_create', value: 'secrets_store_system_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a store in the account

```sql
INSERT INTO cloudflare.secrets_store.stores (
name,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="secrets_store_system_create">

Creates a store in the account on behalf of the calling service. The store will be marked as managed by the authenticated service. Requires account_id in the request body.

```sql
INSERT INTO cloudflare.secrets_store.stores (
account_id,
name,
account_tag
)
SELECT 
{{ account_id }} /* required */,
'{{ name }}' /* required */,
'{{ account_tag }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: stores
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the stores resource.
    - name: account_tag
      value: "{{ account_tag }}"
      description: Required parameter for the stores resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the store
    - name: account_id
      value: {{ account_id }}
      description: |
        Account internal ID (numeric). Required for system API routes. This value must remain consistent for all stores within an account managed by the same service.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'secrets_store_system_delete_by_id', value: 'secrets_store_system_delete_by_id' }
    ]}
>
<TabItem value="delete">

Deletes a single store

```sql
DELETE FROM cloudflare.secrets_store.stores
WHERE account_id = '{{ account_id }}' --required
AND store_id = '{{ store_id }}' --required
;
```
</TabItem>
<TabItem value="secrets_store_system_delete_by_id">

Deletes a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
DELETE FROM cloudflare.secrets_store.stores
WHERE account_tag = '{{ account_tag }}' --required
AND store_id = '{{ store_id }}' --required
;
```
</TabItem>
</Tabs>
