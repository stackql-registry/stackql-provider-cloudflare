--- 
title: widgets
hide_title: false
hide_table_of_contents: false
keywords:
  - widgets
  - turnstile
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

Creates, updates, deletes, gets or lists a <code>widgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="widgets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.turnstile.widgets" /></td></tr>
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

Turnstile Widget Details Response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier to identify your widget, and where it is used. (example: blog.cloudflare.com login form)</td>
</tr>
<tr>
    <td><CopyableCode code="ephemeral_id" /></td>
    <td><code>boolean</code></td>
    <td>Return the Ephemeral ID in /siteverify (ENT only).</td>
</tr>
<tr>
    <td><CopyableCode code="bot_fight_mode" /></td>
    <td><code>boolean</code></td>
    <td>If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots (ENT only).</td>
</tr>
<tr>
    <td><CopyableCode code="clearance_level" /></td>
    <td><code>string</code></td>
    <td>If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can determine the clearance level to be set (no_clearance, jschallenge, managed, interactive) (example: interactive)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the widget was created. (example: 2014-01-01T05:20:00.123123Z)</td>
</tr>
<tr>
    <td><CopyableCode code="domains" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Widget Mode (non-interactive, invisible, managed) (example: invisible)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the widget was modified. (example: 2014-01-01T05:20:00.123123Z)</td>
</tr>
<tr>
    <td><CopyableCode code="offlabel" /></td>
    <td><code>boolean</code></td>
    <td>Do not show any Cloudflare branding on the widget (ENT only).</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Region where this widget can be used. This cannot be changed after creation. (world, china) (default: world)</td>
</tr>
<tr>
    <td><CopyableCode code="secret" /></td>
    <td><code>string</code></td>
    <td>Secret key for this widget. (example: 0x4AAF00AAAABn0R22HWm098HVBjhdsYUc)</td>
</tr>
<tr>
    <td><CopyableCode code="sitekey" /></td>
    <td><code>string</code></td>
    <td>Widget item identifier tag. (example: 0x4AAF00AAAABn0R22HWm-YUc)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Turnstile Widgets

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier to identify your widget, and where it is used. (example: blog.cloudflare.com login form)</td>
</tr>
<tr>
    <td><CopyableCode code="ephemeral_id" /></td>
    <td><code>boolean</code></td>
    <td>Return the Ephemeral ID in /siteverify (ENT only).</td>
</tr>
<tr>
    <td><CopyableCode code="bot_fight_mode" /></td>
    <td><code>boolean</code></td>
    <td>If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots (ENT only).</td>
</tr>
<tr>
    <td><CopyableCode code="clearance_level" /></td>
    <td><code>string</code></td>
    <td>If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can determine the clearance level to be set (no_clearance, jschallenge, managed, interactive) (example: interactive)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the widget was created. (example: 2014-01-01T05:20:00.123123Z)</td>
</tr>
<tr>
    <td><CopyableCode code="domains" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Widget Mode (non-interactive, invisible, managed) (example: invisible)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the widget was modified. (example: 2014-01-01T05:20:00.123123Z)</td>
</tr>
<tr>
    <td><CopyableCode code="offlabel" /></td>
    <td><code>boolean</code></td>
    <td>Do not show any Cloudflare branding on the widget (ENT only).</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Region where this widget can be used. This cannot be changed after creation. (world, china) (default: world)</td>
</tr>
<tr>
    <td><CopyableCode code="sitekey" /></td>
    <td><code>string</code></td>
    <td>Widget item identifier tag. (example: 0x4AAF00AAAABn0R22HWm-YUc)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sitekey"><code>sitekey</code></a></td>
    <td></td>
    <td>Show a single challenge widget configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists all turnstile widgets of an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-domains"><code>domains</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists challenge widgets.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sitekey"><code>sitekey</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-domains"><code>domains</code></a></td>
    <td></td>
    <td>Update the configuration of a widget.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sitekey"><code>sitekey</code></a></td>
    <td></td>
    <td>Destroy a Turnstile Widget.</td>
</tr>
<tr>
    <td><a href="#rotate_secret"><CopyableCode code="rotate_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sitekey"><code>sitekey</code></a></td>
    <td></td>
    <td>Generate a new secret key for this widget. If `invalidate_immediately` is set to `false`, the previous secret remains valid for 2 hours. Note that secrets cannot be rotated again during the grace period.</td>
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
<tr id="parameter-sitekey">
    <td><CopyableCode code="sitekey" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Filter widgets by field using case-insensitive substring matching. Format: `field:value` Supported fields: - `name` - Filter by widget name (e.g., `filter=name:login-form`) - `sitekey` - Filter by sitekey (e.g., `filter=sitekey:0x4AAA`) Returns 400 Bad Request if the field is unsupported or format is invalid. An empty filter value returns all results.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Show a single challenge widget configuration.

