--- 
title: ct_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - ct_summary
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

Creates, updates, deletes, gets or lists a <code>ct_summary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ct_summary" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.ct_summary" /></td></tr>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-dimension"><code>dimension</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-dateRange"><code>dateRange</code></a>, <a href="#parameter-dateStart"><code>dateStart</code></a>, <a href="#parameter-dateEnd"><code>dateEnd</code></a>, <a href="#parameter-limitPerGroup"><code>limitPerGroup</code></a>, <a href="#parameter-ca"><code>ca</code></a>, <a href="#parameter-caOwner"><code>caOwner</code></a>, <a href="#parameter-duration"><code>duration</code></a>, <a href="#parameter-entryType"><code>entryType</code></a>, <a href="#parameter-expirationStatus"><code>expirationStatus</code></a>, <a href="#parameter-hasIps"><code>hasIps</code></a>, <a href="#parameter-hasWildcards"><code>hasWildcards</code></a>, <a href="#parameter-log"><code>log</code></a>, <a href="#parameter-logApi"><code>logApi</code></a>, <a href="#parameter-logOperator"><code>logOperator</code></a>, <a href="#parameter-publicKeyAlgorithm"><code>publicKeyAlgorithm</code></a>, <a href="#parameter-signatureAlgorithm"><code>signatureAlgorithm</code></a>, <a href="#parameter-tld"><code>tld</code></a>, <a href="#parameter-validationLevel"><code>validationLevel</code></a>, <a href="#parameter-uniqueEntries"><code>uniqueEntries</code></a>, <a href="#parameter-normalization"><code>normalization</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves an aggregated summary of certificates grouped by the specified dimension.</td>
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
    <td>Specifies the certificate attribute by which to group the results.</td>
</tr>
<tr id="parameter-ca">
    <td><CopyableCode code="ca" /></td>
    <td><code>array</code></td>
    <td>Filters results by certificate authority.</td>
</tr>
<tr id="parameter-caOwner">
    <td><CopyableCode code="caOwner" /></td>
    <td><code>array</code></td>
    <td>Filters results by certificate authority owner.</td>
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
<tr id="parameter-duration">
    <td><CopyableCode code="duration" /></td>
    <td><code>array</code></td>
    <td>Filters results by certificate duration.</td>
</tr>
<tr id="parameter-entryType">
    <td><CopyableCode code="entryType" /></td>
    <td><code>array</code></td>
    <td>Filters results by entry type (certificate vs. pre-certificate).</td>
</tr>
<tr id="parameter-expirationStatus">
    <td><CopyableCode code="expirationStatus" /></td>
    <td><code>array</code></td>
    <td>Filters results by expiration status (expired vs. valid).</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-hasIps">
    <td><CopyableCode code="hasIps" /></td>
    <td><code>array</code></td>
    <td>Filters results based on whether the certificates are bound to specific IP addresses.</td>
</tr>
<tr id="parameter-hasWildcards">
    <td><CopyableCode code="hasWildcards" /></td>
    <td><code>array</code></td>
    <td>Filters results based on whether the certificates contain wildcard domains.</td>
</tr>
<tr id="parameter-limitPerGroup">
    <td><CopyableCode code="limitPerGroup" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects per group to the top items within the specified time range. When item count exceeds the limit, extra items appear grouped under an "other" category.</td>
</tr>
<tr id="parameter-log">
    <td><CopyableCode code="log" /></td>
    <td><code>array</code></td>
    <td>Filters results by certificate log.</td>
</tr>
<tr id="parameter-logApi">
    <td><CopyableCode code="logApi" /></td>
    <td><code>array</code></td>
    <td>Filters results by certificate log API (RFC6962 vs. static).</td>
</tr>
<tr id="parameter-logOperator">
    <td><CopyableCode code="logOperator" /></td>
    <td><code>array</code></td>
    <td>Filters results by certificate log operator.</td>
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
<tr id="parameter-publicKeyAlgorithm">
    <td><CopyableCode code="publicKeyAlgorithm" /></td>
    <td><code>array</code></td>
    <td>Filters results by public key algorithm.</td>
</tr>
<tr id="parameter-signatureAlgorithm">
    <td><CopyableCode code="signatureAlgorithm" /></td>
    <td><code>array</code></td>
    <td>Filters results by signature algorithm.</td>
</tr>
<tr id="parameter-tld">
    <td><CopyableCode code="tld" /></td>
    <td><code>array</code></td>
    <td>Filters results by top-level domain.</td>
</tr>
<tr id="parameter-uniqueEntries">
    <td><CopyableCode code="uniqueEntries" /></td>
    <td><code>array</code></td>
    <td>Specifies whether to filter out duplicate certificates and pre-certificates. Set to true for unique entries only.</td>
</tr>
<tr id="parameter-validationLevel">
    <td><CopyableCode code="validationLevel" /></td>
    <td><code>array</code></td>
    <td>Filters results by validation level.</td>
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

Retrieves an aggregated summary of certificates grouped by the specified dimension.

```sql
SELECT
meta,
summary_0
FROM cloudflare.radar.ct_summary
WHERE dimension = '{{ dimension }}' -- required
AND name = '{{ name }}'
AND dateRange = '{{ dateRange }}'
AND dateStart = '{{ dateStart }}'
AND dateEnd = '{{ dateEnd }}'
AND limitPerGroup = '{{ limitPerGroup }}'
AND ca = '{{ ca }}'
AND caOwner = '{{ caOwner }}'
AND duration = '{{ duration }}'
AND entryType = '{{ entryType }}'
AND expirationStatus = '{{ expirationStatus }}'
AND hasIps = '{{ hasIps }}'
AND hasWildcards = '{{ hasWildcards }}'
AND log = '{{ log }}'
AND logApi = '{{ logApi }}'
AND logOperator = '{{ logOperator }}'
AND publicKeyAlgorithm = '{{ publicKeyAlgorithm }}'
AND signatureAlgorithm = '{{ signatureAlgorithm }}'
AND tld = '{{ tld }}'
AND validationLevel = '{{ validationLevel }}'
AND uniqueEntries = '{{ uniqueEntries }}'
AND normalization = '{{ normalization }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
