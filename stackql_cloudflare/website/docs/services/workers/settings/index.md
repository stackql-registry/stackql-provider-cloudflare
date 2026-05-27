--- 
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.settings" /></td></tr>
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
    <td><a href="#worker_script_environment_patch_settings"><CopyableCode code="worker_script_environment_patch_settings" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-success"><code>success</code></a>, <a href="#parameter-errors"><code>errors</code></a>, <a href="#parameter-messages"><code>messages</code></a>, <a href="#parameter-result"><code>result</code></a></td>
    <td></td>
    <td>Patch script metadata, such as bindings.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Patch script-level settings when using [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions). Including but not limited to Logpush and Tail Consumers.</td>
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
<tr id="parameter-environment_name">
    <td><CopyableCode code="environment_name" /></td>
    <td><code>string</code></td>
    <td>The Worker service environment name.</td>
</tr>
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The Worker service name.</td>
</tr>
</tbody>
</table>

## `UPDATE` examples

<Tabs
    defaultValue="worker_script_environment_patch_settings"
    values={[
        { label: 'worker_script_environment_patch_settings', value: 'worker_script_environment_patch_settings' },
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="worker_script_environment_patch_settings">

Patch script metadata, such as bindings.

```sql
UPDATE cloudflare.workers.settings
SET 
errors = '{{ errors }}',
messages = '{{ messages }}',
success = {{ success }},
result = '{{ result }}'
WHERE 
account_id = '{{ account_id }}' --required
AND service_name = '{{ service_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND success = {{ success }} --required
AND errors = '{{ errors }}' --required
AND messages = '{{ messages }}' --required
AND result = '{{ result }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="edit">

Patch script-level settings when using [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions). Including but not limited to Logpush and Tail Consumers.

```sql
UPDATE cloudflare.workers.settings
SET 
logpush = {{ logpush }},
observability = '{{ observability }}',
tags = '{{ tags }}',
tail_consumers = '{{ tail_consumers }}'
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
