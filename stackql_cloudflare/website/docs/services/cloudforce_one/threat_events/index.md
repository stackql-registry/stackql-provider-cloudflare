--- 
title: threat_events
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_events
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

Creates, updates, deletes, gets or lists a <code>threat_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="threat_events" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.threat_events" /></td></tr>
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

Returns an event.

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
<TabItem value="list">

Returns a list of events.

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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a></td>
    <td></td>
    <td>This Method is deprecated. Please use /events/dataset/:dataset_id/events/:event_id instead.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a>, <a href="#parameter-forceRefresh"><code>forceRefresh</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Use `datasetId=all` or `datasetId=*` to query all event datasets for the account (limited to 10). When `datasetId` is unspecified, events are listed from the default Cloudforce One Threat Events dataset. To list existing datasets, use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint.</td>
</tr>
<tr>
    <td><a href="#bulk_create"><CopyableCode code="bulk_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-data"><code>data</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a></td>
    <td></td>
    <td>The `datasetId` parameter must be defined. To list existing datasets (and their IDs) in your account, use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-event_id">
    <td><CopyableCode code="event_id" /></td>
    <td><code>string</code></td>
    <td>The event ID.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-datasetId">
    <td><CopyableCode code="datasetId" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-forceRefresh">
    <td><CopyableCode code="forceRefresh" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td></td>
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
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>array</code></td>
    <td></td>
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

This Method is deprecated. Please use /events/dataset/:dataset_id/events/:event_id instead.

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
FROM cloudflare.cloudforce_one.threat_events
WHERE account_id = '{{ account_id }}' -- required
AND event_id = '{{ event_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Use `datasetId=all` or `datasetId=*` to query all event datasets for the account (limited to 10). When `datasetId` is unspecified, events are listed from the default Cloudforce One Threat Events dataset. To list existing datasets, use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint.

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
FROM cloudflare.cloudforce_one.threat_events
WHERE account_id = '{{ account_id }}' -- required
AND cursor = '{{ cursor }}'
AND search = '{{ search }}'
AND page = '{{ page }}'
AND pageSize = '{{ pageSize }}'
AND orderBy = '{{ orderBy }}'
AND order = '{{ order }}'
AND datasetId = '{{ datasetId }}'
AND forceRefresh = '{{ forceRefresh }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="bulk_create"
    values={[
        { label: 'bulk_create', value: 'bulk_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="bulk_create">

The `datasetId` parameter must be defined. To list existing datasets (and their IDs) in your account, use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint.

```sql
INSERT INTO cloudflare.cloudforce_one.threat_events (
data,
datasetId,
includeCreatedEvents,
account_id
)
SELECT 
'{{ data }}' /* required */,
'{{ datasetId }}' /* required */,
{{ includeCreatedEvents }},
'{{ account_id }}'
RETURNING
createBulkEventsRequestId,
createdEvents,
createdEventsCount,
createdTagsCount,
errorCount,
errors,
queuedIndicatorsCount
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: threat_events
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the threat_events resource.
    - name: data
      value:
        - accountId: {{ accountId }}
          attacker: "{{ attacker }}"
          attackerCountry: "{{ attackerCountry }}"
          category: "{{ category }}"
          datasetId: "{{ datasetId }}"
          date: "{{ date }}"
          event: "{{ event }}"
          indicator: "{{ indicator }}"
          indicatorType: "{{ indicatorType }}"
          indicators: "{{ indicators }}"
          insight: "{{ insight }}"
          raw:
            data: "{{ data }}"
            source: "{{ source }}"
            tlp: "{{ tlp }}"
          tags: "{{ tags }}"
          targetCountry: "{{ targetCountry }}"
          targetIndustry: "{{ targetIndustry }}"
          tlp: "{{ tlp }}"
    - name: datasetId
      value: "{{ datasetId }}"
    - name: includeCreatedEvents
      value: {{ includeCreatedEvents }}
      description: |
        When true, response includes array of created event UUIDs and shard IDs. Useful for tracking which events were created and where.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

No description available.

```sql
UPDATE cloudflare.cloudforce_one.threat_events
SET 
attacker = '{{ attacker }}',
attackerCountry = '{{ attackerCountry }}',
category = '{{ category }}',
createdAt = '{{ createdAt }}',
datasetId = '{{ datasetId }}',
date = '{{ date }}',
event = '{{ event }}',
indicator = '{{ indicator }}',
indicatorType = '{{ indicatorType }}',
insight = '{{ insight }}',
raw = '{{ raw }}',
targetCountry = '{{ targetCountry }}',
targetIndustry = '{{ targetIndustry }}',
tlp = '{{ tlp }}'
WHERE 
account_id = '{{ account_id }}' --required
AND event_id = '{{ event_id }}' --required
AND datasetId = '{{ datasetId }}' --required
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
uuid;
```
</TabItem>
</Tabs>
