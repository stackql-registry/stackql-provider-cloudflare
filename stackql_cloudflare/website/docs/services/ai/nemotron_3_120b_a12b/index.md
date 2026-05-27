--- 
title: nemotron_3_120b_a12b
hide_title: false
hide_table_of_contents: false
keywords:
  - nemotron_3_120b_a12b
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

Creates, updates, deletes, gets or lists a <code>nemotron_3_120b_a12b</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nemotron_3_120b_a12b" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.nemotron_3_120b_a12b" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_nvidia_nemotron_3_120b_a12b"><CopyableCode code="workers_ai_post_run_cf_nvidia_nemotron_3_120b_a12b" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/nvidia/nemotron-3-120b-a12b model.</td>
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
    defaultValue="workers_ai_post_run_cf_nvidia_nemotron_3_120b_a12b"
    values={[
        { label: 'workers_ai_post_run_cf_nvidia_nemotron_3_120b_a12b', value: 'workers_ai_post_run_cf_nvidia_nemotron_3_120b_a12b' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_nvidia_nemotron_3_120b_a12b">

Runs inference on the @cf/nvidia/nemotron-3-120b-a12b model.

```sql
INSERT INTO cloudflare.ai.nemotron_3_120b_a12b (
audio,
chat_template_kwargs,
frequency_penalty,
function_call,
functions,
logit_bias,
logprobs,
max_completion_tokens,
max_tokens,
metadata,
modalities,
model,
n,
parallel_tool_calls,
prediction,
presence_penalty,
prompt,
reasoning_effort,
response_format,
seed,
service_tier,
stop,
store,
stream,
stream_options,
temperature,
tool_choice,
tools,
top_logprobs,
top_p,
user,
web_search_options,
messages,
account_id,
queueRequest,
tags
)
SELECT 
'{{ audio }}',
'{{ chat_template_kwargs }}',
{{ frequency_penalty }},
'{{ function_call }}',
'{{ functions }}',
'{{ logit_bias }}',
{{ logprobs }},
{{ max_completion_tokens }},
{{ max_tokens }},
'{{ metadata }}',
'{{ modalities }}',
'{{ model }}',
{{ n }},
{{ parallel_tool_calls }},
'{{ prediction }}',
{{ presence_penalty }},
'{{ prompt }}',
'{{ reasoning_effort }}',
'{{ response_format }}',
{{ seed }},
'{{ service_tier }}',
'{{ stop }}',
{{ store }},
{{ stream }},
'{{ stream_options }}',
{{ temperature }},
'{{ tool_choice }}',
'{{ tools }}',
{{ top_logprobs }},
{{ top_p }},
'{{ user }}',
'{{ web_search_options }}',
'{{ messages }}',
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: nemotron_3_120b_a12b
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the nemotron_3_120b_a12b resource.
    - name: audio
      description: |
        Parameters for audio output. Required when modalities includes 'audio'.
      value:
        format: "{{ format }}"
        voice: "{{ voice }}"
    - name: chat_template_kwargs
      value:
        clear_thinking: {{ clear_thinking }}
        enable_thinking: {{ enable_thinking }}
    - name: frequency_penalty
      value: {{ frequency_penalty }}
    - name: function_call
      value: "{{ function_call }}"
      valid_values: ['none', 'auto']
    - name: functions
      value:
        - description: "{{ description }}"
          name: "{{ name }}"
          parameters: "{{ parameters }}"
          strict: {{ strict }}
    - name: logit_bias
      value: "{{ logit_bias }}"
    - name: logprobs
      value: {{ logprobs }}
    - name: max_completion_tokens
      value: {{ max_completion_tokens }}
    - name: max_tokens
      value: {{ max_tokens }}
    - name: metadata
      value: "{{ metadata }}"
    - name: modalities
      value:
        - "{{ modalities }}"
    - name: model
      value: "{{ model }}"
      description: |
        ID of the model to use (e.g. '@cf/zai-org/glm-4.7-flash, etc').
    - name: n
      value: {{ n }}
    - name: parallel_tool_calls
      value: {{ parallel_tool_calls }}
      description: |
        Whether to enable parallel function calling during tool use.
      default: true
    - name: prediction
      value:
        content: "{{ content }}"
        type: "{{ type }}"
    - name: presence_penalty
      value: {{ presence_penalty }}
    - name: prompt
      value: "{{ prompt }}"
      description: |
        The input text prompt for the model to generate a response.
    - name: reasoning_effort
      value: "{{ reasoning_effort }}"
      valid_values: ['low', 'medium', 'high']
    - name: response_format
      description: |
        Specifies the format the model must output.
      value:
        type: "{{ type }}"
        json_schema:
          description: "{{ description }}"
          name: "{{ name }}"
          schema: "{{ schema }}"
          strict: {{ strict }}
    - name: seed
      value: {{ seed }}
    - name: service_tier
      value: "{{ service_tier }}"
      valid_values: ['auto', 'default', 'flex', 'scale', 'priority']
    - name: stop
      value: "{{ stop }}"
    - name: store
      value: {{ store }}
    - name: stream
      value: {{ stream }}
    - name: stream_options
      value:
        include_obfuscation: {{ include_obfuscation }}
        include_usage: {{ include_usage }}
    - name: temperature
      value: {{ temperature }}
    - name: tool_choice
      value: "{{ tool_choice }}"
      description: |
        Controls which (if any) tool is called by the model. 'none' = no tools, 'auto' = model decides, 'required' = must call a tool.
      valid_values: ['none', 'auto', 'required']
    - name: tools
      description: |
        A list of tools the model may call.
      value:
        - function:
            description: "{{ description }}"
            name: "{{ name }}"
            parameters: "{{ parameters }}"
            strict: {{ strict }}
          type: "{{ type }}"
          custom:
            description: "{{ description }}"
            format:
              type: "{{ type }}"
              grammar:
                definition: "{{ definition }}"
                syntax: "{{ syntax }}"
            name: "{{ name }}"
    - name: top_logprobs
      value: {{ top_logprobs }}
    - name: top_p
      value: {{ top_p }}
    - name: user
      value: "{{ user }}"
      description: |
        A unique identifier representing your end-user, for abuse monitoring.
    - name: web_search_options
      description: |
        Options for the web search tool (when using built-in web search).
      value:
        search_context_size: "{{ search_context_size }}"
        user_location:
          approximate:
            city: "{{ city }}"
            country: "{{ country }}"
            region: "{{ region }}"
            timezone: "{{ timezone }}"
          type: "{{ type }}"
    - name: messages
      description: |
        A list of messages comprising the conversation so far.
      value:
        - content: "{{ content }}"
          name: "{{ name }}"
          role: "{{ role }}"
          audio:
            id: "{{ id }}"
          function_call:
            arguments: "{{ arguments }}"
            name: "{{ name }}"
          refusal: "{{ refusal }}"
          tool_calls: "{{ tool_calls }}"
          tool_call_id: "{{ tool_call_id }}"
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
