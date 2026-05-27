--- 
title: invites
hide_title: false
hide_table_of_contents: false
keywords:
  - invites
  - user
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

Creates, updates, deletes, gets or lists an <code>invites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invites" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.user.invites" /></td></tr>
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

Invitation Details response

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
    <td>Invite identifier tag. (example: 4f5f0c14a2a41d5063dd301b2f829f04)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_member_id" /></td>
    <td><code>string</code></td>
    <td>ID of the user to add to the organization. (example: 5a7805061c76ada191ed06f989cc3dac)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>ID of the organization the user will be added to. (example: 5a7805061c76ada191ed06f989cc3dac)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Organization name. (example: Cloudflare, Inc.)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the invite is no longer active. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_by" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the invite. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_member_email" /></td>
    <td><code>string</code></td>
    <td>Email address of the user to add to the organization. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the invite was sent. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_is_enforcing_twofactor" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>List of role names the membership has for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the invitation. (pending, accepted, rejected, expired) (example: accepted)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Invitations response

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
    <td>Invite identifier tag. (example: 4f5f0c14a2a41d5063dd301b2f829f04)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_member_id" /></td>
    <td><code>string</code></td>
    <td>ID of the user to add to the organization. (example: 5a7805061c76ada191ed06f989cc3dac)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>ID of the organization the user will be added to. (example: 5a7805061c76ada191ed06f989cc3dac)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Organization name. (example: Cloudflare, Inc.)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the invite is no longer active. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_by" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the invite. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_member_email" /></td>
    <td><code>string</code></td>
    <td>Email address of the user to add to the organization. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="invited_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the invite was sent. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_is_enforcing_twofactor" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>List of role names the membership has for this account.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the invitation. (pending, accepted, rejected, expired) (example: accepted)</td>
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
    <td><a href="#parameter-invite_id"><code>invite_id</code></a></td>
    <td></td>
    <td>Gets the details of an invitation.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists all invitations associated with my user.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-invite_id"><code>invite_id</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td></td>
    <td>Responds to an invitation.</td>
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
<tr id="parameter-invite_id">
    <td><CopyableCode code="invite_id" /></td>
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

Gets the details of an invitation.

```sql
SELECT
id,
invited_member_id,
organization_id,
organization_name,
expires_on,
invited_by,
invited_member_email,
invited_on,
organization_is_enforcing_twofactor,
roles,
status
FROM cloudflare.user.invites
WHERE invite_id = '{{ invite_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all invitations associated with my user.

```sql
SELECT
id,
invited_member_id,
organization_id,
organization_name,
expires_on,
invited_by,
invited_member_email,
invited_on,
organization_is_enforcing_twofactor,
roles,
status
FROM cloudflare.user.invites
;
```
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

Responds to an invitation.

```sql
UPDATE cloudflare.user.invites
SET 
status = '{{ status }}'
WHERE 
invite_id = '{{ invite_id }}' --required
AND status = '{{ status }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
