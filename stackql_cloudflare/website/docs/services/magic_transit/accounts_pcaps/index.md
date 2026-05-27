--- 
title: accounts_pcaps
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_pcaps
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

Creates, updates, deletes, gets or lists an <code>accounts_pcaps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts_pcaps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.accounts_pcaps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get PCAP request response.

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
    <td>The ID for the packet capture. (example: 66802ca5668e47a2b82c2e6746e45037)</td>
</tr>
<tr>
    <td><CopyableCode code="colo_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data center used for the packet capture. This can be a specific colo (ord02) or a multi-colo name (ORD). This field only applies to `full` packet captures. (example: ord02)</td>
</tr>
<tr>
    <td><CopyableCode code="byte_limit" /></td>
    <td><code>number</code></td>
    <td>The maximum number of bytes to capture. This field only applies to `full` packet captures.</td>
</tr>
<tr>
    <td><CopyableCode code="destination_conf" /></td>
    <td><code>string</code></td>
    <td>The full URI for the bucket. This field only applies to `full` packet captures. (example: s3://pcaps-bucket?region=us-east-1)</td>
</tr>
<tr>
    <td><CopyableCode code="error_message" /></td>
    <td><code>string</code></td>
    <td>An error message that describes why the packet capture failed. This field only applies to `full` packet captures. (example: No packets matched the filter in the time limit given. Please modify the filter or try again.)</td>
</tr>
<tr>
    <td><CopyableCode code="filter_v1" /></td>
    <td><code>object</code></td>
    <td>The packet capture filter. When this field is empty, all packets are captured.</td>
</tr>
<tr>
    <td><CopyableCode code="offset_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The RFC 3339 offset timestamp from which to query backwards for packets. Must be within the last 24h. When this field is empty, defaults to time of request. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="packets_captured" /></td>
    <td><code>integer</code></td>
    <td>The number of packets captured.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the packet capture request. (unknown, success, pending, running, conversion_pending, conversion_running, complete, failed) (example: success)</td>
</tr>
<tr>
    <td><CopyableCode code="stop_requested" /></td>
    <td><code>string (date-time)</code></td>
    <td>The RFC 3339 timestamp when stopping the packet capture was requested. This field only applies to `full` packet captures.</td>
</tr>
<tr>
    <td><CopyableCode code="submitted" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp when the packet capture was created. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="system" /></td>
    <td><code>string</code></td>
    <td>The system used to collect packet captures. (magic-transit) (example: magic-transit)</td>
</tr>
<tr>
    <td><CopyableCode code="time_limit" /></td>
    <td><code>number</code></td>
    <td>The packet capture duration in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of packet capture. `Simple` captures sampled packets, and `full` captures entire payloads and non-sampled packets. (simple, full) (example: simple)</td>
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
    <td><a href="#parameter-pcap_id"><code>pcap_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get information for a PCAP request by id.</td>
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
<tr id="parameter-pcap_id">
    <td><CopyableCode code="pcap_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get information for a PCAP request by id.

```sql
SELECT
id,
colo_name,
byte_limit,
destination_conf,
error_message,
filter_v1,
offset_time,
packets_captured,
status,
stop_requested,
submitted,
system,
time_limit,
type
FROM cloudflare.magic_transit.accounts_pcaps
WHERE pcap_id = '{{ pcap_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
