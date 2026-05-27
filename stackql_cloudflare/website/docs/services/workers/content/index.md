--- 
title: content
hide_title: false
hide_table_of_contents: false
keywords:
  - content
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

Creates, updates, deletes, gets or lists a <code>content</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="content" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.content" /></td></tr>
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
    <td><a href="#worker_environment_put_script_content"><CopyableCode code="worker_environment_put_script_content" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-metadata"><code>metadata</code></a></td>
    <td><a href="#parameter-CF-WORKER-BODY-PART"><code>CF-WORKER-BODY-PART</code></a>, <a href="#parameter-CF-WORKER-MAIN-MODULE-PART"><code>CF-WORKER-MAIN-MODULE-PART</code></a></td>
    <td>Put script content from a worker with an environment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-metadata"><code>metadata</code></a></td>
    <td><a href="#parameter-CF-WORKER-BODY-PART"><code>CF-WORKER-BODY-PART</code></a>, <a href="#parameter-CF-WORKER-MAIN-MODULE-PART"><code>CF-WORKER-MAIN-MODULE-PART</code></a></td>
    <td>Put script content without touching config or metadata.</td>
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
<tr id="parameter-CF-WORKER-BODY-PART">
    <td><CopyableCode code="CF-WORKER-BODY-PART" /></td>
    <td><code>string</code></td>
    <td>The multipart name of a script upload part containing script content in service worker format. Alternative to including in a metadata part.</td>
</tr>
<tr id="parameter-CF-WORKER-MAIN-MODULE-PART">
    <td><CopyableCode code="CF-WORKER-MAIN-MODULE-PART" /></td>
    <td><code>string</code></td>
    <td>The multipart name of a script upload part containing script content in es module format. Alternative to including in a metadata part.</td>
</tr>
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="worker_environment_put_script_content"
    values={[
        { label: 'worker_environment_put_script_content', value: 'worker_environment_put_script_content' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="worker_environment_put_script_content">

Put script content from a worker with an environment.

```sql
REPLACE cloudflare.workers.content
SET 
files = '{{ files }}',
metadata = '{{ metadata }}'
WHERE 
account_id = '{{ account_id }}' --required
AND service_name = '{{ service_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND metadata = '{{ metadata }}' --required
AND CF-WORKER-BODY-PART = '{{ CF-WORKER-BODY-PART}}'
AND CF-WORKER-MAIN-MODULE-PART = '{{ CF-WORKER-MAIN-MODULE-PART}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update">

Put script content without touching config or metadata.

```sql
REPLACE cloudflare.workers.content
SET 
files = '{{ files }}',
metadata = '{{ metadata }}'
WHERE 
account_id = '{{ account_id }}' --required
AND script_name = '{{ script_name }}' --required
AND metadata = '{{ metadata }}' --required
AND CF-WORKER-BODY-PART = '{{ CF-WORKER-BODY-PART}}'
AND CF-WORKER-MAIN-MODULE-PART = '{{ CF-WORKER-MAIN-MODULE-PART}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
