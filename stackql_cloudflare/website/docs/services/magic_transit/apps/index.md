--- 
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - magic_transit
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

Creates, updates, deletes, gets or lists an <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List Apps response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Display name for the app. (example: Cloudflare Dashboard)</td>
</tr>
<tr>
    <td><CopyableCode code="account_app_id" /></td>
    <td><code>string</code></td>
    <td>Magic account app ID. (example: ac60d3d0435248289d446cedd870bcf4)</td>
</tr>
<tr>
    <td><CopyableCode code="managed_app_id" /></td>
    <td><code>string</code></td>
    <td>Managed app ID. (example: cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="hostnames" /></td>
    <td><code>array</code></td>
    <td>FQDNs to associate with traffic decisions.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_subnets" /></td>
    <td><code>array</code></td>
    <td>IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="source_subnets" /></td>
    <td><code>array</code></td>
    <td>IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Category of the app. (example: Development)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Apps associated with an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new App for an account</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_app_id"><code>account_app_id</code></a></td>
    <td></td>
    <td>Updates an Account App</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_app_id"><code>account_app_id</code></a></td>
    <td></td>
    <td>Updates an Account App</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_app_id"><code>account_app_id</code></a></td>
    <td></td>
    <td>Deletes specific Account App.</td>
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
<tr id="parameter-account_app_id">
    <td><CopyableCode code="account_app_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists Apps associated with an account.

```sql
SELECT
name,
account_app_id,
managed_app_id,
hostnames,
ip_subnets,
source_subnets,
type
FROM cloudflare.magic_transit.apps
WHERE account_id = '{{ account_id }}' -- required
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

Creates a new App for an account

```sql
INSERT INTO cloudflare.magic_transit.apps (
hostnames,
ip_subnets,
name,
source_subnets,
type,
account_id
)
SELECT 
'{{ hostnames }}',
'{{ ip_subnets }}',
'{{ name }}',
'{{ source_subnets }}',
'{{ type }}',
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
- name: apps
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the apps resource.
    - name: hostnames
      value:
        - "{{ hostnames }}"
      description: |
        FQDNs to associate with traffic decisions.
    - name: ip_subnets
      value:
        - "{{ ip_subnets }}"
      description: |
        IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)
    - name: name
      value: "{{ name }}"
      description: |
        Display name for the app.
    - name: source_subnets
      value:
        - "{{ source_subnets }}"
      description: |
        IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)
    - name: type
      value: "{{ type }}"
      description: |
        Category of the app.
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

Updates an Account App

```sql
UPDATE cloudflare.magic_transit.apps
SET 
hostnames = '{{ hostnames }}',
ip_subnets = '{{ ip_subnets }}',
name = '{{ name }}',
source_subnets = '{{ source_subnets }}',
type = '{{ type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND account_app_id = '{{ account_app_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
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

Updates an Account App

```sql
REPLACE cloudflare.magic_transit.apps
SET 
hostnames = '{{ hostnames }}',
ip_subnets = '{{ ip_subnets }}',
name = '{{ name }}',
source_subnets = '{{ source_subnets }}',
type = '{{ type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND account_app_id = '{{ account_app_id }}' --required
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

Deletes specific Account App.

```sql
DELETE FROM cloudflare.magic_transit.apps
WHERE account_id = '{{ account_id }}' --required
AND account_app_id = '{{ account_app_id }}' --required
;
```
</TabItem>
</Tabs>
