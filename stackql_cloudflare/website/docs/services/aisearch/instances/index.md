--- 
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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

Creates, updates, deletes, gets or lists an <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.aisearch.instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account_by_account', value: 'list_by_account_by_account' }
    ]}
>
<TabItem value="get_by_account">

Returns the instance.

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
    <td>AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.</td>
</tr>
<tr>
    <td><CopyableCode code="ai_gateway_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="public_endpoint_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="token_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ai_search_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/meta/llama-3.3-70b-instruct-fp8-fast, @cf/zai-org/glm-4.7-flash, @cf/meta/llama-3.1-8b-instruct-fast, @cf/meta/llama-3.1-8b-instruct-fp8, @cf/meta/llama-4-scout-17b-16e-instruct, @cf/qwen/qwen3-30b-a3b-fp8, @cf/deepseek-ai/deepseek-r1-distill-qwen-32b, @cf/moonshotai/kimi-k2-instruct, @cf/google/gemma-3-12b-it, @cf/google/gemma-4-26b-a4b-it, @cf/moonshotai/kimi-k2.5, anthropic/claude-3-7-sonnet, anthropic/claude-sonnet-4, anthropic/claude-opus-4, anthropic/claude-3-5-haiku, cerebras/qwen-3-235b-a22b-instruct, cerebras/qwen-3-235b-a22b-thinking, cerebras/llama-3.3-70b, cerebras/llama-4-maverick-17b-128e-instruct, cerebras/llama-4-scout-17b-16e-instruct, cerebras/gpt-oss-120b, google-ai-studio/gemini-2.5-flash, google-ai-studio/gemini-2.5-pro, grok/grok-4, groq/llama-3.3-70b-versatile, groq/llama-3.1-8b-instant, openai/gpt-5, openai/gpt-5-mini, openai/gpt-5-nano, , )</td>
</tr>
<tr>
    <td><CopyableCode code="cache" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cache_threshold" /></td>
    <td><code>string</code></td>
    <td> (super_strict_match, close_enough, flexible_friend, anything_goes) (default: close_enough)</td>
</tr>
<tr>
    <td><CopyableCode code="chunk_overlap" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="chunk_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_metadata" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="embedding_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/qwen/qwen3-embedding-0.6b, @cf/baai/bge-m3, @cf/baai/bge-large-en-v1.5, @cf/google/embeddinggemma-300m, google-ai-studio/gemini-embedding-001, google-ai-studio/gemini-embedding-2-preview, openai/text-embedding-3-small, openai/text-embedding-3-large, , )</td>
</tr>
<tr>
    <td><CopyableCode code="enable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="engine_version" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="fusion_method" /></td>
    <td><code>string</code></td>
    <td> (max, rrf) (default: rrf)</td>
</tr>
<tr>
    <td><CopyableCode code="hybrid_search_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated — use index_method instead.</td>
</tr>
<tr>
    <td><CopyableCode code="index_method" /></td>
    <td><code>object</code></td>
    <td>Controls which storage backends are used during indexing. Defaults to vector-only.</td>
</tr>
<tr>
    <td><CopyableCode code="indexing_options" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_activity" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_num_results" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="public_endpoint_params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="reranking" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="reranking_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/baai/bge-reranker-base, , )</td>
</tr>
<tr>
    <td><CopyableCode code="retrieval_options" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rewrite_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/meta/llama-3.3-70b-instruct-fp8-fast, @cf/zai-org/glm-4.7-flash, @cf/meta/llama-3.1-8b-instruct-fast, @cf/meta/llama-3.1-8b-instruct-fp8, @cf/meta/llama-4-scout-17b-16e-instruct, @cf/qwen/qwen3-30b-a3b-fp8, @cf/deepseek-ai/deepseek-r1-distill-qwen-32b, @cf/moonshotai/kimi-k2-instruct, @cf/google/gemma-3-12b-it, @cf/google/gemma-4-26b-a4b-it, @cf/moonshotai/kimi-k2.5, anthropic/claude-3-7-sonnet, anthropic/claude-sonnet-4, anthropic/claude-opus-4, anthropic/claude-3-5-haiku, cerebras/qwen-3-235b-a22b-instruct, cerebras/qwen-3-235b-a22b-thinking, cerebras/llama-3.3-70b, cerebras/llama-4-maverick-17b-128e-instruct, cerebras/llama-4-scout-17b-16e-instruct, cerebras/gpt-oss-120b, google-ai-studio/gemini-2.5-flash, google-ai-studio/gemini-2.5-pro, grok/grok-4, groq/llama-3.3-70b-versatile, groq/llama-3.1-8b-instant, openai/gpt-5, openai/gpt-5-mini, openai/gpt-5-nano, , )</td>
