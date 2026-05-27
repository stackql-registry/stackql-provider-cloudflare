--- 
title: dns_top_ases
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_top_ases
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

Creates, updates, deletes, gets or lists a <code>dns_top_ases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dns_top_ases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.dns_top_ases" /></td></tr>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-asn"><code>asn</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-continent"><code>continent</code></a>, <a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-cacheHit"><code>cacheHit</code></a>, <a href="#parameter-nodata"><code>nodata</code></a>, <a href="#parameter-protocol"><code>protocol</code></a>, <a href="#parameter-queryType"><code>queryType</code></a>, <a href="#parameter-responseCode"><code>responseCode</code></a>, <a href="#parameter-responseTtl"><code>responseTtl</code></a>, <a href="#parameter-dnssec"><code>dnssec</code></a>, <a href="#parameter-dnssecAware"><code>dnssecAware</code></a>, <a href="#parameter-dnssecE2e"><code>dnssecE2e</code></a>, <a href="#parameter-ipVersion"><code>ipVersion</code></a>, <a href="#parameter-matchingAnswer"><code>matchingAnswer</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the top autonomous systems by DNS queries made to 1.1.1.1 DNS resolver.</td>
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
    <td><code>array</code></td>
    <td>Filters results by Autonomous System. Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes results from AS174, but includes results from AS3356.</td>
</tr>
<tr id="parameter-cacheHit">
    <td><CopyableCode code="cacheHit" /></td>
    <td><code>array</code></td>
    <td>Filters results based on cache status.</td>
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
<tr id="parameter-dnssec">
    <td><CopyableCode code="dnssec" /></td>
    <td><code>array</code></td>
    <td>Filters results based on DNSSEC (DNS Security Extensions) support.</td>
</tr>
<tr id="parameter-dnssecAware">
    <td><CopyableCode code="dnssecAware" /></td>
    <td><code>array</code></td>
    <td>Filters results based on DNSSEC (DNS Security Extensions) client awareness.</td>
</tr>
<tr id="parameter-dnssecE2e">
    <td><CopyableCode code="dnssecE2e" /></td>
    <td><code>array</code></td>
    <td>Filters results based on DNSSEC-validated answers by end-to-end security status.</td>
</tr>
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>array</code></td>
    <td>Filters results by domain name.</td>
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
<tr id="parameter-matchingAnswer">
    <td><CopyableCode code="matchingAnswer" /></td>
    <td><code>array</code></td>
    <td>Filters results based on whether the queries have a matching answer.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>array</code></td>
    <td>Array of names used to label the series in the response.</td>
</tr>
<tr id="parameter-nodata">
    <td><CopyableCode code="nodata" /></td>
    <td><code>array</code></td>
    <td>Specifies whether the response includes empty DNS responses (NODATA).</td>
</tr>
<tr id="parameter-protocol">
    <td><CopyableCode code="protocol" /></td>
    <td><code>array</code></td>
    <td>Filters results by DNS transport protocol.</td>
</tr>
<tr id="parameter-queryType">
    <td><CopyableCode code="queryType" /></td>
    <td><code>array</code></td>
    <td>Filters results by DNS query type.</td>
</tr>
<tr id="parameter-responseCode">
    <td><CopyableCode code="responseCode" /></td>
    <td><code>array</code></td>
    <td>Filters results by DNS response code.</td>
</tr>
<tr id="parameter-responseTtl">
    <td><CopyableCode code="responseTtl" /></td>
    <td><code>array</code></td>
    <td>Filters results by DNS response TTL.</td>
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

Retrieves the top autonomous systems by DNS queries made to 1.1.1.1 DNS resolver.

```sql
SELECT
meta,
top_0
FROM cloudflare.radar.dns_top_ases
WHERE limit = '{{ limit }}'
AND name = '{{ name }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND asn = '{{ asn }}'
AND location = '{{ location }}'
AND continent = '{{ continent }}'
AND domain = '{{ domain }}'
AND cacheHit = '{{ cacheHit }}'
AND nodata = '{{ nodata }}'
AND protocol = '{{ protocol }}'
AND queryType = '{{ queryType }}'
AND responseCode = '{{ responseCode }}'
AND responseTtl = '{{ responseTtl }}'
AND dnssec = '{{ dnssec }}'
AND dnssecAware = '{{ dnssecAware }}'
AND dnssecE2e = '{{ dnssecE2e }}'
AND ipVersion = '{{ ipVersion }}'
AND matchingAnswer = '{{ matchingAnswer }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
