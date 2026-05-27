--- 
title: lans
hide_title: false
hide_table_of_contents: false
keywords:
  - lans
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

Creates, updates, deletes, gets or lists a <code>lans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.lans" /></td></tr>
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

Site LAN Details response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="bond_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="ha_link" /></td>
    <td><code>boolean</code></td>
    <td>mark true to use this LAN for HA probing. only works for site with HA turned on. only one LAN can be set as the ha_link.</td>
</tr>
<tr>
    <td><CopyableCode code="is_breakout" /></td>
    <td><code>boolean</code></td>
    <td>mark true to use this LAN for source-based breakout traffic</td>
</tr>
<tr>
    <td><CopyableCode code="is_prioritized" /></td>
    <td><code>boolean</code></td>
    <td>mark true to use this LAN for source-based prioritized traffic</td>
</tr>
<tr>
    <td><CopyableCode code="nat" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="physport" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="routed_subnets" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="static_addressing" /></td>
    <td><code>object</code></td>
    <td>If the site is not configured in high availability mode, this configuration is optional (if omitted, use DHCP). However, if in high availability mode, static_address is required along with secondary and virtual address.</td>
</tr>
<tr>
    <td><CopyableCode code="vlan_tag" /></td>
    <td><code>integer</code></td>
    <td>VLAN ID. Use zero for untagged.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Site LANs response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="bond_id" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="ha_link" /></td>
    <td><code>boolean</code></td>
    <td>mark true to use this LAN for HA probing. only works for site with HA turned on. only one LAN can be set as the ha_link.</td>
</tr>
<tr>
    <td><CopyableCode code="is_breakout" /></td>
    <td><code>boolean</code></td>
    <td>mark true to use this LAN for source-based breakout traffic</td>
</tr>
<tr>
    <td><CopyableCode code="is_prioritized" /></td>
    <td><code>boolean</code></td>
    <td>mark true to use this LAN for source-based prioritized traffic</td>
</tr>
<tr>
    <td><CopyableCode code="nat" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="physport" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="routed_subnets" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="static_addressing" /></td>
    <td><code>object</code></td>
    <td>If the site is not configured in high availability mode, this configuration is optional (if omitted, use DHCP). However, if in high availability mode, static_address is required along with secondary and virtual address.</td>
</tr>
<tr>
    <td><CopyableCode code="vlan_tag" /></td>
    <td><code>integer</code></td>
    <td>VLAN ID. Use zero for untagged.</td>
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
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-lan_id"><code>lan_id</code></a></td>
    <td></td>
    <td>Get a specific Site LAN.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Lists Site LANs associated with an account.</td>
</tr>
<tr>
    <td><a href="#magic_site_lans_create_lan"><CopyableCode code="magic_site_lans_create_lan" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Creates a new Site LAN. If the site is in high availability mode, static_addressing is required along with secondary and virtual address.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-lan_id"><code>lan_id</code></a></td>
    <td></td>
    <td>Patch a specific Site LAN.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-lan_id"><code>lan_id</code></a></td>
    <td></td>
    <td>Update a specific Site LAN.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-lan_id"><code>lan_id</code></a></td>
    <td></td>
    <td>Remove a specific Site LAN.</td>
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
<tr id="parameter-lan_id">
    <td><CopyableCode code="lan_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-site_id">
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>The site ID.</td>
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

Get a specific Site LAN.

