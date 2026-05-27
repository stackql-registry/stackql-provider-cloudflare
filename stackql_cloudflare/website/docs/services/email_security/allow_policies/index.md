--- 
title: allow_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - allow_policies
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

Creates, updates, deletes, gets or lists an <code>allow_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="allow_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.allow_policies" /></td></tr>
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

Allow policy details

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
    <td>Allow policy identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Trust all messages send from test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_acceptable_sender" /></td>
    <td><code>boolean</code></td>
    <td>Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions. Note - This will not exempt messages with Malicious or Suspicious dispositions.</td>
</tr>
<tr>
    <td><CopyableCode code="is_exempt_recipient" /></td>
    <td><code>boolean</code></td>
    <td>Messages to this recipient will bypass all detections</td>
</tr>
<tr>
    <td><CopyableCode code="is_recipient" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated as of July 1, 2025. Use `is_exempt_recipient` instead. End of life: July 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="is_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_sender" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated as of July 1, 2025. Use `is_trusted_sender` instead. End of life: July 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="is_spoof" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated as of July 1, 2025. Use `is_acceptable_sender` instead. End of life: July 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="is_trusted_sender" /></td>
    <td><code>boolean</code></td>
    <td>Messages from this sender will bypass all detections and link following</td>
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
<tr>
    <td><CopyableCode code="verify_sender" /></td>
    <td><code>boolean</code></td>
    <td>Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors policies that pass authentication.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of allow policies

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
    <td>Allow policy identifier (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td> (example: Trust all messages send from test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="is_acceptable_sender" /></td>
    <td><code>boolean</code></td>
    <td>Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions. Note - This will not exempt messages with Malicious or Suspicious dispositions.</td>
</tr>
<tr>
    <td><CopyableCode code="is_exempt_recipient" /></td>
    <td><code>boolean</code></td>
    <td>Messages to this recipient will bypass all detections</td>
</tr>
<tr>
    <td><CopyableCode code="is_recipient" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated as of July 1, 2025. Use `is_exempt_recipient` instead. End of life: July 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="is_regex" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_sender" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated as of July 1, 2025. Use `is_trusted_sender` instead. End of life: July 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="is_spoof" /></td>
    <td><code>boolean</code></td>
    <td>Deprecated as of July 1, 2025. Use `is_acceptable_sender` instead. End of life: July 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="is_trusted_sender" /></td>
    <td><code>boolean</code></td>
    <td>Messages from this sender will bypass all detections and link following</td>
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
<tr>
    <td><CopyableCode code="verify_sender" /></td>
    <td><code>boolean</code></td>
    <td>Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors policies that pass authentication.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific allow policy including its pattern, dispositions that are exempted, and whether it applies to all detections.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-is_exempt_recipient"><code>is_exempt_recipient</code></a>, <a href="#parameter-is_trusted_sender"><code>is_trusted_sender</code></a>, <a href="#parameter-is_acceptable_sender"><code>is_acceptable_sender</code></a>, <a href="#parameter-verify_sender"><code>verify_sender</code></a>, <a href="#parameter-pattern_type"><code>pattern_type</code></a>, <a href="#parameter-pattern"><code>pattern</code></a></td>
    <td>Returns a paginated list of email allow policies. These policies exempt matching emails from security detection, allowing them to bypass disposition actions. Supports filtering by pattern type and policy attributes.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-created_at"><code>created_at</code></a>, <a href="#parameter-last_modified"><code>last_modified</code></a></td>
    <td></td>
    <td>Creates a new allow policy that exempts matching emails from security detections. Use with caution as this bypasses email security scanning. Policies can match on sender patterns and apply to specific detections or all detections.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-created_at"><code>created_at</code></a>, <a href="#parameter-last_modified"><code>last_modified</code></a></td>
    <td></td>
    <td>Updates an existing allow policy. Only provided fields will be modified. Changes take effect for new emails matching the pattern.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Removes an allow policy. After deletion, emails matching this pattern will be subject to normal security scanning and disposition actions.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The sorting direction.</td>
</tr>
<tr id="parameter-is_acceptable_sender">
    <td><CopyableCode code="is_acceptable_sender" /></td>
    <td><code>boolean</code></td>
    <td>Filter to show only policies where messages from the sender are exempted from Spam, Spoof, and Bulk dispositions (not Malicious or Suspicious).</td>
</tr>
<tr id="parameter-is_exempt_recipient">
    <td><CopyableCode code="is_exempt_recipient" /></td>
    <td><code>boolean</code></td>
    <td>Filter to show only policies where messages to the recipient bypass all detections.</td>
</tr>
<tr id="parameter-is_trusted_sender">
    <td><CopyableCode code="is_trusted_sender" /></td>
    <td><code>boolean</code></td>
    <td>Filter to show only policies where messages from the sender bypass all detections and link following.</td>
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
<tr id="parameter-pattern_type">
    <td><CopyableCode code="pattern_type" /></td>
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
<tr id="parameter-verify_sender">
    <td><CopyableCode code="verify_sender" /></td>
    <td><code>boolean</code></td>
    <td>Filter to show only policies that enforce DMARC, SPF, or DKIM authentication.</td>
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

Retrieves details for a specific allow policy including its pattern, dispositions that are exempted, and whether it applies to all detections.

```sql
SELECT
id,
comments,
created_at,
is_acceptable_sender,
is_exempt_recipient,
is_recipient,
is_regex,
is_sender,
is_spoof,
is_trusted_sender,
last_modified,
modified_at,
pattern,
pattern_type,
verify_sender
FROM cloudflare.email_security.allow_policies
WHERE account_id = '{{ account_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of email allow policies. These policies exempt matching emails from security detection, allowing them to bypass disposition actions. Supports filtering by pattern type and policy attributes.

```sql
SELECT
id,
comments,
created_at,
is_acceptable_sender,
is_exempt_recipient,
is_recipient,
is_regex,
is_sender,
is_spoof,
is_trusted_sender,
last_modified,
modified_at,
pattern,
pattern_type,
verify_sender
FROM cloudflare.email_security.allow_policies
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND is_exempt_recipient = '{{ is_exempt_recipient }}'
AND is_trusted_sender = '{{ is_trusted_sender }}'
AND is_acceptable_sender = '{{ is_acceptable_sender }}'
AND verify_sender = '{{ verify_sender }}'
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

Creates a new allow policy that exempts matching emails from security detections. Use with caution as this bypasses email security scanning. Policies can match on sender patterns and apply to specific detections or all detections.

```sql
INSERT INTO cloudflare.email_security.allow_policies (
comments,
is_acceptable_sender,
is_exempt_recipient,
is_recipient,
is_regex,
is_sender,
is_spoof,
is_trusted_sender,
pattern,
pattern_type,
verify_sender,
account_id
)
SELECT 
'{{ comments }}',
{{ is_acceptable_sender }},
{{ is_exempt_recipient }},
{{ is_recipient }},
{{ is_regex }},
{{ is_sender }},
{{ is_spoof }},
{{ is_trusted_sender }},
'{{ pattern }}',
'{{ pattern_type }}',
{{ verify_sender }},
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
- name: allow_policies
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the allow_policies resource.
    - name: comments
      value: "{{ comments }}"
    - name: is_acceptable_sender
      value: {{ is_acceptable_sender }}
      description: |
        Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions. Note - This will not exempt messages with Malicious or Suspicious dispositions.
    - name: is_exempt_recipient
      value: {{ is_exempt_recipient }}
      description: |
        Messages to this recipient will bypass all detections
    - name: is_recipient
      value: {{ is_recipient }}
      description: |
        Deprecated as of July 1, 2025. Use \`is_exempt_recipient\` instead. End of life: July 1, 2026.
    - name: is_regex
      value: {{ is_regex }}
    - name: is_sender
      value: {{ is_sender }}
      description: |
        Deprecated as of July 1, 2025. Use \`is_trusted_sender\` instead. End of life: July 1, 2026.
    - name: is_spoof
      value: {{ is_spoof }}
      description: |
        Deprecated as of July 1, 2025. Use \`is_acceptable_sender\` instead. End of life: July 1, 2026.
    - name: is_trusted_sender
      value: {{ is_trusted_sender }}
      description: |
        Messages from this sender will bypass all detections and link following
    - name: pattern
      value: "{{ pattern }}"
    - name: pattern_type
      value: "{{ pattern_type }}"
      description: |
        Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when creating or updating policies, but may be returned for existing entries.
      valid_values: ['EMAIL', 'DOMAIN', 'IP', 'UNKNOWN']
    - name: verify_sender
      value: {{ verify_sender }}
      description: |
        Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors policies that pass authentication.
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

Updates an existing allow policy. Only provided fields will be modified. Changes take effect for new emails matching the pattern.

```sql
UPDATE cloudflare.email_security.allow_policies
SET 
comments = '{{ comments }}',
is_acceptable_sender = {{ is_acceptable_sender }},
is_exempt_recipient = {{ is_exempt_recipient }},
is_recipient = {{ is_recipient }},
is_regex = {{ is_regex }},
is_sender = {{ is_sender }},
is_spoof = {{ is_spoof }},
is_trusted_sender = {{ is_trusted_sender }},
pattern = '{{ pattern }}',
pattern_type = '{{ pattern_type }}',
verify_sender = {{ verify_sender }}
WHERE 
account_id = '{{ account_id }}' --required
AND policy_id = '{{ policy_id }}' --required
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

Removes an allow policy. After deletion, emails matching this pattern will be subject to normal security scanning and disposition actions.

```sql
DELETE FROM cloudflare.email_security.allow_policies
WHERE account_id = '{{ account_id }}' --required
AND policy_id = '{{ policy_id }}' --required
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
EXEC cloudflare.email_security.allow_policies.batch 
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
