--- 
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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

Creates, updates, deletes, gets or lists an <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.assets" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-finetune_id"><code>finetune_id</code></a>, <a href="#parameter-file_name"><code>file_name</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>Uploads training data assets for a Workers AI fine-tuning job.</td>
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
<tr id="parameter-finetune_id">
    <td><CopyableCode code="finetune_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Uploads training data assets for a Workers AI fine-tuning job.

```sql
INSERT INTO cloudflare.ai.assets (
file,
file_name,
account_id,
finetune_id
)
SELECT 
'{{ file }}' /* required */,
'{{ file_name }}' /* required */,
'{{ account_id }}',
'{{ finetune_id }}'
RETURNING
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: assets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the assets resource.
    - name: finetune_id
      value: "{{ finetune_id }}"
      description: Required parameter for the assets resource.
    - name: file
      value: "{{ file }}"
      description: |
        File to upload
    - name: file_name
      value: "{{ file_name }}"
      description: |
        Name of the file (adapter_config.json or adapter_model.safetensors)
`}</CodeBlock>

</TabItem>
</Tabs>
