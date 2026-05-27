--- 
title: chat_completions
hide_title: false
hide_table_of_contents: false
keywords:
  - chat_completions
  - aisearch
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

Creates, updates, deletes, gets or lists a <code>chat_completions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="chat_completions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.aisearch.chat_completions" /></td></tr>
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
    <td><a href="#chat_completions_by_account"><CopyableCode code="chat_completions_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-messages"><code>messages</code></a></td>
    <td></td>
    <td>Performs a chat completion request against an AI Search instance, using indexed content as context for generating responses.</td>
</tr>
<tr>
    <td><a href="#chat_completions"><CopyableCode code="chat_completions" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-messages"><code>messages</code></a>, <a href="#parameter-ai_search_options"><code>ai_search_options</code></a></td>
    <td></td>
    <td>Performs a chat completion request against multiple AI Search instances in parallel, merging retrieved content as context for generating a response.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="chat_completions_by_account"
    values={[
        { label: 'chat_completions_by_account', value: 'chat_completions_by_account' },
        { label: 'chat_completions', value: 'chat_completions' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="chat_completions_by_account">

Performs a chat completion request against an AI Search instance, using indexed content as context for generating responses.

```sql
INSERT INTO cloudflare.aisearch.chat_completions (
ai_search_options,
messages,
model,
stream,
id,
account_id
)
SELECT 
'{{ ai_search_options }}',
'{{ messages }}' /* required */,
'{{ model }}',
{{ stream }},
'{{ id }}',
'{{ account_id }}'
RETURNING
id,
choices,
chunks,
model,
object
;
```
</TabItem>
<TabItem value="chat_completions">

Performs a chat completion request against multiple AI Search instances in parallel, merging retrieved content as context for generating a response.

```sql
INSERT INTO cloudflare.aisearch.chat_completions (
ai_search_options,
messages,
model,
stream,
account_id,
name
)
SELECT 
'{{ ai_search_options }}' /* required */,
'{{ messages }}' /* required */,
'{{ model }}',
{{ stream }},
'{{ account_id }}',
'{{ name }}'
RETURNING
id,
choices,
chunks,
errors,
model,
object
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: chat_completions
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the chat_completions resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the chat_completions resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the chat_completions resource.
    - name: ai_search_options
      value:
        cache:
          cache_threshold: "{{ cache_threshold }}"
          enabled: {{ enabled }}
        instance_ids:
          - "{{ instance_ids }}"
        query_rewrite:
          enabled: {{ enabled }}
          model: "{{ model }}"
          rewrite_prompt: "{{ rewrite_prompt }}"
        reranking:
          enabled: {{ enabled }}
          match_threshold: {{ match_threshold }}
          model: "{{ model }}"
        retrieval:
          boost_by:
            - direction: "{{ direction }}"
              field: "{{ field }}"
          context_expansion: {{ context_expansion }}
          filters: "{{ filters }}"
          fusion_method: "{{ fusion_method }}"
          keyword_match_mode: "{{ keyword_match_mode }}"
          match_threshold: {{ match_threshold }}
          max_num_results: {{ max_num_results }}
          retrieval_type: "{{ retrieval_type }}"
          return_on_failure: {{ return_on_failure }}
    - name: messages
      value:
        - content: "{{ content }}"
          role: "{{ role }}"
    - name: model
      value: "{{ model }}"
      valid_values: ['@cf/meta/llama-3.3-70b-instruct-fp8-fast', '@cf/zai-org/glm-4.7-flash', '@cf/meta/llama-3.1-8b-instruct-fast', '@cf/meta/llama-3.1-8b-instruct-fp8', '@cf/meta/llama-4-scout-17b-16e-instruct', '@cf/qwen/qwen3-30b-a3b-fp8', '@cf/deepseek-ai/deepseek-r1-distill-qwen-32b', '@cf/moonshotai/kimi-k2-instruct', '@cf/google/gemma-3-12b-it', '@cf/google/gemma-4-26b-a4b-it', '@cf/moonshotai/kimi-k2.5', 'anthropic/claude-3-7-sonnet', 'anthropic/claude-sonnet-4', 'anthropic/claude-opus-4', 'anthropic/claude-3-5-haiku', 'cerebras/qwen-3-235b-a22b-instruct', 'cerebras/qwen-3-235b-a22b-thinking', 'cerebras/llama-3.3-70b', 'cerebras/llama-4-maverick-17b-128e-instruct', 'cerebras/llama-4-scout-17b-16e-instruct', 'cerebras/gpt-oss-120b', 'google-ai-studio/gemini-2.5-flash', 'google-ai-studio/gemini-2.5-pro', 'grok/grok-4', 'groq/llama-3.3-70b-versatile', 'groq/llama-3.1-8b-instant', 'openai/gpt-5', 'openai/gpt-5-mini', 'openai/gpt-5-nano']
    - name: stream
      value: {{ stream }}
`}</CodeBlock>

</TabItem>
</Tabs>
