--- 
title: pages_trend
hide_title: false
hide_table_of_contents: false
keywords:
  - pages_trend
  - speed
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

Creates, updates, deletes, gets or lists a <code>pages_trend</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pages_trend" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.speed.pages_trend" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_zone"
    values={[
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_zone">

Page trend.

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
    <td><CopyableCode code="cls" /></td>
    <td><code>array</code></td>
    <td>Cumulative Layout Shift trend.</td>
</tr>
<tr>
    <td><CopyableCode code="fcp" /></td>
    <td><code>array</code></td>
    <td>First Contentful Paint trend.</td>
</tr>
<tr>
    <td><CopyableCode code="lcp" /></td>
    <td><code>array</code></td>
    <td>Largest Contentful Paint trend.</td>
</tr>
<tr>
    <td><CopyableCode code="performanceScore" /></td>
    <td><code>array</code></td>
    <td>The Lighthouse score trend.</td>
</tr>
<tr>
    <td><CopyableCode code="si" /></td>
    <td><code>array</code></td>
    <td>Speed Index trend.</td>
</tr>
<tr>
    <td><CopyableCode code="tbt" /></td>
    <td><code>array</code></td>
    <td>Total Blocking Time trend.</td>
</tr>
<tr>
    <td><CopyableCode code="ttfb" /></td>
    <td><code>array</code></td>
    <td>Time To First Byte trend.</td>
</tr>
<tr>
    <td><CopyableCode code="tti" /></td>
    <td><code>array</code></td>
    <td>Time To Interactive trend.</td>
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
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-region"><code>region</code></a>, <a href="#parameter-deviceType"><code>deviceType</code></a>, <a href="#parameter-start"><code>start</code></a>, <a href="#parameter-end"><code>end</code></a>, <a href="#parameter-tz"><code>tz</code></a>, <a href="#parameter-metrics"><code>metrics</code></a></td>
    <td>Lists the core web vital metrics trend over time for a specific page.</td>
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
<tr id="parameter-url">
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-deviceType">
    <td><CopyableCode code="deviceType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-end">
    <td><CopyableCode code="end" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-metrics">
    <td><CopyableCode code="metrics" /></td>
    <td><code>string</code></td>
    <td>A comma-separated list of metrics to include in the results.</td>
</tr>
<tr id="parameter-region">
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-tz">
    <td><CopyableCode code="tz" /></td>
    <td><code>string</code></td>
    <td>The timezone of the start and end timestamps.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_zone"
    values={[
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_zone">

Lists the core web vital metrics trend over time for a specific page.

```sql
SELECT
cls,
fcp,
lcp,
performanceScore,
si,
tbt,
ttfb,
tti
FROM cloudflare.speed.pages_trend
WHERE zone_id = '{{ zone_id }}' -- required
AND url = '{{ url }}' -- required
AND region = '{{ region }}'
AND deviceType = '{{ deviceType }}'
AND start = '{{ start }}'
AND end = '{{ end }}'
AND tz = '{{ tz }}'
AND metrics = '{{ metrics }}'
;
```
</TabItem>
</Tabs>
