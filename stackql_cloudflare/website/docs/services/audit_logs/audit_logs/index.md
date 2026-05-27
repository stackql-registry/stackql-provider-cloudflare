--- 
title: audit_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_logs
  - audit_logs
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

Creates, updates, deletes, gets or lists an <code>audit_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="audit_logs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.audit_logs.audit_logs" /></td></tr>
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

Get account audit logs response

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
    <td>A string that uniquely identifies the audit log. (example: d5b0f326-1232-4452-8858-1089bd7168ef)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="actor" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="interface" /></td>
    <td><code>string</code></td>
    <td>The source of the event. (example: API)</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>An object which can lend more context to the action being logged. This is a flexible value and varies between different actions.</td>
</tr>
<tr>
    <td><CopyableCode code="newValue" /></td>
    <td><code>string</code></td>
    <td>The new value of the resource that was modified. (example: low)</td>
</tr>
<tr>
    <td><CopyableCode code="oldValue" /></td>
    <td><code>string</code></td>
    <td>The value of the resource before it was modified. (example: high)</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="when" /></td>
    <td><code>string (date-time)</code></td>
    <td>A UTC RFC3339 timestamp that specifies when the action being logged occured. (example: 2017-04-26T17:31:07Z)</td>
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-export"><code>export</code></a>, <a href="#parameter-action.type"><code>action.type</code></a>, <a href="#parameter-actor.ip"><code>actor.ip</code></a>, <a href="#parameter-actor.email"><code>actor.email</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-zone.name"><code>zone.name</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-hide_user_logs"><code>hide_user_logs</code></a></td>
    <td>Gets a list of audit logs for an account. Can be filtered by who made the change, on which zone, and the timeframe of the change.</td>
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
<tr id="parameter-action.type">
    <td><CopyableCode code="action.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-actor.email">
    <td><CopyableCode code="actor.email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr id="parameter-actor.ip">
    <td><CopyableCode code="actor.ip" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string (date)</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-export">
    <td><CopyableCode code="export" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-hide_user_logs">
    <td><CopyableCode code="hide_user_logs" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date)</code></td>
    <td></td>
</tr>
<tr id="parameter-zone.name">
    <td><CopyableCode code="zone.name" /></td>
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

Gets a list of audit logs for an account. Can be filtered by who made the change, on which zone, and the timeframe of the change.

```sql
SELECT
id,
action,
actor,
interface,
metadata,
newValue,
oldValue,
owner,
resource,
when
FROM cloudflare.audit_logs.audit_logs
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}'
AND export = '{{ export }}'
AND action.type = '{{ action.type }}'
AND actor.ip = '{{ actor.ip }}'
AND actor.email = '{{ actor.email }}'
AND since = '{{ since }}'
AND before = '{{ before }}'
AND zone.name = '{{ zone.name }}'
AND direction = '{{ direction }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
AND hide_user_logs = '{{ hide_user_logs }}'
;
```
</TabItem>
</Tabs>
