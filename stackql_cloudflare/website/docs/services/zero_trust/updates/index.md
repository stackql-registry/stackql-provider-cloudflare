--- 
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="updates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.updates" /></td></tr>
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

Get Access SCIM update logs response

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
    <td><CopyableCode code="cf_resource_id" /></td>
    <td><code>string</code></td>
    <td>The unique Cloudflare-generated Id of the SCIM resource. (example: bd97ef8d-7986-43e3-9ee0-c25dda33e4b0)</td>
</tr>
<tr>
    <td><CopyableCode code="idp_id" /></td>
    <td><code>string</code></td>
    <td>The unique Id of the IdP that has SCIM enabled. (example: df7e2w5f-02b7-4d9d-af26-8d1988fca630)</td>
</tr>
<tr>
    <td><CopyableCode code="idp_resource_id" /></td>
    <td><code>string</code></td>
    <td>The IdP-generated Id of the SCIM resource. (example: all_employees)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The display name of the SCIM Group resource if it exists. (example: ALL_EMPLOYEES)</td>
</tr>
<tr>
    <td><CopyableCode code="error_description" /></td>
    <td><code>string</code></td>
    <td>The error message which is generated when the status of the SCIM request is 'FAILURE'. (example: Invalid JSON body)</td>
</tr>
<tr>
    <td><CopyableCode code="logged_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="request_body" /></td>
    <td><code>string</code></td>
    <td>The JSON-encoded string body of the SCIM request. (example: &#123;&#125;&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="request_method" /></td>
    <td><code>string</code></td>
    <td>The request method of the SCIM request. (example: DELETE)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The resource type of the SCIM request. (example: GROUP)</td>
</tr>
<tr>
    <td><CopyableCode code="resource_user_email" /></td>
    <td><code>string (email)</code></td>
    <td>The email address of the SCIM User resource if it exists. (example: john.smith@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the SCIM request. (example: FAILURE)</td>
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
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-until"><code>until</code></a>, <a href="#parameter-idp_id"><code>idp_id</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-request_method"><code>request_method</code></a>, <a href="#parameter-resource_user_email"><code>resource_user_email</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cf_resource_id"><code>cf_resource_id</code></a>, <a href="#parameter-idp_resource_id"><code>idp_resource_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists Access SCIM update logs that maintain a record of updates made to User and Group resources synced to Cloudflare via the System for Cross-domain Identity Management (SCIM).</td>
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
<tr id="parameter-cf_resource_id">
    <td><CopyableCode code="cf_resource_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-idp_id">
    <td><CopyableCode code="idp_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-idp_resource_id">
    <td><CopyableCode code="idp_resource_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-request_method">
    <td><CopyableCode code="request_method" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_user_email">
    <td><CopyableCode code="resource_user_email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
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

Lists Access SCIM update logs that maintain a record of updates made to User and Group resources synced to Cloudflare via the System for Cross-domain Identity Management (SCIM).

```sql
SELECT
cf_resource_id,
idp_id,
idp_resource_id,
resource_group_name,
error_description,
logged_at,
request_body,
request_method,
resource_type,
resource_user_email,
status
FROM cloudflare.zero_trust.updates
WHERE account_id = '{{ account_id }}' -- required
AND limit = '{{ limit }}'
AND direction = '{{ direction }}'
AND since = '{{ since }}'
AND until = '{{ until }}'
AND idp_id = '{{ idp_id }}'
AND status = '{{ status }}'
AND resource_type = '{{ resource_type }}'
AND request_method = '{{ request_method }}'
AND resource_user_email = '{{ resource_user_email }}'
AND resource_group_name = '{{ resource_group_name }}'
AND cf_resource_id = '{{ cf_resource_id }}'
AND idp_resource_id = '{{ idp_resource_id }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>
