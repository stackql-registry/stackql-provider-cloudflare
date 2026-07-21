--- 
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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

Creates, updates, deletes, gets or lists an <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.events" /></td></tr>
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

Returns the event.

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
    <td><CopyableCode code="attacker" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attackerCountry" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="datasetId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="date" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="event" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="hasChildren" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="indicator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="indicatorType" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="indicatorTypeId" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="insight" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="killChain" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mitreAttack" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mitreCapec" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="numReferenced" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="numReferences" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rawId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="referenced" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="referencedIds" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="references" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="referencesIds" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="releasabilityId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="targetCountry" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="targetIndustry" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tlp" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a></td>
    <td></td>
    <td>Retrieves a specific event by its UUID.</td>
</tr>
<tr>
    <td><a href="#post_event_update"><CopyableCode code="post_event_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-date"><code>date</code></a>, <a href="#parameter-category"><code>category</code></a>, <a href="#parameter-event"><code>event</code></a>, <a href="#parameter-tlp"><code>tlp</code></a>, <a href="#parameter-raw"><code>raw</code></a></td>
    <td></td>
    <td>To create a dataset, see the [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/) endpoint. When `datasetId` parameter is unspecified, it will be created in a default dataset named `Cloudforce One Threat Events`.</td>
</tr>
<tr>
    <td><a href="#create_graphql"><CopyableCode code="create_graphql" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Execute GraphQL aggregations over threat events. Supports multi-dimensional group-bys, optional date range filtering, and multi-dataset aggregation.</td>
</tr>
<tr>
    <td><a href="#delete_relate"><CopyableCode code="delete_relate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_delete"><CopyableCode code="delete_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td><a href="#parameter-eventIds"><code>eventIds</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create_graphql_v2"><CopyableCode code="create_graphql_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Execute GraphQL aggregations over threat events. Supports multi-dimensional group-bys, optional date range filtering, and multi-dataset aggregation.</td>
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
<tr id="parameter-event_id">
    <td><CopyableCode code="event_id" /></td>
    <td><code>string</code></td>
    <td>The event ID.</td>
</tr>
<tr id="parameter-eventIds">
    <td><CopyableCode code="eventIds" /></td>
    <td><code>array</code></td>
    <td>Array of Event IDs to delete.</td>
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

Retrieves a specific event by its UUID.

