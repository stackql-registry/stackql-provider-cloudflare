--- 
title: database_query
hide_title: false
hide_table_of_contents: false
keywords:
  - database_query
  - d1
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

Creates, updates, deletes, gets or lists a <code>database_query</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_query" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.d1.database_query" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td></td>
    <td>Returns the query result as an object.</td>
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
<tr id="parameter-database_id">
    <td><CopyableCode code="database_id" /></td>
    <td><code>string</code></td>
    <td>The D1 database ID.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="query">

Returns the query result as an object.

```sql
INSERT INTO cloudflare.d1.database_query (
params,
sql,
batch,
account_id,
database_id
)
SELECT 
'{{ params }}',
'{{ sql }}',
'{{ batch }}',
'{{ account_id }}',
'{{ database_id }}'
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
- name: database_query
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the database_query resource.
    - name: database_id
      value: "{{ database_id }}"
      description: Required parameter for the database_query resource.
    - name: params
      value:
        - "{{ params }}"
    - name: sql
      value: "{{ sql }}"
      description: |
        Your SQL query. Supports multiple statements, joined by semicolons, which will be executed as a batch.
    - name: batch
      value:
        - params: "{{ params }}"
          sql: "{{ sql }}"
`}</CodeBlock>

</TabItem>
</Tabs>
