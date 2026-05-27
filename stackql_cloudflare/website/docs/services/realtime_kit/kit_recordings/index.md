--- 
title: kit_recordings
hide_title: false
hide_table_of_contents: false
keywords:
  - kit_recordings
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

Creates, updates, deletes, gets or lists a <code>kit_recordings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kit_recordings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.kit_recordings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' }
    ]}
>
<TabItem value="get_by_account">

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
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>Data returned by the operation (title: Recording)</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Success status of the operation</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-recording_id"><code>recording_id</code></a></td>
    <td></td>
    <td>Returns details of a recording for the given recording ID.</td>
</tr>
<tr>
    <td><a href="#start_recordings"><CopyableCode code="start_recordings" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Starts recording a meeting. The meeting can be started by an App admin directly, or a participant with permissions to start a recording, based on the type of authorization used.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' }
    ]}
>
<TabItem value="get_by_account">

Returns details of a recording for the given recording ID.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.kit_recordings
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND recording_id = '{{ recording_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="start_recordings"
    values={[
        { label: 'start_recordings', value: 'start_recordings' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="start_recordings">

Starts recording a meeting. The meeting can be started by an App admin directly, or a participant with permissions to start a recording, based on the type of authorization used.

```sql
INSERT INTO cloudflare.realtime_kit.kit_recordings (
allow_multiple_recordings,
audio_config,
file_name_prefix,
interactive_config,
max_seconds,
meeting_id,
realtimekit_bucket_config,
rtmp_out_config,
storage_config,
url,
video_config,
account_id,
app_id
)
SELECT 
{{ allow_multiple_recordings }},
'{{ audio_config }}',
'{{ file_name_prefix }}',
'{{ interactive_config }}',
{{ max_seconds }},
'{{ meeting_id }}',
'{{ realtimekit_bucket_config }}',
'{{ rtmp_out_config }}',
'{{ storage_config }}',
'{{ url }}',
'{{ video_config }}',
'{{ account_id }}',
'{{ app_id }}'
RETURNING
data,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: kit_recordings
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the kit_recordings resource.
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the kit_recordings resource.
    - name: allow_multiple_recordings
      value: {{ allow_multiple_recordings }}
      description: |
        By default, a meeting allows only one recording to run at a time. Enabling the \`allow_multiple_recordings\` parameter to true allows you to initiate multiple recordings concurrently in the same meeting. This allows you to record separate videos of the same meeting with different configurations, such as portrait mode or landscape mode.
      default: false
    - name: audio_config
      description: |
        Object containing configuration regarding the audio that is being recorded.
      value:
        channel: "{{ channel }}"
        codec: "{{ codec }}"
        export_file: {{ export_file }}
    - name: file_name_prefix
      value: "{{ file_name_prefix }}"
      description: |
        Update the recording file name.
    - name: interactive_config
      description: |
        Allows you to add timed metadata to your recordings, which are digital markers inserted into a video file to provide contextual information at specific points in the content range. The ID3 tags containing this information are available to clients on the playback timeline in HLS format. The output files are generated in a compressed .tar format.
      value:
        type: "{{ type }}"
    - name: max_seconds
      value: {{ max_seconds }}
      description: |
        Specifies the maximum duration for recording in seconds, ranging from a minimum of 60 seconds to a maximum of 24 hours.
    - name: meeting_id
      value: "{{ meeting_id }}"
      description: |
        ID of the meeting to record.
    - name: realtimekit_bucket_config
      value:
        enabled: {{ enabled }}
    - name: rtmp_out_config
      value:
        rtmp_url: "{{ rtmp_url }}"
    - name: storage_config
      value:
        access_key: "{{ access_key }}"
        auth_method: "{{ auth_method }}"
        bucket: "{{ bucket }}"
        host: "{{ host }}"
        password: "{{ password }}"
        path: "{{ path }}"
        port: {{ port }}
        private_key: "{{ private_key }}"
        region: "{{ region }}"
        secret: "{{ secret }}"
        type: "{{ type }}"
        username: "{{ username }}"
    - name: url
      value: "{{ url }}"
      description: |
        Pass a custom url to record arbitary screen
    - name: video_config
      value:
        codec: "{{ codec }}"
        export_file: {{ export_file }}
        height: {{ height }}
        watermark:
          position: "{{ position }}"
          size:
            height: {{ height }}
            width: {{ width }}
          url: "{{ url }}"
        width: {{ width }}
`}</CodeBlock>

</TabItem>
</Tabs>
