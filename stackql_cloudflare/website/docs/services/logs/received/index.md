--- 
title: received
hide_title: false
hide_table_of_contents: false
keywords:
  - received
  - logs
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

Creates, updates, deletes, gets or lists a <code>received</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="received" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logs.received" /></td></tr>
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

Get logs received response

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
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-end"><code>end</code></a>, <a href="#parameter-fields"><code>fields</code></a>, <a href="#parameter-sample"><code>sample</code></a>, <a href="#parameter-count"><code>count</code></a>, <a href="#parameter-timestamps"><code>timestamps</code></a></td>
    <td>The `/received` api route allows customers to retrieve their edge HTTP logs. The basic access pattern is "give me all the logs for zone Z for minute M", where the minute M refers to the time records were received at Cloudflare's central data center. `start` is inclusive, and `end` is exclusive. Because of that, to get all data, at minutely cadence, starting at 10AM, the proper values are: `start=2018-05-20T10:00:00Z&end=2018-05-20T10:01:00Z`, then `start=2018-05-20T10:01:00Z&end=2018-05-20T10:02:00Z` and so on; the overlap will be handled properly.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-count">
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-end">
    <td><CopyableCode code="end" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-fields">
    <td><CopyableCode code="fields" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sample">
    <td><CopyableCode code="sample" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-timestamps">
    <td><CopyableCode code="timestamps" /></td>
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

The `/received` api route allows customers to retrieve their edge HTTP logs. The basic access pattern is "give me all the logs for zone Z for minute M", where the minute M refers to the time records were received at Cloudflare's central data center. `start` is inclusive, and `end` is exclusive. Because of that, to get all data, at minutely cadence, starting at 10AM, the proper values are: `start=2018-05-20T10:00:00Z&end=2018-05-20T10:01:00Z`, then `start=2018-05-20T10:01:00Z&end=2018-05-20T10:02:00Z` and so on; the overlap will be handled properly.

```sql
SELECT
contents
FROM cloudflare.logs.received
WHERE zone_id = '{{ zone_id }}' -- required
AND start = '{{ start }}'
AND end = '{{ end }}'
AND fields = '{{ fields }}'
AND sample = '{{ sample }}'
AND count = '{{ count }}'
AND timestamps = '{{ timestamps }}'
;
```
</TabItem>
</Tabs>
