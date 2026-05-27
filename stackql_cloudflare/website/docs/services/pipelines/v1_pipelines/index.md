--- 
title: v1_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - v1_pipelines
  - pipelines
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

Creates, updates, deletes, gets or lists a <code>v1_pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="v1_pipelines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pipelines.v1_pipelines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Indicates a successfully retrieved Pipeline.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Indicates a unique identifier for this pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Indicates the name of the Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="failure_reason" /></td>
    <td><code>string</code></td>
    <td>Indicates the reason for the failure of the Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sql" /></td>
    <td><code>string</code></td>
    <td>Specifies SQL for the Pipeline processing flow.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Indicates the current status of the Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="tables" /></td>
    <td><code>array</code></td>
    <td>List of streams and sinks used by this pipeline.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Indicates a successfully listed Pipelines.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Indicates a unique identifier for this pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Indicates the name of the Pipeline.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="sql" /></td>
    <td><code>string</code></td>
    <td>Specifies SQL for the Pipeline processing flow.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Indicates the current status of the Pipeline.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pipeline_id"><code>pipeline_id</code></a></td>
    <td></td>
    <td>Get Pipelines Details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List/Filter Pipelines in Account.</td>
</tr>
<tr>
    <td><a href="#create_v1"><CopyableCode code="create_v1" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-sql"><code>sql</code></a></td>
    <td></td>
    <td>Create a new Pipeline.</td>
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
<tr id="parameter-pipeline_id">
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Get Pipelines Details.

```sql
SELECT
id,
name,
created_at,
failure_reason,
modified_at,
sql,
status,
tables
FROM cloudflare.pipelines.v1_pipelines
WHERE account_id = '{{ account_id }}' -- required
AND pipeline_id = '{{ pipeline_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List/Filter Pipelines in Account.

```sql
SELECT
id,
name,
created_at,
modified_at,
sql,
status
FROM cloudflare.pipelines.v1_pipelines
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_v1"
    values={[
        { label: 'create_v1', value: 'create_v1' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_v1">

Create a new Pipeline.

```sql
INSERT INTO cloudflare.pipelines.v1_pipelines (
name,
sql,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ sql }}' /* required */,
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: v1_pipelines
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the v1_pipelines resource.
    - name: name
      value: "{{ name }}"
      description: |
        Specifies the name of the Pipeline.
    - name: sql
      value: "{{ sql }}"
      description: |
        Specifies SQL for the Pipeline processing flow.
`}</CodeBlock>

</TabItem>
</Tabs>
