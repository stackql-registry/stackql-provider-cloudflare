--- 
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.iam.groups" /></td></tr>
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

Get SCIM Group response

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

List SCIM Groups response

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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Retrieves a single SCIM Group resource by group ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-startIndex"><code>startIndex</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists SCIM Group resources for the account. Returns both system groups (backed by Cloudflare permission groups, prefixed `cloudflare-v1-`) and custom user groups. Supports filtering by `displayName` using SCIM filter syntax.</td>
</tr>
<tr>
    <td><a href="#scim_groups_create"><CopyableCode code="scim_groups_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-displayName"><code>displayName</code></a></td>
    <td></td>
    <td>Creates a new SCIM Group (user group) for the account. The `displayName` must not be empty and must not begin with `CF` (reserved for system groups).</td>
</tr>
<tr>
    <td><a href="#scim_groups_patch"><CopyableCode code="scim_groups_patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-schemas"><code>schemas</code></a>, <a href="#parameter-Operations"><code>Operations</code></a></td>
    <td></td>
    <td>Partially updates a SCIM Group via PATCH operations (RFC 7644 Section 3.5.2). Supports add, remove, and replace operations on `members`, `displayName`, and `externalId`. For system groups (prefixed `cloudflare-v1-`), only member management operations are supported.</td>
</tr>
<tr>
    <td><a href="#scim_groups_delete"><CopyableCode code="scim_groups_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Deletes a SCIM Group (custom user groups only). System groups backed by Cloudflare permission groups cannot be deleted via SCIM. Returns 204 No Content on success.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The Access group ID.</td>
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

Retrieves a single SCIM Group resource by group ID.

```sql
SELECT
contents
FROM cloudflare.iam.groups
WHERE account_id = '{{ account_id }}' -- required
AND group_id = '{{ group_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists SCIM Group resources for the account. Returns both system groups (backed by Cloudflare permission groups, prefixed `cloudflare-v1-`) and custom user groups. Supports filtering by `displayName` using SCIM filter syntax.

```sql
SELECT
contents
FROM cloudflare.iam.groups
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
    defaultValue="scim_groups_create"
    values={[
        { label: 'scim_groups_create', value: 'scim_groups_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="scim_groups_create">

Creates a new SCIM Group (user group) for the account. The `displayName` must not be empty and must not begin with `CF` (reserved for system groups).

```sql
INSERT INTO cloudflare.iam.groups (
displayName,
externalId,
account_id
)
SELECT 
'{{ displayName }}' /* required */,
'{{ externalId }}',
'{{ account_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the groups resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        A human-readable name for the Group. REQUIRED. Must not start with \`CF\` (reserved prefix for Cloudflare-managed virtual groups).
    - name: externalId
      value: "{{ externalId }}"
      description: |
        Identifier for the Group as defined by the provisioning client (IdP).
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="scim_groups_patch"
    values={[
        { label: 'scim_groups_patch', value: 'scim_groups_patch' }
    ]}
>
<TabItem value="scim_groups_patch">

Partially updates a SCIM Group via PATCH operations (RFC 7644 Section 3.5.2). Supports add, remove, and replace operations on `members`, `displayName`, and `externalId`. For system groups (prefixed `cloudflare-v1-`), only member management operations are supported.

```sql
UPDATE cloudflare.iam.groups
SET 
Operations = '{{ Operations }}',
schemas = '{{ schemas }}'
WHERE 
account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
AND schemas = '{{ schemas }}' --required
AND Operations = '{{ Operations }}' --required
RETURNING
contents;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="scim_groups_delete"
    values={[
        { label: 'scim_groups_delete', value: 'scim_groups_delete' }
    ]}
>
<TabItem value="scim_groups_delete">

Deletes a SCIM Group (custom user groups only). System groups backed by Cloudflare permission groups cannot be deleted via SCIM. Returns 204 No Content on success.

```sql
DELETE FROM cloudflare.iam.groups
WHERE account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
;
```
</TabItem>
</Tabs>
