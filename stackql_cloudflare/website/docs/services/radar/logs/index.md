--- 
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
  - radar
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

Creates, updates, deletes, gets or lists a <code>logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="logs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.logs" /></td></tr>
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

Successful response.

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
    <td><CopyableCode code="certificateLog" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Successful response.

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
    <td><CopyableCode code="api" /></td>
    <td><code>string</code></td>
    <td>The API standard that the certificate log follows. (RFC6962, STATIC)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A brief description of the certificate log.</td>
</tr>
<tr>
    <td><CopyableCode code="endExclusive" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date and time for when the log will stop accepting certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="operator" /></td>
    <td><code>string</code></td>
    <td>The organization responsible for operating the certificate log.</td>
</tr>
<tr>
    <td><CopyableCode code="slug" /></td>
    <td><code>string</code></td>
    <td>A URL-friendly, kebab-case identifier for the certificate log.</td>
</tr>
<tr>
    <td><CopyableCode code="startInclusive" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start date and time for when the log starts accepting certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the certificate log. More details about log states can be found here: https://googlechrome.github.io/CertificateTransparency/log_states.html (USABLE, PENDING, QUALIFIED, READ_ONLY, RETIRED, REJECTED)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the log state was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL for the certificate log.</td>
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
    <td><a href="#parameter-log_slug"><code>log_slug</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the requested certificate log information.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves a list of certificate logs.</td>
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
<tr id="parameter-log_slug">
    <td><CopyableCode code="log_slug" /></td>
    <td><code>string</code></td>
    <td>Certificate log slug.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects returned in the response.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>Skips the specified number of objects before fetching the results.</td>
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

Retrieves the requested certificate log information.

```sql
SELECT
certificateLog
FROM cloudflare.radar.logs
WHERE log_slug = '{{ log_slug }}' -- required
AND format = '{{ format }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of certificate logs.

```sql
SELECT
api,
description,
endExclusive,
operator,
slug,
startInclusive,
state,
stateTimestamp,
url
FROM cloudflare.radar.logs
WHERE limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
