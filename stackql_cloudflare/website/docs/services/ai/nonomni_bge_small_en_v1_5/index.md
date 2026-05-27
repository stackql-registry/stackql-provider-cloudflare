--- 
title: nonomni_bge_small_en_v1_5
hide_title: false
hide_table_of_contents: false
keywords:
  - nonomni_bge_small_en_v1_5
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

Creates, updates, deletes, gets or lists a <code>nonomni_bge_small_en_v1_5</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nonomni_bge_small_en_v1_5" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.nonomni_bge_small_en_v1_5" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_baai_nonomni_bge_small_en_v1_5"><CopyableCode code="workers_ai_post_run_cf_baai_nonomni_bge_small_en_v1_5" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/baai/nonomni-bge-small-en-v1.5 model.</td>
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
    defaultValue="workers_ai_post_run_cf_baai_nonomni_bge_small_en_v1_5"
    values={[
        { label: 'workers_ai_post_run_cf_baai_nonomni_bge_small_en_v1_5', value: 'workers_ai_post_run_cf_baai_nonomni_bge_small_en_v1_5' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_baai_nonomni_bge_small_en_v1_5">

Runs inference on the @cf/baai/nonomni-bge-small-en-v1.5 model.

```sql
INSERT INTO cloudflare.ai.nonomni_bge_small_en_v1_5 (
pooling,
text,
requests,
account_id,
queueRequest,
tags
)
SELECT 
'{{ pooling }}',
'{{ text }}',
'{{ requests }}',
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: nonomni_bge_small_en_v1_5
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the nonomni_bge_small_en_v1_5 resource.
    - name: pooling
      value: "{{ pooling }}"
      description: |
        The pooling method used in the embedding process. \`cls\` pooling will generate more accurate embeddings on larger inputs - however, embeddings created with cls pooling are not compatible with embeddings generated with mean pooling. The default pooling method is \`mean\` in order for this to not be a breaking change, but we highly suggest using the new \`cls\` pooling for better accuracy.
      valid_values: ['mean', 'cls']
      default: mean
    - name: text
      value: "{{ text }}"
      description: |
        The text to embed
    - name: requests
      description: |
        Batch of the embeddings requests to run using async-queue
      value:
        - pooling: "{{ pooling }}"
          text: "{{ text }}"
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
