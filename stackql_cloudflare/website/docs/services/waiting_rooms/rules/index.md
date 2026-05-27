--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - waiting_rooms
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.waiting_rooms.rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List Waiting Room Rules response

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
    <td>The ID of the rule. (example: 25756b2dfe6e378a06b033b670413757)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>The action to take when the expression matches. (bypass_waiting_room) (example: bypass_waiting_room)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the rule. (default: , example: allow all traffic from 10.20.30.40)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, the rule is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>Criteria defining when there is a match for the current rule. (example: ip.src in &#123;10.20.30.40&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the rule. (example: 1)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Lists rules for a waiting room.</td>
</tr>
<tr>
    <td><a href="#waiting_room_create_waiting_room_rule"><CopyableCode code="waiting_room_create_waiting_room_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-expression"><code>expression</code></a></td>
    <td></td>
    <td>Only available for the Waiting Room Advanced subscription. Creates a rule for a waiting room.</td>
</tr>
<tr>
    <td><a href="#waiting_room_patch_waiting_room_rule"><CopyableCode code="waiting_room_patch_waiting_room_rule" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-expression"><code>expression</code></a></td>
    <td></td>
    <td>Patches a rule for a waiting room.</td>
</tr>
<tr>
    <td><a href="#waiting_room_replace_waiting_room_rules"><CopyableCode code="waiting_room_replace_waiting_room_rules" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Only available for the Waiting Room Advanced subscription. Replaces all rules for a waiting room.</td>
</tr>
<tr>
    <td><a href="#waiting_room_delete_waiting_room_rule"><CopyableCode code="waiting_room_delete_waiting_room_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes a rule for a waiting room.</td>
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
<tr id="parameter-waiting_room_id">
    <td><CopyableCode code="waiting_room_id" /></td>
    <td><code>string</code></td>
    <td>The Waiting Room ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists rules for a waiting room.

```sql
SELECT
id,
action,
description,
enabled,
expression,
last_updated,
version
FROM cloudflare.waiting_rooms.rules
WHERE waiting_room_id = '{{ waiting_room_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="waiting_room_create_waiting_room_rule"
    values={[
        { label: 'waiting_room_create_waiting_room_rule', value: 'waiting_room_create_waiting_room_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="waiting_room_create_waiting_room_rule">

Only available for the Waiting Room Advanced subscription. Creates a rule for a waiting room.

```sql
INSERT INTO cloudflare.waiting_rooms.rules (
action,
description,
enabled,
expression,
waiting_room_id,
zone_id
)
SELECT 
'{{ action }}' /* required */,
'{{ description }}',
{{ enabled }},
'{{ expression }}' /* required */,
'{{ waiting_room_id }}',
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: rules
  props:
    - name: waiting_room_id
      value: "{{ waiting_room_id }}"
      description: Required parameter for the rules resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the rules resource.
    - name: action
      value: "{{ action }}"
      description: |
        The action to take when the expression matches.
      valid_values: ['bypass_waiting_room']
    - name: description
      value: "{{ description }}"
      description: |
        The description of the rule.
      default: 
    - name: enabled
      value: {{ enabled }}
      description: |
        When set to true, the rule is enabled.
      default: true
    - name: expression
      value: "{{ expression }}"
      description: |
        Criteria defining when there is a match for the current rule.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="waiting_room_patch_waiting_room_rule"
    values={[
        { label: 'waiting_room_patch_waiting_room_rule', value: 'waiting_room_patch_waiting_room_rule' }
    ]}
>
<TabItem value="waiting_room_patch_waiting_room_rule">

Patches a rule for a waiting room.

```sql
UPDATE cloudflare.waiting_rooms.rules
SET 
action = '{{ action }}',
description = '{{ description }}',
enabled = {{ enabled }},
expression = '{{ expression }}',
position = '{{ position }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND action = '{{ action }}' --required
AND expression = '{{ expression }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="waiting_room_replace_waiting_room_rules"
    values={[
        { label: 'waiting_room_replace_waiting_room_rules', value: 'waiting_room_replace_waiting_room_rules' }
    ]}
>
<TabItem value="waiting_room_replace_waiting_room_rules">

Only available for the Waiting Room Advanced subscription. Replaces all rules for a waiting room.

```sql
REPLACE cloudflare.waiting_rooms.rules
SET 
-- No updatable properties
WHERE 
waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="waiting_room_delete_waiting_room_rule"
    values={[
        { label: 'waiting_room_delete_waiting_room_rule', value: 'waiting_room_delete_waiting_room_rule' }
    ]}
>
<TabItem value="waiting_room_delete_waiting_room_rule">

Deletes a rule for a waiting room.

```sql
DELETE FROM cloudflare.waiting_rooms.rules
WHERE rule_id = '{{ rule_id }}' --required
AND waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
