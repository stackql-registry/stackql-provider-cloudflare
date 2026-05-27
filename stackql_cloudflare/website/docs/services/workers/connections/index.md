--- 
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.connections" /></td></tr>
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
    <td><a href="#upsert_repo_connection"><CopyableCode code="upsert_repo_connection" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-repo_id"><code>repo_id</code></a>, <a href="#parameter-repo_name"><code>repo_name</code></a>, <a href="#parameter-provider_type"><code>provider_type</code></a>, <a href="#parameter-provider_account_id"><code>provider_account_id</code></a>, <a href="#parameter-provider_account_name"><code>provider_account_name</code></a></td>
    <td></td>
    <td>Upsert a repository connection for CI/CD integration</td>
</tr>
<tr>
    <td><a href="#delete_repo_connection"><CopyableCode code="delete_repo_connection" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-repo_connection_uuid"><code>repo_connection_uuid</code></a></td>
    <td></td>
    <td>Remove a repository connection</td>
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
<tr id="parameter-repo_connection_uuid">
    <td><CopyableCode code="repo_connection_uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="upsert_repo_connection"
    values={[
        { label: 'upsert_repo_connection', value: 'upsert_repo_connection' }
    ]}
>
<TabItem value="upsert_repo_connection">

Upsert a repository connection for CI/CD integration

```sql
REPLACE cloudflare.workers.connections
SET 
provider_account_id = '{{ provider_account_id }}',
provider_account_name = '{{ provider_account_name }}',
provider_type = '{{ provider_type }}',
repo_id = '{{ repo_id }}',
repo_name = '{{ repo_name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND repo_id = '{{ repo_id }}' --required
AND repo_name = '{{ repo_name }}' --required
AND provider_type = '{{ provider_type }}' --required
AND provider_account_id = '{{ provider_account_id }}' --required
AND provider_account_name = '{{ provider_account_name }}' --required
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
    defaultValue="delete_repo_connection"
    values={[
        { label: 'delete_repo_connection', value: 'delete_repo_connection' }
    ]}
>
<TabItem value="delete_repo_connection">

Remove a repository connection

```sql
DELETE FROM cloudflare.workers.connections
WHERE account_id = '{{ account_id }}' --required
AND repo_connection_uuid = '{{ repo_connection_uuid }}' --required
;
```
</TabItem>
</Tabs>
