--- 
title: whisper_large_v3_turbo
hide_title: false
hide_table_of_contents: false
keywords:
  - whisper_large_v3_turbo
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

Creates, updates, deletes, gets or lists a <code>whisper_large_v3_turbo</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="whisper_large_v3_turbo" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.whisper_large_v3_turbo" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_openai_whisper_large_v3_turbo"><CopyableCode code="workers_ai_post_run_cf_openai_whisper_large_v3_turbo" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-audio"><code>audio</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/openai/whisper-large-v3-turbo model.</td>
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
    defaultValue="workers_ai_post_run_cf_openai_whisper_large_v3_turbo"
    values={[
        { label: 'workers_ai_post_run_cf_openai_whisper_large_v3_turbo', value: 'workers_ai_post_run_cf_openai_whisper_large_v3_turbo' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_openai_whisper_large_v3_turbo">

Runs inference on the @cf/openai/whisper-large-v3-turbo model.

```sql
INSERT INTO cloudflare.ai.whisper_large_v3_turbo (
audio,
beam_size,
compression_ratio_threshold,
condition_on_previous_text,
hallucination_silence_threshold,
initial_prompt,
language,
log_prob_threshold,
no_speech_threshold,
prefix,
task,
vad_filter,
account_id,
queueRequest,
tags
)
SELECT 
'{{ audio }}' /* required */,
{{ beam_size }},
{{ compression_ratio_threshold }},
{{ condition_on_previous_text }},
{{ hallucination_silence_threshold }},
'{{ initial_prompt }}',
'{{ language }}',
{{ log_prob_threshold }},
{{ no_speech_threshold }},
'{{ prefix }}',
'{{ task }}',
{{ vad_filter }},
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: whisper_large_v3_turbo
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the whisper_large_v3_turbo resource.
    - name: audio
      value: "{{ audio }}"
      description: |
        Base64 encoded value of the audio data.
    - name: beam_size
      value: {{ beam_size }}
      description: |
        The number of beams to use in beam search decoding. Higher values may improve accuracy at the cost of speed.
      default: 5
    - name: compression_ratio_threshold
      value: {{ compression_ratio_threshold }}
      description: |
        Threshold for filtering out segments with high compression ratio, which often indicate repetitive or hallucinated text.
      default: 2.4
    - name: condition_on_previous_text
      value: {{ condition_on_previous_text }}
      description: |
        Whether to condition on previous text during transcription. Setting to false may help prevent hallucination loops.
      default: true
    - name: hallucination_silence_threshold
      value: {{ hallucination_silence_threshold }}
      description: |
        Optional threshold (in seconds) to skip silent periods that may cause hallucinations.
    - name: initial_prompt
      value: "{{ initial_prompt }}"
      description: |
        A text prompt to help provide context to the model on the contents of the audio.
    - name: language
      value: "{{ language }}"
      description: |
        The language of the audio being transcribed or translated.
    - name: log_prob_threshold
      value: {{ log_prob_threshold }}
      description: |
        Threshold for filtering out segments with low average log probability, indicating low confidence.
      default: -1
    - name: no_speech_threshold
      value: {{ no_speech_threshold }}
      description: |
        Threshold for detecting no-speech segments. Segments with no-speech probability above this value are skipped.
      default: 0.6
    - name: prefix
      value: "{{ prefix }}"
      description: |
        The prefix appended to the beginning of the output of the transcription and can guide the transcription result.
    - name: task
      value: "{{ task }}"
      description: |
        Supported tasks are 'translate' or 'transcribe'.
      default: transcribe
    - name: vad_filter
      value: {{ vad_filter }}
      description: |
        Preprocess the audio with a voice activity detection model.
      default: false
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
