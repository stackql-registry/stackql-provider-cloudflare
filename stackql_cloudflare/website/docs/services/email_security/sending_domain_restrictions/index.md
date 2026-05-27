--- 
title: sending_domain_restrictions
hide_title: false
hide_table_of_contents: false
keywords:
  - sending_domain_restrictions
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

Creates, updates, deletes, gets or lists a <code>sending_domain_restrictions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sending_domain_restrictions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.sending_domain_restrictions" /></td></tr>
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

Sending domain restriction details

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
    <td>Sending domain restriction identifier. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415, title: identifier)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Enforce TLS for all mail from this domain)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain that requires TLS enforcement. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Excluded subdomains that are exempt from TLS requirements.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of sending domain restrictions

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
    <td>Sending domain restriction identifier. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415, title: identifier)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Enforce TLS for all mail from this domain)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain that requires TLS enforcement. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Excluded subdomains that are exempt from TLS requirements.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sending_domain_restriction_id"><code>sending_domain_restriction_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific sending domain restriction including the domain requiring TLS and any excluded subdomains exempt from the TLS requirement.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>Returns a paginated list of sending domain restrictions. These restrictions enforce TLS requirements for emails from specific domains. Mail without TLS from restricted domains will be dropped unless the subdomain is in the exclude list. Supports sorting and searching.</td>
</tr>
<tr>
    <td><a href="#email_security_create_sending_domain_restriction"><CopyableCode code="email_security_create_sending_domain_restriction" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new sending domain restriction to enforce TLS requirements for a domain. Emails without TLS from this domain will be dropped unless the subdomain is in the exclude list.</td>
</tr>
<tr>
    <td><a href="#email_security_update_sending_domain_restriction"><CopyableCode code="email_security_update_sending_domain_restriction" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sending_domain_restriction_id"><code>sending_domain_restriction_id</code></a></td>
    <td></td>
    <td>Updates an existing sending domain restriction. Only provided fields will be modified. Changes affect which domains require TLS and which subdomains are excluded.</td>
</tr>
<tr>
    <td><a href="#email_security_delete_sending_domain_restriction"><CopyableCode code="email_security_delete_sending_domain_restriction" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sending_domain_restriction_id"><code>sending_domain_restriction_id</code></a></td>
    <td></td>
    <td>Removes a sending domain restriction. After deletion, TLS will no longer be enforced for emails from this domain.</td>
</tr>
<tr>
    <td><a href="#batch"><CopyableCode code="batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-deletes"><code>deletes</code></a></td>
    <td></td>
    <td>Executes multiple delete operations on sending domain restrictions atomically. All operations succeed or fail together as a transaction. Currently only supports batch deletion. Removes TLS enforcement requirements for the specified domains.</td>
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
<tr id="parameter-sending_domain_restriction_id">
    <td><CopyableCode code="sending_domain_restriction_id" /></td>
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

Retrieves details for a specific sending domain restriction including the domain requiring TLS and any excluded subdomains exempt from the TLS requirement.

```sql
SELECT
id,
comments,
created_at,
domain,
exclude,
last_modified,
modified_at
FROM cloudflare.email_security.sending_domain_restrictions
WHERE account_id = '{{ account_id }}' -- required
AND sending_domain_restriction_id = '{{ sending_domain_restriction_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of sending domain restrictions. These restrictions enforce TLS requirements for emails from specific domains. Mail without TLS from restricted domains will be dropped unless the subdomain is in the exclude list. Supports sorting and searching.

```sql
SELECT
id,
comments,
created_at,
domain,
exclude,
last_modified,
modified_at
FROM cloudflare.email_security.sending_domain_restrictions
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="email_security_create_sending_domain_restriction"
    values={[
        { label: 'email_security_create_sending_domain_restriction', value: 'email_security_create_sending_domain_restriction' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="email_security_create_sending_domain_restriction">

Creates a new sending domain restriction to enforce TLS requirements for a domain. Emails without TLS from this domain will be dropped unless the subdomain is in the exclude list.

```sql
INSERT INTO cloudflare.email_security.sending_domain_restrictions (
comments,
domain,
exclude,
account_id
)
SELECT 
'{{ comments }}',
'{{ domain }}',
'{{ exclude }}',
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
- name: sending_domain_restrictions
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the sending_domain_restrictions resource.
    - name: comments
      value: "{{ comments }}"
    - name: domain
      value: "{{ domain }}"
      description: |
        Domain that requires TLS enforcement.
    - name: exclude
      value:
        - "{{ exclude }}"
      description: |
        Excluded subdomains that are exempt from TLS requirements.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="email_security_update_sending_domain_restriction"
    values={[
        { label: 'email_security_update_sending_domain_restriction', value: 'email_security_update_sending_domain_restriction' }
    ]}
>
<TabItem value="email_security_update_sending_domain_restriction">

Updates an existing sending domain restriction. Only provided fields will be modified. Changes affect which domains require TLS and which subdomains are excluded.

```sql
UPDATE cloudflare.email_security.sending_domain_restrictions
SET 
comments = '{{ comments }}',
domain = '{{ domain }}',
exclude = '{{ exclude }}'
WHERE 
account_id = '{{ account_id }}' --required
AND sending_domain_restriction_id = '{{ sending_domain_restriction_id }}' --required
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
    defaultValue="email_security_delete_sending_domain_restriction"
    values={[
        { label: 'email_security_delete_sending_domain_restriction', value: 'email_security_delete_sending_domain_restriction' }
    ]}
>
<TabItem value="email_security_delete_sending_domain_restriction">

Removes a sending domain restriction. After deletion, TLS will no longer be enforced for emails from this domain.

```sql
DELETE FROM cloudflare.email_security.sending_domain_restrictions
WHERE account_id = '{{ account_id }}' --required
AND sending_domain_restriction_id = '{{ sending_domain_restriction_id }}' --required
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

Executes multiple delete operations on sending domain restrictions atomically. All operations succeed or fail together as a transaction. Currently only supports batch deletion. Removes TLS enforcement requirements for the specified domains.

```sql
EXEC cloudflare.email_security.sending_domain_restrictions.batch 
@account_id='{{ account_id }}' --required 
@@json=
'{
"deletes": "{{ deletes }}"
}'
;
```
</TabItem>
</Tabs>
