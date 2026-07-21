--- 
title: cache_reserve
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_reserve
  - zones
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

Creates, updates, deletes, gets or lists a <code>cache_reserve</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cache_reserve" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.cache_reserve" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_clear_status"
    values={[
        { label: 'get_clear_status', value: 'get_clear_status' }
    ]}
>
<TabItem value="get_clear_status">

Get Cache Reserve Clear response.

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
    <td>ID of the zone setting. (cache_reserve_clear) (example: cache_reserve_clear)</td>
</tr>
<tr>
    <td><CopyableCode code="end_ts" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the latest Cache Reserve Clear operation completed. (example: 2023-10-02T12:00:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time this setting was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="start_ts" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time that the latest Cache Reserve Clear operation started. (example: 2023-10-02T10:00:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Cache Reserve Clear operation. (In-progress, Completed) (example: In-progress)</td>
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
    <td><a href="#get_clear_status"><CopyableCode code="get_clear_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.</td>
</tr>
<tr>
    <td><a href="#start_clear"><CopyableCode code="start_clear" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.</td>
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
    defaultValue="get_clear_status"
    values={[
        { label: 'get_clear_status', value: 'get_clear_status' }
    ]}
>
<TabItem value="get_clear_status">

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

```sql
SELECT
id,
end_ts,
modified_on,
start_ts,
state
FROM cloudflare.zones.cache_reserve
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_clear"
    values={[
        { label: 'start_clear', value: 'start_clear' }
    ]}
>
<TabItem value="start_clear">

You can use Cache Reserve Clear to clear your Cache Reserve, but you must first disable Cache Reserve. In most cases, this will be accomplished within 24 hours. You cannot re-enable Cache Reserve while this process is ongoing. Keep in mind that you cannot undo or cancel this operation.

```sql
EXEC cloudflare.zones.cache_reserve.start_clear 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
