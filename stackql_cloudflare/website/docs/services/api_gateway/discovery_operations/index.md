--- 
title: discovery_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - discovery_operations
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

Creates, updates, deletes, gets or lists a <code>discovery_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="discovery_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.discovery_operations" /></td></tr>
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

Retrieve discovered operations on a zone response

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
    <td><CopyableCode code="origin" /></td>
    <td><code>array</code></td>
    <td>API discovery engine(s) that discovered this operation</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State of operation in API Discovery * `review` - Operation is not saved into API Shield Endpoint Management * `saved` - Operation is saved into API Shield Endpoint Management * `ignored` - Operation is marked as ignored (review, saved, ignored)</td>
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
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-method"><code>method</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-diff"><code>diff</code></a>, <a href="#parameter-origin"><code>origin</code></a>, <a href="#parameter-state"><code>state</code></a></td>
    <td>Retrieve the most up to date view of discovered operations</td>
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
<tr id="parameter-diff">
    <td><CopyableCode code="diff" /></td>
    <td><code>boolean</code></td>
    <td></td>
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
<tr id="parameter-origin">
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>Filter results to only include discovery results sourced from a particular discovery engine * `ML` - Discovered operations that were sourced using ML API Discovery * `SessionIdentifier` - Discovered operations that were sourced using Session Identifier API Discovery</td>
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
<tr id="parameter-state">
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Filter results to only include discovery results in a particular state. States are as follows * `review` - Discovered operations that are not saved into API Shield Endpoint Management * `saved` - Discovered operations that are already saved into API Shield Endpoint Management * `ignored` - Discovered operations that have been marked as ignored</td>
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

Retrieve the most up to date view of discovered operations

```sql
SELECT
id,
endpoint,
features,
host,
last_updated,
method,
origin,
state
FROM cloudflare.api_gateway.discovery_operations
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND host = '{{ host }}'
AND method = '{{ method }}'
AND endpoint = '{{ endpoint }}'
AND direction = '{{ direction }}'
AND order = '{{ order }}'
AND diff = '{{ diff }}'
AND origin = '{{ origin }}'
AND state = '{{ state }}'
;
```
</TabItem>
</Tabs>
