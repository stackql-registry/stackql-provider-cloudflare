--- 
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - workers
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

Creates, updates, deletes, gets or lists a <code>tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tokens" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.tokens" /></td></tr>
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

Build tokens retrieved successfully

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
    <td><CopyableCode code="cloudflare_token_id" /></td>
    <td><code>string</code></td>
    <td> (example: cf-token-123)</td>
</tr>
<tr>
    <td><CopyableCode code="build_token_name" /></td>
    <td><code>string</code></td>
    <td> (example: My Build Token)</td>
</tr>
<tr>
    <td><CopyableCode code="build_token_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Build token UUID.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_type" /></td>
    <td><code>string</code></td>
    <td> (example: user)</td>
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
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Get all build tokens with pagination</td>
</tr>
<tr>
    <td><a href="#create_build_token"><CopyableCode code="create_build_token" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-build_token_name"><code>build_token_name</code></a>, <a href="#parameter-build_token_secret"><code>build_token_secret</code></a>, <a href="#parameter-cloudflare_token_id"><code>cloudflare_token_id</code></a></td>
    <td></td>
    <td>Create a new build authentication token</td>
</tr>
<tr>
    <td><a href="#delete_build_token"><CopyableCode code="delete_build_token" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-build_token_uuid"><code>build_token_uuid</code></a></td>
    <td></td>
    <td>Remove a build authentication token</td>
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
<tr id="parameter-build_token_uuid">
    <td><CopyableCode code="build_token_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number for pagination</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of items per page</td>
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

Get all build tokens with pagination

```sql
SELECT
cloudflare_token_id,
build_token_name,
build_token_uuid,
owner_type
FROM cloudflare.workers.tokens
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_build_token"
    values={[
        { label: 'create_build_token', value: 'create_build_token' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_build_token">

Create a new build authentication token

```sql
INSERT INTO cloudflare.workers.tokens (
build_token_name,
build_token_secret,
cloudflare_token_id,
account_id
)
SELECT 
'{{ build_token_name }}' /* required */,
'{{ build_token_secret }}' /* required */,
'{{ cloudflare_token_id }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tokens
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the tokens resource.
    - name: build_token_name
      value: "{{ build_token_name }}"
    - name: build_token_secret
      value: "{{ build_token_secret }}"
    - name: cloudflare_token_id
      value: "{{ cloudflare_token_id }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_build_token"
    values={[
        { label: 'delete_build_token', value: 'delete_build_token' }
    ]}
>
<TabItem value="delete_build_token">

Remove a build authentication token

```sql
DELETE FROM cloudflare.workers.tokens
WHERE account_id = '{{ account_id }}' --required
AND build_token_uuid = '{{ build_token_uuid }}' --required
;
```
</TabItem>
</Tabs>
