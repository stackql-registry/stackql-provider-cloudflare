--- 
title: wans
hide_title: false
hide_table_of_contents: false
keywords:
  - wans
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

Creates, updates, deletes, gets or lists a <code>wans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="wans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.wans" /></td></tr>
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

Site WAN Details response

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
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="health_check_rate" /></td>
    <td><code>string</code></td>
    <td>Magic WAN health check rate for tunnels created on this link. The default value is `mid`. (low, mid, high) (default: mid, example: low)</td>
</tr>
<tr>
    <td><CopyableCode code="physport" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of WAN for traffic loadbalancing.</td>
</tr>
<tr>
    <td><CopyableCode code="static_addressing" /></td>
    <td><code>object</code></td>
    <td>(optional) if omitted, use DHCP. Submit secondary_address when site is in high availability mode.</td>
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

List Site WANs response

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
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="health_check_rate" /></td>
    <td><code>string</code></td>
    <td>Magic WAN health check rate for tunnels created on this link. The default value is `mid`. (low, mid, high) (default: mid, example: low)</td>
</tr>
<tr>
    <td><CopyableCode code="physport" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of WAN for traffic loadbalancing.</td>
</tr>
<tr>
    <td><CopyableCode code="static_addressing" /></td>
    <td><code>object</code></td>
    <td>(optional) if omitted, use DHCP. Submit secondary_address when site is in high availability mode.</td>
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
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-wan_id"><code>wan_id</code></a></td>
    <td></td>
    <td>Get a specific Site WAN.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Lists Site WANs associated with an account.</td>
</tr>
<tr>
    <td><a href="#magic_site_wans_create_wan"><CopyableCode code="magic_site_wans_create_wan" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-physport"><code>physport</code></a></td>
    <td></td>
    <td>Creates a new Site WAN.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-wan_id"><code>wan_id</code></a></td>
    <td></td>
    <td>Patch a specific Site WAN.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-wan_id"><code>wan_id</code></a></td>
    <td></td>
    <td>Update a specific Site WAN.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-wan_id"><code>wan_id</code></a></td>
    <td></td>
    <td>Remove a specific Site WAN.</td>
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
<tr id="parameter-site_id">
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>The site ID.</td>
</tr>
<tr id="parameter-wan_id">
    <td><CopyableCode code="wan_id" /></td>
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

Get a specific Site WAN.

```sql
SELECT
id,
name,
site_id,
health_check_rate,
physport,
priority,
static_addressing,
vlan_tag
FROM cloudflare.magic_transit.wans
WHERE site_id = '{{ site_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND wan_id = '{{ wan_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Site WANs associated with an account.

```sql
SELECT
id,
name,
site_id,
health_check_rate,
physport,
priority,
static_addressing,
vlan_tag
FROM cloudflare.magic_transit.wans
WHERE account_id = '{{ account_id }}' -- required
AND site_id = '{{ site_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="magic_site_wans_create_wan"
    values={[
        { label: 'magic_site_wans_create_wan', value: 'magic_site_wans_create_wan' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="magic_site_wans_create_wan">

Creates a new Site WAN.

```sql
INSERT INTO cloudflare.magic_transit.wans (
name,
physport,
priority,
static_addressing,
vlan_tag,
account_id,
site_id
)
SELECT 
'{{ name }}',
{{ physport }} /* required */,
{{ priority }},
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
- name: wans
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the wans resource.
    - name: site_id
      value: "{{ site_id }}"
      description: Required parameter for the wans resource.
    - name: name
      value: "{{ name }}"
    - name: physport
      value: {{ physport }}
    - name: priority
      value: {{ priority }}
    - name: static_addressing
      description: |
        (optional) if omitted, use DHCP. Submit secondary_address when site is in high availability mode.
      value:
        address: "{{ address }}"
        gateway_address: "{{ gateway_address }}"
        secondary_address: "{{ secondary_address }}"
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

Patch a specific Site WAN.

```sql
UPDATE cloudflare.magic_transit.wans
SET 
name = '{{ name }}',
physport = {{ physport }},
priority = {{ priority }},
static_addressing = '{{ static_addressing }}',
vlan_tag = {{ vlan_tag }}
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND wan_id = '{{ wan_id }}' --required
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

Update a specific Site WAN.

```sql
REPLACE cloudflare.magic_transit.wans
SET 
name = '{{ name }}',
physport = {{ physport }},
priority = {{ priority }},
static_addressing = '{{ static_addressing }}',
vlan_tag = {{ vlan_tag }}
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND wan_id = '{{ wan_id }}' --required
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

Remove a specific Site WAN.

```sql
DELETE FROM cloudflare.magic_transit.wans
WHERE site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND wan_id = '{{ wan_id }}' --required
;
```
</TabItem>
</Tabs>
