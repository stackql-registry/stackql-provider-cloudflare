--- 
title: recipients
hide_title: false
hide_table_of_contents: false
keywords:
  - recipients
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

Creates, updates, deletes, gets or lists a <code>recipients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recipients" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.resource_sharing.recipients" /></td></tr>
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

Get account share recipient response.

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
    <td>Share Recipient identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="association_status" /></td>
    <td><code>string</code></td>
    <td>Share Recipient association status. (associating, associated, disassociating, disassociated)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List account share recipients response.

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
    <td>Share Recipient identifier tag. (example: 3fd85f74b32742f1bff64a85009dda07)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="association_status" /></td>
    <td><code>string</code></td>
    <td>Share Recipient association status. (associating, associated, disassociating, disassociated)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was created. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the share was modified. (example: 2023-09-21T18:56:32.624632Z)</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-recipient_id"><code>recipient_id</code></a></td>
    <td><a href="#parameter-include_resources"><code>include_resources</code></a></td>
    <td>Get share recipient by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a></td>
    <td><a href="#parameter-include_resources"><code>include_resources</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List share recipients by share ID.</td>
</tr>
<tr>
    <td><a href="#share_recipient_create"><CopyableCode code="share_recipient_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a></td>
    <td></td>
    <td>Adds a recipient to a resource share, granting them access to the shared resources.</td>
</tr>
<tr>
    <td><a href="#share_recipients_update"><CopyableCode code="share_recipients_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a></td>
    <td></td>
    <td>Changes a share's recipients to match the given list. Returns an error if the share targets an organization.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-share_id"><code>share_id</code></a>, <a href="#parameter-recipient_id"><code>recipient_id</code></a></td>
    <td></td>
    <td>Deletion is not immediate, an updated share recipient object with a new status will be returned.</td>
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
<tr id="parameter-recipient_id">
    <td><CopyableCode code="recipient_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-share_id">
    <td><CopyableCode code="share_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-include_resources">
    <td><CopyableCode code="include_resources" /></td>
    <td><code>boolean</code></td>
    <td>Include resources in the response.</td>
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

Get share recipient by ID.

```sql
SELECT
id,
account_id,
association_status,
created,
modified,
resources
FROM cloudflare.resource_sharing.recipients
WHERE account_id = '{{ account_id }}' -- required
AND share_id = '{{ share_id }}' -- required
AND recipient_id = '{{ recipient_id }}' -- required
AND include_resources = '{{ include_resources }}'
;
```
</TabItem>
<TabItem value="list">

List share recipients by share ID.

```sql
SELECT
id,
account_id,
association_status,
created,
modified,
resources
FROM cloudflare.resource_sharing.recipients
WHERE account_id = '{{ account_id }}' -- required
AND share_id = '{{ share_id }}' -- required
AND include_resources = '{{ include_resources }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="share_recipient_create"
    values={[
        { label: 'share_recipient_create', value: 'share_recipient_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="share_recipient_create">

Adds a recipient to a resource share, granting them access to the shared resources.

```sql
INSERT INTO cloudflare.resource_sharing.recipients (
account_id,
organization_id,
account_id,
share_id
)
SELECT 
'{{ account_id }}',
'{{ organization_id }}',
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
- name: recipients
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the recipients resource.
    - name: share_id
      value: "{{ share_id }}"
      description: Required parameter for the recipients resource.
    - name: account_id
      value: "{{ account_id }}"
      description: |
        Account identifier.
    - name: organization_id
      value: "{{ organization_id }}"
      description: |
        Organization identifier.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="share_recipients_update"
    values={[
        { label: 'share_recipients_update', value: 'share_recipients_update' }
    ]}
>
<TabItem value="share_recipients_update">

Changes a share's recipients to match the given list. Returns an error if the share targets an organization.

```sql
REPLACE cloudflare.resource_sharing.recipients
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND share_id = '{{ share_id }}' --required;
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

Deletion is not immediate, an updated share recipient object with a new status will be returned.

```sql
DELETE FROM cloudflare.resource_sharing.recipients
WHERE account_id = '{{ account_id }}' --required
AND share_id = '{{ share_id }}' --required
AND recipient_id = '{{ recipient_id }}' --required
;
```
</TabItem>
</Tabs>
