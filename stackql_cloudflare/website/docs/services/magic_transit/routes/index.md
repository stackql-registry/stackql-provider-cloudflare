--- 
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - magic_transit
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.routes" /></td></tr>
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

Route Details response

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
    <td><CopyableCode code="route" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Routes response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the route was created. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional human provided description of the static route. (example: New route for new prefix 203.0.113.1)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the route was last modified. (example: 2017-06-14T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="nexthop" /></td>
    <td><code>string</code></td>
    <td>The next-hop IP Address for the static route. (example: 203.0.113.1)</td>
</tr>
<tr>
    <td><CopyableCode code="prefix" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of the static route.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>Used only for ECMP routes.</td>
</tr>
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>Optional weight of the ECMP scope - if provided.</td>
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
    <td><a href="#parameter-route_id"><code>route_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get a specific Magic static route.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all Magic static routes.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-nexthop"><code>nexthop</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td></td>
    <td>Creates a new Magic static route. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-route_id"><code>route_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix"><code>prefix</code></a>, <a href="#parameter-nexthop"><code>nexthop</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td></td>
    <td>Update a specific Magic static route. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes.</td>
</tr>
<tr>
    <td><a href="#bulk_update"><CopyableCode code="bulk_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-routes"><code>routes</code></a></td>
    <td></td>
    <td>Update multiple Magic static routes. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes. Only fields for a route that need to be changed need be provided.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-route_id"><code>route_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Disable and remove a specific Magic static route.</td>
</tr>
<tr>
    <td><a href="#empty"><CopyableCode code="empty" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete multiple Magic static routes.</td>
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
<tr id="parameter-route_id">
    <td><CopyableCode code="route_id" /></td>
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

Get a specific Magic static route.

```sql
SELECT
route
FROM cloudflare.magic_transit.routes
WHERE route_id = '{{ route_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Magic static routes.

```sql
SELECT
id,
created_on,
description,
modified_on,
nexthop,
prefix,
priority,
scope,
weight
FROM cloudflare.magic_transit.routes
WHERE account_id = '{{ account_id }}' -- required
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

Creates a new Magic static route. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes.

```sql
INSERT INTO cloudflare.magic_transit.routes (
description,
nexthop,
prefix,
priority,
scope,
weight,
account_id
)
SELECT 
'{{ description }}',
'{{ nexthop }}' /* required */,
'{{ prefix }}' /* required */,
{{ priority }} /* required */,
'{{ scope }}',
{{ weight }},
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
- name: routes
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the routes resource.
    - name: description
      value: "{{ description }}"
      description: |
        An optional human provided description of the static route.
    - name: nexthop
      value: "{{ nexthop }}"
      description: |
        The next-hop IP Address for the static route.
    - name: prefix
      value: "{{ prefix }}"
      description: |
        IP Prefix in Classless Inter-Domain Routing format.
    - name: priority
      value: {{ priority }}
      description: |
        Priority of the static route.
    - name: scope
      description: |
        Used only for ECMP routes.
      value:
        colo_names:
          - "{{ colo_names }}"
        colo_regions:
          - "{{ colo_regions }}"
    - name: weight
      value: {{ weight }}
      description: |
        Optional weight of the ECMP scope - if provided.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'bulk_update', value: 'bulk_update' }
    ]}
>
<TabItem value="update">

Update a specific Magic static route. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes.

```sql
REPLACE cloudflare.magic_transit.routes
SET 
description = '{{ description }}',
nexthop = '{{ nexthop }}',
prefix = '{{ prefix }}',
priority = {{ priority }},
scope = '{{ scope }}',
weight = {{ weight }}
WHERE 
route_id = '{{ route_id }}' --required
AND account_id = '{{ account_id }}' --required
AND prefix = '{{ prefix }}' --required
AND nexthop = '{{ nexthop }}' --required
AND priority = '{{ priority }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="bulk_update">

Update multiple Magic static routes. Use `?validate_only=true` as an optional query parameter to run validation only without persisting changes. Only fields for a route that need to be changed need be provided.

```sql
REPLACE cloudflare.magic_transit.routes
SET 
routes = '{{ routes }}'
WHERE 
account_id = '{{ account_id }}' --required
AND routes = '{{ routes }}' --required
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
        { label: 'empty', value: 'empty' }
    ]}
>
<TabItem value="delete">

Disable and remove a specific Magic static route.

```sql
DELETE FROM cloudflare.magic_transit.routes
WHERE route_id = '{{ route_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="empty">

Delete multiple Magic static routes.

```sql
DELETE FROM cloudflare.magic_transit.routes
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
