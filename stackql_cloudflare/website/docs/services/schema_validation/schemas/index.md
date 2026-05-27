--- 
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - schema_validation
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schemas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.schema_validation.schemas" /></td></tr>
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
    <td>A human-readable name for the schema (example: petstore schema)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>A unique identifier of this schema (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the schema (openapi_v3) (example: openapi_v3)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The raw schema, e.g., the OpenAPI schema, either as JSON or YAML (example: &lt;schema file contents&gt;)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_enabled" /></td>
    <td><code>boolean</code></td>
    <td>An indicator if this schema is enabled</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>A human-readable name for the schema (example: petstore schema)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>A unique identifier of this schema (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the schema (openapi_v3) (example: openapi_v3)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The raw schema, e.g., the OpenAPI schema, either as JSON or YAML (example: &lt;schema file contents&gt;)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_enabled" /></td>
    <td><code>boolean</code></td>
    <td>An indicator if this schema is enabled</td>
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
    <td>Gets the contents and metadata of a specific OpenAPI schema uploaded to API Shield.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-omit_source"><code>omit_source</code></a>, <a href="#parameter-validation_enabled"><code>validation_enabled</code></a></td>
    <td>Lists all OpenAPI schemas uploaded to API Shield with pagination support.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-validation_enabled"><code>validation_enabled</code></a></td>
    <td></td>
    <td>Uploads a new OpenAPI schema for API Shield schema validation. The schema defines expected request/response formats for API endpoints.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a></td>
    <td></td>
    <td>Modifies an existing OpenAPI schema in API Shield, updating the validation rules for associated API operations.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a></td>
    <td></td>
    <td>Permanently removes an uploaded OpenAPI schema from API Shield. Operations using this schema will lose their validation rules.</td>
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
    <td>The unique identifier of the schema</td>
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
    <td>Filter for enabled schemas</td>
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

Gets the contents and metadata of a specific OpenAPI schema uploaded to API Shield.

```sql
SELECT
name,
schema_id,
created_at,
kind,
source,
validation_enabled
FROM cloudflare.schema_validation.schemas
WHERE zone_id = '{{ zone_id }}' -- required
AND schema_id = '{{ schema_id }}' -- required
AND omit_source = '{{ omit_source }}'
;
```
</TabItem>
<TabItem value="list">

Lists all OpenAPI schemas uploaded to API Shield with pagination support.

```sql
SELECT
name,
schema_id,
created_at,
kind,
source,
validation_enabled
FROM cloudflare.schema_validation.schemas
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

Uploads a new OpenAPI schema for API Shield schema validation. The schema defines expected request/response formats for API endpoints.

```sql
INSERT INTO cloudflare.schema_validation.schemas (
kind,
name,
source,
validation_enabled,
zone_id
)
SELECT 
'{{ kind }}' /* required */,
'{{ name }}' /* required */,
'{{ source }}' /* required */,
{{ validation_enabled }} /* required */,
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
- name: schemas
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the schemas resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the schema
      valid_values: ['openapi_v3']
    - name: name
      value: "{{ name }}"
      description: |
        A human-readable name for the schema
    - name: source
      value: "{{ source }}"
      description: |
        The raw schema, e.g., the OpenAPI schema, either as JSON or YAML
    - name: validation_enabled
      value: {{ validation_enabled }}
      description: |
        An indicator if this schema is enabled
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

Modifies an existing OpenAPI schema in API Shield, updating the validation rules for associated API operations.

```sql
UPDATE cloudflare.schema_validation.schemas
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

Permanently removes an uploaded OpenAPI schema from API Shield. Operations using this schema will lose their validation rules.

```sql
DELETE FROM cloudflare.schema_validation.schemas
WHERE zone_id = '{{ zone_id }}' --required
AND schema_id = '{{ schema_id }}' --required
;
```
</TabItem>
</Tabs>
