--- 
title: traffic_anomalies
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_anomalies
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

Creates, updates, deletes, gets or lists a <code>traffic_anomalies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="traffic_anomalies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.traffic_anomalies" /></td></tr>
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

List of Internet traffic anomalies.

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
    <td><CopyableCode code="asnDetails" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endDate" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="locationDetails" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="originDetails" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="startDate" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="visibleInDataSources" /></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-asn"><code>asn</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-origin"><code>origin</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the latest Internet traffic anomalies, which are signals that might indicate an outage. These alerts are automatically detected by Radar and manually verified by our team.</td>
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
<tr id="parameter-asn">
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Filters results by Autonomous System. Specify a single Autonomous System Number (ASN) as integer.</td>
</tr>
<tr id="parameter-dateEnd">
    <td><CopyableCode code="dateEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>End of the date range (inclusive).</td>
</tr>
<tr id="parameter-dateRange">
    <td><CopyableCode code="dateRange" /></td>
    <td><code>string</code></td>
    <td>Filters results by date range.</td>
</tr>
<tr id="parameter-dateStart">
    <td><CopyableCode code="dateStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start of the date range (inclusive).</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Filters results by location. Specify an alpha-2 location code.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>Skips the specified number of objects before fetching the results.</td>
</tr>
<tr id="parameter-origin">
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>Filters results by origin.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>array</code></td>
    <td>Filters results by entity type (LOCATION, AS, or ORIGIN).</td>
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

Retrieves the latest Internet traffic anomalies, which are signals that might indicate an outage. These alerts are automatically detected by Radar and manually verified by our team.

```sql
SELECT
asnDetails,
endDate,
locationDetails,
originDetails,
startDate,
status,
type,
uuid,
visibleInDataSources
FROM cloudflare.radar.traffic_anomalies
WHERE limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND status = '{{ status }}'
AND type = '{{ type }}'
AND asn = '{{ asn }}'
AND location = '{{ location }}'
AND origin = '{{ origin }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
