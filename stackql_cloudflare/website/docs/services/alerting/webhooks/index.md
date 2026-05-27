--- 
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
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

Creates, updates, deletes, gets or lists a <code>webhooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="webhooks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.alerting.webhooks" /></td></tr>
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

Get a webhook response

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
    <td>The unique identifier of a webhook (example: b115d5ec15c641ee8b7692c449b5227b)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the webhook destination. This will be included in the request body when you receive a webhook notification. (example: Slack Webhook)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the webhook destination was created. (example: 2020-10-26T18:25:04.532316Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_failure" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last time an attempt to dispatch a notification to this webhook failed. (example: 2020-10-26T18:25:04.532316Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_success" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last time Cloudflare was able to successfully dispatch a notification using this webhook. (example: 2020-10-26T18:25:04.532316Z)</td>
</tr>
<tr>
    <td><CopyableCode code="secret" /></td>
    <td><code>string</code></td>
    <td>Optional secret that will be passed in the `cf-webhook-auth` header when dispatching generic webhook notifications or formatted for supported destinations. Secrets are not returned in any API response body.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of webhook endpoint. (datadog, discord, feishu, gchat, generic, opsgenie, slack, splunk) (example: slack)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The POST endpoint to call when dispatching a notification. (example: https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List webhooks response

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
    <td>The unique identifier of a webhook (example: b115d5ec15c641ee8b7692c449b5227b)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the webhook destination. This will be included in the request body when you receive a webhook notification. (example: Slack Webhook)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the webhook destination was created. (example: 2020-10-26T18:25:04.532316Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_failure" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last time an attempt to dispatch a notification to this webhook failed. (example: 2020-10-26T18:25:04.532316Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_success" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the last time Cloudflare was able to successfully dispatch a notification using this webhook. (example: 2020-10-26T18:25:04.532316Z)</td>
</tr>
<tr>
    <td><CopyableCode code="secret" /></td>
    <td><code>string</code></td>
    <td>Optional secret that will be passed in the `cf-webhook-auth` header when dispatching generic webhook notifications or formatted for supported destinations. Secrets are not returned in any API response body.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of webhook endpoint. (datadog, discord, feishu, gchat, generic, opsgenie, slack, splunk) (example: slack)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The POST endpoint to call when dispatching a notification. (example: https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-webhook_id"><code>webhook_id</code></a></td>
    <td></td>
    <td>Get details for a single webhooks destination.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets a list of all configured webhook destinations.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Creates a new webhook destination.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-webhook_id"><code>webhook_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Update a webhook destination.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-webhook_id"><code>webhook_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured webhook destination.</td>
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
<tr id="parameter-webhook_id">
    <td><CopyableCode code="webhook_id" /></td>
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

Get details for a single webhooks destination.

```sql
SELECT
id,
name,
created_at,
last_failure,
last_success,
secret,
type,
url
FROM cloudflare.alerting.webhooks
WHERE account_id = '{{ account_id }}' -- required
AND webhook_id = '{{ webhook_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of all configured webhook destinations.

```sql
SELECT
id,
name,
created_at,
last_failure,
last_success,
secret,
type,
url
FROM cloudflare.alerting.webhooks
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

Creates a new webhook destination.

```sql
INSERT INTO cloudflare.alerting.webhooks (
name,
secret,
url,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ secret }}',
'{{ url }}' /* required */,
'{{ account_id }}'
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
- name: webhooks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the webhooks resource.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the webhook destination. This will be included in the request body when you receive a webhook notification.
    - name: secret
      value: "{{ secret }}"
      description: |
        Optional secret that will be passed in the \`cf-webhook-auth\` header when dispatching generic webhook notifications or formatted for supported destinations. Secrets are not returned in any API response body.
    - name: url
      value: "{{ url }}"
      description: |
        The POST endpoint to call when dispatching a notification.
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

Update a webhook destination.

```sql
REPLACE cloudflare.alerting.webhooks
SET 
name = '{{ name }}',
secret = '{{ secret }}',
url = '{{ url }}'
WHERE 
webhook_id = '{{ webhook_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND url = '{{ url }}' --required
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

Delete a configured webhook destination.

```sql
DELETE FROM cloudflare.alerting.webhooks
WHERE webhook_id = '{{ webhook_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
