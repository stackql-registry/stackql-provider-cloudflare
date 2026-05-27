--- 
title: silences
hide_title: false
hide_table_of_contents: false
keywords:
  - silences
  - alerting
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

Creates, updates, deletes, gets or lists a <code>silences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="silences" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.alerting.silences" /></td></tr>
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

Get Silence response

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
    <td>Silence ID (example: f878e90c23f44126ae3cfc399f646977)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of a notification policy (example: 0da2b59ef118439d8097bdfb215203c9)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>When the silence was created. (example: 2022-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="end_time" /></td>
    <td><code>string</code></td>
    <td>When the silence ends. (example: 2022-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string</code></td>
    <td>When the silence starts. (example: 2022-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>When the silence was modified. (example: 2022-01-01T00:00:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Silences response

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
    <td>Silence ID (example: f878e90c23f44126ae3cfc399f646977)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of a notification policy (example: 0da2b59ef118439d8097bdfb215203c9)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>When the silence was created. (example: 2022-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="end_time" /></td>
    <td><code>string</code></td>
    <td>When the silence ends. (example: 2022-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string</code></td>
    <td>When the silence starts. (example: 2022-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>When the silence was modified. (example: 2022-01-01T00:00:00Z)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-silence_id"><code>silence_id</code></a></td>
    <td></td>
    <td>Gets a specific silence for an account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets a list of silences for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new silence for an account.</td>
</tr>
<tr>
    <td><a href="#notification_silences_update_silences"><CopyableCode code="notification_silences_update_silences" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates existing silences for an account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-silence_id"><code>silence_id</code></a></td>
    <td></td>
    <td>Deletes an existing silence for an account.</td>
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
<tr id="parameter-silence_id">
    <td><CopyableCode code="silence_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Gets a specific silence for an account.

```sql
SELECT
id,
policy_id,
created_at,
end_time,
start_time,
updated_at
FROM cloudflare.alerting.silences
WHERE account_id = '{{ account_id }}' -- required
AND silence_id = '{{ silence_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of silences for an account.

```sql
SELECT
id,
policy_id,
created_at,
end_time,
start_time,
updated_at
FROM cloudflare.alerting.silences
WHERE account_id = '{{ account_id }}' -- required
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

Creates a new silence for an account.

```sql
INSERT INTO cloudflare.alerting.silences (
account_id
)
SELECT 
'{{ account_id }}'
RETURNING
errors,
messages,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: silences
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the silences resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="notification_silences_update_silences"
    values={[
        { label: 'notification_silences_update_silences', value: 'notification_silences_update_silences' }
    ]}
>
<TabItem value="notification_silences_update_silences">

Updates existing silences for an account.

```sql
REPLACE cloudflare.alerting.silences
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
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

Deletes an existing silence for an account.

```sql
DELETE FROM cloudflare.alerting.silences
WHERE account_id = '{{ account_id }}' --required
AND silence_id = '{{ silence_id }}' --required
;
```
</TabItem>
</Tabs>
