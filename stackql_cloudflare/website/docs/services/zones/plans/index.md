--- 
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
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

Creates, updates, deletes, gets or lists a <code>plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="plans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.plans" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Available Plan Details response

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The plan name. (example: Free Plan)</td>
</tr>
<tr>
    <td><CopyableCode code="legacy_id" /></td>
    <td><code>string</code></td>
    <td>The legacy identifier for this rate plan, if any. (example: free)</td>
</tr>
<tr>
    <td><CopyableCode code="can_subscribe" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether you can subscribe to this plan.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The monetary unit in which pricing information is displayed. (example: USD)</td>
</tr>
<tr>
    <td><CopyableCode code="externally_managed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this plan is managed externally.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which you will be billed for this plan. (weekly, monthly, quarterly, yearly) (example: monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="is_subscribed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether you are currently subscribed to this plan.</td>
</tr>
<tr>
    <td><CopyableCode code="legacy_discount" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this plan has a legacy discount applied.</td>
</tr>
<tr>
    <td><CopyableCode code="price" /></td>
    <td><code>number</code></td>
    <td>The amount you will be billed for this plan.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Available Plans response

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The plan name. (example: Free Plan)</td>
</tr>
<tr>
    <td><CopyableCode code="legacy_id" /></td>
    <td><code>string</code></td>
    <td>The legacy identifier for this rate plan, if any. (example: free)</td>
</tr>
<tr>
    <td><CopyableCode code="can_subscribe" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether you can subscribe to this plan.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The monetary unit in which pricing information is displayed. (example: USD)</td>
</tr>
<tr>
    <td><CopyableCode code="externally_managed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this plan is managed externally.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>The frequency at which you will be billed for this plan. (weekly, monthly, quarterly, yearly) (example: monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="is_subscribed" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether you are currently subscribed to this plan.</td>
</tr>
<tr>
    <td><CopyableCode code="legacy_discount" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this plan has a legacy discount applied.</td>
</tr>
<tr>
    <td><CopyableCode code="price" /></td>
    <td><code>number</code></td>
    <td>The amount you will be billed for this plan.</td>
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
    <td><a href="#parameter-plan_identifier"><code>plan_identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Details of the available plan that the zone can subscribe to.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Lists available plans the zone can subscribe to.</td>
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
<tr id="parameter-plan_identifier">
    <td><CopyableCode code="plan_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Details of the available plan that the zone can subscribe to.

```sql
SELECT
id,
name,
legacy_id,
can_subscribe,
currency,
externally_managed,
frequency,
is_subscribed,
legacy_discount,
price
FROM cloudflare.zones.plans
WHERE plan_identifier = '{{ plan_identifier }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists available plans the zone can subscribe to.

```sql
SELECT
id,
name,
legacy_id,
can_subscribe,
currency,
externally_managed,
frequency,
is_subscribed,
legacy_discount,
price
FROM cloudflare.zones.plans
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>
