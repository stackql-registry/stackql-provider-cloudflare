--- 
title: ua_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - ua_rules
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

Creates, updates, deletes, gets or lists a <code>ua_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ua_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.ua_rules" /></td></tr>
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

Get a User Agent Blocking rule response

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
    <td>The unique identifier of the User Agent Blocking rule. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>The configuration object for the current rule.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule. (example: Prevent access from abusive clients identified by this User Agent to mitigate a DDoS attack)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The action to apply to a matched request. (block, challenge, js_challenge, managed_challenge) (example: js_challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the rule is currently paused.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List User Agent Blocking rules response

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
    <td>The unique identifier of the User Agent Blocking rule. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="configuration" /></td>
    <td><code>object</code></td>
    <td>The configuration object for the current rule.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule. (example: Prevent access from abusive clients identified by this User Agent to mitigate a DDoS attack)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The action to apply to a matched request. (block, challenge, js_challenge, managed_challenge) (example: js_challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the rule is currently paused.</td>
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
    <td><a href="#parameter-ua_rule_id"><code>ua_rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a User Agent Blocking rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-user_agent"><code>user_agent</code></a>, <a href="#parameter-paused"><code>paused</code></a></td>
    <td>Fetches User Agent Blocking rules in a zone. You can filter the results using several optional parameters.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Creates a new User Agent Blocking rule in a zone.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-ua_rule_id"><code>ua_rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration"><code>configuration</code></a></td>
    <td></td>
    <td>Updates an existing User Agent Blocking rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-ua_rule_id"><code>ua_rule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing User Agent Blocking rule.</td>
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
<tr id="parameter-ua_rule_id">
    <td><CopyableCode code="ua_rule_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-description">
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-paused">
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-user_agent">
    <td><CopyableCode code="user_agent" /></td>
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

Fetches the details of a User Agent Blocking rule.

```sql
SELECT
id,
configuration,
description,
mode,
paused
FROM cloudflare.firewall.ua_rules
WHERE ua_rule_id = '{{ ua_rule_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches User Agent Blocking rules in a zone. You can filter the results using several optional parameters.

```sql
SELECT
id,
configuration,
description,
mode,
paused
FROM cloudflare.firewall.ua_rules
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND description = '{{ description }}'
AND per_page = '{{ per_page }}'
AND user_agent = '{{ user_agent }}'
AND paused = '{{ paused }}'
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

Creates a new User Agent Blocking rule in a zone.

```sql
INSERT INTO cloudflare.firewall.ua_rules (
configuration,
description,
mode,
paused,
zone_id
)
SELECT 
'{{ configuration }}' /* required */,
'{{ description }}',
'{{ mode }}' /* required */,
{{ paused }},
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
- name: ua_rules
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the ua_rules resource.
    - name: configuration
      value:
        target: "{{ target }}"
        value: "{{ value }}"
    - name: description
      value: "{{ description }}"
      description: |
        An informative summary of the rule. This value is sanitized and any tags will be removed.
    - name: mode
      value: "{{ mode }}"
      description: |
        The action to apply to a matched request.
      valid_values: ['block', 'challenge', 'whitelist', 'js_challenge', 'managed_challenge']
    - name: paused
      value: {{ paused }}
      description: |
        When true, indicates that the rule is currently paused.
      default: false
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

Updates an existing User Agent Blocking rule.

```sql
REPLACE cloudflare.firewall.ua_rules
SET 
configuration = '{{ configuration }}',
description = '{{ description }}',
mode = '{{ mode }}',
paused = {{ paused }}
WHERE 
ua_rule_id = '{{ ua_rule_id }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an existing User Agent Blocking rule.

```sql
DELETE FROM cloudflare.firewall.ua_rules
WHERE ua_rule_id = '{{ ua_rule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
