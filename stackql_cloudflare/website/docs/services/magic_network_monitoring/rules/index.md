--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - magic_network_monitoring
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_network_monitoring.rules" /></td></tr>
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

Get rule response

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
    <td>The id of the rule. Must be unique. (example: 2890e6fa406311ed9b5a23f70f6fb8cf)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9, underscore (_), dash (-), period (.), and tilde (~). You can’t have a space in the rule name. Max 256 characters. (example: my_rule_1)</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_advertisement" /></td>
    <td><code>boolean</code></td>
    <td>Toggle on if you would like Cloudflare to automatically advertise the IP Prefixes within the rule via Magic Transit when the rule is triggered. Only available for users of Magic Transit.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidth_threshold" /></td>
    <td><code>number</code></td>
    <td>The number of bits per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that the rule threshold must be exceeded to send an alert notification. The final value must be equivalent to one of the following 8 values ["1m","5m","10m","15m","20m","30m","45m","60m"]. (1m, 5m, 10m, 15m, 20m, 30m, 45m, 60m) (default: 1m)</td>
</tr>
<tr>
    <td><CopyableCode code="packet_threshold" /></td>
    <td><code>number</code></td>
    <td>The number of packets per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.</td>
</tr>
<tr>
    <td><CopyableCode code="prefix_match" /></td>
    <td><code>string</code></td>
    <td>Prefix match type to be applied for a prefix auto advertisement when using an advanced_ddos rule. (exact, subnet, supernet) (example: exact)</td>
</tr>
<tr>
    <td><CopyableCode code="prefixes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>MNM rule type. (threshold, zscore, advanced_ddos) (example: zscore)</td>
</tr>
<tr>
    <td><CopyableCode code="zscore_sensitivity" /></td>
    <td><code>string</code></td>
    <td>Level of sensitivity set for zscore rules. (low, medium, high) (example: high)</td>
</tr>
<tr>
    <td><CopyableCode code="zscore_target" /></td>
    <td><code>string</code></td>
    <td>Target of the zscore rule analysis. (bits, packets) (example: bits)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List rules response

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
    <td>The id of the rule. Must be unique. (example: 2890e6fa406311ed9b5a23f70f6fb8cf)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9, underscore (_), dash (-), period (.), and tilde (~). You can’t have a space in the rule name. Max 256 characters. (example: my_rule_1)</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_advertisement" /></td>
    <td><code>boolean</code></td>
    <td>Toggle on if you would like Cloudflare to automatically advertise the IP Prefixes within the rule via Magic Transit when the rule is triggered. Only available for users of Magic Transit.</td>
</tr>
<tr>
    <td><CopyableCode code="bandwidth_threshold" /></td>
    <td><code>number</code></td>
    <td>The number of bits per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that the rule threshold must be exceeded to send an alert notification. The final value must be equivalent to one of the following 8 values ["1m","5m","10m","15m","20m","30m","45m","60m"]. (1m, 5m, 10m, 15m, 20m, 30m, 45m, 60m) (default: 1m)</td>
</tr>
<tr>
    <td><CopyableCode code="packet_threshold" /></td>
    <td><code>number</code></td>
    <td>The number of packets per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.</td>
</tr>
<tr>
    <td><CopyableCode code="prefix_match" /></td>
    <td><code>string</code></td>
    <td>Prefix match type to be applied for a prefix auto advertisement when using an advanced_ddos rule. (exact, subnet, supernet) (example: exact)</td>
</tr>
<tr>
    <td><CopyableCode code="prefixes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>MNM rule type. (threshold, zscore, advanced_ddos) (example: zscore)</td>
</tr>
<tr>
    <td><CopyableCode code="zscore_sensitivity" /></td>
    <td><code>string</code></td>
    <td>Level of sensitivity set for zscore rules. (low, medium, high) (example: high)</td>
</tr>
<tr>
    <td><CopyableCode code="zscore_target" /></td>
    <td><code>string</code></td>
    <td>Target of the zscore rule analysis. (bits, packets) (example: bits)</td>
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
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List a single network monitoring rule for account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists network monitoring rules for account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-prefixes"><code>prefixes</code></a>, <a href="#parameter-automatic_advertisement"><code>automatic_advertisement</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create network monitoring rules for account. Currently only supports creating a single rule per API request.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-prefixes"><code>prefixes</code></a>, <a href="#parameter-automatic_advertisement"><code>automatic_advertisement</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Update a network monitoring rule for account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-prefixes"><code>prefixes</code></a>, <a href="#parameter-automatic_advertisement"><code>automatic_advertisement</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Update network monitoring rules for account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a network monitoring rule for account.</td>
</tr>
<tr>
    <td><a href="#update_advertisement"><CopyableCode code="update_advertisement" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Update advertisement for rule.</td>
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

List a single network monitoring rule for account.

