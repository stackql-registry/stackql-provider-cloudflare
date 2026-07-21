--- 
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
  - radar
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

Creates, updates, deletes, gets or lists a <code>bots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.bots" /></td></tr>
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

Successful response.

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
    <td><CopyableCode code="bot" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Successful response.

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
    <td>The name of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A summary for the bot (e.g., purpose).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="operator" /></td>
    <td><code>string</code></td>
    <td>The organization that owns and operates the bot.</td>
</tr>
<tr>
    <td><CopyableCode code="slug" /></td>
    <td><code>string</code></td>
    <td>A kebab-case identifier derived from the bot name.</td>
</tr>
<tr>
    <td><CopyableCode code="userAgentPatterns" /></td>
    <td><code>array</code></td>
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
    <td><a href="#parameter-bot_slug"><code>bot_slug</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the requested bot information.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-botCategory"><code>botCategory</code></a>, <a href="#parameter-botOperator"><code>botOperator</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-botVerificationStatus"><code>botVerificationStatus</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves a list of bots.</td>
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
<tr id="parameter-bot_slug">
    <td><CopyableCode code="bot_slug" /></td>
    <td><code>string</code></td>
    <td>Bot slug.</td>
</tr>
<tr id="parameter-botCategory">
    <td><CopyableCode code="botCategory" /></td>
    <td><code>string</code></td>
    <td>Filters results by bot category.</td>
</tr>
<tr id="parameter-botOperator">
    <td><CopyableCode code="botOperator" /></td>
    <td><code>string</code></td>
    <td>Filters results by bot operator.</td>
</tr>
<tr id="parameter-botVerificationStatus">
    <td><CopyableCode code="botVerificationStatus" /></td>
    <td><code>string</code></td>
    <td>Filters results by bot verification status.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Filters results by bot kind.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects returned in the response.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>Skips the specified number of objects before fetching the results.</td>
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

Retrieves the requested bot information.

```sql
SELECT
bot
FROM cloudflare.radar.bots
WHERE bot_slug = '{{ bot_slug }}' -- required
AND format = '{{ format }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of bots.

```sql
SELECT
name,
category,
description,
kind,
operator,
slug,
userAgentPatterns
FROM cloudflare.radar.bots
WHERE limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND botCategory = '{{ botCategory }}'
AND botOperator = '{{ botOperator }}'
AND kind = '{{ kind }}'
AND botVerificationStatus = '{{ botVerificationStatus }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
