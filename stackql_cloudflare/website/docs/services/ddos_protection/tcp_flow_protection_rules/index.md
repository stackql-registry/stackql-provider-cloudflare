--- 
title: tcp_flow_protection_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tcp_flow_protection_rules
  - ddos_protection
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

Creates, updates, deletes, gets or lists a <code>tcp_flow_protection_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tcp_flow_protection_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ddos_protection.tcp_flow_protection_rules" /></td></tr>
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

Get TCP Flow Protection rule response.

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
    <td>The unique ID of the TCP Flow Protection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the TCP Flow Protection rule. Value is relative to the 'scope' setting. For 'global' scope, name should be 'global'. For either the 'region' or 'datacenter' scope, name should be the actual name of the region or datacenter, e.g., 'wnam' or 'lax'.</td>
</tr>
<tr>
    <td><CopyableCode code="burst_sensitivity" /></td>
    <td><code>string</code></td>
    <td>The burst sensitivity. Must be one of 'low', 'medium', 'high'.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation timestamp of the TCP Flow Protection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode for TCP Flow Protection. Must be one of 'enabled', 'disabled', 'monitoring'.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modification timestamp of the TCP Flow Protection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="rate_sensitivity" /></td>
    <td><code>string</code></td>
    <td>The rate sensitivity. Must be one of 'low', 'medium', 'high'.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the TCP Flow Protection rule. Must be one of 'global', 'region', or 'datacenter'.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List all TCP Flow Protection rules response.

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
    <td>The unique ID of the TCP Flow Protection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the TCP Flow Protection rule. Value is relative to the 'scope' setting. For 'global' scope, name should be 'global'. For either the 'region' or 'datacenter' scope, name should be the actual name of the region or datacenter, e.g., 'wnam' or 'lax'.</td>
</tr>
<tr>
    <td><CopyableCode code="burst_sensitivity" /></td>
    <td><code>string</code></td>
    <td>The burst sensitivity. Must be one of 'low', 'medium', 'high'.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation timestamp of the TCP Flow Protection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>The mode for TCP Flow Protection. Must be one of 'enabled', 'disabled', 'monitoring'.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modification timestamp of the TCP Flow Protection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="rate_sensitivity" /></td>
    <td><code>string</code></td>
    <td>The rate sensitivity. Must be one of 'low', 'medium', 'high'.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope for the TCP Flow Protection rule. Must be one of 'global', 'region', or 'datacenter'.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Get a TCP Flow Protection rule specified by the given UUID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>List all TCP Flow Protection rules for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-rate_sensitivity"><code>rate_sensitivity</code></a>, <a href="#parameter-burst_sensitivity"><code>burst_sensitivity</code></a></td>
    <td></td>
    <td>Create a TCP Flow Protection rule for an account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Update a TCP Flow Protection rule specified by the given UUID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Delete a TCP Flow Protection rule specified by the given UUID.</td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete all TCP Flow Protection rules for an account.</td>
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
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The direction of ordering (ASC or DESC). Defaults to 'ASC'.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>The field to order by. Defaults to 'prefix'.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer (int64)</code></td>
    <td>The page number for pagination. Defaults to 1.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer (int64)</code></td>
    <td>The number of items per page. Must be between 10 and 1000. Defaults to 25.</td>
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

Get a TCP Flow Protection rule specified by the given UUID.

```sql
SELECT
id,
name,
burst_sensitivity,
created_on,
mode,
modified_on,
rate_sensitivity,
scope
FROM cloudflare.ddos_protection.tcp_flow_protection_rules
WHERE account_id = '{{ account_id }}' -- required
AND rule_id = '{{ rule_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all TCP Flow Protection rules for an account.

```sql
SELECT
id,
name,
burst_sensitivity,
created_on,
mode,
modified_on,
rate_sensitivity,
scope
FROM cloudflare.ddos_protection.tcp_flow_protection_rules
WHERE account_id = '{{ account_id }}' -- required
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
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a TCP Flow Protection rule for an account.

```sql
INSERT INTO cloudflare.ddos_protection.tcp_flow_protection_rules (
burst_sensitivity,
mode,
name,
rate_sensitivity,
scope,
account_id
)
SELECT 
'{{ burst_sensitivity }}' /* required */,
'{{ mode }}' /* required */,
'{{ name }}' /* required */,
'{{ rate_sensitivity }}' /* required */,
'{{ scope }}' /* required */,
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
- name: tcp_flow_protection_rules
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the tcp_flow_protection_rules resource.
    - name: burst_sensitivity
      value: "{{ burst_sensitivity }}"
      description: |
        The burst sensitivity. Must be one of 'low', 'medium', 'high'.
    - name: mode
      value: "{{ mode }}"
      description: |
        The mode for the TCP Flow Protection. Must be one of 'enabled', 'disabled', 'monitoring'.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the TCP Flow Protection rule. Value is relative to the 'scope' setting. For 'global' scope, name should be 'global'. For either the 'region' or 'datacenter' scope, name should be the actual name of the region or datacenter, e.g., 'wnam' or 'lax'.
    - name: rate_sensitivity
      value: "{{ rate_sensitivity }}"
      description: |
        The rate sensitivity. Must be one of 'low', 'medium', 'high'.
    - name: scope
      value: "{{ scope }}"
      description: |
        The scope for the TCP Flow Protection rule.
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

Update a TCP Flow Protection rule specified by the given UUID.

```sql
UPDATE cloudflare.ddos_protection.tcp_flow_protection_rules
SET 
burst_sensitivity = '{{ burst_sensitivity }}',
mode = '{{ mode }}',
rate_sensitivity = '{{ rate_sensitivity }}'
WHERE 
account_id = '{{ account_id }}' --required
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
        { label: 'delete', value: 'delete' },
        { label: 'bulk_delete', value: 'bulk_delete' }
    ]}
>
<TabItem value="delete">

Delete a TCP Flow Protection rule specified by the given UUID.

```sql
DELETE FROM cloudflare.ddos_protection.tcp_flow_protection_rules
WHERE account_id = '{{ account_id }}' --required
AND rule_id = '{{ rule_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Delete all TCP Flow Protection rules for an account.

```sql
DELETE FROM cloudflare.ddos_protection.tcp_flow_protection_rules
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
