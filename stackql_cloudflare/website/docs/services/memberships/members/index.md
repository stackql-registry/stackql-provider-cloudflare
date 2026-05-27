--- 
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - memberships
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.memberships.members" /></td></tr>
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

The request has succeeded.

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
    <td>Organization Member ID (example: a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8)</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (active, canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

The request has succeeded.

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
    <td>Organization Member ID (example: a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8)</td>
</tr>
<tr>
    <td><CopyableCode code="create_time" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (active, canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="update_time" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td></td>
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
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-member_id"><code>member_id</code></a></td>
    <td></td>
    <td>Retrieve a single membership from an Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-user.email"><code>user.email</code></a>, <a href="#parameter-user.email.contains"><code>user.email.contains</code></a>, <a href="#parameter-user.email.startsWith"><code>user.email.startsWith</code></a>, <a href="#parameter-user.email.endsWith"><code>user.email.endsWith</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>List memberships for an Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#members_create"><CopyableCode code="members_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-member"><code>member</code></a></td>
    <td></td>
    <td>Create a membership that grants access to a specific Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#members_delete"><CopyableCode code="members_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-member_id"><code>member_id</code></a></td>
    <td></td>
    <td>Delete a membership to a particular Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
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
<tr id="parameter-member_id">
    <td><CopyableCode code="member_id" /></td>
    <td><code>string</code></td>
    <td>The account member ID.</td>
</tr>
<tr id="parameter-organization_id">
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>The organization ID.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The amount of items to return. Defaults to 10.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>An opaque token returned from the last list response that when provided will retrieve the next page. Parameters used to filter the retrieved list must remain in subsequent requests with a page token.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>array</code></td>
    <td>Filter the list of memberships by membership status.</td>
</tr>
<tr id="parameter-user.email">
    <td><CopyableCode code="user.email" /></td>
    <td><code>string</code></td>
    <td>Filter the list of memberships for a specific email.</td>
</tr>
<tr id="parameter-user.email.contains">
    <td><CopyableCode code="user.email.contains" /></td>
    <td><code>string</code></td>
    <td>Filter the list of memberships for a specific email that contains a substring.</td>
</tr>
<tr id="parameter-user.email.endsWith">
    <td><CopyableCode code="user.email.endsWith" /></td>
    <td><code>string</code></td>
    <td>Filter the list of memberships for a specific email that ends with a substring.</td>
</tr>
<tr id="parameter-user.email.startsWith">
    <td><CopyableCode code="user.email.startsWith" /></td>
    <td><code>string</code></td>
    <td>Filter the list of memberships for a specific email that starts with a substring.</td>
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

Retrieve a single membership from an Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
SELECT
id,
create_time,
meta,
status,
update_time,
user
FROM cloudflare.memberships.members
WHERE organization_id = '{{ organization_id }}' -- required
AND member_id = '{{ member_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List memberships for an Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
SELECT
id,
create_time,
meta,
status,
update_time,
user
FROM cloudflare.memberships.members
WHERE organization_id = '{{ organization_id }}' -- required
AND status = '{{ status }}'
AND user.email = '{{ user.email }}'
AND user.email.contains = '{{ user.email.contains }}'
AND user.email.startsWith = '{{ user.email.startsWith }}'
AND user.email.endsWith = '{{ user.email.endsWith }}'
AND page_token = '{{ page_token }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="members_create"
    values={[
        { label: 'members_create', value: 'members_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="members_create">

Create a membership that grants access to a specific Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
INSERT INTO cloudflare.memberships.members (
member,
organization_id
)
SELECT 
'{{ member }}' /* required */,
'{{ organization_id }}'
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
    - name: organization_id
      value: "{{ organization_id }}"
      description: Required parameter for the members resource.
    - name: member
      value:
        status: "{{ status }}"
        user:
          email: "{{ email }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="members_delete"
    values={[
        { label: 'members_delete', value: 'members_delete' }
    ]}
>
<TabItem value="members_delete">

Delete a membership to a particular Organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
DELETE FROM cloudflare.memberships.members
WHERE organization_id = '{{ organization_id }}' --required
AND member_id = '{{ member_id }}' --required
;
```
</TabItem>
</Tabs>
