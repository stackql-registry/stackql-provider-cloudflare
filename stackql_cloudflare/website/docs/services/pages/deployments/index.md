--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - pages
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pages.deployments" /></td></tr>
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

Get deployment info response.

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
    <td>Id of the deployment. (example: f64788e9-fccd-4d4a-a28a-cb84f88f6)</td>
</tr>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>Id of the project. (example: 7b162ea7-7367-4d67-bcde-1160995d5)</td>
</tr>
<tr>
    <td><CopyableCode code="short_id" /></td>
    <td><code>string</code></td>
    <td>Short Id (8 character) of the deployment. (example: f64788e9)</td>
</tr>
<tr>
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. (example: this-is-my-project-01)</td>
</tr>
<tr>
    <td><CopyableCode code="aliases" /></td>
    <td><code>array</code></td>
    <td>A list of alias URLs pointing to this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="build_config" /></td>
    <td><code>object</code></td>
    <td>Configs for the project build process.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the deployment was created. (example: 2021-03-09T00:55:03.923456Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_trigger" /></td>
    <td><code>object</code></td>
    <td>Info about what caused the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="env_vars" /></td>
    <td><code>object</code></td>
    <td>Environment variables used for builds and Pages Functions.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Type of deploy. (preview, production) (example: preview)</td>
</tr>
<tr>
    <td><CopyableCode code="is_skipped" /></td>
    <td><code>boolean</code></td>
    <td>If the deployment has been skipped.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_stage" /></td>
    <td><code>object</code></td>
    <td>The status of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the deployment was last modified. (example: 2021-03-09T00:58:59.045655Z)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Configs for the project source control.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>List of past stages.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The live URL to view this deployment. (example: https://f64788e9.ninjakittens.pages.dev)</td>
</tr>
<tr>
    <td><CopyableCode code="uses_functions" /></td>
    <td><code>boolean</code></td>
    <td>Whether the deployment uses functions.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get deployments response.

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
    <td>Id of the deployment. (example: f64788e9-fccd-4d4a-a28a-cb84f88f6)</td>
</tr>
<tr>
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>Id of the project. (example: 7b162ea7-7367-4d67-bcde-1160995d5)</td>
</tr>
<tr>
    <td><CopyableCode code="short_id" /></td>
    <td><code>string</code></td>
    <td>Short Id (8 character) of the deployment. (example: f64788e9)</td>
</tr>
<tr>
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. (example: this-is-my-project-01)</td>
</tr>
<tr>
    <td><CopyableCode code="aliases" /></td>
    <td><code>array</code></td>
    <td>A list of alias URLs pointing to this deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="build_config" /></td>
    <td><code>object</code></td>
    <td>Configs for the project build process.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the deployment was created. (example: 2021-03-09T00:55:03.923456Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_trigger" /></td>
    <td><code>object</code></td>
    <td>Info about what caused the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="env_vars" /></td>
    <td><code>object</code></td>
    <td>Environment variables used for builds and Pages Functions.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Type of deploy. (preview, production) (example: preview)</td>
</tr>
<tr>
    <td><CopyableCode code="is_skipped" /></td>
    <td><code>boolean</code></td>
    <td>If the deployment has been skipped.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_stage" /></td>
    <td><code>object</code></td>
    <td>The status of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the deployment was last modified. (example: 2021-03-09T00:58:59.045655Z)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Configs for the project source control.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>List of past stages.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The live URL to view this deployment. (example: https://f64788e9.ninjakittens.pages.dev)</td>
</tr>
<tr>
    <td><CopyableCode code="uses_functions" /></td>
    <td><code>boolean</code></td>
    <td>Whether the deployment uses functions.</td>
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
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch information about a deployment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-env"><code>env</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetch a list of project deployments.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Start a new deployment from production. The repository and account must have already been authorized on the Cloudflare Pages dashboard.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete a deployment.</td>
</tr>
<tr>
    <td><a href="#retry"><CopyableCode code="retry" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retry a previous deployment.</td>
</tr>
<tr>
    <td><a href="#rollback"><CopyableCode code="rollback" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Rollback the production deployment to a previous deployment. You can only rollback to succesful builds on production.</td>
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
<tr id="parameter-deployment_id">
    <td><CopyableCode code="deployment_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The Pages project name.</td>
</tr>
<tr id="parameter-env">
    <td><CopyableCode code="env" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td></td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Fetch information about a deployment.

```sql
SELECT
id,
project_id,
short_id,
project_name,
aliases,
build_config,
created_on,
deployment_trigger,
env_vars,
environment,
is_skipped,
latest_stage,
modified_on,
source,
stages,
url,
uses_functions
FROM cloudflare.pages.deployments
WHERE deployment_id = '{{ deployment_id }}' -- required
AND project_name = '{{ project_name }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetch a list of project deployments.

```sql
SELECT
id,
project_id,
short_id,
project_name,
aliases,
build_config,
created_on,
deployment_trigger,
env_vars,
environment,
is_skipped,
latest_stage,
modified_on,
source,
stages,
url,
uses_functions
FROM cloudflare.pages.deployments
WHERE project_name = '{{ project_name }}' -- required
AND account_id = '{{ account_id }}' -- required
AND env = '{{ env }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Start a new deployment from production. The repository and account must have already been authorized on the Cloudflare Pages dashboard.

```sql
INSERT INTO cloudflare.pages.deployments (
_headers,
_redirects,
_routes.json,
_worker.bundle,
_worker.js,
branch,
commit_dirty,
commit_hash,
commit_message,
functions-filepath-routing-config.json,
manifest,
pages_build_output_dir,
wrangler_config_hash,
project_name,
account_id
)
SELECT 
'{{ _headers }}',
'{{ _redirects }}',
'{{ _routes.json }}',
'{{ _worker.bundle }}',
'{{ _worker.js }}',
'{{ branch }}',
'{{ commit_dirty }}',
'{{ commit_hash }}',
'{{ commit_message }}',
'{{ functions-filepath-routing-config.json }}',
'{{ manifest }}',
'{{ pages_build_output_dir }}',
'{{ wrangler_config_hash }}',
'{{ project_name }}',
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
- name: deployments
  props:
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the deployments resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the deployments resource.
    - name: _headers
      value: "{{ _headers }}"
      description: |
        Headers configuration file for the deployment.
    - name: _redirects
      value: "{{ _redirects }}"
      description: |
        Redirects configuration file for the deployment.
    - name: _routes.json
      value: "{{ _routes.json }}"
      description: |
        Routes configuration file defining routing rules.
    - name: _worker.bundle
      value: "{{ _worker.bundle }}"
      description: |
        Worker bundle file in multipart/form-data format. Mutually exclusive with \`_worker.js\`. Cannot specify both \`_worker.js\` and \`_worker.bundle\` in the same request. Maximum size: 25 MiB.
    - name: _worker.js
      value: "{{ _worker.js }}"
      description: |
        Worker JavaScript file. Mutually exclusive with \`_worker.bundle\`. Cannot specify both \`_worker.js\` and \`_worker.bundle\` in the same request.
    - name: branch
      value: "{{ branch }}"
      description: |
        The branch to build the new deployment from. The \`HEAD\` of the branch will be used. If omitted, the production branch will be used by default.
    - name: commit_dirty
      value: "{{ commit_dirty }}"
      description: |
        Boolean string indicating if the working directory has uncommitted changes.
      valid_values: ['true', 'false']
    - name: commit_hash
      value: "{{ commit_hash }}"
      description: |
        Git commit SHA associated with this deployment.
    - name: commit_message
      value: "{{ commit_message }}"
      description: |
        Git commit message associated with this deployment.
    - name: functions-filepath-routing-config.json
      value: "{{ functions-filepath-routing-config.json }}"
      description: |
        Functions routing configuration file.
    - name: manifest
      value: "{{ manifest }}"
      description: |
        JSON string containing a manifest of files to deploy. Maps file paths to their content hashes. Required for direct upload deployments. Maximum 20,000 entries.
    - name: pages_build_output_dir
      value: "{{ pages_build_output_dir }}"
      description: |
        The build output directory path.
    - name: wrangler_config_hash
      value: "{{ wrangler_config_hash }}"
      description: |
        Hash of the Wrangler configuration file used for this deployment.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a deployment.

```sql
DELETE FROM cloudflare.pages.deployments
WHERE deployment_id = '{{ deployment_id }}' --required
AND project_name = '{{ project_name }}' --required
AND account_id = '{{ account_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="retry"
    values={[
        { label: 'retry', value: 'retry' },
        { label: 'rollback', value: 'rollback' }
    ]}
>
<TabItem value="retry">

Retry a previous deployment.

```sql
EXEC cloudflare.pages.deployments.retry 
@deployment_id='{{ deployment_id }}' --required, 
@project_name='{{ project_name }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="rollback">

Rollback the production deployment to a previous deployment. You can only rollback to succesful builds on production.

```sql
EXEC cloudflare.pages.deployments.rollback 
@deployment_id='{{ deployment_id }}' --required, 
@project_name='{{ project_name }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
