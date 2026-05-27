--- 
title: pagerules
hide_title: false
hide_table_of_contents: false
keywords:
  - pagerules
  - page_rules
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

Creates, updates, deletes, gets or lists a <code>pagerules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pagerules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.page_rules.pagerules" /></td></tr>
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

Get a Page Rule response

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
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions to perform if the targets of this rule match the request. Actions can redirect to another URL or override settings, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the Page Rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the Page Rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the rule, used to define which Page Rule is processed over another. A higher number indicates a higher priority. For example, if you have a catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to take precedence (rule B: `/images/special/*`), specify a higher priority for rule B so it overrides rule A.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the Page Rule. (active, disabled) (default: disabled, example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="targets" /></td>
    <td><code>array</code></td>
    <td>The rule targets to evaluate on each request.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Page Rules response

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
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The set of actions to perform if the targets of this rule match the request. Actions can redirect to another URL or override settings, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the Page Rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the Page Rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the rule, used to define which Page Rule is processed over another. A higher number indicates a higher priority. For example, if you have a catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to take precedence (rule B: `/images/special/*`), specify a higher priority for rule B so it overrides rule A.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the Page Rule. (active, disabled) (default: disabled, example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="targets" /></td>
    <td><code>array</code></td>
    <td>The rule targets to evaluate on each request.</td>
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
    <td><a href="#parameter-pagerule_id"><code>pagerule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a Page Rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td>Fetches Page Rules in a zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-targets"><code>targets</code></a>, <a href="#parameter-actions"><code>actions</code></a></td>
    <td></td>
    <td>Creates a new Page Rule.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-pagerule_id"><code>pagerule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates one or more fields of an existing Page Rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pagerule_id"><code>pagerule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-targets"><code>targets</code></a>, <a href="#parameter-actions"><code>actions</code></a></td>
    <td></td>
    <td>Replaces the configuration of an existing Page Rule. The configuration of the updated Page Rule will exactly match the data passed in the API request.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pagerule_id"><code>pagerule_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing Page Rule.</td>
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
<tr id="parameter-pagerule_id">
    <td><CopyableCode code="pagerule_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
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

Fetches the details of a Page Rule.

```sql
SELECT
id,
actions,
created_on,
modified_on,
priority,
status,
targets
FROM cloudflare.page_rules.pagerules
WHERE pagerule_id = '{{ pagerule_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches Page Rules in a zone.

```sql
SELECT
id,
actions,
created_on,
modified_on,
priority,
status,
targets
FROM cloudflare.page_rules.pagerules
WHERE zone_id = '{{ zone_id }}' -- required
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND match = '{{ match }}'
AND status = '{{ status }}'
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

Creates a new Page Rule.

```sql
INSERT INTO cloudflare.page_rules.pagerules (
actions,
priority,
status,
targets,
zone_id
)
SELECT 
'{{ actions }}' /* required */,
{{ priority }},
'{{ status }}',
'{{ targets }}' /* required */,
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
- name: pagerules
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the pagerules resource.
    - name: actions
      description: |
        The set of actions to perform if the targets of this rule match the request. Actions can redirect to another URL or override settings, but not both.
      value:
        - id: "{{ id }}"
          value: "{{ value }}"
    - name: priority
      value: {{ priority }}
      description: |
        The priority of the rule, used to define which Page Rule is processed over another. A higher number indicates a higher priority. For example, if you have a catch-all Page Rule (rule A: \`/images/*\`) but want a more specific Page Rule to take precedence (rule B: \`/images/special/*\`), specify a higher priority for rule B so it overrides rule A.
      default: 1
    - name: status
      value: "{{ status }}"
      description: |
        The status of the Page Rule.
      valid_values: ['active', 'disabled']
      default: disabled
    - name: targets
      description: |
        The rule targets to evaluate on each request.
      value:
        - constraint:
            operator: "{{ operator }}"
            value: "{{ value }}"
          target: "{{ target }}"
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

Updates one or more fields of an existing Page Rule.

```sql
UPDATE cloudflare.page_rules.pagerules
SET 
actions = '{{ actions }}',
priority = {{ priority }},
status = '{{ status }}',
targets = '{{ targets }}'
WHERE 
pagerule_id = '{{ pagerule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
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

Replaces the configuration of an existing Page Rule. The configuration of the updated Page Rule will exactly match the data passed in the API request.

```sql
REPLACE cloudflare.page_rules.pagerules
SET 
actions = '{{ actions }}',
priority = {{ priority }},
status = '{{ status }}',
targets = '{{ targets }}'
WHERE 
pagerule_id = '{{ pagerule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND targets = '{{ targets }}' --required
AND actions = '{{ actions }}' --required
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

Deletes an existing Page Rule.

```sql
DELETE FROM cloudflare.page_rules.pagerules
WHERE pagerule_id = '{{ pagerule_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
