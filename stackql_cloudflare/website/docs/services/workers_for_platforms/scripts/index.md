--- 
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
  - workers_for_platforms
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

Creates, updates, deletes, gets or lists a <code>scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scripts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers_for_platforms.scripts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Worker Details Response (Workers for Platforms).

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
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was created. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="dispatch_namespace" /></td>
    <td><code>string</code></td>
    <td>Name of the Workers for Platforms dispatch namespace. (example: my-dispatch-namespace)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was last modified. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="script" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Fetch information about a script uploaded to a Workers for Platforms namespace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td><a href="#parameter-bindings_inherit"><code>bindings_inherit</code></a></td>
    <td>Upload a worker module to a Workers for Platforms namespace. You can find more about the multipart metadata on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete a worker from a Workers for Platforms namespace. This call has no response body on a successful delete.</td>
</tr>
<tr>
    <td><a href="#create_assets_upload_session"><CopyableCode code="create_assets_upload_session" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-manifest"><code>manifest</code></a></td>
    <td></td>
    <td>Start uploading a collection of assets for use in a Worker version. To learn more about the direct uploads of assets, see https://developers.cloudflare.com/workers/static-assets/direct-upload/.</td>
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
<tr id="parameter-dispatch_namespace">
    <td><CopyableCode code="dispatch_namespace" /></td>
    <td><code>string</code></td>
    <td>The Workers-for-Platforms dispatch namespace.</td>
</tr>
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
</tr>
<tr id="parameter-bindings_inherit">
    <td><CopyableCode code="bindings_inherit" /></td>
    <td><code>string</code></td>
    <td>When set to "strict", the upload will fail if any `inherit` type bindings cannot be resolved against the previous version of the script. Without this, unresolvable inherit bindings are silently dropped.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, delete will not be stopped by associated service binding, durable object, or other binding. Any of these associated bindings/durable objects will be deleted along with the script.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Fetch information about a script uploaded to a Workers for Platforms namespace.

```sql
SELECT
created_on,
dispatch_namespace,
modified_on,
script
FROM cloudflare.workers_for_platforms.scripts
WHERE account_id = '{{ account_id }}' -- required
AND dispatch_namespace = '{{ dispatch_namespace }}' -- required
AND script_name = '{{ script_name }}' -- required
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

Upload a worker module to a Workers for Platforms namespace. You can find more about the multipart metadata on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.

```sql
REPLACE cloudflare.workers_for_platforms.scripts
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND bindings_inherit = '{{ bindings_inherit}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a worker from a Workers for Platforms namespace. This call has no response body on a successful delete.

```sql
DELETE FROM cloudflare.workers_for_platforms.scripts
WHERE account_id = '{{ account_id }}' --required
AND dispatch_namespace = '{{ dispatch_namespace }}' --required
AND script_name = '{{ script_name }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_assets_upload_session"
    values={[
        { label: 'create_assets_upload_session', value: 'create_assets_upload_session' }
    ]}
>
<TabItem value="create_assets_upload_session">

Start uploading a collection of assets for use in a Worker version. To learn more about the direct uploads of assets, see https://developers.cloudflare.com/workers/static-assets/direct-upload/.

```sql
EXEC cloudflare.workers_for_platforms.scripts.create_assets_upload_session 
@account_id='{{ account_id }}' --required, 
@dispatch_namespace='{{ dispatch_namespace }}' --required, 
@script_name='{{ script_name }}' --required 
@@json=
'{
"manifest": "{{ manifest }}"
}'
;
```
</TabItem>
</Tabs>
