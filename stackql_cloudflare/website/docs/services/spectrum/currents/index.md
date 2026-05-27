--- 
title: currents
hide_title: false
hide_table_of_contents: false
keywords:
  - currents
  - spectrum
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

Creates, updates, deletes, gets or lists a <code>currents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="currents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.spectrum.currents" /></td></tr>
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

Get current aggregated analytics response

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
    <td><CopyableCode code="appID" /></td>
    <td><code>string</code></td>
    <td>Application identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="bytesEgress" /></td>
    <td><code>number</code></td>
    <td>Number of bytes sent</td>
</tr>
<tr>
    <td><CopyableCode code="bytesIngress" /></td>
    <td><code>number</code></td>
    <td>Number of bytes received</td>
</tr>
<tr>
    <td><CopyableCode code="connections" /></td>
    <td><code>number</code></td>
    <td>Number of connections</td>
</tr>
<tr>
    <td><CopyableCode code="durationAvg" /></td>
    <td><code>number</code></td>
    <td>Average duration of connections</td>
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
    <td><a href="#parameter-appID"><code>appID</code></a>, <a href="#parameter-colo_name"><code>colo_name</code></a></td>
    <td>Retrieves analytics aggregated from the last minute of usage on Spectrum applications underneath a given zone.</td>
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
<tr id="parameter-appID">
    <td><CopyableCode code="appID" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-colo_name">
    <td><CopyableCode code="colo_name" /></td>
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

Retrieves analytics aggregated from the last minute of usage on Spectrum applications underneath a given zone.

```sql
SELECT
appID,
bytesEgress,
bytesIngress,
connections,
durationAvg
FROM cloudflare.spectrum.currents
WHERE zone_id = '{{ zone_id }}' -- required
AND appID = '{{ appID }}'
AND colo_name = '{{ colo_name }}'
;
```
</TabItem>
</Tabs>
