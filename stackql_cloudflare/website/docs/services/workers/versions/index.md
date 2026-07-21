--- 
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.versions" /></td></tr>
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

Get version success.

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
    <td><code>string (uuid)</code></td>
    <td>Version identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>object</code></td>
    <td>Metadata about the version.</td>
</tr>
<tr>
    <td><CopyableCode code="assets" /></td>
    <td><code>object</code></td>
    <td>Configuration for assets within a Worker. [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files should be included as modules named `_headers` and `_redirects` with content type `text/plain`.</td>
</tr>
<tr>
    <td><CopyableCode code="bindings" /></td>
    <td><code>array</code></td>
    <td>List of bindings attached to a Worker. You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_date" /></td>
    <td><code>string</code></td>
    <td>Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker. (example: 2021-01-01)</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_flags" /></td>
    <td><code>array</code></td>
    <td>Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a `compatibility_date`. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>List of containers attached to a Worker. Containers can only be attached to Durable Object classes of this Worker script. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the version was created.</td>
</tr>
<tr>
    <td><CopyableCode code="limits" /></td>
    <td><code>object</code></td>
    <td>Resource limits enforced at runtime. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="main_module" /></td>
    <td><code>string</code></td>
    <td>The name of the main module in the `modules` array (e.g. the name of the module that exports a `fetch` handler). (example: index.js)</td>
</tr>
<tr>
    <td><CopyableCode code="migration_tag" /></td>
    <td><code>string</code></td>
    <td>Durable Object migration tag. Set when the version is deployed. Omitted if the version has not been deployed or the Worker does not use Durable Objects. (example: v1)</td>
</tr>
<tr>
    <td><CopyableCode code="migrations" /></td>
    <td><code>object</code></td>
    <td>Migrations for Durable Objects associated with the version. Migrations are applied when the version is deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>Code, sourcemaps, and other content used at runtime. This includes [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files used to configure [Static Assets](https://developers.cloudflare.com/workers/static-assets/). `_headers` and `_redirects` files should be included as modules named `_headers` and `_redirects` with content type `text/plain`. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="number" /></td>
    <td><code>integer</code></td>
    <td>The integer version number, starting from one.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Configuration for [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). Specify mode='smart' for Smart Placement, or one of region/hostname/host.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The client used to create the version. (example: wrangler)</td>
</tr>
<tr>
    <td><CopyableCode code="startup_time_ms" /></td>
    <td><code>integer</code></td>
    <td>Time in milliseconds spent on [Worker startup](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).</td>
</tr>
<tr>
    <td><CopyableCode code="urls" /></td>
    <td><code>array</code></td>
    <td>All routable URLs that always point to this version. Does not include alias URLs, since aliases can be updated to point to a different version.</td>
</tr>
<tr>
    <td><CopyableCode code="usage_model" /></td>
    <td><code>string</code></td>
    <td>Usage model for the version. (standard, bundled, unbound) (default: standard, example: standard)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List versions success.

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
    <td><code>string (uuid)</code></td>
    <td>Version identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>object</code></td>
    <td>Metadata about the version.</td>
</tr>
<tr>
    <td><CopyableCode code="assets" /></td>
    <td><code>object</code></td>
    <td>Configuration for assets within a Worker. [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files should be included as modules named `_headers` and `_redirects` with content type `text/plain`.</td>
</tr>
<tr>
    <td><CopyableCode code="bindings" /></td>
    <td><code>array</code></td>
    <td>List of bindings attached to a Worker. You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_date" /></td>
    <td><code>string</code></td>
    <td>Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker. (example: 2021-01-01)</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_flags" /></td>
    <td><code>array</code></td>
    <td>Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a `compatibility_date`. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>List of containers attached to a Worker. Containers can only be attached to Durable Object classes of this Worker script. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the version was created.</td>
</tr>
<tr>
    <td><CopyableCode code="limits" /></td>
    <td><code>object</code></td>
    <td>Resource limits enforced at runtime. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="main_module" /></td>
    <td><code>string</code></td>
    <td>The name of the main module in the `modules` array (e.g. the name of the module that exports a `fetch` handler). (example: index.js)</td>
</tr>
<tr>
    <td><CopyableCode code="migration_tag" /></td>
    <td><code>string</code></td>
    <td>Durable Object migration tag. Set when the version is deployed. Omitted if the version has not been deployed or the Worker does not use Durable Objects. (example: v1)</td>
</tr>
<tr>
    <td><CopyableCode code="migrations" /></td>
    <td><code>object</code></td>
    <td>Migrations for Durable Objects associated with the version. Migrations are applied when the version is deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>Code, sourcemaps, and other content used at runtime. This includes [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files used to configure [Static Assets](https://developers.cloudflare.com/workers/static-assets/). `_headers` and `_redirects` files should be included as modules named `_headers` and `_redirects` with content type `text/plain`. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="number" /></td>
    <td><code>integer</code></td>
    <td>The integer version number, starting from one.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Configuration for [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). Specify mode='smart' for Smart Placement, or one of region/hostname/host.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The client used to create the version. (example: wrangler)</td>
</tr>
<tr>
    <td><CopyableCode code="startup_time_ms" /></td>
    <td><code>integer</code></td>
    <td>Time in milliseconds spent on [Worker startup](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).</td>
</tr>
<tr>
    <td><CopyableCode code="urls" /></td>
    <td><code>array</code></td>
    <td>All routable URLs that always point to this version. Does not include alias URLs, since aliases can be updated to point to a different version.</td>
</tr>
<tr>
    <td><CopyableCode code="usage_model" /></td>
    <td><code>string</code></td>
    <td>Usage model for the version. (standard, bundled, unbound) (default: standard, example: standard)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a></td>
    <td><a href="#parameter-include"><code>include</code></a></td>
    <td>Get details about a specific version.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List all versions for a Worker.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-worker_id"><code>worker_id</code></a></td>
    <td><a href="#parameter-deploy"><code>deploy</code></a></td>
    <td>Create a new version.</td>
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
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-worker_id">
    <td><CopyableCode code="worker_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-deploy">
    <td><CopyableCode code="deploy" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-include">
    <td><CopyableCode code="include" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Current page.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Items per-page.</td>
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

Get details about a specific version.

```sql
SELECT
id,
annotations,
assets,
bindings,
compatibility_date,
compatibility_flags,
containers,
created_on,
limits,
main_module,
migration_tag,
migrations,
modules,
number,
placement,
source,
startup_time_ms,
urls,
usage_model
FROM cloudflare.workers.versions
WHERE account_id = '{{ account_id }}' -- required
AND worker_id = '{{ worker_id }}' -- required
AND version_id = '{{ version_id }}' -- required
AND include = '{{ include }}'
;
```
</TabItem>
<TabItem value="list">

List all versions for a Worker.

```sql
SELECT
id,
annotations,
assets,
bindings,
compatibility_date,
compatibility_flags,
containers,
created_on,
limits,
main_module,
migration_tag,
migrations,
modules,
number,
placement,
source,
startup_time_ms,
urls,
usage_model
FROM cloudflare.workers.versions
WHERE account_id = '{{ account_id }}' -- required
AND worker_id = '{{ worker_id }}' -- required
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

Create a new version.

```sql
INSERT INTO cloudflare.workers.versions (
annotations,
assets,
bindings,
compatibility_date,
compatibility_flags,
containers,
limits,
main_module,
migrations,
modules,
placement,
usage_model,
account_id,
worker_id,
deploy
)
SELECT 
'{{ annotations }}',
'{{ assets }}',
'{{ bindings }}',
'{{ compatibility_date }}',
'{{ compatibility_flags }}',
'{{ containers }}',
'{{ limits }}',
'{{ main_module }}',
'{{ migrations }}',
'{{ modules }}',
'{{ placement }}',
'{{ usage_model }}',
'{{ account_id }}',
'{{ worker_id }}',
'{{ deploy }}'
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
- name: versions
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the versions resource.
    - name: worker_id
      value: "{{ worker_id }}"
      description: Required parameter for the versions resource.
    - name: annotations
      description: |
        Metadata about the version.
      value:
        workers/message: "{{ workers/message }}"
        workers/tag: "{{ workers/tag }}"
        workers/triggered_by: "{{ workers/triggered_by }}"
    - name: assets
      description: |
        Configuration for assets within a Worker. [\`_headers\`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and [\`_redirects\`](https://developers.cloudflare.com/workers/static-assets/redirects/) files should be included as modules named \`_headers\` and \`_redirects\` with content type \`text/plain\`.
      value:
        config:
          html_handling: "{{ html_handling }}"
          not_found_handling: "{{ not_found_handling }}"
          run_worker_first:
            - "{{ run_worker_first }}"
        jwt: "{{ jwt }}"
    - name: bindings
      description: |
        List of bindings attached to a Worker. You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
      value:
        - name: "{{ name }}"
          type: "{{ type }}"
          instance_name: "{{ instance_name }}"
          namespace: "{{ namespace }}"
          dataset: "{{ dataset }}"
          database_id: "{{ database_id }}"
          id: "{{ id }}"
          part: "{{ part }}"
          outbound:
            params:
              - name: "{{ name }}"
            worker:
              entrypoint: "{{ entrypoint }}"
              environment: "{{ environment }}"
              service: "{{ service }}"
          class_name: "{{ class_name }}"
          dispatch_namespace: "{{ dispatch_namespace }}"
          environment: "{{ environment }}"
          namespace_id: "{{ namespace_id }}"
          script_name: "{{ script_name }}"
          old_name: "{{ old_name }}"
          version_id: "{{ version_id }}"
          json: "{{ json }}"
          certificate_id: "{{ certificate_id }}"
          text: "{{ text }}"
          pipeline: "{{ pipeline }}"
          queue_name: "{{ queue_name }}"
          simple:
            limit: {{ limit }}
            mitigation_timeout: {{ mitigation_timeout }}
            period: {{ period }}
          bucket_name: "{{ bucket_name }}"
          jurisdiction: "{{ jurisdiction }}"
          allowed_destination_addresses: "{{ allowed_destination_addresses }}"
          allowed_sender_addresses: "{{ allowed_sender_addresses }}"
          destination_address: "{{ destination_address }}"
          entrypoint: "{{ entrypoint }}"
          service: "{{ service }}"
          index_name: "{{ index_name }}"
          secret_name: "{{ secret_name }}"
          store_id: "{{ store_id }}"
          app_id: "{{ app_id }}"
          algorithm: "{{ algorithm }}"
          format: "{{ format }}"
          key_base64: "{{ key_base64 }}"
          key_jwk: "{{ key_jwk }}"
          usages: "{{ usages }}"
          workflow_name: "{{ workflow_name }}"
          service_id: "{{ service_id }}"
          network_id: "{{ network_id }}"
          tunnel_id: "{{ tunnel_id }}"
    - name: compatibility_date
      value: "{{ compatibility_date }}"
      description: |
        Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.
    - name: compatibility_flags
      value:
        - "{{ compatibility_flags }}"
      description: |
        Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a \`compatibility_date\`.
      default: 
    - name: containers
      description: |
        List of containers attached to a Worker. Containers can only be attached to Durable Object classes of this Worker script.
      value:
        - class_name: "{{ class_name }}"
    - name: limits
      description: |
        Resource limits enforced at runtime.
      value:
        cpu_ms: {{ cpu_ms }}
        subrequests: {{ subrequests }}
    - name: main_module
      value: "{{ main_module }}"
      description: |
        The name of the main module in the \`modules\` array (e.g. the name of the module that exports a \`fetch\` handler).
    - name: migrations
      description: |
        Migrations for Durable Objects associated with the version. Migrations are applied when the version is deployed.
      value:
        new_tag: "{{ new_tag }}"
        old_tag: "{{ old_tag }}"
        deleted_classes:
          - "{{ deleted_classes }}"
        new_classes:
          - "{{ new_classes }}"
        new_sqlite_classes:
          - "{{ new_sqlite_classes }}"
        renamed_classes:
          - from: "{{ from }}"
            to: "{{ to }}"
        transferred_classes:
          - from: "{{ from }}"
            from_script: "{{ from_script }}"
            to: "{{ to }}"
        steps:
          - deleted_classes: "{{ deleted_classes }}"
            new_classes: "{{ new_classes }}"
            new_sqlite_classes: "{{ new_sqlite_classes }}"
            renamed_classes: "{{ renamed_classes }}"
            transferred_classes: "{{ transferred_classes }}"
    - name: modules
      description: |
        Code, sourcemaps, and other content used at runtime. This includes [\`_headers\`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and [\`_redirects\`](https://developers.cloudflare.com/workers/static-assets/redirects/) files used to configure [Static Assets](https://developers.cloudflare.com/workers/static-assets/). \`_headers\` and \`_redirects\` files should be included as modules named \`_headers\` and \`_redirects\` with content type \`text/plain\`.
      value:
        - content_base64: "{{ content_base64 }}"
          content_type: "{{ content_type }}"
          name: "{{ name }}"
    - name: placement
      description: |
        Configuration for [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). Specify mode='smart' for Smart Placement, or one of region/hostname/host.
      value:
        mode: "{{ mode }}"
        region: "{{ region }}"
        hostname: "{{ hostname }}"
        host: "{{ host }}"
        target:
          - region: "{{ region }}"
            hostname: "{{ hostname }}"
            host: "{{ host }}"
    - name: usage_model
      value: "{{ usage_model }}"
      description: |
        Usage model for the version.
      valid_values: ['standard', 'bundled', 'unbound']
      default: standard
    - name: deploy
      value: {{ deploy }}
`}</CodeBlock>

</TabItem>
</Tabs>
