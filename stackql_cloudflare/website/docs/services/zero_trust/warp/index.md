--- 
title: warp
hide_title: false
hide_table_of_contents: false
keywords:
  - warp
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

Creates, updates, deletes, gets or lists a <code>warp</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="warp" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.warp" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get subnet response

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
    <td>The UUID of the subnet. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the subnet. (example: IPv4 Cloudflare Source IPs)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>An optional description of the subnet. (default: , example: example comment, x-stainless-terraform-configurability: computed_optional)</td>
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
    <td>If `true`, this is the default subnet for the account. There can only be one default subnet per account. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td>The private IPv4 or IPv6 range defining the subnet, in CIDR notation. (example: 100.64.0.0/12)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_type" /></td>
    <td><code>string</code></td>
    <td>The type of subnet. (cloudflare_source, warp) (example: cloudflare_source)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-subnet_id"><code>subnet_id</code></a></td>
    <td></td>
    <td>Get a WARP IP assignment subnet.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-network"><code>network</code></a></td>
    <td></td>
    <td>Create a WARP IP assignment subnet. Currently, only IPv4 subnets can be created. **Network constraints:** - The network must be within one of the following private IP ranges: - `10.0.0.0/8` (RFC 1918) - `172.16.0.0/12` (RFC 1918) - `192.168.0.0/16` (RFC 1918) - `100.64.0.0/10` (RFC 6598 - CGNAT) - The subnet must have a prefix length of `/24` or larger (e.g., `/16`, `/20`, `/24` are valid; `/25`, `/28` are not)</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-subnet_id"><code>subnet_id</code></a></td>
    <td></td>
    <td>Updates a WARP IP assignment subnet. **Update constraints:** - The `network` field cannot be modified for WARP subnets. Only `name`, `comment`, and `is_default_network` can be updated. - IPv6 subnets cannot be updated</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-subnet_id"><code>subnet_id</code></a></td>
    <td></td>
    <td>Delete a WARP IP assignment subnet. This operation is idempotent - deleting an already-deleted or non-existent subnet will return success with a null result.</td>
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
<tr id="parameter-subnet_id">
    <td><CopyableCode code="subnet_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get a WARP IP assignment subnet.

```sql
SELECT
id,
name,
comment,
created_at,
deleted_at,
is_default_network,
network,
subnet_type
FROM cloudflare.zero_trust.warp
WHERE account_id = '{{ account_id }}' -- required
AND subnet_id = '{{ subnet_id }}' -- required
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

Create a WARP IP assignment subnet. Currently, only IPv4 subnets can be created. **Network constraints:** - The network must be within one of the following private IP ranges: - `10.0.0.0/8` (RFC 1918) - `172.16.0.0/12` (RFC 1918) - `192.168.0.0/16` (RFC 1918) - `100.64.0.0/10` (RFC 6598 - CGNAT) - The subnet must have a prefix length of `/24` or larger (e.g., `/16`, `/20`, `/24` are valid; `/25`, `/28` are not)

```sql
INSERT INTO cloudflare.zero_trust.warp (
comment,
is_default_network,
name,
network,
account_id
)
SELECT 
'{{ comment }}',
{{ is_default_network }},
'{{ name }}' /* required */,
'{{ network }}' /* required */,
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
- name: warp
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the warp resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        An optional description of the subnet.
      default: 
    - name: is_default_network
      value: {{ is_default_network }}
      description: |
        If \`true\`, this is the default subnet for the account. There can only be one default subnet per account.
      default: false
    - name: name
      value: "{{ name }}"
      description: |
        A user-friendly name for the subnet.
    - name: network
      value: "{{ network }}"
      description: |
        The private IPv4 or IPv6 range defining the subnet, in CIDR notation.
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

Updates a WARP IP assignment subnet. **Update constraints:** - The `network` field cannot be modified for WARP subnets. Only `name`, `comment`, and `is_default_network` can be updated. - IPv6 subnets cannot be updated

```sql
UPDATE cloudflare.zero_trust.warp
SET 
comment = '{{ comment }}',
is_default_network = {{ is_default_network }},
name = '{{ name }}',
network = '{{ network }}'
WHERE 
account_id = '{{ account_id }}' --required
AND subnet_id = '{{ subnet_id }}' --required
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

Delete a WARP IP assignment subnet. This operation is idempotent - deleting an already-deleted or non-existent subnet will return success with a null result.

```sql
DELETE FROM cloudflare.zero_trust.warp
WHERE account_id = '{{ account_id }}' --required
AND subnet_id = '{{ subnet_id }}' --required
;
```
</TabItem>
</Tabs>
