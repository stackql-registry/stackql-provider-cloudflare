--- 
title: incoming
hide_title: false
hide_table_of_contents: false
keywords:
  - incoming
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

Creates, updates, deletes, gets or lists an <code>incoming</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="incoming" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.incoming" /></td></tr>
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

Secondary Zone Configuration Details response.

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
    <td><CopyableCode code="auto_refresh_seconds" /></td>
    <td><code>number</code></td>
    <td>How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not applicable for primary zones.</td>
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
    <td><CopyableCode code="modified_time" /></td>
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
    <td>Get secondary zone configuration for incoming zone transfers.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-peers"><code>peers</code></a>, <a href="#parameter-auto_refresh_seconds"><code>auto_refresh_seconds</code></a></td>
    <td></td>
    <td>Create secondary zone configuration for incoming zone transfers.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-peers"><code>peers</code></a>, <a href="#parameter-auto_refresh_seconds"><code>auto_refresh_seconds</code></a></td>
    <td></td>
    <td>Update secondary zone configuration for incoming zone transfers.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Delete secondary zone configuration for incoming zone transfers.</td>
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

Get secondary zone configuration for incoming zone transfers.

```sql
SELECT
id,
name,
auto_refresh_seconds,
checked_time,
created_time,
modified_time,
peers,
soa_serial
FROM cloudflare.dns.incoming
WHERE zone_id = '{{ zone_id }}' -- required
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

Create secondary zone configuration for incoming zone transfers.

```sql
INSERT INTO cloudflare.dns.incoming (
auto_refresh_seconds,
name,
peers,
zone_id
)
SELECT 
{{ auto_refresh_seconds }} /* required */,
'{{ name }}' /* required */,
'{{ peers }}' /* required */,
'{{ zone_id }}'
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
- name: incoming
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the incoming resource.
    - name: auto_refresh_seconds
      value: {{ auto_refresh_seconds }}
      description: |
        How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not applicable for primary zones.
      default: 86400
    - name: name
      value: "{{ name }}"
      description: |
        Zone name.
    - name: peers
      value:
        - "{{ peers }}"
      description: |
        A list of peer tags.
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

Update secondary zone configuration for incoming zone transfers.

```sql
REPLACE cloudflare.dns.incoming
SET 
auto_refresh_seconds = {{ auto_refresh_seconds }},
name = '{{ name }}',
peers = '{{ peers }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND peers = '{{ peers }}' --required
AND auto_refresh_seconds = '{{ auto_refresh_seconds }}' --required
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

Delete secondary zone configuration for incoming zone transfers.

```sql
DELETE FROM cloudflare.dns.incoming
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
