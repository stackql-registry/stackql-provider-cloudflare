--- 
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - user
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.user.events" /></td></tr>
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

List Healthcheck Events response.

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
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pool" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td></td>
    <td><a href="#parameter-until"><code>until</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-origin_healthy"><code>origin_healthy</code></a>, <a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-pool_healthy"><code>pool_healthy</code></a></td>
    <td>List origin health changes.</td>
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
<tr id="parameter-origin_healthy">
    <td><CopyableCode code="origin_healthy" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-origin_name">
    <td><CopyableCode code="origin_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-pool_healthy">
    <td><CopyableCode code="pool_healthy" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
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

List origin health changes.

```sql
SELECT
id,
origins,
pool,
timestamp
FROM cloudflare.user.events
WHERE until = '{{ until }}'
AND pool_name = '{{ pool_name }}'
AND origin_healthy = '{{ origin_healthy }}'
AND pool_id = '{{ pool_id }}'
AND since = '{{ since }}'
AND origin_name = '{{ origin_name }}'
AND pool_healthy = '{{ pool_healthy }}'
;
```
</TabItem>
</Tabs>
