--- 
title: session
hide_title: false
hide_table_of_contents: false
keywords:
  - session
  - browser_rendering
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

Creates, updates, deletes, gets or lists a <code>session</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="session" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.browser_rendering.session" /></td></tr>
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

Returns the session details.

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
    <td><CopyableCode code="closeReason" /></td>
    <td><code>string</code></td>
    <td>Reason for session closure.</td>
</tr>
<tr>
    <td><CopyableCode code="closeReasonText" /></td>
    <td><code>string</code></td>
    <td>Human-readable close reason.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionEndTime" /></td>
    <td><code>number</code></td>
    <td>Connection end time.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionId" /></td>
    <td><code>string</code></td>
    <td>Connection ID.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStartTime" /></td>
    <td><code>number</code></td>
    <td>Connection start time.</td>
</tr>
<tr>
    <td><CopyableCode code="devtoolsFrontendUrl" /></td>
    <td><code>string</code></td>
    <td>DevTools frontend URL.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>number</code></td>
    <td>Session end time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>number</code></td>
    <td>Last updated timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Session ID.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>number</code></td>
    <td>Session start time.</td>
</tr>
<tr>
    <td><CopyableCode code="webSocketDebuggerUrl" /></td>
    <td><code>string</code></td>
    <td>WebSocket URL for debugging this target.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns the account's sessions.

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
    <td><CopyableCode code="closeReason" /></td>
    <td><code>string</code></td>
    <td>Reason for session closure.</td>
</tr>
<tr>
    <td><CopyableCode code="closeReasonText" /></td>
    <td><code>string</code></td>
    <td>Human-readable close reason.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionEndTime" /></td>
    <td><code>number</code></td>
    <td>Connection end time.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionId" /></td>
    <td><code>string</code></td>
    <td>Connection ID.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStartTime" /></td>
    <td><code>number</code></td>
    <td>Connection start time.</td>
</tr>
<tr>
    <td><CopyableCode code="devtoolsFrontendUrl" /></td>
    <td><code>string</code></td>
    <td>DevTools frontend URL.</td>
</tr>
<tr>
    <td><CopyableCode code="endTime" /></td>
    <td><code>number</code></td>
    <td>Session end time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>number</code></td>
    <td>Last updated timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="sessionId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Session ID.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>number</code></td>
    <td>Session start time.</td>
</tr>
<tr>
    <td><CopyableCode code="webSocketDebuggerUrl" /></td>
    <td><code>string</code></td>
    <td>WebSocket URL for debugging this target.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td></td>
    <td>Get details for a specific browser session.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a></td>
    <td>List active browser sessions.</td>
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
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The session ID.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>number</code></td>
    <td></td>
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

Get details for a specific browser session.

```sql
SELECT
closeReason,
closeReasonText,
connectionEndTime,
connectionId,
connectionStartTime,
devtoolsFrontendUrl,
endTime,
lastUpdated,
sessionId,
startTime,
webSocketDebuggerUrl
FROM cloudflare.browser_rendering.session
WHERE account_id = '{{ account_id }}' -- required
AND session_id = '{{ session_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List active browser sessions.

```sql
SELECT
closeReason,
closeReasonText,
connectionEndTime,
connectionId,
connectionStartTime,
devtoolsFrontendUrl,
endTime,
lastUpdated,
sessionId,
startTime,
webSocketDebuggerUrl
FROM cloudflare.browser_rendering.session
WHERE account_id = '{{ account_id }}' -- required
AND limit = '{{ limit }}'
AND offset = '{{ offset }}'
;
```
</TabItem>
</Tabs>
