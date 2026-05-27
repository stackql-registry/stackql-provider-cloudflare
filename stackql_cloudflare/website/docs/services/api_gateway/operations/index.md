--- 
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
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

Creates, updates, deletes, gets or lists an <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.operations" /></td></tr>
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

Retrieve information about an operation response

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
<tr>
    <td><CopyableCode code="schemas" /></td>
    <td><code>object</code></td>
    <td>OpenAPI JSON schemas for an operation, including both user-uploaded and Cloudflare-learned schemas.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Retrieve all operations from a schema response

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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td><a href="#parameter-feature"><code>feature</code></a>, <a href="#parameter-with_schemas"><code>with_schemas</code></a></td>
    <td>Gets detailed information about a specific API operation in API Shield, including its schema validation settings and traffic statistics.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-schema_id"><code>schema_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-feature"><code>feature</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-method"><code>method</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-operation_status"><code>operation_status</code></a></td>
    <td>Retrieves all operations from the schema. Operations that already exist in API Shield Endpoint Management will be returned as full operations.</td>
</tr>
<tr>
    <td><a href="#api_shield_api_patch_discovered_operation"><CopyableCode code="api_shield_api_patch_discovered_operation" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Update the `state` on a discovered operation</td>
</tr>
<tr>
    <td><a href="#bulk_edit"><CopyableCode code="bulk_edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Update the `state` on one or more discovered operations</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Removes a single API operation from API Shield endpoint management. The operation will no longer be tracked or protected by API Shield rules.</td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Bulk removes multiple API operations from API Shield endpoint management in a single request. Efficient for cleaning up unused endpoints.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for the operation</td>
</tr>
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
    <td>Filter results by whether operations exist in API Shield Endpoint Management or not. `new` will just return operations from the schema that do not exist in API Shield Endpoint Management. `existing` will just return operations from the schema that already exist in API Shield Endpoint Management.</td>
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
<tr id="parameter-with_schemas">
    <td><CopyableCode code="with_schemas" /></td>
    <td><code>boolean</code></td>
    <td>When true, includes OpenAPI schemas (both uploaded and learned) for the operation in the response. Due to the conversion overhead, this parameter is only supported on single-operation retrieval.</td>
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

Gets detailed information about a specific API operation in API Shield, including its schema validation settings and traffic statistics.

```sql
SELECT
operation_id,
endpoint,
features,
host,
last_updated,
method,
schemas
FROM cloudflare.api_gateway.operations
WHERE zone_id = '{{ zone_id }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND feature = '{{ feature }}'
AND with_schemas = '{{ with_schemas }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves all operations from the schema. Operations that already exist in API Shield Endpoint Management will be returned as full operations.

```sql
SELECT
operation_id,
endpoint,
features,
host,
last_updated,
method
FROM cloudflare.api_gateway.operations
WHERE schema_id = '{{ schema_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
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


## `UPDATE` examples

<Tabs
    defaultValue="api_shield_api_patch_discovered_operation"
    values={[
        { label: 'api_shield_api_patch_discovered_operation', value: 'api_shield_api_patch_discovered_operation' },
        { label: 'bulk_edit', value: 'bulk_edit' }
    ]}
>
<TabItem value="api_shield_api_patch_discovered_operation">

Update the `state` on a discovered operation

```sql
UPDATE cloudflare.api_gateway.operations
SET 
state = '{{ state }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND operation_id = '{{ operation_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="bulk_edit">

Update the `state` on one or more discovered operations

```sql
UPDATE cloudflare.api_gateway.operations
SET 
-- No updatable properties
WHERE 
zone_id = '{{ zone_id }}' --required
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
        { label: 'delete', value: 'delete' },
        { label: 'bulk_delete', value: 'bulk_delete' }
    ]}
>
<TabItem value="delete">

Removes a single API operation from API Shield endpoint management. The operation will no longer be tracked or protected by API Shield rules.

```sql
DELETE FROM cloudflare.api_gateway.operations
WHERE zone_id = '{{ zone_id }}' --required
AND operation_id = '{{ operation_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Bulk removes multiple API operations from API Shield endpoint management in a single request. Efficient for cleaning up unused endpoints.

```sql
DELETE FROM cloudflare.api_gateway.operations
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
