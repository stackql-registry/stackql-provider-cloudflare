--- 
title: audit
hide_title: false
hide_table_of_contents: false
keywords:
  - audit
  - accounts
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

Creates, updates, deletes, gets or lists an <code>audit</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="audit" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.accounts.audit" /></td></tr>
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

Get account audit logs successful response

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
    <td>A unique identifier for the audit log entry. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="account" /></td>
    <td><code>object</code></td>
    <td>Contains account related information.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>Provides information about the action performed.</td>
</tr>
<tr>
    <td><CopyableCode code="actor" /></td>
    <td><code>object</code></td>
    <td>Provides details about the actor who performed the action.</td>
</tr>
<tr>
    <td><CopyableCode code="raw" /></td>
    <td><code>object</code></td>
    <td>Provides raw information about the request and response.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code>object</code></td>
    <td>Provides details about the affected resource.</td>
</tr>
<tr>
    <td><CopyableCode code="zone" /></td>
    <td><code>object</code></td>
    <td>Provides details about the zone affected by the action.</td>
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
    <td><a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-action_result"><code>action_result</code></a>, <a href="#parameter-action_type"><code>action_type</code></a>, <a href="#parameter-actor_context"><code>actor_context</code></a>, <a href="#parameter-actor_email"><code>actor_email</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a>, <a href="#parameter-actor_ip_address"><code>actor_ip_address</code></a>, <a href="#parameter-actor_token_id"><code>actor_token_id</code></a>, <a href="#parameter-actor_token_name"><code>actor_token_name</code></a>, <a href="#parameter-actor_type"><code>actor_type</code></a>, <a href="#parameter-audit_log_id"><code>audit_log_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-raw_cf_ray_id"><code>raw_cf_ray_id</code></a>, <a href="#parameter-raw_method"><code>raw_method</code></a>, <a href="#parameter-raw_status_code"><code>raw_status_code</code></a>, <a href="#parameter-raw_uri"><code>raw_uri</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-resource_product"><code>resource_product</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_scope"><code>resource_scope</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-account_name.not"><code>account_name.not</code></a>, <a href="#parameter-action_result.not"><code>action_result.not</code></a>, <a href="#parameter-action_type.not"><code>action_type.not</code></a>, <a href="#parameter-actor_context.not"><code>actor_context.not</code></a>, <a href="#parameter-actor_email.not"><code>actor_email.not</code></a>, <a href="#parameter-actor_id.not"><code>actor_id.not</code></a>, <a href="#parameter-actor_ip_address.not"><code>actor_ip_address.not</code></a>, <a href="#parameter-actor_token_id.not"><code>actor_token_id.not</code></a>, <a href="#parameter-actor_token_name.not"><code>actor_token_name.not</code></a>, <a href="#parameter-actor_type.not"><code>actor_type.not</code></a>, <a href="#parameter-audit_log_id.not"><code>audit_log_id.not</code></a>, <a href="#parameter-id.not"><code>id.not</code></a>, <a href="#parameter-raw_cf_ray_id.not"><code>raw_cf_ray_id.not</code></a>, <a href="#parameter-raw_method.not"><code>raw_method.not</code></a>, <a href="#parameter-raw_status_code.not"><code>raw_status_code.not</code></a>, <a href="#parameter-raw_uri.not"><code>raw_uri.not</code></a>, <a href="#parameter-resource_id.not"><code>resource_id.not</code></a>, <a href="#parameter-resource_product.not"><code>resource_product.not</code></a>, <a href="#parameter-resource_type.not"><code>resource_type.not</code></a>, <a href="#parameter-resource_scope.not"><code>resource_scope.not</code></a>, <a href="#parameter-zone_id.not"><code>zone_id.not</code></a>, <a href="#parameter-zone_name.not"><code>zone_name.not</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-cursor"><code>cursor</code></a></td>
    <td>Gets a list of audit logs for an account.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-account_name.not">
    <td><CopyableCode code="account_name.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-action_result">
    <td><CopyableCode code="action_result" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-action_result.not">
    <td><CopyableCode code="action_result.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-action_type">
    <td><CopyableCode code="action_type" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-action_type.not">
    <td><CopyableCode code="action_type.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_context">
    <td><CopyableCode code="actor_context" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_context.not">
    <td><CopyableCode code="actor_context.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_email">
    <td><CopyableCode code="actor_email" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_email.not">
    <td><CopyableCode code="actor_email.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_id">
    <td><CopyableCode code="actor_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_id.not">
    <td><CopyableCode code="actor_id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_ip_address">
    <td><CopyableCode code="actor_ip_address" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_ip_address.not">
    <td><CopyableCode code="actor_ip_address.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_token_id">
    <td><CopyableCode code="actor_token_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_token_id.not">
    <td><CopyableCode code="actor_token_id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_token_name">
    <td><CopyableCode code="actor_token_name" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_token_name.not">
    <td><CopyableCode code="actor_token_name.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_type">
    <td><CopyableCode code="actor_type" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-actor_type.not">
    <td><CopyableCode code="actor_type.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-audit_log_id">
    <td><CopyableCode code="audit_log_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-audit_log_id.not">
    <td><CopyableCode code="audit_log_id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string (date)</code></td>
    <td>Limits the returned results to logs older than the specified date. This can be a date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that conforms to RFC3339.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-id.not">
    <td><CopyableCode code="id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_cf_ray_id">
    <td><CopyableCode code="raw_cf_ray_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_cf_ray_id.not">
    <td><CopyableCode code="raw_cf_ray_id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_method">
    <td><CopyableCode code="raw_method" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_method.not">
    <td><CopyableCode code="raw_method.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_status_code">
    <td><CopyableCode code="raw_status_code" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_status_code.not">
    <td><CopyableCode code="raw_status_code.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_uri">
    <td><CopyableCode code="raw_uri" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-raw_uri.not">
    <td><CopyableCode code="raw_uri.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_id.not">
    <td><CopyableCode code="resource_id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_product">
    <td><CopyableCode code="resource_product" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_product.not">
    <td><CopyableCode code="resource_product.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_scope">
    <td><CopyableCode code="resource_scope" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_scope.not">
    <td><CopyableCode code="resource_scope.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_type.not">
    <td><CopyableCode code="resource_type.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date)</code></td>
    <td>Limits the returned results to logs newer than the specified date. This can be a date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that conforms to RFC3339.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id.not">
    <td><CopyableCode code="zone_id.not" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_name">
    <td><CopyableCode code="zone_name" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_name.not">
    <td><CopyableCode code="zone_name.not" /></td>
    <td><code>array</code></td>
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

