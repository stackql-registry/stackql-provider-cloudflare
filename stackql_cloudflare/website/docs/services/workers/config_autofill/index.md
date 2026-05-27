--- 
title: config_autofill
hide_title: false
hide_table_of_contents: false
keywords:
  - config_autofill
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

Creates, updates, deletes, gets or lists a <code>config_autofill</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="config_autofill" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.config_autofill" /></td></tr>
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

Configuration autofill data retrieved successfully

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
    <td><CopyableCode code="default_worker_name" /></td>
    <td><code>string</code></td>
    <td> (example: my-worker)</td>
</tr>
<tr>
    <td><CopyableCode code="config_file" /></td>
    <td><code>string</code></td>
    <td> (example: wrangler.toml)</td>
</tr>
<tr>
    <td><CopyableCode code="env_worker_names" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="package_manager" /></td>
    <td><code>string</code></td>
    <td> (npm, yarn, pnpm, bun, uv) (example: npm)</td>
</tr>
<tr>
    <td><CopyableCode code="scripts" /></td>
    <td><code>object</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-provider_type"><code>provider_type</code></a>, <a href="#parameter-provider_account_id"><code>provider_account_id</code></a>, <a href="#parameter-repo_id"><code>repo_id</code></a></td>
    <td><a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-root_directory"><code>root_directory</code></a></td>
    <td>Analyze repository for automatic configuration detection</td>
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
<tr id="parameter-provider_account_id">
    <td><CopyableCode code="provider_account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-provider_type">
    <td><CopyableCode code="provider_type" /></td>
    <td><code>string</code></td>
    <td>SCM provider type</td>
</tr>
<tr id="parameter-repo_id">
    <td><CopyableCode code="repo_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-branch">
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-root_directory">
    <td><CopyableCode code="root_directory" /></td>
    <td><code>string</code></td>
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

Analyze repository for automatic configuration detection

```sql
SELECT
default_worker_name,
config_file,
env_worker_names,
package_manager,
scripts
FROM cloudflare.workers.config_autofill
WHERE account_id = '{{ account_id }}' -- required
AND provider_type = '{{ provider_type }}' -- required
AND provider_account_id = '{{ provider_account_id }}' -- required
AND repo_id = '{{ repo_id }}' -- required
AND branch = '{{ branch }}'
AND root_directory = '{{ root_directory }}'
;
```
</TabItem>
</Tabs>
