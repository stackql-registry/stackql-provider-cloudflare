--- 
title: categories
hide_title: false
hide_table_of_contents: false
keywords:
  - categories
  - cloudforce_one
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

Creates, updates, deletes, gets or lists a <code>categories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="categories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.categories" /></td></tr>
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

Returns a category.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="killChain" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mitreAttack" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mitreCapec" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="shortname" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-category_id"><code>category_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#post_category_update"><CopyableCode code="post_category_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-category_id"><code>category_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-category_id"><code>category_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#patch_tag_category_update"><CopyableCode code="patch_tag_category_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-category_uuid"><code>category_uuid</code></a></td>
    <td></td>
    <td>Updates a Source-of-Truth tag category by UUID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-category_id"><code>category_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_tag_category_delete"><CopyableCode code="delete_tag_category_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-category_uuid"><code>category_uuid</code></a></td>
    <td></td>
    <td>Deletes a Source-of-Truth tag category by UUID.</td>
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
<tr id="parameter-category_id">
    <td><CopyableCode code="category_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Category UUID.</td>
</tr>
<tr id="parameter-category_uuid">
    <td><CopyableCode code="category_uuid" /></td>
    <td><code>string</code></td>
    <td>Tag Category UUID.</td>
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

Returns a category.

```sql
SELECT
name,
killChain,
mitreAttack,
mitreCapec,
shortname,
uuid
FROM cloudflare.cloudforce_one.categories
WHERE account_id = '{{ account_id }}' -- required
AND category_id = '{{ category_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_category_update"
    values={[
        { label: 'post_category_update', value: 'post_category_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_category_update">

No description available.

```sql
INSERT INTO cloudflare.cloudforce_one.categories (
killChain,
mitreAttack,
mitreCapec,
name,
shortname,
account_id,
category_id
)
SELECT 
{{ killChain }},
'{{ mitreAttack }}',
'{{ mitreCapec }}',
'{{ name }}',
'{{ shortname }}',
'{{ account_id }}',
'{{ category_id }}'
RETURNING
name,
killChain,
mitreAttack,
mitreCapec,
shortname,
uuid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: categories
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the categories resource.
    - name: category_id
      value: "{{ category_id }}"
      description: Required parameter for the categories resource.
    - name: killChain
      value: {{ killChain }}
    - name: mitreAttack
      value:
        - "{{ mitreAttack }}"
    - name: mitreCapec
      value:
        - "{{ mitreCapec }}"
    - name: name
      value: "{{ name }}"
    - name: shortname
      value: "{{ shortname }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'patch_tag_category_update', value: 'patch_tag_category_update' }
    ]}
>
<TabItem value="edit">

No description available.

```sql
UPDATE cloudflare.cloudforce_one.categories
SET 
killChain = {{ killChain }},
mitreAttack = '{{ mitreAttack }}',
mitreCapec = '{{ mitreCapec }}',
name = '{{ name }}',
shortname = '{{ shortname }}'
WHERE 
account_id = '{{ account_id }}' --required
AND category_id = '{{ category_id }}' --required
RETURNING
name,
killChain,
mitreAttack,
mitreCapec,
shortname,
uuid;
```
</TabItem>
<TabItem value="patch_tag_category_update">

Updates a Source-of-Truth tag category by UUID.

```sql
UPDATE cloudflare.cloudforce_one.categories
SET 
description = '{{ description }}',
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND category_uuid = '{{ category_uuid }}' --required
RETURNING
name,
createdAt,
description,
updatedAt,
uuid;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_tag_category_delete', value: 'delete_tag_category_delete' }
    ]}
>
<TabItem value="delete">

No description available.

```sql
DELETE FROM cloudflare.cloudforce_one.categories
WHERE account_id = '{{ account_id }}' --required
AND category_id = '{{ category_id }}' --required
;
```
</TabItem>
<TabItem value="delete_tag_category_delete">

Deletes a Source-of-Truth tag category by UUID.

```sql
DELETE FROM cloudflare.cloudforce_one.categories
WHERE account_id = '{{ account_id }}' --required
AND category_uuid = '{{ category_uuid }}' --required
;
```
</TabItem>
</Tabs>
