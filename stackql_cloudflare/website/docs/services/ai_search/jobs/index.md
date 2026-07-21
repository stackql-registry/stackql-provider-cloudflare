--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - ai_search
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai_search.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account_by_account', value: 'list_by_account_by_account' }
    ]}
>
<TabItem value="get_by_account">

Returns a AI Search Job Details.

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="end_reason" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ended_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td> (user, schedule)</td>
</tr>
<tr>
    <td><CopyableCode code="started_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account_by_account">

Returns a list of AI Search Jobs.

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="end_reason" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ended_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td> (user, schedule)</td>
</tr>
<tr>
    <td><CopyableCode code="started_at" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific AI Search indexing job.</td>
</tr>
<tr>
    <td><a href="#list_by_account_by_account"><CopyableCode code="list_by_account_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists indexing jobs for an AI Search instance.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new indexing job for an AI Search instance.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Updates the status of an AI Search indexing job.</td>
</tr>
<tr>
    <td><a href="#ai_search_instance_change_job_status"><CopyableCode code="ai_search_instance_change_job_status" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Updates the status of an AI Search indexing job.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job ID.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account_by_account', value: 'list_by_account_by_account' }
    ]}
>
<TabItem value="get_by_account">

Retrieves details for a specific AI Search indexing job.

```sql
SELECT
id,
description,
end_reason,
ended_at,
last_seen_at,
source,
started_at
FROM cloudflare.ai_search.jobs
WHERE id = '{{ id }}' -- required
AND job_id = '{{ job_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account_by_account">

Lists indexing jobs for an AI Search instance.

```sql
SELECT
id,
description,
end_reason,
ended_at,
last_seen_at,
source,
started_at
FROM cloudflare.ai_search.jobs
WHERE id = '{{ id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Creates a new indexing job for an AI Search instance.

```sql
INSERT INTO cloudflare.ai_search.jobs (
description,
id,
account_id
)
SELECT 
'{{ description }}',
'{{ id }}',
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: jobs
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the jobs resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the jobs resource.
    - name: description
      value: "{{ description }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'ai_search_instance_change_job_status', value: 'ai_search_instance_change_job_status' }
    ]}
>
<TabItem value="update">

Updates the status of an AI Search indexing job.

```sql
UPDATE cloudflare.ai_search.jobs
SET 
action = '{{ action }}'
WHERE 
id = '{{ id }}' --required
AND job_id = '{{ job_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND action = '{{ action }}' --required
RETURNING
result,
success;
```
</TabItem>
<TabItem value="ai_search_instance_change_job_status">

Updates the status of an AI Search indexing job.

```sql
UPDATE cloudflare.ai_search.jobs
SET 
action = '{{ action }}'
WHERE 
id = '{{ id }}' --required
AND job_id = '{{ job_id }}' --required
AND account_id = '{{ account_id }}' --required
AND action = '{{ action }}' --required
RETURNING
result,
success;
```
</TabItem>
</Tabs>
