--- 
title: analytics_colos
hide_title: false
hide_table_of_contents: false
keywords:
  - analytics_colos
  - zones
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

Creates, updates, deletes, gets or lists an <code>analytics_colos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analytics_colos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.analytics_colos" /></td></tr>
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

Get analytics by Co-locations response

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
    <td><CopyableCode code="colo_id" /></td>
    <td><code>string</code></td>
    <td>The airport code identifer for the co-location. (example: SFO)</td>
</tr>
<tr>
    <td><CopyableCode code="timeseries" /></td>
    <td><code>array</code></td>
    <td>Time deltas containing metadata about each bucket of time. The number of buckets (resolution) is determined by the amount of time between the since and until parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="totals" /></td>
    <td><code>object</code></td>
    <td>Breakdown of totals by data type.</td>
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
    <td><a href="#parameter-zone_identifier"><code>zone_identifier</code></a></td>
    <td><a href="#parameter-until"><code>until</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-continuous"><code>continuous</code></a></td>
    <td>This view provides a breakdown of analytics data by datacenter. Note: This is available to Enterprise customers only.</td>
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
<tr id="parameter-zone_identifier">
    <td><CopyableCode code="zone_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-continuous">
    <td><CopyableCode code="continuous" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string</code></td>
    <td></td>
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

This view provides a breakdown of analytics data by datacenter. Note: This is available to Enterprise customers only.

```sql
SELECT
colo_id,
timeseries,
totals
FROM cloudflare.zones.analytics_colos
WHERE zone_identifier = '{{ zone_identifier }}' -- required
AND until = '{{ until }}'
AND since = '{{ since }}'
AND continuous = '{{ continuous }}'
;
```
</TabItem>
</Tabs>
