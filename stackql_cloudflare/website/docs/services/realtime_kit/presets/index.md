--- 
title: presets
hide_title: false
hide_table_of_contents: false
keywords:
  - presets
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

Creates, updates, deletes, gets or lists a <code>presets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="presets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.presets" /></td></tr>
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
    <td>Data returned by the operation (title: Preset)</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Success status of the operation</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Example response

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
    <td>ID of the preset</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the preset</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp this preset was created at</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp this preset was last updated</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-preset_id"><code>preset_id</code></a></td>
    <td></td>
    <td>Fetches details of a preset using the provided preset ID</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page_no"><code>page_no</code></a></td>
    <td>Fetches all the presets belonging to an App.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-config"><code>config</code></a>, <a href="#parameter-ui"><code>ui</code></a></td>
    <td></td>
    <td>Creates a preset belonging to the current App</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-preset_id"><code>preset_id</code></a></td>
    <td></td>
    <td>Update a preset by the provided preset ID</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-preset_id"><code>preset_id</code></a></td>
    <td></td>
    <td>Deletes a preset using the provided preset ID</td>
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
<tr id="parameter-preset_id">
    <td><CopyableCode code="preset_id" /></td>
    <td><code>string</code></td>
    <td>ID of the preset to fetch</td>
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

Fetches details of a preset using the provided preset ID

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.presets
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND preset_id = '{{ preset_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches all the presets belonging to an App.

```sql
SELECT
id,
name,
created_at,
updated_at
FROM cloudflare.realtime_kit.presets
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND per_page = '{{ per_page }}'
AND page_no = '{{ page_no }}'
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

Creates a preset belonging to the current App

```sql
INSERT INTO cloudflare.realtime_kit.presets (
config,
name,
permissions,
ui,
account_id,
app_id
)
SELECT 
'{{ config }}' /* required */,
'{{ name }}' /* required */,
'{{ permissions }}',
'{{ ui }}' /* required */,
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
- name: presets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the presets resource.
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the presets resource.
    - name: config
      value:
        max_screenshare_count: {{ max_screenshare_count }}
        max_video_streams:
          desktop: {{ desktop }}
          mobile: {{ mobile }}
        media:
          audio:
            enable_high_bitrate: {{ enable_high_bitrate }}
            enable_stereo: {{ enable_stereo }}
          screenshare:
            frame_rate: {{ frame_rate }}
            quality: "{{ quality }}"
          video:
            frame_rate: {{ frame_rate }}
            quality: "{{ quality }}"
        view_type: "{{ view_type }}"
    - name: name
      value: "{{ name }}"
      description: |
        Name of the preset
    - name: permissions
      value:
        accept_waiting_requests: {{ accept_waiting_requests }}
        can_accept_production_requests: {{ can_accept_production_requests }}
        can_change_participant_permissions: {{ can_change_participant_permissions }}
        can_edit_display_name: {{ can_edit_display_name }}
        can_livestream: {{ can_livestream }}
        can_record: {{ can_record }}
        can_spotlight: {{ can_spotlight }}
        chat:
          private:
            can_receive: {{ can_receive }}
            can_send: {{ can_send }}
            files: {{ files }}
            text: {{ text }}
          public:
            can_send: {{ can_send }}
            files: {{ files }}
            text: {{ text }}
        connected_meetings:
          can_alter_connected_meetings: {{ can_alter_connected_meetings }}
          can_switch_connected_meetings: {{ can_switch_connected_meetings }}
          can_switch_to_parent_meeting: {{ can_switch_to_parent_meeting }}
        disable_participant_audio: {{ disable_participant_audio }}
        disable_participant_screensharing: {{ disable_participant_screensharing }}
        disable_participant_video: {{ disable_participant_video }}
        hidden_participant: {{ hidden_participant }}
        is_recorder: {{ is_recorder }}
        kick_participant: {{ kick_participant }}
        media:
          audio:
            can_produce: "{{ can_produce }}"
          screenshare:
            can_produce: "{{ can_produce }}"
          video:
            can_produce: "{{ can_produce }}"
        pin_participant: {{ pin_participant }}
        plugins:
          can_close: {{ can_close }}
          can_edit_config: {{ can_edit_config }}
          can_start: {{ can_start }}
          config: "{{ config }}"
        polls:
          can_create: {{ can_create }}
          can_view: {{ can_view }}
          can_vote: {{ can_vote }}
        recorder_type: "{{ recorder_type }}"
        show_participant_list: {{ show_participant_list }}
        waiting_room_type: "{{ waiting_room_type }}"
    - name: ui
      value:
        config_diff: "{{ config_diff }}"
        design_tokens:
          border_radius: "{{ border_radius }}"
          border_width: "{{ border_width }}"
          colors:
            background:
              600: "{{ 600 }}"
              700: "{{ 700 }}"
              800: "{{ 800 }}"
              900: "{{ 900 }}"
              1000: "{{ 1000 }}"
            brand:
              300: "{{ 300 }}"
              400: "{{ 400 }}"
              500: "{{ 500 }}"
              600: "{{ 600 }}"
              700: "{{ 700 }}"
            danger: "{{ danger }}"
            success: "{{ success }}"
            text: "{{ text }}"
            text_on_brand: "{{ text_on_brand }}"
            video_bg: "{{ video_bg }}"
            warning: "{{ warning }}"
          logo: "{{ logo }}"
          spacing_base: {{ spacing_base }}
          theme: "{{ theme }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a preset by the provided preset ID

```sql
UPDATE cloudflare.realtime_kit.presets
SET 
config = '{{ config }}',
name = '{{ name }}',
permissions = '{{ permissions }}',
ui = '{{ ui }}'
WHERE 
account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
AND preset_id = '{{ preset_id }}' --required
RETURNING
data,
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

Deletes a preset using the provided preset ID

```sql
DELETE FROM cloudflare.realtime_kit.presets
WHERE account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
AND preset_id = '{{ preset_id }}' --required
;
```
</TabItem>
</Tabs>
