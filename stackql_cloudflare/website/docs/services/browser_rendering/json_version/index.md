--- 
title: json_version
hide_title: false
hide_table_of_contents: false
keywords:
  - json_version
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

Creates, updates, deletes, gets or lists a <code>json_version</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="json_version" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.browser_rendering.json_version" /></td></tr>
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

Browser version information.

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
    <td><CopyableCode code="Browser" /></td>
    <td><code>string</code></td>
    <td>Browser name and version.</td>
</tr>
<tr>
    <td><CopyableCode code="Protocol-Version" /></td>
    <td><code>string</code></td>
    <td>Chrome DevTools Protocol version.</td>
</tr>
<tr>
    <td><CopyableCode code="User-Agent" /></td>
    <td><code>string</code></td>
    <td>User agent string.</td>
</tr>
<tr>
    <td><CopyableCode code="V8-Version" /></td>
    <td><code>string</code></td>
    <td>V8 JavaScript engine version.</td>
</tr>
<tr>
    <td><CopyableCode code="WebKit-Version" /></td>
    <td><code>string</code></td>
    <td>WebKit version.</td>
</tr>
<tr>
    <td><CopyableCode code="webSocketDebuggerUrl" /></td>
    <td><code>string</code></td>
    <td>WebSocket URL for debugging the browser.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td></td>
    <td>Get browser version metadata.</td>
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

Get browser version metadata.

```sql
SELECT
Browser,
Protocol-Version,
User-Agent,
V8-Version,
WebKit-Version,
webSocketDebuggerUrl
FROM cloudflare.browser_rendering.json_version
WHERE account_id = '{{ account_id }}' -- required
AND session_id = '{{ session_id }}' -- required
;
```
</TabItem>
</Tabs>
