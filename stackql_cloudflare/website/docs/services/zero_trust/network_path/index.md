--- 
title: network_path
hide_title: false
hide_table_of_contents: false
keywords:
  - network_path
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

Creates, updates, deletes, gets or lists a <code>network_path</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_path" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.network_path" /></td></tr>
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

DEX traceroute test result network path response

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
    <td><CopyableCode code="deviceName" /></td>
    <td><code>string</code></td>
    <td>name of the device associated with this network path response</td>
</tr>
<tr>
    <td><CopyableCode code="hops" /></td>
    <td><code>array</code></td>
    <td>an array of the hops taken by the device to reach the end destination</td>
</tr>
<tr>
    <td><CopyableCode code="resultId" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="testName" /></td>
    <td><code>string</code></td>
    <td>name of the tracroute test</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-test_result_id"><code>test_result_id</code></a></td>
    <td></td>
    <td>Get a breakdown of hops and performance metrics for a specific traceroute test run</td>
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
<tr id="parameter-test_result_id">
    <td><CopyableCode code="test_result_id" /></td>
    <td><code>string</code></td>
    <td>unique identifier for a specific traceroute test</td>
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

Get a breakdown of hops and performance metrics for a specific traceroute test run

```sql
SELECT
deviceName,
hops,
resultId,
testId,
testName
FROM cloudflare.zero_trust.network_path
WHERE account_id = '{{ account_id }}' -- required
AND test_result_id = '{{ test_result_id }}' -- required
;
```
</TabItem>
</Tabs>
