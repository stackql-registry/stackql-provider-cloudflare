--- 
title: audio_tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - audio_tracks
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

Creates, updates, deletes, gets or lists an <code>audio_tracks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="audio_tracks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.audio_tracks" /></td></tr>
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

Lists additional audio tracks on a video.

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
    <td><CopyableCode code="default" /></td>
    <td><code>boolean</code></td>
    <td>Denotes whether the audio track will be played by default in a player.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>A string to uniquely identify the track amongst other audio track labels for the specified video. (example: director commentary)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies the processing status of the video. (queued, ready, error)</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>A Cloudflare-generated unique identifier for a media item. (example: ea95132c15732412d22c1476fa83f27a)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-identifier"><code>identifier</code></a></td>
    <td></td>
    <td>Lists additional audio tracks on a video. Note this API will not return information for audio attached to the video upload.</td>
</tr>
<tr>
    <td><a href="#copy"><CopyableCode code="copy" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-label"><code>label</code></a></td>
    <td></td>
    <td>Adds an additional audio track to a video using the provided audio track URL.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-audio_identifier"><code>audio_identifier</code></a></td>
    <td></td>
    <td>Edits additional audio tracks on a video. Editing the default status of an audio track to `true` will mark all other audio tracks on the video default status to `false`.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-audio_identifier"><code>audio_identifier</code></a></td>
    <td></td>
    <td>Deletes additional audio tracks on a video. Deleting a default audio track is not allowed. You must assign another audio track as default prior to deletion.</td>
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
<tr id="parameter-audio_identifier">
    <td><CopyableCode code="audio_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-identifier">
    <td><CopyableCode code="identifier" /></td>
    <td><code>string</code></td>
    <td>Resource identifier.</td>
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

Lists additional audio tracks on a video. Note this API will not return information for audio attached to the video upload.

```sql
SELECT
default,
label,
status,
uid
FROM cloudflare.streams.audio_tracks
WHERE account_id = '{{ account_id }}' -- required
AND identifier = '{{ identifier }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="copy"
    values={[
        { label: 'copy', value: 'copy' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="copy">

Adds an additional audio track to a video using the provided audio track URL.

```sql
INSERT INTO cloudflare.streams.audio_tracks (
label,
url,
account_id,
identifier
)
SELECT 
'{{ label }}' /* required */,
'{{ url }}',
'{{ account_id }}',
'{{ identifier }}'
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
- name: audio_tracks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the audio_tracks resource.
    - name: identifier
      value: "{{ identifier }}"
      description: Required parameter for the audio_tracks resource.
    - name: label
      value: "{{ label }}"
      description: |
        A string to uniquely identify the track amongst other audio track labels for the specified video.
    - name: url
      value: "{{ url }}"
      description: |
        An audio track URL. The server must be publicly routable and support \`HTTP HEAD\` requests and \`HTTP GET\` range requests. The server should respond to \`HTTP HEAD\` requests with a \`content-range\` header that includes the size of the file.
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

Edits additional audio tracks on a video. Editing the default status of an audio track to `true` will mark all other audio tracks on the video default status to `false`.

```sql
UPDATE cloudflare.streams.audio_tracks
SET 
default = {{ default }},
label = '{{ label }}'
WHERE 
account_id = '{{ account_id }}' --required
AND identifier = '{{ identifier }}' --required
AND audio_identifier = '{{ audio_identifier }}' --required
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

Deletes additional audio tracks on a video. Deleting a default audio track is not allowed. You must assign another audio track as default prior to deletion.

```sql
DELETE FROM cloudflare.streams.audio_tracks
WHERE account_id = '{{ account_id }}' --required
AND identifier = '{{ identifier }}' --required
AND audio_identifier = '{{ audio_identifier }}' --required
;
```
</TabItem>
</Tabs>
