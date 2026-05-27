--- 
title: snippets
hide_title: false
hide_table_of_contents: false
keywords:
  - snippets
  - snippets
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

Creates, updates, deletes, gets or lists a <code>snippets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snippets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.snippets.snippets" /></td></tr>
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

Return a snippet response.

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
    <td><CopyableCode code="snippet_name" /></td>
    <td><code>string</code></td>
    <td>Identify the snippet. (example: my_snippet, title: Snippet Name)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates when the snippet was created. (example: 2000-01-01T00:00:00.000000Z, title: Created On)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates when the snippet was last modified. (example: 2000-01-01T00:00:00.000000Z, title: Modified On)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

A snippets response.

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
    <td><CopyableCode code="snippet_name" /></td>
    <td><code>string</code></td>
    <td>Identify the snippet. (example: my_snippet, title: Snippet Name)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates when the snippet was created. (example: 2000-01-01T00:00:00.000000Z, title: Created On)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates when the snippet was last modified. (example: 2000-01-01T00:00:00.000000Z, title: Modified On)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-snippet_name"><code>snippet_name</code></a></td>
    <td></td>
    <td>Fetches a snippet belonging to the zone.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetches all snippets belonging to the zone.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-snippet_name"><code>snippet_name</code></a>, <a href="#parameter-metadata"><code>metadata</code></a>, <a href="#parameter-files"><code>files</code></a></td>
    <td></td>
    <td>Creates or updates a snippet belonging to the zone.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-snippet_name"><code>snippet_name</code></a></td>
    <td></td>
    <td>Deletes a snippet belonging to the zone.</td>
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
<tr id="parameter-snippet_name">
    <td><CopyableCode code="snippet_name" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare Snippet name.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
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

Fetches a snippet belonging to the zone.

```sql
SELECT
snippet_name,
created_on,
modified_on
FROM cloudflare.snippets.snippets
WHERE zone_id = '{{ zone_id }}' -- required
AND snippet_name = '{{ snippet_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches all snippets belonging to the zone.

```sql
SELECT
snippet_name,
created_on,
modified_on
FROM cloudflare.snippets.snippets
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Creates or updates a snippet belonging to the zone.

```sql
REPLACE cloudflare.snippets.snippets
SET 
metadata = '{{ metadata }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND snippet_name = '{{ snippet_name }}' --required
AND metadata = '{{ metadata }}' --required
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

Deletes a snippet belonging to the zone.

```sql
DELETE FROM cloudflare.snippets.snippets
WHERE zone_id = '{{ zone_id }}' --required
AND snippet_name = '{{ snippet_name }}' --required
;
```
</TabItem>
</Tabs>
