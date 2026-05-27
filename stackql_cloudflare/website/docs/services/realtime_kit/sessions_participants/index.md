--- 
title: sessions_participants
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions_participants
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

Creates, updates, deletes, gets or lists a <code>sessions_participants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sessions_participants" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.sessions_participants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Returns details of a participant along with callstats data.

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
<TabItem value="list">

Get participants list of a particular session

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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-participant_id"><code>participant_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td><a href="#parameter-filters"><code>filters</code></a>, <a href="#parameter-include_peer_events"><code>include_peer_events</code></a></td>
    <td>Returns details of the given participant ID along with call statistics for the given session ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td><a href="#parameter-search"><code>search</code></a>, <a href="#parameter-page_no"><code>page_no</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-include_peer_events"><code>include_peer_events</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Returns a list of participants for the given session ID.</td>
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
<tr id="parameter-participant_id">
    <td><CopyableCode code="participant_id" /></td>
    <td><code>string</code></td>
    <td>ID of the participant</td>
</tr>
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The session ID.</td>
</tr>
<tr id="parameter-filters">
    <td><CopyableCode code="filters" /></td>
    <td><code>string</code></td>
    <td>Comma separated list of filters to apply. Note that there must be no spaces between the filters.</td>
</tr>
<tr id="parameter-include_peer_events">
    <td><CopyableCode code="include_peer_events" /></td>
    <td><code>boolean</code></td>
    <td>if true, response includes all the peer events of participants.</td>
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
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>In breakout room sessions, the view parameter can be set to `raw` for session specific duration for participants or `consolidated` to accumulate breakout room durations.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Returns details of the given participant ID along with call statistics for the given session ID.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.sessions_participants
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND participant_id = '{{ participant_id }}' -- required
AND session_id = '{{ session_id }}' -- required
AND filters = '{{ filters }}'
AND include_peer_events = '{{ include_peer_events }}'
;
```
</TabItem>
<TabItem value="list">

Returns a list of participants for the given session ID.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.sessions_participants
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND session_id = '{{ session_id }}' -- required
AND search = '{{ search }}'
AND page_no = '{{ page_no }}'
AND per_page = '{{ per_page }}'
AND sort_order = '{{ sort_order }}'
AND sort_by = '{{ sort_by }}'
AND include_peer_events = '{{ include_peer_events }}'
AND view = '{{ view }}'
;
```
</TabItem>
</Tabs>
