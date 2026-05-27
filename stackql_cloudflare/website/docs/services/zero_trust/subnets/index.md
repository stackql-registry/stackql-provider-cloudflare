--- 
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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

Creates, updates, deletes, gets or lists a <code>subnets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subnets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.subnets" /></td></tr>
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

List subnets response

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
    <td><CopyableCode code="id" /></td>
    <td><code>string (uuid)</code></td>
    <td>The UUID of the subnet. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the subnet. (example: IPv4 Cloudflare Source IPs)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>An optional description of the subnet. (default: , example: example comment, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was created. (example: 2021-01-25T18:22:34.317854Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was deleted. If `null`, the resource has not been deleted. (example: 2009-11-10T23:00:00.000000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_default_network" /></td>
    <td><code>boolean</code></td>
    <td>If `true`, this is the default subnet for the account. There can only be one default subnet per account. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td>The private IPv4 or IPv6 range defining the subnet, in CIDR notation. (example: 100.64.0.0/12)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_type" /></td>
    <td><code>string</code></td>
    <td>The type of subnet. (cloudflare_source, warp) (example: cloudflare_source)</td>
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-comment"><code>comment</code></a>, <a href="#parameter-network"><code>network</code></a>, <a href="#parameter-existed_at"><code>existed_at</code></a>, <a href="#parameter-address_family"><code>address_family</code></a>, <a href="#parameter-is_default_network"><code>is_default_network</code></a>, <a href="#parameter-is_deleted"><code>is_deleted</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-subnet_types"><code>subnet_types</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a></td>
    <td>Lists and filters subnets in an account.</td>
</tr>
<tr>
    <td><a href="#update_cloudflare_source"><CopyableCode code="update_cloudflare_source" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-address_family"><code>address_family</code></a></td>
    <td></td>
    <td>Updates the Cloudflare Source subnet of the given address family</td>
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
<tr id="parameter-address_family">
    <td><CopyableCode code="address_family" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-address_family">
    <td><CopyableCode code="address_family" /></td>
    <td><code>string</code></td>
    <td>If set, only include subnets in the given address family - `v4` or `v6`</td>
</tr>
<tr id="parameter-comment">
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-existed_at">
    <td><CopyableCode code="existed_at" /></td>
    <td><code>string (url-encoded-date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-is_default_network">
    <td><CopyableCode code="is_default_network" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-is_deleted">
    <td><CopyableCode code="is_deleted" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>If set, only list subnets with the given name</td>
</tr>
<tr id="parameter-network">
    <td><CopyableCode code="network" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-subnet_types">
    <td><CopyableCode code="subnet_types" /></td>
    <td><code>string</code></td>
    <td></td>
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

Lists and filters subnets in an account.

```sql
SELECT
id,
name,
comment,
created_at,
deleted_at,
is_default_network,
network,
subnet_type
FROM cloudflare.zero_trust.subnets
WHERE account_id = '{{ account_id }}' -- required
AND name = '{{ name }}'
AND comment = '{{ comment }}'
AND network = '{{ network }}'
AND existed_at = '{{ existed_at }}'
AND address_family = '{{ address_family }}'
AND is_default_network = '{{ is_default_network }}'
AND is_deleted = '{{ is_deleted }}'
AND sort_order = '{{ sort_order }}'
AND subnet_types = '{{ subnet_types }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_cloudflare_source"
    values={[
        { label: 'update_cloudflare_source', value: 'update_cloudflare_source' }
    ]}
>
<TabItem value="update_cloudflare_source">

Updates the Cloudflare Source subnet of the given address family

```sql
EXEC cloudflare.zero_trust.subnets.update_cloudflare_source 
@account_id='{{ account_id }}' --required, 
@address_family='{{ address_family }}' --required 
@@json=
'{
"comment": "{{ comment }}", 
"name": "{{ name }}", 
"network": "{{ network }}"
}'
;
```
</TabItem>
</Tabs>
