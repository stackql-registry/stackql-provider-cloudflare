--- 
title: http_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - http_tests
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

Creates, updates, deletes, gets or lists a <code>http_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="http_tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.http_tests" /></td></tr>
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

DEX HTTP test details response

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
    <td>The name of the HTTP synthetic application test (example: Atlassian Sign In Page)</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td>The url of the HTTP synthetic application test (example: http://example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="httpStats" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="httpStatsByColo" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval at which the HTTP synthetic application test is set to run. (example: 0h5m0s)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td> (http)</td>
</tr>
<tr>
    <td><CopyableCode code="method" /></td>
    <td><code>string</code></td>
    <td>The HTTP method to use when running the test (example: GET)</td>
</tr>
<tr>
    <td><CopyableCode code="target_policies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="targeted" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-test_id"><code>test_id</code></a></td>
    <td><a href="#parameter-deviceId"><code>deviceId</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-colo"><code>colo</code></a></td>
    <td>Get test details and aggregate performance metrics for an http test for a given time period between 1 hour and 7 days.</td>
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
<tr id="parameter-test_id">
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td>unique identifier for a specific test</td>
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
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>string</code></td>
    <td>Start time for aggregate metrics in ISO ms</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>Time interval for aggregate time slots.</td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>string</code></td>
    <td>End time for aggregate metrics in ISO ms</td>
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

Get test details and aggregate performance metrics for an http test for a given time period between 1 hour and 7 days.

```sql
SELECT
name,
host,
httpStats,
httpStatsByColo,
interval,
kind,
method,
target_policies,
targeted
FROM cloudflare.zero_trust.http_tests
WHERE account_id = '{{ account_id }}' -- required
AND test_id = '{{ test_id }}' -- required
AND deviceId = '{{ deviceId }}'
AND from = '{{ from }}'
AND to = '{{ to }}'
AND interval = '{{ interval }}'
AND colo = '{{ colo }}'
;
```
</TabItem>
</Tabs>
