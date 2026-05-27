--- 
title: monitor_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_groups
  - load_balancers
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

Creates, updates, deletes, gets or lists a <code>monitor_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitor_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.load_balancers.monitor_groups" /></td></tr>
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

Monitor Group Details response

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
    <td><code>string</code></td>
    <td>The ID of the Monitor Group to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the monitor group was created (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short description of the monitor group (example: Primary datacenter monitors)</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td>List of monitors in this group</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the monitor group was last updated (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Monitor Groups response

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
    <td><code>string</code></td>
    <td>The ID of the Monitor Group to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the monitor group was created (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short description of the monitor group (example: Primary datacenter monitors)</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td>List of monitors in this group</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the monitor group was last updated (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-monitor_group_id"><code>monitor_group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch a single configured monitor group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List configured monitor groups.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-members"><code>members</code></a></td>
    <td></td>
    <td>Create a new monitor group.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-monitor_group_id"><code>monitor_group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-members"><code>members</code></a></td>
    <td></td>
    <td>Apply changes to an existing monitor group, overwriting the supplied properties.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-monitor_group_id"><code>monitor_group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-members"><code>members</code></a></td>
    <td></td>
    <td>Modify a configured monitor group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-monitor_group_id"><code>monitor_group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured monitor group.</td>
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
<tr id="parameter-monitor_group_id">
    <td><CopyableCode code="monitor_group_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Fetch a single configured monitor group.

```sql
SELECT
id,
created_at,
description,
members,
updated_at
FROM cloudflare.load_balancers.monitor_groups
WHERE monitor_group_id = '{{ monitor_group_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List configured monitor groups.

```sql
SELECT
id,
created_at,
description,
members,
updated_at
FROM cloudflare.load_balancers.monitor_groups
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new monitor group.

```sql
INSERT INTO cloudflare.load_balancers.monitor_groups (
description,
id,
members,
account_id
)
SELECT 
'{{ description }}' /* required */,
'{{ id }}' /* required */,
'{{ members }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: monitor_groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the monitor_groups resource.
    - name: description
      value: "{{ description }}"
      description: |
        A short description of the monitor group
    - name: id
      value: "{{ id }}"
      description: |
        The ID of the Monitor Group to use for checking the health of origins within this pool.
    - name: members
      description: |
        List of monitors in this group
      value:
        - created_at: "{{ created_at }}"
          enabled: {{ enabled }}
          monitor_id: "{{ monitor_id }}"
          monitoring_only: {{ monitoring_only }}
          must_be_healthy: {{ must_be_healthy }}
          updated_at: "{{ updated_at }}"
`}</CodeBlock>

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

Apply changes to an existing monitor group, overwriting the supplied properties.

```sql
UPDATE cloudflare.load_balancers.monitor_groups
SET 
description = '{{ description }}',
id = '{{ id }}',
members = '{{ members }}'
WHERE 
monitor_group_id = '{{ monitor_group_id }}' --required
AND account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
AND description = '{{ description }}' --required
AND members = '{{ members }}' --required
RETURNING
errors,
messages,
result,
success;
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

Modify a configured monitor group.

```sql
REPLACE cloudflare.load_balancers.monitor_groups
SET 
description = '{{ description }}',
id = '{{ id }}',
members = '{{ members }}'
WHERE 
monitor_group_id = '{{ monitor_group_id }}' --required
AND account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
AND description = '{{ description }}' --required
AND members = '{{ members }}' --required
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
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a configured monitor group.

```sql
DELETE FROM cloudflare.load_balancers.monitor_groups
WHERE monitor_group_id = '{{ monitor_group_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
