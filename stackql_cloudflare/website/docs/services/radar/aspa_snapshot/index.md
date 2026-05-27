--- 
title: aspa_snapshot
hide_title: false
hide_table_of_contents: false
keywords:
  - aspa_snapshot
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

Creates, updates, deletes, gets or lists an <code>aspa_snapshot</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="aspa_snapshot" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.aspa_snapshot" /></td></tr>
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
    <td><CopyableCode code="asnInfo" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aspaObjects" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
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
    <td><a href="#parameter-customerAsn"><code>customerAsn</code></a>, <a href="#parameter-providerAsn"><code>providerAsn</code></a>, <a href="#parameter-date"><code>date</code></a>, <a href="#parameter-includeAsnInfo"><code>includeAsnInfo</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves current or historical ASPA (Autonomous System Provider Authorization) objects. ASPA objects define which ASNs are authorized upstream providers for a customer ASN.</td>
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
<tr id="parameter-customerAsn">
    <td><CopyableCode code="customerAsn" /></td>
    <td><code>integer</code></td>
    <td>Filter by customer ASN (the ASN publishing the ASPA object).</td>
</tr>
<tr id="parameter-date">
    <td><CopyableCode code="date" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filters results by the specified datetime (ISO 8601).</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-includeAsnInfo">
    <td><CopyableCode code="includeAsnInfo" /></td>
    <td><code>boolean</code></td>
    <td>Include ASN metadata (name, country) in response.</td>
</tr>
<tr id="parameter-providerAsn">
    <td><CopyableCode code="providerAsn" /></td>
    <td><code>integer</code></td>
    <td>Filter by provider ASN (an authorized upstream provider in ASPA objects).</td>
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

Retrieves current or historical ASPA (Autonomous System Provider Authorization) objects. ASPA objects define which ASNs are authorized upstream providers for a customer ASN.

```sql
SELECT
asnInfo,
aspaObjects,
meta
FROM cloudflare.radar.aspa_snapshot
WHERE customerAsn = '{{ customerAsn }}'
AND providerAsn = '{{ providerAsn }}'
AND date = '{{ date }}'
AND includeAsnInfo = '{{ includeAsnInfo }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
