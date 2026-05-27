--- 
title: deploy_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - deploy_hooks
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

Creates, updates, deletes, gets or lists a <code>deploy_hooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deploy_hooks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.deploy_hooks" /></td></tr>
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

Deploy hook retrieved successfully

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
    <td><CopyableCode code="external_script_id" /></td>
    <td><code>string</code></td>
    <td>System-generated worker script tag. (example: dd7160bb9cef458093557736f4b9e75b)</td>
</tr>
<tr>
    <td><CopyableCode code="deploy_hook_name" /></td>
    <td><code>string</code></td>
    <td>Deploy hook name (1-58 characters). (example: Production Deploy Hook)</td>
</tr>
<tr>
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>Git branch name. (example: main)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deploy_hook_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Deploy hook UUID.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Deploy hooks retrieved successfully

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
    <td><CopyableCode code="external_script_id" /></td>
    <td><code>string</code></td>
    <td>System-generated worker script tag. (example: dd7160bb9cef458093557736f4b9e75b)</td>
</tr>
<tr>
    <td><CopyableCode code="deploy_hook_name" /></td>
    <td><code>string</code></td>
    <td>Deploy hook name (1-58 characters). (example: Production Deploy Hook)</td>
</tr>
<tr>
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>Git branch name. (example: main)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deploy_hook_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Deploy hook UUID.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_build" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-deploy_hook_uuid"><code>deploy_hook_uuid</code></a></td>
    <td></td>
    <td>Get details of a specific deploy hook.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Get all deploy hooks for a specific worker script.</td>
</tr>
<tr>
    <td><a href="#create_deploy_hook"><CopyableCode code="create_deploy_hook" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-deploy_hook_name"><code>deploy_hook_name</code></a>, <a href="#parameter-branch"><code>branch</code></a></td>
    <td></td>
    <td>Create a new deploy hook for a worker script.</td>
</tr>
<tr>
    <td><a href="#trigger_deploy_hook"><CopyableCode code="trigger_deploy_hook" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deploy_hook_uuid"><code>deploy_hook_uuid</code></a></td>
    <td></td>
    <td>Trigger a build using a deploy hook. This endpoint does not require authentication - the deploy_hook_uuid acts as a secret token.</td>
</tr>
<tr>
    <td><a href="#update_deploy_hook"><CopyableCode code="update_deploy_hook" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-deploy_hook_uuid"><code>deploy_hook_uuid</code></a>, <a href="#parameter-deploy_hook_name"><code>deploy_hook_name</code></a>, <a href="#parameter-branch"><code>branch</code></a></td>
    <td></td>
    <td>Update an existing deploy hook.</td>
</tr>
<tr>
    <td><a href="#delete_deploy_hook"><CopyableCode code="delete_deploy_hook" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-deploy_hook_uuid"><code>deploy_hook_uuid</code></a></td>
    <td></td>
    <td>Delete a deploy hook.</td>
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
<tr id="parameter-deploy_hook_uuid">
    <td><CopyableCode code="deploy_hook_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Deploy hook UUID</td>
</tr>
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
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

Get details of a specific deploy hook.

```sql
SELECT
external_script_id,
deploy_hook_name,
branch,
created_on,
deploy_hook_uuid,
modified_on
FROM cloudflare.workers.deploy_hooks
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
AND deploy_hook_uuid = '{{ deploy_hook_uuid }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all deploy hooks for a specific worker script.

```sql
SELECT
external_script_id,
deploy_hook_name,
branch,
created_on,
deploy_hook_uuid,
latest_build,
modified_on
FROM cloudflare.workers.deploy_hooks
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_deploy_hook"
    values={[
        { label: 'create_deploy_hook', value: 'create_deploy_hook' },
        { label: 'trigger_deploy_hook', value: 'trigger_deploy_hook' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_deploy_hook">

Create a new deploy hook for a worker script.

```sql
INSERT INTO cloudflare.workers.deploy_hooks (
branch,
deploy_hook_name,
account_id,
script_name
)
SELECT 
'{{ branch }}' /* required */,
'{{ deploy_hook_name }}' /* required */,
'{{ account_id }}',
'{{ script_name }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="trigger_deploy_hook">

Trigger a build using a deploy hook. This endpoint does not require authentication - the deploy_hook_uuid acts as a secret token.

```sql
INSERT INTO cloudflare.workers.deploy_hooks (
deploy_hook_uuid
)
SELECT 
'{{ deploy_hook_uuid }}'
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
- name: deploy_hooks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the deploy_hooks resource.
    - name: script_name
      value: "{{ script_name }}"
      description: Required parameter for the deploy_hooks resource.
    - name: deploy_hook_uuid
      value: "{{ deploy_hook_uuid }}"
      description: Required parameter for the deploy_hooks resource.
    - name: branch
      value: "{{ branch }}"
      description: |
        Git branch name.
    - name: deploy_hook_name
      value: "{{ deploy_hook_name }}"
      description: |
        Deploy hook name (1-58 characters).
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_deploy_hook"
    values={[
        { label: 'update_deploy_hook', value: 'update_deploy_hook' }
    ]}
>
<TabItem value="update_deploy_hook">

Update an existing deploy hook.

```sql
REPLACE cloudflare.workers.deploy_hooks
SET 
branch = '{{ branch }}',
deploy_hook_name = '{{ deploy_hook_name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND script_name = '{{ script_name }}' --required
AND deploy_hook_uuid = '{{ deploy_hook_uuid }}' --required
AND deploy_hook_name = '{{ deploy_hook_name }}' --required
AND branch = '{{ branch }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_deploy_hook"
    values={[
        { label: 'delete_deploy_hook', value: 'delete_deploy_hook' }
    ]}
>
<TabItem value="delete_deploy_hook">

Delete a deploy hook.

```sql
DELETE FROM cloudflare.workers.deploy_hooks
WHERE account_id = '{{ account_id }}' --required
AND script_name = '{{ script_name }}' --required
AND deploy_hook_uuid = '{{ deploy_hook_uuid }}' --required
;
```
</TabItem>
</Tabs>
