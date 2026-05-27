--- 
title: update_status
hide_title: false
hide_table_of_contents: false
keywords:
  - update_status
  - registrar
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

Creates, updates, deletes, gets or lists a <code>update_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="update_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.registrar.update_status" /></td></tr>
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

Update workflow status.

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
    <td><CopyableCode code="completed" /></td>
    <td><code>boolean</code></td>
    <td>Whether the workflow has reached a terminal state. `true` when `state` is `succeeded` or `failed`. `false` for `pending`, `in_progress`, `action_required`, and `blocked`.</td>
</tr>
<tr>
    <td><CopyableCode code="context" /></td>
    <td><code>object</code></td>
    <td>Workflow-specific data for this workflow. The workflow subject is identified by `context.domain_name` for domain-centric workflows.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error details when a workflow reaches the `failed` state. The specific error codes and messages depend on the workflow type (registration, update, etc.) and the underlying registry response. These workflow error codes are separate from immediate HTTP error `errors[].code` values returned by non-2xx responses. Surface `error.message` to the user for context.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Workflow lifecycle state. - `pending`: Workflow has been created but not yet started processing. - `in_progress`: Actively processing. Continue polling `links.self`. The workflow has an internal deadline and will not remain in this state indefinitely. - `action_required`: Paused — requires action by the user (not the system). See `context.action` for what is needed. An automated polling loop must break on this state; it will not resolve on its own without user intervention. - `blocked`: The workflow cannot make progress due to a third party such as the domain extension's registry or a losing registrar. No user action will help. Continue polling — the block may resolve when the third party responds. - `succeeded`: Terminal. The operation completed successfully. `completed` will be `true`. For registrations, `context.registration` contains the resulting registration resource. - `failed`: Terminal. The operation failed. `completed` will be `true`. See `error.code` and `error.message` for the reason. Do not auto-retry without user review. (pending, in_progress, action_required, blocked, succeeded, failed) (example: in_progress)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a></td>
    <td></td>
    <td>Returns the current status of a domain update workflow. Use this endpoint to poll for completion when the PATCH response returned `202 Accepted`. The URL is provided in the `links.self` field of the workflow status response. Poll this endpoint until the workflow reaches a terminal state or a state that requires user attention. Use increasing backoff between polls. When the workflow remains blocked on a third party, use a longer polling interval and do not poll indefinitely.</td>
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
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td></td>
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

Returns the current status of a domain update workflow. Use this endpoint to poll for completion when the PATCH response returned `202 Accepted`. The URL is provided in the `links.self` field of the workflow status response. Poll this endpoint until the workflow reaches a terminal state or a state that requires user attention. Use increasing backoff between polls. When the workflow remains blocked on a third party, use a longer polling interval and do not poll indefinitely.

```sql
SELECT
completed,
context,
created_at,
error,
links,
state,
updated_at
FROM cloudflare.registrar.update_status
WHERE account_id = '{{ account_id }}' -- required
AND domain_name = '{{ domain_name }}' -- required
;
```
</TabItem>
</Tabs>
