--- 
title: devices_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_policy
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

Creates, updates, deletes, gets or lists a <code>devices_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.devices_policy" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' }
    ]}
>
<TabItem value="get_by_account">

Get device settings profile by ID response.

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
    <td>The name of the device settings profile. (example: Allow Developers)</td>
</tr>
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
    <td>Whether the policy is the default policy for an account.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the policy. (example: Policy for test teams.)</td>
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
    <td><CopyableCode code="lan_allow_minutes" /></td>
    <td><code>number</code></td>
    <td>The amount of time in minutes a user is allowed access to their LAN. A value of 0 will allow LAN access until the next WARP reconnection, such as a reboot or a laptop waking from sleep. Note that this field is omitted from the response if null or unset.</td>
</tr>
<tr>
    <td><CopyableCode code="lan_allow_subnet_size" /></td>
    <td><code>number</code></td>
    <td>The size of the subnet for the local access network. Note that this field is omitted from the response if null or unset.</td>
</tr>
<tr>
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td>The wirefilter expression to match devices. Available values: "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.service_token_uuid", "identity.saml_attributes", "network", "os.name", "os.version". (example: identity.email == "test@cloudflare.com")</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>number</code></td>
    <td>The precedence of the policy. Lower values indicate higher precedence. Policies will be evaluated in ascending order of this field.</td>
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
    <td><CopyableCode code="target_tests" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a device settings profile by ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-precedence"><code>precedence</code></a>, <a href="#parameter-match"><code>match</code></a></td>
    <td></td>
    <td>Creates a device settings profile to be applied to certain devices matching the criteria.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' }
    ]}
>
<TabItem value="get_by_account">

Fetches a device settings profile by ID.

