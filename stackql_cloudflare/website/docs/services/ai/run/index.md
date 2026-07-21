--- 
title: run
hide_title: false
hide_table_of_contents: false
keywords:
  - run
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

Creates, updates, deletes, gets or lists a <code>run</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="run" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.run" /></td></tr>
</tbody></table>

<br />

:::info[Supported models]

Set `model_name` to one of the following models:

<details>
<summary>Text Generation (55 models)</summary>

<CopyableCode code="@cf/aisingapore/gemma-sea-lion-v4-27b-it" /><br />
<CopyableCode code="@cf/deepseek-ai/deepseek-math-7b-instruct" /><br />
<CopyableCode code="@cf/deepseek-ai/deepseek-r1-distill-qwen-32b" /><br />
<CopyableCode code="@cf/defog/sqlcoder-7b-2" /><br />
<CopyableCode code="@cf/fblgit/una-cybertron-7b-v2-bf16" /><br />
<CopyableCode code="@cf/google/gemma-2b-it-lora" /><br />
<CopyableCode code="@cf/google/gemma-3-12b-it" /><br />
<CopyableCode code="@cf/google/gemma-7b-it-lora" /><br />
<CopyableCode code="@cf/ibm-granite/granite-4.0-h-micro" /><br />
<CopyableCode code="@cf/meta-llama/llama-2-7b-chat-hf-lora" /><br />
<CopyableCode code="@cf/meta/llama-2-7b-chat-fp16" /><br />
<CopyableCode code="@cf/meta/llama-2-7b-chat-int8" /><br />
<CopyableCode code="@cf/meta/llama-3-8b-instruct" /><br />
<CopyableCode code="@cf/meta/llama-3-8b-instruct-awq" /><br />
<CopyableCode code="@cf/meta/llama-3.1-70b-instruct-fp8-fast" /><br />
<CopyableCode code="@cf/meta/llama-3.1-8b-instruct-awq" /><br />
<CopyableCode code="@cf/meta/llama-3.1-8b-instruct-fp8" /><br />
<CopyableCode code="@cf/meta/llama-3.1-8b-instruct-fp8-fast" /><br />
<CopyableCode code="@cf/meta/llama-3.2-11b-vision-instruct" /><br />
<CopyableCode code="@cf/meta/llama-3.2-1b-instruct" /><br />
<CopyableCode code="@cf/meta/llama-3.2-3b-instruct" /><br />
<CopyableCode code="@cf/meta/llama-3.3-70b-instruct-fp8-fast" /><br />
<CopyableCode code="@cf/meta/llama-4-scout-17b-16e-instruct" /><br />
<CopyableCode code="@cf/meta/llama-guard-3-8b" /><br />
<CopyableCode code="@cf/microsoft/phi-2" /><br />
<CopyableCode code="@cf/mistral/mistral-7b-instruct-v0.1" /><br />
<CopyableCode code="@cf/mistral/mistral-7b-instruct-v0.2-lora" /><br />
<CopyableCode code="@cf/mistralai/mistral-small-3.1-24b-instruct" /><br />
<CopyableCode code="@cf/moonshotai/kimi-k2.5" /><br />
<CopyableCode code="@cf/nvidia/nemotron-3-120b-a12b" /><br />
<CopyableCode code="@cf/openai/gpt-oss-120b" /><br />
<CopyableCode code="@cf/openai/gpt-oss-20b" /><br />
<CopyableCode code="@cf/openchat/openchat-3.5-0106" /><br />
<CopyableCode code="@cf/qwen/qwen1.5-0.5b-chat" /><br />
<CopyableCode code="@cf/qwen/qwen1.5-1.8b-chat" /><br />
<CopyableCode code="@cf/qwen/qwen1.5-14b-chat-awq" /><br />
<CopyableCode code="@cf/qwen/qwen1.5-7b-chat-awq" /><br />
<CopyableCode code="@cf/qwen/qwen2.5-coder-32b-instruct" /><br />
<CopyableCode code="@cf/qwen/qwen3-30b-a3b-fp8" /><br />
<CopyableCode code="@cf/qwen/qwq-32b" /><br />
<CopyableCode code="@cf/thebloke/discolm-german-7b-v1-awq" /><br />
<CopyableCode code="@cf/tiiuae/falcon-7b-instruct" /><br />
<CopyableCode code="@cf/tinyllama/tinyllama-1.1b-chat-v1.0" /><br />
<CopyableCode code="@cf/zai-org/glm-4.7-flash" /><br />
<CopyableCode code="@hf/google/gemma-7b-it" /><br />
<CopyableCode code="@hf/mistral/mistral-7b-instruct-v0.2" /><br />
<CopyableCode code="@hf/nexusflow/starling-lm-7b-beta" /><br />
<CopyableCode code="@hf/nousresearch/hermes-2-pro-mistral-7b" /><br />
<CopyableCode code="@hf/thebloke/deepseek-coder-6.7b-base-awq" /><br />
<CopyableCode code="@hf/thebloke/deepseek-coder-6.7b-instruct-awq" /><br />
<CopyableCode code="@hf/thebloke/llama-2-13b-chat-awq" /><br />
<CopyableCode code="@hf/thebloke/mistral-7b-instruct-v0.1-awq" /><br />
<CopyableCode code="@hf/thebloke/neural-chat-7b-v3-1-awq" /><br />
<CopyableCode code="@hf/thebloke/openhermes-2.5-mistral-7b-awq" /><br />
<CopyableCode code="@hf/thebloke/zephyr-7b-beta-awq" /><br />

