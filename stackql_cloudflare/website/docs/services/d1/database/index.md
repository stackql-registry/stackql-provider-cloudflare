--- 
title: database
hide_title: false
hide_table_of_contents: false
keywords:
  - database
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

Creates, updates, deletes, gets or lists a <code>database</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.d1.database" /></td></tr>
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

Database details response

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
    <td>D1 database name. (example: my-database)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the timestamp the resource was created as an ISO8601 string. (example: 2022-11-15T18:25:44.442097Z)</td>
</tr>
<tr>
    <td><CopyableCode code="file_size" /></td>
    <td><code>number</code></td>
    <td>The D1 database's size, in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="jurisdiction" /></td>
    <td><code>string</code></td>
    <td>Specify the location to restrict the D1 database to run and store data. If this option is present, the location hint is ignored. (eu, fedramp) (example: eu)</td>
</tr>
<tr>
    <td><CopyableCode code="num_tables" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="read_replication" /></td>
    <td><code>object</code></td>
    <td>Configuration for D1 read replication.</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>D1 database identifier (UUID). (example: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td> (example: production)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List D1 databases response

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
    <td>D1 database name. (example: my-database)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the timestamp the resource was created as an ISO8601 string. (example: 2022-11-15T18:25:44.442097Z)</td>
</tr>
<tr>
    <td><CopyableCode code="jurisdiction" /></td>
    <td><code>string</code></td>
    <td>Specify the location to restrict the D1 database to run and store data. If this option is present, the location hint is ignored. (eu, fedramp) (example: eu)</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string</code></td>
    <td>D1 database identifier (UUID). (example: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td> (example: production)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td></td>
    <td>Returns the specified D1 database.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Returns a list of D1 databases.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Returns the created D1 database.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td></td>
    <td>Updates partially the specified D1 database.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-read_replication"><code>read_replication</code></a></td>
    <td></td>
    <td>Updates the specified D1 database.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td></td>
    <td>Deletes the specified D1 database.</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-output_format"><code>output_format</code></a></td>
    <td></td>
    <td>Returns a URL where the SQL contents of your D1 can be downloaded. Note: this process may take some time for larger DBs, during which your D1 will be unavailable to serve queries. To avoid blocking your DB unnecessarily, an in-progress export must be continually polled or will automatically cancel.</td>
</tr>
<tr>
    <td><a href="#import"><CopyableCode code="import" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Generates a temporary URL for uploading an SQL file to, then instructing the D1 to import it and polling it for status updates. Imports block the D1 for their duration.</td>
</tr>
<tr>
    <td><a href="#create_raw"><CopyableCode code="create_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a></td>
    <td></td>
    <td>Returns the query result rows as arrays rather than objects. This is a performance-optimized version of the /query endpoint.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
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

Returns the specified D1 database.

```sql
SELECT
name,
created_at,
file_size,
jurisdiction,
num_tables,
read_replication,
uuid,
version
FROM cloudflare.d1.database
WHERE account_id = '{{ account_id }}' -- required
AND database_id = '{{ database_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of D1 databases.

```sql
SELECT
name,
created_at,
jurisdiction,
uuid,
version
FROM cloudflare.d1.database
WHERE account_id = '{{ account_id }}' -- required
AND name = '{{ name }}'
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

Returns the created D1 database.

```sql
INSERT INTO cloudflare.d1.database (
jurisdiction,
name,
primary_location_hint,
account_id
)
SELECT 
'{{ jurisdiction }}',
'{{ name }}' /* required */,
'{{ primary_location_hint }}',
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
- name: database
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the database resource.
    - name: jurisdiction
      value: "{{ jurisdiction }}"
      description: |
        Specify the location to restrict the D1 database to run and store data. If this option is present, the location hint is ignored.
      valid_values: ['eu', 'fedramp']
    - name: name
      value: "{{ name }}"
      description: |
        D1 database name.
    - name: primary_location_hint
      value: "{{ primary_location_hint }}"
      description: |
        Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as possible to the current user.
      valid_values: ['wnam', 'enam', 'weur', 'eeur', 'apac', 'oc']
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

Updates partially the specified D1 database.

```sql
UPDATE cloudflare.d1.database
SET 
read_replication = '{{ read_replication }}'
WHERE 
account_id = '{{ account_id }}' --required
AND database_id = '{{ database_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates the specified D1 database.

```sql
REPLACE cloudflare.d1.database
SET 
read_replication = '{{ read_replication }}'
WHERE 
account_id = '{{ account_id }}' --required
AND database_id = '{{ database_id }}' --required
AND read_replication = '{{ read_replication }}' --required
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

Deletes the specified D1 database.

```sql
DELETE FROM cloudflare.d1.database
WHERE account_id = '{{ account_id }}' --required
AND database_id = '{{ database_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="export"
    values={[
        { label: 'export', value: 'export' },
        { label: 'import', value: 'import' },
        { label: 'create_raw', value: 'create_raw' }
    ]}
>
<TabItem value="export">

Returns a URL where the SQL contents of your D1 can be downloaded. Note: this process may take some time for larger DBs, during which your D1 will be unavailable to serve queries. To avoid blocking your DB unnecessarily, an in-progress export must be continually polled or will automatically cancel.

```sql
EXEC cloudflare.d1.database.export 
@account_id='{{ account_id }}' --required, 
@database_id='{{ database_id }}' --required 
@@json=
'{
"current_bookmark": "{{ current_bookmark }}", 
"dump_options": "{{ dump_options }}", 
"output_format": "{{ output_format }}"
}'
;
```
</TabItem>
<TabItem value="import">

Generates a temporary URL for uploading an SQL file to, then instructing the D1 to import it and polling it for status updates. Imports block the D1 for their duration.

```sql
EXEC cloudflare.d1.database.import 
@account_id='{{ account_id }}' --required, 
@database_id='{{ database_id }}' --required 
@@json=
'{
"action": "{{ action }}", 
"etag": "{{ etag }}", 
"filename": "{{ filename }}", 
"current_bookmark": "{{ current_bookmark }}"
}'
;
```
</TabItem>
<TabItem value="create_raw">

Returns the query result rows as arrays rather than objects. This is a performance-optimized version of the /query endpoint.

```sql
EXEC cloudflare.d1.database.create_raw 
@account_id='{{ account_id }}' --required, 
@database_id='{{ database_id }}' --required 
@@json=
'{
"params": "{{ params }}", 
"sql": "{{ sql }}", 
"batch": "{{ batch }}"
}'
;
```
</TabItem>
</Tabs>
