--- 
title: outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - outputs
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

Creates, updates, deletes, gets or lists an <code>outputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="outputs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.outputs" /></td></tr>
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

List all outputs associated with a specified live input response.

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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>When enabled, live video streamed to the associated live input will be sent to the output URL. When disabled, live video will not be sent to the output URL, even when streaming to the associated live input. Use this to control precisely when you start and stop simulcasting to specific destinations like YouTube and Twitch.</td>
</tr>
<tr>
    <td><CopyableCode code="streamKey" /></td>
    <td><code>string</code></td>
    <td>The streamKey used to authenticate against an output's target. (example: uzya-f19y-g2g9-a2ee-51j2)</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for the output. (example: baea4d9c515887b80289d5c33cf01145)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL an output uses to restream. (example: rtmp://a.rtmp.youtube.com/live2)</td>
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
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves all outputs associated with a specified live input.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-streamKey"><code>streamKey</code></a></td>
    <td></td>
    <td>Creates a new output that can be used to simulcast or restream live video to other RTMP or SRT destinations. Outputs are always linked to a specific live input — one live input can have many outputs.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-output_identifier"><code>output_identifier</code></a>, <a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Updates the state of an output.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-output_identifier"><code>output_identifier</code></a>, <a href="#parameter-live_input_identifier"><code>live_input_identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an output and removes it from the associated live input.</td>
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
<tr id="parameter-output_identifier">
    <td><CopyableCode code="output_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
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

Retrieves all outputs associated with a specified live input.

```sql
SELECT
enabled,
streamKey,
uid,
url
FROM cloudflare.streams.outputs
WHERE live_input_identifier = '{{ live_input_identifier }}' -- required
AND account_id = '{{ account_id }}' -- required
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

Creates a new output that can be used to simulcast or restream live video to other RTMP or SRT destinations. Outputs are always linked to a specific live input — one live input can have many outputs.

```sql
INSERT INTO cloudflare.streams.outputs (
enabled,
streamKey,
url,
live_input_identifier,
account_id
)
SELECT 
{{ enabled }},
'{{ streamKey }}' /* required */,
'{{ url }}' /* required */,
'{{ live_input_identifier }}',
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
- name: outputs
  props:
    - name: live_input_identifier
      value: "{{ live_input_identifier }}"
      description: Required parameter for the outputs resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the outputs resource.
    - name: enabled
      value: {{ enabled }}
      description: |
        When enabled, live video streamed to the associated live input will be sent to the output URL. When disabled, live video will not be sent to the output URL, even when streaming to the associated live input. Use this to control precisely when you start and stop simulcasting to specific destinations like YouTube and Twitch.
      default: true
    - name: streamKey
      value: "{{ streamKey }}"
      description: |
        The streamKey used to authenticate against an output's target.
    - name: url
      value: "{{ url }}"
      description: |
        The URL an output uses to restream.
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

Updates the state of an output.

```sql
REPLACE cloudflare.streams.outputs
SET 
enabled = {{ enabled }}
WHERE 
output_identifier = '{{ output_identifier }}' --required
AND live_input_identifier = '{{ live_input_identifier }}' --required
AND account_id = '{{ account_id }}' --required
AND enabled = {{ enabled }} --required
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

Deletes an output and removes it from the associated live input.

```sql
DELETE FROM cloudflare.streams.outputs
WHERE output_identifier = '{{ output_identifier }}' --required
AND live_input_identifier = '{{ live_input_identifier }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
