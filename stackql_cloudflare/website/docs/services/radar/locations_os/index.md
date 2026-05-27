--- 
title: locations_os
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_os
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

Creates, updates, deletes, gets or lists a <code>locations_os</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="locations_os" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.locations_os" /></td></tr>
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
    <td><CopyableCode code="top_0" /></td>
    <td><code>array</code></td>
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
    <td><a href="#parameter-os"><code>os</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-asn"><code>asn</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-continent"><code>continent</code></a>, <a href="#parameter-geoId"><code>geoId</code></a>, <a href="#parameter-botClass"><code>botClass</code></a>, <a href="#parameter-deviceType"><code>deviceType</code></a>, <a href="#parameter-httpProtocol"><code>httpProtocol</code></a>, <a href="#parameter-httpVersion"><code>httpVersion</code></a>, <a href="#parameter-ipVersion"><code>ipVersion</code></a>, <a href="#parameter-tlsVersion"><code>tlsVersion</code></a>, <a href="#parameter-browserFamily"><code>browserFamily</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the top locations, by HTTP requests, of the requested operating system.</td>
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
<tr id="parameter-os">
    <td><CopyableCode code="os" /></td>
    <td><code>string</code></td>
    <td>Operating system.</td>
</tr>
<tr id="parameter-asn">
    <td><CopyableCode code="asn" /></td>
    <td><code>array</code></td>
    <td>Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.</td>
</tr>
<tr id="parameter-botClass">
    <td><CopyableCode code="botClass" /></td>
    <td><code>array</code></td>
    <td>Filters results by bot class. Refer to [Bot classes](https://developers.cloudflare.com/radar/concepts/bot-classes/).</td>
</tr>
<tr id="parameter-browserFamily">
    <td><CopyableCode code="browserFamily" /></td>
    <td><code>array</code></td>
    <td>Filters results by browser family.</td>
</tr>
<tr id="parameter-continent">
    <td><CopyableCode code="continent" /></td>
    <td><code>array</code></td>
    <td>Filters results by continent. Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude continents from results. For example, `-EU,NA` excludes results from EU, but includes results from NA.</td>
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
<tr id="parameter-deviceType">
    <td><CopyableCode code="deviceType" /></td>
    <td><code>array</code></td>
    <td>Filters results by device type.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-geoId">
    <td><CopyableCode code="geoId" /></td>
    <td><code>array</code></td>
    <td>Filters results by Geolocation. Specify a comma-separated list of GeoNames IDs. Prefix with `-` to exclude geoIds from results. For example, `-2267056,360689` excludes results from the 2267056 (Lisbon), but includes results from 5128638 (New York).</td>
</tr>
<tr id="parameter-httpProtocol">
    <td><CopyableCode code="httpProtocol" /></td>
    <td><code>array</code></td>
    <td>Filters results by HTTP protocol (HTTP vs. HTTPS).</td>
</tr>
<tr id="parameter-httpVersion">
    <td><CopyableCode code="httpVersion" /></td>
    <td><code>array</code></td>
    <td>Filters results by HTTP version.</td>
</tr>
<tr id="parameter-ipVersion">
    <td><CopyableCode code="ipVersion" /></td>
    <td><code>array</code></td>
    <td>Filters results by IP version (Ipv4 vs. IPv6).</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects returned in the response.</td>
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
<tr id="parameter-tlsVersion">
    <td><CopyableCode code="tlsVersion" /></td>
    <td><code>array</code></td>
    <td>Filters results by TLS version.</td>
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

Retrieves the top locations, by HTTP requests, of the requested operating system.

```sql
SELECT
meta,
top_0
FROM cloudflare.radar.locations_os
WHERE os = '{{ os }}' -- required
AND limit = '{{ limit }}'
AND name = '{{ name }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND asn = '{{ asn }}'
AND location = '{{ location }}'
AND continent = '{{ continent }}'
AND geoId = '{{ geoId }}'
AND botClass = '{{ botClass }}'
AND deviceType = '{{ deviceType }}'
AND httpProtocol = '{{ httpProtocol }}'
AND httpVersion = '{{ httpVersion }}'
AND ipVersion = '{{ ipVersion }}'
AND tlsVersion = '{{ tlsVersion }}'
AND browserFamily = '{{ browserFamily }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