```sql
SELECT
id,
name,
bond_id,
site_id,
ha_link,
is_breakout,
is_prioritized,
nat,
physport,
routed_subnets,
static_addressing,
vlan_tag
FROM cloudflare.magic_transit.lans
WHERE site_id = '{{ site_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND lan_id = '{{ lan_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Site LANs associated with an account.

```sql
SELECT
id,
name,
bond_id,
site_id,
ha_link,
is_breakout,
is_prioritized,
nat,
physport,
routed_subnets,
static_addressing,
vlan_tag
FROM cloudflare.magic_transit.lans
WHERE account_id = '{{ account_id }}' -- required
AND site_id = '{{ site_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="magic_site_lans_create_lan"
    values={[
        { label: 'magic_site_lans_create_lan', value: 'magic_site_lans_create_lan' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="magic_site_lans_create_lan">

Creates a new Site LAN. If the site is in high availability mode, static_addressing is required along with secondary and virtual address.

```sql
INSERT INTO cloudflare.magic_transit.lans (
bond_id,
ha_link,
is_breakout,
is_prioritized,
name,
nat,
physport,
routed_subnets,
static_addressing,
vlan_tag,
account_id,
site_id
)
SELECT 
{{ bond_id }},
{{ ha_link }},
{{ is_breakout }},
{{ is_prioritized }},
'{{ name }}',
'{{ nat }}',
{{ physport }},
'{{ routed_subnets }}',
'{{ static_addressing }}',
{{ vlan_tag }},
'{{ account_id }}',
'{{ site_id }}'
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
- name: lans
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the lans resource.
    - name: site_id
      value: "{{ site_id }}"
      description: Required parameter for the lans resource.
    - name: bond_id
      value: {{ bond_id }}
    - name: ha_link
      value: {{ ha_link }}
      description: |
        mark true to use this LAN for HA probing. only works for site with HA turned on. only one LAN can be set as the ha_link.
    - name: is_breakout
      value: {{ is_breakout }}
      description: |
        mark true to use this LAN for source-based breakout traffic
    - name: is_prioritized
      value: {{ is_prioritized }}
      description: |
        mark true to use this LAN for source-based prioritized traffic
    - name: name
      value: "{{ name }}"
    - name: nat
      value:
        static_prefix: "{{ static_prefix }}"
    - name: physport
      value: {{ physport }}
    - name: routed_subnets
      value:
        - nat:
            static_prefix: "{{ static_prefix }}"
          next_hop: "{{ next_hop }}"
          prefix: "{{ prefix }}"
    - name: static_addressing
      description: |
        If the site is not configured in high availability mode, this configuration is optional (if omitted, use DHCP). However, if in high availability mode, static_address is required along with secondary and virtual address.
      value:
        address: "{{ address }}"
        dhcp_relay:
          server_addresses:
            - "{{ server_addresses }}"
        dhcp_server:
          dhcp_options:
            - code: {{ code }}
              type: "{{ type }}"
              value: "{{ value }}"
          dhcp_pool_end: "{{ dhcp_pool_end }}"
          dhcp_pool_start: "{{ dhcp_pool_start }}"
          dns_server: "{{ dns_server }}"
          dns_servers:
            - "{{ dns_servers }}"
          reservations: "{{ reservations }}"
        secondary_address: "{{ secondary_address }}"
        virtual_address: "{{ virtual_address }}"
    - name: vlan_tag
      value: {{ vlan_tag }}
      description: |
        VLAN ID. Use zero for untagged.
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

Patch a specific Site LAN.

```sql
UPDATE cloudflare.magic_transit.lans
SET 
bond_id = {{ bond_id }},
is_breakout = {{ is_breakout }},
is_prioritized = {{ is_prioritized }},
name = '{{ name }}',
nat = '{{ nat }}',
physport = {{ physport }},
routed_subnets = '{{ routed_subnets }}',
static_addressing = '{{ static_addressing }}',
vlan_tag = {{ vlan_tag }}
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND lan_id = '{{ lan_id }}' --required
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

Update a specific Site LAN.

```sql
REPLACE cloudflare.magic_transit.lans
SET 
bond_id = {{ bond_id }},
is_breakout = {{ is_breakout }},
is_prioritized = {{ is_prioritized }},
name = '{{ name }}',
nat = '{{ nat }}',
physport = {{ physport }},
routed_subnets = '{{ routed_subnets }}',
static_addressing = '{{ static_addressing }}',
vlan_tag = {{ vlan_tag }}
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND lan_id = '{{ lan_id }}' --required
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

Remove a specific Site LAN.

```sql
DELETE FROM cloudflare.magic_transit.lans
WHERE site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND lan_id = '{{ lan_id }}' --required
;
```
</TabItem>
</Tabs>
