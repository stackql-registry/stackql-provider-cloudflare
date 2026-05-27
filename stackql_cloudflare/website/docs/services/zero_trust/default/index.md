--- 
title: default
hide_title: false
hide_table_of_contents: false
keywords:
  - default
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

Creates, updates, deletes, gets or lists a <code>default</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="default" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.default" /></td></tr>
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

Get the default device settings profile response.

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
    <td><CopyableCode code="gateway_unique_id" /></td>
    <td><code>string</code></td>
    <td> (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td> (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_mode_switch" /></td>
    <td><code>boolean</code></td>
    <td>Whether to allow the user to switch WARP between modes.</td>
</tr>
<tr>
    <td><CopyableCode code="allow_updates" /></td>
    <td><code>boolean</code></td>
    <td>Whether to receive update notifications when a new version of the client is available.</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_to_leave" /></td>
    <td><code>boolean</code></td>
    <td>Whether to allow devices to leave the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="auto_connect" /></td>
    <td><code>number</code></td>
    <td>The amount of time in seconds to reconnect after having been disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="captive_portal" /></td>
    <td><code>number</code></td>
    <td>Turn on the captive portal after the specified amount of time.</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><code>boolean</code></td>
    <td>Whether the policy will be applied to matching devices.</td>
</tr>
<tr>
    <td><CopyableCode code="disable_auto_fallback" /></td>
    <td><code>boolean</code></td>
    <td>If the `dns_server` field of a fallback domain is not present, the client will fall back to a best guess of the default/system DNS resolvers unless this policy option is set to `true`.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the policy will be applied to matching devices.</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>List of routes excluded in the WARP client's tunnel.</td>
</tr>
<tr>
    <td><CopyableCode code="exclude_office_ips" /></td>
    <td><code>boolean</code></td>
    <td>Whether to add Microsoft IPs to Split Tunnel exclusions.</td>
</tr>
<tr>
    <td><CopyableCode code="fallback_domains" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>List of routes included in the WARP client's tunnel.</td>
</tr>
<tr>
    <td><CopyableCode code="register_interface_ip_with_dns" /></td>
    <td><code>boolean</code></td>
    <td>Determines if the operating system will register WARP's local interface IP with your on-premises DNS server.</td>
</tr>
<tr>
    <td><CopyableCode code="sccm_vpn_boundary_support" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the WARP client indicates to SCCM that it is inside a VPN boundary. (Windows only).</td>
</tr>
<tr>
    <td><CopyableCode code="service_mode_v2" /></td>
    <td><code>object</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="support_url" /></td>
    <td><code>string</code></td>
    <td>The URL to launch when the Send Feedback button is clicked. (default: , example: https://1.1.1.1/help)</td>
</tr>
<tr>
    <td><CopyableCode code="switch_locked" /></td>
    <td><code>boolean</code></td>
    <td>Whether to allow the user to turn off the WARP switch and disconnect the client.</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_protocol" /></td>
    <td><code>string</code></td>
    <td>Determines which tunnel protocol to use. (default: , example: wireguard)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_networks" /></td>
    <td><code>object</code></td>
    <td>Virtual network access settings for the device.</td>
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
    <td>Fetches the default device settings profile for an account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates the default device settings profile for an account.</td>
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

Fetches the default device settings profile for an account.

```sql
SELECT
gateway_unique_id,
policy_id,
allow_mode_switch,
allow_updates,
allowed_to_leave,
auto_connect,
captive_portal,
default,
disable_auto_fallback,
enabled,
exclude,
exclude_office_ips,
fallback_domains,
include,
register_interface_ip_with_dns,
sccm_vpn_boundary_support,
service_mode_v2,
support_url,
switch_locked,
tunnel_protocol,
virtual_networks
FROM cloudflare.zero_trust.default
WHERE account_id = '{{ account_id }}' -- required
;
```
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

Updates the default device settings profile for an account.

```sql
UPDATE cloudflare.zero_trust.default
SET 
allow_mode_switch = {{ allow_mode_switch }},
allow_updates = {{ allow_updates }},
allowed_to_leave = {{ allowed_to_leave }},
auto_connect = {{ auto_connect }},
captive_portal = {{ captive_portal }},
disable_auto_fallback = {{ disable_auto_fallback }},
exclude = '{{ exclude }}',
exclude_office_ips = {{ exclude_office_ips }},
include = '{{ include }}',
lan_allow_minutes = {{ lan_allow_minutes }},
lan_allow_subnet_size = {{ lan_allow_subnet_size }},
register_interface_ip_with_dns = {{ register_interface_ip_with_dns }},
sccm_vpn_boundary_support = {{ sccm_vpn_boundary_support }},
service_mode_v2 = '{{ service_mode_v2 }}',
support_url = '{{ support_url }}',
switch_locked = {{ switch_locked }},
tunnel_protocol = '{{ tunnel_protocol }}',
virtual_networks = '{{ virtual_networks }}'
WHERE 
account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
