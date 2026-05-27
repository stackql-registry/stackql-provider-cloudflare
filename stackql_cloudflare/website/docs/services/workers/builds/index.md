--- 
title: builds
hide_title: false
hide_table_of_contents: false
keywords:
  - builds
  - workers
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

Creates, updates, deletes, gets or lists a <code>builds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="builds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.builds" /></td></tr>
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

Build retrieved successfully

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
    <td><CopyableCode code="build_outcome" /></td>
    <td><code>string</code></td>
    <td> (success, fail, skipped, cancelled, terminated) (example: success)</td>
</tr>
<tr>
    <td><CopyableCode code="build_trigger_metadata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="build_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Build UUID.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="initializing_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="pull_request" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="running_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (queued, initializing, running, stopped) (example: running)</td>
</tr>
<tr>
    <td><CopyableCode code="stopped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="trigger" /></td>
    <td><code>object</code></td>
    <td>Trigger information without build_token_uuid</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-build_uuid"><code>build_uuid</code></a></td>
    <td></td>
    <td>Retrieve detailed information about a specific build</td>
</tr>
<tr>
    <td><a href="#create_manual_build"><CopyableCode code="create_manual_build" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a></td>
    <td></td>
    <td>Trigger a manual build for a specific trigger</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-build_uuid"><code>build_uuid</code></a></td>
    <td></td>
    <td>Cancel a running or queued build</td>
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
<tr id="parameter-build_uuid">
    <td><CopyableCode code="build_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-trigger_uuid">
    <td><CopyableCode code="trigger_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
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

Retrieve detailed information about a specific build

```sql
SELECT
build_outcome,
build_trigger_metadata,
build_uuid,
created_on,
initializing_on,
modified_on,
pull_request,
running_on,
status,
stopped_on,
trigger
FROM cloudflare.workers.builds
WHERE account_id = '{{ account_id }}' -- required
AND build_uuid = '{{ build_uuid }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_manual_build"
    values={[
        { label: 'create_manual_build', value: 'create_manual_build' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_manual_build">

Trigger a manual build for a specific trigger

```sql
INSERT INTO cloudflare.workers.builds (
branch,
commit_hash,
seed_repo,
account_id,
trigger_uuid
)
SELECT 
'{{ branch }}',
'{{ commit_hash }}',
'{{ seed_repo }}',
'{{ account_id }}',
'{{ trigger_uuid }}'
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
- name: builds
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the builds resource.
    - name: trigger_uuid
      value: "{{ trigger_uuid }}"
      description: Required parameter for the builds resource.
    - name: branch
      value: "{{ branch }}"
      description: |
        Git branch name.
    - name: commit_hash
      value: "{{ commit_hash }}"
      description: |
        Git commit hash
    - name: seed_repo
      value:
        branch: "{{ branch }}"
        files:
          - content: "{{ content }}"
            filename: "{{ filename }}"
            isBase64: {{ isBase64 }}
            replace: "{{ replace }}"
        owner: "{{ owner }}"
        path: "{{ path }}"
        provider: "{{ provider }}"
        repository: "{{ repository }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancel a running or queued build

```sql
EXEC cloudflare.workers.builds.cancel 
@account_id='{{ account_id }}' --required, 
@build_uuid='{{ build_uuid }}' --required
;
```
</TabItem>
</Tabs>
