--- 
title: v2_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - v2_responses
  - url_scanner
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

Creates, updates, deletes, gets or lists a <code>v2_responses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="v2_responses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.url_scanner.v2_responses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_responses_v2"
    values={[
        { label: 'get_responses_v2', value: 'get_responses_v2' }
    ]}
>
<TabItem value="get_responses_v2">

Get the raw response by its hash.

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
    <td><CopyableCode code="contents" /></td>
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
    <td><a href="#get_responses_v2"><CopyableCode code="get_responses_v2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-response_id"><code>response_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns the raw response of the network request. Find the `response_id` in the `data.requests.response.hash`.</td>
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
<tr id="parameter-response_id">
    <td><CopyableCode code="response_id" /></td>
    <td><code>string</code></td>
    <td>Response hash.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_responses_v2"
    values={[
        { label: 'get_responses_v2', value: 'get_responses_v2' }
    ]}
>
<TabItem value="get_responses_v2">

Returns the raw response of the network request. Find the `response_id` in the `data.requests.response.hash`.

```sql
SELECT
contents
FROM cloudflare.url_scanner.v2_responses
WHERE response_id = '{{ response_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
