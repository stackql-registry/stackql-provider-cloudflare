--- 
title: cfd_tunnel_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - cfd_tunnel_connections
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

Creates, updates, deletes, gets or lists a <code>cfd_tunnel_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cfd_tunnel_connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.cfd_tunnel_connections" /></td></tr>
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

List Cloudflare Tunnel connections response

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
    <td>UUID of the Cloudflare Tunnel connection. (example: 1bedc50d-42b3-473c-b108-ff3d10c0d925)</td>
</tr>
<tr>
    <td><CopyableCode code="arch" /></td>
    <td><code>string</code></td>
    <td>The cloudflared OS architecture used to establish this connection. (example: linux_amd64)</td>
</tr>
<tr>
    <td><CopyableCode code="config_version" /></td>
    <td><code>integer</code></td>
    <td>The version of the remote tunnel configuration. Used internally to sync cloudflared with the Zero Trust dashboard.</td>
</tr>
<tr>
    <td><CopyableCode code="conns" /></td>
    <td><code>array</code></td>
    <td>The Cloudflare Tunnel connections between your origin and Cloudflare's edge.</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>Features enabled for the Cloudflare Tunnel.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a></td>
    <td></td>
    <td>Fetches connection details for a Cloudflare Tunnel.</td>
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
<tr id="parameter-tunnel_id">
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare Tunnel ID.</td>
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

Fetches connection details for a Cloudflare Tunnel.

```sql
SELECT
id,
arch,
config_version,
conns,
features,
run_at,
version
FROM cloudflare.zero_trust.cfd_tunnel_connections
WHERE account_id = '{{ account_id }}' -- required
AND tunnel_id = '{{ tunnel_id }}' -- required
;
```
</TabItem>
</Tabs>
