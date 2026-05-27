--- 
title: cf_interconnects
hide_title: false
hide_table_of_contents: false
keywords:
  - cf_interconnects
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

Creates, updates, deletes, gets or lists a <code>cf_interconnects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cf_interconnects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.cf_interconnects" /></td></tr>
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

List interconnect Details response

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
    <td><CopyableCode code="interconnect" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List interconnects response

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
    <td>Identifier (example: c4a7362d577a6c3019a474fd6f485821)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the interconnect. The name cannot share a name with other tunnels. (example: pni_ord)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_port_reservation_id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: c4a7362d577a6c3019a474fd6f485821)</td>
</tr>
<tr>
    <td><CopyableCode code="colo_name" /></td>
    <td><code>string</code></td>
    <td>The name of the interconnect. The name cannot share a name with other tunnels. (example: pni_ord)</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_return_routing" /></td>
    <td><code>boolean</code></td>
    <td>True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the `coupler_integration` account flag to be enabled; requests setting this to `true` without that flag will be rejected.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the tunnel was created. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description of the interconnect. (example: Tunnel for Interconnect to ORD)</td>
</tr>
<tr>
    <td><CopyableCode code="gre" /></td>
    <td><code>object</code></td>
    <td>The configuration specific to GRE interconnects.</td>
</tr>
<tr>
    <td><CopyableCode code="health_check" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="interface_address" /></td>
    <td><code>string</code></td>
    <td>A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side of the tunnel. Select the subnet from the following private IP space: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255. (example: 192.0.2.0/31)</td>
</tr>
<tr>
    <td><CopyableCode code="interface_address6" /></td>
    <td><code>string</code></td>
    <td>A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127 (example: 2606:54c1:7:0:a9fe:12d2:1:200/127)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the tunnel was last modified. (example: 2017-06-14T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mtu" /></td>
    <td><code>integer</code></td>
    <td>The Maximum Transmission Unit (MTU) in bytes for the interconnect. The minimum value is 576.</td>
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
    <td><a href="#parameter-cf_interconnect_id"><code>cf_interconnect_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Lists details for a specific interconnect.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Lists interconnects associated with an account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-cf_interconnect_id"><code>cf_interconnect_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Updates a specific interconnect associated with an account. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.</td>
</tr>
<tr>
    <td><a href="#bulk_update"><CopyableCode code="bulk_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Updates multiple interconnects associated with an account. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.</td>
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
<tr id="parameter-cf_interconnect_id">
    <td><CopyableCode code="cf_interconnect_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-magic-new-hc-target">
    <td><CopyableCode code="x-magic-new-hc-target" /></td>
    <td><code>boolean</code></td>
    <td>If true, the health check target in the request and response bodies will be presented using the new object format. Defaults to false.</td>
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

Lists details for a specific interconnect.

```sql
SELECT
interconnect
FROM cloudflare.magic_transit.cf_interconnects
WHERE cf_interconnect_id = '{{ cf_interconnect_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND x-magic-new-hc-target = '{{ x-magic-new-hc-target }}'
;
```
</TabItem>
<TabItem value="list">

Lists interconnects associated with an account.

```sql
SELECT
id,
name,
virtual_port_reservation_id,
colo_name,
automatic_return_routing,
created_on,
description,
gre,
health_check,
interface_address,
interface_address6,
modified_on,
mtu
FROM cloudflare.magic_transit.cf_interconnects
WHERE account_id = '{{ account_id }}' -- required
AND x-magic-new-hc-target = '{{ x-magic-new-hc-target }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'bulk_update', value: 'bulk_update' }
    ]}
>
<TabItem value="update">

Updates a specific interconnect associated with an account. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

```sql
REPLACE cloudflare.magic_transit.cf_interconnects
SET 
automatic_return_routing = {{ automatic_return_routing }},
description = '{{ description }}',
gre = '{{ gre }}',
health_check = '{{ health_check }}',
interface_address = '{{ interface_address }}',
interface_address6 = '{{ interface_address6 }}',
mtu = {{ mtu }},
name = '{{ name }}'
WHERE 
cf_interconnect_id = '{{ cf_interconnect_id }}' --required
AND account_id = '{{ account_id }}' --required
AND x-magic-new-hc-target = {{ x-magic-new-hc-target}}
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="bulk_update">

Updates multiple interconnects associated with an account. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

```sql
REPLACE cloudflare.magic_transit.cf_interconnects
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND x-magic-new-hc-target = {{ x-magic-new-hc-target}}
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
