--- 
title: content
hide_title: false
hide_table_of_contents: false
keywords:
  - content
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

Creates, updates, deletes, gets or lists a <code>content</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="content" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers_for_platforms.content" /></td></tr>
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

Get script content.

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
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td>Fetch script content from a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-metadata"><code>metadata</code></a></td>
    <td><a href="#parameter-CF-WORKER-BODY-PART"><code>CF-WORKER-BODY-PART</code></a>, <a href="#parameter-CF-WORKER-MAIN-MODULE-PART"><code>CF-WORKER-MAIN-MODULE-PART</code></a></td>
    <td>Put script content for a script uploaded to a Workers for Platforms namespace.</td>
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
<tr id="parameter-CF-WORKER-BODY-PART">
    <td><CopyableCode code="CF-WORKER-BODY-PART" /></td>
    <td><code>string</code></td>
    <td>The multipart name of a script upload part containing script content in service worker format. Alternative to including in a metadata part.</td>
</tr>
<tr id="parameter-CF-WORKER-MAIN-MODULE-PART">
    <td><CopyableCode code="CF-WORKER-MAIN-MODULE-PART" /></td>
    <td><code>string</code></td>
    <td>The multipart name of a script upload part containing script content in es module format. Alternative to including in a metadata part.</td>
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

Fetch script content from a script uploaded to a Workers for Platforms namespace.

```sql
SELECT
contents
FROM cloudflare.workers_for_platforms.content
WHERE account_id = '{{ account_id }}' -- required
AND dispatch_namespace = '{{ dispatch_namespace }}' -- required
AND script_name = '{{ script_name }}' -- required
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

Put script content for a script uploaded to a Workers for Platforms namespace.

```sql
REPLACE cloudflare.workers_for_platforms.content
SET 
files = '{{ files }}',
metadata = '{{ metadata }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND metadata = '{{ metadata }}' --required
AND CF-WORKER-BODY-PART = '{{ CF-WORKER-BODY-PART}}'
AND CF-WORKER-MAIN-MODULE-PART = '{{ CF-WORKER-MAIN-MODULE-PART}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
