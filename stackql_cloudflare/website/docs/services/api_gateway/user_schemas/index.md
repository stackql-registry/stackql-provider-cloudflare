--- 
title: user_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - user_schemas
  - api_gateway
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

Creates, updates, deletes, gets or lists a <code>user_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_schemas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.user_schemas" /></td></tr>
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

Retrieve information about a specific schema on a zone response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the schema (example: petstore schema)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_id" /></td>
    <td><code>string</code></td>
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of schema (openapi_v3) (example: openapi_v3)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the schema (example: &lt;schema file bytes&gt;)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag whether schema is enabled for validation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Retrieve information about all schemas on a zone response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the schema (example: petstore schema)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_id" /></td>
    <td><code>string</code></td>
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of schema (openapi_v3) (example: openapi_v3)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the schema (example: &lt;schema file bytes&gt;)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag whether schema is enabled for validation.</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a></td>
    <td><a href="#parameter-omit_source"><code>omit_source</code></a></td>
    <td>Gets detailed information about a specific uploaded OpenAPI schema, including its contents and validation configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-omit_source"><code>omit_source</code></a>, <a href="#parameter-validation_enabled"><code>validation_enabled</code></a></td>
    <td>Lists all OpenAPI schemas uploaded to API Shield for the zone, including their validation status and associated operations.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-file"><code>file</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a></td>
    <td></td>
    <td>Activates schema validation for an uploaded OpenAPI schema. Requests to matching endpoints will be validated against the schema definitions.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a></td>
    <td></td>
    <td>Permanently removes an uploaded OpenAPI schema from API Shield schema validation. Operations using this schema will lose their validation rules.</td>
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
<tr id="parameter-schema_id">
    <td><CopyableCode code="schema_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Identifier for the schema-ID</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-omit_source">
    <td><CopyableCode code="omit_source" /></td>
    <td><code>boolean</code></td>
    <td>Omit the source-files of schemas and only retrieve their meta-data.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number of paginated results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results per page.</td>
</tr>
<tr id="parameter-validation_enabled">
    <td><CopyableCode code="validation_enabled" /></td>
    <td><code>boolean</code></td>
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

Gets detailed information about a specific uploaded OpenAPI schema, including its contents and validation configuration.

```sql
SELECT
name,
schema_id,
created_at,
kind,
source,
validation_enabled
FROM cloudflare.api_gateway.user_schemas
WHERE zone_id = '{{ zone_id }}' -- required
AND schema_id = '{{ schema_id }}' -- required
AND omit_source = '{{ omit_source }}'
;
```
</TabItem>
<TabItem value="list">

Lists all OpenAPI schemas uploaded to API Shield for the zone, including their validation status and associated operations.

```sql
SELECT
name,
schema_id,
created_at,
kind,
source,
validation_enabled
FROM cloudflare.api_gateway.user_schemas
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND omit_source = '{{ omit_source }}'
AND validation_enabled = '{{ validation_enabled }}'
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

No description available.

```sql
INSERT INTO cloudflare.api_gateway.user_schemas (
file,
kind,
name,
validation_enabled,
zone_id
)
SELECT 
'{{ file }}' /* required */,
'{{ kind }}' /* required */,
'{{ name }}',
'{{ validation_enabled }}',
'{{ zone_id }}'
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
- name: user_schemas
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the user_schemas resource.
    - name: file
      value: "{{ file }}"
      description: |
        Schema file bytes
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of schema
      valid_values: ['openapi_v3']
    - name: name
      value: "{{ name }}"
      description: |
        Name of the schema
    - name: validation_enabled
      value: "{{ validation_enabled }}"
      description: |
        Flag whether schema is enabled for validation.
      valid_values: ['true', 'false']
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

Activates schema validation for an uploaded OpenAPI schema. Requests to matching endpoints will be validated against the schema definitions.

```sql
UPDATE cloudflare.api_gateway.user_schemas
SET 
validation_enabled = {{ validation_enabled }}
WHERE 
zone_id = '{{ zone_id }}' --required
AND schema_id = '{{ schema_id }}' --required
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

Permanently removes an uploaded OpenAPI schema from API Shield schema validation. Operations using this schema will lose their validation rules.

```sql
DELETE FROM cloudflare.api_gateway.user_schemas
WHERE zone_id = '{{ zone_id }}' --required
AND schema_id = '{{ schema_id }}' --required
;
```
</TabItem>
</Tabs>
