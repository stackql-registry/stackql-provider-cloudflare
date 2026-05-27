--- 
title: routes_pfx2as
hide_title: false
hide_table_of_contents: false
keywords:
  - routes_pfx2as
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

Creates, updates, deletes, gets or lists a <code>routes_pfx2as</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routes_pfx2as" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.routes_pfx2as" /></td></tr>
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
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="prefix_origins" /></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-origin"><code>origin</code></a>, <a href="#parameter-rpkiStatus"><code>rpkiStatus</code></a>, <a href="#parameter-longestPrefixMatch"><code>longestPrefixMatch</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the prefix-to-ASN mapping from global routing tables.</td>
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
<tr id="parameter-longestPrefixMatch">
    <td><CopyableCode code="longestPrefixMatch" /></td>
    <td><code>boolean</code></td>
    <td>Return only results with the longest prefix match for the given prefix. For example, specify a /32 prefix to lookup the origin ASN for an IPv4 address.</td>
</tr>
<tr id="parameter-origin">
    <td><CopyableCode code="origin" /></td>
    <td><code>integer</code></td>
    <td>Lookup prefixes originated by the given ASN.</td>
</tr>
<tr id="parameter-prefix">
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-rpkiStatus">
    <td><CopyableCode code="rpkiStatus" /></td>
    <td><code>string</code></td>
    <td>Return only results with matching rpki status: valid, invalid or unknown.</td>
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

Retrieves the prefix-to-ASN mapping from global routing tables.

```sql
SELECT
meta,
prefix_origins
FROM cloudflare.radar.routes_pfx2as
WHERE prefix = '{{ prefix }}'
AND origin = '{{ origin }}'
AND rpkiStatus = '{{ rpkiStatus }}'
AND longestPrefixMatch = '{{ longestPrefixMatch }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
