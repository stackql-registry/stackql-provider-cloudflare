--- 
title: items
hide_title: false
hide_table_of_contents: false
keywords:
  - items
  - aisearch
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

Creates, updates, deletes, gets or lists an <code>items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.aisearch.items" /></td></tr>
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

Returns a AI Search Item detail.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source_id" /></td>
    <td><code>string</code></td>
    <td>Identifies which data source this item belongs to. "builtin" for uploaded files, "&#123;type&#125;:&#123;source&#125;" for external sources, null for legacy items.</td>
</tr>
<tr>
    <td><CopyableCode code="checksum" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="chunks_count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="file_size" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="next_action" /></td>
    <td><code>string</code></td>
    <td> (INDEX, DELETE, )</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (queued, running, completed, error, skipped, outdated)</td>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Retrieves a specific indexed item from an AI Search instance.</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>Uploads a file to a managed AI Search instance via multipart/form-data (max 4MB).</td>
</tr>
<tr>
    <td><a href="#sync"><CopyableCode code="sync" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-next_action"><code>next_action</code></a></td>
    <td></td>
    <td>Syncs an item to an AI Search instance index.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-next_action"><code>next_action</code></a></td>
    <td></td>
    <td>Creates or updates an indexed item in an AI Search instance.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Deletes a file from a managed AI Search instance and triggers a reindex.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr id="parameter-item_id">
    <td><CopyableCode code="item_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
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

Retrieves a specific indexed item from an AI Search instance.

```sql
SELECT
id,
source_id,
checksum,
chunks_count,
created_at,
error,
file_size,
key,
last_seen_at,
namespace,
next_action,
status
FROM cloudflare.aisearch.items
WHERE id = '{{ id }}' -- required
AND item_id = '{{ item_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND name = '{{ name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="upload"
    values={[
        { label: 'upload', value: 'upload' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="upload">

Uploads a file to a managed AI Search instance via multipart/form-data (max 4MB).

```sql
INSERT INTO cloudflare.aisearch.items (
file,
metadata,
wait_for_completion,
id,
account_id,
name
)
SELECT 
'{{ file }}' /* required */,
'{{ metadata }}',
{{ wait_for_completion }},
'{{ id }}',
'{{ account_id }}',
'{{ name }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: items
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the items resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the items resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the items resource.
    - name: file
      value: "{{ file }}"
      description: |
        The file to upload (max 4MB). Filename must not exceed 128 characters.
    - name: metadata
      value: "{{ metadata }}"
      description: |
        JSON string of custom metadata key-value pairs.
    - name: wait_for_completion
      value: {{ wait_for_completion }}
      description: |
        Wait for indexing to fully complete before responding. On RAGs with vector indexing enabled, this additionally waits for Vectorize ingestion confirmation (up to 40s) so the returned item reflects a queryable state. On timeout the item is returned in \`running\` state and the background alarm continues polling. Defaults to false.
      default: false
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="sync"
    values={[
        { label: 'sync', value: 'sync' }
    ]}
>
<TabItem value="sync">

Syncs an item to an AI Search instance index.

```sql
UPDATE cloudflare.aisearch.items
SET 
next_action = '{{ next_action }}',
wait_for_completion = {{ wait_for_completion }}
WHERE 
id = '{{ id }}' --required
AND item_id = '{{ item_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND next_action = '{{ next_action }}' --required
RETURNING
result,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates an indexed item in an AI Search instance.

```sql
REPLACE cloudflare.aisearch.items
SET 
key = '{{ key }}',
next_action = '{{ next_action }}',
wait_for_completion = {{ wait_for_completion }}
WHERE 
id = '{{ id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND key = '{{ key }}' --required
AND next_action = '{{ next_action }}' --required
RETURNING
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

Deletes a file from a managed AI Search instance and triggers a reindex.

```sql
DELETE FROM cloudflare.aisearch.items
WHERE id = '{{ id }}' --required
AND item_id = '{{ item_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
;
```
</TabItem>
</Tabs>
