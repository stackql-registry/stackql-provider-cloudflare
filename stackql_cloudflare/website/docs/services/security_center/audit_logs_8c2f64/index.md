--- 
title: audit_logs_8c2f64
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_logs_8c2f64
  - security_center
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

Creates, updates, deletes, gets or lists an <code>audit_logs_8c2f64</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="audit_logs_8c2f64" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.security_center.audit_logs_8c2f64" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

The request was successful.

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
    <td>UUIDv7 identifier for the audit log entry, time-ordered.</td>
</tr>
<tr>
    <td><CopyableCode code="issue_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the insight this audit log entry relates to.</td>
</tr>
<tr>
    <td><CopyableCode code="zone_id" /></td>
    <td><code>integer (int64)</code></td>
    <td>The zone ID associated with the insight. Only present for zone-level insights.</td>
</tr>
<tr>
    <td><CopyableCode code="changed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the change occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="changed_by" /></td>
    <td><code>string</code></td>
    <td>The actor that made the change. 'system' for automated changes, or a user identifier. (example: system)</td>
</tr>
<tr>
    <td><CopyableCode code="current_value" /></td>
    <td><code>string</code></td>
    <td>The value of the field after the change. Null if the field was cleared.</td>
</tr>
<tr>
    <td><CopyableCode code="field_changed" /></td>
    <td><code>string</code></td>
    <td>The field that was changed. (status, user_classification)</td>
</tr>
<tr>
    <td><CopyableCode code="previous_value" /></td>
    <td><code>string</code></td>
    <td>The value of the field before the change. Null if the field was not previously set.</td>
</tr>
<tr>
    <td><CopyableCode code="rationale" /></td>
    <td><code>string</code></td>
    <td>Optional rationale provided for the change.</td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-issue_id"><code>issue_id</code></a></td>
    <td><a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-field_changed"><code>field_changed</code></a>, <a href="#parameter-changed_by"><code>changed_by</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>Lists audit log entries for a specific Security Center insight, showing changes to its status and classification over time.</td>
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
<tr id="parameter-issue_id">
    <td><CopyableCode code="issue_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filter entries changed before this timestamp (RFC 3339).</td>
</tr>
<tr id="parameter-changed_by">
    <td><CopyableCode code="changed_by" /></td>
    <td><code>string</code></td>
    <td>Filter by the actor that made the change.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Opaque cursor for pagination. Use the cursor value from result_info of the previous response.</td>
</tr>
<tr id="parameter-field_changed">
    <td><CopyableCode code="field_changed" /></td>
    <td><code>string</code></td>
    <td>Filter by the field that was changed.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order for results. Use 'asc' for oldest first or 'desc' for newest first.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of results per page.</td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filter entries changed at or after this timestamp (RFC 3339).</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

Lists audit log entries for a specific Security Center insight, showing changes to its status and classification over time.

```sql
SELECT
id,
issue_id,
zone_id,
changed_at,
changed_by,
current_value,
field_changed,
previous_value,
rationale
FROM cloudflare.security_center.audit_logs_8c2f64
WHERE account_id = '{{ account_id }}' -- required
AND issue_id = '{{ issue_id }}' -- required
AND per_page = '{{ per_page }}'
AND cursor = '{{ cursor }}'
AND field_changed = '{{ field_changed }}'
AND changed_by = '{{ changed_by }}'
AND since = '{{ since }}'
AND before = '{{ before }}'
AND order = '{{ order }}'
;
```
</TabItem>
</Tabs>
