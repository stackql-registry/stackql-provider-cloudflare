--- 
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
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

Creates, updates, deletes, gets or lists a <code>templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.templates" /></td></tr>
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

Template retrieved successfully

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td> (system, user)</td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Templates listed successfully

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td> (system, user)</td>
</tr>
<tr>
    <td><CopyableCode code="updatedAt" /></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-template_id"><code>template_id</code></a></td>
    <td></td>
    <td>Get a specific takedown letter template by ID</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all available takedown letter templates (system templates and user-defined templates)</td>
</tr>
<tr>
    <td><a href="#post_letter_template_create"><CopyableCode code="post_letter_template_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-category"><code>category</code></a>, <a href="#parameter-body"><code>body</code></a></td>
    <td></td>
    <td>Create a new user-defined takedown letter template</td>
</tr>
<tr>
    <td><a href="#put_letter_template_update"><CopyableCode code="put_letter_template_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-template_id"><code>template_id</code></a></td>
    <td></td>
    <td>Update a user-defined takedown letter template. System templates cannot be modified.</td>
</tr>
<tr>
    <td><a href="#delete_letter_template_delete"><CopyableCode code="delete_letter_template_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-template_id"><code>template_id</code></a></td>
    <td></td>
    <td>Delete a user-defined takedown letter template. System templates cannot be deleted.</td>
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
<tr id="parameter-template_id">
    <td><CopyableCode code="template_id" /></td>
    <td><code>string</code></td>
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

Get a specific takedown letter template by ID

```sql
SELECT
id,
name,
body,
category,
createdAt,
description,
source,
updatedAt
FROM cloudflare.cloudforce_one.templates
WHERE account_id = '{{ account_id }}' -- required
AND template_id = '{{ template_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all available takedown letter templates (system templates and user-defined templates)

```sql
SELECT
id,
name,
category,
createdAt,
description,
source,
updatedAt
FROM cloudflare.cloudforce_one.templates
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_letter_template_create"
    values={[
        { label: 'post_letter_template_create', value: 'post_letter_template_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_letter_template_create">

Create a new user-defined takedown letter template

```sql
INSERT INTO cloudflare.cloudforce_one.templates (
body,
category,
description,
name,
account_id
)
SELECT 
'{{ body }}' /* required */,
'{{ category }}' /* required */,
'{{ description }}',
'{{ name }}' /* required */,
'{{ account_id }}'
RETURNING
id,
name,
body,
category,
createdAt,
description,
source,
updatedAt
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: templates
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the templates resource.
    - name: body
      value: "{{ body }}"
    - name: category
      value: "{{ category }}"
    - name: description
      value: "{{ description }}"
    - name: name
      value: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_letter_template_update"
    values={[
        { label: 'put_letter_template_update', value: 'put_letter_template_update' }
    ]}
>
<TabItem value="put_letter_template_update">

Update a user-defined takedown letter template. System templates cannot be modified.

```sql
REPLACE cloudflare.cloudforce_one.templates
SET 
body = '{{ body }}',
category = '{{ category }}',
description = '{{ description }}',
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND template_id = '{{ template_id }}' --required
RETURNING
id,
name,
body,
category,
createdAt,
description,
source,
updatedAt;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_letter_template_delete"
    values={[
        { label: 'delete_letter_template_delete', value: 'delete_letter_template_delete' }
    ]}
>
<TabItem value="delete_letter_template_delete">

Delete a user-defined takedown letter template. System templates cannot be deleted.

```sql
DELETE FROM cloudflare.cloudforce_one.templates
WHERE account_id = '{{ account_id }}' --required
AND template_id = '{{ template_id }}' --required
;
```
</TabItem>
</Tabs>
