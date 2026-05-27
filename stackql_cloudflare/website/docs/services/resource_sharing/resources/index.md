--- 
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - resource_sharing
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.resource_sharing.resources" /></td></tr>
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

Get account share resource response.

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
    <td>Share Resource identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Share Resource identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Resource Metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Resource Type. (custom-ruleset, gateway-policy, gateway-destination-ip, gateway-block-page-settings, gateway-extended-email-matching)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_version" /></td>
    <td><code>integer</code></td>
    <td>Resource Version.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Resource Status. (active, deleting, deleted)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List account share resources response.

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
    <td>Share Resource identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>Share Resource identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Resource Metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Resource Type. (custom-ruleset, gateway-policy, gateway-destination-ip, gateway-block-page-settings, gateway-extended-email-matching)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_version" /></td>
    <td><code>integer</code></td>
    <td>Resource Version.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Resource Status. (active, deleting, deleted)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Get share resource by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List share resources by share ID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_account_id"><code>resource_account_id</code></a>, <a href="#parameter-meta"><code>meta</code></a></td>
    <td></td>
    <td>Adds a resource to an existing share, making it available to share recipients.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-meta"><code>meta</code></a></td>
    <td></td>
    <td>Update is not immediate, an updated share resource object with a new status will be returned.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Deletion is not immediate, an updated share resource object with a new status will be returned.</td>
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
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-share_id">
    <td><CopyableCode code="share_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Page number.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of objects to return per page.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>Filter share resources by resource_type.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter share resources by status.</td>
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

Get share resource by ID.

```sql
SELECT
id,
resource_account_id,
resource_id,
created,
meta,
modified,
resource_type,
resource_version,
status
FROM cloudflare.resource_sharing.resources
WHERE account_id = '{{ account_id }}' -- required
AND share_id = '{{ share_id }}' -- required
AND resource_id = '{{ resource_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List share resources by share ID.

```sql
SELECT
id,
resource_account_id,
resource_id,
created,
meta,
modified,
resource_type,
resource_version,
status
FROM cloudflare.resource_sharing.resources
WHERE account_id = '{{ account_id }}' -- required
AND share_id = '{{ share_id }}' -- required
AND status = '{{ status }}'
AND resource_type = '{{ resource_type }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Adds a resource to an existing share, making it available to share recipients.

```sql
INSERT INTO cloudflare.resource_sharing.resources (
meta,
resource_account_id,
resource_id,
resource_type,
account_id,
share_id
)
SELECT 
'{{ meta }}' /* required */,
'{{ resource_account_id }}' /* required */,
'{{ resource_id }}' /* required */,
'{{ resource_type }}' /* required */,
'{{ account_id }}',
'{{ share_id }}'
RETURNING
errors,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: resources
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the resources resource.
    - name: share_id
      value: "{{ share_id }}"
      description: Required parameter for the resources resource.
    - name: meta
      value: "{{ meta }}"
      description: |
        Resource Metadata.
    - name: resource_account_id
      value: "{{ resource_account_id }}"
      description: |
        Account identifier.
    - name: resource_id
      value: "{{ resource_id }}"
      description: |
        Share Resource identifier.
    - name: resource_type
      value: "{{ resource_type }}"
      description: |
        Resource Type.
      valid_values: ['custom-ruleset', 'gateway-policy', 'gateway-destination-ip', 'gateway-block-page-settings', 'gateway-extended-email-matching']
`}</CodeBlock>

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

Update is not immediate, an updated share resource object with a new status will be returned.

```sql
REPLACE cloudflare.resource_sharing.resources
SET 
meta = '{{ meta }}'
WHERE 
account_id = '{{ account_id }}' --required
AND share_id = '{{ share_id }}' --required
AND resource_id = '{{ resource_id }}' --required
AND meta = '{{ meta }}' --required
RETURNING
errors,
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

Deletion is not immediate, an updated share resource object with a new status will be returned.

```sql
DELETE FROM cloudflare.resource_sharing.resources
WHERE account_id = '{{ account_id }}' --required
AND share_id = '{{ share_id }}' --required
AND resource_id = '{{ resource_id }}' --required
;
```
</TabItem>
</Tabs>
