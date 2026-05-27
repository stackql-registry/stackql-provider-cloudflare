--- 
title: cloudflared
hide_title: false
hide_table_of_contents: false
keywords:
  - cloudflared
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

Creates, updates, deletes, gets or lists a <code>cloudflared</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloudflared" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.cloudflared" /></td></tr>
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

Get a Cloudflare Tunnel response

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
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for a tunnel. (example: blog)</td>
</tr>
<tr>
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>Cloudflare account ID (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="config_src" /></td>
    <td><code>string</code></td>
    <td>Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel on the Zero Trust dashboard. (local, cloudflare) (default: local, example: cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>The Cloudflare Tunnel connections between your origin and Cloudflare's edge. (x-stainless-deprecation-message: This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/&#123;account_id&#125;/&#123;tunnel_type&#125;/&#123;tunnel_id&#125;/connections`)</td>
</tr>
<tr>
    <td><CopyableCode code="conns_active_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the tunnel established at least one connection to Cloudflare's edge. If `null`, the tunnel is inactive. (example: 2009-11-10T23:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="conns_inactive_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the tunnel became inactive (no connections to Cloudflare's edge). If `null`, the tunnel is active. (example: 2009-11-10T23:00:00Z)</td>
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
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata associated with the tunnel.</td>
</tr>
<tr>
    <td><CopyableCode code="remote_config" /></td>
    <td><code>boolean</code></td>
    <td>If `true`, the tunnel can be configured remotely from the Zero Trust dashboard. If `false`, the tunnel must be configured locally on the origin machine. (x-stainless-deprecation-message: Use the config_src field instead.)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge). (inactive, degraded, healthy, down) (example: healthy)</td>
</tr>
<tr>
    <td><CopyableCode code="tun_type" /></td>
    <td><code>string</code></td>
    <td>The type of tunnel. (cfd_tunnel, warp_connector, warp, magic, ip_sec, gre, cni) (example: cfd_tunnel)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Cloudflare Tunnels response

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
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for a tunnel. (example: blog)</td>
</tr>
<tr>
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>Cloudflare account ID (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="config_src" /></td>
    <td><code>string</code></td>
    <td>Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the origin machine. If `cloudflare`, manage the tunnel on the Zero Trust dashboard. (local, cloudflare) (default: local, example: cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>array</code></td>
    <td>The Cloudflare Tunnel connections between your origin and Cloudflare's edge. (x-stainless-deprecation-message: This field will start returning an empty array. To fetch the connections of a given tunnel, please use the dedicated endpoint `/accounts/&#123;account_id&#125;/&#123;tunnel_type&#125;/&#123;tunnel_id&#125;/connections`)</td>
</tr>
<tr>
    <td><CopyableCode code="conns_active_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the tunnel established at least one connection to Cloudflare's edge. If `null`, the tunnel is inactive. (example: 2009-11-10T23:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="conns_inactive_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the tunnel became inactive (no connections to Cloudflare's edge). If `null`, the tunnel is active. (example: 2009-11-10T23:00:00Z)</td>
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
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata associated with the tunnel.</td>
</tr>
<tr>
    <td><CopyableCode code="remote_config" /></td>
    <td><code>boolean</code></td>
    <td>If `true`, the tunnel can be configured remotely from the Zero Trust dashboard. If `false`, the tunnel must be configured locally on the origin machine. (x-stainless-deprecation-message: Use the config_src field instead.)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the tunnel. Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is active and able to serve traffic but in an unhealthy state), `healthy` (tunnel is active and able to serve traffic), or `down` (tunnel can not serve traffic as it has no connections to the Cloudflare Edge). (inactive, degraded, healthy, down) (example: healthy)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a></td>
    <td></td>
    <td>Fetches a single Cloudflare Tunnel.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-is_deleted"><code>is_deleted</code></a>, <a href="#parameter-existed_at"><code>existed_at</code></a>, <a href="#parameter-uuid"><code>uuid</code></a>, <a href="#parameter-was_active_at"><code>was_active_at</code></a>, <a href="#parameter-was_inactive_at"><code>was_inactive_at</code></a>, <a href="#parameter-include_prefix"><code>include_prefix</code></a>, <a href="#parameter-exclude_prefix"><code>exclude_prefix</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a></td>
    <td>Lists and filters Cloudflare Tunnels in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new Cloudflare Tunnel in an account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-tunnel_id"><code>tunnel_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates an existing Cloudflare Tunnel.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a></td>
    <td></td>
    <td>Deletes a Cloudflare Tunnel from an account.</td>
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
<tr id="parameter-exclude_prefix">
    <td><CopyableCode code="exclude_prefix" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-existed_at">
    <td><CopyableCode code="existed_at" /></td>
    <td><code>string (url-encoded-date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-include_prefix">
    <td><CopyableCode code="include_prefix" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-is_deleted">
    <td><CopyableCode code="is_deleted" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-uuid">
    <td><CopyableCode code="uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-was_active_at">
    <td><CopyableCode code="was_active_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-was_inactive_at">
    <td><CopyableCode code="was_inactive_at" /></td>
    <td><code>string (date-time)</code></td>
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

Fetches a single Cloudflare Tunnel.

```sql
SELECT
id,
name,
account_tag,
config_src,
connections,
conns_active_at,
conns_inactive_at,
created_at,
deleted_at,
metadata,
remote_config,
status,
tun_type
FROM cloudflare.zero_trust.cloudflared
WHERE account_id = '{{ account_id }}' -- required
AND tunnel_id = '{{ tunnel_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists and filters Cloudflare Tunnels in an account.

```sql
SELECT
id,
name,
account_tag,
config_src,
connections,
conns_active_at,
conns_inactive_at,
created_at,
deleted_at,
metadata,
remote_config,
status,
tun_type
FROM cloudflare.zero_trust.cloudflared
WHERE account_id = '{{ account_id }}' -- required
AND name = '{{ name }}'
AND is_deleted = '{{ is_deleted }}'
AND existed_at = '{{ existed_at }}'
AND uuid = '{{ uuid }}'
AND was_active_at = '{{ was_active_at }}'
AND was_inactive_at = '{{ was_inactive_at }}'
AND include_prefix = '{{ include_prefix }}'
AND exclude_prefix = '{{ exclude_prefix }}'
AND status = '{{ status }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
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

Creates a new Cloudflare Tunnel in an account.

```sql
INSERT INTO cloudflare.zero_trust.cloudflared (
config_src,
name,
tunnel_secret,
account_id
)
SELECT 
'{{ config_src }}',
'{{ name }}' /* required */,
'{{ tunnel_secret }}',
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
- name: cloudflared
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the cloudflared resource.
    - name: config_src
      value: "{{ config_src }}"
      description: |
        Indicates if this is a locally or remotely configured tunnel. If \`local\`, manage the tunnel using a YAML file on the origin machine. If \`cloudflare\`, manage the tunnel on the Zero Trust dashboard.
      valid_values: ['local', 'cloudflare']
      default: local
    - name: name
      value: "{{ name }}"
      description: |
        A user-friendly name for a tunnel.
    - name: tunnel_secret
      value: "{{ tunnel_secret }}"
      description: |
        Sets the password required to run a locally-managed tunnel. Must be at least 32 bytes and encoded as a base64 string.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Updates an existing Cloudflare Tunnel.

```sql
UPDATE cloudflare.zero_trust.cloudflared
SET 
name = '{{ name }}',
tunnel_secret = '{{ tunnel_secret }}'
WHERE 
tunnel_id = '{{ tunnel_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a Cloudflare Tunnel from an account.

```sql
DELETE FROM cloudflare.zero_trust.cloudflared
WHERE account_id = '{{ account_id }}' --required
AND tunnel_id = '{{ tunnel_id }}' --required
;
```
</TabItem>
</Tabs>
