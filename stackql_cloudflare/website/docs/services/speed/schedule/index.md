--- 
title: schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule
  - speed
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

Creates, updates, deletes, gets or lists a <code>schedule</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schedule" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.speed.schedule" /></td></tr>
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

Page test schedule.

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
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>The frequency of the test. (DAILY, WEEKLY) (example: DAILY)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>A test region. (asia-east1, asia-northeast1, asia-northeast2, asia-south1, asia-southeast1, australia-southeast1, europe-north1, europe-southwest1, europe-west1, europe-west2, europe-west3, europe-west4, europe-west8, europe-west9, me-west1, southamerica-east1, us-central1, us-east1, us-east4, us-south1, us-west1) (example: us-central1)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>A URL. (example: example.com)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-region"><code>region</code></a></td>
    <td>Retrieves the test schedule for a page in a specific region.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-region"><code>region</code></a>, <a href="#parameter-frequency"><code>frequency</code></a></td>
    <td>Creates a scheduled test for a page.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-region"><code>region</code></a></td>
    <td>Deletes a scheduled test for a page.</td>
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
<tr id="parameter-url">
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-frequency">
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>The frequency of the scheduled test. Defaults to WEEKLY for free plans, DAILY for paid plans.</td>
</tr>
<tr id="parameter-region">
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
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

Retrieves the test schedule for a page in a specific region.

```sql
SELECT
frequency,
region,
url
FROM cloudflare.speed.schedule
WHERE zone_id = '{{ zone_id }}' -- required
AND url = '{{ url }}' -- required
AND region = '{{ region }}'
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

Creates a scheduled test for a page.

```sql
INSERT INTO cloudflare.speed.schedule (
zone_id,
url,
region,
frequency
)
SELECT 
'{{ zone_id }}',
'{{ url }}',
'{{ region }}',
'{{ frequency }}'
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
- name: schedule
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the schedule resource.
    - name: url
      value: "{{ url }}"
      description: Required parameter for the schedule resource.
    - name: region
      value: "{{ region }}"
    - name: frequency
      value: "{{ frequency }}"
      description: The frequency of the scheduled test. Defaults to WEEKLY for free plans, DAILY for paid plans.
      description: The frequency of the scheduled test. Defaults to WEEKLY for free plans, DAILY for paid plans.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a scheduled test for a page.

```sql
DELETE FROM cloudflare.speed.schedule
WHERE zone_id = '{{ zone_id }}' --required
AND url = '{{ url }}' --required
AND region = '{{ region }}'
;
```
</TabItem>
</Tabs>
