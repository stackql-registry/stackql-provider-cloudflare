--- 
title: address_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - address_maps
  - addressing
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

Creates, updates, deletes, gets or lists an <code>address_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="address_maps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.address_maps" /></td></tr>
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

Address Map Details response

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
    <td>Identifier of an Address Map. (example: 055817b111884e0227e1be16a0be6ee0)</td>
</tr>
<tr>
    <td><CopyableCode code="can_delete" /></td>
    <td><code>boolean</code></td>
    <td>If set to false, then the Address Map cannot be deleted via API. This is true for Cloudflare-managed maps.</td>
</tr>
<tr>
    <td><CopyableCode code="can_modify_ips" /></td>
    <td><code>boolean</code></td>
    <td>If set to false, then the IPs on the Address Map cannot be modified via the API. This is true for Cloudflare-managed maps.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="default_sni" /></td>
    <td><code>string</code></td>
    <td>If you have legacy TLS clients which do not send the TLS server name indicator, then you can specify one default SNI on the map. If Cloudflare receives a TLS handshake from a client without an SNI, it will respond with the default SNI on those IPs. The default SNI can be any valid zone or subdomain owned by the account. (example: *.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description field which may be used to describe the types of IPs or zones on the map. (example: My Ecommerce zones)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Address Map is enabled or not. Cloudflare's DNS will not respond with IP addresses on an Address Map until the map is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="ips" /></td>
    <td><code>array</code></td>
    <td>The set of IPs on the Address Map.</td>
</tr>
<tr>
    <td><CopyableCode code="memberships" /></td>
    <td><code>array</code></td>
    <td>Zones and Accounts which will be assigned IPs on this Address Map. A zone membership will take priority over an account membership.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Address Maps response

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
    <td>Identifier of an Address Map. (example: 055817b111884e0227e1be16a0be6ee0)</td>
</tr>
<tr>
    <td><CopyableCode code="can_delete" /></td>
    <td><code>boolean</code></td>
    <td>If set to false, then the Address Map cannot be deleted via API. This is true for Cloudflare-managed maps.</td>
</tr>
<tr>
    <td><CopyableCode code="can_modify_ips" /></td>
    <td><code>boolean</code></td>
    <td>If set to false, then the IPs on the Address Map cannot be modified via the API. This is true for Cloudflare-managed maps.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="default_sni" /></td>
    <td><code>string</code></td>
    <td>If you have legacy TLS clients which do not send the TLS server name indicator, then you can specify one default SNI on the map. If Cloudflare receives a TLS handshake from a client without an SNI, it will respond with the default SNI on those IPs. The default SNI can be any valid zone or subdomain owned by the account. (example: *.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description field which may be used to describe the types of IPs or zones on the map. (example: My Ecommerce zones)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Address Map is enabled or not. Cloudflare's DNS will not respond with IP addresses on an Address Map until the map is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-address_map_id"><code>address_map_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Show a particular address map owned by the account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all address maps owned by the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create a new address map under the account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-address_map_id"><code>address_map_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Modify properties of an address map owned by the account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-address_map_id"><code>address_map_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a particular address map owned by the account. An Address Map must be disabled before it can be deleted.</td>
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
<tr id="parameter-address_map_id">
    <td><CopyableCode code="address_map_id" /></td>
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

Show a particular address map owned by the account.

```sql
SELECT
id,
can_delete,
can_modify_ips,
created_at,
default_sni,
description,
enabled,
ips,
memberships,
modified_at
FROM cloudflare.addressing.address_maps
WHERE address_map_id = '{{ address_map_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all address maps owned by the account.

```sql
SELECT
id,
can_delete,
can_modify_ips,
created_at,
default_sni,
description,
enabled,
modified_at
FROM cloudflare.addressing.address_maps
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

Create a new address map under the account.

```sql
INSERT INTO cloudflare.addressing.address_maps (
description,
enabled,
ips,
memberships,
account_id
)
SELECT 
'{{ description }}',
{{ enabled }},
'{{ ips }}',
'{{ memberships }}',
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
- name: address_maps
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the address_maps resource.
    - name: description
      value: "{{ description }}"
      description: |
        An optional description field which may be used to describe the types of IPs or zones on the map.
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether the Address Map is enabled or not. Cloudflare's DNS will not respond with IP addresses on an Address Map until the map is enabled.
      default: false
    - name: ips
      value:
        - "{{ ips }}"
    - name: memberships
      description: |
        Zones and Accounts which will be assigned IPs on this Address Map. A zone membership will take priority over an account membership.
      value:
        - identifier: "{{ identifier }}"
          kind: "{{ kind }}"
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

Modify properties of an address map owned by the account.

```sql
UPDATE cloudflare.addressing.address_maps
SET 
default_sni = '{{ default_sni }}',
description = '{{ description }}',
enabled = {{ enabled }}
WHERE 
address_map_id = '{{ address_map_id }}' --required
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

Delete a particular address map owned by the account. An Address Map must be disabled before it can be deleted.

```sql
DELETE FROM cloudflare.addressing.address_maps
WHERE address_map_id = '{{ address_map_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
