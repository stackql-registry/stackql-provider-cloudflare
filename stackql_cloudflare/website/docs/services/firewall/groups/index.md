--- 
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.groups" /></td></tr>
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

Get a WAF rule group response.

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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether the API call was successful. (true)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Defines the list WAF rule groups response.

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
    <td>Defines the unique identifier of the rule group. (example: de677e5818985db1285d0e80225f06e5)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Defines the name of the rule group. (example: Project Honey Pot)</td>
</tr>
<tr>
    <td><CopyableCode code="package_id" /></td>
    <td><code>string</code></td>
    <td>Defines the unique identifier of a WAF package. (example: a25a9a7e9c00afc1fb2e0245519d725b)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_modes" /></td>
    <td><code>array</code></td>
    <td>Defines the available states for the rule group.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Defines an informative summary of what the rule group does. (example: Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks)</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>Defines the state of the rules contained in the rule group. When `on`, the rules in the group are configurable/usable. (on, off) (default: on)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_rules_count" /></td>
    <td><code>number</code></td>
    <td>Defines the number of rules within the group that have been modified from their default configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="rules_count" /></td>
    <td><code>number</code></td>
    <td>Defines the number of rules in the current rule group.</td>
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
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-package_id"><code>package_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a WAF rule group. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-package_id"><code>package_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-mode"><code>mode</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-rules_count"><code>rules_count</code></a></td>
    <td>Fetches the WAF rule groups in a WAF package. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-package_id"><code>package_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates a WAF rule group. You can update the state (`mode` parameter) of a rule group. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The Access group ID.</td>
</tr>
<tr id="parameter-package_id">
    <td><CopyableCode code="package_id" /></td>
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
<tr id="parameter-mode">
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
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
<tr id="parameter-rules_count">
    <td><CopyableCode code="rules_count" /></td>
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

Fetches the details of a WAF rule group. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

```sql
SELECT
errors,
messages,
result,
success
FROM cloudflare.firewall.groups
WHERE group_id = '{{ group_id }}' -- required
AND package_id = '{{ package_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches the WAF rule groups in a WAF package. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

```sql
SELECT
id,
name,
package_id,
allowed_modes,
description,
mode,
modified_rules_count,
rules_count
FROM cloudflare.firewall.groups
WHERE package_id = '{{ package_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
AND mode = '{{ mode }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND match = '{{ match }}'
AND name = '{{ name }}'
AND rules_count = '{{ rules_count }}'
;
```
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

Updates a WAF rule group. You can update the state (`mode` parameter) of a rule group. **Note:** Applies only to the [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

```sql
UPDATE cloudflare.firewall.groups
SET 
mode = '{{ mode }}'
WHERE 
group_id = '{{ group_id }}' --required
AND package_id = '{{ package_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
