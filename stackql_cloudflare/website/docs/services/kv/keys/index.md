--- 
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - kv
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.kv.keys" /></td></tr>
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

List a Namespace's Keys response.

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
    <td>A key's name. The name may be at most 512 bytes. All printable, non-whitespace characters are valid. Use percent-encoding to define key names as part of a URL. (example: My-Key)</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>number</code></td>
    <td>The time, measured in number of seconds since the UNIX epoch, at which the key will expire. This property is omitted for keys that will not expire.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code></code></td>
    <td>Arbitrary JSON that is associated with a key.</td>
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
    <td><a href="#parameter-namespace_id"><code>namespace_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-cursor"><code>cursor</code></a></td>
    <td>Lists a namespace's keys.</td>
</tr>
<tr>
    <td><a href="#bulk_update"><CopyableCode code="bulk_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-namespace_id"><code>namespace_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Write multiple keys and values at once. Body should be an array of up to 10,000 key-value pairs to be stored, along with optional expiration information. Existing values and expirations will be overwritten. If neither `expiration` nor `expiration_ttl` is specified, the key-value pair will never expire. If both are set, `expiration_ttl` is used and `expiration` is ignored. The entire request size must be 100 megabytes or less.</td>
</tr>
<tr>
    <td><a href="#bulk"><CopyableCode code="bulk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-namespace_id"><code>namespace_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Remove multiple KV pairs from the namespace. Body should be an array of up to 10,000 keys to be removed.</td>
</tr>
<tr>
    <td><a href="#create_delete"><CopyableCode code="create_delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-namespace_id"><code>namespace_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Remove multiple KV pairs from the namespace. Body should be an array of up to 10,000 keys to be removed.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-namespace_id"><code>namespace_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-keys"><code>keys</code></a></td>
    <td></td>
    <td>Retrieve up to 100 KV pairs from the namespace. Keys must contain text-based values. JSON values can optionally be parsed instead of being returned as a string value. Metadata can be included if `withMetadata` is true.</td>
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
<tr id="parameter-namespace_id">
    <td><CopyableCode code="namespace_id" /></td>
    <td><code>string</code></td>
    <td>The Workers KV namespace ID.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-prefix">
    <td><CopyableCode code="prefix" /></td>
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

Lists a namespace's keys.

```sql
SELECT
name,
expiration,
metadata
FROM cloudflare.kv.keys
WHERE namespace_id = '{{ namespace_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND limit = '{{ limit }}'
AND prefix = '{{ prefix }}'
AND cursor = '{{ cursor }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="bulk_update"
    values={[
        { label: 'bulk_update', value: 'bulk_update' }
    ]}
>
<TabItem value="bulk_update">

Write multiple keys and values at once. Body should be an array of up to 10,000 key-value pairs to be stored, along with optional expiration information. Existing values and expirations will be overwritten. If neither `expiration` nor `expiration_ttl` is specified, the key-value pair will never expire. If both are set, `expiration_ttl` is used and `expiration` is ignored. The entire request size must be 100 megabytes or less.

```sql
REPLACE cloudflare.kv.keys
SET 
-- No updatable properties
WHERE 
namespace_id = '{{ namespace_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="bulk"
    values={[
        { label: 'bulk', value: 'bulk' },
        { label: 'create_delete', value: 'create_delete' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="bulk">

Remove multiple KV pairs from the namespace. Body should be an array of up to 10,000 keys to be removed.

```sql
EXEC cloudflare.kv.keys.bulk 
@namespace_id='{{ namespace_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="create_delete">

Remove multiple KV pairs from the namespace. Body should be an array of up to 10,000 keys to be removed.

```sql
EXEC cloudflare.kv.keys.create_delete 
@namespace_id='{{ namespace_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="get">

Retrieve up to 100 KV pairs from the namespace. Keys must contain text-based values. JSON values can optionally be parsed instead of being returned as a string value. Metadata can be included if `withMetadata` is true.

```sql
EXEC cloudflare.kv.keys.get 
@namespace_id='{{ namespace_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"keys": "{{ keys }}", 
"type": "{{ type }}", 
"withMetadata": {{ withMetadata }}
}'
;
```
</TabItem>
</Tabs>
