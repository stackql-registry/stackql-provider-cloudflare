--- 
title: workers_scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - workers_scripts
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

Creates, updates, deletes, gets or lists a <code>workers_scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workers_scripts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.workers_scripts" /></td></tr>
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

List Workers response.

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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The name used to identify the script. (example: my-workers-script)</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_date" /></td>
    <td><code>string</code></td>
    <td>Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker. (example: 2021-01-01)</td>
</tr>
<tr>
    <td><CopyableCode code="compatibility_flags" /></td>
    <td><code>array</code></td>
    <td>Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a `compatibility_date`. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was created. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Hashed script content, can be used in a If-None-Match header when updating. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="handlers" /></td>
    <td><code>array</code></td>
    <td>The names of handlers exported as part of the default export.</td>
</tr>
<tr>
    <td><CopyableCode code="has_assets" /></td>
    <td><code>boolean</code></td>
    <td>Whether a Worker contains assets.</td>
</tr>
<tr>
    <td><CopyableCode code="has_modules" /></td>
    <td><code>boolean</code></td>
    <td>Whether a Worker contains modules.</td>
</tr>
<tr>
    <td><CopyableCode code="last_deployed_from" /></td>
    <td><code>string</code></td>
    <td>The client most recently used to deploy this Worker. (example: wrangler)</td>
</tr>
<tr>
    <td><CopyableCode code="logpush" /></td>
    <td><code>boolean</code></td>
    <td>Whether Logpush is turned on for the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="migration_tag" /></td>
    <td><code>string</code></td>
    <td>The tag of the Durable Object migration that was most recently applied for this Worker. (example: v1)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the script was last modified. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="named_handlers" /></td>
    <td><code>array</code></td>
    <td>Named exports, such as Durable Object class implementations and named entrypoints.</td>
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
    <td><CopyableCode code="placement_mode" /></td>
    <td><code>string</code></td>
    <td>Configuration for [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). Specify mode='smart' for Smart Placement, or one of region/hostname/host. (smart, targeted)</td>
</tr>
<tr>
    <td><CopyableCode code="placement_status" /></td>
    <td><code>string</code></td>
    <td>Status of [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). (SUCCESS, UNSUPPORTED_APPLICATION, INSUFFICIENT_INVOCATIONS)</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Routes associated with the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of the script. (example: e8f70fdbc8b1fb0b8ddb1af166186758)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-tags"><code>tags</code></a></td>
    <td>Fetch a list of uploaded workers.</td>
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
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>Filter scripts by tags. Format: comma-separated list of tag:allowed pairs where allowed is 'yes' or 'no'.</td>
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

Fetch a list of uploaded workers.

```sql
SELECT
id,
compatibility_date,
compatibility_flags,
created_on,
etag,
handlers,
has_assets,
has_modules,
last_deployed_from,
logpush,
migration_tag,
modified_on,
named_handlers,
observability,
placement,
placement_mode,
placement_status,
routes,
tag,
tags,
tail_consumers,
usage_model
FROM cloudflare.workers.workers_scripts
WHERE account_id = '{{ account_id }}' -- required
AND tags = '{{ tags }}'
;
```
</TabItem>
</Tabs>
