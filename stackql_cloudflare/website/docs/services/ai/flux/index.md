--- 
title: flux
hide_title: false
hide_table_of_contents: false
keywords:
  - flux
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

Creates, updates, deletes, gets or lists a <code>flux</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="flux" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.flux" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_deepgram_flux"><CopyableCode code="workers_ai_post_run_cf_deepgram_flux" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sample_rate"><code>sample_rate</code></a>, <a href="#parameter-encoding"><code>encoding</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/deepgram/flux model.</td>
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
    defaultValue="workers_ai_post_run_cf_deepgram_flux"
    values={[
        { label: 'workers_ai_post_run_cf_deepgram_flux', value: 'workers_ai_post_run_cf_deepgram_flux' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_deepgram_flux">

Runs inference on the @cf/deepgram/flux model.

```sql
INSERT INTO cloudflare.ai.flux (
eager_eot_threshold,
encoding,
eot_threshold,
eot_timeout_ms,
keyterm,
mip_opt_out,
sample_rate,
tag,
account_id,
queueRequest,
tags
)
SELECT 
'{{ eager_eot_threshold }}',
'{{ encoding }}' /* required */,
'{{ eot_threshold }}',
'{{ eot_timeout_ms }}',
'{{ keyterm }}',
'{{ mip_opt_out }}',
'{{ sample_rate }}' /* required */,
'{{ tag }}',
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: flux
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the flux resource.
    - name: eager_eot_threshold
      value: "{{ eager_eot_threshold }}"
      description: |
        End-of-turn confidence required to fire an eager end-of-turn event. When set, enables EagerEndOfTurn and TurnResumed events. Valid Values 0.3 - 0.9.
    - name: encoding
      value: "{{ encoding }}"
      description: |
        Encoding of the audio stream. Currently only supports raw signed little-endian 16-bit PCM.
      valid_values: ['linear16']
    - name: eot_threshold
      value: "{{ eot_threshold }}"
      description: |
        End-of-turn confidence required to finish a turn. Valid Values 0.5 - 0.9.
      default: 0.7
    - name: eot_timeout_ms
      value: "{{ eot_timeout_ms }}"
      description: |
        A turn will be finished when this much time has passed after speech, regardless of EOT confidence.
      default: 5000
    - name: keyterm
      value: "{{ keyterm }}"
      description: |
        Keyterm prompting can improve recognition of specialized terminology. Pass multiple keyterm query parameters to boost multiple keyterms.
    - name: mip_opt_out
      value: "{{ mip_opt_out }}"
      description: |
        Opts out requests from the Deepgram Model Improvement Program. Refer to Deepgram Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip
      valid_values: ['true', 'false']
      default: false
    - name: sample_rate
      value: "{{ sample_rate }}"
      description: |
        Sample rate of the audio stream in Hz.
    - name: tag
      value: "{{ tag }}"
      description: |
        Label your requests for the purpose of identification during usage reporting
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
