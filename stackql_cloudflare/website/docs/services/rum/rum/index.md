--- 
title: rum
hide_title: false
hide_table_of_contents: false
keywords:
  - rum
  - rum
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

Creates, updates, deletes, gets or lists a <code>rum</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rum" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rum.rum" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_rule_v2"><CopyableCode code="create_rule_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a></td>
    <td></td>
    <td>Creates a new rule in a Web Analytics ruleset.</td>
</tr>
<tr>
    <td><a href="#create_rules_v2"><CopyableCode code="create_rules_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a></td>
    <td></td>
    <td>Modifies one or more rules in a Web Analytics ruleset with a single request.</td>
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
<tr id="parameter-ruleset_id">
    <td><CopyableCode code="ruleset_id" /></td>
    <td><code>string</code></td>
    <td>The ruleset ID.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="create_rule_v2"
    values={[
        { label: 'create_rule_v2', value: 'create_rule_v2' },
        { label: 'create_rules_v2', value: 'create_rules_v2' }
    ]}
>
<TabItem value="create_rule_v2">

Creates a new rule in a Web Analytics ruleset.

```sql
EXEC cloudflare.rum.rum.create_rule_v2 
@account_id='{{ account_id }}' --required, 
@ruleset_id='{{ ruleset_id }}' --required 
@@json=
'{
"host": "{{ host }}", 
"inclusive": {{ inclusive }}, 
"is_paused": {{ is_paused }}, 
"paths": "{{ paths }}"
}'
;
```
</TabItem>
<TabItem value="create_rules_v2">

Modifies one or more rules in a Web Analytics ruleset with a single request.

```sql
EXEC cloudflare.rum.rum.create_rules_v2 
@account_id='{{ account_id }}' --required, 
@ruleset_id='{{ ruleset_id }}' --required 
@@json=
'{
"delete_rules": "{{ delete_rules }}", 
"rules": "{{ rules }}"
}'
;
```
</TabItem>
</Tabs>
