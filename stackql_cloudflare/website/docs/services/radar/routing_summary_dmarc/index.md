--- 
title: routing_summary_dmarc
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_summary_dmarc
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

Creates, updates, deletes, gets or lists a <code>routing_summary_dmarc</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routing_summary_dmarc" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.routing_summary_dmarc" /></td></tr>
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
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Metadata for the results.</td>
</tr>
<tr>
    <td><CopyableCode code="summary_0" /></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-arc"><code>arc</code></a>, <a href="#parameter-dkim"><code>dkim</code></a>, <a href="#parameter-spf"><code>spf</code></a>, <a href="#parameter-ipVersion"><code>ipVersion</code></a>, <a href="#parameter-encrypted"><code>encrypted</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the distribution of emails by DMARC (Domain-based Message Authentication, Reporting and Conformance) validation.</td>
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
<tr id="parameter-arc">
    <td><CopyableCode code="arc" /></td>
    <td><code>array</code></td>
    <td>Filters results by ARC (Authenticated Received Chain) validation.</td>
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
<tr id="parameter-dkim">
    <td><CopyableCode code="dkim" /></td>
    <td><code>array</code></td>
    <td>Filters results by DKIM (DomainKeys Identified Mail) validation status.</td>
</tr>
<tr id="parameter-encrypted">
    <td><CopyableCode code="encrypted" /></td>
    <td><code>array</code></td>
    <td>Filters results by encryption status (encrypted vs. not-encrypted).</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-ipVersion">
    <td><CopyableCode code="ipVersion" /></td>
    <td><code>array</code></td>
    <td>Filters results by IP version (Ipv4 vs. IPv6).</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>array</code></td>
    <td>Array of names used to label the series in the response.</td>
</tr>
<tr id="parameter-spf">
    <td><CopyableCode code="spf" /></td>
    <td><code>array</code></td>
    <td>Filters results by SPF (Sender Policy Framework) validation status.</td>
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

Retrieves the distribution of emails by DMARC (Domain-based Message Authentication, Reporting and Conformance) validation.

```sql
SELECT
meta,
summary_0
FROM cloudflare.radar.routing_summary_dmarc
WHERE name = '{{ name }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND arc = '{{ arc }}'
AND dkim = '{{ dkim }}'
AND spf = '{{ spf }}'
AND ipVersion = '{{ ipVersion }}'
AND encrypted = '{{ encrypted }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
