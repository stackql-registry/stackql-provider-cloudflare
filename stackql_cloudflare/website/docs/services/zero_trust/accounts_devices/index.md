--- 
title: accounts_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_devices
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

Creates, updates, deletes, gets or lists an <code>accounts_devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts_devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.accounts_devices" /></td></tr>
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

Get device details response.

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
    <td>Registration ID. Equal to Device ID except for accounts which enabled [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/). (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The device name. (example: My mobile device)</td>
</tr>
<tr>
    <td><CopyableCode code="gateway_device_id" /></td>
    <td><code>string</code></td>
    <td> (example: PD33E90AXfafe14643cbbbc-4a0ed4fc8415Q)</td>
</tr>
<tr>
    <td><CopyableCode code="account" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device was created. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted" /></td>
    <td><code>boolean</code></td>
    <td>True if the device was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="device_type" /></td>
    <td><code>string</code></td>
    <td> (example: windows)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>IPv4 or IPv6 address. (example: 1.1.1.1)</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The device's public key. (example: yek0SUYoOQ10vMGsIYAevozXUQpQtNFJFfFGqER/BGc=)</td>
</tr>
<tr>
    <td><CopyableCode code="key_type" /></td>
    <td><code>string</code></td>
    <td>Type of the key. (example: curve25519)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device last connected to Cloudflare services. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mac_address" /></td>
    <td><code>string</code></td>
    <td>The device mac address. (example: 00-00-5E-00-53-00)</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The device model name. (example: MyPhone(pro-X))</td>
</tr>
<tr>
    <td><CopyableCode code="os_version" /></td>
    <td><code>string</code></td>
    <td>The operating system version. (example: 10.0.0)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The device serial number. (example: EXAMPLEHMD6R)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_type" /></td>
    <td><code>string</code></td>
    <td>Type of the tunnel connection used. (example: masque)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device was updated. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The WARP client version. (example: 1.0.0)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List devices response.

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
    <td>Registration ID. Equal to Device ID except for accounts which enabled [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/). (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The device name. (example: My mobile device)</td>
</tr>
<tr>
    <td><CopyableCode code="os_distro_name" /></td>
    <td><code>string</code></td>
    <td>The Linux distro name. (example: ubuntu)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device was created. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted" /></td>
    <td><code>boolean</code></td>
    <td>True if the device was deleted.</td>
</tr>
<tr>
    <td><CopyableCode code="device_type" /></td>
    <td><code>string</code></td>
    <td> (windows, mac, linux, android, ios, chromeos) (example: windows)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>IPv4 or IPv6 address. (example: 1.1.1.1)</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The device's public key. (example: yek0SUYoOQ10vMGsIYAevozXUQpQtNFJFfFGqER/BGc=)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device last connected to Cloudflare services. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mac_address" /></td>
    <td><code>string</code></td>
    <td>The device mac address. (example: 00-00-5E-00-53-00)</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>The device manufacturer name. (example: My phone corp)</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The device model name. (example: MyPhone(pro-X))</td>
</tr>
<tr>
    <td><CopyableCode code="os_distro_revision" /></td>
    <td><code>string</code></td>
    <td>The Linux distro revision. (example: 1.0.0)</td>
</tr>
<tr>
    <td><CopyableCode code="os_version" /></td>
    <td><code>string</code></td>
    <td>The operating system version. (example: 10.0.0)</td>
</tr>
<tr>
    <td><CopyableCode code="os_version_extra" /></td>
    <td><code>string</code></td>
    <td>Additional operating system version details. For Windows, the UBR (Update Build Revision). For Mac or iOS, the Product Version Extra. For Linux, the distribution name and version. (example: (a) or 6889 or Ubuntu 24.04)</td>
</tr>
<tr>
    <td><CopyableCode code="revoked_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device was revoked. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The device serial number. (example: EXAMPLEHMD6R)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the device was updated. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The WARP client version. (example: 1.0.0)</td>
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
    <td></td>
    <td>Fetches a single WARP device. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account. **Deprecated**: please use one of the following endpoints instead: - GET /accounts/&#123;account_id&#125;/devices/physical-devices/&#123;device_id&#125; - GET /accounts/&#123;account_id&#125;/devices/registrations/&#123;registration_id&#125;</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List WARP devices. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account. **Deprecated**: please use one of the following endpoints instead: - GET /accounts/&#123;account_id&#125;/devices/physical-devices - GET /accounts/&#123;account_id&#125;/devices/registrations</td>
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

Fetches a single WARP device. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account. **Deprecated**: please use one of the following endpoints instead: - GET /accounts/&#123;account_id&#125;/devices/physical-devices/&#123;device_id&#125; - GET /accounts/&#123;account_id&#125;/devices/registrations/&#123;registration_id&#125;

```sql
SELECT
id,
name,
gateway_device_id,
account,
created,
deleted,
device_type,
ip,
key,
key_type,
last_seen,
mac_address,
model,
os_version,
serial_number,
tunnel_type,
updated,
user,
version
FROM cloudflare.zero_trust.accounts_devices
WHERE device_id = '{{ device_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List WARP devices. Not supported when [multi-user mode](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/mdm-deployment/windows-multiuser/) is enabled for the account. **Deprecated**: please use one of the following endpoints instead: - GET /accounts/&#123;account_id&#125;/devices/physical-devices - GET /accounts/&#123;account_id&#125;/devices/registrations

```sql
SELECT
id,
name,
os_distro_name,
created,
deleted,
device_type,
ip,
key,
last_seen,
mac_address,
manufacturer,
model,
os_distro_revision,
os_version,
os_version_extra,
revoked_at,
serial_number,
updated,
user,
version
FROM cloudflare.zero_trust.accounts_devices
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
