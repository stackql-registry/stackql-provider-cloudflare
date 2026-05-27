--- 
title: brand_protection_logos
hide_title: false
hide_table_of_contents: false
keywords:
  - brand_protection_logos
  - brand_protection
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

Creates, updates, deletes, gets or lists a <code>brand_protection_logos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="brand_protection_logos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.brand_protection.brand_protection_logos" /></td></tr>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-tag"><code>tag</code></a>, <a href="#parameter-match_type"><code>match_type</code></a>, <a href="#parameter-threshold"><code>threshold</code></a></td>
    <td>Return new saved logo queries created from image files</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-logo_id"><code>logo_id</code></a></td>
    <td></td>
    <td>Return a success message after deleting saved logo queries by ID</td>
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
<tr id="parameter-logo_id">
    <td><CopyableCode code="logo_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-match_type">
    <td><CopyableCode code="match_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag">
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-threshold">
    <td><CopyableCode code="threshold" /></td>
    <td><code>number</code></td>
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

Return new saved logo queries created from image files

```sql
INSERT INTO cloudflare.brand_protection.brand_protection_logos (
image,
account_id,
tag,
match_type,
threshold
)
SELECT 
'{{ image }}',
'{{ account_id }}',
'{{ tag }}',
'{{ match_type }}',
'{{ threshold }}'
RETURNING
id,
tag,
upload_path
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: brand_protection_logos
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the brand_protection_logos resource.
    - name: image
      value: "{{ image }}"
    - name: tag
      value: "{{ tag }}"
    - name: match_type
      value: "{{ match_type }}"
    - name: threshold
      value: {{ threshold }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' }
    ]}
>
<TabItem value="delete_by_account">

Return a success message after deleting saved logo queries by ID

```sql
DELETE FROM cloudflare.brand_protection.brand_protection_logos
WHERE account_id = '{{ account_id }}' --required
AND logo_id = '{{ logo_id }}' --required
;
```
</TabItem>
</Tabs>
