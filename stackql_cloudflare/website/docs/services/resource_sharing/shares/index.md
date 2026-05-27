--- 
title: shares
hide_title: false
hide_table_of_contents: false
keywords:
  - shares
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

Creates, updates, deletes, gets or lists a <code>shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="shares" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.resource_sharing.shares" /></td></tr>
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

Get account share response.

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
    <td>Share identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the share. (example: My Shared WAF Managed Rule)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>Organization identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The display name of an account. (example: Account A)</td>
</tr>
<tr>
    <td><CopyableCode code="associated_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'associated' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="associating_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'associating' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="disassociated_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'disassociated' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="disassociating_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'disassociating' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td> (sent, received)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>A list of resources that are part of the share. This field is only included when requested via the 'include_resources' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (active, deleting, deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="target_type" /></td>
    <td><code>string</code></td>
    <td> (account, organization)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List account shares response.

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
    <td>Share identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the share. (example: My Shared WAF Managed Rule)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>Organization identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The display name of an account. (example: Account A)</td>
</tr>
<tr>
    <td><CopyableCode code="associated_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'associated' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="associating_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'associating' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="disassociated_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'disassociated' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="disassociating_recipient_count" /></td>
    <td><code>integer</code></td>
    <td>The number of recipients in the 'disassociating' state. This field is only included when requested via the 'include_recipient_counts' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td> (sent, received)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>A list of resources that are part of the share. This field is only included when requested via the 'include_resources' parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (active, deleting, deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="target_type" /></td>
    <td><code>string</code></td>
    <td> (account, organization)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a></td>
    <td><a href="#parameter-include_resources"><code>include_resources</code></a>, <a href="#parameter-include_recipient_counts"><code>include_recipient_counts</code></a></td>
    <td>Fetches share by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-target_type"><code>target_type</code></a>, <a href="#parameter-resource_types"><code>resource_types</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-include_resources"><code>include_resources</code></a>, <a href="#parameter-include_recipient_counts"><code>include_recipient_counts</code></a></td>
    <td>Lists all account shares.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-resources"><code>resources</code></a>, <a href="#parameter-recipients"><code>recipients</code></a></td>
    <td></td>
    <td>Creates a new resource share for sharing Cloudflare resources with other accounts or organizations.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Updating is not immediate, an updated share object with a new status will be returned.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a></td>
    <td></td>
    <td>Deletion is not immediate, an updated share object with a new status will be returned.</td>
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
<tr id="parameter-share_id">
    <td><CopyableCode code="share_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Direction to sort objects.</td>
</tr>
<tr id="parameter-include_recipient_counts">
    <td><CopyableCode code="include_recipient_counts" /></td>
    <td><code>boolean</code></td>
    <td>Include recipient counts in the response.</td>
</tr>
<tr id="parameter-include_resources">
    <td><CopyableCode code="include_resources" /></td>
    <td><code>boolean</code></td>
    <td>Include resources in the response.</td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Filter shares by kind.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Order shares by values in the given field.</td>
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
<tr id="parameter-resource_types">
    <td><CopyableCode code="resource_types" /></td>
    <td><code>array</code></td>
    <td>Filter share resources by resource_types.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter shares by status.</td>
</tr>
<tr id="parameter-target_type">
    <td><CopyableCode code="target_type" /></td>
    <td><code>string</code></td>
    <td>Filter shares by target_type.</td>
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

Fetches share by ID.

```sql
SELECT
id,
name,
account_id,
organization_id,
account_name,
associated_recipient_count,
associating_recipient_count,
created,
disassociated_recipient_count,
disassociating_recipient_count,
kind,
modified,
resources,
status,
target_type
FROM cloudflare.resource_sharing.shares
WHERE account_id = '{{ account_id }}' -- required
AND share_id = '{{ share_id }}' -- required
AND include_resources = '{{ include_resources }}'
AND include_recipient_counts = '{{ include_recipient_counts }}'
;
```
</TabItem>
<TabItem value="list">

Lists all account shares.

```sql
SELECT
id,
name,
account_id,
organization_id,
account_name,
associated_recipient_count,
associating_recipient_count,
created,
disassociated_recipient_count,
disassociating_recipient_count,
kind,
modified,
resources,
status,
target_type
FROM cloudflare.resource_sharing.shares
WHERE account_id = '{{ account_id }}' -- required
AND status = '{{ status }}'
AND kind = '{{ kind }}'
AND target_type = '{{ target_type }}'
AND resource_types = '{{ resource_types }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND include_resources = '{{ include_resources }}'
AND include_recipient_counts = '{{ include_recipient_counts }}'
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

Creates a new resource share for sharing Cloudflare resources with other accounts or organizations.

```sql
INSERT INTO cloudflare.resource_sharing.shares (
name,
recipients,
resources,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ recipients }}' /* required */,
'{{ resources }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: shares
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the shares resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the share.
    - name: recipients
      value:
        - account_id: "{{ account_id }}"
          organization_id: "{{ organization_id }}"
    - name: resources
      value:
        - meta: "{{ meta }}"
          resource_account_id: "{{ resource_account_id }}"
          resource_id: "{{ resource_id }}"
          resource_type: "{{ resource_type }}"
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

Updating is not immediate, an updated share object with a new status will be returned.

```sql
REPLACE cloudflare.resource_sharing.shares
SET 
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND share_id = '{{ share_id }}' --required
AND name = '{{ name }}' --required
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

Deletion is not immediate, an updated share object with a new status will be returned.

```sql
DELETE FROM cloudflare.resource_sharing.shares
WHERE account_id = '{{ account_id }}' --required
AND share_id = '{{ share_id }}' --required
;
```
</TabItem>
</Tabs>
