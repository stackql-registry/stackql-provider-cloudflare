--- 
title: radar_tlds
hide_title: false
hide_table_of_contents: false
keywords:
  - radar_tlds
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

Creates, updates, deletes, gets or lists a <code>radar_tlds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="radar_tlds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.radar_tlds" /></td></tr>
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
    <td><CopyableCode code="manager" /></td>
    <td><code>string</code></td>
    <td>The organization that manages the TLD.</td>
</tr>
<tr>
    <td><CopyableCode code="tld" /></td>
    <td><code>string</code></td>
    <td>The actual TLD.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of TLD.</td>
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
    <td></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-tldManager"><code>tldManager</code></a>, <a href="#parameter-tldType"><code>tldType</code></a>, <a href="#parameter-tld"><code>tld</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves a list of TLDs.</td>
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
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
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
<tr id="parameter-tld">
    <td><CopyableCode code="tld" /></td>
    <td><code>string</code></td>
    <td>Filters results by top-level domain. Specify a comma-separated list of TLDs.</td>
</tr>
<tr id="parameter-tldManager">
    <td><CopyableCode code="tldManager" /></td>
    <td><code>string</code></td>
    <td>Filters results by TLD manager.</td>
</tr>
<tr id="parameter-tldType">
    <td><CopyableCode code="tldType" /></td>
    <td><code>string</code></td>
    <td>Filters results by TLD type.</td>
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

Retrieves a list of TLDs.

```sql
SELECT
manager,
tld,
type
FROM cloudflare.radar.radar_tlds
WHERE limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND tldManager = '{{ tldManager }}'
AND tldType = '{{ tldType }}'
AND tld = '{{ tld }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
