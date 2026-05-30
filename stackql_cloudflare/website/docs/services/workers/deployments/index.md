--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.deployments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get Deployment response.

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
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="author_email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td> (example: api)</td>
</tr>
<tr>
    <td><CopyableCode code="strategy" /></td>
    <td><code>string</code></td>
    <td> (percentage)</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Deployments response.

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
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="author_email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td> (example: api)</td>
</tr>
<tr>
    <td><CopyableCode code="strategy" /></td>
    <td><code>string</code></td>
    <td> (percentage)</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-deployment_id"><code>deployment_id</code></a></td>
    <td></td>
    <td>Get information about a Worker Deployment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>List of Worker Deployments. The first deployment in the list is the latest deployment actively serving traffic.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-strategy"><code>strategy</code></a>, <a href="#parameter-versions"><code>versions</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Deployments configure how [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions) are deployed to traffic. A deployment can consist of one or two versions of a Worker.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-deployment_id"><code>deployment_id</code></a></td>
    <td></td>
    <td>Delete a Worker Deployment. The latest deployment, which is actively serving traffic, cannot be deleted. All other deployments can be deleted.</td>
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
<tr id="parameter-deployment_id">
    <td><CopyableCode code="deployment_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, the deployment will be created even if normally blocked by something such rolling back to an older version when a secret has changed.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get information about a Worker Deployment.

```sql
SELECT
id,
annotations,
author_email,
created_on,
source,
strategy,
versions
FROM cloudflare.workers.deployments
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
AND deployment_id = '{{ deployment_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List of Worker Deployments. The first deployment in the list is the latest deployment actively serving traffic.

```sql
SELECT
id,
annotations,
author_email,
created_on,
source,
strategy,
versions
FROM cloudflare.workers.deployments
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Deployments configure how [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions) are deployed to traffic. A deployment can consist of one or two versions of a Worker.

```sql
INSERT INTO cloudflare.workers.deployments (
annotations,
strategy,
versions,
account_id,
script_name,
force
)
SELECT 
'{{ annotations }}',
'{{ strategy }}' /* required */,
'{{ versions }}' /* required */,
'{{ account_id }}',
'{{ script_name }}',
'{{ force }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: deployments
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the deployments resource.
    - name: script_name
      value: "{{ script_name }}"
      description: Required parameter for the deployments resource.
    - name: annotations
      value:
        workers/message: "{{ workers/message }}"
        workers/triggered_by: "{{ workers/triggered_by }}"
    - name: strategy
      value: "{{ strategy }}"
      valid_values: ['percentage']
    - name: versions
      value:
        - percentage: {{ percentage }}
          version_id: "{{ version_id }}"
    - name: force
      value: {{ force }}
      description: If set to true, the deployment will be created even if normally blocked by something such rolling back to an older version when a secret has changed.
      description: If set to true, the deployment will be created even if normally blocked by something such rolling back to an older version when a secret has changed.
`}</CodeBlock>

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

Delete a Worker Deployment. The latest deployment, which is actively serving traffic, cannot be deleted. All other deployments can be deleted.

```sql
DELETE FROM cloudflare.workers.deployments
WHERE account_id = '{{ account_id }}' --required
AND script_name = '{{ script_name }}' --required
AND deployment_id = '{{ deployment_id }}' --required
;
```
</TabItem>
</Tabs>
