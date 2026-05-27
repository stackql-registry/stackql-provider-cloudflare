--- 
title: meetings
hide_title: false
hide_table_of_contents: false
keywords:
  - meetings
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

Creates, updates, deletes, gets or lists a <code>meetings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="meetings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.meetings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#refresh_participant_token"><CopyableCode code="refresh_participant_token" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-participant_id"><code>participant_id</code></a></td>
    <td></td>
    <td>Regenerates participant's authentication token for the given meeting and participant ID.</td>
</tr>
<tr>
    <td><a href="#add_participant"><CopyableCode code="add_participant" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-preset_name"><code>preset_name</code></a>, <a href="#parameter-custom_participant_id"><code>custom_participant_id</code></a></td>
    <td></td>
    <td>Adds a participant to the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Create a meeting for the given App ID.</td>
</tr>
<tr>
    <td><a href="#edit_participant"><CopyableCode code="edit_participant" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-participant_id"><code>participant_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Updates a participant's details for the given meeting and participant ID.</td>
</tr>
<tr>
    <td><a href="#update_meeting_by_id"><CopyableCode code="update_meeting_by_id" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Updates a meeting in an App for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#replace_meeting_by_id"><CopyableCode code="replace_meeting_by_id" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Replaces all the details for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#delete_meeting_participant"><CopyableCode code="delete_meeting_participant" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-participant_id"><code>participant_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Deletes a participant for the given meeting and participant ID.</td>
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
<tr id="parameter-participant_id">
    <td><CopyableCode code="participant_id" /></td>
    <td><code>string</code></td>
    <td>ID of the participant. You can fetch the participant ID using the add a participant API.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="refresh_participant_token"
    values={[
        { label: 'refresh_participant_token', value: 'refresh_participant_token' },
        { label: 'add_participant', value: 'add_participant' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="refresh_participant_token">

Regenerates participant's authentication token for the given meeting and participant ID.

```sql
INSERT INTO cloudflare.realtime_kit.meetings (
account_id,
app_id,
meeting_id,
participant_id
)
SELECT 
'{{ account_id }}',
'{{ app_id }}',
'{{ meeting_id }}',
'{{ participant_id }}'
RETURNING
data,
success
;
```
</TabItem>
<TabItem value="add_participant">

Adds a participant to the given meeting ID.

```sql
INSERT INTO cloudflare.realtime_kit.meetings (
custom_participant_id,
name,
picture,
preset_name,
account_id,
app_id,
meeting_id
)
SELECT 
'{{ custom_participant_id }}' /* required */,
'{{ name }}',
'{{ picture }}',
'{{ preset_name }}' /* required */,
'{{ account_id }}',
'{{ app_id }}',
'{{ meeting_id }}'
RETURNING
data,
success
;
```
</TabItem>
<TabItem value="create">

Create a meeting for the given App ID.

```sql
INSERT INTO cloudflare.realtime_kit.meetings (
ai_config,
live_stream_on_start,
persist_chat,
record_on_start,
recording_config,
session_keep_alive_time_in_secs,
summarize_on_end,
title,
account_id,
app_id
)
SELECT 
'{{ ai_config }}',
{{ live_stream_on_start }},
{{ persist_chat }},
{{ record_on_start }},
'{{ recording_config }}',
{{ session_keep_alive_time_in_secs }},
{{ summarize_on_end }},
'{{ title }}',
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
- name: meetings
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the meetings resource.
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the meetings resource.
    - name: meeting_id
      value: "{{ meeting_id }}"
      description: Required parameter for the meetings resource.
    - name: participant_id
      value: "{{ participant_id }}"
      description: Required parameter for the meetings resource.
    - name: custom_participant_id
      value: "{{ custom_participant_id }}"
      description: |
        A unique participant ID. You must specify a unique ID for the participant, for example, UUID, email address, and so on.
    - name: name
      value: "{{ name }}"
      description: |
        (Optional) Name of the participant.
    - name: picture
      value: "{{ picture }}"
      description: |
        (Optional) A URL to a picture to be used for the participant.
    - name: preset_name
      value: "{{ preset_name }}"
      description: |
        Name of the preset to apply to this participant.
      default: group_call_host
    - name: ai_config
      description: |
        The AI Config allows you to customize the behavior of meeting transcriptions and summaries
      value:
        summarization:
          summary_type: "{{ summary_type }}"
          text_format: "{{ text_format }}"
          word_limit: {{ word_limit }}
        transcription:
          keywords:
            - "{{ keywords }}"
          language: "{{ language }}"
          profanity_filter: {{ profanity_filter }}
    - name: live_stream_on_start
      value: {{ live_stream_on_start }}
      description: |
        Specifies if the meeting should start getting livestreamed on start.
      default: false
    - name: persist_chat
      value: {{ persist_chat }}
      description: |
        If a meeting is set to persist_chat, meeting chat would remain for a week within the meeting space.
      default: false
    - name: record_on_start
      value: {{ record_on_start }}
      description: |
        Specifies if the meeting should start getting recorded as soon as someone joins the meeting.
      default: false
    - name: recording_config
      description: |
        Recording Configurations to be used for this meeting. This level of configs takes higher preference over App level configs on the RealtimeKit developer portal.
      value:
        audio_config:
          channel: "{{ channel }}"
          codec: "{{ codec }}"
          export_file: {{ export_file }}
        file_name_prefix: "{{ file_name_prefix }}"
        live_streaming_config:
          rtmp_url: "{{ rtmp_url }}"
        max_seconds: {{ max_seconds }}
        realtimekit_bucket_config:
          enabled: {{ enabled }}
        storage_config:
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
        video_config:
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
    - name: session_keep_alive_time_in_secs
      value: {{ session_keep_alive_time_in_secs }}
      description: |
        Time in seconds, for which a session remains active, after the last participant has left the meeting.
      default: 60
    - name: summarize_on_end
      value: {{ summarize_on_end }}
      description: |
        Automatically generate summary of meetings using transcripts. Requires Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.
      default: false
    - name: title
      value: "{{ title }}"
      description: |
        Title of the meeting
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit_participant"
    values={[
        { label: 'edit_participant', value: 'edit_participant' },
        { label: 'update_meeting_by_id', value: 'update_meeting_by_id' }
    ]}
>
<TabItem value="edit_participant">

Updates a participant's details for the given meeting and participant ID.

```sql
UPDATE cloudflare.realtime_kit.meetings
SET 
name = '{{ name }}',
picture = '{{ picture }}',
preset_name = '{{ preset_name }}'
WHERE 
meeting_id = '{{ meeting_id }}' --required
AND participant_id = '{{ participant_id }}' --required
AND account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
RETURNING
data,
success;
```
</TabItem>
<TabItem value="update_meeting_by_id">

Updates a meeting in an App for the given meeting ID.

```sql
UPDATE cloudflare.realtime_kit.meetings
SET 
ai_config = '{{ ai_config }}',
live_stream_on_start = {{ live_stream_on_start }},
persist_chat = {{ persist_chat }},
record_on_start = {{ record_on_start }},
session_keep_alive_time_in_secs = {{ session_keep_alive_time_in_secs }},
status = '{{ status }}',
summarize_on_end = {{ summarize_on_end }},
title = '{{ title }}'
WHERE 
meeting_id = '{{ meeting_id }}' --required
AND account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
RETURNING
data,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace_meeting_by_id"
    values={[
        { label: 'replace_meeting_by_id', value: 'replace_meeting_by_id' }
    ]}
>
<TabItem value="replace_meeting_by_id">

Replaces all the details for the given meeting ID.

```sql
REPLACE cloudflare.realtime_kit.meetings
SET 
ai_config = '{{ ai_config }}',
live_stream_on_start = {{ live_stream_on_start }},
persist_chat = {{ persist_chat }},
record_on_start = {{ record_on_start }},
recording_config = '{{ recording_config }}',
session_keep_alive_time_in_secs = {{ session_keep_alive_time_in_secs }},
summarize_on_end = {{ summarize_on_end }},
title = '{{ title }}'
WHERE 
meeting_id = '{{ meeting_id }}' --required
AND account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
RETURNING
data,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_meeting_participant"
    values={[
        { label: 'delete_meeting_participant', value: 'delete_meeting_participant' }
    ]}
>
<TabItem value="delete_meeting_participant">

Deletes a participant for the given meeting and participant ID.

```sql
DELETE FROM cloudflare.realtime_kit.meetings
WHERE meeting_id = '{{ meeting_id }}' --required
AND participant_id = '{{ participant_id }}' --required
AND account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
;
```
</TabItem>
</Tabs>
