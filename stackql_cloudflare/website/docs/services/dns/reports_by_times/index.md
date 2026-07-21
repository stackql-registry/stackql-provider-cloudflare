--- 
title: reports_by_times
hide_title: false
hide_table_of_contents: false
keywords:
  - reports_by_times
  - dns
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

Creates, updates, deletes, gets or lists a <code>reports_by_times</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reports_by_times" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.reports_by_times" /></td></tr>
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

By Time response

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
    <td><CopyableCode code="dimensions" /></td>
    <td><code>array</code></td>
    <td>Array of dimension values, representing the combination of dimension values corresponding to this row.</td>
</tr>
<tr>
    <td><CopyableCode code="metrics" /></td>
    <td><code>array</code></td>
    <td>Array with one item per requested metric. Each item is an array of values, broken down by time interval.</td>
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
    <td><a href="#parameter-metrics"><code>metrics</code></a>, <a href="#parameter-dimensions"><code>dimensions</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-until"><code>until</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-sort"><code>sort</code></a>, <a href="#parameter-filters"><code>filters</code></a>, <a href="#parameter-time_delta"><code>time_delta</code></a></td>
    <td>Retrieves a list of aggregate metrics grouped by time interval. See [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/) for detailed information about the available query parameters.</td>
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
<tr id="parameter-dimensions">
    <td><CopyableCode code="dimensions" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-filters">
    <td><CopyableCode code="filters" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-metrics">
    <td><CopyableCode code="metrics" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-sort">
    <td><CopyableCode code="sort" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-time_delta">
    <td><CopyableCode code="time_delta" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string (date-time)</code></td>
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

Retrieves a list of aggregate metrics grouped by time interval. See [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/) for detailed information about the available query parameters.

```sql
SELECT
dimensions,
metrics
FROM cloudflare.dns.reports_by_times
WHERE zone_id = '{{ zone_id }}' -- required
AND metrics = '{{ metrics }}'
AND dimensions = '{{ dimensions }}'
AND since = '{{ since }}'
AND until = '{{ until }}'
AND limit = '{{ limit }}'
AND sort = '{{ sort }}'
AND filters = '{{ filters }}'
AND time_delta = '{{ time_delta }}'
;
```
</TabItem>
</Tabs>