</tr>
<tr>
    <td><CopyableCode code="rewrite_query" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="score_threshold" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source_params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (default: waiting)</td>
</tr>
<tr>
    <td><CopyableCode code="sync_interval" /></td>
    <td><code>number</code></td>
    <td>Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h). (900)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (r2, web-crawler, )</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account_by_account">

List of instances.

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
    <td>AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.</td>
</tr>
<tr>
    <td><CopyableCode code="ai_gateway_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="public_endpoint_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="token_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ai_search_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/meta/llama-3.3-70b-instruct-fp8-fast, @cf/zai-org/glm-4.7-flash, @cf/meta/llama-3.1-8b-instruct-fast, @cf/meta/llama-3.1-8b-instruct-fp8, @cf/meta/llama-4-scout-17b-16e-instruct, @cf/qwen/qwen3-30b-a3b-fp8, @cf/deepseek-ai/deepseek-r1-distill-qwen-32b, @cf/moonshotai/kimi-k2-instruct, @cf/google/gemma-3-12b-it, @cf/google/gemma-4-26b-a4b-it, @cf/moonshotai/kimi-k2.5, anthropic/claude-3-7-sonnet, anthropic/claude-sonnet-4, anthropic/claude-opus-4, anthropic/claude-3-5-haiku, cerebras/qwen-3-235b-a22b-instruct, cerebras/qwen-3-235b-a22b-thinking, cerebras/llama-3.3-70b, cerebras/llama-4-maverick-17b-128e-instruct, cerebras/llama-4-scout-17b-16e-instruct, cerebras/gpt-oss-120b, google-ai-studio/gemini-2.5-flash, google-ai-studio/gemini-2.5-pro, grok/grok-4, groq/llama-3.3-70b-versatile, groq/llama-3.1-8b-instant, openai/gpt-5, openai/gpt-5-mini, openai/gpt-5-nano, , )</td>
</tr>
<tr>
    <td><CopyableCode code="cache" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cache_threshold" /></td>
    <td><code>string</code></td>
    <td> (super_strict_match, close_enough, flexible_friend, anything_goes) (default: close_enough)</td>
</tr>
<tr>
    <td><CopyableCode code="chunk_overlap" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="chunk_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_metadata" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="embedding_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/qwen/qwen3-embedding-0.6b, @cf/baai/bge-m3, @cf/baai/bge-large-en-v1.5, @cf/google/embeddinggemma-300m, google-ai-studio/gemini-embedding-001, google-ai-studio/gemini-embedding-2-preview, openai/text-embedding-3-small, openai/text-embedding-3-large, , )</td>
</tr>
<tr>
    <td><CopyableCode code="enable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="engine_version" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="fusion_method" /></td>
    <td><code>string</code></td>
    <td> (max, rrf) (default: rrf)</td>
</tr>
<tr>
    <td><CopyableCode code="hybrid_search_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated — use index_method instead.</td>
</tr>
<tr>
    <td><CopyableCode code="index_method" /></td>
    <td><code>object</code></td>
    <td>Controls which storage backends are used during indexing. Defaults to vector-only.</td>
</tr>
<tr>
    <td><CopyableCode code="indexing_options" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_activity" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="max_num_results" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="public_endpoint_params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="reranking" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="reranking_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/baai/bge-reranker-base, , )</td>
