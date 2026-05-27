--- 
title: catch_alls
hide_title: false
hide_table_of_contents: false
keywords:
  - catch_alls
  - email_routing
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

Creates, updates, deletes, gets or lists a <code>catch_alls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="catch_alls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_routing.catch_alls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get catch-all rule response

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
    <td>Routing rule identifier. (example: a7e6fb77503c41d8a7f3113c6918f10c)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Routing rule name. (example: Send to user@example.net rule.)</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>List actions for the catch-all routing rule.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Routing rule status. (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="matchers" /></td>
    <td><code>array</code></td>
    <td>List of matchers for the catch-all routing rule.</td>
</tr>
<tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td>Routing rule tag. (Deprecated, replaced by routing rule identifier) (example: a7e6fb77503c41d8a7f3113c6918f10c)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Get information on the default catch-all routing rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-actions"><code>actions</code></a>, <a href="#parameter-matchers"><code>matchers</code></a></td>
    <td></td>
    <td>Enable or disable catch-all routing rule, or change action to forward to specific destination address. Forward actions require all destination addresses to be verified.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get information on the default catch-all routing rule.

```sql
SELECT
id,
name,
actions,
enabled,
matchers,
tag
FROM cloudflare.email_routing.catch_alls
WHERE zone_id = '{{ zone_id }}' -- required
;
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

Enable or disable catch-all routing rule, or change action to forward to specific destination address. Forward actions require all destination addresses to be verified.

```sql
REPLACE cloudflare.email_routing.catch_alls
SET 
actions = '{{ actions }}',
enabled = {{ enabled }},
matchers = '{{ matchers }}',
name = '{{ name }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND actions = '{{ actions }}' --required
AND matchers = '{{ matchers }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
