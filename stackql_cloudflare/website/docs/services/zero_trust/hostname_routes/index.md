--- 
title: hostname_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - hostname_routes
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>hostname_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="hostname_routes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.hostname_routes" /></td></tr>
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

Get hostname route response

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
    <td><code>string (uuid)</code></td>
    <td>The hostname route ID. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for a tunnel. (example: api-tunnel)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>An optional description of the hostname route. (example: example comment)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was created. (example: 2021-01-25T18:22:34.317854Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was deleted. If `null`, the resource has not been deleted. (example: 2009-11-10T23:00:00.000000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname of the route. (example: office-1.local)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List hostname routes response

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
    <td><code>string (uuid)</code></td>
    <td>The hostname route ID. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>UUID of the tunnel. (example: f70ff985-a4ef-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for a tunnel. (example: api-tunnel)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>An optional description of the hostname route. (example: example comment)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was created. (example: 2021-01-25T18:22:34.317854Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the resource was deleted. If `null`, the resource has not been deleted. (example: 2009-11-10T23:00:00.000000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname of the route. (example: office-1.local)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hostname_route_id"><code>hostname_route_id</code></a></td>
    <td></td>
    <td>Get a hostname route.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a>, <a href="#parameter-comment"><code>comment</code></a>, <a href="#parameter-existed_at"><code>existed_at</code></a>, <a href="#parameter-is_deleted"><code>is_deleted</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a></td>
    <td>Lists and filters hostname routes in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create a hostname route.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hostname_route_id"><code>hostname_route_id</code></a></td>
    <td></td>
    <td>Updates a hostname route.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hostname_route_id"><code>hostname_route_id</code></a></td>
    <td></td>
    <td>Delete a hostname route.</td>
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
<tr id="parameter-hostname_route_id">
    <td><CopyableCode code="hostname_route_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-comment">
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-existed_at">
    <td><CopyableCode code="existed_at" /></td>
    <td><code>string (url-encoded-date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>If set, only list hostname routes that contain a substring of the given value, the filter is case-insensitive.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-is_deleted">
    <td><CopyableCode code="is_deleted" /></td>
    <td><code>boolean</code></td>
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
<tr id="parameter-tunnel_id">
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>If set, only list hostname routes that point to a specific tunnel.</td>
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

Get a hostname route.

```sql
SELECT
id,
tunnel_id,
tunnel_name,
comment,
created_at,
deleted_at,
hostname
FROM cloudflare.zero_trust.hostname_routes
WHERE account_id = '{{ account_id }}' -- required
AND hostname_route_id = '{{ hostname_route_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists and filters hostname routes in an account.

```sql
SELECT
id,
tunnel_id,
tunnel_name,
comment,
created_at,
deleted_at,
hostname
FROM cloudflare.zero_trust.hostname_routes
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}'
AND hostname = '{{ hostname }}'
AND tunnel_id = '{{ tunnel_id }}'
AND comment = '{{ comment }}'
AND existed_at = '{{ existed_at }}'
AND is_deleted = '{{ is_deleted }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
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

Create a hostname route.

```sql
INSERT INTO cloudflare.zero_trust.hostname_routes (
comment,
hostname,
tunnel_id,
account_id
)
SELECT 
'{{ comment }}',
'{{ hostname }}',
'{{ tunnel_id }}',
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
- name: hostname_routes
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the hostname_routes resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        An optional description of the hostname route.
    - name: hostname
      value: "{{ hostname }}"
      description: |
        The hostname of the route.
    - name: tunnel_id
      value: "{{ tunnel_id }}"
      description: |
        UUID of the tunnel.
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

Updates a hostname route.

```sql
UPDATE cloudflare.zero_trust.hostname_routes
SET 
comment = '{{ comment }}',
hostname = '{{ hostname }}',
tunnel_id = '{{ tunnel_id }}'
WHERE 
account_id = '{{ account_id }}' --required
AND hostname_route_id = '{{ hostname_route_id }}' --required
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

Delete a hostname route.

```sql
DELETE FROM cloudflare.zero_trust.hostname_routes
WHERE account_id = '{{ account_id }}' --required
AND hostname_route_id = '{{ hostname_route_id }}' --required
;
```
</TabItem>
</Tabs>