</details>

<details>
<summary>Text Embeddings (12 models)</summary>

<CopyableCode code="@cf/baai/bge-base-en-v1.5" /><br />
<CopyableCode code="@cf/baai/bge-large-en-v1.5" /><br />
<CopyableCode code="@cf/baai/bge-m3" /><br />
<CopyableCode code="@cf/baai/bge-small-en-v1.5" /><br />
<CopyableCode code="@cf/baai/nonomni-bge-base-en-v1.5" /><br />
<CopyableCode code="@cf/baai/nonomni-bge-large-en-v1.5" /><br />
<CopyableCode code="@cf/baai/nonomni-bge-m3" /><br />
<CopyableCode code="@cf/baai/nonomni-bge-small-en-v1.5" /><br />
<CopyableCode code="@cf/google/embeddinggemma-300m" /><br />
<CopyableCode code="@cf/google/nonomni-embeddinggemma-300m" /><br />
<CopyableCode code="@cf/pfnet/plamo-embedding-1b" /><br />
<CopyableCode code="@cf/qwen/qwen3-embedding-0.6b" /><br />

</details>

<details>
<summary>Speech to Text (3 models)</summary>

<CopyableCode code="@cf/deepgram/flux" /><br />
<CopyableCode code="@cf/deepgram/nova-3" /><br />
<CopyableCode code="@cf/openai/whisper-large-v3-turbo" /><br />

</details>

<details>
<summary>Translation (3 models)</summary>

<CopyableCode code="@cf/ai4bharat/indictrans2-en-indic-1B" /><br />
<CopyableCode code="@cf/ai4bharat/nonomni-indictrans2-en-indic-1b" /><br />
<CopyableCode code="@cf/meta/m2m100-1.2b" /><br />

</details>

<details>
<summary>Summarization (2 models)</summary>

<CopyableCode code="@cf/facebook/bart-large-cnn" /><br />
<CopyableCode code="@cf/facebook/nonomni-bart-large-cnn" /><br />

</details>

<details>
<summary>Text to Image (11 models)</summary>

