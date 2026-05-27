--- 
title: access_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - access_rules
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

Creates, updates, deletes, gets or lists an <code>access_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.access_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get an IP Access rule response.

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
    <td>The unique identifier of the IP Access rule. (example: 92f17202ed8bd63d69a66b86a49a8f6b)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_modes" /></td>
    <td><code>array</code></td>
    <td>The available actions that a rule can apply to a matched request.</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>The rule configuration. (title: An IP address configuration.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The action to apply to a matched request. (block, challenge, whitelist, js_challenge, managed_challenge) (example: challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule, typically used as a reminder or explanation. (example: This rule is enabled because of an event that occurred on date X.)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>All zones owned by the user will have the rule applied.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get an IP Access rule response.

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
    <td>The unique identifier of the IP Access rule. (example: 92f17202ed8bd63d69a66b86a49a8f6b)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_modes" /></td>
    <td><code>array</code></td>
    <td>The available actions that a rule can apply to a matched request.</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>The rule configuration. (title: An IP address configuration.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The action to apply to a matched request. (block, challenge, whitelist, js_challenge, managed_challenge) (example: challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule, typically used as a reminder or explanation. (example: This rule is enabled because of an event that occurred on date X.)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>All zones owned by the user will have the rule applied.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List IP Access rules response.

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
    <td>The unique identifier of the IP Access rule. (example: 92f17202ed8bd63d69a66b86a49a8f6b)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_modes" /></td>
    <td><code>array</code></td>
    <td>The available actions that a rule can apply to a matched request.</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>The rule configuration. (title: An IP address configuration.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The action to apply to a matched request. (block, challenge, whitelist, js_challenge, managed_challenge) (example: challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule, typically used as a reminder or explanation. (example: This rule is enabled because of an event that occurred on date X.)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>All zones owned by the user will have the rule applied.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List IP Access rules response.

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
    <td>The unique identifier of the IP Access rule. (example: 92f17202ed8bd63d69a66b86a49a8f6b)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_modes" /></td>
    <td><code>array</code></td>
    <td>The available actions that a rule can apply to a matched request.</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>The rule configuration. (title: An IP address configuration.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The action to apply to a matched request. (block, challenge, whitelist, js_challenge, managed_challenge) (example: challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule, typically used as a reminder or explanation. (example: This rule is enabled because of an event that occurred on date X.)</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>object</code></td>
    <td>All zones owned by the user will have the rule applied.</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the details of an IP Access rule defined.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of an IP Access rule defined.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration.target"><code>configuration.target</code></a>, <a href="#parameter-configuration.value"><code>configuration.value</code></a>, <a href="#parameter-notes"><code>notes</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>Fetches IP Access rules of an account or zone. These rules apply to all the zones in the account or zone. You can filter the results using several optional parameters.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration.target"><code>configuration.target</code></a>, <a href="#parameter-configuration.value"><code>configuration.value</code></a>, <a href="#parameter-notes"><code>notes</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>Fetches IP Access rules of an account or zone. These rules apply to all the zones in the account or zone. You can filter the results using several optional parameters.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Creates a new IP Access rule for an account or zone. The rule will apply to all zones in the account or zone. Note: To create an IP Access rule that applies to a single zone, refer to the IP Access rules for a zone endpoints.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Creates a new IP Access rule for an account or zone. The rule will apply to all zones in the account or zone. Note: To create an IP Access rule that applies to a single zone, refer to the IP Access rules for a zone endpoints.</td>
</tr>
<tr>
    <td><a href="#edit_by_account"><CopyableCode code="edit_by_account" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-allowed_modes"><code>allowed_modes</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Updates an IP Access rule defined. Note: This operation will affect all zones in the account or zone.</td>
</tr>
<tr>
    <td><a href="#edit_by_zone"><CopyableCode code="edit_by_zone" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-allowed_modes"><code>allowed_modes</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Updates an IP Access rule defined. Note: This operation will affect all zones in the account or zone.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an existing IP Access rule defined. Note: This operation will affect all zones in the account or zone.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing IP Access rule defined. Note: This operation will affect all zones in the account or zone.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-configuration.target">
    <td><CopyableCode code="configuration.target" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-configuration.value">
    <td><CopyableCode code="configuration.value" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-match">
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-mode">
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-notes">
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches the details of an IP Access rule defined.

```sql
SELECT
id,
allowed_modes,
configuration,
created_on,
mode,
modified_on,
notes,
scope
FROM cloudflare.firewall.access_rules
WHERE rule_id = '{{ rule_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches the details of an IP Access rule defined.

```sql
SELECT
id,
allowed_modes,
configuration,
created_on,
mode,
modified_on,
notes,
scope
FROM cloudflare.firewall.access_rules
WHERE rule_id = '{{ rule_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Fetches IP Access rules of an account or zone. These rules apply to all the zones in the account or zone. You can filter the results using several optional parameters.

```sql
SELECT
id,
allowed_modes,
configuration,
created_on,
mode,
modified_on,
notes,
scope
FROM cloudflare.firewall.access_rules
WHERE account_id = '{{ account_id }}' -- required
AND mode = '{{ mode }}'
AND configuration.target = '{{ configuration.target }}'
AND configuration.value = '{{ configuration.value }}'
AND notes = '{{ notes }}'
AND match = '{{ match }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Fetches IP Access rules of an account or zone. These rules apply to all the zones in the account or zone. You can filter the results using several optional parameters.

```sql
SELECT
id,
allowed_modes,
configuration,
created_on,
mode,
modified_on,
notes,
scope
FROM cloudflare.firewall.access_rules
WHERE zone_id = '{{ zone_id }}' -- required
AND mode = '{{ mode }}'
AND configuration.target = '{{ configuration.target }}'
AND configuration.value = '{{ configuration.value }}'
AND notes = '{{ notes }}'
AND match = '{{ match }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
;
```
</TabItem>
</Tabs>


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

Creates a new IP Access rule for an account or zone. The rule will apply to all zones in the account or zone. Note: To create an IP Access rule that applies to a single zone, refer to the IP Access rules for a zone endpoints.

```sql
INSERT INTO cloudflare.firewall.access_rules (
configuration,
mode,
notes,
account_id
)
SELECT 
'{{ configuration }}' /* required */,
'{{ mode }}' /* required */,
'{{ notes }}',
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

Creates a new IP Access rule for an account or zone. The rule will apply to all zones in the account or zone. Note: To create an IP Access rule that applies to a single zone, refer to the IP Access rules for a zone endpoints.

```sql
INSERT INTO cloudflare.firewall.access_rules (
configuration,
mode,
notes,
zone_id
)
SELECT 
'{{ configuration }}' /* required */,
'{{ mode }}' /* required */,
'{{ notes }}',
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
- name: access_rules
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the access_rules resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the access_rules resource.
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
    defaultValue="edit_by_account"
    values={[
        { label: 'edit_by_account', value: 'edit_by_account' },
        { label: 'edit_by_zone', value: 'edit_by_zone' }
    ]}
>
<TabItem value="edit_by_account">

Updates an IP Access rule defined. Note: This operation will affect all zones in the account or zone.

```sql
UPDATE cloudflare.firewall.access_rules
SET 
configuration = '{{ configuration }}',
mode = '{{ mode }}',
notes = '{{ notes }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
AND mode = '{{ mode }}' --required
AND configuration = '{{ configuration }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="edit_by_zone">

Updates an IP Access rule defined. Note: This operation will affect all zones in the account or zone.

```sql
UPDATE cloudflare.firewall.access_rules
SET 
configuration = '{{ configuration }}',
mode = '{{ mode }}',
notes = '{{ notes }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND mode = '{{ mode }}' --required
AND configuration = '{{ configuration }}' --required
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

Deletes an existing IP Access rule defined. Note: This operation will affect all zones in the account or zone.

```sql
DELETE FROM cloudflare.firewall.access_rules
WHERE rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an existing IP Access rule defined. Note: This operation will affect all zones in the account or zone.

```sql
DELETE FROM cloudflare.firewall.access_rules
WHERE rule_id = '{{ rule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
