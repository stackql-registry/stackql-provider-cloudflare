--- 
title: aura_2_en
hide_title: false
hide_table_of_contents: false
keywords:
  - aura_2_en
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

Creates, updates, deletes, gets or lists an <code>aura_2_en</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="aura_2_en" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.aura_2_en" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_deepgram_aura_2_en"><CopyableCode code="workers_ai_post_run_cf_deepgram_aura_2_en" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-text"><code>text</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/deepgram/aura-2-en model.</td>
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
    defaultValue="workers_ai_post_run_cf_deepgram_aura_2_en"
    values={[
        { label: 'workers_ai_post_run_cf_deepgram_aura_2_en', value: 'workers_ai_post_run_cf_deepgram_aura_2_en' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_deepgram_aura_2_en">

Runs inference on the @cf/deepgram/aura-2-en model.

```sql
INSERT INTO cloudflare.ai.aura_2_en (
bit_rate,
container,
encoding,
sample_rate,
speaker,
text,
account_id,
queueRequest,
tags
)
SELECT 
{{ bit_rate }},
'{{ container }}',
'{{ encoding }}',
{{ sample_rate }},
'{{ speaker }}',
'{{ text }}' /* required */,
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: aura_2_en
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the aura_2_en resource.
    - name: bit_rate
      value: {{ bit_rate }}
      description: |
        The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.
    - name: container
      value: "{{ container }}"
      description: |
        Container specifies the file format wrapper for the output audio. The available options depend on the encoding type..
      valid_values: ['none', 'wav', 'ogg']
    - name: encoding
      value: "{{ encoding }}"
      description: |
        Encoding of the output audio.
      valid_values: ['linear16', 'flac', 'mulaw', 'alaw', 'mp3', 'opus', 'aac']
    - name: sample_rate
      value: {{ sample_rate }}
      description: |
        Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable
    - name: speaker
      value: "{{ speaker }}"
      description: |
        Speaker used to produce the audio.
      valid_values: ['amalthea', 'andromeda', 'apollo', 'arcas', 'aries', 'asteria', 'athena', 'atlas', 'aurora', 'callista', 'cora', 'cordelia', 'delia', 'draco', 'electra', 'harmonia', 'helena', 'hera', 'hermes', 'hyperion', 'iris', 'janus', 'juno', 'jupiter', 'luna', 'mars', 'minerva', 'neptune', 'odysseus', 'ophelia', 'orion', 'orpheus', 'pandora', 'phoebe', 'pluto', 'saturn', 'thalia', 'theia', 'vesta', 'zeus']
      default: luna
    - name: text
      value: "{{ text }}"
      description: |
        The text content to be converted to speech
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
