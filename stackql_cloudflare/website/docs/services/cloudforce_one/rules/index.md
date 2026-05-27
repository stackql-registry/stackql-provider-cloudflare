--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - cloudforce_one
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.rules" /></td></tr>
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

Rule details.

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
    <td> (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: block-malicious-workers)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td> (example: rule example &#123; condition: true &#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td> (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Detects malicious proxy workers)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether this rule is active for dice consumers.</td>
</tr>
<tr>
    <td><CopyableCode code="is_public" /></td>
    <td><code>boolean</code></td>
    <td>Whether this rule is visible to other internal accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaces" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><code>string</code></td>
    <td> (example: user@example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of rules.

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
    <td> (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: block-malicious-workers)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td> (example: rule example &#123; condition: true &#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td> (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Detects malicious proxy workers)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether this rule is active for dice consumers.</td>
</tr>
<tr>
    <td><CopyableCode code="is_public" /></td>
    <td><code>boolean</code></td>
    <td>Whether this rule is visible to other internal accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="namespaces" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><code>string</code></td>
    <td> (example: user@example.com)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Get a single rule by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-namespace"><code>namespace</code></a>, <a href="#parameter-recursive"><code>recursive</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-is_public"><code>is_public</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a></td>
    <td>List all rules for an account with optional filtering.</td>
</tr>
<tr>
    <td><a href="#cloudforce_one_create_rule"><CopyableCode code="cloudforce_one_create_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespaces"><code>namespaces</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td>Create a new detection rule.</td>
</tr>
<tr>
    <td><a href="#cloudforce_one_update_rule"><CopyableCode code="cloudforce_one_update_rule" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Update an existing rule.</td>
</tr>
<tr>
    <td><a href="#cloudforce_one_delete_rule"><CopyableCode code="cloudforce_one_delete_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Delete an existing rule.</td>
</tr>
<tr>
    <td><a href="#cloudforce_one_delete_all_rules"><CopyableCode code="cloudforce_one_delete_all_rules" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete all rules in an account.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespaces"><code>namespaces</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td>Validate rule syntax, name uniqueness, namespace, and meta checks.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr id="parameter-is_public">
    <td><CopyableCode code="is_public" /></td>
    <td><code>string</code></td>
    <td>Filter by public visibility.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-namespace">
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>Filter by namespace. Repeat the parameter to filter by multiple namespaces (e.g. namespace=foo&namespace=bar).</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-recursive">
    <td><CopyableCode code="recursive" /></td>
    <td><code>string</code></td>
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

Get a single rule by ID.

```sql
SELECT
id,
name,
content,
created_at,
created_by,
description,
enabled,
is_public,
namespaces,
updated_at,
updated_by
FROM cloudflare.cloudforce_one.rules
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all rules for an account with optional filtering.

```sql
SELECT
id,
name,
content,
created_at,
created_by,
description,
enabled,
is_public,
namespaces,
updated_at,
updated_by
FROM cloudflare.cloudforce_one.rules
WHERE account_id = '{{ account_id }}' -- required
AND namespace = '{{ namespace }}'
AND recursive = '{{ recursive }}'
AND search = '{{ search }}'
AND is_public = '{{ is_public }}'
AND limit = '{{ limit }}'
AND offset = '{{ offset }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="cloudforce_one_create_rule"
    values={[
        { label: 'cloudforce_one_create_rule', value: 'cloudforce_one_create_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="cloudforce_one_create_rule">

Create a new detection rule.

```sql
INSERT INTO cloudflare.cloudforce_one.rules (
actions,
content,
description,
enabled,
is_public,
name,
namespaces,
account_id
)
SELECT 
'{{ actions }}',
'{{ content }}' /* required */,
'{{ description }}',
{{ enabled }},
{{ is_public }},
'{{ name }}' /* required */,
'{{ namespaces }}' /* required */,
'{{ account_id }}'
RETURNING
id,
name,
content,
created_at,
created_by,
description,
enabled,
is_public,
namespaces,
updated_at,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: rules
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the rules resource.
    - name: actions
      value:
        - action_config: "{{ action_config }}"
          action_type: "{{ action_type }}"
          enabled: {{ enabled }}
    - name: content
      value: "{{ content }}"
    - name: description
      value: "{{ description }}"
      description: |
        Human-readable description of the rule. Auto-extracted from YARA meta if present.
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether this rule is active for dice consumers.
      default: true
    - name: is_public
      value: {{ is_public }}
      description: |
        Whether this rule is visible to other internal accounts.
      default: false
    - name: name
      value: "{{ name }}"
    - name: namespaces
      value:
        - "{{ namespaces }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="cloudforce_one_update_rule"
    values={[
        { label: 'cloudforce_one_update_rule', value: 'cloudforce_one_update_rule' }
    ]}
>
<TabItem value="cloudforce_one_update_rule">

Update an existing rule.

```sql
REPLACE cloudflare.cloudforce_one.rules
SET 
content = '{{ content }}',
description = '{{ description }}',
enabled = {{ enabled }},
is_public = {{ is_public }},
name = '{{ name }}',
namespaces = '{{ namespaces }}'
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
RETURNING
id,
name,
content,
created_at,
created_by,
description,
enabled,
is_public,
namespaces,
updated_at,
updated_by;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="cloudforce_one_delete_rule"
    values={[
        { label: 'cloudforce_one_delete_rule', value: 'cloudforce_one_delete_rule' },
        { label: 'cloudforce_one_delete_all_rules', value: 'cloudforce_one_delete_all_rules' }
    ]}
>
<TabItem value="cloudforce_one_delete_rule">

Delete an existing rule.

```sql
DELETE FROM cloudflare.cloudforce_one.rules
WHERE account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
;
```
</TabItem>
<TabItem value="cloudforce_one_delete_all_rules">

Delete all rules in an account.

```sql
DELETE FROM cloudflare.cloudforce_one.rules
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate"
    values={[
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="validate">

Validate rule syntax, name uniqueness, namespace, and meta checks.

```sql
EXEC cloudflare.cloudforce_one.rules.validate 
@account_id='{{ account_id }}' --required 
@@json=
'{
"content": "{{ content }}", 
"excludeRuleId": "{{ excludeRuleId }}", 
"name": "{{ name }}", 
"namespaces": "{{ namespaces }}"
}'
;
```
</TabItem>
</Tabs>
