--- 
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - workflows
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

Creates, updates, deletes, gets or lists an <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workflows.instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get all logs and status from the instance.

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
    <td><CopyableCode code="end" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="output" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="params" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="queued" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="start" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (queued, running, paused, errored, terminated, complete, waitingForPause, waiting)</td>
</tr>
<tr>
    <td><CopyableCode code="step_count" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="steps" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="versionId" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of workflow instances.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workflow_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ended_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="started_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (queued, running, paused, errored, terminated, complete, waitingForPause, waiting)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-simple"><code>simple</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>Retrieves logs and execution status for a specific workflow instance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-date_start"><code>date_start</code></a>, <a href="#parameter-date_end"><code>date_end</code></a></td>
    <td>Lists all instances of a workflow with their execution status.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new instance of a workflow, starting its execution.</td>
</tr>
<tr>
    <td><a href="#batch"><CopyableCode code="batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates multiple workflow instances in a single batch operation.</td>
</tr>
<tr>
    <td><a href="#update_status"><CopyableCode code="update_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td></td>
    <td>Changes the execution status of a workflow instance (e.g., pause, resume, terminate).</td>
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
<tr id="parameter-instance_id">
    <td><CopyableCode code="instance_id" /></td>
    <td><code>string</code></td>
    <td>The Workflow instance ID.</td>
</tr>
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>The Workflow name.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Opaque token for cursor-based pagination. Mutually exclusive with `page`.</td>
</tr>
<tr id="parameter-date_end">
    <td><CopyableCode code="date_end" /></td>
    <td><code>string (date-time)</code></td>
    <td>Accepts ISO 8601 with no timezone offsets and in UTC.</td>
</tr>
<tr id="parameter-date_start">
    <td><CopyableCode code="date_start" /></td>
    <td><code>string (date-time)</code></td>
    <td>Accepts ISO 8601 with no timezone offsets and in UTC.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Defines the direction for cursor-based pagination.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Step ordering: "asc" (default, oldest first) or "desc" (newest first).</td>
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
<tr id="parameter-simple">
    <td><CopyableCode code="simple" /></td>
    <td><code>string</code></td>
    <td>When true, omits step details and returns only metadata with step_count.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves logs and execution status for a specific workflow instance.

```sql
SELECT
end,
error,
output,
params,
queued,
start,
status,
step_count,
steps,
success,
trigger,
versionId
FROM cloudflare.workflows.instances
WHERE workflow_name = '{{ workflow_name }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND simple = '{{ simple }}'
AND order = '{{ order }}'
;
```
</TabItem>
<TabItem value="list">

Lists all instances of a workflow with their execution status.

```sql
SELECT
id,
version_id,
workflow_id,
created_on,
ended_on,
modified_on,
started_on,
status
FROM cloudflare.workflows.instances
WHERE workflow_name = '{{ workflow_name }}' -- required
AND account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND cursor = '{{ cursor }}'
AND direction = '{{ direction }}'
AND status = '{{ status }}'
AND date_start = '{{ date_start }}'
AND date_end = '{{ date_end }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new instance of a workflow, starting its execution.

```sql
INSERT INTO cloudflare.workflows.instances (
instance_id,
instance_retention,
params,
workflow_name,
account_id
)
SELECT 
'{{ instance_id }}',
'{{ instance_retention }}',
'{{ params }}',
'{{ workflow_name }}',
'{{ account_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: instances
  props:
    - name: workflow_name
      value: "{{ workflow_name }}"
      description: Required parameter for the instances resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the instances resource.
    - name: instance_id
      value: "{{ instance_id }}"
    - name: instance_retention
      value:
        error_retention: {{ error_retention }}
        success_retention: {{ success_retention }}
    - name: params
      value: "{{ params }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch"
    values={[
        { label: 'batch', value: 'batch' },
        { label: 'update_status', value: 'update_status' }
    ]}
>
<TabItem value="batch">

Creates multiple workflow instances in a single batch operation.

```sql
EXEC cloudflare.workflows.instances.batch 
@workflow_name='{{ workflow_name }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="update_status">

Changes the execution status of a workflow instance (e.g., pause, resume, terminate).

```sql
EXEC cloudflare.workflows.instances.update_status 
@workflow_name='{{ workflow_name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"from": "{{ from }}", 
"status": "{{ status }}"
}'
;
```
</TabItem>
</Tabs>
