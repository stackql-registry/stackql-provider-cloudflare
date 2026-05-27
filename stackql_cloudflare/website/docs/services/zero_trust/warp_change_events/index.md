--- 
title: warp_change_events
hide_title: false
hide_table_of_contents: false
keywords:
  - warp_change_events
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

Creates, updates, deletes, gets or lists a <code>warp_change_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="warp_change_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.warp_change_events" /></td></tr>
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

success response

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
    <td><CopyableCode code="device_id" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="registration_id" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The account name.</td>
</tr>
<tr>
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>The public account identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="device_registration" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="from" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname of the machine the event is from</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The serial number of the machine the event is from</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string</code></td>
    <td>Timestamp in ISO format (example: 2023-10-11T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="to" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="toggle" /></td>
    <td><code>string</code></td>
    <td>The state of the WARP toggle. (on, off)</td>
</tr>
<tr>
    <td><CopyableCode code="user_email" /></td>
    <td><code>string</code></td>
    <td>Email tied to the device</td>
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
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-toggle"><code>toggle</code></a>, <a href="#parameter-config_name"><code>config_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a></td>
    <td>List WARP configuration and enablement toggle change events by device.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Filter events by account name.</td>
</tr>
<tr id="parameter-config_name">
    <td><CopyableCode code="config_name" /></td>
    <td><code>string</code></td>
    <td>Filter events by WARP configuration name changed from or to. Applicable to type='config' events only.</td>
</tr>
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>string</code></td>
    <td>Start time for the query in ISO (RFC3339 - ISO 8601) format</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td>Page number of paginated results</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Number of items per page</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>Sort response by event timestamp.</td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>string</code></td>
    <td>End time for the query in ISO (RFC3339 - ISO 8601) format</td>
</tr>
<tr id="parameter-toggle">
    <td><CopyableCode code="toggle" /></td>
    <td><code>string</code></td>
    <td>Filter events by type toggle value. Applicable to type='toggle' events only.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Filter events by type 'config' or 'toggle'</td>
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

List WARP configuration and enablement toggle change events by device.

```sql
SELECT
device_id,
registration_id,
account_name,
account_tag,
device_registration,
from,
hostname,
serial_number,
timestamp,
to,
toggle,
user_email
FROM cloudflare.zero_trust.warp_change_events
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND from = '{{ from }}'
AND to = '{{ to }}'
AND type = '{{ type }}'
AND toggle = '{{ toggle }}'
AND config_name = '{{ config_name }}'
AND account_name = '{{ account_name }}'
AND sort_order = '{{ sort_order }}'
;
```
</TabItem>
</Tabs>