<CopyableCode code="@cf/black-forest-labs/flux-1-schnell" /><br />
<CopyableCode code="@cf/black-forest-labs/flux-2-dev" /><br />
<CopyableCode code="@cf/black-forest-labs/flux-2-klein-4b" /><br />
<CopyableCode code="@cf/black-forest-labs/flux-2-klein-9b" /><br />
<CopyableCode code="@cf/bytedance/stable-diffusion-xl-lightning" /><br />
<CopyableCode code="@cf/leonardo/lucid-origin" /><br />
<CopyableCode code="@cf/leonardo/phoenix-1.0" /><br />
<CopyableCode code="@cf/lykon/dreamshaper-8-lcm" /><br />
<CopyableCode code="@cf/runwayml/stable-diffusion-v1-5-img2img" /><br />
<CopyableCode code="@cf/runwayml/stable-diffusion-v1-5-inpainting" /><br />
<CopyableCode code="@cf/stabilityai/stable-diffusion-xl-base-1.0" /><br />

</details>

<details>
<summary>Text to Speech (4 models)</summary>

<CopyableCode code="@cf/deepgram/aura-1" /><br />
<CopyableCode code="@cf/deepgram/aura-2-en" /><br />
<CopyableCode code="@cf/deepgram/aura-2-es" /><br />
<CopyableCode code="@cf/myshell-ai/melotts" /><br />

</details>

<details>
<summary>Text Classification (2 models)</summary>

<CopyableCode code="@cf/huggingface/distilbert-sst-2-int8" /><br />
<CopyableCode code="@cf/huggingface/nonomni-distilbert-sst-2-int8" /><br />

</details>

<details>
<summary>Reranking (1 model)</summary>

<CopyableCode code="@cf/baai/bge-reranker-base" /><br />

</details>

The task-family resources above give these models typed result columns - prefer them over `run` where one exists. Binary-input models (`@cf/facebook/nonomni-detr-resnet-50`, `@cf/microsoft/nonomni-resnet-50`, `@cf/microsoft/resnet-50`, `@cf/openai/whisper`, `@cf/openai/whisper-tiny-en`) take a raw request body and are exposed as exec methods on this resource instead of SELECT.

:::

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="run"
    values={[
        { label: 'run', value: 'run' }
    ]}
>
<TabItem value="run">

Model response

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
    <td><CopyableCode code="data" /></td>
    <td><code>array</code></td>
    <td>Embedding vectors, one per input text.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>Echo of the model name, where reported.</td>
</tr>
<tr>
    <td><CopyableCode code="pooling" /></td>
    <td><code>string</code></td>
    <td>Pooling method used (cls or mean), where applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>string</code></td>
    <td>The generated text response from the model.</td>
</tr>
<tr>
    <td><CopyableCode code="shape" /></td>
    <td><code>array</code></td>
    <td>Dimensions of the returned embedding matrix.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>The summarized text.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>The transcribed text.</td>
</tr>
<tr>
    <td><CopyableCode code="tool_calls" /></td>
    <td><code>array</code></td>
    <td>Tool call requests emitted by the model, if tools were provided.</td>
</tr>
<tr>
    <td><CopyableCode code="transcription_info" /></td>
    <td><code>object</code></td>
    <td>Model/language detail, where reported.</td>
</tr>
<tr>
    <td><CopyableCode code="translated_text" /></td>
    <td><code>string</code></td>
    <td>The translated text.</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>object</code></td>
    <td>Token usage counts (prompt_tokens, completion_tokens, total_tokens).</td>
</tr>
<tr>
    <td><CopyableCode code="vtt" /></td>
    <td><code>string</code></td>
    <td>WebVTT formatted transcription, where reported.</td>
</tr>
<tr>
    <td><CopyableCode code="word_count" /></td>
    <td><code>number</code></td>
    <td>Number of words in the transcription, where reported.</td>
