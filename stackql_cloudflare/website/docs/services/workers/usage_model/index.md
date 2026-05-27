--- 
title: usage_model
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_model
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

Creates, updates, deletes, gets or lists a <code>usage_model</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="usage_model" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.usage_model" /></td></tr>
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

Fetch Usage Model response.

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
    <td><CopyableCode code="usage_model" /></td>
    <td><code>string</code></td>
    <td>Usage model for the Worker invocations. (standard, bundled, unbound) (default: standard, example: standard)</td>
</tr>
<tr>
    <td><CopyableCode code="user_limits" /></td>
    <td><code>object</code></td>
    <td>User-defined resource limits for Workers with standard usage model.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Fetches the Usage Model for a given Worker.</td>
</tr>
<tr>
    <td><a href="#worker_script_update_usage_model"><CopyableCode code="worker_script_update_usage_model" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Updates the Usage Model for a given Worker. Requires a Workers Paid subscription.</td>
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
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
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

Fetches the Usage Model for a given Worker.

```sql
SELECT
usage_model,
user_limits
FROM cloudflare.workers.usage_model
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="worker_script_update_usage_model"
    values={[
        { label: 'worker_script_update_usage_model', value: 'worker_script_update_usage_model' }
    ]}
>
<TabItem value="worker_script_update_usage_model">

Updates the Usage Model for a given Worker. Requires a Workers Paid subscription.

```sql
REPLACE cloudflare.workers.usage_model
SET 
usage_model = '{{ usage_model }}',
user_limits = '{{ user_limits }}'
WHERE 
account_id = '{{ account_id }}' --required
AND script_name = '{{ script_name }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
