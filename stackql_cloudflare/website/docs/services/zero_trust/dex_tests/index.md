--- 
title: dex_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - dex_tests
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>dex_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dex_tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.dex_tests" /></td></tr>
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

Device DEX test details response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the DEX test. Must be unique. (example: HTTP dash health check)</td>
</tr>
<tr>
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the test. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>The configuration object which contains the details for the WARP client to conduct the test.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Additional details about the test. (example: Checks the dash endpoint every 30 minutes)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether or not the test is active.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>How often the test will run. (example: 30m)</td>
</tr>
<tr>
    <td><CopyableCode code="target_policies" /></td>
    <td><code>array</code></td>
    <td>DEX rules targeted by this test</td>
</tr>
<tr>
    <td><CopyableCode code="targeted" /></td>
    <td><code>boolean</code></td>
    <td> (x-stainless-terraform-configurability: computed)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Device DEX test details response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the DEX test. Must be unique. (example: HTTP dash health check)</td>
</tr>
<tr>
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the test. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>The configuration object which contains the details for the WARP client to conduct the test.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Additional details about the test. (example: Checks the dash endpoint every 30 minutes)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether or not the test is active.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>How often the test will run. (example: 30m)</td>
</tr>
<tr>
    <td><CopyableCode code="target_policies" /></td>
    <td><code>array</code></td>
    <td>DEX rules targeted by this test</td>
</tr>
<tr>
    <td><CopyableCode code="targeted" /></td>
    <td><code>boolean</code></td>
    <td> (x-stainless-terraform-configurability: computed)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dex_test_id"><code>dex_test_id</code></a></td>
    <td></td>
    <td>Fetch a single DEX test.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-testName"><code>testName</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td>Fetch all DEX tests</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-data"><code>data</code></a></td>
    <td></td>
    <td>Create a DEX test.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dex_test_id"><code>dex_test_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-data"><code>data</code></a></td>
    <td></td>
    <td>Update a DEX test.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dex_test_id"><code>dex_test_id</code></a></td>
    <td></td>
    <td>Delete a Device DEX test. Returns the remaining device dex tests for the account.</td>
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
<tr id="parameter-dex_test_id">
    <td><CopyableCode code="dex_test_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Filter by test type</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td>Page number of paginated results</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Number of items per page</td>
</tr>
<tr id="parameter-testName">
    <td><CopyableCode code="testName" /></td>
    <td><code>string</code></td>
    <td>Filter by test name</td>
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

Fetch a single DEX test.

```sql
SELECT
name,
test_id,
data,
description,
enabled,
interval,
target_policies,
targeted
FROM cloudflare.zero_trust.dex_tests
WHERE account_id = '{{ account_id }}' -- required
AND dex_test_id = '{{ dex_test_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetch all DEX tests

```sql
SELECT
name,
test_id,
data,
description,
enabled,
interval,
target_policies,
targeted
FROM cloudflare.zero_trust.dex_tests
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND testName = '{{ testName }}'
AND kind = '{{ kind }}'
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

Create a DEX test.

```sql
INSERT INTO cloudflare.zero_trust.dex_tests (
data,
description,
enabled,
interval,
name,
target_policies,
targeted,
account_id
)
SELECT 
'{{ data }}' /* required */,
'{{ description }}',
{{ enabled }} /* required */,
'{{ interval }}' /* required */,
'{{ name }}' /* required */,
'{{ target_policies }}',
{{ targeted }},
'{{ account_id }}'
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
- name: dex_tests
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the dex_tests resource.
    - name: data
      description: |
        The configuration object which contains the details for the WARP client to conduct the test.
      value:
        host: "{{ host }}"
        kind: "{{ kind }}"
        method: "{{ method }}"
    - name: description
      value: "{{ description }}"
      description: |
        Additional details about the test.
    - name: enabled
      value: {{ enabled }}
      description: |
        Determines whether or not the test is active.
    - name: interval
      value: "{{ interval }}"
      description: |
        How often the test will run.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the DEX test. Must be unique.
    - name: target_policies
      description: |
        DEX rules targeted by this test
      value:
        - default: {{ default }}
          id: "{{ id }}"
          name: "{{ name }}"
    - name: targeted
      value: {{ targeted }}
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

Update a DEX test.

```sql
REPLACE cloudflare.zero_trust.dex_tests
SET 
data = '{{ data }}',
description = '{{ description }}',
enabled = {{ enabled }},
interval = '{{ interval }}',
name = '{{ name }}',
target_policies = '{{ target_policies }}',
targeted = {{ targeted }}
WHERE 
account_id = '{{ account_id }}' --required
AND dex_test_id = '{{ dex_test_id }}' --required
AND name = '{{ name }}' --required
AND interval = '{{ interval }}' --required
AND enabled = {{ enabled }} --required
AND data = '{{ data }}' --required
RETURNING
errors,
messages,
result,
success;
```
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

Delete a Device DEX test. Returns the remaining device dex tests for the account.

```sql
DELETE FROM cloudflare.zero_trust.dex_tests
WHERE account_id = '{{ account_id }}' --required
AND dex_test_id = '{{ dex_test_id }}' --required
;
```
</TabItem>
</Tabs>
