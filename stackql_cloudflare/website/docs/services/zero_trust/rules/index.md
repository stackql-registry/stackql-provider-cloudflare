--- 
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.rules" /></td></tr>
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
    <td><a href="#bulk_edit"><CopyableCode code="bulk_edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-new_priorities"><code>new_priorities</code></a></td>
    <td></td>
    <td>Reorders DLP email scanning rules by updating their priority values. Higher priority rules are evaluated first.</td>
</tr>
<tr>
    <td><a href="#reset_expiration"><CopyableCode code="reset_expiration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Resets the expiration of a Zero Trust Gateway Rule if its duration elapsed and it has a default duration. The Zero Trust Gateway Rule must have values for both `expiration.expires_at` and `expiration.duration`.</td>
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
</tbody>
</table>

## `UPDATE` examples

<Tabs
    defaultValue="bulk_edit"
    values={[
        { label: 'bulk_edit', value: 'bulk_edit' }
    ]}
>
<TabItem value="bulk_edit">

Reorders DLP email scanning rules by updating their priority values. Higher priority rules are evaluated first.

```sql
UPDATE cloudflare.zero_trust.rules
SET 
new_priorities = '{{ new_priorities }}'
WHERE 
account_id = '{{ account_id }}' --required
AND new_priorities = '{{ new_priorities }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reset_expiration"
    values={[
        { label: 'reset_expiration', value: 'reset_expiration' }
    ]}
>
<TabItem value="reset_expiration">

Resets the expiration of a Zero Trust Gateway Rule if its duration elapsed and it has a default duration. The Zero Trust Gateway Rule must have values for both `expiration.expires_at` and `expiration.duration`.

```sql
EXEC cloudflare.zero_trust.rules.reset_expiration 
@rule_id='{{ rule_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