```sql
SELECT
id,
name,
automatic_advertisement,
bandwidth_threshold,
duration,
packet_threshold,
prefix_match,
prefixes,
type,
zscore_sensitivity,
zscore_target
FROM cloudflare.magic_network_monitoring.rules
WHERE rule_id = '{{ rule_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists network monitoring rules for account.

```sql
SELECT
id,
name,
automatic_advertisement,
bandwidth_threshold,
duration,
packet_threshold,
prefix_match,
prefixes,
type,
zscore_sensitivity,
zscore_target
FROM cloudflare.magic_network_monitoring.rules
WHERE account_id = '{{ account_id }}' -- required
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

Create network monitoring rules for account. Currently only supports creating a single rule per API request.

```sql
INSERT INTO cloudflare.magic_network_monitoring.rules (
automatic_advertisement,
bandwidth_threshold,
duration,
name,
packet_threshold,
prefix_match,
prefixes,
type,
zscore_sensitivity,
zscore_target,
account_id
)
SELECT 
{{ automatic_advertisement }} /* required */,
{{ bandwidth_threshold }},
'{{ duration }}',
'{{ name }}' /* required */,
{{ packet_threshold }},
'{{ prefix_match }}',
'{{ prefixes }}' /* required */,
'{{ type }}' /* required */,
'{{ zscore_sensitivity }}',
'{{ zscore_target }}',
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
- name: rules
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the rules resource.
    - name: automatic_advertisement
      value: {{ automatic_advertisement }}
      description: |
        Toggle on if you would like Cloudflare to automatically advertise the IP Prefixes within the rule via Magic Transit when the rule is triggered. Only available for users of Magic Transit.
    - name: bandwidth_threshold
      value: {{ bandwidth_threshold }}
      description: |
        The number of bits per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.
    - name: duration
      value: "{{ duration }}"
      description: |
        The amount of time that the rule threshold must be exceeded to send an alert notification. The final value must be equivalent to one of the following 8 values ["1m","5m","10m","15m","20m","30m","45m","60m"].
      valid_values: ['1m', '5m', '10m', '15m', '20m', '30m', '45m', '60m']
      default: 1m
    - name: name
      value: "{{ name }}"
      description: |
        The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9, underscore (_), dash (-), period (.), and tilde (~). You can’t have a space in the rule name. Max 256 characters.
    - name: packet_threshold
      value: {{ packet_threshold }}
      description: |
        The number of packets per second for the rule. When this value is exceeded for the set duration, an alert notification is sent. Minimum of 1 and no maximum.
    - name: prefix_match
      value: "{{ prefix_match }}"
      description: |
        Prefix match type to be applied for a prefix auto advertisement when using an advanced_ddos rule.
      valid_values: ['exact', 'subnet', 'supernet']
    - name: prefixes
      value:
        - "{{ prefixes }}"
    - name: type
      value: "{{ type }}"
      description: |
        MNM rule type.
      valid_values: ['threshold', 'zscore', 'advanced_ddos']
    - name: zscore_sensitivity
      value: "{{ zscore_sensitivity }}"
      description: |
        Level of sensitivity set for zscore rules.
      valid_values: ['low', 'medium', 'high']
    - name: zscore_target
      value: "{{ zscore_target }}"
      description: |
        Target of the zscore rule analysis.
      valid_values: ['bits', 'packets']
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

Update a network monitoring rule for account.

```sql
UPDATE cloudflare.magic_network_monitoring.rules
SET 
automatic_advertisement = {{ automatic_advertisement }},
bandwidth_threshold = {{ bandwidth_threshold }},
duration = '{{ duration }}',
name = '{{ name }}',
packet_threshold = {{ packet_threshold }},
prefix_match = '{{ prefix_match }}',
prefixes = '{{ prefixes }}',
type = '{{ type }}',
zscore_sensitivity = '{{ zscore_sensitivity }}',
zscore_target = '{{ zscore_target }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND prefixes = '{{ prefixes }}' --required
AND automatic_advertisement = {{ automatic_advertisement }} --required
AND type = '{{ type }}' --required
RETURNING
errors,
messages,
result,
success;
```
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

Update network monitoring rules for account.

```sql
REPLACE cloudflare.magic_network_monitoring.rules
SET 
automatic_advertisement = {{ automatic_advertisement }},
bandwidth_threshold = {{ bandwidth_threshold }},
duration = '{{ duration }}',
name = '{{ name }}',
packet_threshold = {{ packet_threshold }},
prefix_match = '{{ prefix_match }}',
prefixes = '{{ prefixes }}',
type = '{{ type }}',
zscore_sensitivity = '{{ zscore_sensitivity }}',
zscore_target = '{{ zscore_target }}'
WHERE 
account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND prefixes = '{{ prefixes }}' --required
AND automatic_advertisement = {{ automatic_advertisement }} --required
AND type = '{{ type }}' --required
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

Delete a network monitoring rule for account.

```sql
DELETE FROM cloudflare.magic_network_monitoring.rules
WHERE rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_advertisement"
    values={[
        { label: 'update_advertisement', value: 'update_advertisement' }
    ]}
>
<TabItem value="update_advertisement">

Update advertisement for rule.

```sql
EXEC cloudflare.magic_network_monitoring.rules.update_advertisement 
@rule_id='{{ rule_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
