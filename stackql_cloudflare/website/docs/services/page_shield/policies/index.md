--- 
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - page_shield
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.page_shield.policies" /></td></tr>
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

Get a Page Shield policy response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>The action to take if the expression matches (allow, log, add_reporting_directives) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the policy (example: Checkout page CSP policy)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the policy is enabled</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>The expression which must match for the policy to be applied, using the Cloudflare Firewall rule expression syntax (example: ends_with(http.request.uri.path, "/checkout"))</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>The policy which will be applied (example: script-src 'none';)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Page Shield policies response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>The action to take if the expression matches (allow, log, add_reporting_directives) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the policy (example: Checkout page CSP policy)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the policy is enabled</td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>The expression which must match for the policy to be applied, using the Cloudflare Firewall rule expression syntax (example: ends_with(http.request.uri.path, "/checkout"))</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>The policy which will be applied (example: script-src 'none';)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Fetches a Page Shield policy by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Lists all Page Shield policies.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-action"><code>action</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Create a Page Shield policy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Update a Page Shield policy by ID.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Delete a Page Shield policy by ID.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Fetches a Page Shield policy by ID.

```sql
SELECT
id,
action,
description,
enabled,
expression,
value
FROM cloudflare.page_shield.policies
WHERE zone_id = '{{ zone_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Page Shield policies.

```sql
SELECT
id,
action,
description,
enabled,
expression,
value
FROM cloudflare.page_shield.policies
WHERE zone_id = '{{ zone_id }}' -- required
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

Create a Page Shield policy.

```sql
INSERT INTO cloudflare.page_shield.policies (
action,
description,
enabled,
expression,
value,
zone_id
)
SELECT 
'{{ action }}' /* required */,
'{{ description }}' /* required */,
{{ enabled }} /* required */,
'{{ expression }}' /* required */,
'{{ value }}' /* required */,
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
- name: policies
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the policies resource.
    - name: action
      value: "{{ action }}"
      description: |
        The action to take if the expression matches
      valid_values: ['allow', 'log', 'add_reporting_directives']
    - name: description
      value: "{{ description }}"
      description: |
        A description for the policy
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether the policy is enabled
    - name: expression
      value: "{{ expression }}"
      description: |
        The expression which must match for the policy to be applied, using the Cloudflare Firewall rule expression syntax
    - name: value
      value: "{{ value }}"
      description: |
        The policy which will be applied
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

Update a Page Shield policy by ID.

```sql
REPLACE cloudflare.page_shield.policies
SET 
action = '{{ action }}',
description = '{{ description }}',
enabled = {{ enabled }},
expression = '{{ expression }}',
value = '{{ value }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND policy_id = '{{ policy_id }}' --required
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

Delete a Page Shield policy by ID.

```sql
DELETE FROM cloudflare.page_shield.policies
WHERE zone_id = '{{ zone_id }}' --required
AND policy_id = '{{ policy_id }}' --required
;
```
</TabItem>
</Tabs>
