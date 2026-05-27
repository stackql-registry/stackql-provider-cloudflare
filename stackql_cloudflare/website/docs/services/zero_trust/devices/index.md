--- 
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.devices" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_id"><code>device_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a WARP device.</td>
</tr>
<tr>
    <td><a href="#create_networks"><CopyableCode code="create_networks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-config"><code>config</code></a></td>
    <td></td>
    <td>Creates a new device managed network.</td>
</tr>
<tr>
    <td><a href="#delete_policy"><CopyableCode code="delete_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a device settings profile and fetches a list of the remaining profiles for an account.</td>
</tr>
<tr>
    <td><a href="#update_policy"><CopyableCode code="update_policy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates a configured device settings profile.</td>
</tr>
<tr>
    <td><a href="#unrevoke"><CopyableCode code="unrevoke" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Unrevokes a list of devices. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled. **Deprecated**: please use POST /accounts/&#123;account_id&#125;/devices/registrations/unrevoke instead.</td>
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
<tr id="parameter-device_id">
    <td><CopyableCode code="device_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
</tbody>
</table>

## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a WARP device.

```sql
DELETE FROM cloudflare.zero_trust.devices
WHERE device_id = '{{ device_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_networks"
    values={[
        { label: 'create_networks', value: 'create_networks' },
        { label: 'delete_policy', value: 'delete_policy' },
        { label: 'update_policy', value: 'update_policy' },
        { label: 'unrevoke', value: 'unrevoke' }
    ]}
>
<TabItem value="create_networks">

Creates a new device managed network.

```sql
EXEC cloudflare.zero_trust.devices.create_networks 
@account_id='{{ account_id }}' --required 
@@json=
'{
"config": "{{ config }}", 
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
<TabItem value="delete_policy">

Deletes a device settings profile and fetches a list of the remaining profiles for an account.

```sql
EXEC cloudflare.zero_trust.devices.delete_policy 
@policy_id='{{ policy_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="update_policy">

Updates a configured device settings profile.

```sql
EXEC cloudflare.zero_trust.devices.update_policy 
@policy_id='{{ policy_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"allow_mode_switch": {{ allow_mode_switch }}, 
"allow_updates": {{ allow_updates }}, 
"allowed_to_leave": {{ allowed_to_leave }}, 
"auto_connect": {{ auto_connect }}, 
"captive_portal": {{ captive_portal }}, 
"description": "{{ description }}", 
"disable_auto_fallback": {{ disable_auto_fallback }}, 
"enabled": {{ enabled }}, 
"exclude": "{{ exclude }}", 
"exclude_office_ips": {{ exclude_office_ips }}, 
"include": "{{ include }}", 
"lan_allow_minutes": {{ lan_allow_minutes }}, 
"lan_allow_subnet_size": {{ lan_allow_subnet_size }}, 
"match": "{{ match }}", 
"name": "{{ name }}", 
"precedence": {{ precedence }}, 
"register_interface_ip_with_dns": {{ register_interface_ip_with_dns }}, 
"sccm_vpn_boundary_support": {{ sccm_vpn_boundary_support }}, 
"service_mode_v2": "{{ service_mode_v2 }}", 
"support_url": "{{ support_url }}", 
"switch_locked": {{ switch_locked }}, 
"tunnel_protocol": "{{ tunnel_protocol }}", 
"virtual_networks": "{{ virtual_networks }}"
}'
;
```
</TabItem>
<TabItem value="unrevoke">

Unrevokes a list of devices. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled. **Deprecated**: please use POST /accounts/&#123;account_id&#125;/devices/registrations/unrevoke instead.

```sql
EXEC cloudflare.zero_trust.devices.unrevoke 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
