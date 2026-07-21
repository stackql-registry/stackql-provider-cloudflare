--- 
title: relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - relationships
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

Creates, updates, deletes, gets or lists a <code>relationships</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="relationships" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.relationships" /></td></tr>
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

Returns a list of events related to the specified starting event.

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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a></td>
    <td><a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-maxDepth"><code>maxDepth</code></a>, <a href="#parameter-relationshipTypes"><code>relationshipTypes</code></a>, <a href="#parameter-indicatorTypeIds"><code>indicatorTypeIds</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a>, <a href="#parameter-includeParent"><code>includeParent</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a></td>
    <td>The `event_id` must be defined (to list existing events (and their IDs), use the [`Filter and List Events`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/) endpoint). Also, must provide query parameters.</td>
</tr>
<tr>
    <td><a href="#post_dosevent_create_bulk_with_relationships"><CopyableCode code="post_dosevent_create_bulk_with_relationships" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-data"><code>data</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a></td>
    <td></td>
    <td>This method is deprecated. Please use `event_create_bulk` instead</td>
</tr>
<tr>
    <td><a href="#create_relate"><CopyableCode code="create_relate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-events"><code>events</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-parentId"><code>parentId</code></a>, <a href="#parameter-childIds"><code>childIds</code></a>, <a href="#parameter-relationshipType"><code>relationshipType</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a></td>
    <td></td>
    <td>Creates a directed relationship between two events. The relationship is from parent to child with a specified type.</td>
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
<tr id="parameter-datasetId">
    <td><CopyableCode code="datasetId" /></td>
    <td><code>string</code></td>
    <td>The dataset ID to search within.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction to traverse the graph. Defaults to 'both' to search all.</td>
</tr>
<tr id="parameter-includeParent">
    <td><CopyableCode code="includeParent" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include the starting event in the results. Defaults to true.</td>
</tr>
<tr id="parameter-indicatorTypeIds">
    <td><CopyableCode code="indicatorTypeIds" /></td>
    <td><code>array</code></td>
    <td>An optional array of indicator type IDs to filter the results by.</td>
</tr>
<tr id="parameter-maxDepth">
    <td><CopyableCode code="maxDepth" /></td>
    <td><code>number</code></td>
    <td>The maximum depth to traverse. Defaults to 5.</td>
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
<tr id="parameter-relationshipTypes">
    <td><CopyableCode code="relationshipTypes" /></td>
    <td><code>string</code></td>
    <td>An optional array of relationship types to filter by.</td>
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

The `event_id` must be defined (to list existing events (and their IDs), use the [`Filter and List Events`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/) endpoint). Also, must provide query parameters.

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
FROM cloudflare.cloudforce_one.relationships
WHERE account_id = '{{ account_id }}' -- required
AND event_id = '{{ event_id }}' -- required
AND direction = '{{ direction }}'
AND maxDepth = '{{ maxDepth }}'
AND relationshipTypes = '{{ relationshipTypes }}'
AND indicatorTypeIds = '{{ indicatorTypeIds }}'
AND datasetId = '{{ datasetId }}'
AND includeParent = '{{ includeParent }}'
AND page = '{{ page }}'
AND pageSize = '{{ pageSize }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_dosevent_create_bulk_with_relationships"
    values={[
        { label: 'post_dosevent_create_bulk_with_relationships', value: 'post_dosevent_create_bulk_with_relationships' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_dosevent_create_bulk_with_relationships">

This method is deprecated. Please use `event_create_bulk` instead

```sql
INSERT INTO cloudflare.cloudforce_one.relationships (
data,
datasetId,
account_id
)
SELECT 
'{{ data }}' /* required */,
'{{ datasetId }}' /* required */,
'{{ account_id }}'
RETURNING
createdEventsCount,
createdIndicatorsCount,
createdRelationshipsCount,
errorCount,
errors
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: relationships
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the relationships resource.
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
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_relate"
    values={[
        { label: 'create_relate', value: 'create_relate' },
        { label: 'create', value: 'create' }
    ]}
>
<TabItem value="create_relate">

Returns success if operation succeeded.

```sql
EXEC cloudflare.cloudforce_one.relationships.create_relate 
@account_id='{{ account_id }}' --required, 
@event_id='{{ event_id }}' --required 
@@json=
'{
"events": "{{ events }}"
}'
;
```
</TabItem>
<TabItem value="create">

Creates a directed relationship between two events. The relationship is from parent to child with a specified type.

```sql
EXEC cloudflare.cloudforce_one.relationships.create 
@account_id='{{ account_id }}' --required 
@@json=
'{
"childIds": "{{ childIds }}", 
"datasetId": "{{ datasetId }}", 
"parentId": "{{ parentId }}", 
"relationshipType": "{{ relationshipType }}"
}'
;
```
</TabItem>
</Tabs>
