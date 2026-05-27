--- 
title: bge_reranker_base
hide_title: false
hide_table_of_contents: false
keywords:
  - bge_reranker_base
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

Creates, updates, deletes, gets or lists a <code>bge_reranker_base</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bge_reranker_base" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.bge_reranker_base" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_baai_bge_reranker_base"><CopyableCode code="workers_ai_post_run_cf_baai_bge_reranker_base" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-contexts"><code>contexts</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/baai/bge-reranker-base model.</td>
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
    defaultValue="workers_ai_post_run_cf_baai_bge_reranker_base"
    values={[
        { label: 'workers_ai_post_run_cf_baai_bge_reranker_base', value: 'workers_ai_post_run_cf_baai_bge_reranker_base' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_baai_bge_reranker_base">

Runs inference on the @cf/baai/bge-reranker-base model.

```sql
INSERT INTO cloudflare.ai.bge_reranker_base (
contexts,
query,
top_k,
account_id,
queueRequest,
tags
)
SELECT 
'{{ contexts }}' /* required */,
'{{ query }}' /* required */,
{{ top_k }},
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bge_reranker_base
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the bge_reranker_base resource.
    - name: contexts
      description: |
        List of provided contexts. Note that the index in this array is important, as the response will refer to it.
      value:
        - text: "{{ text }}"
    - name: query
      value: "{{ query }}"
      description: |
        A query you wish to perform against the provided contexts.
    - name: top_k
      value: {{ top_k }}
      description: |
        Number of returned results starting with the best score.
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
