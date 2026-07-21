--- 
title: namespace_instance_chat_completions
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace_instance_chat_completions
  - ai_search
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

Creates, updates, deletes, gets or lists a <code>namespace_instance_chat_completions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespace_instance_chat_completions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai_search.namespace_instance_chat_completions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="chat_completions_by_account"
    values={[
        { label: 'chat_completions_by_account', value: 'chat_completions_by_account' }
    ]}
>
<TabItem value="chat_completions_by_account">

Returns the chat completions results with retrieved files.

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
    <td><CopyableCode code="choices" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="chunks" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
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
    <td><a href="#chat_completions_by_account"><CopyableCode code="chat_completions_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Performs a chat completion request against an AI Search instance, using indexed content as context for generating responses.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="chat_completions_by_account"
    values={[
        { label: 'chat_completions_by_account', value: 'chat_completions_by_account' }
    ]}
>
<TabItem value="chat_completions_by_account">

Performs a chat completion request against an AI Search instance, using indexed content as context for generating responses.

```sql
SELECT
id,
choices,
chunks,
model,
object
FROM cloudflare.ai_search.namespace_instance_chat_completions
WHERE id = '{{ id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND name = '{{ name }}' -- required
;
```
</TabItem>
</Tabs>
