--- 
title: pcaps
hide_title: false
hide_table_of_contents: false
keywords:
  - pcaps
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

Creates, updates, deletes, gets or lists a <code>pcaps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pcaps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.pcaps" /></td></tr>
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

List packet capture requests response.

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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all packet capture requests for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-system"><code>system</code></a>, <a href="#parameter-time_limit"><code>time_limit</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create new PCAP request for account.</td>
</tr>
<tr>
    <td><a href="#create_ownership"><CopyableCode code="create_ownership" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Adds an AWS or GCP bucket to use with full packet captures.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-pcap_id"><code>pcap_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Stop full PCAP.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists all packet capture requests for an account.

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
FROM cloudflare.magic_transit.pcaps
WHERE account_id = '{{ account_id }}' -- required
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

Create new PCAP request for account.

```sql
INSERT INTO cloudflare.magic_transit.pcaps (
filter_v1,
offset_time,
packet_limit,
system,
time_limit,
type,
byte_limit,
colo_name,
destination_conf,
account_id
)
SELECT 
'{{ filter_v1 }}',
'{{ offset_time }}',
{{ packet_limit }},
'{{ system }}' /* required */,
{{ time_limit }} /* required */,
'{{ type }}' /* required */,
{{ byte_limit }},
'{{ colo_name }}',
'{{ destination_conf }}',
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
- name: pcaps
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the pcaps resource.
    - name: filter_v1
      description: |
        The packet capture filter. When this field is empty, all packets are captured.
      value:
        destination_address: "{{ destination_address }}"
        destination_port: {{ destination_port }}
        protocol: {{ protocol }}
        source_address: "{{ source_address }}"
        source_port: {{ source_port }}
    - name: offset_time
      value: "{{ offset_time }}"
      description: |
        The RFC 3339 offset timestamp from which to query backwards for packets. Must be within the last 24h. When this field is empty, defaults to time of request.
    - name: packet_limit
      value: {{ packet_limit }}
      description: |
        The limit of packets contained in a packet capture.
    - name: system
      value: "{{ system }}"
      description: |
        The system used to collect packet captures.
      valid_values: ['magic-transit']
    - name: time_limit
      value: {{ time_limit }}
      description: |
        The packet capture duration in seconds.
    - name: type
      value: "{{ type }}"
      description: |
        The type of packet capture. \`Simple\` captures sampled packets, and \`full\` captures entire payloads and non-sampled packets.
      valid_values: ['simple', 'full']
    - name: byte_limit
      value: {{ byte_limit }}
      description: |
        The maximum number of bytes to capture. This field only applies to \`full\` packet captures.
    - name: colo_name
      value: "{{ colo_name }}"
      description: |
        The name of the data center used for the packet capture. This can be a specific colo (ord02) or a multi-colo name (ORD). This field only applies to \`full\` packet captures.
    - name: destination_conf
      value: "{{ destination_conf }}"
      description: |
        The full URI for the bucket. This field only applies to \`full\` packet captures.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_ownership"
    values={[
        { label: 'create_ownership', value: 'create_ownership' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="create_ownership">

Adds an AWS or GCP bucket to use with full packet captures.

```sql
EXEC cloudflare.magic_transit.pcaps.create_ownership 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="stop">

Stop full PCAP.

```sql
EXEC cloudflare.magic_transit.pcaps.stop 
@pcap_id='{{ pcap_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