```sql
SELECT
name,
gateway_unique_id,
policy_id,
allow_mode_switch,
allow_updates,
allowed_to_leave,
auto_connect,
captive_portal,
default,
description,
disable_auto_fallback,
enabled,
exclude,
exclude_office_ips,
fallback_domains,
include,
lan_allow_minutes,
lan_allow_subnet_size,
match,
precedence,
register_interface_ip_with_dns,
sccm_vpn_boundary_support,
service_mode_v2,
support_url,
switch_locked,
target_tests,
tunnel_protocol,
virtual_networks
FROM cloudflare.zero_trust.devices_policy
WHERE policy_id = '{{ policy_id }}' -- required
AND account_id = '{{ account_id }}' -- required
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

Creates a device settings profile to be applied to certain devices matching the criteria.

```sql
INSERT INTO cloudflare.zero_trust.devices_policy (
allow_mode_switch,
allow_updates,
allowed_to_leave,
auto_connect,
captive_portal,
description,
disable_auto_fallback,
enabled,
exclude,
exclude_office_ips,
include,
lan_allow_minutes,
lan_allow_subnet_size,
match,
name,
precedence,
register_interface_ip_with_dns,
sccm_vpn_boundary_support,
service_mode_v2,
support_url,
switch_locked,
tunnel_protocol,
virtual_networks,
account_id
)
SELECT 
{{ allow_mode_switch }},
{{ allow_updates }},
{{ allowed_to_leave }},
{{ auto_connect }},
{{ captive_portal }},
'{{ description }}',
{{ disable_auto_fallback }},
{{ enabled }},
'{{ exclude }}',
{{ exclude_office_ips }},
'{{ include }}',
{{ lan_allow_minutes }},
{{ lan_allow_subnet_size }},
'{{ match }}' /* required */,
'{{ name }}' /* required */,
{{ precedence }} /* required */,
{{ register_interface_ip_with_dns }},
{{ sccm_vpn_boundary_support }},
'{{ service_mode_v2 }}',
'{{ support_url }}',
{{ switch_locked }},
'{{ tunnel_protocol }}',
'{{ virtual_networks }}',
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
- name: devices_policy
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the devices_policy resource.
    - name: allow_mode_switch
      value: {{ allow_mode_switch }}
      description: |
        Whether to allow the user to switch WARP between modes.
      default: false
    - name: allow_updates
      value: {{ allow_updates }}
      description: |
        Whether to receive update notifications when a new version of the client is available.
      default: false
    - name: allowed_to_leave
      value: {{ allowed_to_leave }}
      description: |
        Whether to allow devices to leave the organization.
      default: true
    - name: auto_connect
      value: {{ auto_connect }}
      description: |
        The amount of time in seconds to reconnect after having been disabled.
      default: 0
    - name: captive_portal
      value: {{ captive_portal }}
      description: |
        Turn on the captive portal after the specified amount of time.
      default: 180
    - name: description
      value: "{{ description }}"
      description: |
        A description of the policy.
      default: 
    - name: disable_auto_fallback
      value: {{ disable_auto_fallback }}
      description: |
        If the \`dns_server\` field of a fallback domain is not present, the client will fall back to a best guess of the default/system DNS resolvers unless this policy option is set to \`true\`.
      default: false
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether the policy will be applied to matching devices.
      default: true
    - name: exclude
      description: |
        List of routes excluded in the WARP client's tunnel. Both 'exclude' and 'include' cannot be set in the same request.
      value:
        - address: "{{ address }}"
          description: "{{ description }}"
          host: "{{ host }}"
    - name: exclude_office_ips
      value: {{ exclude_office_ips }}
      description: |
        Whether to add Microsoft IPs to Split Tunnel exclusions.
      default: false
    - name: include
      description: |
        List of routes included in the WARP client's tunnel. Both 'exclude' and 'include' cannot be set in the same request.
      value:
        - address: "{{ address }}"
          description: "{{ description }}"
          host: "{{ host }}"
    - name: lan_allow_minutes
      value: {{ lan_allow_minutes }}
      description: |
        The amount of time in minutes a user is allowed access to their LAN. A value of 0 will allow LAN access until the next WARP reconnection, such as a reboot or a laptop waking from sleep. Note that this field is omitted from the response if null or unset.
    - name: lan_allow_subnet_size
      value: {{ lan_allow_subnet_size }}
      description: |
        The size of the subnet for the local access network. Note that this field is omitted from the response if null or unset.
    - name: match
      value: "{{ match }}"
      description: |
        The wirefilter expression to match devices. Available values: "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.service_token_uuid", "identity.saml_attributes", "network", "os.name", "os.version".
    - name: name
      value: "{{ name }}"
      description: |
        The name of the device settings profile.
    - name: precedence
      value: {{ precedence }}
      description: |
        The precedence of the policy. Lower values indicate higher precedence. Policies will be evaluated in ascending order of this field.
    - name: register_interface_ip_with_dns
      value: {{ register_interface_ip_with_dns }}
      description: |
        Determines if the operating system will register WARP's local interface IP with your on-premises DNS server.
      default: true
    - name: sccm_vpn_boundary_support
      value: {{ sccm_vpn_boundary_support }}
      description: |
        Determines whether the WARP client indicates to SCCM that it is inside a VPN boundary. (Windows only).
      default: false
    - name: service_mode_v2
      value:
        mode: "{{ mode }}"
        port: {{ port }}
    - name: support_url
      value: "{{ support_url }}"
      description: |
        The URL to launch when the Send Feedback button is clicked.
      default: 
    - name: switch_locked
      value: {{ switch_locked }}
      description: |
        Whether to allow the user to turn off the WARP switch and disconnect the client.
      default: false
    - name: tunnel_protocol
      value: "{{ tunnel_protocol }}"
      description: |
        Determines which tunnel protocol to use.
      default: 
    - name: virtual_networks
      description: |
        Virtual network access settings for the device.
      value:
        allowed:
          - "{{ allowed }}"
        default: "{{ default }}"
`}</CodeBlock>

</TabItem>
</Tabs>
