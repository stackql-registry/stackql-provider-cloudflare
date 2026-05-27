--- 
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - api_gateway
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

Creates, updates, deletes, gets or lists a <code>user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.user" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieve user label response

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
    <td>The name of the label (example: login)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the label (example: All endpoints that deal with logins)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mapped_resources" /></td>
    <td><code>object</code></td>
    <td>Provides counts of what resources are linked to this label</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata for the label</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>* `user` - label is owned by the user * `managed` - label is owned by cloudflare (user, managed)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td><a href="#parameter-with_mapped_resource_counts"><code>with_mapped_resource_counts</code></a></td>
    <td>Retrieve user label</td>
</tr>
<tr>
    <td><a href="#api_shield_labels_create_user_labels"><CopyableCode code="api_shield_labels_create_user_labels" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Update certain fields on a label</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Update all fields on a label</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Delete user label</td>
</tr>
<tr>
    <td><a href="#api_shield_labels_delete_user_labels"><CopyableCode code="api_shield_labels_delete_user_labels" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-with_mapped_resource_counts">
    <td><CopyableCode code="with_mapped_resource_counts" /></td>
    <td><code>boolean</code></td>
    <td>Include `mapped_resources` for each label</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieve user label

```sql
SELECT
name,
created_at,
description,
last_updated,
mapped_resources,
metadata,
source
FROM cloudflare.api_gateway.user
WHERE zone_id = '{{ zone_id }}' -- required
AND name = '{{ name }}' -- required
AND with_mapped_resource_counts = '{{ with_mapped_resource_counts }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="api_shield_labels_create_user_labels"
    values={[
        { label: 'api_shield_labels_create_user_labels', value: 'api_shield_labels_create_user_labels' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="api_shield_labels_create_user_labels">

No description available.

```sql
INSERT INTO cloudflare.api_gateway.user (
zone_id
)
SELECT 
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: user
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the user resource.
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

Update certain fields on a label

```sql
UPDATE cloudflare.api_gateway.user
SET 
description = '{{ description }}',
metadata = '{{ metadata }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
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

Update all fields on a label

```sql
REPLACE cloudflare.api_gateway.user
SET 
description = '{{ description }}',
metadata = '{{ metadata }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
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
        { label: 'api_shield_labels_delete_user_labels', value: 'api_shield_labels_delete_user_labels' }
    ]}
>
<TabItem value="delete">

Delete user label

```sql
DELETE FROM cloudflare.api_gateway.user
WHERE zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
;
```
</TabItem>
<TabItem value="api_shield_labels_delete_user_labels">

No description available.

```sql
DELETE FROM cloudflare.api_gateway.user
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
