--- 
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - iam
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

Creates, updates, deletes, gets or lists a <code>members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.iam.members" /></td></tr>
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

Get User Group Member response

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
    <td>Account member identifier. (example: 4f5f0c14a2a41d5063dd301b2f829f04)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the member was added to the user group. (example: 2026-01-15T10:30:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>The contact email address of the user. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The member's status in the account. (accepted, pending) (example: accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td>Details of the user associated with this membership.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List User Group Members

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
    <td>Account member identifier. (example: 4f5f0c14a2a41d5063dd301b2f829f04)</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>The contact email address of the user. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The member's status in the account. (accepted, pending) (example: accepted)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_group_id"><code>user_group_id</code></a>, <a href="#parameter-member_id"><code>member_id</code></a></td>
    <td></td>
    <td>Get details of a specific member in a user group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_group_id"><code>user_group_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-fuzzyEmail"><code>fuzzyEmail</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>List all the members attached to a user group.</td>
</tr>
<tr>
    <td><a href="#account_user_group_member_create"><CopyableCode code="account_user_group_member_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_group_id"><code>user_group_id</code></a></td>
    <td></td>
    <td>Add members to a User Group.</td>
</tr>
<tr>
    <td><a href="#account_user_group_members_update"><CopyableCode code="account_user_group_members_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_group_id"><code>user_group_id</code></a></td>
    <td></td>
    <td>Replace the set of members attached to a User Group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_group_id"><code>user_group_id</code></a>, <a href="#parameter-member_id"><code>member_id</code></a></td>
    <td></td>
    <td>Remove a member from User Group</td>
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
<tr id="parameter-member_id">
    <td><CopyableCode code="member_id" /></td>
    <td><code>string</code></td>
    <td>The account member ID.</td>
</tr>
<tr id="parameter-user_group_id">
    <td><CopyableCode code="user_group_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-fuzzyEmail">
    <td><CopyableCode code="fuzzyEmail" /></td>
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

Get details of a specific member in a user group.

```sql
SELECT
id,
created_at,
email,
status,
user
FROM cloudflare.iam.members
WHERE account_id = '{{ account_id }}' -- required
AND user_group_id = '{{ user_group_id }}' -- required
AND member_id = '{{ member_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all the members attached to a user group.

```sql
SELECT
id,
email,
status
FROM cloudflare.iam.members
WHERE account_id = '{{ account_id }}' -- required
AND user_group_id = '{{ user_group_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND fuzzyEmail = '{{ fuzzyEmail }}'
AND direction = '{{ direction }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="account_user_group_member_create"
    values={[
        { label: 'account_user_group_member_create', value: 'account_user_group_member_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="account_user_group_member_create">

Add members to a User Group.

```sql
INSERT INTO cloudflare.iam.members (
account_id,
user_group_id
)
SELECT 
'{{ account_id }}',
'{{ user_group_id }}'
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
- name: members
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the members resource.
    - name: user_group_id
      value: "{{ user_group_id }}"
      description: Required parameter for the members resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="account_user_group_members_update"
    values={[
        { label: 'account_user_group_members_update', value: 'account_user_group_members_update' }
    ]}
>
<TabItem value="account_user_group_members_update">

Replace the set of members attached to a User Group.

```sql
REPLACE cloudflare.iam.members
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND user_group_id = '{{ user_group_id }}' --required
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

Remove a member from User Group

```sql
DELETE FROM cloudflare.iam.members
WHERE account_id = '{{ account_id }}' --required
AND user_group_id = '{{ user_group_id }}' --required
AND member_id = '{{ member_id }}' --required
;
```
</TabItem>
</Tabs>
