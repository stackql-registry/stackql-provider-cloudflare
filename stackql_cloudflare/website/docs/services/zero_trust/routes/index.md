--- 
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.routes" /></td></tr>
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

Get a tunnel route response

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
    <td>UUID of the route. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the virtual network. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional remark describing the route. (default: , example: Example comment for this route.)</td>
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
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td>The private IPv4 or IPv6 range connected by the route, in CIDR notation. (example: 172.16.0.0/16)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List tunnel routes response

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
    <td>UUID of the route. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the virtual network. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for a tunnel. (example: blog)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the virtual network. (example: us-east-1-vpc)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional remark describing the route. (default: , example: Example comment for this route.)</td>
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
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td>The private IPv4 or IPv6 range connected by the route, in CIDR notation. (example: 172.16.0.0/16)</td>
</tr>
<tr>
    <td><CopyableCode code="tun_type" /></td>
    <td><code>string</code></td>
    <td>The type of tunnel. (cfd_tunnel, warp_connector, warp, magic, ip_sec, gre, cni) (example: cfd_tunnel)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-route_id"><code>route_id</code></a></td>
    <td></td>
    <td>Get a private network route in an account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-comment"><code>comment</code></a>, <a href="#parameter-is_deleted"><code>is_deleted</code></a>, <a href="#parameter-network_subset"><code>network_subset</code></a>, <a href="#parameter-network_superset"><code>network_superset</code></a>, <a href="#parameter-existed_at"><code>existed_at</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a>, <a href="#parameter-route_id"><code>route_id</code></a>, <a href="#parameter-tun_types"><code>tun_types</code></a>, <a href="#parameter-virtual_network_id"><code>virtual_network_id</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a></td>
    <td>Lists and filters private network routes in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-network"><code>network</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a></td>
    <td></td>
    <td>Routes a private network through a Cloudflare Tunnel.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-route_id"><code>route_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates an existing private network route in an account. The fields that are meant to be updated should be provided in the body of the request.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-route_id"><code>route_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a private network route from an account.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-ip_network_encoded"><code>ip_network_encoded</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a></td>
    <td></td>
    <td>Routes a private network through a Cloudflare Tunnel. The CIDR in `ip_network_encoded` must be written in URL-encoded format.</td>
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
<tr id="parameter-ip_network_encoded">
    <td><CopyableCode code="ip_network_encoded" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-route_id">
    <td><CopyableCode code="route_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment">
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-existed_at">
    <td><CopyableCode code="existed_at" /></td>
    <td><code>string (url-encoded-date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-is_deleted">
    <td><CopyableCode code="is_deleted" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-network_subset">
    <td><CopyableCode code="network_subset" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-network_superset">
    <td><CopyableCode code="network_superset" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-route_id">
    <td><CopyableCode code="route_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tun_types">
    <td><CopyableCode code="tun_types" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-tunnel_id">
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-virtual_network_id">
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
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

Get a private network route in an account.

```sql
SELECT
id,
tunnel_id,
virtual_network_id,
comment,
created_at,
deleted_at,
network
FROM cloudflare.zero_trust.routes
WHERE account_id = '{{ account_id }}' -- required
AND route_id = '{{ route_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists and filters private network routes in an account.

```sql
SELECT
id,
tunnel_id,
virtual_network_id,
tunnel_name,
virtual_network_name,
comment,
created_at,
deleted_at,
network,
tun_type
FROM cloudflare.zero_trust.routes
WHERE account_id = '{{ account_id }}' -- required
AND comment = '{{ comment }}'
AND is_deleted = '{{ is_deleted }}'
AND network_subset = '{{ network_subset }}'
AND network_superset = '{{ network_superset }}'
AND existed_at = '{{ existed_at }}'
AND tunnel_id = '{{ tunnel_id }}'
AND route_id = '{{ route_id }}'
AND tun_types = '{{ tun_types }}'
AND virtual_network_id = '{{ virtual_network_id }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
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

Routes a private network through a Cloudflare Tunnel.

```sql
INSERT INTO cloudflare.zero_trust.routes (
comment,
network,
tunnel_id,
virtual_network_id,
account_id
)
SELECT 
'{{ comment }}',
'{{ network }}' /* required */,
'{{ tunnel_id }}' /* required */,
'{{ virtual_network_id }}',
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
- name: routes
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the routes resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        Optional remark describing the route.
      default: 
    - name: network
      value: "{{ network }}"
      description: |
        The private IPv4 or IPv6 range connected by the route, in CIDR notation.
    - name: tunnel_id
      value: "{{ tunnel_id }}"
      description: |
        UUID of the tunnel.
    - name: virtual_network_id
      value: "{{ virtual_network_id }}"
      description: |
        UUID of the virtual network.
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

Updates an existing private network route in an account. The fields that are meant to be updated should be provided in the body of the request.

```sql
UPDATE cloudflare.zero_trust.routes
SET 
comment = '{{ comment }}',
network = '{{ network }}',
tunnel_id = '{{ tunnel_id }}',
virtual_network_id = '{{ virtual_network_id }}'
WHERE 
route_id = '{{ route_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Deletes a private network route from an account.

```sql
DELETE FROM cloudflare.zero_trust.routes
WHERE route_id = '{{ route_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' }
    ]}
>
<TabItem value="create_by_account">

Routes a private network through a Cloudflare Tunnel. The CIDR in `ip_network_encoded` must be written in URL-encoded format.

```sql
EXEC cloudflare.zero_trust.routes.create_by_account 
@ip_network_encoded='{{ ip_network_encoded }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"comment": "{{ comment }}", 
"tunnel_id": "{{ tunnel_id }}", 
"virtual_network_id": "{{ virtual_network_id }}"
}'
;
```
</TabItem>
</Tabs>
