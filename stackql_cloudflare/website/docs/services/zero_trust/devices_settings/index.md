--- 
title: devices_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_settings
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

Creates, updates, deletes, gets or lists a <code>devices_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.devices_settings" /></td></tr>
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

Get device settings for a Zero Trust account response.

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
    <td><CopyableCode code="disable_for_time" /></td>
    <td><code>number</code></td>
    <td>Sets the time limit, in seconds, that a user can use an override code to bypass WARP.</td>
</tr>
<tr>
    <td><CopyableCode code="external_emergency_signal_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Controls whether the external emergency disconnect feature is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="external_emergency_signal_fingerprint" /></td>
    <td><code>string</code></td>
    <td>The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server certificate for the external_emergency_signal_url. If provided, the WARP client will use this value to verify the server's identity. The device will ignore any response if the server's certificate fingerprint does not exactly match this value. (example: abcd1234567890abcd1234567890abcd1234567890abcd1234567890abcd1234)</td>
</tr>
<tr>
    <td><CopyableCode code="external_emergency_signal_interval" /></td>
    <td><code>string</code></td>
    <td>The interval at which the WARP client fetches the emergency disconnect signal, formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds. (example: 5m)</td>
</tr>
<tr>
    <td><CopyableCode code="external_emergency_signal_url" /></td>
    <td><code>string</code></td>
    <td>The HTTPS URL from which to fetch the emergency disconnect signal. Must use HTTPS and have an IPv4 or IPv6 address as the host. (example: https://192.0.2.1/signal)</td>
</tr>
<tr>
    <td><CopyableCode code="gateway_proxy_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable gateway proxy filtering on TCP.</td>
</tr>
<tr>
    <td><CopyableCode code="gateway_udp_proxy_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable gateway proxy filtering on UDP.</td>
</tr>
<tr>
    <td><CopyableCode code="root_certificate_installation_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Enable installation of cloudflare managed root certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="use_zt_virtual_ip" /></td>
    <td><code>boolean</code></td>
    <td>Enable using CGNAT virtual IPv4.</td>
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
    <td>Describes the current device settings for a Zero Trust account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Patches the current device settings for a Zero Trust account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates the current device settings for a Zero Trust account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Resets the current device settings for a Zero Trust account.</td>
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

Describes the current device settings for a Zero Trust account.

```sql
SELECT
disable_for_time,
external_emergency_signal_enabled,
external_emergency_signal_fingerprint,
external_emergency_signal_interval,
external_emergency_signal_url,
gateway_proxy_enabled,
gateway_udp_proxy_enabled,
root_certificate_installation_enabled,
use_zt_virtual_ip
FROM cloudflare.zero_trust.devices_settings
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

Patches the current device settings for a Zero Trust account.

```sql
UPDATE cloudflare.zero_trust.devices_settings
SET 
disable_for_time = {{ disable_for_time }},
external_emergency_signal_enabled = {{ external_emergency_signal_enabled }},
external_emergency_signal_fingerprint = '{{ external_emergency_signal_fingerprint }}',
external_emergency_signal_interval = '{{ external_emergency_signal_interval }}',
external_emergency_signal_url = '{{ external_emergency_signal_url }}',
gateway_proxy_enabled = {{ gateway_proxy_enabled }},
gateway_udp_proxy_enabled = {{ gateway_udp_proxy_enabled }},
root_certificate_installation_enabled = {{ root_certificate_installation_enabled }},
use_zt_virtual_ip = {{ use_zt_virtual_ip }}
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


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the current device settings for a Zero Trust account.

```sql
REPLACE cloudflare.zero_trust.devices_settings
SET 
disable_for_time = {{ disable_for_time }},
external_emergency_signal_enabled = {{ external_emergency_signal_enabled }},
external_emergency_signal_fingerprint = '{{ external_emergency_signal_fingerprint }}',
external_emergency_signal_interval = '{{ external_emergency_signal_interval }}',
external_emergency_signal_url = '{{ external_emergency_signal_url }}',
gateway_proxy_enabled = {{ gateway_proxy_enabled }},
gateway_udp_proxy_enabled = {{ gateway_udp_proxy_enabled }},
root_certificate_installation_enabled = {{ root_certificate_installation_enabled }},
use_zt_virtual_ip = {{ use_zt_virtual_ip }}
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Resets the current device settings for a Zero Trust account.

```sql
DELETE FROM cloudflare.zero_trust.devices_settings
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
