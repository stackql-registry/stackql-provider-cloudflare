--- 
title: sinks
hide_title: false
hide_table_of_contents: false
keywords:
  - sinks
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

Creates, updates, deletes, gets or lists a <code>sinks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sinks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pipelines.sinks" /></td></tr>
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

Indicates that Sink was retrieved.

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
    <td>Indicates a unique identifier for this sink.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Defines the name of the Sink.</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>Defines the configuration of the R2 Sink. (title: R2 Sink Public)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>object</code></td>
    <td> (title: Json)</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of sink. (r2, r2_data_catalog)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Indicates successfully listed Sinks.

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
    <td>Indicates a unique identifier for this sink.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Defines the name of the Sink.</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>Defines the configuration of the R2 Sink. (title: R2 Sink Public)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>object</code></td>
    <td> (title: Json)</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of sink. (r2, r2_data_catalog)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sink_id"><code>sink_id</code></a></td>
    <td></td>
    <td>Get Sink Details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-pipeline_id"><code>pipeline_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List/Filter Sinks in Account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create a new Sink.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sink_id"><code>sink_id</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete Pipeline in Account.</td>
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
<tr id="parameter-sink_id">
    <td><CopyableCode code="sink_id" /></td>
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

Get Sink Details.

```sql
SELECT
id,
name,
config,
created_at,
format,
modified_at,
schema,
type
FROM cloudflare.pipelines.sinks
WHERE account_id = '{{ account_id }}' -- required
AND sink_id = '{{ sink_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List/Filter Sinks in Account.

```sql
SELECT
id,
name,
config,
created_at,
format,
modified_at,
schema,
type
FROM cloudflare.pipelines.sinks
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

Create a new Sink.

```sql
INSERT INTO cloudflare.pipelines.sinks (
config,
format,
name,
schema,
type,
account_id
)
SELECT 
'{{ config }}',
'{{ format }}',
'{{ name }}' /* required */,
'{{ schema }}',
'{{ type }}' /* required */,
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sinks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the sinks resource.
    - name: config
      description: |
        Defines the configuration of the R2 Sink.
      value:
        account_id: "{{ account_id }}"
        bucket: "{{ bucket }}"
        credentials:
          access_key_id: "{{ access_key_id }}"
          secret_access_key: "{{ secret_access_key }}"
        file_naming:
          prefix: "{{ prefix }}"
          strategy: "{{ strategy }}"
          suffix: "{{ suffix }}"
        jurisdiction: "{{ jurisdiction }}"
        partitioning:
          time_pattern: "{{ time_pattern }}"
        path: "{{ path }}"
        rolling_policy:
          file_size_bytes: {{ file_size_bytes }}
          inactivity_seconds: {{ inactivity_seconds }}
          interval_seconds: {{ interval_seconds }}
        namespace: "{{ namespace }}"
        table_name: "{{ table_name }}"
        token: "{{ token }}"
    - name: format
      value:
        decimal_encoding: "{{ decimal_encoding }}"
        timestamp_format: "{{ timestamp_format }}"
        unstructured: {{ unstructured }}
        type: "{{ type }}"
        compression: "{{ compression }}"
        row_group_bytes: {{ row_group_bytes }}
    - name: name
      value: "{{ name }}"
      description: |
        Defines the name of the Sink.
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
    - name: type
      value: "{{ type }}"
      description: |
        Specifies the type of sink.
      valid_values: ['r2', 'r2_data_catalog']
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

Delete Pipeline in Account.

```sql
DELETE FROM cloudflare.pipelines.sinks
WHERE account_id = '{{ account_id }}' --required
AND sink_id = '{{ sink_id }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
