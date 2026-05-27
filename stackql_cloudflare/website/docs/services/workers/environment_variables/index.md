--- 
title: environment_variables
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_variables
  - workers
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

Creates, updates, deletes, gets or lists an <code>environment_variables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="environment_variables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.environment_variables" /></td></tr>
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

Environment variables retrieved successfully

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
    <td><CopyableCode code="result_info" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a></td>
    <td></td>
    <td>Get all environment variables for a trigger</td>
</tr>
<tr>
    <td><a href="#upsert_environment_variables"><CopyableCode code="upsert_environment_variables" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a></td>
    <td></td>
    <td>Create or update environment variables for a trigger</td>
</tr>
<tr>
    <td><a href="#delete_environment_variable"><CopyableCode code="delete_environment_variable" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-trigger_uuid"><code>trigger_uuid</code></a>, <a href="#parameter-environment_variable_key"><code>environment_variable_key</code></a></td>
    <td></td>
    <td>Remove a specific environment variable from a trigger</td>
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
<tr id="parameter-environment_variable_key">
    <td><CopyableCode code="environment_variable_key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-trigger_uuid">
    <td><CopyableCode code="trigger_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
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

Get all environment variables for a trigger

```sql
SELECT
errors,
messages,
result,
result_info,
success
FROM cloudflare.workers.environment_variables
WHERE account_id = '{{ account_id }}' -- required
AND trigger_uuid = '{{ trigger_uuid }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="upsert_environment_variables"
    values={[
        { label: 'upsert_environment_variables', value: 'upsert_environment_variables' }
    ]}
>
<TabItem value="upsert_environment_variables">

Create or update environment variables for a trigger

```sql
UPDATE cloudflare.workers.environment_variables
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND trigger_uuid = '{{ trigger_uuid }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_environment_variable"
    values={[
        { label: 'delete_environment_variable', value: 'delete_environment_variable' }
    ]}
>
<TabItem value="delete_environment_variable">

Remove a specific environment variable from a trigger

```sql
DELETE FROM cloudflare.workers.environment_variables
WHERE account_id = '{{ account_id }}' --required
AND trigger_uuid = '{{ trigger_uuid }}' --required
AND environment_variable_key = '{{ environment_variable_key }}' --required
;
```
</TabItem>
</Tabs>
