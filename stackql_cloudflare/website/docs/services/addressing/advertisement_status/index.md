--- 
title: advertisement_status
hide_title: false
hide_table_of_contents: false
keywords:
  - advertisement_status
  - addressing
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

Creates, updates, deletes, gets or lists an <code>advertisement_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="advertisement_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.advertisement_status" /></td></tr>
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

Get Advertisement Status response

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
    <td><CopyableCode code="advertised" /></td>
    <td><code>boolean</code></td>
    <td>Advertisement status of the prefix. If `true`, the BGP route for the prefix is advertised to the Internet. If `false`, the BGP route is withdrawn.</td>
</tr>
<tr>
    <td><CopyableCode code="advertised_modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the advertisement status was changed. This field is only not 'null' if on demand is enabled. (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>View the current advertisement state for a prefix. **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing subnets of an IP prefix.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-advertised"><code>advertised</code></a></td>
    <td></td>
    <td>Advertise or withdraw the BGP route for a prefix. **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing subnets of an IP prefix.</td>
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
<tr id="parameter-prefix_id">
    <td><CopyableCode code="prefix_id" /></td>
    <td><code>string</code></td>
    <td>The IP prefix ID.</td>
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

View the current advertisement state for a prefix. **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing subnets of an IP prefix.

```sql
SELECT
advertised,
advertised_modified_at
FROM cloudflare.addressing.advertisement_status
WHERE prefix_id = '{{ prefix_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Advertise or withdraw the BGP route for a prefix. **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing subnets of an IP prefix.

```sql
UPDATE cloudflare.addressing.advertisement_status
SET 
advertised = {{ advertised }}
WHERE 
prefix_id = '{{ prefix_id }}' --required
AND account_id = '{{ account_id }}' --required
AND advertised = {{ advertised }} --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
