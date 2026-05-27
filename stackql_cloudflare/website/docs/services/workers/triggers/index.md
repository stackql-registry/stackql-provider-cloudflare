--- 
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
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

Creates, updates, deletes, gets or lists a <code>triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="triggers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.triggers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Triggers retrieved successfully

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
    <td><CopyableCode code="build_token_name" /></td>
    <td><code>string</code></td>
    <td> (example: My Build Token)</td>
</tr>
<tr>
    <td><CopyableCode code="trigger_name" /></td>
    <td><code>string</code></td>
    <td> (example: Production Deploy)</td>
</tr>
<tr>
    <td><CopyableCode code="branch_excludes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="branch_includes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="build_caching_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="build_command" /></td>
    <td><code>string</code></td>
    <td> (example: npm run build)</td>
</tr>
<tr>
    <td><CopyableCode code="build_token_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Build token UUID.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deleted_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deploy_command" /></td>
    <td><code>string</code></td>
    <td> (example: npx wrangler deploy)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path_excludes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path_includes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="repo_connection" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="root_directory" /></td>
    <td><code>string</code></td>
    <td>Root directory path. (example: /)</td>
</tr>
<tr>
    <td><CopyableCode code="trigger_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Trigger UUID.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-external_script_id"><code>external_script_id</code></a></td>
    <td></td>
    <td>Get all triggers for a specific worker script</td>
</tr>
<tr>
    <td><a href="#create_trigger"><CopyableCode code="create_trigger" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-external_script_id"><code>external_script_id</code></a>, <a href="#parameter-build_token_uuid"><code>build_token_uuid</code></a>, <a href="#parameter-trigger_name"><code>trigger_name</code></a>, <a href="#parameter-build_command"><code>build_command</code></a>, <a href="#parameter-deploy_command"><code>deploy_command</code></a>, <a href="#parameter-root_directory"><code>root_directory</code></a>, <a href="#parameter-branch_includes"><code>branch_includes</code></a>, <a href="#parameter-branch_excludes"><code>branch_excludes</code></a>, <a href="#parameter-path_includes"><code>path_includes</code></a>, <a href="#parameter-path_excludes"><code>path_excludes</code></a>, <a href="#parameter-repo_connection_uuid"><code>repo_connection_uuid</code></a></td>
    <td></td>
    <td>Create a new CI/CD trigger</td>
</tr>
<tr>
    <td><a href="#update_trigger"><CopyableCode code="update_trigger" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a></td>
    <td></td>
    <td>Update an existing CI/CD trigger</td>
</tr>
<tr>
    <td><a href="#delete_trigger"><CopyableCode code="delete_trigger" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a></td>
    <td></td>
    <td>Remove a CI/CD trigger</td>
</tr>
<tr>
    <td><a href="#purge_build_cache"><CopyableCode code="purge_build_cache" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a></td>
    <td></td>
    <td>Clear the build cache for a specific trigger</td>
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
<tr id="parameter-external_script_id">
    <td><CopyableCode code="external_script_id" /></td>
    <td><code>string</code></td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get all triggers for a specific worker script

```sql
SELECT
external_script_id,
build_token_name,
trigger_name,
branch_excludes,
branch_includes,
build_caching_enabled,
build_command,
build_token_uuid,
created_on,
deleted_on,
deploy_command,
modified_on,
path_excludes,
path_includes,
repo_connection,
root_directory,
trigger_uuid
FROM cloudflare.workers.triggers
WHERE account_id = '{{ account_id }}' -- required
AND external_script_id = '{{ external_script_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_trigger"
    values={[
        { label: 'create_trigger', value: 'create_trigger' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_trigger">

Create a new CI/CD trigger

```sql
INSERT INTO cloudflare.workers.triggers (
branch_excludes,
branch_includes,
build_caching_enabled,
build_command,
build_token_uuid,
deploy_command,
external_script_id,
path_excludes,
path_includes,
repo_connection_uuid,
root_directory,
trigger_name,
account_id
)
SELECT 
'{{ branch_excludes }}' /* required */,
'{{ branch_includes }}' /* required */,
{{ build_caching_enabled }},
'{{ build_command }}' /* required */,
'{{ build_token_uuid }}' /* required */,
'{{ deploy_command }}' /* required */,
'{{ external_script_id }}' /* required */,
'{{ path_excludes }}' /* required */,
'{{ path_includes }}' /* required */,
'{{ repo_connection_uuid }}' /* required */,
'{{ root_directory }}' /* required */,
'{{ trigger_name }}' /* required */,
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
- name: triggers
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the triggers resource.
    - name: branch_excludes
      value:
        - "{{ branch_excludes }}"
    - name: branch_includes
      value:
        - "{{ branch_includes }}"
    - name: build_caching_enabled
      value: {{ build_caching_enabled }}
      default: false
    - name: build_command
      value: "{{ build_command }}"
    - name: build_token_uuid
      value: "{{ build_token_uuid }}"
      description: |
        Build token UUID.
    - name: deploy_command
      value: "{{ deploy_command }}"
    - name: external_script_id
      value: "{{ external_script_id }}"
      description: |
        System-generated worker script tag.
    - name: path_excludes
      value:
        - "{{ path_excludes }}"
    - name: path_includes
      value:
        - "{{ path_includes }}"
    - name: repo_connection_uuid
      value: "{{ repo_connection_uuid }}"
      description: |
        Repository connection UUID.
    - name: root_directory
      value: "{{ root_directory }}"
      description: |
        Root directory path.
    - name: trigger_name
      value: "{{ trigger_name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_trigger"
    values={[
        { label: 'update_trigger', value: 'update_trigger' }
    ]}
>
<TabItem value="update_trigger">

Update an existing CI/CD trigger

```sql
UPDATE cloudflare.workers.triggers
SET 
branch_excludes = '{{ branch_excludes }}',
branch_includes = '{{ branch_includes }}',
build_caching_enabled = {{ build_caching_enabled }},
build_command = '{{ build_command }}',
build_token_uuid = '{{ build_token_uuid }}',
deploy_command = '{{ deploy_command }}',
path_excludes = '{{ path_excludes }}',
path_includes = '{{ path_includes }}',
root_directory = '{{ root_directory }}',
trigger_name = '{{ trigger_name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND trigger_uuid = '{{ trigger_uuid }}' --required
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
    defaultValue="delete_trigger"
    values={[
        { label: 'delete_trigger', value: 'delete_trigger' }
    ]}
>
<TabItem value="delete_trigger">

Remove a CI/CD trigger

```sql
DELETE FROM cloudflare.workers.triggers
WHERE account_id = '{{ account_id }}' --required
AND trigger_uuid = '{{ trigger_uuid }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="purge_build_cache"
    values={[
        { label: 'purge_build_cache', value: 'purge_build_cache' }
    ]}
>
<TabItem value="purge_build_cache">

Clear the build cache for a specific trigger

```sql
EXEC cloudflare.workers.triggers.purge_build_cache 
@account_id='{{ account_id }}' --required, 
@trigger_uuid='{{ trigger_uuid }}' --required
;
```
</TabItem>
</Tabs>
