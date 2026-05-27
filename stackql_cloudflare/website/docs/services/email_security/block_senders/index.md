--- 
title: block_senders
hide_title: false
hide_table_of_contents: false
keywords:
  - block_senders
  - email_security
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

Creates, updates, deletes, gets or lists a <code>block_senders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="block_senders" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.block_senders" /></td></tr>
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

Blocked sender details

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
    <td>Blocked sender pattern identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Block sender with email test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Deprecated, use `modified_at` instead. End of life: November 1, 2026. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td> (example: test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="pattern_type" /></td>
    <td><code>string</code></td>
    <td>Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when creating or updating policies, but may be returned for existing entries. (EMAIL, DOMAIN, IP, UNKNOWN) (example: EMAIL)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of blocked senders

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
    <td>Blocked sender pattern identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Block sender with email test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>Deprecated, use `modified_at` instead. End of life: November 1, 2026. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td> (example: test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="pattern_type" /></td>
    <td><code>string</code></td>
    <td>Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when creating or updating policies, but may be returned for existing entries. (EMAIL, DOMAIN, IP, UNKNOWN) (example: EMAIL)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pattern_id"><code>pattern_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific blocked sender pattern including its pattern type, value, and metadata.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-pattern_type"><code>pattern_type</code></a>, <a href="#parameter-pattern"><code>pattern</code></a></td>
    <td>Returns a paginated list of blocked email sender patterns. These patterns prevent emails from matching senders from being delivered. Supports filtering by pattern type and searching across patterns.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new blocked sender pattern. Emails matching this pattern will be blocked from delivery. Patterns can be email addresses, domains, or IP addresses, and support regular expressions.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pattern_id"><code>pattern_id</code></a></td>
    <td></td>
    <td>Updates an existing blocked sender pattern. Only provided fields will be modified. The pattern will continue blocking emails until deleted.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pattern_id"><code>pattern_id</code></a></td>
    <td></td>
    <td>Removes a blocked sender pattern. After deletion, emails from this sender will no longer be automatically blocked based on this rule.</td>
</tr>
<tr>
    <td><a href="#batch"><CopyableCode code="batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-deletes"><code>deletes</code></a>, <a href="#parameter-patches"><code>patches</code></a>, <a href="#parameter-puts"><code>puts</code></a>, <a href="#parameter-posts"><code>posts</code></a></td>
    <td></td>
    <td>Execute multiple operations atomically. All four operation arrays (deletes, patches, puts, posts) are required and executed in order. Send empty arrays for unused operations.</td>
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
<tr id="parameter-pattern_id">
    <td><CopyableCode code="pattern_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The sorting direction.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Field to sort by.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Current page within paginated list of results.</td>
</tr>
<tr id="parameter-pattern">
    <td><CopyableCode code="pattern" /></td>
    <td><code>string</code></td>
    <td>Filter by pattern value.</td>
</tr>
<tr id="parameter-pattern_type">
    <td><CopyableCode code="pattern_type" /></td>
    <td><code>string</code></td>
    <td>Filter by pattern type.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The number of results per page. Maximum value is 1000.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Search term for filtering records. Behavior may change.</td>
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

Retrieves details for a specific blocked sender pattern including its pattern type, value, and metadata.

```sql
SELECT
id,
comments,
created_at,
is_regex,
last_modified,
modified_at,
pattern,
pattern_type
FROM cloudflare.email_security.block_senders
WHERE account_id = '{{ account_id }}' -- required
AND pattern_id = '{{ pattern_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of blocked email sender patterns. These patterns prevent emails from matching senders from being delivered. Supports filtering by pattern type and searching across patterns.

```sql
SELECT
id,
comments,
created_at,
is_regex,
last_modified,
modified_at,
pattern,
pattern_type
FROM cloudflare.email_security.block_senders
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND pattern_type = '{{ pattern_type }}'
AND pattern = '{{ pattern }}'
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

Creates a new blocked sender pattern. Emails matching this pattern will be blocked from delivery. Patterns can be email addresses, domains, or IP addresses, and support regular expressions.

```sql
INSERT INTO cloudflare.email_security.block_senders (
comments,
is_regex,
pattern,
pattern_type,
account_id
)
SELECT 
'{{ comments }}',
{{ is_regex }},
'{{ pattern }}',
'{{ pattern_type }}',
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
- name: block_senders
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the block_senders resource.
    - name: comments
      value: "{{ comments }}"
    - name: is_regex
      value: {{ is_regex }}
    - name: pattern
      value: "{{ pattern }}"
    - name: pattern_type
      value: "{{ pattern_type }}"
      description: |
        Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when creating or updating policies, but may be returned for existing entries.
      valid_values: ['EMAIL', 'DOMAIN', 'IP', 'UNKNOWN']
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

Updates an existing blocked sender pattern. Only provided fields will be modified. The pattern will continue blocking emails until deleted.

```sql
UPDATE cloudflare.email_security.block_senders
SET 
comments = '{{ comments }}',
is_regex = {{ is_regex }},
pattern = '{{ pattern }}',
pattern_type = '{{ pattern_type }}'
WHERE 
account_id = '{{ account_id }}' --required
AND pattern_id = '{{ pattern_id }}' --required
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

Removes a blocked sender pattern. After deletion, emails from this sender will no longer be automatically blocked based on this rule.

```sql
DELETE FROM cloudflare.email_security.block_senders
WHERE account_id = '{{ account_id }}' --required
AND pattern_id = '{{ pattern_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch"
    values={[
        { label: 'batch', value: 'batch' }
    ]}
>
<TabItem value="batch">

Execute multiple operations atomically. All four operation arrays (deletes, patches, puts, posts) are required and executed in order. Send empty arrays for unused operations.

```sql
EXEC cloudflare.email_security.block_senders.batch 
@account_id='{{ account_id }}' --required 
@@json=
'{
"deletes": "{{ deletes }}", 
"patches": "{{ patches }}", 
"posts": "{{ posts }}", 
"puts": "{{ puts }}"
}'
;
```
</TabItem>
</Tabs>
