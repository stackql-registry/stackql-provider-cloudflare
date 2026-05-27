--- 
title: scripts_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts_versions
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

Creates, updates, deletes, gets or lists a <code>scripts_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scripts_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.scripts_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get_by_account">

Get Version Detail response.

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
    <td>Unique identifier for the version. (example: 18f97339-c287-4872-9bdd-e2135c07ec12)</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="number" /></td>
    <td><code>number</code></td>
    <td>Sequential version number.</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List Versions response.

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
    <td>Unique identifier for the version. (example: 18f97339-c287-4872-9bdd-e2135c07ec12)</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="number" /></td>
    <td><code>number</code></td>
    <td>Sequential version number.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-version_id"><code>version_id</code></a></td>
    <td></td>
    <td>Retrieves detailed information about a specific version of a Workers script.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td><a href="#parameter-deployable"><code>deployable</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List of Worker Versions. The first version in the list is the latest version.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-metadata"><code>metadata</code></a></td>
    <td><a href="#parameter-bindings_inherit"><code>bindings_inherit</code></a></td>
    <td>Upload a Worker Version without deploying to Cloudflare's network. You can find more about the multipart metadata on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.</td>
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
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
</tr>
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-bindings_inherit">
    <td><CopyableCode code="bindings_inherit" /></td>
    <td><code>string</code></td>
    <td>When set to "strict", the upload will fail if any `inherit` type bindings cannot be resolved against the previous version of the Worker. Without this, unresolvable inherit bindings are silently dropped.</td>
</tr>
<tr id="parameter-deployable">
    <td><CopyableCode code="deployable" /></td>
    <td><code>boolean</code></td>
    <td>Only return versions that can be used in a deployment. Ignores pagination.</td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get_by_account">

Retrieves detailed information about a specific version of a Workers script.

```sql
SELECT
id,
metadata,
number,
resources
FROM cloudflare.workers.scripts_versions
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
AND version_id = '{{ version_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

List of Worker Versions. The first version in the list is the latest version.

```sql
SELECT
id,
metadata,
number
FROM cloudflare.workers.scripts_versions
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
AND deployable = '{{ deployable }}'
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

Upload a Worker Version without deploying to Cloudflare's network. You can find more about the multipart metadata on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.

```sql
INSERT INTO cloudflare.workers.scripts_versions (
files,
metadata,
account_id,
script_name,
bindings_inherit
)
SELECT 
'{{ files }}',
'{{ metadata }}' /* required */,
'{{ account_id }}',
'{{ script_name }}',
'{{ bindings_inherit }}'
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
- name: scripts_versions
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the scripts_versions resource.
    - name: script_name
      value: "{{ script_name }}"
      description: Required parameter for the scripts_versions resource.
    - name: files
      value:
        - "{{ files }}"
      description: |
        An array of modules (often JavaScript files) comprising a Worker script. At least one module must be present and referenced in the metadata as \`main_module\` or \`body_part\` by filename.<br/>Possible Content-Type(s) are: \`application/javascript+module\`, \`text/javascript+module\`, \`application/javascript\`, \`text/javascript\`, \`text/x-python\`, \`text/x-python-requirement\`, \`application/wasm\`, \`text/plain\`, \`application/octet-stream\`, \`application/source-map\`.
    - name: metadata
      description: |
        JSON-encoded metadata about the uploaded parts and Worker configuration.
      value:
        annotations:
          workers/alias: "{{ workers/alias }}"
          workers/message: "{{ workers/message }}"
          workers/tag: "{{ workers/tag }}"
        bindings:
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
        compatibility_date: "{{ compatibility_date }}"
        compatibility_flags:
          - "{{ compatibility_flags }}"
        keep_bindings:
          - "{{ keep_bindings }}"
        main_module: "{{ main_module }}"
        usage_model: "{{ usage_model }}"
    - name: bindings_inherit
      value: "{{ bindings_inherit }}"
      description: When set to "strict", the upload will fail if any \`inherit\` type bindings cannot be resolved against the previous version of the Worker. Without this, unresolvable inherit bindings are silently dropped.
      description: When set to "strict", the upload will fail if any \`inherit\` type bindings cannot be resolved against the previous version of the Worker. Without this, unresolvable inherit bindings are silently dropped.
`}</CodeBlock>

</TabItem>
</Tabs>
