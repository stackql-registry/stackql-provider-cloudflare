--- 
title: syn_protection_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - syn_protection_filters
  - ddos_protection
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

Creates, updates, deletes, gets or lists a <code>syn_protection_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="syn_protection_filters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ddos_protection.syn_protection_filters" /></td></tr>
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

Get SYN Protection filter response.

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
    <td>The unique ID of the expression filter.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation timestamp of the expression filter.</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>The filter expression. (example: ip.dst in &#123; 192.0.2.0/24 198.51.100.0/24 &#125; and tcp.srcport in &#123; 80 443 10000..65535 &#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modification timestamp of the expression filter.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List all SYN Protection filters response.

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
    <td>The unique ID of the expression filter.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation timestamp of the expression filter.</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>The filter expression. (example: ip.dst in &#123; 192.0.2.0/24 198.51.100.0/24 &#125; and tcp.srcport in &#123; 80 443 10000..65535 &#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modification timestamp of the expression filter.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-filter_id"><code>filter_id</code></a></td>
    <td></td>
    <td>Get a SYN Protection filter specified by the given UUID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>List all SYN Protection filters for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-mode"><code>mode</code></a></td>
    <td></td>
    <td>Create a SYN Protection filter for an account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-filter_id"><code>filter_id</code></a></td>
    <td></td>
    <td>Update a SYN Protection filter specified by the given UUID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-filter_id"><code>filter_id</code></a></td>
    <td></td>
    <td>Delete a SYN Protection filter specified by the given UUID.</td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete all SYN Protection filters for an account.</td>
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
<tr id="parameter-filter_id">
    <td><CopyableCode code="filter_id" /></td>
    <td><code>string</code></td>
    <td>The UUID of the filter to delete.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of ordering (ASC or DESC). Defaults to 'ASC'.</td>
</tr>
<tr id="parameter-mode">
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode of the filters to get. Optional. Valid values: 'enabled', 'disabled', 'monitoring'.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>The field to order by. Defaults to 'prefix'.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer (int64)</code></td>
    <td>The page number for pagination. Defaults to 1.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer (int64)</code></td>
    <td>The number of items per page. Must be between 10 and 1000. Defaults to 25.</td>
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

Get a SYN Protection filter specified by the given UUID.

```sql
SELECT
id,
created_on,
expression,
mode,
modified_on
FROM cloudflare.ddos_protection.syn_protection_filters
WHERE account_id = '{{ account_id }}' -- required
AND filter_id = '{{ filter_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all SYN Protection filters for an account.

```sql
SELECT
id,
created_on,
expression,
mode,
modified_on
FROM cloudflare.ddos_protection.syn_protection_filters
WHERE account_id = '{{ account_id }}' -- required
AND mode = '{{ mode }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
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

Create a SYN Protection filter for an account.

```sql
INSERT INTO cloudflare.ddos_protection.syn_protection_filters (
expression,
mode,
account_id
)
SELECT 
'{{ expression }}' /* required */,
'{{ mode }}' /* required */,
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
- name: syn_protection_filters
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the syn_protection_filters resource.
    - name: expression
      value: "{{ expression }}"
      description: |
        The filter expression.
    - name: mode
      value: "{{ mode }}"
      description: |
        The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'.
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

Update a SYN Protection filter specified by the given UUID.

```sql
UPDATE cloudflare.ddos_protection.syn_protection_filters
SET 
expression = '{{ expression }}',
mode = '{{ mode }}'
WHERE 
account_id = '{{ account_id }}' --required
AND filter_id = '{{ filter_id }}' --required
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

Delete a SYN Protection filter specified by the given UUID.

```sql
DELETE FROM cloudflare.ddos_protection.syn_protection_filters
WHERE account_id = '{{ account_id }}' --required
AND filter_id = '{{ filter_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Delete all SYN Protection filters for an account.

```sql
DELETE FROM cloudflare.ddos_protection.syn_protection_filters
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