</tr>
<tr>
    <td><CopyableCode code="retrieval_options" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rewrite_model" /></td>
    <td><code>string</code></td>
    <td> (@cf/meta/llama-3.3-70b-instruct-fp8-fast, @cf/zai-org/glm-4.7-flash, @cf/meta/llama-3.1-8b-instruct-fast, @cf/meta/llama-3.1-8b-instruct-fp8, @cf/meta/llama-4-scout-17b-16e-instruct, @cf/qwen/qwen3-30b-a3b-fp8, @cf/deepseek-ai/deepseek-r1-distill-qwen-32b, @cf/moonshotai/kimi-k2-instruct, @cf/google/gemma-3-12b-it, @cf/google/gemma-4-26b-a4b-it, @cf/moonshotai/kimi-k2.5, anthropic/claude-3-7-sonnet, anthropic/claude-sonnet-4, anthropic/claude-opus-4, anthropic/claude-3-5-haiku, cerebras/qwen-3-235b-a22b-instruct, cerebras/qwen-3-235b-a22b-thinking, cerebras/llama-3.3-70b, cerebras/llama-4-maverick-17b-128e-instruct, cerebras/llama-4-scout-17b-16e-instruct, cerebras/gpt-oss-120b, google-ai-studio/gemini-2.5-flash, google-ai-studio/gemini-2.5-pro, grok/grok-4, groq/llama-3.3-70b-versatile, groq/llama-3.1-8b-instant, openai/gpt-5, openai/gpt-5-mini, openai/gpt-5-nano, , )</td>
</tr>
<tr>
    <td><CopyableCode code="rewrite_query" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="score_threshold" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source_params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (default: waiting)</td>
</tr>
<tr>
    <td><CopyableCode code="sync_interval" /></td>
    <td><code>number</code></td>
    <td>Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h). (900)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (r2, web-crawler, )</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Read instance.</td>
</tr>
<tr>
    <td><a href="#list_by_account_by_account"><CopyableCode code="list_by_account_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-namespace"><code>namespace</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-order_by_direction"><code>order_by_direction</code></a></td>
    <td>List instances.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Create a new instance.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Update instance.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Delete instance.</td>
</tr>
<tr>
    <td><a href="#ai_search_move_instance"><CopyableCode code="ai_search_move_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-new_namespace"><code>new_namespace</code></a></td>
    <td></td>
    <td>Moves an instance from its current namespace to the specified target namespace. Use 'default' as new_namespace to move the instance back to the default namespace. Fails with 400 if the target namespace already has an instance with the same id (ids must be unique within a namespace — the same id can exist in different namespaces).</td>
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
<tr id="parameter-namespace">
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>Filter by namespace.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>Field to order results by.</td>
</tr>
<tr id="parameter-order_by_direction">
    <td><CopyableCode code="order_by_direction" /></td>
    <td><code>string</code></td>
    <td>Order direction.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number (1-indexed).</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of results per page.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Filter instances whose id contains this string (case-insensitive).</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account_by_account', value: 'list_by_account_by_account' }
    ]}
>
<TabItem value="get_by_account">

Read instance.

```sql
SELECT
id,
ai_gateway_id,
public_endpoint_id,
token_id,
ai_search_model,
cache,
cache_threshold,
chunk_overlap,
chunk_size,
created_at,
created_by,
custom_metadata,
embedding_model,
enable,
engine_version,
fusion_method,
hybrid_search_enabled,
index_method,
indexing_options,
last_activity,
max_num_results,
metadata,
modified_at,
modified_by,
namespace,
paused,
public_endpoint_params,
reranking,
reranking_model,
retrieval_options,
rewrite_model,
rewrite_query,
score_threshold,
source,
source_params,
status,
sync_interval,
type
FROM cloudflare.aisearch.instances
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account_by_account">

List instances.

```sql
SELECT
id,
ai_gateway_id,
public_endpoint_id,
token_id,
ai_search_model,
cache,
cache_threshold,
chunk_overlap,
chunk_size,
created_at,
created_by,
custom_metadata,
embedding_model,
enable,
engine_version,
fusion_method,
hybrid_search_enabled,
index_method,
indexing_options,
last_activity,
max_num_results,
metadata,
modified_at,
modified_by,
namespace,
paused,
public_endpoint_params,
reranking,
reranking_model,
retrieval_options,
rewrite_model,
rewrite_query,
score_threshold,
source,
source_params,
status,
sync_interval,
type
FROM cloudflare.aisearch.instances
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND namespace = '{{ namespace }}'
AND order_by = '{{ order_by }}'
AND order_by_direction = '{{ order_by_direction }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Create a new instance.

