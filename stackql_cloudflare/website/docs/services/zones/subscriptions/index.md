--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.subscriptions" /></td></tr>
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

Zone Subscription Details response

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
    <td>Subscription identifier tag. (example: 506e3185e9c882d175a2d0cb0093d9f2)</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>The monetary unit in which pricing information is displayed. (example: USD)</td>
</tr>
<tr>
    <td><CopyableCode code="current_period_end" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of the current period and also when the next billing is due. (example: 2014-03-31T12:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="current_period_start" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the current billing period started. May match initial_period_start if this is the first period. (example: 2014-05-11T12:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>How often the subscription is renewed automatically. (weekly, monthly, quarterly, yearly, not-applicable) (example: monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="price" /></td>
    <td><code>number</code></td>
    <td>The price of the subscription that will be billed, in US dollars.</td>
</tr>
<tr>
    <td><CopyableCode code="rate_plan" /></td>
    <td><code>object</code></td>
    <td>The rate plan applied to the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state that the subscription is in. (Trial, Provisioned, Paid, AwaitingPayment, Cancelled, Failed, Expired) (example: Paid)</td>
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
    <td></td>
    <td>Lists zone subscription details.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Create a zone subscription, either plan or add-ons.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates zone subscriptions, either plan or add-ons.</td>
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

Lists zone subscription details.

```sql
SELECT
id,
currency,
current_period_end,
current_period_start,
frequency,
price,
rate_plan,
state
FROM cloudflare.zones.subscriptions
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a zone subscription, either plan or add-ons.

```sql
INSERT INTO cloudflare.zones.subscriptions (
frequency,
rate_plan,
zone_id
)
SELECT 
'{{ frequency }}',
'{{ rate_plan }}',
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: subscriptions
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the subscriptions resource.
    - name: frequency
      value: "{{ frequency }}"
      description: |
        How often the subscription is renewed automatically.
      valid_values: ['weekly', 'monthly', 'quarterly', 'yearly']
    - name: rate_plan
      description: |
        The rate plan applied to the subscription.
      value:
        currency: "{{ currency }}"
        externally_managed: {{ externally_managed }}
        id: "{{ id }}"
        is_contract: {{ is_contract }}
        public_name: "{{ public_name }}"
        scope: "{{ scope }}"
        sets:
          - "{{ sets }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates zone subscriptions, either plan or add-ons.

```sql
REPLACE cloudflare.zones.subscriptions
SET 
frequency = '{{ frequency }}',
rate_plan = '{{ rate_plan }}'
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
