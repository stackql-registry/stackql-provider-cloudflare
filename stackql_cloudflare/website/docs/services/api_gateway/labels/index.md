--- 
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
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

Creates, updates, deletes, gets or lists a <code>labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="labels" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.labels" /></td></tr>
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

Retrieve all labels response

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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-with_mapped_resource_counts"><code>with_mapped_resource_counts</code></a></td>
    <td>Retrieve all labels</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Attach label(s) on an operation in endpoint management</td>
</tr>
<tr>
    <td><a href="#api_shield_operations_bulk_post_labels_to_operations"><CopyableCode code="api_shield_operations_bulk_post_labels_to_operations" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-selector"><code>selector</code></a></td>
    <td></td>
    <td>Bulk attach label(s) on operation(s) in endpoint management</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Replace label(s) on an operation in endpoint management</td>
</tr>
<tr>
    <td><a href="#api_shield_operations_bulk_put_labels_to_operations"><CopyableCode code="api_shield_operations_bulk_put_labels_to_operations" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-selector"><code>selector</code></a>, <a href="#parameter-user"><code>user</code></a>, <a href="#parameter-managed"><code>managed</code></a></td>
    <td></td>
    <td>Bulk replace label(s) on operation(s) in endpoint management</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Remove label(s) on an operation in endpoint management</td>
</tr>
<tr>
    <td><a href="#api_shield_operations_bulk_delete_labels_to_operations"><CopyableCode code="api_shield_operations_bulk_delete_labels_to_operations" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Bulk remove label(s) on operation(s) in endpoint management</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for the operation</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Filter for labels where the name or description matches using substring match</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number of paginated results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results per page.</td>
</tr>
<tr id="parameter-source">
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Filter for labels with source</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieve all labels

```sql
SELECT
name,
created_at,
description,
last_updated,
mapped_resources,
metadata,
source
FROM cloudflare.api_gateway.labels
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND source = '{{ source }}'
AND filter = '{{ filter }}'
AND with_mapped_resource_counts = '{{ with_mapped_resource_counts }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'api_shield_operations_bulk_post_labels_to_operations', value: 'api_shield_operations_bulk_post_labels_to_operations' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Attach label(s) on an operation in endpoint management

```sql
INSERT INTO cloudflare.api_gateway.labels (
managed,
user,
zone_id,
operation_id
)
SELECT 
'{{ managed }}',
'{{ user }}',
'{{ zone_id }}',
'{{ operation_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="api_shield_operations_bulk_post_labels_to_operations">

Bulk attach label(s) on operation(s) in endpoint management

```sql
INSERT INTO cloudflare.api_gateway.labels (
managed,
selector,
user,
zone_id
)
SELECT 
'{{ managed }}',
'{{ selector }}' /* required */,
'{{ user }}',
'{{ zone_id }}'
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
- name: labels
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the labels resource.
    - name: operation_id
      value: "{{ operation_id }}"
      description: Required parameter for the labels resource.
    - name: managed
      value:
        labels:
          - "{{ labels }}"
    - name: user
      value:
        labels:
          - "{{ labels }}"
    - name: selector
      description: |
        Operation IDs selector
      value:
        include:
          operation_ids:
            - "{{ operation_ids }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'api_shield_operations_bulk_put_labels_to_operations', value: 'api_shield_operations_bulk_put_labels_to_operations' }
    ]}
>
<TabItem value="update">

Replace label(s) on an operation in endpoint management

```sql
REPLACE cloudflare.api_gateway.labels
SET 
managed = '{{ managed }}',
user = '{{ user }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND operation_id = '{{ operation_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="api_shield_operations_bulk_put_labels_to_operations">

Bulk replace label(s) on operation(s) in endpoint management

```sql
REPLACE cloudflare.api_gateway.labels
SET 
managed = '{{ managed }}',
selector = '{{ selector }}',
user = '{{ user }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND selector = '{{ selector }}' --required
AND user = '{{ user }}' --required
AND managed = '{{ managed }}' --required
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
        { label: 'api_shield_operations_bulk_delete_labels_to_operations', value: 'api_shield_operations_bulk_delete_labels_to_operations' }
    ]}
>
<TabItem value="delete">

Remove label(s) on an operation in endpoint management

```sql
DELETE FROM cloudflare.api_gateway.labels
WHERE zone_id = '{{ zone_id }}' --required
AND operation_id = '{{ operation_id }}' --required
;
```
</TabItem>
<TabItem value="api_shield_operations_bulk_delete_labels_to_operations">

Bulk remove label(s) on operation(s) in endpoint management

```sql
DELETE FROM cloudflare.api_gateway.labels
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
