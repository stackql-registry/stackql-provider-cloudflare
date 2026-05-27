--- 
title: origins_timeseries_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - origins_timeseries_groups
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

Creates, updates, deletes, gets or lists an <code>origins_timeseries_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="origins_timeseries_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.origins_timeseries_groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Metadata for the results.</td>
</tr>
<tr>
    <td><CopyableCode code="serie_0" /></td>
    <td><code>object</code></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-dimension"><code>dimension</code></a></td>
    <td><a href="#parameter-aggInterval"><code>aggInterval</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-limitPerGroup"><code>limitPerGroup</code></a>, <a href="#parameter-origin"><code>origin</code></a>, <a href="#parameter-metric"><code>metric</code></a>, <a href="#parameter-region"><code>region</code></a>, <a href="#parameter-normalization"><code>normalization</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the distribution of origin metrics grouped by the specified dimension over time.</td>
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
<tr id="parameter-dimension">
    <td><CopyableCode code="dimension" /></td>
    <td><code>string</code></td>
    <td>Specifies the origin attribute by which to group the results.</td>
</tr>
<tr id="parameter-aggInterval">
    <td><CopyableCode code="aggInterval" /></td>
    <td><code>string</code></td>
    <td>Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).</td>
</tr>
<tr id="parameter-dateEnd">
    <td><CopyableCode code="dateEnd" /></td>
    <td><code>array</code></td>
    <td>End of the date range (inclusive).</td>
</tr>
<tr id="parameter-dateRange">
    <td><CopyableCode code="dateRange" /></td>
    <td><code>array</code></td>
    <td>Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).</td>
</tr>
<tr id="parameter-dateStart">
    <td><CopyableCode code="dateStart" /></td>
    <td><code>array</code></td>
    <td>Start of the date range.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-limitPerGroup">
    <td><CopyableCode code="limitPerGroup" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.</td>
</tr>
<tr id="parameter-metric">
    <td><CopyableCode code="metric" /></td>
    <td><code>string</code></td>
    <td>Specifies the metric to retrieve.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>array</code></td>
    <td>Array of names used to label the series in the response.</td>
</tr>
<tr id="parameter-normalization">
    <td><CopyableCode code="normalization" /></td>
    <td><code>string</code></td>
    <td>Normalization method applied to the results. Refer to [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).</td>
</tr>
<tr id="parameter-origin">
    <td><CopyableCode code="origin" /></td>
    <td><code>array</code></td>
    <td>Filters results by origin. Required for all dimensions except ORIGIN.</td>
</tr>
<tr id="parameter-region">
    <td><CopyableCode code="region" /></td>
    <td><code>array</code></td>
    <td>Filters results by origin region.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieves the distribution of origin metrics grouped by the specified dimension over time.

```sql
SELECT
meta,
serie_0
FROM cloudflare.radar.origins_timeseries_groups
WHERE dimension = '{{ dimension }}' -- required
AND aggInterval = '{{ aggInterval }}'
AND name = '{{ name }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND limitPerGroup = '{{ limitPerGroup }}'
AND origin = '{{ origin }}'
AND metric = '{{ metric }}'
AND region = '{{ region }}'
AND normalization = '{{ normalization }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
