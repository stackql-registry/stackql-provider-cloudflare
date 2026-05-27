--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - accounts
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.accounts.accounts" /></td></tr>
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

Account Details response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Account name (example: Demo Account)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the creation of the account (example: 2014-03-01T12:21:02.0000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="managed_by" /></td>
    <td><code>object</code></td>
    <td>Parent container details</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Account settings</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (standard, enterprise)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Accounts response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Account name (example: Demo Account)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the creation of the account (example: 2014-03-01T12:21:02.0000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="managed_by" /></td>
    <td><code>object</code></td>
    <td>Parent container details</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Account settings</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (standard, enterprise)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get information about a specific account that you are a member of.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>List all accounts you have ownership or verified access to.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create an account (only available for tenant admins at this time)</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Update an existing account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a specific account (only available for tenant admins at this time). This is a permanent operation that will delete any zones or other resources under the account</td>
</tr>
<tr>
    <td><a href="#accounts_batch_move_accounts"><CopyableCode code="accounts_batch_move_accounts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_ids"><code>account_ids</code></a>, <a href="#parameter-destination_organization_id"><code>destination_organization_id</code></a></td>
    <td></td>
    <td>Batch move a collection of accounts to a specific organization. ⚠️ Not implemented.</td>
</tr>
<tr>
    <td><a href="#accounts_move_accounts"><CopyableCode code="accounts_move_accounts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_organization_id"><code>destination_organization_id</code></a></td>
    <td></td>
    <td>Move an account within an organization hierarchy or an account outside an organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
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
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
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

Get information about a specific account that you are a member of.

```sql
SELECT
id,
name,
created_on,
managed_by,
settings,
type
FROM cloudflare.accounts.accounts
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all accounts you have ownership or verified access to.

```sql
SELECT
id,
name,
created_on,
managed_by,
settings,
type
FROM cloudflare.accounts.accounts
WHERE name = '{{ name }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND direction = '{{ direction }}'
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

Create an account (only available for tenant admins at this time)

```sql
INSERT INTO cloudflare.accounts.accounts (
name,
type,
unit
)
SELECT 
'{{ name }}' /* required */,
'{{ type }}',
'{{ unit }}'
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
- name: accounts
  props:
    - name: name
      value: "{{ name }}"
      description: |
        Account name
    - name: type
      value: "{{ type }}"
      valid_values: ['standard', 'enterprise']
    - name: unit
      description: |
        information related to the tenant unit, and optionally, an id of the unit to create the account on. see https://developers.cloudflare.com/tenant/how-to/manage-accounts/
      value:
        id: "{{ id }}"
`}</CodeBlock>

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

Update an existing account.

```sql
REPLACE cloudflare.accounts.accounts
SET 
id = '{{ id }}',
managed_by = '{{ managed_by }}',
name = '{{ name }}',
settings = '{{ settings }}',
type = '{{ type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
AND name = '{{ name }}' --required
AND type = '{{ type }}' --required
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

Delete a specific account (only available for tenant admins at this time). This is a permanent operation that will delete any zones or other resources under the account

```sql
DELETE FROM cloudflare.accounts.accounts
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="accounts_batch_move_accounts"
    values={[
        { label: 'accounts_batch_move_accounts', value: 'accounts_batch_move_accounts' },
        { label: 'accounts_move_accounts', value: 'accounts_move_accounts' }
    ]}
>
<TabItem value="accounts_batch_move_accounts">

Batch move a collection of accounts to a specific organization. ⚠️ Not implemented.

```sql
EXEC cloudflare.accounts.accounts.accounts_batch_move_accounts 
@@json=
'{
"account_ids": "{{ account_ids }}", 
"destination_organization_id": "{{ destination_organization_id }}"
}'
;
```
</TabItem>
<TabItem value="accounts_move_accounts">

Move an account within an organization hierarchy or an account outside an organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
EXEC cloudflare.accounts.accounts.accounts_move_accounts 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_organization_id": "{{ destination_organization_id }}"
}'
;
```
</TabItem>
</Tabs>
