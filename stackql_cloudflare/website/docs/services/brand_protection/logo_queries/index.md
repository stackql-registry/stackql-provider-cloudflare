--- 
title: logo_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - logo_queries
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

Creates, updates, deletes, gets or lists a <code>logo_queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="logo_queries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.brand_protection.logo_queries" /></td></tr>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tag"><code>tag</code></a>, <a href="#parameter-image_data"><code>image_data</code></a>, <a href="#parameter-similarity_threshold"><code>similarity_threshold</code></a></td>
    <td></td>
    <td>Create a new saved brand protection logo query for visual similarity matching</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Delete a saved brand protection logo query. Returns 404 if the query ID doesn't exist.</td>
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
<tr id="parameter-query_id">
    <td><CopyableCode code="query_id" /></td>
    <td><code>string</code></td>
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

Create a new saved brand protection logo query for visual similarity matching

```sql
INSERT INTO cloudflare.brand_protection.logo_queries (
image_data,
search_lookback,
similarity_threshold,
tag,
account_id
)
SELECT 
'{{ image_data }}' /* required */,
{{ search_lookback }},
{{ similarity_threshold }} /* required */,
'{{ tag }}' /* required */,
'{{ account_id }}'
RETURNING
query_id,
message,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: logo_queries
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the logo_queries resource.
    - name: image_data
      value: "{{ image_data }}"
      description: |
        Base64 encoded image data. Can include data URI prefix (e.g., 'data:image/png;base64,...') or just the base64 string.
    - name: search_lookback
      value: {{ search_lookback }}
      description: |
        If true, search historic scanned images for matches above the similarity threshold
      default: true
    - name: similarity_threshold
      value: {{ similarity_threshold }}
      description: |
        Minimum similarity score (0-1) required for visual matches
    - name: tag
      value: "{{ tag }}"
      description: |
        Unique identifier for the logo query
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

Delete a saved brand protection logo query. Returns 404 if the query ID doesn't exist.

```sql
DELETE FROM cloudflare.brand_protection.logo_queries
WHERE account_id = '{{ account_id }}' --required
AND query_id = '{{ query_id }}' --required
;
```
</TabItem>
</Tabs>