</tr>
<tr>
    <td><CopyableCode code="words" /></td>
    <td><code>array</code></td>
    <td>Per-word timing detail, where reported.</td>
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
    <td><a href="#run"><CopyableCode code="run" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-model_name"><code>model_name</code></a></td>
    <td></td>
    <td>This endpoint provides users with the capability to run specific AI models on-demand. By submitting the required input data, users can receive real-time predictions or results generated by the chosen AI model. The endpoint supports various AI model types, ensuring flexibility and adaptability for diverse use cases. Model specific inputs available in [Cloudflare Docs](https://developers.cloudflare.com/workers-ai/models/).</td>
</tr>
<tr>
    <td><a href="#nonomni_detr_resnet_50"><CopyableCode code="nonomni_detr_resnet_50" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/facebook/nonomni-detr-resnet-50 model.</td>
</tr>
<tr>
    <td><a href="#nonomni_resnet_50"><CopyableCode code="nonomni_resnet_50" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/microsoft/nonomni-resnet-50 model.</td>
</tr>
<tr>
    <td><a href="#resnet_50"><CopyableCode code="resnet_50" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/microsoft/resnet-50 model.</td>
</tr>
<tr>
    <td><a href="#whisper"><CopyableCode code="whisper" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/openai/whisper model.</td>
</tr>
<tr>
    <td><a href="#whisper_tiny_en"><CopyableCode code="whisper_tiny_en" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/openai/whisper-tiny-en model.</td>
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
<tr id="parameter-model_name">
    <td><CopyableCode code="model_name" /></td>
    <td><code>string</code></td>
    <td></td>
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

## `SELECT` examples

<Tabs
    defaultValue="run"
    values={[
        { label: 'run', value: 'run' }
    ]}
>
<TabItem value="run">

This endpoint provides users with the capability to run specific AI models on-demand. By submitting the required input data, users can receive real-time predictions or results generated by the chosen AI model. The endpoint supports various AI model types, ensuring flexibility and adaptability for diverse use cases. Model specific inputs available in [Cloudflare Docs](https://developers.cloudflare.com/workers-ai/models/).

```sql
SELECT
response,
usage,
data,
shape,
text,
translated_text,
summary
FROM cloudflare.ai.run
WHERE account_id = '{{ account_id }}' -- required
AND model_name = '{{ model_name }}' -- required
AND prompt = '{{ prompt }}' -- model input
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="nonomni_detr_resnet_50"
    values={[
        { label: 'nonomni_detr_resnet_50', value: 'nonomni_detr_resnet_50' },
        { label: 'nonomni_resnet_50', value: 'nonomni_resnet_50' },
        { label: 'resnet_50', value: 'resnet_50' },
        { label: 'whisper', value: 'whisper' },
        { label: 'whisper_tiny_en', value: 'whisper_tiny_en' }
    ]}
>
<TabItem value="nonomni_detr_resnet_50">

Runs inference on the @cf/facebook/nonomni-detr-resnet-50 model.

```sql
EXEC cloudflare.ai.run.nonomni_detr_resnet_50 
@account_id='{{ account_id }}' --required, 
@queueRequest='{{ queueRequest }}', 
@tags='{{ tags }}'
;
```
</TabItem>
<TabItem value="nonomni_resnet_50">

Runs inference on the @cf/microsoft/nonomni-resnet-50 model.

```sql
EXEC cloudflare.ai.run.nonomni_resnet_50 
@account_id='{{ account_id }}' --required, 
@queueRequest='{{ queueRequest }}', 
@tags='{{ tags }}'
;
```
</TabItem>
<TabItem value="resnet_50">

Runs inference on the @cf/microsoft/resnet-50 model.

```sql
EXEC cloudflare.ai.run.resnet_50 
@account_id='{{ account_id }}' --required, 
@queueRequest='{{ queueRequest }}', 
@tags='{{ tags }}'
;
```
</TabItem>
<TabItem value="whisper">

Runs inference on the @cf/openai/whisper model.

```sql
EXEC cloudflare.ai.run.whisper 
@account_id='{{ account_id }}' --required, 
@queueRequest='{{ queueRequest }}', 
@tags='{{ tags }}'
;
```
</TabItem>
<TabItem value="whisper_tiny_en">

Runs inference on the @cf/openai/whisper-tiny-en model.

```sql
EXEC cloudflare.ai.run.whisper_tiny_en 
@account_id='{{ account_id }}' --required, 
@queueRequest='{{ queueRequest }}', 
@tags='{{ tags }}'
;
```
</TabItem>
</Tabs>
