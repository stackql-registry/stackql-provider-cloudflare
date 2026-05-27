--- 
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="keys" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.keys" /></td></tr>
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

Get the Access key configuration response

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
    <td><CopyableCode code="days_until_next_rotation" /></td>
    <td><code>number</code></td>
    <td>The number of days until the next key rotation.</td>
</tr>
<tr>
    <td><CopyableCode code="key_rotation_interval_days" /></td>
    <td><code>number</code></td>
    <td>The number of days between key rotations.</td>
</tr>
<tr>
    <td><CopyableCode code="last_key_rotation_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of the previous key rotation. (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets the Access key rotation settings for an account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-key_rotation_interval_days"><code>key_rotation_interval_days</code></a></td>
    <td></td>
    <td>Updates the Access key rotation settings for an account.</td>
</tr>
<tr>
    <td><a href="#rotate"><CopyableCode code="rotate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Perfoms a key rotation for an account.</td>
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

Gets the Access key rotation settings for an account.

```sql
SELECT
days_until_next_rotation,
key_rotation_interval_days,
last_key_rotation_at
FROM cloudflare.zero_trust.keys
WHERE account_id = '{{ account_id }}' -- required
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

Updates the Access key rotation settings for an account.

```sql
REPLACE cloudflare.zero_trust.keys
SET 
key_rotation_interval_days = {{ key_rotation_interval_days }}
WHERE 
account_id = '{{ account_id }}' --required
AND key_rotation_interval_days = '{{ key_rotation_interval_days }}' --required
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
    defaultValue="rotate"
    values={[
        { label: 'rotate', value: 'rotate' }
    ]}
>
<TabItem value="rotate">

Perfoms a key rotation for an account.

```sql
EXEC cloudflare.zero_trust.keys.rotate 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
