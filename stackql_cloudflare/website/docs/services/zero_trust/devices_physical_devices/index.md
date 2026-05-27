--- 
title: devices_physical_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_physical_devices
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

Creates, updates, deletes, gets or lists a <code>devices_physical_devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices_physical_devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.devices_physical_devices" /></td></tr>
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

Returns a Device.

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
    <td>The unique ID of the device. (example: fc9ab6ab-3b94-4319-9941-459462b3d73e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the device. (example: My Device)</td>
</tr>
<tr>
    <td><CopyableCode code="hardware_id" /></td>
    <td><code>string</code></td>
    <td>A string that uniquely identifies the hardware or virtual machine (VM).</td>
</tr>
<tr>
    <td><CopyableCode code="active_registrations" /></td>
    <td><code>integer</code></td>
    <td>The number of active registrations for the device. Active registrations are those which haven't been revoked or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="client_version" /></td>
    <td><code>string</code></td>
    <td>Version of the WARP client. (example: 1.0.0)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was created. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was deleted. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="device_type" /></td>
    <td><code>string</code></td>
    <td>The device operating system. (example: linux)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was last seen. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_registration" /></td>
    <td><code>object</code></td>
    <td>The last seen registration for the device.</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_user" /></td>
    <td><code>object</code></td>
    <td>The last user to use the WARP device.</td>
</tr>
<tr>
    <td><CopyableCode code="mac_address" /></td>
    <td><code>string</code></td>
    <td>The device MAC address. (example: f5:01:73:cf:12:23)</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>The device manufacturer. (example: ACME)</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The model name of the device. (example: Mark VII)</td>
</tr>
<tr>
    <td><CopyableCode code="os_version" /></td>
    <td><code>string</code></td>
    <td>The device operating system version number.</td>
</tr>
<tr>
    <td><CopyableCode code="os_version_extra" /></td>
    <td><code>string</code></td>
    <td>Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.</td>
</tr>
<tr>
    <td><CopyableCode code="public_ip" /></td>
    <td><code>string</code></td>
    <td>**Deprecated**: IP information is provided by DEX - see https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/subresources/devices/methods/list/ (example: 1.1.1.1)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The device serial number. (example: ABS765ASD8A)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was last updated. (example: 2025-02-14T13:17:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns a list of Devices.

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
    <td>The unique ID of the device. (example: fc9ab6ab-3b94-4319-9941-459462b3d73e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the device. (example: My Device)</td>
</tr>
<tr>
    <td><CopyableCode code="hardware_id" /></td>
    <td><code>string</code></td>
    <td>A string that uniquely identifies the hardware or virtual machine (VM).</td>
</tr>
<tr>
    <td><CopyableCode code="active_registrations" /></td>
    <td><code>integer</code></td>
    <td>The number of active registrations for the device. Active registrations are those which haven't been revoked or deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="client_version" /></td>
    <td><code>string</code></td>
    <td>Version of the WARP client. (example: 1.0.0)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was created. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was deleted. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="device_type" /></td>
    <td><code>string</code></td>
    <td>The device operating system. (example: linux)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was last seen. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_registration" /></td>
    <td><code>object</code></td>
    <td>The last seen registration for the device.</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_user" /></td>
    <td><code>object</code></td>
    <td>The last user to use the WARP device.</td>
</tr>
<tr>
    <td><CopyableCode code="mac_address" /></td>
    <td><code>string</code></td>
    <td>The device MAC address. (example: f5:01:73:cf:12:23)</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>The device manufacturer. (example: ACME)</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The model name of the device. (example: Mark VII)</td>
</tr>
<tr>
    <td><CopyableCode code="os_version" /></td>
    <td><code>string</code></td>
    <td>The device operating system version number.</td>
</tr>
<tr>
    <td><CopyableCode code="os_version_extra" /></td>
    <td><code>string</code></td>
    <td>Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version.</td>
</tr>
<tr>
    <td><CopyableCode code="public_ip" /></td>
    <td><code>string</code></td>
    <td>**Deprecated**: IP information is provided by DEX - see https://developers.cloudflare.com/api/resources/zero_trust/subresources/dex/subresources/fleet_status/subresources/devices/methods/list/ (example: 1.1.1.1)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The device serial number. (example: ABS765ASD8A)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the device was last updated. (example: 2025-02-14T13:17:00Z)</td>
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
    <td><a href="#parameter-device_id"><code>device_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-include"><code>include</code></a></td>
    <td>Fetches a single WARP device.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-last_seen_user.email"><code>last_seen_user.email</code></a>, <a href="#parameter-seen_after"><code>seen_after</code></a>, <a href="#parameter-seen_before"><code>seen_before</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-active_registrations"><code>active_registrations</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td>Lists WARP devices.</td>
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
<tr id="parameter-active_registrations">
    <td><CopyableCode code="active_registrations" /></td>
    <td><code>string</code></td>
    <td>Include or exclude devices with active registrations. The default is "only" - return only devices with active registrations.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Opaque token indicating the starting position when requesting the next set of records. A cursor value can be obtained from the result_info.cursor field in the response.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>array</code></td>
    <td>Filter by a one or more device IDs.</td>
</tr>
<tr id="parameter-include">
    <td><CopyableCode code="include" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of additional information that should be included in the device response. Supported values are: "last_seen_registration.policy".</td>
</tr>
<tr id="parameter-last_seen_user.email">
    <td><CopyableCode code="last_seen_user.email" /></td>
    <td><code>string</code></td>
    <td>Filter by the last seen user's email.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer (uint64)</code></td>
    <td>The maximum number of devices to return in a single response.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Search by device details.</td>
</tr>
<tr id="parameter-seen_after">
    <td><CopyableCode code="seen_after" /></td>
    <td><code>string</code></td>
    <td>Filter by the last_seen timestamp - returns only devices last seen after this timestamp.</td>
</tr>
<tr id="parameter-seen_before">
    <td><CopyableCode code="seen_before" /></td>
    <td><code>string</code></td>
    <td>Filter by the last_seen timestamp - returns only devices last seen before this timestamp.</td>
</tr>
<tr id="parameter-sort_by">
    <td><CopyableCode code="sort_by" /></td>
    <td><code>string</code></td>
    <td>The device field to order results by.</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>Sort direction.</td>
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

Fetches a single WARP device.

```sql
SELECT
id,
name,
hardware_id,
active_registrations,
client_version,
created_at,
deleted_at,
device_type,
last_seen_at,
last_seen_registration,
last_seen_user,
mac_address,
manufacturer,
model,
os_version,
os_version_extra,
public_ip,
serial_number,
updated_at
FROM cloudflare.zero_trust.devices_physical_devices
WHERE device_id = '{{ device_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND include = '{{ include }}'
;
```
</TabItem>
<TabItem value="list">

Lists WARP devices.

```sql
SELECT
id,
name,
hardware_id,
active_registrations,
client_version,
created_at,
deleted_at,
device_type,
last_seen_at,
last_seen_registration,
last_seen_user,
mac_address,
manufacturer,
model,
os_version,
os_version_extra,
public_ip,
serial_number,
updated_at
FROM cloudflare.zero_trust.devices_physical_devices
WHERE account_id = '{{ account_id }}' -- required
AND cursor = '{{ cursor }}'
AND sort_by = '{{ sort_by }}'
AND sort_order = '{{ sort_order }}'
AND last_seen_user.email = '{{ last_seen_user.email }}'
AND seen_after = '{{ seen_after }}'
AND seen_before = '{{ seen_before }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND active_registrations = '{{ active_registrations }}'
AND id = '{{ id }}'
AND include = '{{ include }}'
;
```
</TabItem>
</Tabs>
