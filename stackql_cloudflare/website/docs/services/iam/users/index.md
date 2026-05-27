--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.iam.users" /></td></tr>
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

Get SCIM User response

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
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List SCIM Users response

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
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>Retrieves a single account member as a SCIM User resource by user tag.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-startIndex"><code>startIndex</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists account members as SCIM User resources. Supports optional filtering by `userName` (email) using the SCIM filter syntax (e.g. `userName eq "user@example.com"`). Pagination is controlled via `startIndex` and `count` query parameters per RFC 7644 Section 3.4.2.4.</td>
</tr>
<tr>
    <td><a href="#scim_users_create"><CopyableCode code="scim_users_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-schemas"><code>schemas</code></a>, <a href="#parameter-userName"><code>userName</code></a>, <a href="#parameter-emails"><code>emails</code></a>, <a href="#parameter-active"><code>active</code></a></td>
    <td></td>
    <td>Provisions a new account member via SCIM. The `userName` field must be a valid email address and must match the primary email in `emails`. The account must be an Enterprise account with SCIM entitlements enabled.</td>
</tr>
<tr>
    <td><a href="#scim_users_patch"><CopyableCode code="scim_users_patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-schemas"><code>schemas</code></a>, <a href="#parameter-Operations"><code>Operations</code></a></td>
    <td></td>
    <td>Partially updates a SCIM User via PATCH operations (RFC 7644 Section 3.5.2). Supports updating `userName`, `name.givenName`, `name.familyName`, and `active`. Setting `active: false` deprovisions the user (removes them from the account). For IdP compatibility, `emails[type eq "work"].value` is also accepted as an alias for `userName`.</td>
</tr>
<tr>
    <td><a href="#scim_users_put"><CopyableCode code="scim_users_put" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-schemas"><code>schemas</code></a>, <a href="#parameter-userName"><code>userName</code></a></td>
    <td></td>
    <td>Replaces a SCIM User resource (RFC 7644 Section 3.5.1). Fully replaces the mutable attributes of the user. Supports updating `userName`, `name`, `emails`, and `active`.</td>
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
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The user ID.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-startIndex">
    <td><CopyableCode code="startIndex" /></td>
    <td><code>integer</code></td>
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

Retrieves a single account member as a SCIM User resource by user tag.

```sql
SELECT
contents
FROM cloudflare.iam.users
WHERE account_id = '{{ account_id }}' -- required
AND user_id = '{{ user_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists account members as SCIM User resources. Supports optional filtering by `userName` (email) using the SCIM filter syntax (e.g. `userName eq "user@example.com"`). Pagination is controlled via `startIndex` and `count` query parameters per RFC 7644 Section 3.4.2.4.

```sql
SELECT
contents
FROM cloudflare.iam.users
WHERE account_id = '{{ account_id }}' -- required
AND startIndex = '{{ startIndex }}'
AND count = '{{ count }}'
AND filter = '{{ filter }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="scim_users_create"
    values={[
        { label: 'scim_users_create', value: 'scim_users_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="scim_users_create">

Provisions a new account member via SCIM. The `userName` field must be a valid email address and must match the primary email in `emails`. The account must be an Enterprise account with SCIM entitlements enabled.

```sql
INSERT INTO cloudflare.iam.users (
active,
displayName,
emails,
externalId,
name,
schemas,
userName,
account_id
)
SELECT 
{{ active }} /* required */,
'{{ displayName }}',
'{{ emails }}' /* required */,
'{{ externalId }}',
'{{ name }}',
'{{ schemas }}' /* required */,
'{{ userName }}' /* required */,
'{{ account_id }}'
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
    - name: active
      value: {{ active }}
      description: |
        A Boolean value indicating the user's administrative status. Must be \`true\` for user creation.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The name of the user, suitable for display to end-users. If not explicitly set, falls back to the formatted name or userName.
    - name: emails
      description: |
        Email addresses for the user. The primary email must match \`userName\`.
      value:
        - primary: {{ primary }}
          type: "{{ type }}"
          value: "{{ value }}"
    - name: externalId
      value: "{{ externalId }}"
      description: |
        An identifier for the user as defined by the provisioning client (IdP). This value is stored and returned but not interpreted by Cloudflare.
    - name: name
      description: |
        The components of the user's real name.
      value:
        familyName: "{{ familyName }}"
        formatted: "{{ formatted }}"
        givenName: "{{ givenName }}"
    - name: schemas
      value:
        - "{{ schemas }}"
      description: |
        Must contain \`urn:ietf:params:scim:schemas:core:2.0:User\`.
    - name: userName
      value: "{{ userName }}"
      description: |
        Unique identifier for the user, equal to the user's email address.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="scim_users_patch"
    values={[
        { label: 'scim_users_patch', value: 'scim_users_patch' }
    ]}
>
<TabItem value="scim_users_patch">

Partially updates a SCIM User via PATCH operations (RFC 7644 Section 3.5.2). Supports updating `userName`, `name.givenName`, `name.familyName`, and `active`. Setting `active: false` deprovisions the user (removes them from the account). For IdP compatibility, `emails[type eq "work"].value` is also accepted as an alias for `userName`.

```sql
UPDATE cloudflare.iam.users
SET 
Operations = '{{ Operations }}',
schemas = '{{ schemas }}'
WHERE 
account_id = '{{ account_id }}' --required
AND user_id = '{{ user_id }}' --required
AND schemas = '{{ schemas }}' --required
AND Operations = '{{ Operations }}' --required
RETURNING
contents;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="scim_users_put"
    values={[
        { label: 'scim_users_put', value: 'scim_users_put' }
    ]}
>
<TabItem value="scim_users_put">

Replaces a SCIM User resource (RFC 7644 Section 3.5.1). Fully replaces the mutable attributes of the user. Supports updating `userName`, `name`, `emails`, and `active`.

```sql
REPLACE cloudflare.iam.users
SET 
active = {{ active }},
displayName = '{{ displayName }}',
emails = '{{ emails }}',
externalId = '{{ externalId }}',
name = '{{ name }}',
schemas = '{{ schemas }}',
userName = '{{ userName }}'
WHERE 
account_id = '{{ account_id }}' --required
AND user_id = '{{ user_id }}' --required
AND schemas = '{{ schemas }}' --required
AND userName = '{{ userName }}' --required
RETURNING
contents;
```
</TabItem>
</Tabs>