```sql
SELECT
attacker,
attackerCountry,
category,
datasetId,
date,
event,
hasChildren,
indicator,
indicatorType,
indicatorTypeId,
insight,
killChain,
mitreAttack,
mitreCapec,
numReferenced,
numReferences,
rawId,
referenced,
referencedIds,
references,
referencesIds,
releasabilityId,
tags,
targetCountry,
targetIndustry,
tlp,
uuid
FROM cloudflare.cloudforce_one.events
WHERE account_id = '{{ account_id }}' -- required
AND dataset_id = '{{ dataset_id }}' -- required
AND event_id = '{{ event_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_event_update"
    values={[
        { label: 'post_event_update', value: 'post_event_update' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_event_update">

No description available.

```sql
INSERT INTO cloudflare.cloudforce_one.events (
attacker,
attackerCountry,
category,
createdAt,
datasetId,
date,
event,
indicator,
indicatorType,
insight,
raw,
targetCountry,
targetIndustry,
tlp,
account_id,
event_id
)
SELECT 
'{{ attacker }}',
'{{ attackerCountry }}',
'{{ category }}',
'{{ createdAt }}',
'{{ datasetId }}' /* required */,
'{{ date }}',
'{{ event }}',
'{{ indicator }}',
'{{ indicatorType }}',
'{{ insight }}',
'{{ raw }}',
'{{ targetCountry }}',
'{{ targetIndustry }}',
'{{ tlp }}',
'{{ account_id }}',
'{{ event_id }}'
RETURNING
attacker,
attackerCountry,
category,
datasetId,
date,
event,
hasChildren,
indicator,
indicatorType,
indicatorTypeId,
insight,
killChain,
mitreAttack,
mitreCapec,
numReferenced,
numReferences,
rawId,
referenced,
referencedIds,
references,
referencesIds,
releasabilityId,
tags,
targetCountry,
targetIndustry,
tlp,
uuid
;
```
</TabItem>
<TabItem value="create">

To create a dataset, see the [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/) endpoint. When `datasetId` parameter is unspecified, it will be created in a default dataset named `Cloudforce One Threat Events`.

```sql
INSERT INTO cloudflare.cloudforce_one.events (
accountId,
attacker,
attackerCountry,
category,
datasetId,
date,
event,
indicator,
indicatorType,
indicators,
insight,
raw,
tags,
targetCountry,
targetIndustry,
tlp,
account_id
)
SELECT 
{{ accountId }},
'{{ attacker }}',
'{{ attackerCountry }}',
'{{ category }}' /* required */,
'{{ datasetId }}',
'{{ date }}' /* required */,
'{{ event }}' /* required */,
'{{ indicator }}',
'{{ indicatorType }}',
'{{ indicators }}',
'{{ insight }}',
'{{ raw }}' /* required */,
'{{ tags }}',
'{{ targetCountry }}',
'{{ targetIndustry }}',
'{{ tlp }}' /* required */,
'{{ account_id }}'
RETURNING
attacker,
attackerCountry,
category,
datasetId,
date,
event,
hasChildren,
indicator,
indicatorType,
indicatorTypeId,
insight,
killChain,
mitreAttack,
mitreCapec,
numReferenced,
numReferences,
rawId,
referenced,
referencedIds,
references,
referencesIds,
releasabilityId,
tags,
targetCountry,
targetIndustry,
tlp,
uuid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: events
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the events resource.
    - name: event_id
      value: "{{ event_id }}"
      description: Required parameter for the events resource.
    - name: attacker
      value: "{{ attacker }}"
    - name: attackerCountry
      value: "{{ attackerCountry }}"
    - name: category
      value: "{{ category }}"
    - name: createdAt
      value: "{{ createdAt }}"
    - name: datasetId
      value: "{{ datasetId }}"
    - name: date
      value: "{{ date }}"
    - name: event
      value: "{{ event }}"
    - name: indicator
      value: "{{ indicator }}"
    - name: indicatorType
      value: "{{ indicatorType }}"
    - name: insight
      value: "{{ insight }}"
    - name: raw
      value:
        data: "{{ data }}"
        source: "{{ source }}"
        tlp: "{{ tlp }}"
    - name: targetCountry
      value: "{{ targetCountry }}"
    - name: targetIndustry
      value: "{{ targetIndustry }}"
    - name: tlp
      value: "{{ tlp }}"
    - name: accountId
      value: {{ accountId }}
    - name: indicators
      description: |
        Array of indicators for this event. Supports multiple indicators per event for complex scenarios.
      value:
        - indicatorType: "{{ indicatorType }}"
          value: "{{ value }}"
    - name: tags
      value:
        - "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_graphql"
    values={[
        { label: 'create_graphql', value: 'create_graphql' },
        { label: 'delete_relate', value: 'delete_relate' },
        { label: 'delete_delete', value: 'delete_delete' },
        { label: 'create_graphql_v2', value: 'create_graphql_v2' }
    ]}
>
<TabItem value="create_graphql">

Execute GraphQL aggregations over threat events. Supports multi-dimensional group-bys, optional date range filtering, and multi-dataset aggregation.

```sql
EXEC cloudflare.cloudforce_one.events.create_graphql 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_relate">

Returns success if operation succeeded.

```sql
EXEC cloudflare.cloudforce_one.events.delete_relate 
@account_id='{{ account_id }}' --required, 
@event_id='{{ event_id }}' --required
;
```
</TabItem>
<TabItem value="delete_delete">

Returns the number of deleted events.

```sql
EXEC cloudflare.cloudforce_one.events.delete_delete 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required, 
@eventIds='{{ eventIds }}'
;
```
</TabItem>
<TabItem value="create_graphql_v2">

Execute GraphQL aggregations over threat events. Supports multi-dimensional group-bys, optional date range filtering, and multi-dataset aggregation.

```sql
EXEC cloudflare.cloudforce_one.events.create_graphql_v2 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
