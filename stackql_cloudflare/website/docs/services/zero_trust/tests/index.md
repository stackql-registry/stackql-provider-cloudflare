--- 
title: tests
hide_title: false
hide_table_of_contents: false
keywords:
  - tests
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

Creates, updates, deletes, gets or lists a <code>tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.tests" /></td></tr>
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

success response

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
    <td><CopyableCode code="overviewMetrics" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tests" /></td>
    <td><code>array</code></td>
    <td>array of test results objects.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-colo"><code>colo</code></a>, <a href="#parameter-testName"><code>testName</code></a>, <a href="#parameter-deviceId"><code>deviceId</code></a>, <a href="#parameter-registration_id"><code>registration_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td>List DEX tests with overview metrics</td>
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
<tr id="parameter-colo">
    <td><CopyableCode code="colo" /></td>
    <td><code>string</code></td>
    <td>Optionally filter result stats to a Cloudflare colo. Cannot be used in combination with deviceId param.</td>
</tr>
<tr id="parameter-deviceId">
    <td><CopyableCode code="deviceId" /></td>
    <td><code>array</code></td>
    <td>Optionally filter result stats to a specific device(s). Cannot be used in combination with colo param.</td>
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
<tr id="parameter-registration_id">
    <td><CopyableCode code="registration_id" /></td>
    <td><code>string</code></td>
    <td>Optionally filter results to a specific device registration. Must be used in combination with a single deviceId.</td>
</tr>
<tr id="parameter-testName">
    <td><CopyableCode code="testName" /></td>
    <td><code>string</code></td>
    <td>Optionally filter results by test name</td>
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

List DEX tests with overview metrics

```sql
SELECT
overviewMetrics,
tests
FROM cloudflare.zero_trust.tests
WHERE account_id = '{{ account_id }}' -- required
AND colo = '{{ colo }}'
AND testName = '{{ testName }}'
AND deviceId = '{{ deviceId }}'
AND registration_id = '{{ registration_id }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND kind = '{{ kind }}'
;
```
</TabItem>
</Tabs>
