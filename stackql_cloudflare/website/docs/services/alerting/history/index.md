--- 
title: history
hide_title: false
hide_table_of_contents: false
keywords:
  - history
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

Creates, updates, deletes, gets or lists a <code>history</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="history" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.alerting.history" /></td></tr>
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

List History response

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
    <td>UUID (example: f174e90afafe4643bbbc4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the policy. (example: SSL Notification Event Policy)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of a notification policy (example: 0da2b59ef118439d8097bdfb215203c9)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_body" /></td>
    <td><code>string</code></td>
    <td>Message body included in the notification sent. (example: SSL certificate has expired)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_type" /></td>
    <td><code>string</code></td>
    <td>Type of notification that has been dispatched. (example: universal_ssl_event_type)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the notification policy (if present). (example: Universal Certificate validation status, issuance, renewal, and expiration notices)</td>
</tr>
<tr>
    <td><CopyableCode code="mechanism" /></td>
    <td><code>string</code></td>
    <td>The mechanism to which the notification has been dispatched. (example: test@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="mechanism_type" /></td>
    <td><code>string</code></td>
    <td>The type of mechanism to which the notification has been dispatched. This can be email/pagerduty/webhook based on the mechanism configured. (email, pagerduty, webhook) (example: email)</td>
</tr>
<tr>
    <td><CopyableCode code="sent" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the notification was dispatched in ISO 8601 format. (example: 2021-10-08T17:52:17.571336Z)</td>
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
    <td><a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-since"><code>since</code></a></td>
    <td>Gets a list of history records for notifications sent to an account. The records are displayed for last `x` number of days based on the zone plan (free = 30, pro = 30, biz = 30, ent = 90).</td>
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
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string (date-time)</code></td>
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
    <td><code>string (date-time)</code></td>
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

Gets a list of history records for notifications sent to an account. The records are displayed for last `x` number of days based on the zone plan (free = 30, pro = 30, biz = 30, ent = 90).

```sql
SELECT
id,
name,
policy_id,
alert_body,
alert_type,
description,
mechanism,
mechanism_type,
sent
FROM cloudflare.alerting.history
WHERE account_id = '{{ account_id }}' -- required
AND per_page = '{{ per_page }}'
AND before = '{{ before }}'
AND page = '{{ page }}'
AND since = '{{ since }}'
;
```
</TabItem>
</Tabs>
