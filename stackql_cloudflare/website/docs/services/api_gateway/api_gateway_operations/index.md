--- 
title: api_gateway_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_gateway_operations
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

Creates, updates, deletes, gets or lists an <code>api_gateway_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="api_gateway_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.api_gateway_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieve information about all operations on a zone response

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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-method"><code>method</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-feature"><code>feature</code></a></td>
    <td>Lists all API operations tracked by API Shield for a zone with pagination. Returns operation details including method, path, and feature configurations.</td>
</tr>
<tr>
    <td><a href="#api_shield_endpoint_management_add_operations_to_a_zone"><CopyableCode code="api_shield_endpoint_management_add_operations_to_a_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Add one or more operations to a zone. Endpoints can contain path variables. Host, method, endpoint will be normalized to a canoncial form when creating an operation and must be unique on the zone. Inserting an operation that matches an existing one will return the record of the already existing operation and update its last_updated date.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
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
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists all API operations tracked by API Shield for a zone with pagination. Returns operation details including method, path, and feature configurations.

```sql
SELECT
operation_id,
endpoint,
features,
host,
last_updated,
method
FROM cloudflare.api_gateway.api_gateway_operations
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND host = '{{ host }}'
AND method = '{{ method }}'
AND endpoint = '{{ endpoint }}'
AND feature = '{{ feature }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="api_shield_endpoint_management_add_operations_to_a_zone"
    values={[
        { label: 'api_shield_endpoint_management_add_operations_to_a_zone', value: 'api_shield_endpoint_management_add_operations_to_a_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="api_shield_endpoint_management_add_operations_to_a_zone">

Add one or more operations to a zone. Endpoints can contain path variables. Host, method, endpoint will be normalized to a canoncial form when creating an operation and must be unique on the zone. Inserting an operation that matches an existing one will return the record of the already existing operation and update its last_updated date.

```sql
INSERT INTO cloudflare.api_gateway.api_gateway_operations (
zone_id
)
SELECT 
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
- name: api_gateway_operations
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the api_gateway_operations resource.
`}</CodeBlock>

</TabItem>
</Tabs>
