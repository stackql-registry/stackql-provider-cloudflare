--- 
title: peers
hide_title: false
hide_table_of_contents: false
keywords:
  - peers
  - dns
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

Creates, updates, deletes, gets or lists a <code>peers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="peers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.peers" /></td></tr>
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

Peer Details response.

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
    <td> (example: 23ff594956f20c2a721606e94745a8aa)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the peer. (example: my-peer-1)</td>
</tr>
<tr>
    <td><CopyableCode code="tsig_id" /></td>
    <td><code>string</code></td>
    <td>TSIG authentication will be used for zone transfer if configured. (example: 69cd1e104af3e6ed3cb344f263fd0d5a)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to. (example: 192.0.2.53)</td>
</tr>
<tr>
    <td><CopyableCode code="ixfr_enable" /></td>
    <td><code>boolean</code></td>
    <td>Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>number</code></td>
    <td>DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Peers response.

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
    <td> (example: 23ff594956f20c2a721606e94745a8aa)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the peer. (example: my-peer-1)</td>
</tr>
<tr>
    <td><CopyableCode code="tsig_id" /></td>
    <td><code>string</code></td>
    <td>TSIG authentication will be used for zone transfer if configured. (example: 69cd1e104af3e6ed3cb344f263fd0d5a)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to. (example: 192.0.2.53)</td>
</tr>
<tr>
    <td><CopyableCode code="ixfr_enable" /></td>
    <td><code>boolean</code></td>
    <td>Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>number</code></td>
    <td>DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.</td>
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
    <td><a href="#parameter-peer_id"><code>peer_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get Peer.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List Peers.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create Peer.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-peer_id"><code>peer_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Modify Peer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-peer_id"><code>peer_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete Peer.</td>
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
<tr id="parameter-peer_id">
    <td><CopyableCode code="peer_id" /></td>
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

Get Peer.

```sql
SELECT
id,
name,
tsig_id,
ip,
ixfr_enable,
port
FROM cloudflare.dns.peers
WHERE peer_id = '{{ peer_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Peers.

```sql
SELECT
id,
name,
tsig_id,
ip,
ixfr_enable,
port
FROM cloudflare.dns.peers
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

Create Peer.

```sql
INSERT INTO cloudflare.dns.peers (
name,
account_id
)
SELECT 
'{{ name }}' /* required */,
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
- name: peers
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the peers resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the peer.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Modify Peer.

```sql
REPLACE cloudflare.dns.peers
SET 
ip = '{{ ip }}',
ixfr_enable = {{ ixfr_enable }},
name = '{{ name }}',
port = {{ port }},
tsig_id = '{{ tsig_id }}'
WHERE 
peer_id = '{{ peer_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
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

Delete Peer.

```sql
DELETE FROM cloudflare.dns.peers
WHERE peer_id = '{{ peer_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
