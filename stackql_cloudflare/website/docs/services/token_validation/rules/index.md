--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - token_validation
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.token_validation.rules" /></td></tr>
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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>Action to take on requests that match operations included in `selector` and fail `expression`. (log, block) (example: log)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description that gives more details than `title`. (example: Long description for Token Validation Rule)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Toggle rule on or off.</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>Rule expression. Requests that fail to match this expression will be subject to `action`. For details on expressions, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/). (example: is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423"))</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="selector" /></td>
    <td><code>object</code></td>
    <td>Select operations covered by this rule. For details on selectors, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>A human-readable name for the rule. (example: Example Token Validation Rule)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>Action to take on requests that match operations included in `selector` and fail `expression`. (log, block) (example: log)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description that gives more details than `title`. (example: Long description for Token Validation Rule)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Toggle rule on or off.</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>Rule expression. Requests that fail to match this expression will be subject to `action`. For details on expressions, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/). (example: is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423"))</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="selector" /></td>
    <td><code>object</code></td>
    <td>Select operations covered by this rule. For details on selectors, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>A human-readable name for the rule. (example: Example Token Validation Rule)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Get a zone token validation rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-token_configuration"><code>token_configuration</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-hostname"><code>hostname</code></a></td>
    <td>List token validation rules</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Create a token validation rule.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Edit a zone token validation rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Delete a zone token validation rule.</td>
</tr>
<tr>
    <td><a href="#bulk_edit"><CopyableCode code="bulk_edit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Edit token validation rules. A request can update multiple Token Validation Rules. Rules can be re-ordered using the `position` field. Returns all updated rules.</td>
</tr>
<tr>
    <td><a href="#bulk_create"><CopyableCode code="bulk_create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Create zone token validation rules. A request can create multiple Token Validation Rules.</td>
</tr>
<tr>
    <td><a href="#preview"><CopyableCode code="preview" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-state"><code>state</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-method"><code>method</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td>Preview operations covered by a Token Validation rule. The API will return all operations on a zone annotated with an additional `state` field. Operations with an `included` `state` will be covered by a Token Validation Rule.</td>
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
<tr id="parameter-rule_id">
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td>The rule ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-action">
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-enabled">
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>array</code></td>
    <td>Filter operations by endpoint. Allows substring matching.</td>
</tr>
<tr id="parameter-host">
    <td><CopyableCode code="host" /></td>
    <td><code>array</code></td>
    <td>Filter operations by host.</td>
</tr>
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>array</code></td>
    <td>Filter operations by host.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Select rules with these IDs.</td>
</tr>
<tr id="parameter-method">
    <td><CopyableCode code="method" /></td>
    <td><code>array</code></td>
    <td>Filter operations by method.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number of paginated results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of results per page.</td>
</tr>
<tr id="parameter-rule_id">
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td>Select rules with these IDs.</td>
</tr>
<tr id="parameter-state">
    <td><CopyableCode code="state" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-token_configuration">
    <td><CopyableCode code="token_configuration" /></td>
    <td><code>array</code></td>
    <td>Select rules using any of these token configurations.</td>
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

Get a zone token validation rule.

```sql
SELECT
id,
action,
created_at,
description,
enabled,
expression,
last_updated,
selector,
title
FROM cloudflare.token_validation.rules
WHERE zone_id = '{{ zone_id }}' -- required
AND rule_id = '{{ rule_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List token validation rules

```sql
SELECT
id,
action,
created_at,
description,
enabled,
expression,
last_updated,
selector,
title
FROM cloudflare.token_validation.rules
WHERE zone_id = '{{ zone_id }}' -- required
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
AND token_configuration = '{{ token_configuration }}'
AND action = '{{ action }}'
AND enabled = '{{ enabled }}'
AND id = '{{ id }}'
AND rule_id = '{{ rule_id }}'
AND host = '{{ host }}'
AND hostname = '{{ hostname }}'
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

Create a token validation rule.

```sql
INSERT INTO cloudflare.token_validation.rules (
action,
description,
enabled,
expression,
selector,
title,
zone_id
)
SELECT 
'{{ action }}',
'{{ description }}',
{{ enabled }},
'{{ expression }}',
'{{ selector }}',
'{{ title }}',
'{{ zone_id }}'
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
- name: rules
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the rules resource.
    - name: action
      value: "{{ action }}"
      description: |
        Action to take on requests that match operations included in \`selector\` and fail \`expression\`.
      valid_values: ['log', 'block']
    - name: description
      value: "{{ description }}"
      description: |
        A human-readable description that gives more details than \`title\`.
    - name: enabled
      value: {{ enabled }}
      description: |
        Toggle rule on or off.
    - name: expression
      value: "{{ expression }}"
      description: |
        Rule expression. Requests that fail to match this expression will be subject to \`action\`. For details on expressions, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
    - name: selector
      description: |
        Select operations covered by this rule. For details on selectors, see the [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).
      value:
        exclude:
          - operation_ids: "{{ operation_ids }}"
        include:
          - host: "{{ host }}"
    - name: title
      value: "{{ title }}"
      description: |
        A human-readable name for the rule.
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

Edit a zone token validation rule.

```sql
UPDATE cloudflare.token_validation.rules
SET 
action = '{{ action }}',
description = '{{ description }}',
enabled = {{ enabled }},
expression = '{{ expression }}',
selector = '{{ selector }}',
title = '{{ title }}',
position = '{{ position }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND rule_id = '{{ rule_id }}' --required
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

Delete a zone token validation rule.

```sql
DELETE FROM cloudflare.token_validation.rules
WHERE zone_id = '{{ zone_id }}' --required
AND rule_id = '{{ rule_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="bulk_edit"
    values={[
        { label: 'bulk_edit', value: 'bulk_edit' },
        { label: 'bulk_create', value: 'bulk_create' },
        { label: 'preview', value: 'preview' }
    ]}
>
<TabItem value="bulk_edit">

Edit token validation rules. A request can update multiple Token Validation Rules. Rules can be re-ordered using the `position` field. Returns all updated rules.

```sql
EXEC cloudflare.token_validation.rules.bulk_edit 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_create">

Create zone token validation rules. A request can create multiple Token Validation Rules.

```sql
EXEC cloudflare.token_validation.rules.bulk_create 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="preview">

Preview operations covered by a Token Validation rule. The API will return all operations on a zone annotated with an additional `state` field. Operations with an `included` `state` will be covered by a Token Validation Rule.

```sql
EXEC cloudflare.token_validation.rules.preview 
@zone_id='{{ zone_id }}' --required, 
@per_page='{{ per_page }}', 
@page='{{ page }}', 
@state='{{ state }}', 
@host='{{ host }}', 
@hostname='{{ hostname }}', 
@method='{{ method }}', 
@endpoint='{{ endpoint }}' 
@@json=
'{
"exclude": "{{ exclude }}", 
"include": "{{ include }}"
}'
;
```
</TabItem>
</Tabs>
