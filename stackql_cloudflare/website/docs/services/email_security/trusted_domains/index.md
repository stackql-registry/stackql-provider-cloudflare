--- 
title: trusted_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - trusted_domains
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

Creates, updates, deletes, gets or lists a <code>trusted_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="trusted_domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.trusted_domains" /></td></tr>
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

Trusted domain details

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
    <td>Trusted domain identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Trusted partner domain)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_recent" /></td>
    <td><code>boolean</code></td>
    <td>Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.</td>
</tr>
<tr>
    <td><CopyableCode code="is_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_similarity" /></td>
    <td><code>boolean</code></td>
    <td>Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.</td>
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
    <td> (example: example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of trusted domains

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
    <td>Trusted domain identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Trusted partner domain)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_recent" /></td>
    <td><code>boolean</code></td>
    <td>Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.</td>
</tr>
<tr>
    <td><CopyableCode code="is_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_similarity" /></td>
    <td><code>boolean</code></td>
    <td>Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.</td>
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
    <td> (example: example.com)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trusted_domain_id"><code>trusted_domain_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific trusted domain pattern including its pattern value, whether it uses regex matching, and which detection types it affects.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-is_recent"><code>is_recent</code></a>, <a href="#parameter-is_similarity"><code>is_similarity</code></a>, <a href="#parameter-pattern"><code>pattern</code></a></td>
    <td>Returns a paginated list of trusted domain patterns. Trusted domains prevent false positives for recently registered domains and lookalike domain detections. Patterns can use regular expressions for flexible matching.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new trusted domain pattern. Use for partner domains or approved senders that should bypass recent domain registration and similarity checks. Configure whether it prevents recent domain or spoof dispositions.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trusted_domain_id"><code>trusted_domain_id</code></a></td>
    <td></td>
    <td>Updates an existing trusted domain pattern. Only provided fields will be modified. Changes take effect for new emails matching the pattern.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trusted_domain_id"><code>trusted_domain_id</code></a></td>
    <td></td>
    <td>Removes a trusted domain pattern. After deletion, emails from this domain will be subject to normal recent domain and similarity checks.</td>
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
<tr id="parameter-trusted_domain_id">
    <td><CopyableCode code="trusted_domain_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The sorting direction.</td>
</tr>
<tr id="parameter-is_recent">
    <td><CopyableCode code="is_recent" /></td>
    <td><code>boolean</code></td>
    <td>Filter to show only recently registered domains that are trusted to prevent triggering Suspicious or Malicious dispositions.</td>
</tr>
<tr id="parameter-is_similarity">
    <td><CopyableCode code="is_similarity" /></td>
    <td><code>boolean</code></td>
    <td>Filter to show only proximity domains (partner or approved domains with similar spelling to connected domains) that prevent Spoof dispositions.</td>
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
    <td></td>
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

Retrieves details for a specific trusted domain pattern including its pattern value, whether it uses regex matching, and which detection types it affects.

```sql
SELECT
id,
comments,
created_at,
is_recent,
is_regex,
is_similarity,
last_modified,
modified_at,
pattern
FROM cloudflare.email_security.trusted_domains
WHERE account_id = '{{ account_id }}' -- required
AND trusted_domain_id = '{{ trusted_domain_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of trusted domain patterns. Trusted domains prevent false positives for recently registered domains and lookalike domain detections. Patterns can use regular expressions for flexible matching.

```sql
SELECT
id,
comments,
created_at,
is_recent,
is_regex,
is_similarity,
last_modified,
modified_at,
pattern
FROM cloudflare.email_security.trusted_domains
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND is_recent = '{{ is_recent }}'
AND is_similarity = '{{ is_similarity }}'
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

Creates a new trusted domain pattern. Use for partner domains or approved senders that should bypass recent domain registration and similarity checks. Configure whether it prevents recent domain or spoof dispositions.

```sql
INSERT INTO cloudflare.email_security.trusted_domains (
comments,
is_recent,
is_regex,
is_similarity,
pattern,
account_id
)
SELECT 
'{{ comments }}',
{{ is_recent }},
{{ is_regex }},
{{ is_similarity }},
'{{ pattern }}',
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
- name: trusted_domains
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the trusted_domains resource.
    - name: comments
      value: "{{ comments }}"
    - name: is_recent
      value: {{ is_recent }}
      description: |
        Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.
    - name: is_regex
      value: {{ is_regex }}
    - name: is_similarity
      value: {{ is_similarity }}
      description: |
        Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.
    - name: pattern
      value: "{{ pattern }}"
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

Updates an existing trusted domain pattern. Only provided fields will be modified. Changes take effect for new emails matching the pattern.

```sql
UPDATE cloudflare.email_security.trusted_domains
SET 
comments = '{{ comments }}',
is_recent = {{ is_recent }},
is_regex = {{ is_regex }},
is_similarity = {{ is_similarity }},
pattern = '{{ pattern }}'
WHERE 
account_id = '{{ account_id }}' --required
AND trusted_domain_id = '{{ trusted_domain_id }}' --required
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

Removes a trusted domain pattern. After deletion, emails from this domain will be subject to normal recent domain and similarity checks.

```sql
DELETE FROM cloudflare.email_security.trusted_domains
WHERE account_id = '{{ account_id }}' --required
AND trusted_domain_id = '{{ trusted_domain_id }}' --required
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
EXEC cloudflare.email_security.trusted_domains.batch 
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
