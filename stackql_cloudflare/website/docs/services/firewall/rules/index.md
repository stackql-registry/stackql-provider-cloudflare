--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - firewall
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.rules" /></td></tr>
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
    <td><a href="#firewall_rules_create_firewall_rules"><CopyableCode code="firewall_rules_create_firewall_rules" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Create one or more firewall rules.</td>
</tr>
<tr>
    <td><a href="#ip_access_rules_for_a_user_create_an_ip_access_rule"><CopyableCode code="ip_access_rules_for_a_user_create_an_ip_access_rule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Creates a new IP Access rule for all zones owned by the current user. Note: To create an IP Access rule that applies to a specific zone, refer to the IP Access rules for a zone endpoints.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-package_id"><code>package_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates a WAF rule. You can only update the mode/action of the rule. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).</td>
</tr>
<tr>
    <td><a href="#firewall_rules_update_priority_of_a_firewall_rule"><CopyableCode code="firewall_rules_update_priority_of_a_firewall_rule" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Updates the priority of an existing firewall rule.</td>
</tr>
<tr>
    <td><a href="#ip_access_rules_for_a_user_update_an_ip_access_rule"><CopyableCode code="ip_access_rules_for_a_user_update_an_ip_access_rule" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Updates an IP Access rule defined at the user level. You can only update the rule action (`mode` parameter) and notes.</td>
</tr>
<tr>
    <td><a href="#firewall_rules_update_priority_of_firewall_rules"><CopyableCode code="firewall_rules_update_priority_of_firewall_rules" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates the priority of existing firewall rules.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Updates an existing firewall rule.</td>
</tr>
<tr>
    <td><a href="#firewall_rules_update_firewall_rules"><CopyableCode code="firewall_rules_update_firewall_rules" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates one or more existing firewall rules.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing firewall rule.</td>
</tr>
<tr>
    <td><a href="#ip_access_rules_for_a_user_delete_an_ip_access_rule"><CopyableCode code="ip_access_rules_for_a_user_delete_an_ip_access_rule" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Deletes an IP Access rule at the user level. Note: Deleting a user-level rule will affect all zones owned by the user.</td>
</tr>
<tr>
    <td><a href="#firewall_rules_delete_firewall_rules"><CopyableCode code="firewall_rules_delete_firewall_rules" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes existing firewall rules.</td>
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
<tr id="parameter-package_id">
    <td><CopyableCode code="package_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="firewall_rules_create_firewall_rules"
    values={[
        { label: 'firewall_rules_create_firewall_rules', value: 'firewall_rules_create_firewall_rules' },
        { label: 'ip_access_rules_for_a_user_create_an_ip_access_rule', value: 'ip_access_rules_for_a_user_create_an_ip_access_rule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="firewall_rules_create_firewall_rules">

Create one or more firewall rules.

```sql
INSERT INTO cloudflare.firewall.rules (
action,
filter,
zone_id
)
SELECT 
'{{ action }}' /* required */,
'{{ filter }}' /* required */,
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
<TabItem value="ip_access_rules_for_a_user_create_an_ip_access_rule">

Creates a new IP Access rule for all zones owned by the current user. Note: To create an IP Access rule that applies to a specific zone, refer to the IP Access rules for a zone endpoints.

```sql
INSERT INTO cloudflare.firewall.rules (
configuration,
mode,
notes
)
SELECT 
'{{ configuration }}' /* required */,
'{{ mode }}' /* required */,
'{{ notes }}'
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
      description: |
        The action to perform when the threshold of matched traffic within the configured period is exceeded.
      value:
        mode: "{{ mode }}"
        response:
          body: "{{ body }}"
          content_type: "{{ content_type }}"
        timeout: {{ timeout }}
    - name: filter
      value:
        description: "{{ description }}"
        expression: "{{ expression }}"
        id: "{{ id }}"
        paused: {{ paused }}
        ref: "{{ ref }}"
    - name: configuration
      description: |
        The rule configuration.
      value:
        target: "{{ target }}"
        value: "{{ value }}"
    - name: mode
      value: "{{ mode }}"
      description: |
        The action to apply to a matched request.
      valid_values: ['block', 'challenge', 'whitelist', 'js_challenge', 'managed_challenge']
    - name: notes
      value: "{{ notes }}"
      description: |
        An informative summary of the rule, typically used as a reminder or explanation.
      default: 
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'firewall_rules_update_priority_of_a_firewall_rule', value: 'firewall_rules_update_priority_of_a_firewall_rule' },
        { label: 'ip_access_rules_for_a_user_update_an_ip_access_rule', value: 'ip_access_rules_for_a_user_update_an_ip_access_rule' },
        { label: 'firewall_rules_update_priority_of_firewall_rules', value: 'firewall_rules_update_priority_of_firewall_rules' }
    ]}
>
<TabItem value="edit">

Updates a WAF rule. You can only update the mode/action of the rule. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

```sql
UPDATE cloudflare.firewall.rules
SET 
mode = '{{ mode }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND package_id = '{{ package_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="firewall_rules_update_priority_of_a_firewall_rule">

Updates the priority of an existing firewall rule.

```sql
UPDATE cloudflare.firewall.rules
SET 
-- No updatable properties
WHERE 
rule_id = '{{ rule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
<TabItem value="ip_access_rules_for_a_user_update_an_ip_access_rule">

Updates an IP Access rule defined at the user level. You can only update the rule action (`mode` parameter) and notes.

```sql
UPDATE cloudflare.firewall.rules
SET 
mode = '{{ mode }}',
notes = '{{ notes }}'
WHERE 
rule_id = '{{ rule_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="firewall_rules_update_priority_of_firewall_rules">

Updates the priority of existing firewall rules.

```sql
UPDATE cloudflare.firewall.rules
SET 
-- No updatable properties
WHERE 
zone_id = '{{ zone_id }}' --required
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
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'firewall_rules_update_firewall_rules', value: 'firewall_rules_update_firewall_rules' }
    ]}
>
<TabItem value="update">

Updates an existing firewall rule.

```sql
REPLACE cloudflare.firewall.rules
SET 
action = '{{ action }}',
filter = '{{ filter }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND filter = '{{ filter }}' --required
AND action = '{{ action }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="firewall_rules_update_firewall_rules">

Updates one or more existing firewall rules.

```sql
REPLACE cloudflare.firewall.rules
SET 
-- No updatable properties
WHERE 
zone_id = '{{ zone_id }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'ip_access_rules_for_a_user_delete_an_ip_access_rule', value: 'ip_access_rules_for_a_user_delete_an_ip_access_rule' },
        { label: 'firewall_rules_delete_firewall_rules', value: 'firewall_rules_delete_firewall_rules' }
    ]}
>
<TabItem value="delete">

Deletes an existing firewall rule.

```sql
DELETE FROM cloudflare.firewall.rules
WHERE rule_id = '{{ rule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="ip_access_rules_for_a_user_delete_an_ip_access_rule">

Deletes an IP Access rule at the user level. Note: Deleting a user-level rule will affect all zones owned by the user.

```sql
DELETE FROM cloudflare.firewall.rules
WHERE rule_id = '{{ rule_id }}' --required
;
```
</TabItem>
<TabItem value="firewall_rules_delete_firewall_rules">

Deletes existing firewall rules.

```sql
DELETE FROM cloudflare.firewall.rules
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
