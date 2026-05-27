--- 
title: ai_search
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_search
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

Creates, updates, deletes, gets or lists an <code>ai_search</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_search" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.ai_search" /></td></tr>
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
    <td><a href="#autorag_config_ai_search"><CopyableCode code="autorag_config_ai_search" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query"><code>query</code></a></td>
    <td></td>
    <td></td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="autorag_config_ai_search"
    values={[
        { label: 'autorag_config_ai_search', value: 'autorag_config_ai_search' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="autorag_config_ai_search">

No description available.

```sql
INSERT INTO cloudflare.ai.ai_search (
filters,
max_num_results,
model,
query,
ranking_options,
reranking,
rewrite_query,
stream,
system_prompt,
id,
account_id
)
SELECT 
'{{ filters }}',
{{ max_num_results }},
'{{ model }}',
'{{ query }}' /* required */,
'{{ ranking_options }}',
'{{ reranking }}',
{{ rewrite_query }},
{{ stream }},
'{{ system_prompt }}',
'{{ id }}',
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_search
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the ai_search resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the ai_search resource.
    - name: filters
      value:
        key: "{{ key }}"
        type: "{{ type }}"
        value: "{{ value }}"
        filters:
          - key: "{{ key }}"
            type: "{{ type }}"
            value: "{{ value }}"
    - name: max_num_results
      value: {{ max_num_results }}
      default: 10
    - name: model
      value: "{{ model }}"
      valid_values: ['@cf/meta/llama-3.3-70b-instruct-fp8-fast', '@cf/meta/llama-3.1-8b-instruct-fast', '@cf/meta/llama-3.1-8b-instruct-fp8', '@cf/meta/llama-4-scout-17b-16e-instruct', '@cf/qwen/qwen3-30b-a3b-fp8', '@cf/deepseek-ai/deepseek-r1-distill-qwen-32b', '@cf/moonshotai/kimi-k2-instruct', 'anthropic/claude-3-7-sonnet', 'anthropic/claude-sonnet-4', 'anthropic/claude-opus-4', 'anthropic/claude-3-5-haiku', 'cerebras/qwen-3-235b-a22b-instruct', 'cerebras/qwen-3-235b-a22b-thinking', 'cerebras/llama-3.3-70b', 'cerebras/llama-4-maverick-17b-128e-instruct', 'cerebras/llama-4-scout-17b-16e-instruct', 'cerebras/gpt-oss-120b', 'google-ai-studio/gemini-2.5-flash', 'google-ai-studio/gemini-2.5-pro', 'grok/grok-4', 'groq/llama-3.3-70b-versatile', 'groq/llama-3.1-8b-instant', 'openai/gpt-5', 'openai/gpt-5-mini', 'openai/gpt-5-nano']
    - name: query
      value: "{{ query }}"
    - name: ranking_options
      value:
        ranker: "{{ ranker }}"
        score_threshold: {{ score_threshold }}
      default: [object Object]
    - name: reranking
      value:
        enabled: {{ enabled }}
        model: "{{ model }}"
    - name: rewrite_query
      value: {{ rewrite_query }}
      default: false
    - name: stream
      value: {{ stream }}
      default: false
    - name: system_prompt
      value: "{{ system_prompt }}"
`}</CodeBlock>

</TabItem>
</Tabs>
