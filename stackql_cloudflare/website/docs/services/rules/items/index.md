--- 
title: items
hide_title: false
hide_table_of_contents: false
keywords:
  - items
  - rules
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

Creates, updates, deletes, gets or lists an <code>items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rules.items" /></td></tr>
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

Get a list item response.

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
    <td>Defines the unique ID of the item in the List. (example: 34b12448945f11eaa1b71c4d701ab86e)</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Defines a non-negative 32 bit integer.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Defines an informative summary of the list item. (example: Private IP address)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was created. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>object</code></td>
    <td>Valid characters for hostnames are ASCII(7) letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen (-).</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>An IPv4 address, an IPv4 CIDR, an IPv6 address, or an IPv6 CIDR. (example: 10.0.0.1)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was last modified. (example: 2020-01-10T14:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="redirect" /></td>
    <td><code>object</code></td>
    <td>The definition of the redirect.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get list items response.

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
    <td>Defines the unique ID of the item in the List. (example: 34b12448945f11eaa1b71c4d701ab86e)</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Defines a non-negative 32 bit integer.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Defines an informative summary of the list item. (example: Private IP address)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was created. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>object</code></td>
    <td>Valid characters for hostnames are ASCII(7) letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen (-).</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>An IPv4 address, an IPv4 CIDR, an IPv6 address, or an IPv6 CIDR. (example: 10.0.0.1)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was last modified. (example: 2020-01-10T14:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="redirect" /></td>
    <td><code>object</code></td>
    <td>The definition of the redirect.</td>
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
    <td><a href="#parameter-item_id"><code>item_id</code></a>, <a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a list item in the list.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Fetches all the items in the list.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Appends new items to the list. This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`. There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Removes all existing items from the list and adds the provided items to the list. This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`. There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Removes one or more items from a list. This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`. There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.</td>
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
<tr id="parameter-item_id">
    <td><CopyableCode code="item_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-list_id">
    <td><CopyableCode code="list_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
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

Fetches a list item in the list.

```sql
SELECT
id,
asn,
comment,
created_on,
hostname,
ip,
modified_on,
redirect
FROM cloudflare.rules.items
WHERE item_id = '{{ item_id }}' -- required
AND list_id = '{{ list_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches all the items in the list.

```sql
SELECT
id,
asn,
comment,
created_on,
hostname,
ip,
modified_on,
redirect
FROM cloudflare.rules.items
WHERE list_id = '{{ list_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND cursor = '{{ cursor }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
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

Appends new items to the list. This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`. There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.

```sql
INSERT INTO cloudflare.rules.items (
list_id,
account_id
)
SELECT 
'{{ list_id }}',
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
- name: items
  props:
    - name: list_id
      value: "{{ list_id }}"
      description: Required parameter for the items resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the items resource.
`}</CodeBlock>

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

Removes all existing items from the list and adds the provided items to the list. This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`. There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.

```sql
REPLACE cloudflare.rules.items
SET 
-- No updatable properties
WHERE 
list_id = '{{ list_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Removes one or more items from a list. This operation is asynchronous. To get current the operation status, invoke the `Get bulk operation status` endpoint with the returned `operation_id`. There is a limit of 1 pending bulk operation per account. If an outstanding bulk operation is in progress, the request will be rejected.

```sql
DELETE FROM cloudflare.rules.items
WHERE list_id = '{{ list_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
