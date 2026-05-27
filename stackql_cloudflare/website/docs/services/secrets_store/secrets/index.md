--- 
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secrets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.secrets_store.secrets" /></td></tr>
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

secret detail

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
    <td>Secret identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret (example: MY_API_KEY)</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Freeform text describing the secret (example: info about my secret)</td>
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
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of services that can use this secret.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (pending, active, deleted)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_system">

Secret detail

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
    <td>Secret identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret (example: MY_API_KEY)</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Freeform text describing the secret (example: info about my secret)</td>
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
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of services that can use this secret.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (pending, active, deleted)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List store secrets response

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
    <td>Secret identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret (example: MY_API_KEY)</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Freeform text describing the secret (example: info about my secret)</td>
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
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of services that can use this secret.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (pending, active, deleted)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_system">

List store secrets response

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
    <td>Secret identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the secret (example: MY_API_KEY)</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td>Store Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Freeform text describing the secret (example: info about my secret)</td>
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
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>The list of services that can use this secret.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (pending, active, deleted)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Returns details of a single secret</td>
</tr>
<tr>
    <td><a href="#get_by_system"><CopyableCode code="get_by_system" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Returns details of a single secret from a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td><a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-scopes"><code>scopes</code></a></td>
    <td>Lists all store secrets</td>
</tr>
<tr>
    <td><a href="#list_by_system"><CopyableCode code="list_by_system" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td><a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-scopes"><code>scopes</code></a></td>
    <td>Lists all secrets in a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#duplicate_by_account"><CopyableCode code="duplicate_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-scopes"><code>scopes</code></a></td>
    <td></td>
    <td>Duplicates the secret, keeping the value</td>
</tr>
<tr>
    <td><a href="#secrets_store_secret_create"><CopyableCode code="secrets_store_secret_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Creates a secret in the account</td>
</tr>
<tr>
    <td><a href="#secrets_store_system_secret_create"><CopyableCode code="secrets_store_system_secret_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Creates one or more secrets in a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Updates a single secret</td>
</tr>
<tr>
    <td><a href="#secrets_store_system_patch_by_id"><CopyableCode code="secrets_store_system_patch_by_id" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Updates a single secret in a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Deletes a single secret</td>
</tr>
<tr>
    <td><a href="#secrets_store_system_secret_delete_by_id"><CopyableCode code="secrets_store_system_secret_delete_by_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a></td>
    <td></td>
    <td>Deletes a single secret from a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Deletes one or more secrets</td>
</tr>
<tr>
    <td><a href="#secrets_store_system_delete_bulk"><CopyableCode code="secrets_store_system_delete_bulk" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a></td>
    <td></td>
    <td>Deletes one or more secrets from a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
</tr>
<tr>
    <td><a href="#duplicate_by_system"><CopyableCode code="duplicate_by_system" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_tag"><code>account_tag</code></a>, <a href="#parameter-store_id"><code>store_id</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-scopes"><code>scopes</code></a></td>
    <td></td>
    <td>Duplicates a secret in a store managed by the calling service, keeping the value. Returns 404 if the store doesn't exist or is not managed by the authenticated service.</td>
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
<tr id="parameter-secret_id">
    <td><CopyableCode code="secret_id" /></td>
    <td><code>string</code></td>
    <td>The secret ID.</td>
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
<tr id="parameter-scopes">
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>Only secrets with the given scopes will be returned</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Search secrets using a filter string, filtering across name and comment</td>
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

Returns details of a single secret

```sql
SELECT
id,
name,
store_id,
comment,
created,
modified,
scopes,
status
FROM cloudflare.secrets_store.secrets
WHERE account_id = '{{ account_id }}' -- required
AND store_id = '{{ store_id }}' -- required
AND secret_id = '{{ secret_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_system">

Returns details of a single secret from a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
SELECT
id,
name,
store_id,
comment,
created,
modified,
scopes,
status
FROM cloudflare.secrets_store.secrets
WHERE account_tag = '{{ account_tag }}' -- required
AND store_id = '{{ store_id }}' -- required
AND secret_id = '{{ secret_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Lists all store secrets

```sql
SELECT
id,
name,
store_id,
comment,
created,
modified,
scopes,
status
FROM cloudflare.secrets_store.secrets
WHERE account_id = '{{ account_id }}' -- required
AND store_id = '{{ store_id }}' -- required
AND direction = '{{ direction }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND scopes = '{{ scopes }}'
;
```
</TabItem>
<TabItem value="list_by_system">

Lists all secrets in a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
SELECT
id,
name,
store_id,
comment,
created,
modified,
scopes,
status
FROM cloudflare.secrets_store.secrets
WHERE account_tag = '{{ account_tag }}' -- required
AND store_id = '{{ store_id }}' -- required
AND direction = '{{ direction }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND scopes = '{{ scopes }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="duplicate_by_account"
    values={[
        { label: 'duplicate_by_account', value: 'duplicate_by_account' },
        { label: 'secrets_store_secret_create', value: 'secrets_store_secret_create' },
        { label: 'secrets_store_system_secret_create', value: 'secrets_store_system_secret_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="duplicate_by_account">

Duplicates the secret, keeping the value

```sql
INSERT INTO cloudflare.secrets_store.secrets (
comment,
name,
scopes,
account_id,
store_id,
secret_id
)
SELECT 
'{{ comment }}',
'{{ name }}' /* required */,
'{{ scopes }}' /* required */,
'{{ account_id }}',
'{{ store_id }}',
'{{ secret_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="secrets_store_secret_create">

