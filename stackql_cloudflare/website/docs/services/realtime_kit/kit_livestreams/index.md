--- 
title: kit_livestreams
hide_title: false
hide_table_of_contents: false
keywords:
  - kit_livestreams
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

Creates, updates, deletes, gets or lists a <code>kit_livestreams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="kit_livestreams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.kit_livestreams" /></td></tr>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-livestream_id"><code>livestream_id</code></a></td>
    <td><a href="#parameter-page_no"><code>page_no</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Returns details of a livestream with sessions for the given livestream ID. Retreive the livestream ID using the `Start livestreaming a meeting` API.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-exclude_meetings"><code>exclude_meetings</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page_no"><code>page_no</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-start_time"><code>start_time</code></a>, <a href="#parameter-end_time"><code>end_time</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a></td>
    <td>Returns details of livestreams associated with the given App ID. It includes livestreams created by your App and RealtimeKit meetings that are livestreamed by your App. If you only want details of livestreams created by your App and not RealtimeKit meetings, you can use the `exclude_meetings` query parameter.</td>
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
<tr id="parameter-livestream_id">
    <td><CopyableCode code="livestream_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-end_time">
    <td><CopyableCode code="end_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specify the end time range in ISO format to access the live stream.</td>
</tr>
<tr id="parameter-exclude_meetings">
    <td><CopyableCode code="exclude_meetings" /></td>
    <td><code>boolean</code></td>
    <td>Exclude the RealtimeKit meetings that are livestreamed.</td>
</tr>
<tr id="parameter-page_no">
    <td><CopyableCode code="page_no" /></td>
    <td><code>integer</code></td>
    <td>The page number from which you want your page search results to be displayed.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of results per page.</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>Specifies the sorting order for the results.</td>
</tr>
<tr id="parameter-start_time">
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specify the start time range in ISO format to access the live stream.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of the operation.</td>
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

Returns details of a livestream with sessions for the given livestream ID. Retreive the livestream ID using the `Start livestreaming a meeting` API.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.kit_livestreams
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND livestream_id = '{{ livestream_id }}' -- required
AND page_no = '{{ page_no }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list">

Returns details of livestreams associated with the given App ID. It includes livestreams created by your App and RealtimeKit meetings that are livestreamed by your App. If you only want details of livestreams created by your App and not RealtimeKit meetings, you can use the `exclude_meetings` query parameter.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.kit_livestreams
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND exclude_meetings = '{{ exclude_meetings }}'
AND per_page = '{{ per_page }}'
AND page_no = '{{ page_no }}'
AND status = '{{ status }}'
AND start_time = '{{ start_time }}'
AND end_time = '{{ end_time }}'
AND sort_order = '{{ sort_order }}'
;
```
</TabItem>
</Tabs>
