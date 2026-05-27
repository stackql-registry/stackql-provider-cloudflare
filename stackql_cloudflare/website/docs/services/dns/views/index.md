--- 
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - dns
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="views" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.views" /></td></tr>
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

Get DNS Internal View response

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
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the view. (example: my view)</td>
</tr>
<tr>
    <td><CopyableCode code="created_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the view was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the view was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The list of zones linked to this view. (x-stainless-collection-type: set)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Internal DNS Views response

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
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the view. (example: my view)</td>
</tr>
<tr>
    <td><CopyableCode code="created_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the view was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the view was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The list of zones linked to this view. (x-stainless-collection-type: set)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-view_id"><code>view_id</code></a></td>
    <td></td>
    <td>Get DNS Internal View</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-name.exact"><code>name.exact</code></a>, <a href="#parameter-name.contains"><code>name.contains</code></a>, <a href="#parameter-name.startswith"><code>name.startswith</code></a>, <a href="#parameter-name.endswith"><code>name.endswith</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>List DNS Internal Views for an Account</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create Internal DNS View for an account</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-view_id"><code>view_id</code></a></td>
    <td></td>
    <td>Update an existing Internal DNS View</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-view_id"><code>view_id</code></a></td>
    <td></td>
    <td>Delete an existing Internal DNS View</td>
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
<tr id="parameter-view_id">
    <td><CopyableCode code="view_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-match">
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.contains">
    <td><CopyableCode code="name.contains" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.endswith">
    <td><CopyableCode code="name.endswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.exact">
    <td><CopyableCode code="name.exact" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.startswith">
    <td><CopyableCode code="name.startswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_name">
    <td><CopyableCode code="zone_name" /></td>
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

Get DNS Internal View

```sql
SELECT
id,
name,
created_time,
modified_time,
zones
FROM cloudflare.dns.views
WHERE account_id = '{{ account_id }}' -- required
AND view_id = '{{ view_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List DNS Internal Views for an Account

```sql
SELECT
id,
name,
created_time,
modified_time,
zones
FROM cloudflare.dns.views
WHERE account_id = '{{ account_id }}' -- required
AND name = '{{ name }}'
AND name.exact = '{{ name.exact }}'
AND name.contains = '{{ name.contains }}'
AND name.startswith = '{{ name.startswith }}'
AND name.endswith = '{{ name.endswith }}'
AND zone_id = '{{ zone_id }}'
AND zone_name = '{{ zone_name }}'
AND match = '{{ match }}'
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

Create Internal DNS View for an account

```sql
INSERT INTO cloudflare.dns.views (
name,
zones,
account_id
)
SELECT 
'{{ name }}',
'{{ zones }}',
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
- name: views
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the views resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the view.
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The list of zones linked to this view.
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

Update an existing Internal DNS View

```sql
UPDATE cloudflare.dns.views
SET 
name = '{{ name }}',
zones = '{{ zones }}'
WHERE 
account_id = '{{ account_id }}' --required
AND view_id = '{{ view_id }}' --required
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

Delete an existing Internal DNS View

```sql
DELETE FROM cloudflare.dns.views
WHERE account_id = '{{ account_id }}' --required
AND view_id = '{{ view_id }}' --required
;
```
</TabItem>
</Tabs>
