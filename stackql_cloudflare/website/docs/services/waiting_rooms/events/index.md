--- 
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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

Creates, updates, deletes, gets or lists an <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.waiting_rooms.events" /></td></tr>
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

Event details response

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
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List events response

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
    <td>If set, the event will override the waiting room's `custom_page_html` property while it is active. If null, the event will inherit it. (example: &#123;&#123;#waitTimeKnown&#125;&#125; &#123;&#123;waitTime&#125;&#125; mins &#123;&#123;/waitTimeKnown&#125;&#125; &#123;&#123;^waitTimeKnown&#125;&#125; Event is prequeueing / Queue all enabled &#123;&#123;/waitTimeKnown&#125;&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A note that you can use to add more details about the event. (default: , example: Production event - DO NOT MODIFY)</td>
</tr>
<tr>
    <td><CopyableCode code="disable_session_renewal" /></td>
    <td><code>boolean</code></td>
    <td>If set, the event will override the waiting room's `disable_session_renewal` property while it is active. If null, the event will inherit it.</td>
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
    <td>If set, the event will override the waiting room's `new_users_per_minute` property while it is active. If null, the event will inherit it. This can only be set if the event's `total_active_users` property is also set.</td>
</tr>
<tr>
    <td><CopyableCode code="prequeue_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks when to begin queueing all users before the event starts. The prequeue must start at least five minutes before `event_start_time`. (example: 2021-09-28T15:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="queueing_method" /></td>
    <td><code>string</code></td>
    <td>If set, the event will override the waiting room's `queueing_method` property while it is active. If null, the event will inherit it. (example: random)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>integer</code></td>
    <td>If set, the event will override the waiting room's `session_duration` property while it is active. If null, the event will inherit it.</td>
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
    <td>If set, the event will override the waiting room's `total_active_users` property while it is active. If null, the event will inherit it. This can only be set if the event's `new_users_per_minute` property is also set.</td>
</tr>
<tr>
    <td><CopyableCode code="turnstile_action" /></td>
    <td><code>string</code></td>
    <td>If set, the event will override the waiting room's `turnstile_action` property while it is active. If null, the event will inherit it. (log, infinite_queue)</td>
</tr>
<tr>
    <td><CopyableCode code="turnstile_mode" /></td>
    <td><code>string</code></td>
    <td>If set, the event will override the waiting room's `turnstile_mode` property while it is active. If null, the event will inherit it. (off, invisible, visible_non_interactive, visible_managed)</td>
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
    <td><a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches a single configured event for a waiting room.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists events for a waiting room.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-event_start_time"><code>event_start_time</code></a>, <a href="#parameter-event_end_time"><code>event_end_time</code></a></td>
    <td></td>
    <td>Only available for the Waiting Room Advanced subscription. Creates an event for a waiting room. An event takes place during a specified period of time, temporarily changing the behavior of a waiting room. While the event is active, some of the properties in the event's configuration may either override or inherit from the waiting room's configuration. Note that events cannot overlap with each other, so only one event can be active at a time.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-event_start_time"><code>event_start_time</code></a>, <a href="#parameter-event_end_time"><code>event_end_time</code></a></td>
    <td></td>
    <td>Patches a configured event for a waiting room.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-event_start_time"><code>event_start_time</code></a>, <a href="#parameter-event_end_time"><code>event_end_time</code></a></td>
    <td></td>
    <td>Updates a configured event for a waiting room.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an event for a waiting room.</td>
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
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td>Page number of paginated results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Maximum number of results per page. Must be a multiple of 5.</td>
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

Fetches a single configured event for a waiting room.

