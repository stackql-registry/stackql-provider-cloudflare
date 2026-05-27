--- 
title: flux_2_klein_9b
hide_title: false
hide_table_of_contents: false
keywords:
  - flux_2_klein_9b
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

Creates, updates, deletes, gets or lists a <code>flux_2_klein_9b</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="flux_2_klein_9b" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.flux_2_klein_9b" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_black_forest_labs_flux_2_klein_9b"><CopyableCode code="workers_ai_post_run_cf_black_forest_labs_flux_2_klein_9b" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-multipart"><code>multipart</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/black-forest-labs/flux-2-klein-9b model.</td>
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
    defaultValue="workers_ai_post_run_cf_black_forest_labs_flux_2_klein_9b"
    values={[
        { label: 'workers_ai_post_run_cf_black_forest_labs_flux_2_klein_9b', value: 'workers_ai_post_run_cf_black_forest_labs_flux_2_klein_9b' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_black_forest_labs_flux_2_klein_9b">

Runs inference on the @cf/black-forest-labs/flux-2-klein-9b model.

```sql
INSERT INTO cloudflare.ai.flux_2_klein_9b (
multipart,
account_id,
queueRequest,
tags
)
SELECT 
'{{ multipart }}' /* required */,
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: flux_2_klein_9b
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the flux_2_klein_9b resource.
    - name: multipart
      value:
        body: "{{ body }}"
        contentType: "{{ contentType }}"
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
