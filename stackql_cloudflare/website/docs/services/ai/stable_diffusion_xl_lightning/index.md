--- 
title: stable_diffusion_xl_lightning
hide_title: false
hide_table_of_contents: false
keywords:
  - stable_diffusion_xl_lightning
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

Creates, updates, deletes, gets or lists a <code>stable_diffusion_xl_lightning</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="stable_diffusion_xl_lightning" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.stable_diffusion_xl_lightning" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_bytedance_stable_diffusion_xl_lightning"><CopyableCode code="workers_ai_post_run_cf_bytedance_stable_diffusion_xl_lightning" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prompt"><code>prompt</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/bytedance/stable-diffusion-xl-lightning model.</td>
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
    defaultValue="workers_ai_post_run_cf_bytedance_stable_diffusion_xl_lightning"
    values={[
        { label: 'workers_ai_post_run_cf_bytedance_stable_diffusion_xl_lightning', value: 'workers_ai_post_run_cf_bytedance_stable_diffusion_xl_lightning' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_bytedance_stable_diffusion_xl_lightning">

Runs inference on the @cf/bytedance/stable-diffusion-xl-lightning model.

```sql
INSERT INTO cloudflare.ai.stable_diffusion_xl_lightning (
guidance,
height,
image,
image_b64,
mask,
negative_prompt,
num_steps,
prompt,
seed,
strength,
width,
account_id,
queueRequest,
tags
)
SELECT 
{{ guidance }},
{{ height }},
'{{ image }}',
'{{ image_b64 }}',
'{{ mask }}',
'{{ negative_prompt }}',
{{ num_steps }},
'{{ prompt }}' /* required */,
{{ seed }},
{{ strength }},
{{ width }},
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: stable_diffusion_xl_lightning
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the stable_diffusion_xl_lightning resource.
    - name: guidance
      value: {{ guidance }}
      description: |
        Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt
      default: 7.5
    - name: height
      value: {{ height }}
      description: |
        The height of the generated image in pixels
    - name: image
      value:
        - {{ image }}
      description: |
        For use with img2img tasks. An array of integers that represent the image data constrained to 8-bit unsigned integer values
    - name: image_b64
      value: "{{ image_b64 }}"
      description: |
        For use with img2img tasks. A base64-encoded string of the input image
    - name: mask
      value:
        - {{ mask }}
      description: |
        An array representing An array of integers that represent mask image data for inpainting constrained to 8-bit unsigned integer values
    - name: negative_prompt
      value: "{{ negative_prompt }}"
      description: |
        Text describing elements to avoid in the generated image
    - name: num_steps
      value: {{ num_steps }}
      description: |
        The number of diffusion steps; higher values can improve quality but take longer
      default: 20
    - name: prompt
      value: "{{ prompt }}"
      description: |
        A text description of the image you want to generate
    - name: seed
      value: {{ seed }}
      description: |
        Random seed for reproducibility of the image generation
    - name: strength
      value: {{ strength }}
      description: |
        A value between 0 and 1 indicating how strongly to apply the transformation during img2img tasks; lower values make the output closer to the input image
      default: 1
    - name: width
      value: {{ width }}
      description: |
        The width of the generated image in pixels
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
