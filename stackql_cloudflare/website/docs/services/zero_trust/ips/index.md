--- 
title: ips
hide_title: false
hide_table_of_contents: false
keywords:
  - ips
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

Creates, updates, deletes, gets or lists an <code>ips</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ips" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.ips" /></td></tr>
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

Get tunnel route by IP response

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
    <td>UUID of the route. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the virtual network. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for a tunnel. (example: blog)</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_network_name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the virtual network. (example: us-east-1-vpc)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional remark describing the route. (default: , example: Example comment for this route.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was created. (example: 2021-01-25T18:22:34.317854Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was deleted. If `null`, the resource has not been deleted. (example: 2009-11-10T23:00:00.000000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td>The private IPv4 or IPv6 range connected by the route, in CIDR notation. (example: 172.16.0.0/16)</td>
</tr>
<tr>
    <td><CopyableCode code="tun_type" /></td>
    <td><code>string</code></td>
    <td>The type of tunnel. (cfd_tunnel, warp_connector, warp, magic, ip_sec, gre, cni) (example: cfd_tunnel)</td>
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
    <td><a href="#parameter-ip"><code>ip</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-virtual_network_id"><code>virtual_network_id</code></a>, <a href="#parameter-default_virtual_network_fallback"><code>default_virtual_network_fallback</code></a></td>
    <td>Fetches routes that contain the given IP address.</td>
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
<tr id="parameter-ip">
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-default_virtual_network_fallback">
    <td><CopyableCode code="default_virtual_network_fallback" /></td>
    <td><code>boolean</code></td>
    <td>When the virtual_network_id parameter is not provided the request filter will default search routes that are in the default virtual network for the account. If this parameter is set to false, the search will include routes that do not have a virtual network.</td>
</tr>
<tr id="parameter-virtual_network_id">
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
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

Fetches routes that contain the given IP address.

```sql
SELECT
id,
tunnel_id,
virtual_network_id,
tunnel_name,
virtual_network_name,
comment,
created_at,
deleted_at,
network,
tun_type
FROM cloudflare.zero_trust.ips
WHERE ip = '{{ ip }}' -- required
AND account_id = '{{ account_id }}' -- required
AND virtual_network_id = '{{ virtual_network_id }}'
AND default_virtual_network_fallback = '{{ default_virtual_network_fallback }}'
;
```
</TabItem>
</Tabs>
