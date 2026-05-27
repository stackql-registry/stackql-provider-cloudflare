--- 
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - intel
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

Creates, updates, deletes, gets or lists a <code>permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.intel.permissions" /></td></tr>
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

Get indicator feed metadata

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
    <td><code>integer</code></td>
    <td>The unique identifier for the indicator feed</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the indicator feed</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the example test</td>
</tr>
<tr>
    <td><CopyableCode code="is_attributable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the indicator feed can be attributed to a provider</td>
</tr>
<tr>
    <td><CopyableCode code="is_downloadable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the indicator feed can be downloaded</td>
</tr>
<tr>
    <td><CopyableCode code="is_public" /></td>
    <td><code>boolean</code></td>
    <td>Whether the indicator feed is exposed to customers</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists current access permissions for custom threat indicator feeds.</td>
</tr>
<tr>
    <td><a href="#update_add"><CopyableCode code="update_add" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Grants access permissions for a custom threat indicator feed to other accounts.</td>
</tr>
<tr>
    <td><a href="#update_remove"><CopyableCode code="update_remove" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Revokes access permissions for a custom threat indicator feed.</td>
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

Lists current access permissions for custom threat indicator feeds.

```sql
SELECT
id,
name,
description,
is_attributable,
is_downloadable,
is_public
FROM cloudflare.intel.permissions
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_add"
    values={[
        { label: 'update_add', value: 'update_add' },
        { label: 'update_remove', value: 'update_remove' }
    ]}
>
<TabItem value="update_add">

Grants access permissions for a custom threat indicator feed to other accounts.

```sql
EXEC cloudflare.intel.permissions.update_add 
@account_id='{{ account_id }}' --required 
@@json=
'{
"account_tag": "{{ account_tag }}", 
"feed_id": {{ feed_id }}
}'
;
```
</TabItem>
<TabItem value="update_remove">

Revokes access permissions for a custom threat indicator feed.

```sql
EXEC cloudflare.intel.permissions.update_remove 
@account_id='{{ account_id }}' --required 
@@json=
'{
"account_tag": "{{ account_tag }}", 
"feed_id": {{ feed_id }}
}'
;
```
</TabItem>
</Tabs>
