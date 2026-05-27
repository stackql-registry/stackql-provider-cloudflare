--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - r2
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Job details

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
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="finishedAt" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="overwrite" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td> (title: S3SourceResponseSchema)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (running, paused, aborted, completed)</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>object</code></td>
    <td> (title: R2TargetResponseSchema)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Retrieves detailed status and configuration for a specific R2 Super Slurper migration job.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new R2 Super Slurper migration job to transfer objects from a source bucket (e.g. S3, GCS, R2) to R2.</td>
</tr>
<tr>
    <td><a href="#abort_all"><CopyableCode code="abort_all" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Cancels all running R2 Super Slurper migration jobs for the account. Any objects in the middle of a transfer will finish, but no new objects will start transferring.</td>
</tr>
<tr>
    <td><a href="#slurper_delete_job"><CopyableCode code="slurper_delete_job" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Deletes a completed, aborted, or errored R2 Super Slurper migration job. Active jobs cannot be deleted.</td>
</tr>
<tr>
    <td><a href="#abort"><CopyableCode code="abort" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Cancels a specific R2 Super Slurper migration job. Any objects in the middle of a transfer will finish, but no new objects will start transferring.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Pauses a running R2 Super Slurper migration job. The job can be resumed later to continue transferring.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Resumes a paused R2 Super Slurper migration job, continuing the transfer from where it stopped.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieves detailed status and configuration for a specific R2 Super Slurper migration job.

```sql
SELECT
id,
createdAt,
finishedAt,
overwrite,
source,
status,
target
FROM cloudflare.r2.jobs
WHERE account_id = '{{ account_id }}' -- required
AND job_id = '{{ job_id }}' -- required
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

Creates a new R2 Super Slurper migration job to transfer objects from a source bucket (e.g. S3, GCS, R2) to R2.

```sql
INSERT INTO cloudflare.r2.jobs (
overwrite,
source,
target,
account_id
)
SELECT 
{{ overwrite }},
'{{ source }}',
'{{ target }}',
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: jobs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the jobs resource.
    - name: overwrite
      value: {{ overwrite }}
      default: true
    - name: source
      value:
        bucket: "{{ bucket }}"
        endpoint: "{{ endpoint }}"
        keys:
          - "{{ keys }}"
        pathPrefix: "{{ pathPrefix }}"
        region: "{{ region }}"
        secret:
          accessKeyId: "{{ accessKeyId }}"
          secretAccessKey: "{{ secretAccessKey }}"
        vendor: "{{ vendor }}"
        jurisdiction: "{{ jurisdiction }}"
    - name: target
      value:
        bucket: "{{ bucket }}"
        jurisdiction: "{{ jurisdiction }}"
        secret:
          accessKeyId: "{{ accessKeyId }}"
          secretAccessKey: "{{ secretAccessKey }}"
        vendor: "{{ vendor }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="abort_all"
    values={[
        { label: 'abort_all', value: 'abort_all' }
    ]}
>
<TabItem value="abort_all">

Cancels all running R2 Super Slurper migration jobs for the account. Any objects in the middle of a transfer will finish, but no new objects will start transferring.

```sql
REPLACE cloudflare.r2.jobs
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="slurper_delete_job"
    values={[
        { label: 'slurper_delete_job', value: 'slurper_delete_job' }
    ]}
>
<TabItem value="slurper_delete_job">

Deletes a completed, aborted, or errored R2 Super Slurper migration job. Active jobs cannot be deleted.

```sql
DELETE FROM cloudflare.r2.jobs
WHERE account_id = '{{ account_id }}' --required
AND job_id = '{{ job_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="abort"
    values={[
        { label: 'abort', value: 'abort' },
        { label: 'pause', value: 'pause' },
        { label: 'resume', value: 'resume' }
    ]}
>
<TabItem value="abort">

Cancels a specific R2 Super Slurper migration job. Any objects in the middle of a transfer will finish, but no new objects will start transferring.

```sql
EXEC cloudflare.r2.jobs.abort 
@account_id='{{ account_id }}' --required, 
@job_id='{{ job_id }}' --required
;
```
</TabItem>
<TabItem value="pause">

Pauses a running R2 Super Slurper migration job. The job can be resumed later to continue transferring.

```sql
EXEC cloudflare.r2.jobs.pause 
@account_id='{{ account_id }}' --required, 
@job_id='{{ job_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resumes a paused R2 Super Slurper migration job, continuing the transfer from where it stopped.

```sql
EXEC cloudflare.r2.jobs.resume 
@account_id='{{ account_id }}' --required, 
@job_id='{{ job_id }}' --required
;
```
</TabItem>
</Tabs>
