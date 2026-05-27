--- 
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
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

Creates, updates, deletes, gets or lists an <code>entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.entries" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-entry_id"><code>entry_id</code></a></td>
    <td></td>
    <td>This is used for multi-column EDMv2 datasets. The EDMv2 format can only be created in the Cloudflare dashboard.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-entry_id"><code>entry_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates a DLP entry.</td>
</tr>
<tr>
    <td><a href="#update_custom"><CopyableCode code="update_custom" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-entry_id"><code>entry_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-pattern"><code>pattern</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Updates a DLP custom entry.</td>
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
<tr id="parameter-dataset_id">
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>The dataset ID.</td>
</tr>
<tr id="parameter-entry_id">
    <td><CopyableCode code="entry_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

This is used for multi-column EDMv2 datasets. The EDMv2 format can only be created in the Cloudflare dashboard.

```sql
INSERT INTO cloudflare.zero_trust.entries (
account_id,
dataset_id,
version,
entry_id
)
SELECT 
'{{ account_id }}',
'{{ dataset_id }}',
'{{ version }}',
'{{ entry_id }}'
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
- name: entries
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the entries resource.
    - name: dataset_id
      value: "{{ dataset_id }}"
      description: Required parameter for the entries resource.
    - name: version
      value: "{{ version }}"
      description: Required parameter for the entries resource.
    - name: entry_id
      value: "{{ entry_id }}"
      description: Required parameter for the entries resource.
`}</CodeBlock>

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

Updates a DLP entry.

```sql
REPLACE cloudflare.zero_trust.entries
SET 
enabled = {{ enabled }},
description = '{{ description }}',
name = '{{ name }}',
pattern = '{{ pattern }}',
type = '{{ type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND entry_id = '{{ entry_id }}' --required
AND type = '{{ type }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_custom"
    values={[
        { label: 'update_custom', value: 'update_custom' }
    ]}
>
<TabItem value="update_custom">

Updates a DLP custom entry.

```sql
EXEC cloudflare.zero_trust.entries.update_custom 
@account_id='{{ account_id }}' --required, 
@entry_id='{{ entry_id }}' --required 
@@json=
'{
"description": "{{ description }}", 
"name": "{{ name }}", 
"pattern": "{{ pattern }}", 
"enabled": {{ enabled }}
}'
;
```
</TabItem>
</Tabs>
