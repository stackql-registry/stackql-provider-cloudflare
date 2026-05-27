--- 
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - realtime_kit
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

Creates, updates, deletes, gets or lists a <code>webhooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="webhooks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.webhooks" /></td></tr>
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

Operation successful

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
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Operation successful

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
    <td>ID of the webhook (example: 0d1f069d-43bb-489a-ad8c-7eb95592ba8e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the webhook (example: All events webhook)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this webhook was created (example: 2022-05-28T07:01:53.075Z)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Set to true if the webhook is active</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>Events this webhook will send updates for</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this webhook was updated (example: 2022-05-28T07:01:53.075Z)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>URL the webhook will send events to (example: https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-webhook_id"><code>webhook_id</code></a></td>
    <td></td>
    <td>Returns webhook details for the given webhook ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Returns details of all webhooks for an App.</td>
</tr>
<tr>
    <td><a href="#create_webhook"><CopyableCode code="create_webhook" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-events"><code>events</code></a></td>
    <td></td>
    <td>Adds a new webhook to an App.</td>
</tr>
<tr>
    <td><a href="#edit_webhook"><CopyableCode code="edit_webhook" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-webhook_id"><code>webhook_id</code></a></td>
    <td></td>
    <td>Edits the webhook details for the given webhook ID.</td>
</tr>
<tr>
    <td><a href="#replace_webhook"><CopyableCode code="replace_webhook" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-webhook_id"><code>webhook_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-events"><code>events</code></a></td>
    <td></td>
    <td>Replace all details for the given webhook ID.</td>
</tr>
<tr>
    <td><a href="#delete_webhook"><CopyableCode code="delete_webhook" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-webhook_id"><code>webhook_id</code></a></td>
    <td></td>
    <td>Removes a webhook for the given webhook ID.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-webhook_id">
    <td><CopyableCode code="webhook_id" /></td>
    <td><code>string</code></td>
    <td>ID of the webhook</td>
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

Returns webhook details for the given webhook ID.

```sql
SELECT
data,
success
FROM cloudflare.realtime_kit.webhooks
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
AND webhook_id = '{{ webhook_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns details of all webhooks for an App.

```sql
SELECT
id,
name,
created_at,
enabled,
events,
updated_at,
url
FROM cloudflare.realtime_kit.webhooks
WHERE account_id = '{{ account_id }}' -- required
AND app_id = '{{ app_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_webhook"
    values={[
        { label: 'create_webhook', value: 'create_webhook' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_webhook">

Adds a new webhook to an App.

```sql
INSERT INTO cloudflare.realtime_kit.webhooks (
enabled,
events,
name,
url,
account_id,
app_id
)
SELECT 
{{ enabled }},
'{{ events }}' /* required */,
'{{ name }}' /* required */,
'{{ url }}' /* required */,
'{{ account_id }}',
'{{ app_id }}'
RETURNING
data,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: webhooks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the webhooks resource.
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the webhooks resource.
    - name: enabled
      value: {{ enabled }}
      description: |
        Set whether or not the webhook should be active when created
      default: true
    - name: events
      value:
        - "{{ events }}"
      description: |
        Events that this webhook will get triggered by
    - name: name
      value: "{{ name }}"
      description: |
        Name of the webhook
    - name: url
      value: "{{ url }}"
      description: |
        URL this webhook will send events to
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit_webhook"
    values={[
        { label: 'edit_webhook', value: 'edit_webhook' }
    ]}
>
<TabItem value="edit_webhook">

Edits the webhook details for the given webhook ID.

```sql
UPDATE cloudflare.realtime_kit.webhooks
SET 
enabled = {{ enabled }},
events = '{{ events }}',
name = '{{ name }}',
url = '{{ url }}'
WHERE 
account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
AND webhook_id = '{{ webhook_id }}' --required
RETURNING
data,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace_webhook"
    values={[
        { label: 'replace_webhook', value: 'replace_webhook' }
    ]}
>
<TabItem value="replace_webhook">

Replace all details for the given webhook ID.

```sql
REPLACE cloudflare.realtime_kit.webhooks
SET 
enabled = {{ enabled }},
events = '{{ events }}',
name = '{{ name }}',
url = '{{ url }}'
WHERE 
account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
AND webhook_id = '{{ webhook_id }}' --required
AND name = '{{ name }}' --required
AND url = '{{ url }}' --required
AND events = '{{ events }}' --required
RETURNING
data,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_webhook"
    values={[
        { label: 'delete_webhook', value: 'delete_webhook' }
    ]}
>
<TabItem value="delete_webhook">

Removes a webhook for the given webhook ID.

```sql
DELETE FROM cloudflare.realtime_kit.webhooks
WHERE account_id = '{{ account_id }}' --required
AND app_id = '{{ app_id }}' --required
AND webhook_id = '{{ webhook_id }}' --required
;
```
</TabItem>
</Tabs>