```sql
SELECT
name,
ephemeral_id,
bot_fight_mode,
clearance_level,
created_on,
domains,
mode,
modified_on,
offlabel,
region,
secret,
sitekey
FROM cloudflare.turnstile.widgets
WHERE account_id = '{{ account_id }}' -- required
AND sitekey = '{{ sitekey }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all turnstile widgets of an account.

```sql
SELECT
name,
ephemeral_id,
bot_fight_mode,
clearance_level,
created_on,
domains,
mode,
modified_on,
offlabel,
region,
sitekey
FROM cloudflare.turnstile.widgets
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND filter = '{{ filter }}'
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

Lists challenge widgets.

```sql
INSERT INTO cloudflare.turnstile.widgets (
bot_fight_mode,
clearance_level,
domains,
ephemeral_id,
mode,
name,
offlabel,
region,
account_id,
page,
per_page,
order,
direction,
filter
)
SELECT 
{{ bot_fight_mode }},
'{{ clearance_level }}',
'{{ domains }}' /* required */,
{{ ephemeral_id }},
'{{ mode }}' /* required */,
'{{ name }}' /* required */,
{{ offlabel }},
'{{ region }}',
'{{ account_id }}',
'{{ page }}',
'{{ per_page }}',
'{{ order }}',
'{{ direction }}',
'{{ filter }}'
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
- name: widgets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the widgets resource.
    - name: bot_fight_mode
      value: {{ bot_fight_mode }}
      description: |
        If bot_fight_mode is set to \`true\`, Cloudflare issues computationally expensive challenges in response to malicious bots (ENT only).
    - name: clearance_level
      value: "{{ clearance_level }}"
      description: |
        If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can determine the clearance level to be set
      valid_values: ['no_clearance', 'jschallenge', 'managed', 'interactive']
    - name: domains
      value:
        - "{{ domains }}"
    - name: ephemeral_id
      value: {{ ephemeral_id }}
      description: |
        Return the Ephemeral ID in /siteverify (ENT only).
    - name: mode
      value: "{{ mode }}"
      description: |
        Widget Mode
      valid_values: ['non-interactive', 'invisible', 'managed']
    - name: name
      value: "{{ name }}"
      description: |
        Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier to identify your widget, and where it is used.
    - name: offlabel
      value: {{ offlabel }}
      description: |
        Do not show any Cloudflare branding on the widget (ENT only).
    - name: region
      value: "{{ region }}"
      description: |
        Region where this widget can be used. This cannot be changed after creation.
      valid_values: ['world', 'china']
      default: world
    - name: page
      value: {{ page }}
    - name: per_page
      value: {{ per_page }}
    - name: order
      value: "{{ order }}"
    - name: direction
      value: "{{ direction }}"
    - name: filter
      value: "{{ filter }}"
      description: Filter widgets by field using case-insensitive substring matching. Format: \`field:value\` Supported fields: - \`name\` - Filter by widget name (e.g., \`filter=name:login-form\`) - \`sitekey\` - Filter by sitekey (e.g., \`filter=sitekey:0x4AAA\`) Returns 400 Bad Request if the field is unsupported or format is invalid. An empty filter value returns all results.
      description: Filter widgets by field using case-insensitive substring matching. Format: \`field:value\` Supported fields: - \`name\` - Filter by widget name (e.g., \`filter=name:login-form\`) - \`sitekey\` - Filter by sitekey (e.g., \`filter=sitekey:0x4AAA\`) Returns 400 Bad Request if the field is unsupported or format is invalid. An empty filter value returns all results.
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

Update the configuration of a widget.

```sql
REPLACE cloudflare.turnstile.widgets
SET 
bot_fight_mode = {{ bot_fight_mode }},
clearance_level = '{{ clearance_level }}',
domains = '{{ domains }}',
ephemeral_id = {{ ephemeral_id }},
mode = '{{ mode }}',
name = '{{ name }}',
offlabel = {{ offlabel }},
region = '{{ region }}'
WHERE 
account_id = '{{ account_id }}' --required
AND sitekey = '{{ sitekey }}' --required
AND name = '{{ name }}' --required
AND mode = '{{ mode }}' --required
AND domains = '{{ domains }}' --required
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

Destroy a Turnstile Widget.

```sql
DELETE FROM cloudflare.turnstile.widgets
WHERE account_id = '{{ account_id }}' --required
AND sitekey = '{{ sitekey }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rotate_secret"
    values={[
        { label: 'rotate_secret', value: 'rotate_secret' }
    ]}
>
<TabItem value="rotate_secret">

Generate a new secret key for this widget. If `invalidate_immediately` is set to `false`, the previous secret remains valid for 2 hours. Note that secrets cannot be rotated again during the grace period.

```sql
EXEC cloudflare.turnstile.widgets.rotate_secret 
@account_id='{{ account_id }}' --required, 
@sitekey='{{ sitekey }}' --required 
@@json=
'{
"invalidate_immediately": {{ invalidate_immediately }}
}'
;
```
</TabItem>
</Tabs>
