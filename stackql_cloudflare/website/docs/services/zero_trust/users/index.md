--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get user response

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the user. (example: Jane Doe)</td>
</tr>
<tr>
    <td><CopyableCode code="access_seat" /></td>
    <td><code>boolean</code></td>
    <td>True if the user has authenticated with Cloudflare Access.</td>
</tr>
<tr>
    <td><CopyableCode code="active_device_count" /></td>
    <td><code>number</code></td>
    <td>The number of active devices registered to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string (email)</code></td>
    <td>The email of the user. (example: jdoe@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="gateway_seat" /></td>
    <td><code>boolean</code></td>
    <td>True if the user has logged into the WARP client.</td>
</tr>
<tr>
    <td><CopyableCode code="last_successful_login" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the user last successfully logged in. (example: 2020-07-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="seat_uid" /></td>
    <td><code>string</code></td>
    <td>The unique API identifier for the Zero Trust seat.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>The unique API identifier for the user.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets a specific user for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-email"><code>email</code></a></td>
    <td></td>
    <td>Creates a new user.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-email"><code>email</code></a></td>
    <td></td>
    <td>Updates a specific user's name for an account. Requires the user's current email as confirmation (email cannot be changed).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a specific user for an account. This will also revoke any active seats and tokens for the user.</td>
</tr>
<tr>
    <td><a href="#delete_mfa_authenticators"><CopyableCode code="delete_mfa_authenticators" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-authenticator_id"><code>authenticator_id</code></a></td>
    <td></td>
    <td>Deletes a specific MFA device for a user. This action is only available if MFA is turned on for the organization.</td>
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
<tr id="parameter-authenticator_id">
    <td><CopyableCode code="authenticator_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The user ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a specific user for an account.

```sql
SELECT
id,
name,
access_seat,
active_device_count,
created_at,
email,
gateway_seat,
last_successful_login,
seat_uid,
uid,
updated_at
FROM cloudflare.zero_trust.users
WHERE user_id = '{{ user_id }}' -- required
AND account_id = '{{ account_id }}' -- required
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

Creates a new user.

```sql
INSERT INTO cloudflare.zero_trust.users (
email,
name,
account_id
)
SELECT 
'{{ email }}' /* required */,
'{{ name }}',
'{{ account_id }}'
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
- name: users
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the users resource.
    - name: email
      value: "{{ email }}"
      description: |
        The email of the user.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the user.
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

Updates a specific user's name for an account. Requires the user's current email as confirmation (email cannot be changed).

```sql
REPLACE cloudflare.zero_trust.users
SET 
email = '{{ email }}',
name = '{{ name }}'
WHERE 
user_id = '{{ user_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND email = '{{ email }}' --required
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

Deletes a specific user for an account. This will also revoke any active seats and tokens for the user.

```sql
DELETE FROM cloudflare.zero_trust.users
WHERE user_id = '{{ user_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete_mfa_authenticators"
    values={[
        { label: 'delete_mfa_authenticators', value: 'delete_mfa_authenticators' }
    ]}
>
<TabItem value="delete_mfa_authenticators">

Deletes a specific MFA device for a user. This action is only available if MFA is turned on for the organization.

```sql
EXEC cloudflare.zero_trust.users.delete_mfa_authenticators 
@user_id='{{ user_id }}' --required, 
@account_id='{{ account_id }}' --required, 
@authenticator_id='{{ authenticator_id }}' --required
;
```
</TabItem>
</Tabs>