```sql
INSERT INTO cloudflare.aisearch.instances (
ai_gateway_id,
ai_search_model,
cache,
cache_threshold,
chunk,
chunk_overlap,
chunk_size,
custom_metadata,
embedding_model,
fusion_method,
hybrid_search_enabled,
id,
index_method,
indexing_options,
max_num_results,
metadata,
public_endpoint_params,
reranking,
reranking_model,
retrieval_options,
rewrite_model,
rewrite_query,
score_threshold,
source,
source_params,
sync_interval,
token_id,
type,
account_id
)
SELECT 
'{{ ai_gateway_id }}',
'{{ ai_search_model }}',
{{ cache }},
'{{ cache_threshold }}',
{{ chunk }},
{{ chunk_overlap }},
{{ chunk_size }},
'{{ custom_metadata }}',
'{{ embedding_model }}',
'{{ fusion_method }}',
{{ hybrid_search_enabled }},
'{{ id }}' /* required */,
'{{ index_method }}',
'{{ indexing_options }}',
{{ max_num_results }},
'{{ metadata }}',
'{{ public_endpoint_params }}',
{{ reranking }},
'{{ reranking_model }}',
'{{ retrieval_options }}',
'{{ rewrite_model }}',
{{ rewrite_query }},
{{ score_threshold }},
'{{ source }}',
'{{ source_params }}',
{{ sync_interval }},
'{{ token_id }}',
'{{ type }}',
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: instances
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the instances resource.
    - name: ai_gateway_id
      value: "{{ ai_gateway_id }}"
    - name: ai_search_model
      value: "{{ ai_search_model }}"
      valid_values: ['@cf/meta/llama-3.3-70b-instruct-fp8-fast', '@cf/zai-org/glm-4.7-flash', '@cf/meta/llama-3.1-8b-instruct-fast', '@cf/meta/llama-3.1-8b-instruct-fp8', '@cf/meta/llama-4-scout-17b-16e-instruct', '@cf/qwen/qwen3-30b-a3b-fp8', '@cf/deepseek-ai/deepseek-r1-distill-qwen-32b', '@cf/moonshotai/kimi-k2-instruct', '@cf/google/gemma-3-12b-it', '@cf/google/gemma-4-26b-a4b-it', '@cf/moonshotai/kimi-k2.5', 'anthropic/claude-3-7-sonnet', 'anthropic/claude-sonnet-4', 'anthropic/claude-opus-4', 'anthropic/claude-3-5-haiku', 'cerebras/qwen-3-235b-a22b-instruct', 'cerebras/qwen-3-235b-a22b-thinking', 'cerebras/llama-3.3-70b', 'cerebras/llama-4-maverick-17b-128e-instruct', 'cerebras/llama-4-scout-17b-16e-instruct', 'cerebras/gpt-oss-120b', 'google-ai-studio/gemini-2.5-flash', 'google-ai-studio/gemini-2.5-pro', 'grok/grok-4', 'groq/llama-3.3-70b-versatile', 'groq/llama-3.1-8b-instant', 'openai/gpt-5', 'openai/gpt-5-mini', 'openai/gpt-5-nano', '', '']
    - name: cache
      value: {{ cache }}
      default: true
    - name: cache_threshold
      value: "{{ cache_threshold }}"
      valid_values: ['super_strict_match', 'close_enough', 'flexible_friend', 'anything_goes']
      default: close_enough
    - name: chunk
      value: {{ chunk }}
      default: true
    - name: chunk_overlap
      value: {{ chunk_overlap }}
      default: 10
    - name: chunk_size
      value: {{ chunk_size }}
    - name: custom_metadata
      value:
        - data_type: "{{ data_type }}"
          field_name: "{{ field_name }}"
    - name: embedding_model
      value: "{{ embedding_model }}"
      valid_values: ['@cf/qwen/qwen3-embedding-0.6b', '@cf/baai/bge-m3', '@cf/baai/bge-large-en-v1.5', '@cf/google/embeddinggemma-300m', 'google-ai-studio/gemini-embedding-001', 'google-ai-studio/gemini-embedding-2-preview', 'openai/text-embedding-3-small', 'openai/text-embedding-3-large', '', '']
    - name: fusion_method
      value: "{{ fusion_method }}"
      valid_values: ['max', 'rrf']
      default: rrf
    - name: hybrid_search_enabled
      value: {{ hybrid_search_enabled }}
      description: |
        Deprecated — use index_method instead.
      default: false
    - name: id
      value: "{{ id }}"
      description: |
        AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
    - name: index_method
      description: |
        Controls which storage backends are used during indexing. Defaults to vector-only.
      value:
        keyword: {{ keyword }}
        vector: {{ vector }}
      default: [object Object]
    - name: indexing_options
      value:
        keyword_tokenizer: "{{ keyword_tokenizer }}"
    - name: max_num_results
      value: {{ max_num_results }}
      default: 10
    - name: metadata
      value:
        created_from_aisearch_wizard: {{ created_from_aisearch_wizard }}
        search_for_agents:
          hostname: "{{ hostname }}"
          zone_id: "{{ zone_id }}"
          zone_name: "{{ zone_name }}"
        worker_domain: "{{ worker_domain }}"
    - name: public_endpoint_params
      value:
        authorized_hosts:
          - "{{ authorized_hosts }}"
        chat_completions_endpoint:
          disabled: {{ disabled }}
        enabled: {{ enabled }}
        mcp:
          description: "{{ description }}"
          disabled: {{ disabled }}
        rate_limit:
          period_ms: {{ period_ms }}
          requests: {{ requests }}
          technique: "{{ technique }}"
        search_endpoint:
          disabled: {{ disabled }}
    - name: reranking
      value: {{ reranking }}
      default: false
    - name: reranking_model
      value: "{{ reranking_model }}"
      valid_values: ['@cf/baai/bge-reranker-base', '', '']
    - name: retrieval_options
      value:
        boost_by:
          - direction: "{{ direction }}"
            field: "{{ field }}"
        keyword_match_mode: "{{ keyword_match_mode }}"
    - name: rewrite_model
      value: "{{ rewrite_model }}"
      valid_values: ['@cf/meta/llama-3.3-70b-instruct-fp8-fast', '@cf/zai-org/glm-4.7-flash', '@cf/meta/llama-3.1-8b-instruct-fast', '@cf/meta/llama-3.1-8b-instruct-fp8', '@cf/meta/llama-4-scout-17b-16e-instruct', '@cf/qwen/qwen3-30b-a3b-fp8', '@cf/deepseek-ai/deepseek-r1-distill-qwen-32b', '@cf/moonshotai/kimi-k2-instruct', '@cf/google/gemma-3-12b-it', '@cf/google/gemma-4-26b-a4b-it', '@cf/moonshotai/kimi-k2.5', 'anthropic/claude-3-7-sonnet', 'anthropic/claude-sonnet-4', 'anthropic/claude-opus-4', 'anthropic/claude-3-5-haiku', 'cerebras/qwen-3-235b-a22b-instruct', 'cerebras/qwen-3-235b-a22b-thinking', 'cerebras/llama-3.3-70b', 'cerebras/llama-4-maverick-17b-128e-instruct', 'cerebras/llama-4-scout-17b-16e-instruct', 'cerebras/gpt-oss-120b', 'google-ai-studio/gemini-2.5-flash', 'google-ai-studio/gemini-2.5-pro', 'grok/grok-4', 'groq/llama-3.3-70b-versatile', 'groq/llama-3.1-8b-instant', 'openai/gpt-5', 'openai/gpt-5-mini', 'openai/gpt-5-nano', '', '']
    - name: rewrite_query
      value: {{ rewrite_query }}
      default: false
    - name: score_threshold
      value: {{ score_threshold }}
      default: 0.4
    - name: source
      value: "{{ source }}"
    - name: source_params
      value:
        exclude_items:
          - "{{ exclude_items }}"
        include_items:
          - "{{ include_items }}"
        prefix: "{{ prefix }}"
        r2_jurisdiction: "{{ r2_jurisdiction }}"
        web_crawler:
          crawl_options:
            depth: {{ depth }}
            include_external_links: {{ include_external_links }}
            include_subdomains: {{ include_subdomains }}
            max_age: {{ max_age }}
            source: "{{ source }}"
          parse_options:
            content_selector:
              - path: "{{ path }}"
                selector: "{{ selector }}"
            include_headers: "{{ include_headers }}"
            include_images: {{ include_images }}
            specific_sitemaps:
              - "{{ specific_sitemaps }}"
            use_browser_rendering: {{ use_browser_rendering }}
          parse_type: "{{ parse_type }}"
          store_options:
            r2_jurisdiction: "{{ r2_jurisdiction }}"
            storage_id: "{{ storage_id }}"
            storage_type: "{{ storage_type }}"
    - name: sync_interval
      value: {{ sync_interval }}
      description: |
        Interval between automatic syncs, in seconds. Allowed values: 900 (15min), 1800 (30min), 3600 (1h), 7200 (2h), 14400 (4h), 21600 (6h), 43200 (12h), 86400 (24h).
      valid_values: ['900']
      default: 21600
    - name: token_id
      value: "{{ token_id }}"
    - name: type
      value: "{{ type }}"
      valid_values: ['r2', 'web-crawler', '']
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' }
    ]}
>
<TabItem value="update_by_account">

Update instance.

```sql
REPLACE cloudflare.aisearch.instances
SET 
ai_gateway_id = '{{ ai_gateway_id }}',
ai_search_model = '{{ ai_search_model }}',
cache = {{ cache }},
cache_threshold = '{{ cache_threshold }}',
chunk = {{ chunk }},
chunk_overlap = {{ chunk_overlap }},
chunk_size = {{ chunk_size }},
custom_metadata = '{{ custom_metadata }}',
embedding_model = '{{ embedding_model }}',
fusion_method = '{{ fusion_method }}',
index_method = '{{ index_method }}',
indexing_options = '{{ indexing_options }}',
max_num_results = {{ max_num_results }},
metadata = '{{ metadata }}',
paused = {{ paused }},
public_endpoint_params = '{{ public_endpoint_params }}',
reranking = {{ reranking }},
reranking_model = '{{ reranking_model }}',
retrieval_options = '{{ retrieval_options }}',
rewrite_model = '{{ rewrite_model }}',
rewrite_query = {{ rewrite_query }},
score_threshold = {{ score_threshold }},
source_params = '{{ source_params }}',
summarization = {{ summarization }},
summarization_model = '{{ summarization_model }}',
sync_interval = {{ sync_interval }},
system_prompt_ai_search = '{{ system_prompt_ai_search }}',
system_prompt_index_summarization = '{{ system_prompt_index_summarization }}',
system_prompt_rewrite_query = '{{ system_prompt_rewrite_query }}',
token_id = '{{ token_id }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
RETURNING
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' }
    ]}
>
<TabItem value="delete_by_account">

Delete instance.

```sql
DELETE FROM cloudflare.aisearch.instances
WHERE account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="ai_search_move_instance"
    values={[
        { label: 'ai_search_move_instance', value: 'ai_search_move_instance' }
    ]}
>
<TabItem value="ai_search_move_instance">

Moves an instance from its current namespace to the specified target namespace. Use 'default' as new_namespace to move the instance back to the default namespace. Fails with 400 if the target namespace already has an instance with the same id (ids must be unique within a namespace — the same id can exist in different namespaces).

```sql
EXEC cloudflare.aisearch.instances.ai_search_move_instance 
@account_id='{{ account_id }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required 
@@json=
'{
"new_namespace": "{{ new_namespace }}"
}'
;
```
</TabItem>
</Tabs>
