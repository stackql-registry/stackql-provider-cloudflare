--- 
title: tables_maintenance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - tables_maintenance_configs
  - r2_data_catalog
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

Creates, updates, deletes, gets or lists a <code>tables_maintenance_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tables_maintenance_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2_data_catalog.tables_maintenance_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

Table maintenance configuration retrieved successfully.

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
    <td><CopyableCode code="maintenance_config" /></td>
    <td><code>object</code></td>
    <td>Configures maintenance for the table.</td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-namespace"><code>namespace</code></a>, <a href="#parameter-table_name"><code>table_name</code></a></td>
    <td></td>
    <td>Retrieve the maintenance configuration for a specific table, including compaction settings.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-namespace"><code>namespace</code></a>, <a href="#parameter-table_name"><code>table_name</code></a></td>
    <td></td>
    <td>Update the maintenance configuration for a specific table. This allows you to enable or disable compaction and adjust target file sizes for optimization.</td>
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
<tr id="parameter-bucket_name">
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>The R2 bucket name.</td>
</tr>
<tr id="parameter-namespace">
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace identifier (use %1F as separator for nested namespaces).</td>
</tr>
<tr id="parameter-table_name">
    <td><CopyableCode code="table_name" /></td>
    <td><code>string</code></td>
    <td>The table name.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

Retrieve the maintenance configuration for a specific table, including compaction settings.

```sql
SELECT
maintenance_config
FROM cloudflare.r2_data_catalog.tables_maintenance_configs
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND namespace = '{{ namespace }}' -- required
AND table_name = '{{ table_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="update_by_account">

Update the maintenance configuration for a specific table. This allows you to enable or disable compaction and adjust target file sizes for optimization.

```sql
INSERT INTO cloudflare.r2_data_catalog.tables_maintenance_configs (
compaction,
snapshot_expiration,
account_id,
bucket_name,
namespace,
table_name
)
SELECT 
'{{ compaction }}',
'{{ snapshot_expiration }}',
'{{ account_id }}',
'{{ bucket_name }}',
'{{ namespace }}',
'{{ table_name }}'
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
- name: tables_maintenance_configs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the tables_maintenance_configs resource.
    - name: bucket_name
      value: "{{ bucket_name }}"
      description: Required parameter for the tables_maintenance_configs resource.
    - name: namespace
      value: "{{ namespace }}"
      description: Required parameter for the tables_maintenance_configs resource.
    - name: table_name
      value: "{{ table_name }}"
      description: Required parameter for the tables_maintenance_configs resource.
    - name: compaction
      description: |
        Updates compaction configuration (all fields optional).
      value:
        state: "{{ state }}"
        target_size_mb: "{{ target_size_mb }}"
    - name: snapshot_expiration
      description: |
        Updates snapshot expiration configuration (all fields optional).
      value:
        max_snapshot_age: "{{ max_snapshot_age }}"
        min_snapshots_to_keep: {{ min_snapshots_to_keep }}
        state: "{{ state }}"
`}</CodeBlock>

</TabItem>
</Tabs>
