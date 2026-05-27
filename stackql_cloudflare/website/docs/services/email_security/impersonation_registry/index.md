--- 
title: impersonation_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - impersonation_registry
  - email_security
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

Creates, updates, deletes, gets or lists an <code>impersonation_registry</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="impersonation_registry" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.impersonation_registry" /></td></tr>
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

Impersonation registry entry details

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
    <td><code>string (uuid)</code></td>
    <td>Impersonation registry entry identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415, title: identifier)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: John Doe)</td>
</tr>
<tr>
    <td><CopyableCode code="directory_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="directory_node_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="external_directory_node_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td> (example: john.doe@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="is_email_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Deprecated, use `modified_at` instead. End of life: November 1, 2026. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="provenance" /></td>
    <td><code>string</code></td>
    <td> (A1S_INTERNAL, SNOOPY-CASB_OFFICE_365, SNOOPY-OFFICE_365, SNOOPY-GOOGLE_DIRECTORY)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of impersonation registry entries

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
    <td><code>string (uuid)</code></td>
    <td>Impersonation registry entry identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415, title: identifier)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: John Doe)</td>
</tr>
<tr>
    <td><CopyableCode code="directory_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="directory_node_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="external_directory_node_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td> (example: john.doe@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="is_email_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Deprecated, use `modified_at` instead. End of life: November 1, 2026. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="provenance" /></td>
    <td><code>string</code></td>
    <td> (A1S_INTERNAL, SNOOPY-CASB_OFFICE_365, SNOOPY-OFFICE_365, SNOOPY-GOOGLE_DIRECTORY)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-impersonation_registry_id"><code>impersonation_registry_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific impersonation registry entry including the protected identity, email pattern, and synchronization source if directory-synced.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-provenance"><code>provenance</code></a></td>
    <td>Returns a paginated list of protected identities in the impersonation registry. These entries define identities and email addresses to protect from impersonation attacks. Can be manually added or automatically synced from directory integrations.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new entry in the impersonation registry to protect against impersonation. Emails attempting to impersonate this identity will be flagged. Supports regex patterns for flexible email matching.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-impersonation_registry_id"><code>impersonation_registry_id</code></a></td>
    <td></td>
    <td>Updates an existing impersonation registry entry. Only provided fields will be modified. Directory-synced entries can't be updated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-impersonation_registry_id"><code>impersonation_registry_id</code></a></td>
    <td></td>
    <td>Removes an entry from the impersonation registry. After deletion, this identity will no longer be protected from impersonation.</td>
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
<tr id="parameter-impersonation_registry_id">
    <td><CopyableCode code="impersonation_registry_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The sorting direction.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Field to sort by.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Current page within paginated list of results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The number of results per page. Maximum value is 1000.</td>
</tr>
<tr id="parameter-provenance">
    <td><CopyableCode code="provenance" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Search term for filtering records. Behavior may change.</td>
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

Retrieves details for a specific impersonation registry entry including the protected identity, email pattern, and synchronization source if directory-synced.

```sql
SELECT
id,
name,
directory_id,
directory_node_id,
external_directory_node_id,
comments,
created_at,
email,
is_email_regex,
last_modified,
modified_at,
provenance
FROM cloudflare.email_security.impersonation_registry
WHERE account_id = '{{ account_id }}' -- required
AND impersonation_registry_id = '{{ impersonation_registry_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of protected identities in the impersonation registry. These entries define identities and email addresses to protect from impersonation attacks. Can be manually added or automatically synced from directory integrations.

```sql
SELECT
id,
name,
directory_id,
directory_node_id,
external_directory_node_id,
comments,
created_at,
email,
is_email_regex,
last_modified,
modified_at,
provenance
FROM cloudflare.email_security.impersonation_registry
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND provenance = '{{ provenance }}'
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

Creates a new entry in the impersonation registry to protect against impersonation. Emails attempting to impersonate this identity will be flagged. Supports regex patterns for flexible email matching.

```sql
INSERT INTO cloudflare.email_security.impersonation_registry (
comments,
directory_id,
directory_node_id,
email,
external_directory_node_id,
is_email_regex,
name,
provenance,
account_id
)
SELECT 
'{{ comments }}',
{{ directory_id }},
{{ directory_node_id }},
'{{ email }}',
'{{ external_directory_node_id }}',
{{ is_email_regex }},
'{{ name }}',
'{{ provenance }}',
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
- name: impersonation_registry
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the impersonation_registry resource.
    - name: comments
      value: "{{ comments }}"
    - name: directory_id
      value: {{ directory_id }}
    - name: directory_node_id
      value: {{ directory_node_id }}
    - name: email
      value: "{{ email }}"
    - name: external_directory_node_id
      value: "{{ external_directory_node_id }}"
    - name: is_email_regex
      value: {{ is_email_regex }}
    - name: name
      value: "{{ name }}"
    - name: provenance
      value: "{{ provenance }}"
      valid_values: ['A1S_INTERNAL', 'SNOOPY-CASB_OFFICE_365', 'SNOOPY-OFFICE_365', 'SNOOPY-GOOGLE_DIRECTORY']
`}</CodeBlock>

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

Updates an existing impersonation registry entry. Only provided fields will be modified. Directory-synced entries can't be updated.

```sql
UPDATE cloudflare.email_security.impersonation_registry
SET 
comments = '{{ comments }}',
directory_id = {{ directory_id }},
directory_node_id = {{ directory_node_id }},
email = '{{ email }}',
external_directory_node_id = '{{ external_directory_node_id }}',
is_email_regex = {{ is_email_regex }},
name = '{{ name }}',
provenance = '{{ provenance }}'
WHERE 
account_id = '{{ account_id }}' --required
AND impersonation_registry_id = '{{ impersonation_registry_id }}' --required
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

Removes an entry from the impersonation registry. After deletion, this identity will no longer be protected from impersonation.

```sql
DELETE FROM cloudflare.email_security.impersonation_registry
WHERE account_id = '{{ account_id }}' --required
AND impersonation_registry_id = '{{ impersonation_registry_id }}' --required
;
```
</TabItem>
</Tabs>