Gets a list of audit logs for an account.

```sql
SELECT
id,
account,
action,
actor,
raw,
resource,
zone
FROM cloudflare.accounts.audit
WHERE account_id = '{{ account_id }}' -- required
AND account_name = '{{ account_name }}'
AND action_result = '{{ action_result }}'
AND action_type = '{{ action_type }}'
AND actor_context = '{{ actor_context }}'
AND actor_email = '{{ actor_email }}'
AND actor_id = '{{ actor_id }}'
AND actor_ip_address = '{{ actor_ip_address }}'
AND actor_token_id = '{{ actor_token_id }}'
AND actor_token_name = '{{ actor_token_name }}'
AND actor_type = '{{ actor_type }}'
AND audit_log_id = '{{ audit_log_id }}'
AND id = '{{ id }}'
AND raw_cf_ray_id = '{{ raw_cf_ray_id }}'
AND raw_method = '{{ raw_method }}'
AND raw_status_code = '{{ raw_status_code }}'
AND raw_uri = '{{ raw_uri }}'
AND resource_id = '{{ resource_id }}'
AND resource_product = '{{ resource_product }}'
AND resource_type = '{{ resource_type }}'
AND resource_scope = '{{ resource_scope }}'
AND zone_id = '{{ zone_id }}'
AND zone_name = '{{ zone_name }}'
AND account_name.not = '{{ account_name.not }}'
AND action_result.not = '{{ action_result.not }}'
AND action_type.not = '{{ action_type.not }}'
AND actor_context.not = '{{ actor_context.not }}'
AND actor_email.not = '{{ actor_email.not }}'
AND actor_id.not = '{{ actor_id.not }}'
AND actor_ip_address.not = '{{ actor_ip_address.not }}'
AND actor_token_id.not = '{{ actor_token_id.not }}'
AND actor_token_name.not = '{{ actor_token_name.not }}'
AND actor_type.not = '{{ actor_type.not }}'
AND audit_log_id.not = '{{ audit_log_id.not }}'
AND id.not = '{{ id.not }}'
AND raw_cf_ray_id.not = '{{ raw_cf_ray_id.not }}'
AND raw_method.not = '{{ raw_method.not }}'
AND raw_status_code.not = '{{ raw_status_code.not }}'
AND raw_uri.not = '{{ raw_uri.not }}'
AND resource_id.not = '{{ resource_id.not }}'
AND resource_product.not = '{{ resource_product.not }}'
AND resource_type.not = '{{ resource_type.not }}'
AND resource_scope.not = '{{ resource_scope.not }}'
AND zone_id.not = '{{ zone_id.not }}'
AND zone_name.not = '{{ zone_name.not }}'
AND since = '{{ since }}'
AND before = '{{ before }}'
AND direction = '{{ direction }}'
AND limit = '{{ limit }}'
AND cursor = '{{ cursor }}'
;
```
</TabItem>
</Tabs>
