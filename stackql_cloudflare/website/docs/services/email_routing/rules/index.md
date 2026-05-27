--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - email_routing
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_routing.rules" /></td></tr>
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

Get routing rule response

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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Whether the API call was successful. (true)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List routing rules response

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
    <td>Routing rule identifier. (example: a7e6fb77503c41d8a7f3113c6918f10c)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Routing rule name. (example: Send to user@example.net rule.)</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>List actions patterns.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Routing rule status. (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="matchers" /></td>
    <td><code>array</code></td>
    <td>Matching patterns to forward to your actions.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number</code></td>
    <td>Priority of the routing rule.</td>
</tr>
<tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td>Routing rule tag. (Deprecated, replaced by routing rule identifier) (example: a7e6fb77503c41d8a7f3113c6918f10c)</td>
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
    <td><a href="#parameter-rule_identifier"><code>rule_identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Get information for a specific routing rule already created.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td>Lists existing routing rules.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-actions"><code>actions</code></a>, <a href="#parameter-matchers"><code>matchers</code></a></td>
    <td></td>
    <td>Rules consist of a set of criteria for matching emails (such as an email being sent to a specific custom email address) plus a set of actions to take on the email (like forwarding it to a specific destination address). Forward actions require all destination addresses to be verified.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-rule_identifier"><code>rule_identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-actions"><code>actions</code></a>, <a href="#parameter-matchers"><code>matchers</code></a></td>
    <td></td>
    <td>Update actions and matches, or enable/disable specific routing rules. Forward actions require all destination addresses to be verified.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_identifier"><code>rule_identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Delete a specific routing rule.</td>
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
<tr id="parameter-rule_identifier">
    <td><CopyableCode code="rule_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-enabled">
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
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

Get information for a specific routing rule already created.

```sql
SELECT
errors,
messages,
result,
success
FROM cloudflare.email_routing.rules
WHERE rule_identifier = '{{ rule_identifier }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists existing routing rules.

```sql
SELECT
id,
name,
actions,
enabled,
matchers,
priority,
tag
FROM cloudflare.email_routing.rules
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND enabled = '{{ enabled }}'
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

Rules consist of a set of criteria for matching emails (such as an email being sent to a specific custom email address) plus a set of actions to take on the email (like forwarding it to a specific destination address). Forward actions require all destination addresses to be verified.

```sql
INSERT INTO cloudflare.email_routing.rules (
actions,
enabled,
matchers,
name,
priority,
zone_id
)
SELECT 
'{{ actions }}' /* required */,
{{ enabled }},
'{{ matchers }}' /* required */,
'{{ name }}',
{{ priority }},
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
    - name: actions
      description: |
        List actions patterns.
      value:
        - type: "{{ type }}"
          value: "{{ value }}"
    - name: enabled
      value: {{ enabled }}
      description: |
        Routing rule status.
      valid_values: ['true', 'false']
      default: true
    - name: matchers
      description: |
        Matching patterns to forward to your actions.
      value:
        - field: "{{ field }}"
          type: "{{ type }}"
          value: "{{ value }}"
    - name: name
      value: "{{ name }}"
      description: |
        Routing rule name.
    - name: priority
      value: {{ priority }}
      description: |
        Priority of the routing rule.
      default: 0
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

Update actions and matches, or enable/disable specific routing rules. Forward actions require all destination addresses to be verified.

```sql
REPLACE cloudflare.email_routing.rules
SET 
actions = '{{ actions }}',
enabled = {{ enabled }},
matchers = '{{ matchers }}',
name = '{{ name }}',
priority = {{ priority }}
WHERE 
rule_identifier = '{{ rule_identifier }}' --required
AND zone_id = '{{ zone_id }}' --required
AND actions = '{{ actions }}' --required
AND matchers = '{{ matchers }}' --required
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

Delete a specific routing rule.

```sql
DELETE FROM cloudflare.email_routing.rules
WHERE rule_identifier = '{{ rule_identifier }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
