--- 
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tags" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers_for_platforms.tags" /></td></tr>
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

Fetch script tags.

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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Whether the API call was successful. (true)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Fetch tags from a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#namespace_worker_put_script_tag"><CopyableCode code="namespace_worker_put_script_tag" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-tag"><code>tag</code></a></td>
    <td></td>
    <td>Put a single tag on a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#namespace_worker_put_script_tags"><CopyableCode code="namespace_worker_put_script_tags" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Put script tags for a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-tag"><code>tag</code></a></td>
    <td></td>
    <td>Delete script tag for a script uploaded to a Workers for Platforms namespace.</td>
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
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
</tr>
<tr id="parameter-tag">
    <td><CopyableCode code="tag" /></td>
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

Fetch tags from a script uploaded to a Workers for Platforms namespace.

```sql
SELECT
errors,
messages,
result,
success
FROM cloudflare.workers_for_platforms.tags
WHERE account_id = '{{ account_id }}' -- required
AND dispatch_namespace = '{{ dispatch_namespace }}' -- required
AND script_name = '{{ script_name }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="namespace_worker_put_script_tag"
    values={[
        { label: 'namespace_worker_put_script_tag', value: 'namespace_worker_put_script_tag' },
        { label: 'namespace_worker_put_script_tags', value: 'namespace_worker_put_script_tags' }
    ]}
>
<TabItem value="namespace_worker_put_script_tag">

Put a single tag on a script uploaded to a Workers for Platforms namespace.

```sql
REPLACE cloudflare.workers_for_platforms.tags
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND tag = '{{ tag }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="namespace_worker_put_script_tags">

Put script tags for a script uploaded to a Workers for Platforms namespace.

```sql
REPLACE cloudflare.workers_for_platforms.tags
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
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

Delete script tag for a script uploaded to a Workers for Platforms namespace.

```sql
DELETE FROM cloudflare.workers_for_platforms.tags
WHERE account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND tag = '{{ tag }}' --required
;
```
</TabItem>
</Tabs>
