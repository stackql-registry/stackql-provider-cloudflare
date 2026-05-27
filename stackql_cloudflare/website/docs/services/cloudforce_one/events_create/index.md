--- 
title: events_create
hide_title: false
hide_table_of_contents: false
keywords:
  - events_create
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

Creates, updates, deletes, gets or lists an <code>events_create</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="events_create" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.events_create" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-date"><code>date</code></a>, <a href="#parameter-category"><code>category</code></a>, <a href="#parameter-event"><code>event</code></a>, <a href="#parameter-tlp"><code>tlp</code></a>, <a href="#parameter-raw"><code>raw</code></a></td>
    <td></td>
    <td>To create a dataset, see the [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/) endpoint. When `datasetId` parameter is unspecified, it will be created in a default dataset named `Cloudforce One Threat Events`.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' }
    ]}
>
<TabItem value="create_by_account">

To create a dataset, see the [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/) endpoint. When `datasetId` parameter is unspecified, it will be created in a default dataset named `Cloudforce One Threat Events`.

```sql
EXEC cloudflare.cloudforce_one.events_create.create_by_account 
@account_id='{{ account_id }}' --required 
@@json=
'{
"accountId": {{ accountId }}, 
"attacker": "{{ attacker }}", 
"attackerCountry": "{{ attackerCountry }}", 
"category": "{{ category }}", 
"datasetId": "{{ datasetId }}", 
"date": "{{ date }}", 
"event": "{{ event }}", 
"indicator": "{{ indicator }}", 
"indicatorType": "{{ indicatorType }}", 
"indicators": "{{ indicators }}", 
"insight": "{{ insight }}", 
"raw": "{{ raw }}", 
"tags": "{{ tags }}", 
"targetCountry": "{{ targetCountry }}", 
"targetIndustry": "{{ targetIndustry }}", 
"tlp": "{{ tlp }}"
}'
;
```
</TabItem>
</Tabs>
