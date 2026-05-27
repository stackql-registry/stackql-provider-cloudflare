--- 
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
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

Creates, updates, deletes, gets or lists a <code>sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.sessions" /></td></tr>
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

Get all sessions success response

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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-page_no"><code>page_no</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-start_time"><code>start_time</code></a>, <a href="#parameter-end_time"><code>end_time</code></a>, <a href="#parameter-participants"><code>participants</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-associated_id"><code>associated_id</code></a></td>
    <td>Returns details of all sessions of an App.</td>
</tr>
<tr>
    <td><a href="#generate_summary_of_transcripts"><CopyableCode code="generate_summary_of_transcripts" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td></td>
    <td>Trigger Summary generation of Transcripts for the session ID.</td>
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
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The session ID.</td>
</tr>
<tr id="parameter-associated_id">
    <td><CopyableCode code="associated_id" /></td>
    <td><code>string</code></td>
    <td>ID of the meeting that sessions should be associated with</td>
</tr>
<tr id="parameter-end_time">
    <td><CopyableCode code="end_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time range for which you want to retrieve the meetings. The time must be specified in ISO format.</td>
</tr>
<tr id="parameter-page_no">
    <td><CopyableCode code="page_no" /></td>
    <td><code>number</code></td>
    <td>The page number from which you want your page search results to be displayed.</td>
</tr>
<tr id="parameter-participants">
    <td><CopyableCode code="participants" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Number of results per page</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Search string that matches sessions based on meeting title, meeting ID, and session ID</td>
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

Returns details of all sessions of an App.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.sessions
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND page_no = '{{ page_no }}'
AND per_page = '{{ per_page }}'
AND sort_by = '{{ sort_by }}'
AND sort_order = '{{ sort_order }}'
AND start_time = '{{ start_time }}'
AND end_time = '{{ end_time }}'
AND participants = '{{ participants }}'
AND status = '{{ status }}'
AND search = '{{ search }}'
AND associated_id = '{{ associated_id }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="generate_summary_of_transcripts"
    values={[
        { label: 'generate_summary_of_transcripts', value: 'generate_summary_of_transcripts' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="generate_summary_of_transcripts">

Trigger Summary generation of Transcripts for the session ID.

```sql
INSERT INTO cloudflare.realtime_kit.sessions (
account_id,
app_id,
session_id
)
SELECT 
'{{ account_id }}',
'{{ app_id }}',
'{{ session_id }}'
RETURNING
data,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sessions
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the sessions resource.
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the sessions resource.
    - name: session_id
      value: "{{ session_id }}"
      description: Required parameter for the sessions resource.
`}</CodeBlock>

</TabItem>
</Tabs>
