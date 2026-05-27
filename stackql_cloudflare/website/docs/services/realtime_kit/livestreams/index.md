--- 
title: livestreams
hide_title: false
hide_table_of_contents: false
keywords:
  - livestreams
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

Creates, updates, deletes, gets or lists a <code>livestreams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="livestreams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.livestreams" /></td></tr>
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
    <td><a href="#start_livestreaming_a_meeting"><CopyableCode code="start_livestreaming_a_meeting" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Starts livestream of a meeting associated with the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.</td>
</tr>
<tr>
    <td><a href="#create_independent_livestream"><CopyableCode code="create_independent_livestream" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Creates a livestream for the given App ID and returns ingest server, stream key, and playback URL. You can pass custom input to the ingest server and stream key, and freely distribute the content using the playback URL on any player that supports HLS/LHLS.</td>
</tr>
<tr>
    <td><a href="#stop_livestreaming_a_meeting"><CopyableCode code="stop_livestreaming_a_meeting" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Stops the active livestream of a meeting associated with the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="start_livestreaming_a_meeting"
    values={[
        { label: 'start_livestreaming_a_meeting', value: 'start_livestreaming_a_meeting' },
        { label: 'create_independent_livestream', value: 'create_independent_livestream' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="start_livestreaming_a_meeting">

Starts livestream of a meeting associated with the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.

```sql
INSERT INTO cloudflare.realtime_kit.livestreams (
name,
video_config,
meeting_id,
account_id,
app_id
)
SELECT 
'{{ name }}',
'{{ video_config }}',
'{{ meeting_id }}',
'{{ account_id }}',
'{{ app_id }}'
RETURNING
data,
success
;
```
</TabItem>
<TabItem value="create_independent_livestream">

Creates a livestream for the given App ID and returns ingest server, stream key, and playback URL. You can pass custom input to the ingest server and stream key, and freely distribute the content using the playback URL on any player that supports HLS/LHLS.

```sql
INSERT INTO cloudflare.realtime_kit.livestreams (
name,
account_id,
app_id
)
SELECT 
'{{ name }}',
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
- name: livestreams
  props:
    - name: meeting_id
      value: "{{ meeting_id }}"
      description: Required parameter for the livestreams resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the livestreams resource.
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the livestreams resource.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the livestream
    - name: video_config
      value:
        height: {{ height }}
        width: {{ width }}
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop_livestreaming_a_meeting"
    values={[
        { label: 'stop_livestreaming_a_meeting', value: 'stop_livestreaming_a_meeting' }
    ]}
>
<TabItem value="stop_livestreaming_a_meeting">

Stops the active livestream of a meeting associated with the given meeting ID. Retreive the meeting ID using the `Create a meeting` API.

```sql
EXEC cloudflare.realtime_kit.livestreams.stop_livestreaming_a_meeting 
@meeting_id='{{ meeting_id }}' --required, 
@account_id='{{ account_id }}' --required, 
@app_id='{{ app_id }}' --required
;
```
</TabItem>
</Tabs>
