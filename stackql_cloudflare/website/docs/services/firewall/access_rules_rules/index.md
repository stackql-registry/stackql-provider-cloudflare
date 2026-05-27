--- 
title: access_rules_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - access_rules_rules
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

Creates, updates, deletes, gets or lists an <code>access_rules_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_rules_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.access_rules_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_user"
    values={[
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="list_by_user">

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
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-configuration.target"><code>configuration.target</code></a>, <a href="#parameter-configuration.value"><code>configuration.value</code></a>, <a href="#parameter-notes"><code>notes</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>Fetches IP Access rules of the user. You can filter the results using several optional parameters.</td>
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
    defaultValue="list_by_user"
    values={[
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="list_by_user">

Fetches IP Access rules of the user. You can filter the results using several optional parameters.

```sql
SELECT
id,
allowed_modes,
configuration,
created_on,
mode,
modified_on,
notes
FROM cloudflare.firewall.access_rules_rules
WHERE mode = '{{ mode }}'
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
