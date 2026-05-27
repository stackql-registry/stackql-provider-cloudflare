--- 
title: qwen3_embedding_0_6b
hide_title: false
hide_table_of_contents: false
keywords:
  - qwen3_embedding_0_6b
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

Creates, updates, deletes, gets or lists a <code>qwen3_embedding_0_6b</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="qwen3_embedding_0_6b" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.qwen3_embedding_0_6b" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_qwen_qwen3_embedding_0_6b"><CopyableCode code="workers_ai_post_run_cf_qwen_qwen3_embedding_0_6b" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/qwen/qwen3-embedding-0.6b model.</td>
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
    defaultValue="workers_ai_post_run_cf_qwen_qwen3_embedding_0_6b"
    values={[
        { label: 'workers_ai_post_run_cf_qwen_qwen3_embedding_0_6b', value: 'workers_ai_post_run_cf_qwen_qwen3_embedding_0_6b' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_qwen_qwen3_embedding_0_6b">

Runs inference on the @cf/qwen/qwen3-embedding-0.6b model.

```sql
INSERT INTO cloudflare.ai.qwen3_embedding_0_6b (
documents,
instruction,
queries,
text,
account_id,
queueRequest,
tags
)
SELECT 
'{{ documents }}',
'{{ instruction }}',
'{{ queries }}',
'{{ text }}',
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: qwen3_embedding_0_6b
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the qwen3_embedding_0_6b resource.
    - name: documents
      value: "{{ documents }}"
      description: |
        A single document string
    - name: instruction
      value: "{{ instruction }}"
      description: |
        Optional instruction for the task
      default: Given a web search query, retrieve relevant passages that answer the query
    - name: queries
      value: "{{ queries }}"
      description: |
        A single query string
    - name: text
      value: "{{ text }}"
      description: |
        Alias for documents: a single text string
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
