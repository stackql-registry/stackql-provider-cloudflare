--- 
title: usage
hide_title: false
hide_table_of_contents: false
keywords:
  - usage
  - billing
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

Creates, updates, deletes, gets or lists a <code>usage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="usage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.billing.usage" /></td></tr>
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

Indicates PayGo account usage data was successfully retrieved.

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
    <td><CopyableCode code="BillingCurrency" /></td>
    <td><code>string</code></td>
    <td>Specifies the billing currency code (ISO 4217). (example: USD)</td>
</tr>
<tr>
    <td><CopyableCode code="BillingPeriodStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the start of the billing period. (example: 2025-02-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="ChargePeriodEnd" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the end of the charge period. (example: 2025-02-02T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="ChargePeriodStart" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the start of the charge period. (example: 2025-02-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="ConsumedQuantity" /></td>
    <td><code>number</code></td>
    <td>Specifies the quantity consumed during this charge period.</td>
</tr>
<tr>
    <td><CopyableCode code="ConsumedUnit" /></td>
    <td><code>string</code></td>
    <td>Specifies the unit of measurement for consumed quantity. (example: Requests)</td>
</tr>
<tr>
    <td><CopyableCode code="ContractedCost" /></td>
    <td><code>number</code></td>
    <td>Specifies the cost for this charge period in the billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="CumulatedContractedCost" /></td>
    <td><code>number</code></td>
    <td>Specifies the cumulated cost for the billing period in the billing currency.</td>
</tr>
<tr>
    <td><CopyableCode code="CumulatedPricingQuantity" /></td>
    <td><code>integer</code></td>
    <td>Specifies the cumulated pricing quantity for the billing period.</td>
</tr>
<tr>
    <td><CopyableCode code="PricingQuantity" /></td>
    <td><code>integer</code></td>
    <td>Specifies the pricing quantity for this charge period.</td>
</tr>
<tr>
    <td><CopyableCode code="ServiceName" /></td>
    <td><code>string</code></td>
    <td>Identifies the Cloudflare service. (example: Workers Standard)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a></td>
    <td>Returns billable usage data for PayGo (self-serve) accounts. When no query parameters are provided, returns usage for the current billing period. This endpoint is currently in alpha and access is restricted to select accounts. While in alpha, the endpoint may get breaking changes.</td>
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
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>string (date)</code></td>
    <td>Defines the start date for the usage query (e.g., 2025-02-01).</td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>string (date)</code></td>
    <td>Defines the end date for the usage query (e.g., 2025-03-01).</td>
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

Returns billable usage data for PayGo (self-serve) accounts. When no query parameters are provided, returns usage for the current billing period. This endpoint is currently in alpha and access is restricted to select accounts. While in alpha, the endpoint may get breaking changes.

```sql
SELECT
BillingCurrency,
BillingPeriodStart,
ChargePeriodEnd,
ChargePeriodStart,
ConsumedQuantity,
ConsumedUnit,
ContractedCost,
CumulatedContractedCost,
CumulatedPricingQuantity,
PricingQuantity,
ServiceName
FROM cloudflare.billing.usage
WHERE account_id = '{{ account_id }}' -- required
AND from = '{{ from }}'
AND to = '{{ to }}'
;
```
</TabItem>
</Tabs>
