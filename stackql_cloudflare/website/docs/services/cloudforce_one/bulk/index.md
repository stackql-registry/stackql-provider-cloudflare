--- 
title: bulk
hide_title: false
hide_table_of_contents: false
keywords:
  - bulk
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

Creates, updates, deletes, gets or lists a <code>bulk</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bulk" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.bulk" /></td></tr>
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
    <td><a href="#post_indicator_create_bulk"><CopyableCode code="post_indicator_create_bulk" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-indicators"><code>indicators</code></a></td>
    <td></td>
    <td>Creates multiple indicators at once with their respective types and related datasets.</td>
</tr>
<tr>
    <td><a href="#patch_event_update_bulk"><CopyableCode code="patch_event_update_bulk" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-eventIds"><code>eventIds</code></a>, <a href="#parameter-datasetId"><code>datasetId</code></a>, <a href="#parameter-updates"><code>updates</code></a></td>
    <td></td>
    <td>Updates multiple events with the same field values. Maximum 100 events per request.</td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="post_indicator_create_bulk"
    values={[
        { label: 'post_indicator_create_bulk', value: 'post_indicator_create_bulk' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_indicator_create_bulk">

Creates multiple indicators at once with their respective types and related datasets.

```sql
INSERT INTO cloudflare.cloudforce_one.bulk (
autoCreateType,
indicators,
account_id,
dataset_id
)
SELECT 
{{ autoCreateType }},
'{{ indicators }}' /* required */,
'{{ account_id }}',
'{{ dataset_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bulk
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the bulk resource.
    - name: dataset_id
      value: "{{ dataset_id }}"
      description: Required parameter for the bulk resource.
    - name: autoCreateType
      value: {{ autoCreateType }}
      description: |
        Global flag to automatically create indicator types if they don't exist. Individual indicators can override this with their own autoCreateType flag.
    - name: indicators
      value:
        - autoCreateType: {{ autoCreateType }}
          indicatorType: "{{ indicatorType }}"
          relatedEvents: "{{ relatedEvents }}"
          tags: "{{ tags }}"
          value: "{{ value }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="patch_event_update_bulk"
    values={[
        { label: 'patch_event_update_bulk', value: 'patch_event_update_bulk' }
    ]}
>
<TabItem value="patch_event_update_bulk">

Updates multiple events with the same field values. Maximum 100 events per request.

```sql
UPDATE cloudflare.cloudforce_one.bulk
SET 
datasetId = '{{ datasetId }}',
eventIds = '{{ eventIds }}',
updates = '{{ updates }}'
WHERE 
account_id = '{{ account_id }}' --required
AND eventIds = '{{ eventIds }}' --required
AND datasetId = '{{ datasetId }}' --required
AND updates = '{{ updates }}' --required
RETURNING
failedCount,
failures,
updatedCount;
```
</TabItem>
</Tabs>
