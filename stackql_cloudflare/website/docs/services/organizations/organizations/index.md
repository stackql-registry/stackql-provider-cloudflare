--- 
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - organizations
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

Creates, updates, deletes, gets or lists an <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="organizations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.organizations.organizations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'get', value: 'get' },
        { label: 'list_by_organization', value: 'list_by_organization' }
    ]}
>
<TabItem value="list_by_account">

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
    <td> (example: a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8, title: Organization ID)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td> (example: a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8, title: Organization ID)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_organization">

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
    <td> (example: a7b9c3d2e8f4g1h5i6j0k9l2m3n7o4p8, title: Organization ID)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="parent" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieve a list of the organizations that "contain" this account or are managing it. The returned list will be in order from "root" to "leaf", where the "leaf" will be the organization that _immediately_ contains the specified account.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a></td>
    <td></td>
    <td>Retrieve the details of a certain organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#list_by_organization"><CopyableCode code="list_by_organization" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-name.startsWith"><code>name.startsWith</code></a>, <a href="#parameter-name.endsWith"><code>name.endsWith</code></a>, <a href="#parameter-name.contains"><code>name.contains</code></a>, <a href="#parameter-containing.account"><code>containing.account</code></a>, <a href="#parameter-containing.user"><code>containing.user</code></a>, <a href="#parameter-containing.organization"><code>containing.organization</code></a>, <a href="#parameter-parent.id"><code>parent.id</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Retrieve a list of organizations a particular user has access to. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-create_time"><code>create_time</code></a>, <a href="#parameter-meta"><code>meta</code></a></td>
    <td></td>
    <td>Create a new organization for a user. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-create_time"><code>create_time</code></a>, <a href="#parameter-meta"><code>meta</code></a></td>
    <td></td>
    <td>Modify organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a></td>
    <td></td>
    <td>Delete an organization. The organization MUST be empty before deleting. It must not contain any sub-organizations, accounts, members or users. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
</tr>
<tr>
    <td><a href="#create_members_batch_create"><CopyableCode code="create_members_batch_create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-members"><code>members</code></a></td>
    <td></td>
    <td>Batch create multiple memberships that grant access to a specific Organization.</td>
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
<tr id="parameter-organization_id">
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>The organization ID.</td>
</tr>
<tr id="parameter-containing.account">
    <td><CopyableCode code="containing.account" /></td>
    <td><code>string</code></td>
    <td>Filter the list of organizations to the ones that contain this particular account.</td>
</tr>
<tr id="parameter-containing.organization">
    <td><CopyableCode code="containing.organization" /></td>
    <td><code>string</code></td>
    <td>Filter the list of organizations to the ones that contain this particular organization.</td>
</tr>
<tr id="parameter-containing.user">
    <td><CopyableCode code="containing.user" /></td>
    <td><code>string</code></td>
    <td>Filter the list of organizations to the ones that contain this particular user. IMPORTANT: Just because an organization "contains" a user is not a representation of any authorization or privilege to manage any resources therein. An organization "containing" a user simply means the user is managed by that organization.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>array</code></td>
    <td>Only return organizations with the specified IDs (ex. id=foo&id=bar). Send multiple elements by repeating the query value.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>(case-sensitive) Filter the list of organizations to where the name is equal to a particular string.</td>
</tr>
<tr id="parameter-name.contains">
    <td><CopyableCode code="name.contains" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of organizations to where the name contains a particular string.</td>
</tr>
<tr id="parameter-name.endsWith">
    <td><CopyableCode code="name.endsWith" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of organizations to where the name ends with a particular string.</td>
</tr>
<tr id="parameter-name.startsWith">
    <td><CopyableCode code="name.startsWith" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of organizations to where the name starts with a particular string.</td>
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
<tr id="parameter-parent.id">
    <td><CopyableCode code="parent.id" /></td>
    <td><code>string</code></td>
    <td>Filter the list of organizations to the ones that are a sub-organization of the specified organization. "null" is a valid value to provide for this parameter. It means "where an organization has no parent (i.e. it is a 'root' organization)."</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'get', value: 'get' },
        { label: 'list_by_organization', value: 'list_by_organization' }
    ]}
>
<TabItem value="list_by_account">

Retrieve a list of the organizations that "contain" this account or are managing it. The returned list will be in order from "root" to "leaf", where the "leaf" will be the organization that _immediately_ contains the specified account.

```sql
SELECT
id,
name,
create_time,
meta,
parent,
profile
FROM cloudflare.organizations.organizations
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieve the details of a certain organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
SELECT
id,
name,
create_time,
meta,
parent,
profile
FROM cloudflare.organizations.organizations
WHERE organization_id = '{{ organization_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_organization">

Retrieve a list of organizations a particular user has access to. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
SELECT
id,
name,
create_time,
meta,
parent,
profile
FROM cloudflare.organizations.organizations
WHERE id = '{{ id }}'
AND name = '{{ name }}'
AND name.startsWith = '{{ name.startsWith }}'
AND name.endsWith = '{{ name.endsWith }}'
AND name.contains = '{{ name.contains }}'
AND containing.account = '{{ containing.account }}'
AND containing.user = '{{ containing.user }}'
AND containing.organization = '{{ containing.organization }}'
AND parent.id = '{{ parent.id }}'
AND page_token = '{{ page_token }}'
AND page_size = '{{ page_size }}'
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

Create a new organization for a user. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
INSERT INTO cloudflare.organizations.organizations (
name,
parent,
profile
)
SELECT 
'{{ name }}' /* required */,
'{{ parent }}',
'{{ profile }}'
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
- name: organizations
  props:
    - name: name
      value: "{{ name }}"
    - name: parent
      value:
        id: "{{ id }}"
        name: "{{ name }}"
    - name: profile
      value:
        business_address: "{{ business_address }}"
        business_email: "{{ business_email }}"
        business_name: "{{ business_name }}"
        business_phone: "{{ business_phone }}"
        external_metadata: "{{ external_metadata }}"
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

Modify organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
REPLACE cloudflare.organizations.organizations
SET 
name = '{{ name }}',
parent = '{{ parent }}',
profile = '{{ profile }}'
WHERE 
organization_id = '{{ organization_id }}' --required
AND name = '{{ name }}' --required
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

Delete an organization. The organization MUST be empty before deleting. It must not contain any sub-organizations, accounts, members or users. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
DELETE FROM cloudflare.organizations.organizations
WHERE organization_id = '{{ organization_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_members_batch_create"
    values={[
        { label: 'create_members_batch_create', value: 'create_members_batch_create' }
    ]}
>
<TabItem value="create_members_batch_create">

Batch create multiple memberships that grant access to a specific Organization.

```sql
EXEC cloudflare.organizations.organizations.create_members_batch_create 
@organization_id='{{ organization_id }}' --required 
@@json=
'{
"members": "{{ members }}"
}'
;
```
</TabItem>
</Tabs>
