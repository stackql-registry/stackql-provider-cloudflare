--- 
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - workers_for_platforms
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers_for_platforms.namespaces" /></td></tr>
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

Get a Workers for Platforms namespace.

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
    <td><CopyableCode code="namespace_id" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Workers for Platforms dispatch namespace. (example: my-dispatch-namespace)</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was created. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_by" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was last modified. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="script_count" /></td>
    <td><code>integer</code></td>
    <td>The current number of scripts in this Dispatch Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="trusted_workers" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Workers in the namespace are executed in a "trusted" manner. When a Worker is trusted, it has access to the shared caches for the zone in the Cache API, and has access to the `request.cf` object on incoming Requests. When a Worker is untrusted, caches are not shared across the zone, and `request.cf` is undefined. By default, Workers in a namespace are "untrusted".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Fetch a list of Workers for Platforms namespaces.

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
    <td><CopyableCode code="namespace_id" /></td>
    <td><code>string</code></td>
    <td>API Resource UUID tag. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Workers for Platforms dispatch namespace. (example: my-dispatch-namespace)</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was created. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_by" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was last modified. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="script_count" /></td>
    <td><code>integer</code></td>
    <td>The current number of scripts in this Dispatch Namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="trusted_workers" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Workers in the namespace are executed in a "trusted" manner. When a Worker is trusted, it has access to the shared caches for the zone in the Cache API, and has access to the `request.cf` object on incoming Requests. When a Worker is untrusted, caches are not shared across the zone, and `request.cf` is undefined. By default, Workers in a namespace are "untrusted".</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a></td>
    <td></td>
    <td>Get a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch a list of Workers for Platforms namespaces.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create a new Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#namespace_worker_patch_namespace"><CopyableCode code="namespace_worker_patch_namespace" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a></td>
    <td></td>
    <td>Patch a Workers for Platforms namespace. Omitted fields are left unchanged.</td>
</tr>
<tr>
    <td><a href="#namespace_worker_put_namespace"><CopyableCode code="namespace_worker_put_namespace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a></td>
    <td></td>
    <td>Update a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a></td>
    <td></td>
    <td>Delete a Workers for Platforms namespace.</td>
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
<tr id="parameter-dispatch_namespace">
    <td><CopyableCode code="dispatch_namespace" /></td>
    <td><code>string</code></td>
    <td>The Workers-for-Platforms dispatch namespace.</td>
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

Get a Workers for Platforms namespace.

```sql
SELECT
namespace_id,
namespace_name,
created_by,
created_on,
modified_by,
modified_on,
script_count,
trusted_workers
FROM cloudflare.workers_for_platforms.namespaces
WHERE account_id = '{{ account_id }}' -- required
AND dispatch_namespace = '{{ dispatch_namespace }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetch a list of Workers for Platforms namespaces.

```sql
SELECT
namespace_id,
namespace_name,
created_by,
created_on,
modified_by,
modified_on,
script_count,
trusted_workers
FROM cloudflare.workers_for_platforms.namespaces
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

Create a new Workers for Platforms namespace.

```sql
INSERT INTO cloudflare.workers_for_platforms.namespaces (
name,
account_id
)
SELECT 
'{{ name }}',
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
- name: namespaces
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the namespaces resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the dispatch namespace.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="namespace_worker_patch_namespace"
    values={[
        { label: 'namespace_worker_patch_namespace', value: 'namespace_worker_patch_namespace' }
    ]}
>
<TabItem value="namespace_worker_patch_namespace">

Patch a Workers for Platforms namespace. Omitted fields are left unchanged.

```sql
UPDATE cloudflare.workers_for_platforms.namespaces
SET 
name = '{{ name }}',
trusted_workers = {{ trusted_workers }}
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
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
    defaultValue="namespace_worker_put_namespace"
    values={[
        { label: 'namespace_worker_put_namespace', value: 'namespace_worker_put_namespace' }
    ]}
>
<TabItem value="namespace_worker_put_namespace">

Update a Workers for Platforms namespace.

```sql
REPLACE cloudflare.workers_for_platforms.namespaces
SET 
name = '{{ name }}',
trusted_workers = {{ trusted_workers }}
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
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

Delete a Workers for Platforms namespace.

```sql
DELETE FROM cloudflare.workers_for_platforms.namespaces
WHERE account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
;
```
</TabItem>
</Tabs>
