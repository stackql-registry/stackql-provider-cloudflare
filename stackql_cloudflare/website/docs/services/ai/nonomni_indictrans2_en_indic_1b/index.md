--- 
title: nonomni_indictrans2_en_indic_1b
hide_title: false
hide_table_of_contents: false
keywords:
  - nonomni_indictrans2_en_indic_1b
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

Creates, updates, deletes, gets or lists a <code>nonomni_indictrans2_en_indic_1b</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nonomni_indictrans2_en_indic_1b" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.nonomni_indictrans2_en_indic_1b" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_ai4bharat_nonomni_indictrans2_en_indic_1b"><CopyableCode code="workers_ai_post_run_cf_ai4bharat_nonomni_indictrans2_en_indic_1b" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-text"><code>text</code></a>, <a href="#parameter-target_language"><code>target_language</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/ai4bharat/nonomni-indictrans2-en-indic-1b model.</td>
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
    defaultValue="workers_ai_post_run_cf_ai4bharat_nonomni_indictrans2_en_indic_1b"
    values={[
        { label: 'workers_ai_post_run_cf_ai4bharat_nonomni_indictrans2_en_indic_1b', value: 'workers_ai_post_run_cf_ai4bharat_nonomni_indictrans2_en_indic_1b' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_ai4bharat_nonomni_indictrans2_en_indic_1b">

Runs inference on the @cf/ai4bharat/nonomni-indictrans2-en-indic-1b model.

```sql
INSERT INTO cloudflare.ai.nonomni_indictrans2_en_indic_1b (
target_language,
text,
account_id,
queueRequest,
tags
)
SELECT 
'{{ target_language }}' /* required */,
'{{ text }}' /* required */,
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: nonomni_indictrans2_en_indic_1b
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the nonomni_indictrans2_en_indic_1b resource.
    - name: target_language
      value: "{{ target_language }}"
      description: |
        Target langauge to translate to
      valid_values: ['asm_Beng', 'awa_Deva', 'ben_Beng', 'bho_Deva', 'brx_Deva', 'doi_Deva', 'eng_Latn', 'gom_Deva', 'gon_Deva', 'guj_Gujr', 'hin_Deva', 'hne_Deva', 'kan_Knda', 'kas_Arab', 'kas_Deva', 'kha_Latn', 'lus_Latn', 'mag_Deva', 'mai_Deva', 'mal_Mlym', 'mar_Deva', 'mni_Beng', 'mni_Mtei', 'npi_Deva', 'ory_Orya', 'pan_Guru', 'san_Deva', 'sat_Olck', 'snd_Arab', 'snd_Deva', 'tam_Taml', 'tel_Telu', 'urd_Arab', 'unr_Deva']
      default: hin_Deva
    - name: text
      value: "{{ text }}"
      description: |
        Input text to translate. Can be a single string or a list of strings.
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
