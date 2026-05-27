--- 
title: live_inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - live_inputs
  - streams
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

Creates, updates, deletes, gets or lists a <code>live_inputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="live_inputs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.live_inputs" /></td></tr>
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

Retrieve a live input response.

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
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the live input was created. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleteRecordingAfterDays" /></td>
    <td><code>number</code></td>
    <td>Indicates the number of days after which the live inputs recordings will be deleted. When a stream completes and the recording is ready, the value is used to calculate a scheduled deletion date for that recording. Omit the field to indicate no change, or include with a `null` value to remove an existing scheduled deletion.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the live input is enabled and can accept streams.</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>A user modifiable key-value store used to reference other systems of record for managing live inputs.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the live input was last modified. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="recording" /></td>
    <td><code>object</code></td>
    <td>Records the input to a Cloudflare Stream video. Behavior depends on the mode. In most cases, the video will initially be viewable as a live video and transition to on-demand after a condition is satisfied.</td>
</tr>
<tr>
    <td><CopyableCode code="rtmps" /></td>
    <td><code>object</code></td>
    <td>Details for streaming to an live input using RTMPS.</td>
</tr>
<tr>
    <td><CopyableCode code="rtmpsPlayback" /></td>
    <td><code>object</code></td>
    <td>Details for playback from an live input using RTMPS.</td>
</tr>
<tr>
    <td><CopyableCode code="srt" /></td>
    <td><code>object</code></td>
    <td>Details for streaming to a live input using SRT.</td>
</tr>
<tr>
    <td><CopyableCode code="srtPlayback" /></td>
    <td><code>object</code></td>
    <td>Details for playback from an live input using SRT.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The connection status of a live input. (, connected, reconnected, reconnecting, client_disconnect, ttl_exceeded, failed_to_connect, failed_to_reconnect, new_configuration_accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for a live input. (example: 66be4bf738797e01e1fca35a7bdecdcd)</td>
</tr>
<tr>
    <td><CopyableCode code="webRTC" /></td>
    <td><code>object</code></td>
    <td>Details for streaming to a live input using WebRTC.</td>
</tr>
<tr>
    <td><CopyableCode code="webRTCPlayback" /></td>
    <td><code>object</code></td>
    <td>Details for playback from a live input using WebRTC.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List live inputs response.

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
    <td><CopyableCode code="liveInputs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="range" /></td>
    <td><code>integer</code></td>
    <td>The total number of remaining live inputs based on cursor position.</td>
</tr>
<tr>
    <td><CopyableCode code="total" /></td>
    <td><code>integer</code></td>
    <td>The total number of live inputs that match the provided filters.</td>
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
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves details of an existing live input.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-include_counts"><code>include_counts</code></a></td>
    <td>Lists the live inputs created for an account. To get the credentials needed to stream to a specific live input, request a single live input.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a live input, and returns credentials that you or your users can use to stream live video to Cloudflare Stream.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates a specified live input.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Prevents a live input from being streamed to and makes the live input inaccessible to any future API calls.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Prevents a live input from being streamed to and makes the live input inaccessible to any future API calls until enabled.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Allows a live input to be streamed to and makes the live input accessible to any future API calls.</td>
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
<tr id="parameter-live_input_identifier">
    <td><CopyableCode code="live_input_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-include_counts">
    <td><CopyableCode code="include_counts" /></td>
    <td><code>boolean</code></td>
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

Retrieves details of an existing live input.

```sql
SELECT
created,
deleteRecordingAfterDays,
enabled,
meta,
modified,
recording,
rtmps,
rtmpsPlayback,
srt,
srtPlayback,
status,
uid,
webRTC,
webRTCPlayback
FROM cloudflare.streams.live_inputs
WHERE live_input_identifier = '{{ live_input_identifier }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the live inputs created for an account. To get the credentials needed to stream to a specific live input, request a single live input.

```sql
SELECT
liveInputs,
range,
total
FROM cloudflare.streams.live_inputs
WHERE account_id = '{{ account_id }}' -- required
AND include_counts = '{{ include_counts }}'
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

Creates a live input, and returns credentials that you or your users can use to stream live video to Cloudflare Stream.

```sql
INSERT INTO cloudflare.streams.live_inputs (
defaultCreator,
deleteRecordingAfterDays,
enabled,
meta,
recording,
account_id
)
SELECT 
'{{ defaultCreator }}',
{{ deleteRecordingAfterDays }},
{{ enabled }},
'{{ meta }}',
'{{ recording }}',
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
- name: live_inputs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the live_inputs resource.
    - name: defaultCreator
      value: "{{ defaultCreator }}"
      description: |
        Sets the creator ID asssociated with this live input.
    - name: deleteRecordingAfterDays
      value: {{ deleteRecordingAfterDays }}
      description: |
        Indicates the number of days after which the live inputs recordings will be deleted. When a stream completes and the recording is ready, the value is used to calculate a scheduled deletion date for that recording. Omit the field to indicate no change, or include with a \`null\` value to remove an existing scheduled deletion.
    - name: enabled
      value: {{ enabled }}
      description: |
        Indicates whether the live input is enabled and can accept streams.
      default: true
    - name: meta
      value: "{{ meta }}"
      description: |
        A user modifiable key-value store used to reference other systems of record for managing live inputs.
    - name: recording
      description: |
        Records the input to a Cloudflare Stream video. Behavior depends on the mode. In most cases, the video will initially be viewable as a live video and transition to on-demand after a condition is satisfied.
      value:
        allowedOrigins:
          - "{{ allowedOrigins }}"
        hideLiveViewerCount: {{ hideLiveViewerCount }}
        mode: "{{ mode }}"
        requireSignedURLs: {{ requireSignedURLs }}
        timeoutSeconds: {{ timeoutSeconds }}
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

Updates a specified live input.

```sql
REPLACE cloudflare.streams.live_inputs
SET 
defaultCreator = '{{ defaultCreator }}',
deleteRecordingAfterDays = {{ deleteRecordingAfterDays }},
enabled = {{ enabled }},
meta = '{{ meta }}',
recording = '{{ recording }}'
WHERE 
live_input_identifier = '{{ live_input_identifier }}' --required
AND account_id = '{{ account_id }}' --required
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

Prevents a live input from being streamed to and makes the live input inaccessible to any future API calls.

```sql
DELETE FROM cloudflare.streams.live_inputs
WHERE live_input_identifier = '{{ live_input_identifier }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disable"
    values={[
        { label: 'disable', value: 'disable' },
        { label: 'enable', value: 'enable' }
    ]}
>
<TabItem value="disable">

Prevents a live input from being streamed to and makes the live input inaccessible to any future API calls until enabled.

```sql
EXEC cloudflare.streams.live_inputs.disable 
@live_input_identifier='{{ live_input_identifier }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="enable">

Allows a live input to be streamed to and makes the live input accessible to any future API calls.

```sql
EXEC cloudflare.streams.live_inputs.enable 
@live_input_identifier='{{ live_input_identifier }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
