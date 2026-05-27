--- 
title: ip_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_profiles
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

Creates, updates, deletes, gets or lists an <code>ip_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ip_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.ip_profiles" /></td></tr>
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

Get Device IP profile response.

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
    <td>The ID of the Device IP profile. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the Device IP profile. (example: IPv4 Cloudflare Source IPs)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Subnet. (example: b70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the Device IP profile was created. (example: 2025-02-14T13:17:00.123456789Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description of the Device IP profile. (example: example comment)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Device IP profile is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td>The wirefilter expression to match registrations. Available values: "identity.name", "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.saml_attributes". (example: identity.email == "test@cloudflare.com")</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the Device IP profile was last updated. (example: 2025-02-14T13:17:00.123456789Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Device IP profiles response.

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
    <td>The ID of the Device IP profile. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the Device IP profile. (example: IPv4 Cloudflare Source IPs)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Subnet. (example: b70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the Device IP profile was created. (example: 2025-02-14T13:17:00.123456789Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description of the Device IP profile. (example: example comment)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Device IP profile is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td>The wirefilter expression to match registrations. Available values: "identity.name", "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.saml_attributes". (example: identity.email == "test@cloudflare.com")</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the Device IP profile was last updated. (example: 2025-02-14T13:17:00.123456789Z)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Fetches a single WARP Device IP profile.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists WARP Device IP profiles.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subnet_id"><code>subnet_id</code></a>, <a href="#parameter-precedence"><code>precedence</code></a>, <a href="#parameter-match"><code>match</code></a></td>
    <td></td>
    <td>Creates a WARP Device IP profile. Currently, only IPv4 Device subnets can be associated.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Updates a WARP Device IP profile. Currently, only IPv4 Device subnets can be associated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Delete a WARP Device IP profile.</td>
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
<tr id="parameter-profile_id">
    <td><CopyableCode code="profile_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The number of IP profiles to return per page.</td>
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

Fetches a single WARP Device IP profile.

```sql
SELECT
id,
name,
subnet_id,
created_at,
description,
enabled,
match,
precedence,
updated_at
FROM cloudflare.zero_trust.ip_profiles
WHERE account_id = '{{ account_id }}' -- required
AND profile_id = '{{ profile_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists WARP Device IP profiles.

```sql
SELECT
id,
name,
subnet_id,
created_at,
description,
enabled,
match,
precedence,
updated_at
FROM cloudflare.zero_trust.ip_profiles
WHERE account_id = '{{ account_id }}' -- required
AND per_page = '{{ per_page }}'
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

Creates a WARP Device IP profile. Currently, only IPv4 Device subnets can be associated.

```sql
INSERT INTO cloudflare.zero_trust.ip_profiles (
description,
enabled,
match,
name,
precedence,
subnet_id,
account_id
)
SELECT 
'{{ description }}',
{{ enabled }},
'{{ match }}' /* required */,
'{{ name }}' /* required */,
{{ precedence }} /* required */,
'{{ subnet_id }}' /* required */,
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
- name: ip_profiles
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the ip_profiles resource.
    - name: description
      value: "{{ description }}"
      description: |
        An optional description of the Device IP profile.
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether the Device IP profile will be applied to matching devices.
      default: true
    - name: match
      value: "{{ match }}"
      description: |
        The wirefilter expression to match registrations. Available values: "identity.name", "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.saml_attributes".
    - name: name
      value: "{{ name }}"
      description: |
        A user-friendly name for the Device IP profile.
    - name: precedence
      value: {{ precedence }}
      description: |
        The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.
    - name: subnet_id
      value: "{{ subnet_id }}"
      description: |
        The ID of the Subnet.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a WARP Device IP profile. Currently, only IPv4 Device subnets can be associated.

```sql
UPDATE cloudflare.zero_trust.ip_profiles
SET 
description = '{{ description }}',
enabled = {{ enabled }},
match = '{{ match }}',
name = '{{ name }}',
precedence = {{ precedence }},
subnet_id = '{{ subnet_id }}'
WHERE 
account_id = '{{ account_id }}' --required
AND profile_id = '{{ profile_id }}' --required
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

Delete a WARP Device IP profile.

```sql
DELETE FROM cloudflare.zero_trust.ip_profiles
WHERE account_id = '{{ account_id }}' --required
AND profile_id = '{{ profile_id }}' --required
;
```
</TabItem>
</Tabs>
