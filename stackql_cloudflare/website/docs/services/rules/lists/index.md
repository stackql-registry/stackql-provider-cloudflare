--- 
title: lists
hide_title: false
hide_table_of_contents: false
keywords:
  - lists
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

Creates, updates, deletes, gets or lists a <code>lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rules.lists" /></td></tr>
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

Get a list response.

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
    <td>The unique ID of the list. (example: 2c0fc9fa937b11eaa1b71c4d701ab86e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>An informative name for the list. Use this name in filter and rule expressions. (example: list1)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was created. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the list. (example: This is a note)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type of the list. Each type supports specific list items (IP addresses, ASNs, hostnames or redirects). (ip, redirect, hostname, asn) (example: ip)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was last modified. (example: 2020-01-10T14:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="num_items" /></td>
    <td><code>number</code></td>
    <td>The number of items in the list.</td>
</tr>
<tr>
    <td><CopyableCode code="num_referencing_filters" /></td>
    <td><code>number</code></td>
    <td>The number of [filters](https://developers.cloudflare.com/api/resources/filters/) referencing the list.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get lists response.

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
    <td>The unique ID of the list. (example: 2c0fc9fa937b11eaa1b71c4d701ab86e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>An informative name for the list. Use this name in filter and rule expressions. (example: list1)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was created. (example: 2020-01-01T08:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the list. (example: This is a note)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The type of the list. Each type supports specific list items (IP addresses, ASNs, hostnames or redirects). (ip, redirect, hostname, asn) (example: ip)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td>The RFC 3339 timestamp of when the list was last modified. (example: 2020-01-10T14:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="num_items" /></td>
    <td><code>number</code></td>
    <td>The number of items in the list.</td>
</tr>
<tr>
    <td><CopyableCode code="num_referencing_filters" /></td>
    <td><code>number</code></td>
    <td>The number of [filters](https://developers.cloudflare.com/api/resources/filters/) referencing the list.</td>
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
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the details of a list.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches all lists in the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates a new list of the specified kind.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates the description of a list.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-list_id"><code>list_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a specific list and all its items.</td>
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
<tr id="parameter-list_id">
    <td><CopyableCode code="list_id" /></td>
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

Fetches the details of a list.

```sql
SELECT
id,
name,
created_on,
description,
kind,
modified_on,
num_items,
num_referencing_filters
FROM cloudflare.rules.lists
WHERE list_id = '{{ list_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches all lists in the account.

```sql
SELECT
id,
name,
created_on,
description,
kind,
modified_on,
num_items,
num_referencing_filters
FROM cloudflare.rules.lists
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

Creates a new list of the specified kind.

```sql
INSERT INTO cloudflare.rules.lists (
description,
kind,
name,
account_id
)
SELECT 
'{{ description }}',
'{{ kind }}' /* required */,
'{{ name }}' /* required */,
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
- name: lists
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the lists resource.
    - name: description
      value: "{{ description }}"
      description: |
        An informative summary of the list.
    - name: kind
      value: "{{ kind }}"
      description: |
        The type of the list. Each type supports specific list items (IP addresses, ASNs, hostnames or redirects).
      valid_values: ['ip', 'redirect', 'hostname', 'asn']
    - name: name
      value: "{{ name }}"
      description: |
        An informative name for the list. Use this name in filter and rule expressions.
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

Updates the description of a list.

```sql
REPLACE cloudflare.rules.lists
SET 
description = '{{ description }}'
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

Deletes a specific list and all its items.

```sql
DELETE FROM cloudflare.rules.lists
WHERE list_id = '{{ list_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
