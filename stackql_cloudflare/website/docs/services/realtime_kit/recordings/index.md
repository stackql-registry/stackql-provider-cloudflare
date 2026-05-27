--- 
title: recordings
hide_title: false
hide_table_of_contents: false
keywords:
  - recordings
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

Creates, updates, deletes, gets or lists a <code>recordings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recordings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.recordings" /></td></tr>
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

Success response

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
    <td><code>string (uuid)</code></td>
    <td>ID of the recording</td>
</tr>
<tr>
    <td><CopyableCode code="session_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>ID of the meeting session this recording is for.</td>
</tr>
<tr>
    <td><CopyableCode code="output_file_name" /></td>
    <td><code>string</code></td>
    <td>File name of the recording.</td>
</tr>
<tr>
    <td><CopyableCode code="audio_download_url" /></td>
    <td><code>string (uri)</code></td>
    <td>If the audio_config is passed, the URL for downloading the audio recording is returned.</td>
</tr>
<tr>
    <td><CopyableCode code="download_url" /></td>
    <td><code>string (uri)</code></td>
    <td>URL where the recording can be downloaded.</td>
</tr>
<tr>
    <td><CopyableCode code="download_url_expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the download URL expires.</td>
</tr>
<tr>
    <td><CopyableCode code="file_size" /></td>
    <td><code>number</code></td>
    <td>File size of the recording, in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="invoked_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this recording was invoked.</td>
</tr>
<tr>
    <td><CopyableCode code="meeting" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="recording_duration" /></td>
    <td><code>integer</code></td>
    <td>Total recording time in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="started_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the recording. (INVOKED, RECORDING, UPLOADING, UPLOADED, ERRORED, PAUSED)</td>
</tr>
<tr>
    <td><CopyableCode code="stopped_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.</td>
</tr>
<tr>
    <td><CopyableCode code="storage_config" /></td>
    <td><code>object</code></td>
    <td> (title: StorageConfig)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-page_no"><code>page_no</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-expired"><code>expired</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_time"><code>start_time</code></a>, <a href="#parameter-end_time"><code>end_time</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td>Returns all recordings for an App. If the `meeting_id` parameter is passed, returns all recordings for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#pause_resume_stop_recording"><CopyableCode code="pause_resume_stop_recording" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-recording_id"><code>recording_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Pause/Resume/Stop a given recording ID.</td>
</tr>
<tr>
    <td><a href="#create_track"><CopyableCode code="create_track" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-layers"><code>layers</code></a></td>
    <td></td>
    <td>Starts a track recording in a meeting. Track recordings consist of "layers". Layers are used to map audio/video tracks in a meeting to output destinations. More information about track recordings is available in the [Track Recordings Guide Page](https://docs.realtime.cloudflare.com/guides/capabilities/recording/recording-overview).</td>
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
<tr id="parameter-recording_id">
    <td><CopyableCode code="recording_id" /></td>
    <td><code>string</code></td>
    <td>ID of the recording</td>
</tr>
<tr id="parameter-end_time">
    <td><CopyableCode code="end_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time range for which you want to retrieve the meetings. The time must be specified in ISO format.</td>
</tr>
<tr id="parameter-expired">
    <td><CopyableCode code="expired" /></td>
    <td><code>boolean</code></td>
    <td>If passed, only shows expired/non-expired recordings on RealtimeKit's bucket</td>
</tr>
<tr id="parameter-meeting_id">
    <td><CopyableCode code="meeting_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>ID of a meeting. Optional. Will limit results to only this meeting if passed.</td>
</tr>
<tr id="parameter-page_no">
    <td><CopyableCode code="page_no" /></td>
    <td><code>number</code></td>
    <td>The page number from which you want your page search results to be displayed.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Number of results per page</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>The search query string. You can search using the meeting ID or title.</td>
</tr>
<tr id="parameter-sort_by">
    <td><CopyableCode code="sort_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-start_time">
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time range for which you want to retrieve the meetings. The time must be specified in ISO format.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>array</code></td>
    <td>Filter by one or more recording status</td>
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

Returns all recordings for an App. If the `meeting_id` parameter is passed, returns all recordings for the given meeting ID.

```sql
SELECT
id,
session_id,
output_file_name,
audio_download_url,
download_url,
download_url_expiry,
file_size,
invoked_time,
meeting,
recording_duration,
started_time,
status,
stopped_time,
storage_config
FROM cloudflare.realtime_kit.recordings
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND meeting_id = '{{ meeting_id }}'
AND page_no = '{{ page_no }}'
AND per_page = '{{ per_page }}'
AND expired = '{{ expired }}'
AND search = '{{ search }}'
AND sort_by = '{{ sort_by }}'
AND sort_order = '{{ sort_order }}'
AND start_time = '{{ start_time }}'
AND end_time = '{{ end_time }}'
AND status = '{{ status }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="pause_resume_stop_recording"
    values={[
        { label: 'pause_resume_stop_recording', value: 'pause_resume_stop_recording' }
    ]}
>
<TabItem value="pause_resume_stop_recording">

Pause/Resume/Stop a given recording ID.

```sql
REPLACE cloudflare.realtime_kit.recordings
SET 
action = '{{ action }}'
WHERE 
account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
AND recording_id = '{{ recording_id }}' --required
AND action = '{{ action }}' --required
RETURNING
data,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_track"
    values={[
        { label: 'create_track', value: 'create_track' }
    ]}
>
<TabItem value="create_track">

Starts a track recording in a meeting. Track recordings consist of "layers". Layers are used to map audio/video tracks in a meeting to output destinations. More information about track recordings is available in the [Track Recordings Guide Page](https://docs.realtime.cloudflare.com/guides/capabilities/recording/recording-overview).

```sql
EXEC cloudflare.realtime_kit.recordings.create_track 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required 
@@json=
'{
"layers": "{{ layers }}", 
"max_seconds": {{ max_seconds }}, 
"meeting_id": "{{ meeting_id }}"
}'
;
```
</TabItem>
</Tabs>
