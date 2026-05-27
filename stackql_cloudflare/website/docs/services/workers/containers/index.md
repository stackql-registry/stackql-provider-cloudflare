--- 
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
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

Creates, updates, deletes, gets or lists a <code>containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="containers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.containers" /></td></tr>
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

Returns all public applications associated with your account.

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
    <td>An Application ID represents an identifier of an application</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>UTC timestamp string in ISO 8601 format (example: 2021-04-01T12:32:41.488Z)</td>
</tr>
<tr>
    <td><CopyableCode code="durable_object" /></td>
    <td><code>object</code></td>
    <td>Durable object configuration using a namespace ID</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Shows a count of application instance states.</td>
</tr>
<tr>
    <td><CopyableCode code="image" /></td>
    <td><code>string</code></td>
    <td>Image url</td>
</tr>
<tr>
    <td><CopyableCode code="instance_type" /></td>
    <td><code>object</code></td>
    <td>Specifies either a pre-set instance type or a custom resource allocation. (lite, basic, standard-1, standard-2, standard-3, standard-4) (example: lite, default: lite)</td>
</tr>
<tr>
    <td><CopyableCode code="max_instances" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of instances that the application will allow.</td>
</tr>
<tr>
    <td><CopyableCode code="network" /></td>
    <td><code>object</code></td>
    <td>Network settings for an application</td>
</tr>
<tr>
    <td><CopyableCode code="observability" /></td>
    <td><code>object</code></td>
    <td>Settings for application observability such as logging.</td>
</tr>
<tr>
    <td><CopyableCode code="rollout_active_grace_period" /></td>
    <td><code>integer</code></td>
    <td>Grace period for active instances to stay alive before becoming eligible for shutdown signal due to a rollout, in seconds. Defaults to 0.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>UTC timestamp string in ISO 8601 format (example: 2021-04-01T12:32:41.488Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>The current version number of this application. This increments with application rollouts.</td>
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-image"><code>image</code></a></td>
    <td>Lists all the container applications that are associated with your account.</td>
</tr>
<tr>
    <td><a href="#create_credentials"><CopyableCode code="create_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-permissions"><code>permissions</code></a>, <a href="#parameter-expiration_minutes"><code>expiration_minutes</code></a></td>
    <td></td>
    <td>Generates temporary credentials for accessing Cloudflare's container image registry. Used for pulling and pushing container images.</td>
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
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-image">
    <td><CopyableCode code="image" /></td>
    <td><code>string</code></td>
    <td>Filter containers by image</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Filter containers by name</td>
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

Lists all the container applications that are associated with your account.

```sql
SELECT
id,
name,
created_at,
durable_object,
health,
image,
instance_type,
max_instances,
network,
observability,
rollout_active_grace_period,
updated_at,
version
FROM cloudflare.workers.containers
WHERE account_id = '{{ account_id }}' -- required
AND name = '{{ name }}'
AND image = '{{ image }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_credentials"
    values={[
        { label: 'create_credentials', value: 'create_credentials' }
    ]}
>
<TabItem value="create_credentials">

Generates temporary credentials for accessing Cloudflare's container image registry. Used for pulling and pushing container images.

```sql
EXEC cloudflare.workers.containers.create_credentials 
@domain='{{ domain }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"expiration_minutes": {{ expiration_minutes }}, 
"permissions": "{{ permissions }}"
}'
;
```
</TabItem>
</Tabs>
