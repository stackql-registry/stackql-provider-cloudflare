--- 
title: cfd_tunnel
hide_title: false
hide_table_of_contents: false
keywords:
  - cfd_tunnel
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

Creates, updates, deletes, gets or lists a <code>cfd_tunnel</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cfd_tunnel" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.cfd_tunnel" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#delete_connections"><CopyableCode code="delete_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a></td>
    <td><a href="#parameter-client_id"><code>client_id</code></a></td>
    <td>Removes a connection (aka Cloudflare Tunnel Connector) from a Cloudflare Tunnel independently of its current state. If no connector id (client_id) is provided all connectors will be removed. We recommend running this command after rotating tokens.</td>
</tr>
<tr>
    <td><a href="#create_management"><CopyableCode code="create_management" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a>, <a href="#parameter-resources"><code>resources</code></a></td>
    <td></td>
    <td>Gets a management token used to access the management resources (i.e. Streaming Logs) of a tunnel.</td>
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
<tr id="parameter-client_id">
    <td><CopyableCode code="client_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="delete_connections"
    values={[
        { label: 'delete_connections', value: 'delete_connections' },
        { label: 'create_management', value: 'create_management' }
    ]}
>
<TabItem value="delete_connections">

Removes a connection (aka Cloudflare Tunnel Connector) from a Cloudflare Tunnel independently of its current state. If no connector id (client_id) is provided all connectors will be removed. We recommend running this command after rotating tokens.

```sql
EXEC cloudflare.zero_trust.cfd_tunnel.delete_connections 
@account_id='{{ account_id }}' --required, 
@tunnel_id='{{ tunnel_id }}' --required, 
@client_id='{{ client_id }}'
;
```
</TabItem>
<TabItem value="create_management">

Gets a management token used to access the management resources (i.e. Streaming Logs) of a tunnel.

```sql
EXEC cloudflare.zero_trust.cfd_tunnel.create_management 
@account_id='{{ account_id }}' --required, 
@tunnel_id='{{ tunnel_id }}' --required 
@@json=
'{
"resources": "{{ resources }}"
}'
;
```
</TabItem>
</Tabs>
