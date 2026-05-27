--- 
title: tests
hide_title: false
hide_table_of_contents: false
keywords:
  - tests
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

Creates, updates, deletes, gets or lists a <code>tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.speed.tests" /></td></tr>
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

Page test result.

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="desktopReport" /></td>
    <td><code>object</code></td>
    <td>The Lighthouse report.</td>
</tr>
<tr>
    <td><CopyableCode code="mobileReport" /></td>
    <td><code>object</code></td>
    <td>The Lighthouse report.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>object</code></td>
    <td>A test region with a label.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency of the test. (DAILY, WEEKLY) (example: DAILY)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>A URL. (example: example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of test history for a page.

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="desktopReport" /></td>
    <td><code>object</code></td>
    <td>The Lighthouse report.</td>
</tr>
<tr>
    <td><CopyableCode code="mobileReport" /></td>
    <td><code>object</code></td>
    <td>The Lighthouse report.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>object</code></td>
    <td>A test region with a label.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleFrequency" /></td>
    <td><code>string</code></td>
    <td>The frequency of the test. (DAILY, WEEKLY) (example: DAILY)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-test_id"><code>test_id</code></a></td>
    <td></td>
    <td>Retrieves the result of a specific test.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td>Test history (list of tests) for a specific webpage.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Starts a test for a specific webpage, in a specific region.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-region"><code>region</code></a></td>
    <td>Deletes all tests for a specific webpage from a specific region. Deleted tests are still counted as part of the quota.</td>
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
<tr id="parameter-test_id">
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
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
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves the result of a specific test.

```sql
SELECT
id,
date,
desktopReport,
mobileReport,
region,
scheduleFrequency,
url
FROM cloudflare.speed.tests
WHERE zone_id = '{{ zone_id }}' -- required
AND url = '{{ url }}' -- required
AND test_id = '{{ test_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Test history (list of tests) for a specific webpage.

```sql
SELECT
id,
date,
desktopReport,
mobileReport,
region,
scheduleFrequency,
url
FROM cloudflare.speed.tests
WHERE zone_id = '{{ zone_id }}' -- required
AND url = '{{ url }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Starts a test for a specific webpage, in a specific region.

```sql
INSERT INTO cloudflare.speed.tests (
region,
zone_id,
url
)
SELECT 
'{{ region }}',
'{{ zone_id }}',
'{{ url }}'
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
- name: tests
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the tests resource.
    - name: url
      value: "{{ url }}"
      description: Required parameter for the tests resource.
    - name: region
      value: "{{ region }}"
      description: |
        A test region.
      valid_values: ['asia-east1', 'asia-northeast1', 'asia-northeast2', 'asia-south1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-southwest1', 'europe-west1', 'europe-west2', 'europe-west3', 'europe-west4', 'europe-west8', 'europe-west9', 'me-west1', 'southamerica-east1', 'us-central1', 'us-east1', 'us-east4', 'us-south1', 'us-west1']
      default: us-central1
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

Deletes all tests for a specific webpage from a specific region. Deleted tests are still counted as part of the quota.

```sql
DELETE FROM cloudflare.speed.tests
WHERE zone_id = '{{ zone_id }}' --required
AND url = '{{ url }}' --required
AND region = '{{ region }}'
;
```
</TabItem>
</Tabs>
