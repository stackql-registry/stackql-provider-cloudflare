--- 
title: bots_timeseries_groups_dimension_5dbf28
hide_title: false
hide_table_of_contents: false
keywords:
  - bots_timeseries_groups_dimension_5dbf28
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

Creates, updates, deletes, gets or lists a <code>bots_timeseries_groups_dimension_5dbf28</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bots_timeseries_groups_dimension_5dbf28" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.bots_timeseries_groups_dimension_5dbf28" /></td></tr>
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
    <td><a href="#parameter-aggInterval"><code>aggInterval</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-asn"><code>asn</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-continent"><code>continent</code></a>, <a href="#parameter-crawlPurpose"><code>crawlPurpose</code></a>, <a href="#parameter-userAgent"><code>userAgent</code></a>, <a href="#parameter-industry"><code>industry</code></a>, <a href="#parameter-vertical"><code>vertical</code></a>, <a href="#parameter-contentType"><code>contentType</code></a>, <a href="#parameter-responseStatus"><code>responseStatus</code></a>, <a href="#parameter-responseStatusCategory"><code>responseStatusCategory</code></a>, <a href="#parameter-limitPerGroup"><code>limitPerGroup</code></a>, <a href="#parameter-normalization"><code>normalization</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the distribution of HTTP requests from AI bots, grouped by the specified dimension over time.</td>
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
    <td>Specifies the attribute by which to group the results.</td>
</tr>
<tr id="parameter-aggInterval">
    <td><CopyableCode code="aggInterval" /></td>
    <td><code>string</code></td>
    <td>Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals). Refer to [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).</td>
</tr>
<tr id="parameter-asn">
    <td><CopyableCode code="asn" /></td>
    <td><code>array</code></td>
    <td>Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.</td>
</tr>
<tr id="parameter-contentType">
    <td><CopyableCode code="contentType" /></td>
    <td><code>array</code></td>
    <td>Filters results by content type category.</td>
</tr>
<tr id="parameter-continent">
    <td><CopyableCode code="continent" /></td>
    <td><code>array</code></td>
    <td>Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.</td>
</tr>
<tr id="parameter-crawlPurpose">
    <td><CopyableCode code="crawlPurpose" /></td>
    <td><code>array</code></td>
    <td>Filters results by bot crawl purpose.</td>
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
<tr id="parameter-industry">
    <td><CopyableCode code="industry" /></td>
    <td><code>array</code></td>
    <td>Filters results by industry.</td>
</tr>
<tr id="parameter-limitPerGroup">
    <td><CopyableCode code="limitPerGroup" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>array</code></td>
    <td>Filters results by location. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude locations from results. For example, `-US,PT` excludes results from the US, but includes results from PT.</td>
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
<tr id="parameter-responseStatus">
    <td><CopyableCode code="responseStatus" /></td>
    <td><code>array</code></td>
    <td>Filters results by HTTP response status code (e.g. 200, 403, 404). Only [IANA-registered codes](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) are accepted.</td>
</tr>
<tr id="parameter-responseStatusCategory">
    <td><CopyableCode code="responseStatusCategory" /></td>
    <td><code>array</code></td>
    <td>Filters results by HTTP response status code category.</td>
</tr>
<tr id="parameter-userAgent">
    <td><CopyableCode code="userAgent" /></td>
    <td><code>array</code></td>
    <td>Filters results by user agent.</td>
</tr>
<tr id="parameter-vertical">
    <td><CopyableCode code="vertical" /></td>
    <td><code>array</code></td>
    <td>Filters results by vertical.</td>
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

Retrieves the distribution of HTTP requests from AI bots, grouped by the specified dimension over time.

```sql
SELECT
meta,
serie_0
FROM cloudflare.radar.bots_timeseries_groups_dimension_5dbf28
WHERE dimension = '{{ dimension }}' -- required
AND aggInterval = '{{ aggInterval }}'
AND name = '{{ name }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND asn = '{{ asn }}'
AND location = '{{ location }}'
AND continent = '{{ continent }}'
AND crawlPurpose = '{{ crawlPurpose }}'
AND userAgent = '{{ userAgent }}'
AND industry = '{{ industry }}'
AND vertical = '{{ vertical }}'
AND contentType = '{{ contentType }}'
AND responseStatus = '{{ responseStatus }}'
AND responseStatusCategory = '{{ responseStatusCategory }}'
AND limitPerGroup = '{{ limitPerGroup }}'
AND normalization = '{{ normalization }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
