--- 
title: fleet_status
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_status
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

Creates, updates, deletes, gets or lists a <code>fleet_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fleet_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.fleet_status" /></td></tr>
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

Get the live status of a latest device

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
    <td><CopyableCode code="alwaysOn" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="batteryCharging" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="batteryCycles" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="batteryPct" /></td>
    <td><code>number (float)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="colo" /></td>
    <td><code>string</code></td>
    <td>Cloudflare colo (example: SJC)</td>
</tr>
<tr>
    <td><CopyableCode code="connectionType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cpuPct" /></td>
    <td><code>number (float)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cpuPctByApp" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>Device identifier (UUID v4)</td>
</tr>
<tr>
    <td><CopyableCode code="deviceIpv4" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deviceIpv6" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deviceName" /></td>
    <td><code>string</code></td>
    <td>Device identifier (human readable)</td>
</tr>
<tr>
    <td><CopyableCode code="diskReadBps" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="diskUsagePct" /></td>
    <td><code>number (float)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="diskWriteBps" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dohSubdomain" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="estimatedLossPct" /></td>
    <td><code>number (float)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="firewallEnabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gatewayIpv4" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gatewayIpv6" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="handshakeLatencyMs" /></td>
    <td><code>number (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ispIpv4" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ispIpv6" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metal" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode under which the WARP client is run (example: proxy)</td>
</tr>
<tr>
    <td><CopyableCode code="networkRcvdBps" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="networkSentBps" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="networkSsid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="personEmail" /></td>
    <td><code>string</code></td>
    <td>User contact email address</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>Operating system (example: windows)</td>
</tr>
<tr>
    <td><CopyableCode code="ramAvailableKb" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ramUsedPct" /></td>
    <td><code>number (float)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ramUsedPctByApp" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="registrationId" /></td>
    <td><code>string</code></td>
    <td>Device registration identifier (UUID v4). On multi-user devices, this uniquely identifies a user's registration on the device.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Network status (example: connected)</td>
</tr>
<tr>
    <td><CopyableCode code="switchLocked" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string</code></td>
    <td>Timestamp in ISO format (example: 2023-10-11T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>WARP client version (example: 1.0.0)</td>
</tr>
<tr>
    <td><CopyableCode code="wifiStrengthDbm" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-device_id"><code>device_id</code></a></td>
    <td><a href="#parameter-since_minutes"><code>since_minutes</code></a>, <a href="#parameter-time_now"><code>time_now</code></a>, <a href="#parameter-colo"><code>colo</code></a></td>
    <td>Get the live status of a latest device given device_id from the device_state table</td>
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
    <td>Unique identifier for device</td>
</tr>
<tr id="parameter-colo">
    <td><CopyableCode code="colo" /></td>
    <td><code>string</code></td>
    <td>List of data centers to filter results</td>
</tr>
<tr id="parameter-since_minutes">
    <td><CopyableCode code="since_minutes" /></td>
    <td><code>number</code></td>
    <td>Number of minutes before current time</td>
</tr>
<tr id="parameter-time_now">
    <td><CopyableCode code="time_now" /></td>
    <td><code>string</code></td>
    <td>Number of minutes before current time</td>
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

Get the live status of a latest device given device_id from the device_state table

```sql
SELECT
alwaysOn,
batteryCharging,
batteryCycles,
batteryPct,
colo,
connectionType,
cpuPct,
cpuPctByApp,
deviceId,
deviceIpv4,
deviceIpv6,
deviceName,
diskReadBps,
diskUsagePct,
diskWriteBps,
dohSubdomain,
estimatedLossPct,
firewallEnabled,
gatewayIpv4,
gatewayIpv6,
handshakeLatencyMs,
ispIpv4,
ispIpv6,
metal,
mode,
networkRcvdBps,
networkSentBps,
networkSsid,
personEmail,
platform,
ramAvailableKb,
ramUsedPct,
ramUsedPctByApp,
registrationId,
status,
switchLocked,
timestamp,
version,
wifiStrengthDbm
FROM cloudflare.zero_trust.fleet_status
WHERE account_id = '{{ account_id }}' -- required
AND device_id = '{{ device_id }}' -- required
AND since_minutes = '{{ since_minutes }}'
AND time_now = '{{ time_now }}'
AND colo = '{{ colo }}'
;
```
</TabItem>
</Tabs>
