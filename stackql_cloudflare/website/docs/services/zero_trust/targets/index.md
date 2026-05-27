--- 
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
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

Creates, updates, deletes, gets or lists a <code>targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="targets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.targets" /></td></tr>
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

Successfully retrieved the target

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
    <td>Target identifier (title: target_id)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was created (example: 2019-08-24T14:15:22Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>A non-unique field that refers to a target (example: infra-access-target)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>object</code></td>
    <td>The IPv4/IPv6 address that identifies where to reach a target</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was modified (example: 2019-08-24T14:15:22Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Successfully retrieved all targets in the account

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
    <td>Target identifier (title: target_id)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was created (example: 2019-08-24T14:15:22Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>A non-unique field that refers to a target (example: infra-access-target)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>object</code></td>
    <td>The IPv4/IPv6 address that identifies where to reach a target</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was modified (example: 2019-08-24T14:15:22Z)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-target_id"><code>target_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-hostname_contains"><code>hostname_contains</code></a>, <a href="#parameter-virtual_network_id"><code>virtual_network_id</code></a>, <a href="#parameter-ip_v4"><code>ip_v4</code></a>, <a href="#parameter-ip_v6"><code>ip_v6</code></a>, <a href="#parameter-created_before"><code>created_before</code></a>, <a href="#parameter-created_after"><code>created_after</code></a>, <a href="#parameter-modified_before"><code>modified_before</code></a>, <a href="#parameter-modified_after"><code>modified_after</code></a>, <a href="#parameter-ips"><code>ips</code></a>, <a href="#parameter-target_ids"><code>target_ids</code></a>, <a href="#parameter-ip_like"><code>ip_like</code></a>, <a href="#parameter-ipv4_start"><code>ipv4_start</code></a>, <a href="#parameter-ipv4_end"><code>ipv4_end</code></a>, <a href="#parameter-ipv6_start"><code>ipv6_start</code></a>, <a href="#parameter-ipv6_end"><code>ipv6_end</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>Lists and sorts an account’s targets. Filters are optional and are ANDed together.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-target_id"><code>target_id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-ip"><code>ip</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-target_id"><code>target_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Removes one or more targets.</td>
</tr>
<tr>
    <td><a href="#batch"><CopyableCode code="batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Adds one or more targets.</td>
</tr>
<tr>
    <td><a href="#batch_delete"><CopyableCode code="batch_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-target_ids"><code>target_ids</code></a></td>
    <td></td>
    <td>Removes one or more targets.</td>
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
<tr id="parameter-target_id">
    <td><CopyableCode code="target_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-created_after">
    <td><CopyableCode code="created_after" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was created after (inclusive)</td>
</tr>
<tr id="parameter-created_before">
    <td><CopyableCode code="created_before" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was created before (inclusive)</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The sorting direction.</td>
</tr>
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>Hostname of a target</td>
</tr>
<tr id="parameter-hostname_contains">
    <td><CopyableCode code="hostname_contains" /></td>
    <td><code>string</code></td>
    <td>Partial match to the hostname of a target</td>
</tr>
<tr id="parameter-ip_like">
    <td><CopyableCode code="ip_like" /></td>
    <td><code>string</code></td>
    <td>Filters for targets whose IP addresses look like the specified string. Supports `*` as a wildcard character</td>
</tr>
<tr id="parameter-ip_v4">
    <td><CopyableCode code="ip_v4" /></td>
    <td><code>string</code></td>
    <td>IPv4 address of the target</td>
</tr>
<tr id="parameter-ip_v6">
    <td><CopyableCode code="ip_v6" /></td>
    <td><code>string</code></td>
    <td>IPv6 address of the target</td>
</tr>
<tr id="parameter-ips">
    <td><CopyableCode code="ips" /></td>
    <td><code>array</code></td>
    <td>Filters for targets that have any of the following IP addresses. Specify `ips` multiple times in query parameter to build list of candidates.</td>
</tr>
<tr id="parameter-ipv4_end">
    <td><CopyableCode code="ipv4_end" /></td>
    <td><code>string</code></td>
    <td>Defines an IPv4 filter range's ending value (inclusive). Requires `ipv4_start` to be specified as well.</td>
</tr>
<tr id="parameter-ipv4_start">
    <td><CopyableCode code="ipv4_start" /></td>
    <td><code>string</code></td>
    <td>Defines an IPv4 filter range's starting value (inclusive). Requires `ipv4_end` to be specified as well.</td>
</tr>
<tr id="parameter-ipv6_end">
    <td><CopyableCode code="ipv6_end" /></td>
    <td><code>string</code></td>
    <td>Defines an IPv6 filter range's ending value (inclusive). Requires `ipv6_start` to be specified as well.</td>
</tr>
<tr id="parameter-ipv6_start">
    <td><CopyableCode code="ipv6_start" /></td>
    <td><code>string</code></td>
    <td>Defines an IPv6 filter range's starting value (inclusive). Requires `ipv6_end` to be specified as well.</td>
</tr>
<tr id="parameter-modified_after">
    <td><CopyableCode code="modified_after" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was modified after (inclusive)</td>
</tr>
<tr id="parameter-modified_before">
    <td><CopyableCode code="modified_before" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time at which the target was modified before (inclusive)</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>The field to sort by.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer (int32)</code></td>
    <td>Current page in the response</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer (int32)</code></td>
    <td>Max amount of entries returned per page</td>
</tr>
<tr id="parameter-target_ids">
    <td><CopyableCode code="target_ids" /></td>
    <td><code>array</code></td>
    <td>Filters for targets that have any of the following UUIDs. Specify `target_ids` multiple times in query parameter to build list of candidates.</td>
</tr>
<tr id="parameter-virtual_network_id">
    <td><CopyableCode code="virtual_network_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Private virtual network identifier of the target</td>
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

Successfully retrieved the target

```sql
SELECT
id,
created_at,
hostname,
ip,
modified_at
FROM cloudflare.zero_trust.targets
WHERE account_id = '{{ account_id }}' -- required
AND target_id = '{{ target_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists and sorts an account’s targets. Filters are optional and are ANDed together.

```sql
SELECT
id,
created_at,
hostname,
ip,
modified_at
FROM cloudflare.zero_trust.targets
WHERE account_id = '{{ account_id }}' -- required
AND hostname = '{{ hostname }}'
AND hostname_contains = '{{ hostname_contains }}'
AND virtual_network_id = '{{ virtual_network_id }}'
AND ip_v4 = '{{ ip_v4 }}'
AND ip_v6 = '{{ ip_v6 }}'
AND created_before = '{{ created_before }}'
AND created_after = '{{ created_after }}'
AND modified_before = '{{ modified_before }}'
AND modified_after = '{{ modified_after }}'
AND ips = '{{ ips }}'
AND target_ids = '{{ target_ids }}'
AND ip_like = '{{ ip_like }}'
AND ipv4_start = '{{ ipv4_start }}'
AND ipv4_end = '{{ ipv4_end }}'
AND ipv6_start = '{{ ipv6_start }}'
AND ipv6_end = '{{ ipv6_end }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

No description available.

```sql
REPLACE cloudflare.zero_trust.targets
SET 
hostname = '{{ hostname }}',
ip = '{{ ip }}'
WHERE 
account_id = '{{ account_id }}' --required
AND target_id = '{{ target_id }}' --required
AND hostname = '{{ hostname }}' --required
AND ip = '{{ ip }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'bulk_delete', value: 'bulk_delete' }
    ]}
>
<TabItem value="delete">

No description available.

```sql
DELETE FROM cloudflare.zero_trust.targets
WHERE account_id = '{{ account_id }}' --required
AND target_id = '{{ target_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Removes one or more targets.

```sql
DELETE FROM cloudflare.zero_trust.targets
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch"
    values={[
        { label: 'batch', value: 'batch' },
        { label: 'batch_delete', value: 'batch_delete' }
    ]}
>
<TabItem value="batch">

Adds one or more targets.

```sql
EXEC cloudflare.zero_trust.targets.batch 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="batch_delete">

Removes one or more targets.

```sql
EXEC cloudflare.zero_trust.targets.batch_delete 
@account_id='{{ account_id }}' --required 
@@json=
'{
"target_ids": "{{ target_ids }}"
}'
;
```
</TabItem>
</Tabs>