```sql
SELECT
result
FROM cloudflare.waiting_rooms.events
WHERE event_id = '{{ event_id }}' -- required
AND waiting_room_id = '{{ waiting_room_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists events for a waiting room.

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
total_active_users,
turnstile_action,
turnstile_mode
FROM cloudflare.waiting_rooms.events
WHERE waiting_room_id = '{{ waiting_room_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Only available for the Waiting Room Advanced subscription. Creates an event for a waiting room. An event takes place during a specified period of time, temporarily changing the behavior of a waiting room. While the event is active, some of the properties in the event's configuration may either override or inherit from the waiting room's configuration. Note that events cannot overlap with each other, so only one event can be active at a time.

```sql
INSERT INTO cloudflare.waiting_rooms.events (
custom_page_html,
description,
disable_session_renewal,
event_end_time,
event_start_time,
name,
new_users_per_minute,
prequeue_start_time,
queueing_method,
session_duration,
shuffle_at_event_start,
suspended,
total_active_users,
turnstile_action,
turnstile_mode,
waiting_room_id,
zone_id
)
SELECT 
'{{ custom_page_html }}',
'{{ description }}',
{{ disable_session_renewal }},
'{{ event_end_time }}' /* required */,
'{{ event_start_time }}' /* required */,
'{{ name }}' /* required */,
{{ new_users_per_minute }},
'{{ prequeue_start_time }}',
'{{ queueing_method }}',
{{ session_duration }},
{{ shuffle_at_event_start }},
{{ suspended }},
{{ total_active_users }},
'{{ turnstile_action }}',
'{{ turnstile_mode }}',
'{{ waiting_room_id }}',
'{{ zone_id }}'
RETURNING
result
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: events
  props:
    - name: waiting_room_id
      value: "{{ waiting_room_id }}"
      description: Required parameter for the events resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the events resource.
    - name: custom_page_html
      value: "{{ custom_page_html }}"
      description: |
        If set, the event will override the waiting room's \`custom_page_html\` property while it is active. If null, the event will inherit it.
    - name: description
      value: "{{ description }}"
      description: |
        A note that you can use to add more details about the event.
      default: 
    - name: disable_session_renewal
      value: {{ disable_session_renewal }}
      description: |
        If set, the event will override the waiting room's \`disable_session_renewal\` property while it is active. If null, the event will inherit it.
    - name: event_end_time
      value: "{{ event_end_time }}"
      description: |
        An ISO 8601 timestamp that marks the end of the event.
    - name: event_start_time
      value: "{{ event_start_time }}"
      description: |
        An ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. The start time must be at least one minute before \`event_end_time\`.
    - name: name
      value: "{{ name }}"
      description: |
        A unique name to identify the event. Only alphanumeric characters, hyphens and underscores are allowed.
    - name: new_users_per_minute
      value: {{ new_users_per_minute }}
      description: |
        If set, the event will override the waiting room's \`new_users_per_minute\` property while it is active. If null, the event will inherit it. This can only be set if the event's \`total_active_users\` property is also set.
    - name: prequeue_start_time
      value: "{{ prequeue_start_time }}"
      description: |
        An ISO 8601 timestamp that marks when to begin queueing all users before the event starts. The prequeue must start at least five minutes before \`event_start_time\`.
    - name: queueing_method
      value: "{{ queueing_method }}"
      description: |
        If set, the event will override the waiting room's \`queueing_method\` property while it is active. If null, the event will inherit it.
    - name: session_duration
      value: {{ session_duration }}
      description: |
        If set, the event will override the waiting room's \`session_duration\` property while it is active. If null, the event will inherit it.
    - name: shuffle_at_event_start
      value: {{ shuffle_at_event_start }}
      description: |
        If enabled, users in the prequeue will be shuffled randomly at the \`event_start_time\`. Requires that \`prequeue_start_time\` is not null. This is useful for situations when many users will join the event prequeue at the same time and you want to shuffle them to ensure fairness. Naturally, it makes the most sense to enable this feature when the \`queueing_method\` during the event respects ordering such as **fifo**, or else the shuffling may be unnecessary.
      default: false
    - name: suspended
      value: {{ suspended }}
      description: |
        Suspends or allows an event. If set to \`true\`, the event is ignored and traffic will be handled based on the waiting room configuration.
      default: false
    - name: total_active_users
      value: {{ total_active_users }}
      description: |
        If set, the event will override the waiting room's \`total_active_users\` property while it is active. If null, the event will inherit it. This can only be set if the event's \`new_users_per_minute\` property is also set.
    - name: turnstile_action
      value: "{{ turnstile_action }}"
      description: |
        If set, the event will override the waiting room's \`turnstile_action\` property while it is active. If null, the event will inherit it.
      valid_values: ['log', 'infinite_queue']
    - name: turnstile_mode
      value: "{{ turnstile_mode }}"
      description: |
        If set, the event will override the waiting room's \`turnstile_mode\` property while it is active. If null, the event will inherit it.
      valid_values: ['off', 'invisible', 'visible_non_interactive', 'visible_managed']
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

Patches a configured event for a waiting room.

```sql
UPDATE cloudflare.waiting_rooms.events
SET 
custom_page_html = '{{ custom_page_html }}',
description = '{{ description }}',
disable_session_renewal = {{ disable_session_renewal }},
event_end_time = '{{ event_end_time }}',
event_start_time = '{{ event_start_time }}',
name = '{{ name }}',
new_users_per_minute = {{ new_users_per_minute }},
prequeue_start_time = '{{ prequeue_start_time }}',
queueing_method = '{{ queueing_method }}',
session_duration = {{ session_duration }},
shuffle_at_event_start = {{ shuffle_at_event_start }},
suspended = {{ suspended }},
total_active_users = {{ total_active_users }},
turnstile_action = '{{ turnstile_action }}',
turnstile_mode = '{{ turnstile_mode }}'
WHERE 
event_id = '{{ event_id }}' --required
AND waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND event_start_time = '{{ event_start_time }}' --required
AND event_end_time = '{{ event_end_time }}' --required
RETURNING
result;
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

Updates a configured event for a waiting room.

```sql
REPLACE cloudflare.waiting_rooms.events
SET 
custom_page_html = '{{ custom_page_html }}',
description = '{{ description }}',
disable_session_renewal = {{ disable_session_renewal }},
event_end_time = '{{ event_end_time }}',
event_start_time = '{{ event_start_time }}',
name = '{{ name }}',
new_users_per_minute = {{ new_users_per_minute }},
prequeue_start_time = '{{ prequeue_start_time }}',
queueing_method = '{{ queueing_method }}',
session_duration = {{ session_duration }},
shuffle_at_event_start = {{ shuffle_at_event_start }},
suspended = {{ suspended }},
total_active_users = {{ total_active_users }},
turnstile_action = '{{ turnstile_action }}',
turnstile_mode = '{{ turnstile_mode }}'
WHERE 
event_id = '{{ event_id }}' --required
AND waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND event_start_time = '{{ event_start_time }}' --required
AND event_end_time = '{{ event_end_time }}' --required
RETURNING
result;
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

Deletes an event for a waiting room.

```sql
DELETE FROM cloudflare.waiting_rooms.events
WHERE event_id = '{{ event_id }}' --required
AND waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
