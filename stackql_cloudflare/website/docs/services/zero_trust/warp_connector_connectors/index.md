--- 
title: warp_connector_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - warp_connector_connectors
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

Creates, updates, deletes, gets or lists a <code>warp_connector_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="warp_connector_connectors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.warp_connector_connectors" /></td></tr>
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

Get WARP Connector Tunnel connector response

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
    <td><code>string (uuid)</code></td>
    <td>UUID of the Cloudflare Tunnel connector. (example: 1bedc50d-42b3-473c-b108-ff3d10c0d925)</td>
</tr>
<tr>
    <td><CopyableCode code="arch" /></td>
    <td><code>string</code></td>
    <td>The cloudflared OS architecture used to establish this connection. (example: linux_amd64)</td>
</tr>
<tr>
    <td><CopyableCode code="conns" /></td>
    <td><code>array</code></td>
    <td>The WARP Connector Tunnel connections between your origin and Cloudflare's edge.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>Features enabled for the Cloudflare Tunnel.</td>
</tr>
<tr>
    <td><CopyableCode code="ha_status" /></td>
    <td><code>string</code></td>
    <td>The HA status of a WARP Connector client. (offline, passive, active)</td>
</tr>
<tr>
    <td><CopyableCode code="run_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the tunnel connection was started. (example: 2009-11-10T23:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The cloudflared version used to establish this connection. (example: 2022.7.1)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td></td>
    <td>Fetches connector and connection details for a WARP Connector Tunnel.</td>
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
<tr id="parameter-connector_id">
    <td><CopyableCode code="connector_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-tunnel_id">
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare Tunnel ID.</td>
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

Fetches connector and connection details for a WARP Connector Tunnel.

```sql
SELECT
id,
arch,
conns,
features,
ha_status,
run_at,
version
FROM cloudflare.zero_trust.warp_connector_connectors
WHERE account_id = '{{ account_id }}' -- required
AND tunnel_id = '{{ tunnel_id }}' -- required
AND connector_id = '{{ connector_id }}' -- required
;
```
</TabItem>
</Tabs>
