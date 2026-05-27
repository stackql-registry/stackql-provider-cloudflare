--- 
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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

Creates, updates, deletes, gets or lists a <code>virtual_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_networks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.virtual_networks" /></td></tr>
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

A virtual network response

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
    <td>UUID of the virtual network. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the virtual network. (example: us-east-1-vpc)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional remark describing the virtual network. (default: , example: Staging VPC for data science)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was created. (example: 2021-01-25T18:22:34.317854Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was deleted. If `null`, the resource has not been deleted. (example: 2009-11-10T23:00:00.000000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_default_network" /></td>
    <td><code>boolean</code></td>
    <td>If `true`, this virtual network is the default for the account. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List virtual networks response

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
    <td>UUID of the virtual network. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the virtual network. (example: us-east-1-vpc)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional remark describing the virtual network. (default: , example: Staging VPC for data science)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was created. (example: 2021-01-25T18:22:34.317854Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was deleted. If `null`, the resource has not been deleted. (example: 2009-11-10T23:00:00.000000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_default_network" /></td>
    <td><code>boolean</code></td>
    <td>If `true`, this virtual network is the default for the account. (x-stainless-terraform-configurability: computed_optional)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-virtual_network_id"><code>virtual_network_id</code></a></td>
    <td></td>
    <td>Get a virtual network.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-is_default"><code>is_default</code></a>, <a href="#parameter-is_default_network"><code>is_default_network</code></a>, <a href="#parameter-is_deleted"><code>is_deleted</code></a></td>
    <td>Lists and filters virtual networks in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Adds a new virtual network to an account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-virtual_network_id"><code>virtual_network_id</code></a></td>
    <td></td>
    <td>Updates an existing virtual network.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-virtual_network_id"><code>virtual_network_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an existing virtual network.</td>
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
<tr id="parameter-virtual_network_id">
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-is_default">
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-is_default_network">
    <td><CopyableCode code="is_default_network" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-is_deleted">
    <td><CopyableCode code="is_deleted" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
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

Get a virtual network.

```sql
SELECT
id,
name,
comment,
created_at,
deleted_at,
is_default_network
FROM cloudflare.zero_trust.virtual_networks
WHERE account_id = '{{ account_id }}' -- required
AND virtual_network_id = '{{ virtual_network_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists and filters virtual networks in an account.

```sql
SELECT
id,
name,
comment,
created_at,
deleted_at,
is_default_network
FROM cloudflare.zero_trust.virtual_networks
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}'
AND name = '{{ name }}'
AND is_default = '{{ is_default }}'
AND is_default_network = '{{ is_default_network }}'
AND is_deleted = '{{ is_deleted }}'
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

Adds a new virtual network to an account.

```sql
INSERT INTO cloudflare.zero_trust.virtual_networks (
comment,
is_default,
is_default_network,
name,
account_id
)
SELECT 
'{{ comment }}',
{{ is_default }},
{{ is_default_network }},
'{{ name }}' /* required */,
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
- name: virtual_networks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the virtual_networks resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        Optional remark describing the virtual network.
      default: 
    - name: is_default
      value: {{ is_default }}
      description: |
        If \`true\`, this virtual network is the default for the account.
    - name: is_default_network
      value: {{ is_default_network }}
      description: |
        If \`true\`, this virtual network is the default for the account.
      default: false
    - name: name
      value: "{{ name }}"
      description: |
        A user-friendly name for the virtual network.
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

Updates an existing virtual network.

```sql
UPDATE cloudflare.zero_trust.virtual_networks
SET 
comment = '{{ comment }}',
is_default_network = {{ is_default_network }},
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND virtual_network_id = '{{ virtual_network_id }}' --required
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

Deletes an existing virtual network.

```sql
DELETE FROM cloudflare.zero_trust.virtual_networks
WHERE virtual_network_id = '{{ virtual_network_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
