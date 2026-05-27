--- 
title: schemas_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas_operations
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

Creates, updates, deletes, gets or lists a <code>schemas_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="schemas_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.schema_validation.schemas_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_zone"
    values={[
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_zone">

All operations in the schema

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
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string (uri-template)</code></td>
    <td>The endpoint which can contain path parameter templates in curly braces, each will be replaced from left to right with &#123;varN&#125;, starting with &#123;var1&#125;, during insertion. This will further be Cloudflare-normalized upon insertion. See: https://developers.cloudflare.com/rules/normalization/how-it-works/. (example: /api/v1/users/&#123;var1&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="features" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string (hostname)</code></td>
    <td>RFC3986-compliant host. (example: www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="method" /></td>
    <td><code>string</code></td>
    <td>The HTTP method used to access the endpoint. (GET, POST, HEAD, OPTIONS, PUT, DELETE, CONNECT, PATCH, TRACE) (example: GET)</td>
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
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-schema_id"><code>schema_id</code></a></td>
    <td><a href="#parameter-feature"><code>feature</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-method"><code>method</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-operation_status"><code>operation_status</code></a></td>
    <td>Retrieves all operations from the schema. Operations that already exist in API Shield Endpoint Management will be returned as full operations.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-feature">
    <td><CopyableCode code="feature" /></td>
    <td><code>array</code></td>
    <td>Add feature(s) to the results. The feature name that is given here corresponds to the resulting feature object. Have a look at the top-level object description for more details on the specific meaning.</td>
</tr>
<tr id="parameter-host">
    <td><CopyableCode code="host" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-method">
    <td><CopyableCode code="method" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-operation_status">
    <td><CopyableCode code="operation_status" /></td>
    <td><code>string</code></td>
    <td>Filter results by whether operations exist in Web Asset Management or not. `new` will just return operations from the schema that do not exist otherwise. `existing` will just return operations from the schema that already exist.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_zone"
    values={[
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_zone">

Retrieves all operations from the schema. Operations that already exist in API Shield Endpoint Management will be returned as full operations.

```sql
SELECT
operation_id,
endpoint,
features,
host,
last_updated,
method
FROM cloudflare.schema_validation.schemas_operations
WHERE zone_id = '{{ zone_id }}' -- required
AND schema_id = '{{ schema_id }}' -- required
AND feature = '{{ feature }}'
AND host = '{{ host }}'
AND method = '{{ method }}'
AND endpoint = '{{ endpoint }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND operation_status = '{{ operation_status }}'
;
```
</TabItem>
</Tabs>
