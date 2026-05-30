--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - rulesets
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rulesets.rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Adds a new rule to an account or zone ruleset. The rule will be added to the end of the existing list of rules in the ruleset by default.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Adds a new rule to an account or zone ruleset. The rule will be added to the end of the existing list of rules in the ruleset by default.</td>
</tr>
<tr>
    <td><a href="#edit_by_account"><CopyableCode code="edit_by_account" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates an existing rule in an account or zone ruleset.</td>
</tr>
<tr>
    <td><a href="#edit_by_zone"><CopyableCode code="edit_by_zone" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates an existing rule in an account or zone ruleset.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an existing rule from an account or zone ruleset.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing rule from an account or zone ruleset.</td>
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
<tr id="parameter-rule_id">
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td>The rule ID.</td>
</tr>
<tr id="parameter-ruleset_id">
    <td><CopyableCode code="ruleset_id" /></td>
    <td><code>string</code></td>
    <td>The ruleset ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'create_by_zone', value: 'create_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Adds a new rule to an account or zone ruleset. The rule will be added to the end of the existing list of rules in the ruleset by default.

```sql
INSERT INTO cloudflare.rulesets.rules (
position,
action,
action_parameters,
description,
enabled,
exposed_credential_check,
expression,
id,
logging,
ratelimit,
ref,
ruleset_id,
account_id
)
SELECT 
'{{ position }}',
'{{ action }}',
'{{ action_parameters }}',
'{{ description }}',
{{ enabled }},
'{{ exposed_credential_check }}',
'{{ expression }}',
'{{ id }}',
'{{ logging }}',
'{{ ratelimit }}',
'{{ ref }}',
'{{ ruleset_id }}',
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="create_by_zone">

Adds a new rule to an account or zone ruleset. The rule will be added to the end of the existing list of rules in the ruleset by default.

```sql
INSERT INTO cloudflare.rulesets.rules (
position,
action,
action_parameters,
description,
enabled,
exposed_credential_check,
expression,
id,
logging,
ratelimit,
ref,
ruleset_id,
zone_id
)
SELECT 
'{{ position }}',
'{{ action }}',
'{{ action_parameters }}',
'{{ description }}',
{{ enabled }},
'{{ exposed_credential_check }}',
'{{ expression }}',
'{{ id }}',
'{{ logging }}',
'{{ ratelimit }}',
'{{ ref }}',
'{{ ruleset_id }}',
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
    - name: ruleset_id
      value: "{{ ruleset_id }}"
      description: Required parameter for the rules resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the rules resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the rules resource.
    - name: position
      description: |
        An object configuring where the rule will be placed.
      value:
        before: "{{ before }}"
        after: "{{ after }}"
        index: {{ index }}
    - name: action
      value: "{{ action }}"
      description: |
        The action to perform when the rule matches.
      valid_values: ['block']
    - name: action_parameters
      description: |
        The parameters configuring the rule's action.
      value:
        response:
          content: "{{ content }}"
          content_type: "{{ content_type }}"
          status_code: {{ status_code }}
      default: [object Object]
    - name: description
      value: "{{ description }}"
      description: |
        An informative description of the rule.
      default: 
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether the rule should be executed.
      default: true
    - name: exposed_credential_check
      description: |
        Configuration for exposed credential checking.
      value:
        password_expression: "{{ password_expression }}"
        username_expression: "{{ username_expression }}"
    - name: expression
      value: "{{ expression }}"
      description: |
        The expression defining which traffic will match the rule.
    - name: id
      value: "{{ id }}"
      description: |
        The unique ID of the rule.
    - name: logging
      description: |
        An object configuring the rule's logging behavior.
      value:
        enabled: {{ enabled }}
    - name: ratelimit
      description: |
        An object configuring the rule's rate limit behavior.
      value:
        characteristics:
          - "{{ characteristics }}"
        counting_expression: "{{ counting_expression }}"
        mitigation_timeout: {{ mitigation_timeout }}
        period: {{ period }}
        requests_per_period: {{ requests_per_period }}
        requests_to_origin: {{ requests_to_origin }}
        score_per_period: {{ score_per_period }}
        score_response_header_name: "{{ score_response_header_name }}"
    - name: ref
      value: "{{ ref }}"
      description: |
        The reference of the rule (the rule's ID by default).
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit_by_account"
    values={[
        { label: 'edit_by_account', value: 'edit_by_account' },
        { label: 'edit_by_zone', value: 'edit_by_zone' }
    ]}
>
<TabItem value="edit_by_account">

Updates an existing rule in an account or zone ruleset.

```sql
UPDATE cloudflare.rulesets.rules
SET 
position = '{{ position }}',
action = '{{ action }}',
action_parameters = '{{ action_parameters }}',
description = '{{ description }}',
enabled = {{ enabled }},
exposed_credential_check = '{{ exposed_credential_check }}',
expression = '{{ expression }}',
id = '{{ id }}',
logging = '{{ logging }}',
ratelimit = '{{ ratelimit }}',
ref = '{{ ref }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND ruleset_id = '{{ ruleset_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="edit_by_zone">

Updates an existing rule in an account or zone ruleset.

```sql
UPDATE cloudflare.rulesets.rules
SET 
position = '{{ position }}',
action = '{{ action }}',
action_parameters = '{{ action_parameters }}',
description = '{{ description }}',
enabled = {{ enabled }},
exposed_credential_check = '{{ exposed_credential_check }}',
expression = '{{ expression }}',
id = '{{ id }}',
logging = '{{ logging }}',
ratelimit = '{{ ratelimit }}',
ref = '{{ ref }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND ruleset_id = '{{ ruleset_id }}' --required
AND zone_id = '{{ zone_id }}' --required
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
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' },
        { label: 'delete_by_zone', value: 'delete_by_zone' }
    ]}
>
<TabItem value="delete_by_account">

Deletes an existing rule from an account or zone ruleset.

```sql
DELETE FROM cloudflare.rulesets.rules
WHERE rule_id = '{{ rule_id }}' --required
AND ruleset_id = '{{ ruleset_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an existing rule from an account or zone ruleset.

```sql
DELETE FROM cloudflare.rulesets.rules
WHERE rule_id = '{{ rule_id }}' --required
AND ruleset_id = '{{ ruleset_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
