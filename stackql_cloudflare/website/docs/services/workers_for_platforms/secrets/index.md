--- 
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="secrets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers_for_platforms.secrets" /></td></tr>
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

Get script secret (Workers for Platforms).

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
    <td>A JavaScript variable name for the binding. (example: myBinding)</td>
</tr>
<tr>
    <td><CopyableCode code="algorithm" /></td>
    <td><code>object</code></td>
    <td>Algorithm-specific key parameters. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Data format of the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format). (raw, pkcs8, spki, jwk) (example: raw)</td>
</tr>
<tr>
    <td><CopyableCode code="key_base64" /></td>
    <td><code>string</code></td>
    <td>Base64-encoded key data. Required if `format` is "raw", "pkcs8", or "spki".</td>
</tr>
<tr>
    <td><CopyableCode code="key_jwk" /></td>
    <td><code>object</code></td>
    <td>Key data in [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key) format. Required if `format` is "jwk".</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>The secret value to use. (example: My secret.)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The kind of resource that the binding provides. (secret_text)</td>
</tr>
<tr>
    <td><CopyableCode code="usages" /></td>
    <td><code>array</code></td>
    <td>Allowed operations with the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages). (x-stainless-collection-type: set)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List script secrets.

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
    <td>A JavaScript variable name for the binding. (example: myBinding)</td>
</tr>
<tr>
    <td><CopyableCode code="algorithm" /></td>
    <td><code>object</code></td>
    <td>Algorithm-specific key parameters. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Data format of the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format). (raw, pkcs8, spki, jwk) (example: raw)</td>
</tr>
<tr>
    <td><CopyableCode code="key_base64" /></td>
    <td><code>string</code></td>
    <td>Base64-encoded key data. Required if `format` is "raw", "pkcs8", or "spki".</td>
</tr>
<tr>
    <td><CopyableCode code="key_jwk" /></td>
    <td><code>object</code></td>
    <td>Key data in [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key) format. Required if `format` is "jwk".</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>The secret value to use. (example: My secret.)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The kind of resource that the binding provides. (secret_text)</td>
</tr>
<tr>
    <td><CopyableCode code="usages" /></td>
    <td><code>array</code></td>
    <td>Allowed operations with the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages). (x-stainless-collection-type: set)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-secret_name"><code>secret_name</code></a></td>
    <td><a href="#parameter-url_encoded"><code>url_encoded</code></a></td>
    <td>Get a given secret binding (value omitted) on a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>List secrets bound to a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Add a secret to a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-secret_name"><code>secret_name</code></a></td>
    <td><a href="#parameter-url_encoded"><code>url_encoded</code></a></td>
    <td>Remove a secret from a script uploaded to a Workers for Platforms namespace.</td>
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
<tr id="parameter-secret_name">
    <td><CopyableCode code="secret_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-url_encoded">
    <td><CopyableCode code="url_encoded" /></td>
    <td><code>boolean</code></td>
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

Get a given secret binding (value omitted) on a script uploaded to a Workers for Platforms namespace.

```sql
SELECT
name,
algorithm,
format,
key_base64,
key_jwk,
text,
type,
usages
FROM cloudflare.workers_for_platforms.secrets
WHERE account_id = '{{ account_id }}' -- required
AND dispatch_namespace = '{{ dispatch_namespace }}' -- required
AND script_name = '{{ script_name }}' -- required
AND secret_name = '{{ secret_name }}' -- required
AND url_encoded = '{{ url_encoded }}'
;
```
</TabItem>
<TabItem value="list">

List secrets bound to a script uploaded to a Workers for Platforms namespace.

```sql
SELECT
name,
algorithm,
format,
key_base64,
key_jwk,
text,
type,
usages
FROM cloudflare.workers_for_platforms.secrets
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

Add a secret to a script uploaded to a Workers for Platforms namespace.

```sql
REPLACE cloudflare.workers_for_platforms.secrets
SET 
name = '{{ name }}',
text = '{{ text }}',
type = '{{ type }}',
algorithm = '{{ algorithm }}',
format = '{{ format }}',
key_base64 = '{{ key_base64 }}',
key_jwk = '{{ key_jwk }}',
usages = '{{ usages }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND name = '{{ name }}' --required
AND type = '{{ type }}' --required
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

Remove a secret from a script uploaded to a Workers for Platforms namespace.

```sql
DELETE FROM cloudflare.workers_for_platforms.secrets
WHERE account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND secret_name = '{{ secret_name }}' --required
AND url_encoded = '{{ url_encoded }}'
;
```
</TabItem>
</Tabs>
