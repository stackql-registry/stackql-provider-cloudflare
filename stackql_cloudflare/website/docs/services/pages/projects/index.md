--- 
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="projects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pages.projects" /></td></tr>
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

Get project response.

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
    <td>ID of the project. (example: 7b162ea7-7367-4d67-bcde-1160995d5)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. (example: this-is-my-project-01)</td>
</tr>
<tr>
    <td><CopyableCode code="preview_script_name" /></td>
    <td><code>string</code></td>
    <td>Name of the preview script. (example: pages-worker--1234567-preview)</td>
</tr>
<tr>
    <td><CopyableCode code="production_script_name" /></td>
    <td><code>string</code></td>
    <td>Name of the production script. (example: pages-worker--1234567-production)</td>
</tr>
<tr>
    <td><CopyableCode code="build_config" /></td>
    <td><code>object</code></td>
    <td>Configs for the project build process.</td>
</tr>
<tr>
    <td><CopyableCode code="canonical_deployment" /></td>
    <td><code>object</code></td>
    <td>Most recent production deployment of the project.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the project was created. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_configs" /></td>
    <td><code>object</code></td>
    <td>Configs for deployments in a project.</td>
</tr>
<tr>
    <td><CopyableCode code="domains" /></td>
    <td><code>array</code></td>
    <td>A list of associated custom domains for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="framework" /></td>
    <td><code>string</code></td>
    <td>Framework the project is using.</td>
</tr>
<tr>
    <td><CopyableCode code="framework_version" /></td>
    <td><code>string</code></td>
    <td>Version of the framework the project is using.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_deployment" /></td>
    <td><code>object</code></td>
    <td>Most recent deployment of the project.</td>
</tr>
<tr>
    <td><CopyableCode code="production_branch" /></td>
    <td><code>string</code></td>
    <td>Production branch of the project. Used to identify production deployments. (example: main)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Configs for the project source control.</td>
</tr>
<tr>
    <td><CopyableCode code="subdomain" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare subdomain associated with the project. (example: helloworld.pages.dev)</td>
</tr>
<tr>
    <td><CopyableCode code="uses_functions" /></td>
    <td><code>boolean</code></td>
    <td>Whether the project uses functions.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get projects response.

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
    <td>ID of the project. (example: 7b162ea7-7367-4d67-bcde-1160995d5)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the project. (example: this-is-my-project-01)</td>
</tr>
<tr>
    <td><CopyableCode code="preview_script_name" /></td>
    <td><code>string</code></td>
    <td>Name of the preview script. (example: pages-worker--1234567-preview)</td>
</tr>
<tr>
    <td><CopyableCode code="production_script_name" /></td>
    <td><code>string</code></td>
    <td>Name of the production script. (example: pages-worker--1234567-production)</td>
</tr>
<tr>
    <td><CopyableCode code="build_config" /></td>
    <td><code>object</code></td>
    <td>Configs for the project build process.</td>
</tr>
<tr>
    <td><CopyableCode code="canonical_deployment" /></td>
    <td><code>object</code></td>
    <td>Most recent production deployment of the project.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the project was created. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deployment_configs" /></td>
    <td><code>object</code></td>
    <td>Configs for deployments in a project.</td>
</tr>
<tr>
    <td><CopyableCode code="domains" /></td>
    <td><code>array</code></td>
    <td>A list of associated custom domains for the project.</td>
</tr>
<tr>
    <td><CopyableCode code="framework" /></td>
    <td><code>string</code></td>
    <td>Framework the project is using.</td>
</tr>
<tr>
    <td><CopyableCode code="framework_version" /></td>
    <td><code>string</code></td>
    <td>Version of the framework the project is using.</td>
</tr>
<tr>
    <td><CopyableCode code="latest_deployment" /></td>
    <td><code>object</code></td>
    <td>Most recent deployment of the project.</td>
</tr>
<tr>
    <td><CopyableCode code="production_branch" /></td>
    <td><code>string</code></td>
    <td>Production branch of the project. Used to identify production deployments. (example: main)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Configs for the project source control.</td>
</tr>
<tr>
    <td><CopyableCode code="subdomain" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare subdomain associated with the project. (example: helloworld.pages.dev)</td>
</tr>
<tr>
    <td><CopyableCode code="uses_functions" /></td>
    <td><code>boolean</code></td>
    <td>Whether the project uses functions.</td>
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
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch a project by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetch a list of all user projects.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-production_branch"><code>production_branch</code></a></td>
    <td></td>
    <td>Create a new project.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Set new attributes for an existing project. Modify environment variables. To delete an environment variable, set the key to null.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a project by name.</td>
</tr>
<tr>
    <td><a href="#purge_build_cache"><CopyableCode code="purge_build_cache" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Purge all cached build artifacts for a Pages project</td>
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
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>The Pages project name.</td>
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

Fetch a project by name.

```sql
SELECT
id,
name,
preview_script_name,
production_script_name,
build_config,
canonical_deployment,
created_on,
deployment_configs,
domains,
framework,
framework_version,
latest_deployment,
production_branch,
source,
subdomain,
uses_functions
FROM cloudflare.pages.projects
WHERE project_name = '{{ project_name }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetch a list of all user projects.

```sql
SELECT
id,
name,
preview_script_name,
production_script_name,
build_config,
canonical_deployment,
created_on,
deployment_configs,
domains,
framework,
framework_version,
latest_deployment,
production_branch,
source,
subdomain,
uses_functions
FROM cloudflare.pages.projects
WHERE account_id = '{{ account_id }}' -- required
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

