--- 
title: dataset_indicators
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_indicators
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

Creates, updates, deletes, gets or lists a <code>dataset_indicators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dataset_indicators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.dataset_indicators" /></td></tr>
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

Returns a list of indicators.

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
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="datasetId" /></td>
    <td><code>string</code></td>
    <td>The dataset ID this indicator belongs to. Included in list responses.</td>
</tr>
<tr>
    <td><CopyableCode code="indicatorType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="relatedEvents" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-indicatorType"><code>indicatorType</code></a>, <a href="#parameter-relatedEvent"><code>relatedEvent</code></a></td>
    <td>This method is deprecated. Please use /events/indicators to retrieve a paginated list of indicators.</td>
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
<tr id="parameter-dataset_id">
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>The dataset ID.</td>
</tr>
<tr id="parameter-indicatorType">
    <td><CopyableCode code="indicatorType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Filter by indicator value (substring match)</td>
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
<tr id="parameter-relatedEvent">
    <td><CopyableCode code="relatedEvent" /></td>
    <td><code>array</code></td>
    <td>Filter indicators by related event UUID(s). Multiple UUIDs can be provided by repeating the parameter.</td>
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

This method is deprecated. Please use /events/indicators to retrieve a paginated list of indicators.

```sql
SELECT
createdAt,
datasetId,
indicatorType,
relatedEvents,
tags,
updatedAt,
uuid,
value
FROM cloudflare.cloudforce_one.dataset_indicators
WHERE account_id = '{{ account_id }}' -- required
AND dataset_id = '{{ dataset_id }}' -- required
AND page = '{{ page }}'
AND pageSize = '{{ pageSize }}'
AND name = '{{ name }}'
AND indicatorType = '{{ indicatorType }}'
AND relatedEvent = '{{ relatedEvent }}'
;
```
</TabItem>
</Tabs>
