--- 
title: openchat_3_5_0106
hide_title: false
hide_table_of_contents: false
keywords:
  - openchat_3_5_0106
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

Creates, updates, deletes, gets or lists an <code>openchat_3_5_0106</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="openchat_3_5_0106" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.openchat_3_5_0106" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_openchat_openchat_3_5_0106"><CopyableCode code="workers_ai_post_run_cf_openchat_openchat_3_5_0106" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/openchat/openchat-3.5-0106 model.</td>
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
    defaultValue="workers_ai_post_run_cf_openchat_openchat_3_5_0106"
    values={[
        { label: 'workers_ai_post_run_cf_openchat_openchat_3_5_0106', value: 'workers_ai_post_run_cf_openchat_openchat_3_5_0106' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_openchat_openchat_3_5_0106">

Runs inference on the @cf/openchat/openchat-3.5-0106 model.

```sql
INSERT INTO cloudflare.ai.openchat_3_5_0106 (
frequency_penalty,
lora,
max_tokens,
presence_penalty,
prompt,
raw,
repetition_penalty,
response_format,
seed,
stream,
temperature,
top_k,
top_p,
functions,
messages,
tools,
account_id,
queueRequest,
tags
)
SELECT 
{{ frequency_penalty }},
'{{ lora }}',
{{ max_tokens }},
{{ presence_penalty }},
'{{ prompt }}',
{{ raw }},
{{ repetition_penalty }},
'{{ response_format }}',
{{ seed }},
{{ stream }},
{{ temperature }},
{{ top_k }},
{{ top_p }},
'{{ functions }}',
'{{ messages }}',
'{{ tools }}',
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: openchat_3_5_0106
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the openchat_3_5_0106 resource.
    - name: frequency_penalty
      value: {{ frequency_penalty }}
      description: |
        Decreases the likelihood of the model repeating the same lines verbatim.
    - name: lora
      value: "{{ lora }}"
      description: |
        Name of the LoRA (Low-Rank Adaptation) model to fine-tune the base model.
    - name: max_tokens
      value: {{ max_tokens }}
      description: |
        The maximum number of tokens to generate in the response.
      default: 256
    - name: presence_penalty
      value: {{ presence_penalty }}
      description: |
        Increases the likelihood of the model introducing new topics.
    - name: prompt
      value: "{{ prompt }}"
      description: |
        The input text prompt for the model to generate a response.
    - name: raw
      value: {{ raw }}
      description: |
        If true, a chat template is not applied and you must adhere to the specific model's expected formatting.
      default: false
    - name: repetition_penalty
      value: {{ repetition_penalty }}
      description: |
        Penalty for repeated tokens; higher values discourage repetition.
    - name: response_format
      value:
        json_schema: "{{ json_schema }}"
        type: "{{ type }}"
    - name: seed
      value: {{ seed }}
      description: |
        Random seed for reproducibility of the generation.
    - name: stream
      value: {{ stream }}
      description: |
        If true, the response will be streamed back incrementally using SSE, Server Sent Events.
      default: false
    - name: temperature
      value: {{ temperature }}
      description: |
        Controls the randomness of the output; higher values produce more random results.
      default: 0.6
    - name: top_k
      value: {{ top_k }}
      description: |
        Limits the AI to choose from the top 'k' most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.
    - name: top_p
      value: {{ top_p }}
      description: |
        Adjusts the creativity of the AI's responses by controlling how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.
    - name: functions
      value:
        - code: "{{ code }}"
          name: "{{ name }}"
    - name: messages
      description: |
        An array of message objects representing the conversation history.
      value:
        - content: "{{ content }}"
          role: "{{ role }}"
    - name: tools
      description: |
        A list of tools available for the assistant to use.
      value:
        - description: "{{ description }}"
          name: "{{ name }}"
          parameters:
            properties: "{{ properties }}"
            required:
              - "{{ required }}"
            type: "{{ type }}"
          function:
            description: "{{ description }}"
            name: "{{ name }}"
            parameters:
              properties: "{{ properties }}"
              required:
                - "{{ required }}"
              type: "{{ type }}"
          type: "{{ type }}"
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
