--- 
title: time_travel
hide_title: false
hide_table_of_contents: false
keywords:
  - time_travel
  - d1
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

Creates, updates, deletes, gets or lists a <code>time_travel</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="time_travel" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.d1.time_travel" /></td></tr>
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

Bookmark retrieved successfully

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
    <td><CopyableCode code="bookmark" /></td>
    <td><code>string</code></td>
    <td>A bookmark representing a specific state of the database at a specific point in time. (example: 00000001-00000002-00004e2f-0a83ea2fceebc654de0640c422be4653)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td><a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td>Retrieves the current bookmark, or the nearest bookmark at or before a provided timestamp. Bookmarks can be used with the restore endpoint to revert the database to a previous point in time.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td><a href="#parameter-bookmark"><code>bookmark</code></a>, <a href="#parameter-timestamp"><code>timestamp</code></a></td>
    <td>Restores a D1 database to a previous point in time either via a bookmark or a timestamp.</td>
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
<tr id="parameter-database_id">
    <td><CopyableCode code="database_id" /></td>
    <td><code>string</code></td>
    <td>The D1 database ID.</td>
</tr>
<tr id="parameter-bookmark">
    <td><CopyableCode code="bookmark" /></td>
    <td><code>string</code></td>
    <td>A bookmark to restore the database to. Required if `timestamp` is not provided.</td>
</tr>
<tr id="parameter-timestamp">
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>An ISO 8601 timestamp to restore the database to. Required if `bookmark` is not provided.</td>
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

Retrieves the current bookmark, or the nearest bookmark at or before a provided timestamp. Bookmarks can be used with the restore endpoint to revert the database to a previous point in time.

```sql
SELECT
bookmark
FROM cloudflare.d1.time_travel
WHERE account_id = '{{ account_id }}' -- required
AND database_id = '{{ database_id }}' -- required
AND timestamp = '{{ timestamp }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restore"
    values={[
        { label: 'restore', value: 'restore' }
    ]}
>
<TabItem value="restore">

Restores a D1 database to a previous point in time either via a bookmark or a timestamp.

```sql
EXEC cloudflare.d1.time_travel.restore 
@account_id='{{ account_id }}' --required, 
@database_id='{{ database_id }}' --required, 
@bookmark='{{ bookmark }}', 
@timestamp='{{ timestamp }}'
;
```
</TabItem>
</Tabs>
