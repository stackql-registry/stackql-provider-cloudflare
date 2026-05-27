--- 
title: outages_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - outages_locations
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

Creates, updates, deletes, gets or lists an <code>outages_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="outages_locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.outages_locations" /></td></tr>
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
    <td><CopyableCode code="clientCountryAlpha2" /></td>
    <td><code>string</code></td>
    <td> (example: PT)</td>
</tr>
<tr>
    <td><CopyableCode code="clientCountryName" /></td>
    <td><code>string</code></td>
    <td> (example: Portugal)</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>A numeric string. (example: 10)</td>
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
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the number of outages by location.</td>
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

Retrieves the number of outages by location.

```sql
SELECT
clientCountryAlpha2,
clientCountryName,
value
FROM cloudflare.radar.outages_locations
WHERE limit = '{{ limit }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
