--- 
title: filters
hide_title: false
hide_table_of_contents: false
keywords:
  - filters
  - filters
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

Creates, updates, deletes, gets or lists a <code>filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="filters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.filters.filters" /></td></tr>
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

Get a filter response

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
    <td>The unique identifier of the filter. (example: 372e67954025e0ba6aaa6d586b9e0b61)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the filter. (example: Restrict access from these browsers on this address range.)</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>The filter expression. For more information, refer to [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/). (example: (http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155)</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the filter is currently paused.</td>
</tr>
<tr>
    <td><CopyableCode code="ref" /></td>
    <td><code>string</code></td>
    <td>A short reference tag. Allows you to select related filters. (example: FIL-100)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List filters response

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
    <td>The unique identifier of the filter. (example: 372e67954025e0ba6aaa6d586b9e0b61)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the filter. (example: Restrict access from these browsers on this address range.)</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>The filter expression. For more information, refer to [Expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/). (example: (http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155)</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the filter is currently paused.</td>
</tr>
<tr>
    <td><CopyableCode code="ref" /></td>
    <td><code>string</code></td>
    <td>A short reference tag. Allows you to select related filters. (example: FIL-100)</td>
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
    <td><a href="#parameter-filter_id"><code>filter_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a filter.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-paused"><code>paused</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-ref"><code>ref</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td>Fetches filters in a zone. You can filter the results using several optional parameters.</td>
</tr>
<tr>
    <td><a href="#filters_create_filters"><CopyableCode code="filters_create_filters" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Creates one or more filters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-filter_id"><code>filter_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates an existing filter.</td>
</tr>
<tr>
    <td><a href="#filters_update_filters"><CopyableCode code="filters_update_filters" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates one or more existing filters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-filter_id"><code>filter_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing filter.</td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a></td>
    <td>Deletes one or more existing filters.</td>
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
<tr id="parameter-filter_id">
    <td><CopyableCode code="filter_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-description">
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-expression">
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-paused">
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-ref">
    <td><CopyableCode code="ref" /></td>
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

Fetches the details of a filter.

```sql
SELECT
id,
description,
expression,
paused,
ref
FROM cloudflare.filters.filters
WHERE filter_id = '{{ filter_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches filters in a zone. You can filter the results using several optional parameters.

```sql
SELECT
id,
description,
expression,
paused,
ref
FROM cloudflare.filters.filters
WHERE zone_id = '{{ zone_id }}' -- required
AND paused = '{{ paused }}'
AND expression = '{{ expression }}'
AND description = '{{ description }}'
AND ref = '{{ ref }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND id = '{{ id }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="filters_create_filters"
    values={[
        { label: 'filters_create_filters', value: 'filters_create_filters' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="filters_create_filters">

Creates one or more filters.

```sql
INSERT INTO cloudflare.filters.filters (
zone_id
)
SELECT 
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: filters
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the filters resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'filters_update_filters', value: 'filters_update_filters' }
    ]}
>
<TabItem value="update">

Updates an existing filter.

```sql
REPLACE cloudflare.filters.filters
SET 
description = '{{ description }}',
expression = '{{ expression }}',
paused = {{ paused }},
ref = '{{ ref }}'
WHERE 
filter_id = '{{ filter_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="filters_update_filters">

Updates one or more existing filters.

```sql
REPLACE cloudflare.filters.filters
SET 
-- No updatable properties
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
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

Deletes an existing filter.

```sql
DELETE FROM cloudflare.filters.filters
WHERE filter_id = '{{ filter_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Deletes one or more existing filters.

```sql
DELETE FROM cloudflare.filters.filters
WHERE zone_id = '{{ zone_id }}' --required
AND id = '{{ id }}'
;
```
</TabItem>
</Tabs>
