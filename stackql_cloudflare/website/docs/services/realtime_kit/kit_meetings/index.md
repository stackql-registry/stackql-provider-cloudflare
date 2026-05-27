--- 
title: kit_meetings
hide_title: false
hide_table_of_contents: false
keywords:
  - kit_meetings
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

Creates, updates, deletes, gets or lists a <code>kit_meetings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kit_meetings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.kit_meetings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get_by_account">

Success Response

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
    <td>Data returned by the operation</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Success status of the operation</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

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
    <td>ID of the meeting.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp the object was created at. The time is returned in ISO format.</td>
</tr>
<tr>
    <td><CopyableCode code="live_stream_on_start" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the meeting should start getting livestreamed on start.</td>
</tr>
<tr>
    <td><CopyableCode code="persist_chat" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if Chat within a meeting should persist for a week.</td>
</tr>
<tr>
    <td><CopyableCode code="record_on_start" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if the meeting should start getting recorded as soon as someone joins the meeting.</td>
</tr>
<tr>
    <td><CopyableCode code="session_keep_alive_time_in_secs" /></td>
    <td><code>number</code></td>
    <td>Time in seconds, for which a session remains active, after the last participant has left the meeting.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Whether the meeting is `ACTIVE` or `INACTIVE`. Users will not be able to join an `INACTIVE` meeting. (ACTIVE, INACTIVE)</td>
</tr>
<tr>
    <td><CopyableCode code="summarize_on_end" /></td>
    <td><code>boolean</code></td>
    <td>Automatically generate summary of meetings using transcripts. Requires Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title of the meeting.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp the object was updated at. The time is returned in ISO format.</td>
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
    <td><a href="#parameter-meeting_id"><code>meeting_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a></td>
    <td>Returns a meeting details in an App for the given meeting ID.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-page_no"><code>page_no</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-start_time"><code>start_time</code></a>, <a href="#parameter-end_time"><code>end_time</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Returns all meetings for the given App ID.</td>
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
<tr id="parameter-end_time">
    <td><CopyableCode code="end_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time range for which you want to retrieve the meetings. The time must be specified in ISO format.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
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
<tr id="parameter-start_time">
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time range for which you want to retrieve the meetings. The time must be specified in ISO format.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get_by_account">

Returns a meeting details in an App for the given meeting ID.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.kit_meetings
WHERE meeting_id = '{{ meeting_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND name = '{{ name }}'
;
```
</TabItem>
<TabItem value="list_by_account">

Returns all meetings for the given App ID.

```sql
SELECT
id,
created_at,
live_stream_on_start,
persist_chat,
record_on_start,
session_keep_alive_time_in_secs,
status,
summarize_on_end,
title,
updated_at
FROM cloudflare.realtime_kit.kit_meetings
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND page_no = '{{ page_no }}'
AND per_page = '{{ per_page }}'
AND start_time = '{{ start_time }}'
AND end_time = '{{ end_time }}'
AND search = '{{ search }}'
;
```
</TabItem>
</Tabs>
