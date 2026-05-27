--- 
title: active_session
hide_title: false
hide_table_of_contents: false
keywords:
  - active_session
  - realtime_kit
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

Creates, updates, deletes, gets or lists an <code>active_session</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="active_session" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.active_session" /></td></tr>
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

Active Session Success response

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
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Returns details of an ongoing active session for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#kick"><CopyableCode code="kick" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-participant_ids"><code>participant_ids</code></a>, <a href="#parameter-custom_participant_ids"><code>custom_participant_ids</code></a></td>
    <td></td>
    <td>Kicks one or more participants from an active session using user ID or custom participant ID.</td>
</tr>
<tr>
    <td><a href="#kick_all"><CopyableCode code="kick_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a></td>
    <td></td>
    <td>Kicks all participants from an active session for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#mute"><CopyableCode code="mute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-participant_ids"><code>participant_ids</code></a>, <a href="#parameter-custom_participant_ids"><code>custom_participant_ids</code></a></td>
    <td></td>
    <td>Mutes one or more participants from an active session using user ID or custom participant ID.</td>
</tr>
<tr>
    <td><a href="#mute_all"><CopyableCode code="mute_all" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-allow_unmute"><code>allow_unmute</code></a></td>
    <td></td>
    <td>Mutes all participants of an active session for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#create_poll"><CopyableCode code="create_poll" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-question"><code>question</code></a>, <a href="#parameter-options"><code>options</code></a></td>
    <td></td>
    <td>Creates a new poll in an active session for the given meeting ID.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-meeting_id">
    <td><CopyableCode code="meeting_id" /></td>
    <td><code>string</code></td>
    <td>The Realtime Kit meeting ID.</td>
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

Returns details of an ongoing active session for the given meeting ID.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.active_session
WHERE meeting_id = '{{ meeting_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="kick"
    values={[
        { label: 'kick', value: 'kick' },
        { label: 'kick_all', value: 'kick_all' },
        { label: 'mute', value: 'mute' },
        { label: 'mute_all', value: 'mute_all' },
        { label: 'create_poll', value: 'create_poll' }
    ]}
>
<TabItem value="kick">

Kicks one or more participants from an active session using user ID or custom participant ID.

```sql
EXEC cloudflare.realtime_kit.active_session.kick 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required, 
@meeting_id='{{ meeting_id }}' --required 
@@json=
'{
"custom_participant_ids": "{{ custom_participant_ids }}", 
"participant_ids": "{{ participant_ids }}"
}'
;
```
</TabItem>
<TabItem value="kick_all">

Kicks all participants from an active session for the given meeting ID.

```sql
EXEC cloudflare.realtime_kit.active_session.kick_all 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required, 
@meeting_id='{{ meeting_id }}' --required
;
```
</TabItem>
<TabItem value="mute">

Mutes one or more participants from an active session using user ID or custom participant ID.

```sql
EXEC cloudflare.realtime_kit.active_session.mute 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required, 
@meeting_id='{{ meeting_id }}' --required 
@@json=
'{
"custom_participant_ids": "{{ custom_participant_ids }}", 
"participant_ids": "{{ participant_ids }}"
}'
;
```
</TabItem>
<TabItem value="mute_all">

Mutes all participants of an active session for the given meeting ID.

```sql
EXEC cloudflare.realtime_kit.active_session.mute_all 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required, 
@meeting_id='{{ meeting_id }}' --required 
@@json=
'{
"allow_unmute": {{ allow_unmute }}
}'
;
```
</TabItem>
<TabItem value="create_poll">

Creates a new poll in an active session for the given meeting ID.

```sql
EXEC cloudflare.realtime_kit.active_session.create_poll 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required, 
@meeting_id='{{ meeting_id }}' --required 
@@json=
'{
"anonymous": {{ anonymous }}, 
"hide_votes": {{ hide_votes }}, 
"options": "{{ options }}", 
"question": "{{ question }}"
}'
;
```
</TabItem>
</Tabs>