Creates a secret in the account

```sql
INSERT INTO cloudflare.secrets_store.secrets (
account_id,
store_id
)
SELECT 
'{{ account_id }}',
'{{ store_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="secrets_store_system_secret_create">

Creates one or more secrets in a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
INSERT INTO cloudflare.secrets_store.secrets (
account_tag,
store_id
)
SELECT 
'{{ account_tag }}',
'{{ store_id }}'
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
- name: secrets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the secrets resource.
    - name: store_id
      value: "{{ store_id }}"
      description: Required parameter for the secrets resource.
    - name: secret_id
      value: "{{ secret_id }}"
      description: Required parameter for the secrets resource.
    - name: account_tag
      value: "{{ account_tag }}"
      description: Required parameter for the secrets resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        Freeform text describing the secret
    - name: name
      value: "{{ name }}"
      description: |
        The name of the secret
    - name: scopes
      value:
        - "{{ scopes }}"
      description: |
        The list of services that can use this secret.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'secrets_store_system_patch_by_id', value: 'secrets_store_system_patch_by_id' }
    ]}
>
<TabItem value="edit">

Updates a single secret

```sql
UPDATE cloudflare.secrets_store.secrets
SET 
comment = '{{ comment }}',
scopes = '{{ scopes }}',
value = '{{ value }}'
WHERE 
account_id = '{{ account_id }}' --required
AND store_id = '{{ store_id }}' --required
AND secret_id = '{{ secret_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
<TabItem value="secrets_store_system_patch_by_id">

Updates a single secret in a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
UPDATE cloudflare.secrets_store.secrets
SET 
comment = '{{ comment }}',
scopes = '{{ scopes }}',
value = '{{ value }}'
WHERE 
account_tag = '{{ account_tag }}' --required
AND store_id = '{{ store_id }}' --required
AND secret_id = '{{ secret_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'secrets_store_system_secret_delete_by_id', value: 'secrets_store_system_secret_delete_by_id' },
        { label: 'bulk_delete', value: 'bulk_delete' },
        { label: 'secrets_store_system_delete_bulk', value: 'secrets_store_system_delete_bulk' }
    ]}
>
<TabItem value="delete">

Deletes a single secret

```sql
DELETE FROM cloudflare.secrets_store.secrets
WHERE account_id = '{{ account_id }}' --required
AND store_id = '{{ store_id }}' --required
AND secret_id = '{{ secret_id }}' --required
;
```
</TabItem>
<TabItem value="secrets_store_system_secret_delete_by_id">

Deletes a single secret from a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
DELETE FROM cloudflare.secrets_store.secrets
WHERE account_tag = '{{ account_tag }}' --required
AND store_id = '{{ store_id }}' --required
AND secret_id = '{{ secret_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Deletes one or more secrets

```sql
DELETE FROM cloudflare.secrets_store.secrets
WHERE account_id = '{{ account_id }}' --required
AND store_id = '{{ store_id }}' --required
;
```
</TabItem>
<TabItem value="secrets_store_system_delete_bulk">

Deletes one or more secrets from a store managed by the calling service. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
DELETE FROM cloudflare.secrets_store.secrets
WHERE account_tag = '{{ account_tag }}' --required
AND store_id = '{{ store_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="duplicate_by_system"
    values={[
        { label: 'duplicate_by_system', value: 'duplicate_by_system' }
    ]}
>
<TabItem value="duplicate_by_system">

Duplicates a secret in a store managed by the calling service, keeping the value. Returns 404 if the store doesn't exist or is not managed by the authenticated service.

```sql
EXEC cloudflare.secrets_store.secrets.duplicate_by_system 
@account_tag='{{ account_tag }}' --required, 
@store_id='{{ store_id }}' --required, 
@secret_id='{{ secret_id }}' --required 
@@json=
'{
"comment": "{{ comment }}", 
"name": "{{ name }}", 
"scopes": "{{ scopes }}"
}'
;
```
</TabItem>
</Tabs>