Create a new project.

```sql
INSERT INTO cloudflare.pages.projects (
build_config,
deployment_configs,
name,
production_branch,
source,
account_id
)
SELECT 
'{{ build_config }}',
'{{ deployment_configs }}',
'{{ name }}' /* required */,
'{{ production_branch }}' /* required */,
'{{ source }}',
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
- name: projects
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the projects resource.
    - name: build_config
      description: |
        Configs for the project build process.
      value:
        build_caching: {{ build_caching }}
        build_command: "{{ build_command }}"
        destination_dir: "{{ destination_dir }}"
        root_dir: "{{ root_dir }}"
        web_analytics_tag: "{{ web_analytics_tag }}"
        web_analytics_token: "{{ web_analytics_token }}"
    - name: deployment_configs
      description: |
        Configs for deployments in a project.
      value:
        preview:
          ai_bindings: "{{ ai_bindings }}"
          always_use_latest_compatibility_date: {{ always_use_latest_compatibility_date }}
          analytics_engine_datasets: "{{ analytics_engine_datasets }}"
          browsers: "{{ browsers }}"
          build_image_major_version: {{ build_image_major_version }}
          compatibility_date: "{{ compatibility_date }}"
          compatibility_flags:
            - "{{ compatibility_flags }}"
          d1_databases: "{{ d1_databases }}"
          durable_object_namespaces: "{{ durable_object_namespaces }}"
          env_vars: "{{ env_vars }}"
          fail_open: {{ fail_open }}
          hyperdrive_bindings: "{{ hyperdrive_bindings }}"
          kv_namespaces: "{{ kv_namespaces }}"
          limits:
            cpu_ms: {{ cpu_ms }}
          mtls_certificates: "{{ mtls_certificates }}"
          placement:
            mode: "{{ mode }}"
          queue_producers: "{{ queue_producers }}"
          r2_buckets: "{{ r2_buckets }}"
          services: "{{ services }}"
          usage_model: "{{ usage_model }}"
          vectorize_bindings: "{{ vectorize_bindings }}"
          wrangler_config_hash: "{{ wrangler_config_hash }}"
        production:
          ai_bindings: "{{ ai_bindings }}"
          always_use_latest_compatibility_date: {{ always_use_latest_compatibility_date }}
          analytics_engine_datasets: "{{ analytics_engine_datasets }}"
          browsers: "{{ browsers }}"
          build_image_major_version: {{ build_image_major_version }}
          compatibility_date: "{{ compatibility_date }}"
          compatibility_flags:
            - "{{ compatibility_flags }}"
          d1_databases: "{{ d1_databases }}"
          durable_object_namespaces: "{{ durable_object_namespaces }}"
          env_vars: "{{ env_vars }}"
          fail_open: {{ fail_open }}
          hyperdrive_bindings: "{{ hyperdrive_bindings }}"
          kv_namespaces: "{{ kv_namespaces }}"
          limits:
            cpu_ms: {{ cpu_ms }}
          mtls_certificates: "{{ mtls_certificates }}"
          placement:
            mode: "{{ mode }}"
          queue_producers: "{{ queue_producers }}"
          r2_buckets: "{{ r2_buckets }}"
          services: "{{ services }}"
          usage_model: "{{ usage_model }}"
          vectorize_bindings: "{{ vectorize_bindings }}"
          wrangler_config_hash: "{{ wrangler_config_hash }}"
    - name: name
      value: "{{ name }}"
      description: |
        Name of the project.
    - name: production_branch
      value: "{{ production_branch }}"
      description: |
        Production branch of the project. Used to identify production deployments.
    - name: source
      description: |
        Configs for the project source control.
      value:
        config:
          deployments_enabled: {{ deployments_enabled }}
          owner: "{{ owner }}"
          owner_id: "{{ owner_id }}"
          path_excludes:
            - "{{ path_excludes }}"
          path_includes:
            - "{{ path_includes }}"
          pr_comments_enabled: {{ pr_comments_enabled }}
          preview_branch_excludes:
            - "{{ preview_branch_excludes }}"
          preview_branch_includes:
            - "{{ preview_branch_includes }}"
          preview_deployment_setting: "{{ preview_deployment_setting }}"
          production_branch: "{{ production_branch }}"
          production_deployments_enabled: {{ production_deployments_enabled }}
          repo_id: "{{ repo_id }}"
          repo_name: "{{ repo_name }}"
        type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Set new attributes for an existing project. Modify environment variables. To delete an environment variable, set the key to null.

```sql
UPDATE cloudflare.pages.projects
SET 
build_config = '{{ build_config }}',
deployment_configs = '{{ deployment_configs }}',
name = '{{ name }}',
production_branch = '{{ production_branch }}',
source = '{{ source }}'
WHERE 
project_name = '{{ project_name }}' --required
AND account_id = '{{ account_id }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a project by name.

```sql
DELETE FROM cloudflare.pages.projects
WHERE project_name = '{{ project_name }}' --required
AND account_id = '{{ account_id }}' --required
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

Purge all cached build artifacts for a Pages project

```sql
EXEC cloudflare.pages.projects.purge_build_cache 
@project_name='{{ project_name }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
