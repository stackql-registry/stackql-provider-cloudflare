--- 
title: llama_guard_3_8b
hide_title: false
hide_table_of_contents: false
keywords:
  - llama_guard_3_8b
  - ai
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

Creates, updates, deletes, gets or lists a <code>llama_guard_3_8b</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="llama_guard_3_8b" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.llama_guard_3_8b" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_meta_llama_guard_3_8b"><CopyableCode code="workers_ai_post_run_cf_meta_llama_guard_3_8b" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-messages"><code>messages</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/meta/llama-guard-3-8b model.</td>
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
<tr id="parameter-queueRequest">
    <td><CopyableCode code="queueRequest" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="workers_ai_post_run_cf_meta_llama_guard_3_8b"
    values={[
        { label: 'workers_ai_post_run_cf_meta_llama_guard_3_8b', value: 'workers_ai_post_run_cf_meta_llama_guard_3_8b' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_meta_llama_guard_3_8b">

Runs inference on the @cf/meta/llama-guard-3-8b model.

```sql
INSERT INTO cloudflare.ai.llama_guard_3_8b (
max_tokens,
messages,
response_format,
temperature,
account_id,
queueRequest,
tags
)
SELECT 
{{ max_tokens }},
'{{ messages }}' /* required */,
'{{ response_format }}',
{{ temperature }},
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: llama_guard_3_8b
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the llama_guard_3_8b resource.
    - name: max_tokens
      value: {{ max_tokens }}
      description: |
        The maximum number of tokens to generate in the response.
      default: 256
    - name: messages
      description: |
        An array of message objects representing the conversation history.
      value:
        - content: "{{ content }}"
          role: "{{ role }}"
    - name: response_format
      description: |
        Dictate the output format of the generated response.
      value:
        type: "{{ type }}"
    - name: temperature
      value: {{ temperature }}
      description: |
        Controls the randomness of the output; higher values produce more random results.
      default: 0.6
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
