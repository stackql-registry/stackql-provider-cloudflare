--- 
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - workers
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

Creates, updates, deletes, gets or lists a <code>queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.queries" /></td></tr>
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

Successful request

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Query name</td>
</tr>
<tr>
    <td><CopyableCode code="adhoc" /></td>
    <td><code>boolean</code></td>
    <td>If the query wasn't explcitly saved</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Query description)</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Successful request

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Query name</td>
</tr>
<tr>
    <td><CopyableCode code="adhoc" /></td>
    <td><code>boolean</code></td>
    <td>If the query wasn't explcitly saved</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Query description)</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updatedBy" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieve a saved query.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-perPage"><code>perPage</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a></td>
    <td>List saved queries.</td>
</tr>
<tr>
    <td><a href="#queries_post"><CopyableCode code="queries_post" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-parameters"><code>parameters</code></a></td>
    <td></td>
    <td>Persist query for later use.</td>
</tr>
<tr>
    <td><a href="#queries_patch"><CopyableCode code="queries_patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-parameters"><code>parameters</code></a></td>
    <td></td>
    <td>Update saved query.</td>
</tr>
<tr>
    <td><a href="#queries_delete"><CopyableCode code="queries_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-query_id"><code>query_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a saved query.</td>
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
<tr id="parameter-query_id">
    <td><CopyableCode code="query_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-perPage">
    <td><CopyableCode code="perPage" /></td>
    <td><code>number</code></td>
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

Retrieve a saved query.

```sql
SELECT
id,
name,
adhoc,
created,
createdBy,
description,
parameters,
updated,
updatedBy
FROM cloudflare.workers.queries
WHERE query_id = '{{ query_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List saved queries.

```sql
SELECT
id,
name,
adhoc,
created,
createdBy,
description,
parameters,
updated,
updatedBy
FROM cloudflare.workers.queries
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND perPage = '{{ perPage }}'
AND order = '{{ order }}'
AND orderBy = '{{ orderBy }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="queries_post"
    values={[
        { label: 'queries_post', value: 'queries_post' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="queries_post">

Persist query for later use.

```sql
INSERT INTO cloudflare.workers.queries (
description,
name,
parameters,
account_id
)
SELECT 
'{{ description }}' /* required */,
'{{ name }}' /* required */,
'{{ parameters }}' /* required */,
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
- name: queries
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the queries resource.
    - name: description
      value: "{{ description }}"
    - name: name
      value: "{{ name }}"
      description: |
        Query name
    - name: parameters
      value:
        calculations:
          - alias: "{{ alias }}"
            key: "{{ key }}"
            keyType: "{{ keyType }}"
            operator: "{{ operator }}"
        datasets:
          - "{{ datasets }}"
        filterCombination: "{{ filterCombination }}"
        filters:
          - filterCombination: "{{ filterCombination }}"
            filters: "{{ filters }}"
            kind: "{{ kind }}"
            key: "{{ key }}"
            operation: "{{ operation }}"
            type: "{{ type }}"
            value: "{{ value }}"
        groupBys:
          - type: "{{ type }}"
            value: "{{ value }}"
        havings:
          - key: "{{ key }}"
            operation: "{{ operation }}"
            value: {{ value }}
        limit: {{ limit }}
        needle:
          isRegex: {{ isRegex }}
          matchCase: {{ matchCase }}
          value: "{{ value }}"
        orderBy:
          order: "{{ order }}"
          value: "{{ value }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="queries_patch"
    values={[
        { label: 'queries_patch', value: 'queries_patch' }
    ]}
>
<TabItem value="queries_patch">

Update saved query.

```sql
UPDATE cloudflare.workers.queries
SET 
description = '{{ description }}',
name = '{{ name }}',
parameters = '{{ parameters }}'
WHERE 
query_id = '{{ query_id }}' --required
AND account_id = '{{ account_id }}' --required
AND description = '{{ description }}' --required
AND name = '{{ name }}' --required
AND parameters = '{{ parameters }}' --required
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
    defaultValue="queries_delete"
    values={[
        { label: 'queries_delete', value: 'queries_delete' }
    ]}
>
<TabItem value="queries_delete">

Delete a saved query.

```sql
DELETE FROM cloudflare.workers.queries
WHERE query_id = '{{ query_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
