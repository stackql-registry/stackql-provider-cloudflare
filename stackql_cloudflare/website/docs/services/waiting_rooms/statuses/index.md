--- 
title: statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - statuses
  - waiting_rooms
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

Creates, updates, deletes, gets or lists a <code>statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="statuses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.waiting_rooms.statuses" /></td></tr>
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

Get waiting room status response

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
    <td><CopyableCode code="event_id" /></td>
    <td><code>string</code></td>
    <td> (example: 25756b2dfe6e378a06b033b670413757)</td>
</tr>
<tr>
    <td><CopyableCode code="estimated_queued_users" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="estimated_total_active_users" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_estimated_time_minutes" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (event_prequeueing, not_queueing, queueing, suspended) (example: queueing)</td>
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
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the status of a configured waiting room. Response fields include: 1. `status`: String indicating the status of the waiting room. The possible status are: - **not_queueing** indicates that the configured thresholds have not been met and all users are going through to the origin. - **queueing** indicates that the thresholds have been met and some users are held in the waiting room. - **event_prequeueing** indicates that an event is active and is currently prequeueing users before it starts. - **suspended** indicates that the room is suspended. 2. `event_id`: String of the current event's `id` if an event is active, otherwise an empty string. 3. `estimated_queued_users`: Integer of the estimated number of users currently waiting in the queue. 4. `estimated_total_active_users`: Integer of the estimated number of users currently active on the origin. 5. `max_estimated_time_minutes`: Integer of the maximum estimated time currently presented to the users.</td>
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
<tr id="parameter-waiting_room_id">
    <td><CopyableCode code="waiting_room_id" /></td>
    <td><code>string</code></td>
    <td>The Waiting Room ID.</td>
</tr>
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

Fetches the status of a configured waiting room. Response fields include: 1. `status`: String indicating the status of the waiting room. The possible status are: - **not_queueing** indicates that the configured thresholds have not been met and all users are going through to the origin. - **queueing** indicates that the thresholds have been met and some users are held in the waiting room. - **event_prequeueing** indicates that an event is active and is currently prequeueing users before it starts. - **suspended** indicates that the room is suspended. 2. `event_id`: String of the current event's `id` if an event is active, otherwise an empty string. 3. `estimated_queued_users`: Integer of the estimated number of users currently waiting in the queue. 4. `estimated_total_active_users`: Integer of the estimated number of users currently active on the origin. 5. `max_estimated_time_minutes`: Integer of the maximum estimated time currently presented to the users.

```sql
SELECT
event_id,
estimated_queued_users,
estimated_total_active_users,
max_estimated_time_minutes,
status
FROM cloudflare.waiting_rooms.statuses
WHERE waiting_room_id = '{{ waiting_room_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>
