--- 
title: outgoing
hide_title: false
hide_table_of_contents: false
keywords:
  - outgoing
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

Creates, updates, deletes, gets or lists an <code>outgoing</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="outgoing" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.outgoing" /></td></tr>
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

Primary Zone Configuration Details response.

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
    <td> (example: 269d8f4853475ca241c4e730be286b20)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Zone name. (example: www.example.com.)</td>
</tr>
<tr>
    <td><CopyableCode code="checked_time" /></td>
    <td><code>string</code></td>
    <td>The time for a specific event. (example: 2019-10-24T17:09:42.883908+01:00)</td>
</tr>
<tr>
    <td><CopyableCode code="created_time" /></td>
    <td><code>string</code></td>
    <td>The time for a specific event. (example: 2019-10-24T17:09:42.883908+01:00)</td>
</tr>
<tr>
    <td><CopyableCode code="last_transferred_time" /></td>
    <td><code>string</code></td>
    <td>The time for a specific event. (example: 2019-10-24T17:09:42.883908+01:00)</td>
</tr>
<tr>
    <td><CopyableCode code="peers" /></td>
    <td><code>array</code></td>
    <td>A list of peer tags. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="soa_serial" /></td>
    <td><code>number</code></td>
    <td>The serial number of the SOA for the given zone.</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Get primary zone configuration for outgoing zone transfers.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-peers"><code>peers</code></a></td>
    <td></td>
    <td>Update primary zone configuration for outgoing zone transfers.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Delete primary zone configuration for outgoing zone transfers.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Disable outgoing zone transfers for primary zone and clears IXFR backlog of primary zone.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Enable outgoing zone transfers for primary zone.</td>
</tr>
<tr>
    <td><a href="#force_notify"><CopyableCode code="force_notify" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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

Get primary zone configuration for outgoing zone transfers.

```sql
SELECT
id,
name,
checked_time,
created_time,
last_transferred_time,
peers,
soa_serial
FROM cloudflare.dns.outgoing
WHERE zone_id = '{{ zone_id }}' -- required
;
```
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

Update primary zone configuration for outgoing zone transfers.

```sql
REPLACE cloudflare.dns.outgoing
SET 
name = '{{ name }}',
peers = '{{ peers }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND peers = '{{ peers }}' --required
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

Delete primary zone configuration for outgoing zone transfers.

```sql
DELETE FROM cloudflare.dns.outgoing
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disable"
    values={[
        { label: 'disable', value: 'disable' },
        { label: 'enable', value: 'enable' },
        { label: 'force_notify', value: 'force_notify' }
    ]}
>
<TabItem value="disable">

Disable outgoing zone transfers for primary zone and clears IXFR backlog of primary zone.

```sql
EXEC cloudflare.dns.outgoing.disable 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="enable">

Enable outgoing zone transfers for primary zone.

```sql
EXEC cloudflare.dns.outgoing.enable 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="force_notify">

Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.

```sql
EXEC cloudflare.dns.outgoing.force_notify 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
