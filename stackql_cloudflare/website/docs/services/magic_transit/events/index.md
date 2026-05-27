--- 
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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

Creates, updates, deletes, gets or lists an <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.events" /></td></tr>
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
    <td><CopyableCode code="e" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="n" /></td>
    <td><code>number</code></td>
    <td>Sequence number, used to order events with the same timestamp</td>
</tr>
<tr>
    <td><CopyableCode code="t" /></td>
    <td><code>number</code></td>
    <td>Time the Event was recorded (seconds since the Unix epoch)</td>
</tr>
<tr>
    <td><CopyableCode code="v" /></td>
    <td><code>string</code></td>
    <td>Version</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="a" /></td>
    <td><code>number</code></td>
    <td>Time the Event was collected (seconds since the Unix epoch)</td>
</tr>
<tr>
    <td><CopyableCode code="k" /></td>
    <td><code>string</code></td>
    <td>Kind</td>
</tr>
<tr>
    <td><CopyableCode code="n" /></td>
    <td><code>number</code></td>
    <td>Sequence number, used to order events with the same timestamp</td>
</tr>
<tr>
    <td><CopyableCode code="t" /></td>
    <td><code>number</code></td>
    <td>Time the Event was recorded (seconds since the Unix epoch)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a>, <a href="#parameter-event_t"><code>event_t</code></a>, <a href="#parameter-event_n"><code>event_n</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td><a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-k"><code>k</code></a></td>
    <td></td>
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
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-event_n">
    <td><CopyableCode code="event_n" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-event_t">
    <td><CopyableCode code="event_t" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-k">
    <td><CopyableCode code="k" /></td>
    <td><code>string</code></td>
    <td>Filter by event kind</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>number</code></td>
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

OK

```sql
SELECT
e,
n,
t,
v
FROM cloudflare.magic_transit.events
WHERE account_id = '{{ account_id }}' -- required
AND connector_id = '{{ connector_id }}' -- required
AND event_t = '{{ event_t }}' -- required
AND event_n = '{{ event_n }}' -- required
;
```
</TabItem>
<TabItem value="list">

OK

```sql
SELECT
a,
k,
n,
t
FROM cloudflare.magic_transit.events
WHERE account_id = '{{ account_id }}' -- required
AND connector_id = '{{ connector_id }}' -- required
AND from = '{{ from }}'
AND to = '{{ to }}'
AND limit = '{{ limit }}'
AND cursor = '{{ cursor }}'
AND k = '{{ k }}'
;
```
</TabItem>
</Tabs>
