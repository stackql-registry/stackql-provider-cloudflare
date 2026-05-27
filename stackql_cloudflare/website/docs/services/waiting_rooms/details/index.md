--- 
title: details
hide_title: false
hide_table_of_contents: false
keywords:
  - details
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

Creates, updates, deletes, gets or lists a <code>details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.waiting_rooms.details" /></td></tr>
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

Preview active event details response

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
    <td> (example: 25756b2dfe6e378a06b033b670413757)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A unique name to identify the event. Only alphanumeric characters, hyphens and underscores are allowed. (example: production_webinar_event)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_page_html" /></td>
    <td><code>string</code></td>
    <td> (example: &#123;&#123;#waitTimeKnown&#125;&#125; &#123;&#123;waitTime&#125;&#125; mins &#123;&#123;/waitTimeKnown&#125;&#125; &#123;&#123;^waitTimeKnown&#125;&#125; Event is prequeueing / Queue all enabled &#123;&#123;/waitTimeKnown&#125;&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A note that you can use to add more details about the event. (default: , example: Production event - DO NOT MODIFY)</td>
</tr>
<tr>
    <td><CopyableCode code="disable_session_renewal" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="event_end_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks the end of the event. (example: 2021-09-28T17:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="event_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. The start time must be at least one minute before `event_end_time`. (example: 2021-09-28T15:30:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="new_users_per_minute" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="prequeue_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks when to begin queueing all users before the event starts. The prequeue must start at least five minutes before `event_start_time`. (example: 2021-09-28T15:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="queueing_method" /></td>
    <td><code>string</code></td>
    <td> (example: random)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="shuffle_at_event_start" /></td>
    <td><code>boolean</code></td>
    <td>If enabled, users in the prequeue will be shuffled randomly at the `event_start_time`. Requires that `prequeue_start_time` is not null. This is useful for situations when many users will join the event prequeue at the same time and you want to shuffle them to ensure fairness. Naturally, it makes the most sense to enable this feature when the `queueing_method` during the event respects ordering such as **fifo**, or else the shuffling may be unnecessary.</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>Suspends or allows an event. If set to `true`, the event is ignored and traffic will be handled based on the waiting room configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="total_active_users" /></td>
    <td><code>integer</code></td>
    <td></td>
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
    <td><a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Previews an event's configuration as if it was active. Inherited fields from the waiting room will be displayed with their current values.</td>
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
<tr id="parameter-event_id">
    <td><CopyableCode code="event_id" /></td>
    <td><code>string</code></td>
    <td>The event ID.</td>
</tr>
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

Previews an event's configuration as if it was active. Inherited fields from the waiting room will be displayed with their current values.

```sql
SELECT
id,
name,
created_on,
custom_page_html,
description,
disable_session_renewal,
event_end_time,
event_start_time,
modified_on,
new_users_per_minute,
prequeue_start_time,
queueing_method,
session_duration,
shuffle_at_event_start,
suspended,
total_active_users
FROM cloudflare.waiting_rooms.details
WHERE event_id = '{{ event_id }}' -- required
AND waiting_room_id = '{{ waiting_room_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>
