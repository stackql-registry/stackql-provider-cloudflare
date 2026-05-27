--- 
title: lucid_origin
hide_title: false
hide_table_of_contents: false
keywords:
  - lucid_origin
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

Creates, updates, deletes, gets or lists a <code>lucid_origin</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lucid_origin" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.lucid_origin" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_leonardo_lucid_origin"><CopyableCode code="workers_ai_post_run_cf_leonardo_lucid_origin" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prompt"><code>prompt</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/leonardo/lucid-origin model.</td>
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
    defaultValue="workers_ai_post_run_cf_leonardo_lucid_origin"
    values={[
        { label: 'workers_ai_post_run_cf_leonardo_lucid_origin', value: 'workers_ai_post_run_cf_leonardo_lucid_origin' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_leonardo_lucid_origin">

Runs inference on the @cf/leonardo/lucid-origin model.

```sql
INSERT INTO cloudflare.ai.lucid_origin (
guidance,
height,
num_steps,
prompt,
seed,
steps,
width,
account_id,
queueRequest,
tags
)
SELECT 
{{ guidance }},
{{ height }},
{{ num_steps }},
'{{ prompt }}' /* required */,
{{ seed }},
{{ steps }},
{{ width }},
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: lucid_origin
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the lucid_origin resource.
    - name: guidance
      value: {{ guidance }}
      description: |
        Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt
      default: 4.5
    - name: height
      value: {{ height }}
      description: |
        The height of the generated image in pixels
      default: 1120
    - name: num_steps
      value: {{ num_steps }}
      description: |
        The number of diffusion steps; higher values can improve quality but take longer
    - name: prompt
      value: "{{ prompt }}"
      description: |
        A text description of the image you want to generate.
    - name: seed
      value: {{ seed }}
      description: |
        Random seed for reproducibility of the image generation
    - name: steps
      value: {{ steps }}
      description: |
        The number of diffusion steps; higher values can improve quality but take longer
    - name: width
      value: {{ width }}
      description: |
        The width of the generated image in pixels
      default: 1120
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
