--- 
title: browser
hide_title: false
hide_table_of_contents: false
keywords:
  - browser
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

Creates, updates, deletes, gets or lists a <code>browser</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="browser" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.browser_rendering.browser" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-keep_alive"><code>keep_alive</code></a>, <a href="#parameter-lab"><code>lab</code></a>, <a href="#parameter-targets"><code>targets</code></a>, <a href="#parameter-recording"><code>recording</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td></td>
    <td>Closes an existing browser session.</td>
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
<tr id="parameter-keep_alive">
    <td><CopyableCode code="keep_alive" /></td>
    <td><code>number</code></td>
    <td>Keep-alive time in milliseconds.</td>
</tr>
<tr id="parameter-lab">
    <td><CopyableCode code="lab" /></td>
    <td><code>boolean</code></td>
    <td>Use experimental browser.</td>
</tr>
<tr id="parameter-recording">
    <td><CopyableCode code="recording" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-targets">
    <td><CopyableCode code="targets" /></td>
    <td><code>boolean</code></td>
    <td>Include browser targets in response.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

No description available.

```sql
INSERT INTO cloudflare.browser_rendering.browser (
account_id,
keep_alive,
lab,
targets,
recording
)
SELECT 
'{{ account_id }}',
'{{ keep_alive }}',
'{{ lab }}',
'{{ targets }}',
'{{ recording }}'
RETURNING
sessionId,
webSocketDebuggerUrl
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: browser
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the browser resource.
    - name: keep_alive
      value: {{ keep_alive }}
      description: Keep-alive time in milliseconds.
      description: Keep-alive time in milliseconds.
    - name: lab
      value: {{ lab }}
      description: Use experimental browser.
      description: Use experimental browser.
    - name: targets
      value: {{ targets }}
      description: Include browser targets in response.
      description: Include browser targets in response.
    - name: recording
      value: {{ recording }}
`}</CodeBlock>

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

Closes an existing browser session.

```sql
DELETE FROM cloudflare.browser_rendering.browser
WHERE account_id = '{{ account_id }}' --required
AND session_id = '{{ session_id }}' --required
;
```
</TabItem>
</Tabs>
