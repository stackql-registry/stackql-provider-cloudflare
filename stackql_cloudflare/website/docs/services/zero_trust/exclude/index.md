--- 
title: exclude
hide_title: false
hide_table_of_contents: false
keywords:
  - exclude
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

Creates, updates, deletes, gets or lists an <code>exclude</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exclude" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.exclude" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#devices_set_split_tunnel_exclude_list_for_a_device_settings_policy"><CopyableCode code="devices_set_split_tunnel_exclude_list_for_a_device_settings_policy" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Sets the list of routes excluded from the WARP client's tunnel for a specific device settings profile.</td>
</tr>
<tr>
    <td><a href="#devices_set_split_tunnel_exclude_list"><CopyableCode code="devices_set_split_tunnel_exclude_list" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Sets the list of routes excluded from the WARP client's tunnel.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="devices_set_split_tunnel_exclude_list_for_a_device_settings_policy"
    values={[
        { label: 'devices_set_split_tunnel_exclude_list_for_a_device_settings_policy', value: 'devices_set_split_tunnel_exclude_list_for_a_device_settings_policy' },
        { label: 'devices_set_split_tunnel_exclude_list', value: 'devices_set_split_tunnel_exclude_list' }
    ]}
>
<TabItem value="devices_set_split_tunnel_exclude_list_for_a_device_settings_policy">

Sets the list of routes excluded from the WARP client's tunnel for a specific device settings profile.

```sql
REPLACE cloudflare.zero_trust.exclude
SET 
-- No updatable properties
WHERE 
policy_id = '{{ policy_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
<TabItem value="devices_set_split_tunnel_exclude_list">

Sets the list of routes excluded from the WARP client's tunnel.

```sql
REPLACE cloudflare.zero_trust.exclude
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>
