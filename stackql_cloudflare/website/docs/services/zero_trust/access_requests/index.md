--- 
title: access_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - access_requests
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

Creates, updates, deletes, gets or lists an <code>access_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.access_requests" /></td></tr>
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

Get Access authentication logs response

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
    <td><CopyableCode code="ray_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the request to Cloudflare. (example: 187d944c61940c77)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>The event that occurred, such as a login attempt. (example: login)</td>
</tr>
<tr>
    <td><CopyableCode code="allowed" /></td>
    <td><code>boolean</code></td>
    <td>The result of the authentication event.</td>
</tr>
<tr>
    <td><CopyableCode code="app_domain" /></td>
    <td><code>string</code></td>
    <td>The URL of the Access application. (example: test.example.com/admin)</td>
</tr>
<tr>
    <td><CopyableCode code="app_uid" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the Access application. (example: df7e2w5f-02b7-4d9d-af26-8d1988fca630)</td>
</tr>
<tr>
    <td><CopyableCode code="connection" /></td>
    <td><code>string</code></td>
    <td>The IdP used to authenticate. (example: saml)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="ip_address" /></td>
    <td><code>string</code></td>
    <td>The IP address of the authenticating user. (example: 198.41.129.166)</td>
</tr>
<tr>
    <td><CopyableCode code="user_email" /></td>
    <td><code>string (email)</code></td>
    <td>The email address of the authenticating user. (example: user@example.com)</td>
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
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-since"><code>since</code></a>, <a href="#parameter-until"><code>until</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-email"><code>email</code></a>, <a href="#parameter-email_exact"><code>email_exact</code></a>, <a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-allowedOp"><code>allowedOp</code></a>, <a href="#parameter-country_codeOp"><code>country_codeOp</code></a>, <a href="#parameter-app_typeOp"><code>app_typeOp</code></a>, <a href="#parameter-app_uidOp"><code>app_uidOp</code></a>, <a href="#parameter-ray_idOp"><code>ray_idOp</code></a>, <a href="#parameter-emailOp"><code>emailOp</code></a>, <a href="#parameter-idpOp"><code>idpOp</code></a>, <a href="#parameter-non_identityOp"><code>non_identityOp</code></a>, <a href="#parameter-user_idOp"><code>user_idOp</code></a>, <a href="#parameter-fields"><code>fields</code></a></td>
    <td>Gets a list of Access authentication audit logs for an account.</td>
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
<tr id="parameter-allowedOp">
    <td><CopyableCode code="allowedOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `allowed` filter.</td>
</tr>
<tr id="parameter-app_typeOp">
    <td><CopyableCode code="app_typeOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `app_type` filter.</td>
</tr>
<tr id="parameter-app_uidOp">
    <td><CopyableCode code="app_uidOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `app_uid` filter.</td>
</tr>
<tr id="parameter-country_codeOp">
    <td><CopyableCode code="country_codeOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `country_code` filter.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>The chronological sorting order for the logs.</td>
</tr>
<tr id="parameter-email">
    <td><CopyableCode code="email" /></td>
    <td><code>string (email)</code></td>
    <td>Filter by user email. Defaults to substring matching. To force exact matching, set `email_exact=true`. Example (default): `email=@example.com` returns all events with that domain. Example (exact): `email=user@example.com&email_exact=true` returns only that user.</td>
</tr>
<tr id="parameter-emailOp">
    <td><CopyableCode code="emailOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `email` filter.</td>
</tr>
<tr id="parameter-email_exact">
    <td><CopyableCode code="email_exact" /></td>
    <td><code>boolean</code></td>
    <td>When true, `email` is matched exactly instead of substring matching.</td>
</tr>
<tr id="parameter-fields">
    <td><CopyableCode code="fields" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of fields to include in the response. When omitted, all fields are returned.</td>
</tr>
<tr id="parameter-idpOp">
    <td><CopyableCode code="idpOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `idp` filter.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of log entries to retrieve.</td>
</tr>
<tr id="parameter-non_identityOp">
    <td><CopyableCode code="non_identityOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `non_identity` filter.</td>
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
<tr id="parameter-ray_idOp">
    <td><CopyableCode code="ray_idOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `ray_id` filter.</td>
</tr>
<tr id="parameter-since">
    <td><CopyableCode code="since" /></td>
    <td><code>string (date-time)</code></td>
    <td>The earliest event timestamp to query.</td>
</tr>
<tr id="parameter-until">
    <td><CopyableCode code="until" /></td>
    <td><code>string (date-time)</code></td>
    <td>The latest event timestamp to query.</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Filter by user UUID.</td>
</tr>
<tr id="parameter-user_idOp">
    <td><CopyableCode code="user_idOp" /></td>
    <td><code>string</code></td>
    <td>Operator for the `user_id` filter.</td>
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

Gets a list of Access authentication audit logs for an account.

```sql
SELECT
ray_id,
action,
allowed,
app_domain,
app_uid,
connection,
created_at,
ip_address,
user_email
FROM cloudflare.zero_trust.access_requests
WHERE account_id = '{{ account_id }}' -- required
AND limit = '{{ limit }}'
AND direction = '{{ direction }}'
AND since = '{{ since }}'
AND until = '{{ until }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND email = '{{ email }}'
AND email_exact = '{{ email_exact }}'
AND user_id = '{{ user_id }}'
AND allowedOp = '{{ allowedOp }}'
AND country_codeOp = '{{ country_codeOp }}'
AND app_typeOp = '{{ app_typeOp }}'
AND app_uidOp = '{{ app_uidOp }}'
AND ray_idOp = '{{ ray_idOp }}'
AND emailOp = '{{ emailOp }}'
AND idpOp = '{{ idpOp }}'
AND non_identityOp = '{{ non_identityOp }}'
AND user_idOp = '{{ user_idOp }}'
AND fields = '{{ fields }}'
;
```
</TabItem>
</Tabs>
