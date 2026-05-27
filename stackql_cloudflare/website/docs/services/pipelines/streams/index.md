--- 
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - pipelines
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

Creates, updates, deletes, gets or lists a <code>streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="streams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pipelines.streams" /></td></tr>
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

Indicates a successfully retrieved Stream.

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
    <td>Indicates a unique identifier for this stream.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Indicates the name of the Stream.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string (uri)</code></td>
    <td>Indicates the endpoint URL of this stream.</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>object</code></td>
    <td> (title: Json)</td>
</tr>
<tr>
    <td><CopyableCode code="http" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>Indicates the current version of this stream.</td>
</tr>
<tr>
    <td><CopyableCode code="worker_binding" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Indicates a successfully created Stream.

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
    <td>Indicates a unique identifier for this stream.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Indicates the name of the Stream.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string (uri)</code></td>
    <td>Indicates the endpoint URL of this stream.</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>object</code></td>
    <td> (title: Json)</td>
</tr>
<tr>
    <td><CopyableCode code="http" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>Indicates the current version of this stream.</td>
</tr>
<tr>
    <td><CopyableCode code="worker_binding" /></td>
    <td><code>object</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-stream_id"><code>stream_id</code></a></td>
    <td></td>
    <td>Get Stream Details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List/Filter Streams in Account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a new Stream.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-stream_id"><code>stream_id</code></a></td>
    <td></td>
    <td>Update a Stream.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-stream_id"><code>stream_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete Stream in Account.</td>
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
<tr id="parameter-stream_id">
    <td><CopyableCode code="stream_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-pipeline_id">
    <td><CopyableCode code="pipeline_id" /></td>
    <td><code>string</code></td>
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

Get Stream Details.

```sql
SELECT
id,
name,
created_at,
endpoint,
format,
http,
modified_at,
schema,
version,
worker_binding
FROM cloudflare.pipelines.streams
WHERE account_id = '{{ account_id }}' -- required
AND stream_id = '{{ stream_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List/Filter Streams in Account.

```sql
SELECT
id,
name,
created_at,
endpoint,
format,
http,
modified_at,
schema,
version,
worker_binding
FROM cloudflare.pipelines.streams
WHERE account_id = '{{ account_id }}' -- required
AND pipeline_id = '{{ pipeline_id }}'
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

Create a new Stream.

```sql
INSERT INTO cloudflare.pipelines.streams (
format,
http,
name,
schema,
worker_binding,
account_id
)
SELECT 
'{{ format }}',
'{{ http }}',
'{{ name }}' /* required */,
'{{ schema }}',
'{{ worker_binding }}',
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: streams
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the streams resource.
    - name: format
      value:
        decimal_encoding: "{{ decimal_encoding }}"
        timestamp_format: "{{ timestamp_format }}"
        unstructured: {{ unstructured }}
        type: "{{ type }}"
        compression: "{{ compression }}"
        row_group_bytes: {{ row_group_bytes }}
    - name: http
      value:
        authentication: {{ authentication }}
        cors:
          origins:
            - "{{ origins }}"
        enabled: {{ enabled }}
      default: [object Object]
    - name: name
      value: "{{ name }}"
      description: |
        Specifies the name of the Stream.
    - name: schema
      value:
        fields:
          - metadata_key: "{{ metadata_key }}"
            name: "{{ name }}"
            sql_name: "{{ sql_name }}"
            type: "{{ type }}"
            unit: "{{ unit }}"
            fields: "{{ fields }}"
            items:
              metadata_key: "{{ metadata_key }}"
              name: "{{ name }}"
              sql_name: "{{ sql_name }}"
              type: "{{ type }}"
              unit: "{{ unit }}"
              fields:
                - metadata_key: "{{ metadata_key }}"
                  name: "{{ name }}"
                  sql_name: "{{ sql_name }}"
                  type: "{{ type }}"
                  unit: "{{ unit }}"
                  fields: "{{ fields }}"
                  items:
                    metadata_key: "{{ metadata_key }}"
                    name: "{{ name }}"
                    sql_name: "{{ sql_name }}"
                    type: "{{ type }}"
                    unit: "{{ unit }}"
                    fields: "{{ fields }}"
                    items: "{{ items }}"
              items:
                metadata_key: "{{ metadata_key }}"
                name: "{{ name }}"
                sql_name: "{{ sql_name }}"
                type: "{{ type }}"
                unit: "{{ unit }}"
                fields:
                  - metadata_key: "{{ metadata_key }}"
                    name: "{{ name }}"
                    sql_name: "{{ sql_name }}"
                    type: "{{ type }}"
                    unit: "{{ unit }}"
                    fields: "{{ fields }}"
                    items:
                      metadata_key: "{{ metadata_key }}"
                      name: "{{ name }}"
                      sql_name: "{{ sql_name }}"
                      type: "{{ type }}"
                      unit: "{{ unit }}"
                      fields: "{{ fields }}"
                      items: "{{ items }}"
                items:
                  metadata_key: "{{ metadata_key }}"
                  name: "{{ name }}"
                  sql_name: "{{ sql_name }}"
                  type: "{{ type }}"
                  unit: "{{ unit }}"
                  fields: "{{ fields }}"
                  items: "{{ items }}"
        format:
          decimal_encoding: "{{ decimal_encoding }}"
          timestamp_format: "{{ timestamp_format }}"
          unstructured: {{ unstructured }}
          type: "{{ type }}"
          compression: "{{ compression }}"
          row_group_bytes: {{ row_group_bytes }}
        inferred: {{ inferred }}
    - name: worker_binding
      value:
        enabled: {{ enabled }}
      default: [object Object]
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update a Stream.

```sql
UPDATE cloudflare.pipelines.streams
SET 
http = '{{ http }}',
worker_binding = '{{ worker_binding }}'
WHERE 
account_id = '{{ account_id }}' --required
AND stream_id = '{{ stream_id }}' --required
RETURNING
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

Delete Stream in Account.

```sql
DELETE FROM cloudflare.pipelines.streams
WHERE account_id = '{{ account_id }}' --required
AND stream_id = '{{ stream_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
