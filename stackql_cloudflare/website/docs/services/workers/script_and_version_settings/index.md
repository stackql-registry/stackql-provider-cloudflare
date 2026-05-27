--- 
title: script_and_version_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - script_and_version_settings
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

Creates, updates, deletes, gets or lists a <code>script_and_version_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="script_and_version_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.script_and_version_settings" /></td></tr>
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

Fetch settings.

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
    <td><CopyableCode code="annotations" /></td>
    <td><code>object</code></td>
    <td>Annotations for the Worker version. Annotations are not inherited across settings updates; omitting this field means the new version will have no annotations.</td>
</tr>
<tr>
    <td><CopyableCode code="bindings" /></td>
    <td><code>array</code></td>
    <td>List of bindings attached to a Worker. You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_date" /></td>
    <td><code>string</code></td>
    <td>Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker. (example: 2021-01-01, default: )</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_flags" /></td>
    <td><code>array</code></td>
    <td>Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a `compatibility_date`. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="limits" /></td>
    <td><code>object</code></td>
    <td>Limits to apply for this Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="logpush" /></td>
    <td><code>boolean</code></td>
    <td>Whether Logpush is turned on for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="migrations" /></td>
    <td><code>object</code></td>
    <td>Migrations to apply for Durable Objects associated with this Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="observability" /></td>
    <td><code>object</code></td>
    <td>Observability settings for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="placement" /></td>
    <td><code>object</code></td>
    <td>Configuration for [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). Specify mode='smart' for Smart Placement, or one of region/hostname/host.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Tags associated with the Worker. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="tail_consumers" /></td>
    <td><code>array</code></td>
    <td>List of Workers that will consume logs from the attached Worker. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="usage_model" /></td>
    <td><code>string</code></td>
    <td>Usage model for the Worker invocations. (standard, bundled, unbound) (default: standard, example: standard)</td>
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
    <td>Get metadata and config, such as bindings or usage model.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Patch metadata or config, such as bindings or usage model.</td>
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

Get metadata and config, such as bindings or usage model.

```sql
SELECT
annotations,
bindings,
compatibility_date,
compatibility_flags,
limits,
logpush,
migrations,
observability,
placement,
tags,
tail_consumers,
usage_model
FROM cloudflare.workers.script_and_version_settings
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
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

Patch metadata or config, such as bindings or usage model.

```sql
UPDATE cloudflare.workers.script_and_version_settings
SET 
settings = '{{ settings }}'
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
