--- 
title: events_indicators
hide_title: false
hide_table_of_contents: false
keywords:
  - events_indicators
  - cloudforce_one
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

Creates, updates, deletes, gets or lists an <code>events_indicators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="events_indicators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.events_indicators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

Returns a paginated list of indicators.

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
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-datasetIds"><code>datasetIds</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-indicatorType"><code>indicatorType</code></a>, <a href="#parameter-relatedEvents"><code>relatedEvents</code></a>, <a href="#parameter-tags"><code>tags</code></a>, <a href="#parameter-createdAfter"><code>createdAfter</code></a>, <a href="#parameter-createdBefore"><code>createdBefore</code></a>, <a href="#parameter-relatedEventsLimit"><code>relatedEventsLimit</code></a>, <a href="#parameter-includeTags"><code>includeTags</code></a>, <a href="#parameter-includeTotalCount"><code>includeTotalCount</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves a paginated list of indicators across specified datasets. Use datasetIds=all or datasetIds=* to query all datasets for the account. If no datasetIds provided, uses the default dataset.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account ID.</td>
</tr>
<tr id="parameter-createdAfter">
    <td><CopyableCode code="createdAfter" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filter indicators created on or after this date. Must use ISO 8601 format (e.g., '2024-01-15T00:00:00Z').</td>
</tr>
<tr id="parameter-createdBefore">
    <td><CopyableCode code="createdBefore" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filter indicators created on or before this date. Must use ISO 8601 format (e.g., '2024-12-31T23:59:59Z').</td>
</tr>
<tr id="parameter-datasetIds">
    <td><CopyableCode code="datasetIds" /></td>
    <td><code>array</code></td>
    <td>Dataset IDs to query indicators from (array of UUIDs), or special value 'all' or '*' to query all datasets. If not provided, uses the default dataset.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Output format for indicator data. 'json' returns the default format, 'stix2' returns STIX 2.1 Indicator SDOs.</td>
</tr>
<tr id="parameter-includeTags">
    <td><CopyableCode code="includeTags" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include full tag details for each indicator. Defaults to true.</td>
</tr>
<tr id="parameter-includeTotalCount">
    <td><CopyableCode code="includeTotalCount" /></td>
    <td><code>boolean</code></td>
    <td>Whether to compute accurate total count via COUNT(*). Defaults to false for performance. When false, total_count is an approximation.</td>
</tr>
<tr id="parameter-indicatorType">
    <td><CopyableCode code="indicatorType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Filter indicators by value using substring match (LIKE). Legacy alternative to structured search.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-relatedEvents">
    <td><CopyableCode code="relatedEvents" /></td>
    <td><code>array</code></td>
    <td>Filter by related event IDs</td>
</tr>
<tr id="parameter-relatedEventsLimit">
    <td><CopyableCode code="relatedEventsLimit" /></td>
    <td><code>number</code></td>
    <td>Limit the number of related events returned per indicator. Default: 2. Set to 0 for none, -1 for all events.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>array</code></td>
    <td>Structured search as a JSON array of &#123;field, op, value&#125; objects. Searchable fields: value, indicatorType. Supports operators: equals, not, contains, startsWith, endsWith, gt, lt, gte, lte, like, in, find. Use the 'in' operator with an array value to bulk-check up to 100 indicators in a single request, e.g. search=[&#123;"field":"value","op":"in","value":["evil.com","bad.org"]&#125;]. Multiple conditions are AND'd together. Max 10 conditions per request.</td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Filter by tag values or UUIDs. Indicators must have at least one of the specified tags (OR logic). Supports both tag UUID and tag value.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

Retrieves a paginated list of indicators across specified datasets. Use datasetIds=all or datasetIds=* to query all datasets for the account. If no datasetIds provided, uses the default dataset.

```sql
SELECT
properties,
type
FROM cloudflare.cloudforce_one.events_indicators
WHERE account_id = '{{ account_id }}' -- required
AND datasetIds = '{{ datasetIds }}'
AND page = '{{ page }}'
AND pageSize = '{{ pageSize }}'
AND search = '{{ search }}'
AND name = '{{ name }}'
AND indicatorType = '{{ indicatorType }}'
AND relatedEvents = '{{ relatedEvents }}'
AND tags = '{{ tags }}'
AND createdAfter = '{{ createdAfter }}'
AND createdBefore = '{{ createdBefore }}'
AND relatedEventsLimit = '{{ relatedEventsLimit }}'
AND includeTags = '{{ includeTags }}'
AND includeTotalCount = '{{ includeTotalCount }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
