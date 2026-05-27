--- 
title: hijacks_events
hide_title: false
hide_table_of_contents: false
keywords:
  - hijacks_events
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

Creates, updates, deletes, gets or lists a <code>hijacks_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="hijacks_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.hijacks_events" /></td></tr>
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
    <td><CopyableCode code="asn_info" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="total_monitors" /></td>
    <td><code>integer</code></td>
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
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-eventId"><code>eventId</code></a>, <a href="#parameter-hijackerAsn"><code>hijackerAsn</code></a>, <a href="#parameter-victimAsn"><code>victimAsn</code></a>, <a href="#parameter-involvedAsn"><code>involvedAsn</code></a>, <a href="#parameter-involvedCountry"><code>involvedCountry</code></a>, <a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-minConfidence"><code>minConfidence</code></a>, <a href="#parameter-maxConfidence"><code>maxConfidence</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-sortBy"><code>sortBy</code></a>, <a href="#parameter-sortOrder"><code>sortOrder</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the BGP hijack events.</td>
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
<tr id="parameter-eventId">
    <td><CopyableCode code="eventId" /></td>
    <td><code>integer</code></td>
    <td>The unique identifier of a event.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-hijackerAsn">
    <td><CopyableCode code="hijackerAsn" /></td>
    <td><code>integer</code></td>
    <td>The potential hijacker AS of a BGP hijack event.</td>
</tr>
<tr id="parameter-involvedAsn">
    <td><CopyableCode code="involvedAsn" /></td>
    <td><code>integer</code></td>
    <td>The potential hijacker or victim AS of a BGP hijack event.</td>
</tr>
<tr id="parameter-involvedCountry">
    <td><CopyableCode code="involvedCountry" /></td>
    <td><code>string</code></td>
    <td>The country code of the potential hijacker or victim AS of a BGP hijack event.</td>
</tr>
<tr id="parameter-maxConfidence">
    <td><CopyableCode code="maxConfidence" /></td>
    <td><code>integer</code></td>
    <td>Filters events by maximum confidence score (1-4 low, 5-7 mid, 8+ high).</td>
</tr>
<tr id="parameter-minConfidence">
    <td><CopyableCode code="minConfidence" /></td>
    <td><code>integer</code></td>
    <td>Filters events by minimum confidence score (1-4 low, 5-7 mid, 8+ high).</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Current page number, starting from 1.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of entries per page.</td>
</tr>
<tr id="parameter-prefix">
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sortBy">
    <td><CopyableCode code="sortBy" /></td>
    <td><code>string</code></td>
    <td>Sorts results by the specified field.</td>
</tr>
<tr id="parameter-sortOrder">
    <td><CopyableCode code="sortOrder" /></td>
    <td><code>string</code></td>
    <td>Sort order.</td>
</tr>
<tr id="parameter-victimAsn">
    <td><CopyableCode code="victimAsn" /></td>
    <td><code>integer</code></td>
    <td>The potential victim AS of a BGP hijack event.</td>
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

Retrieves the BGP hijack events.

```sql
SELECT
asn_info,
events,
total_monitors
FROM cloudflare.radar.hijacks_events
WHERE page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND eventId = '{{ eventId }}'
AND hijackerAsn = '{{ hijackerAsn }}'
AND victimAsn = '{{ victimAsn }}'
AND involvedAsn = '{{ involvedAsn }}'
AND involvedCountry = '{{ involvedCountry }}'
AND prefix = '{{ prefix }}'
AND minConfidence = '{{ minConfidence }}'
AND maxConfidence = '{{ maxConfidence }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND sortBy = '{{ sortBy }}'
AND sortOrder = '{{ sortOrder }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
