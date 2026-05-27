--- 
title: registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations
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

Creates, updates, deletes, gets or lists a <code>registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.registrations" /></td></tr>
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

Returns a Registration.

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
    <td>The ID of the registration. (example: 11ffb86f-3f0c-4306-b4a2-e62f872b166a)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was created. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was deleted. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="device" /></td>
    <td><code>object</code></td>
    <td>Device details embedded inside of a registration.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The public key used to connect to the Cloudflare network. (example: U+QTP50RsWfeLGHF4tlGDnmGeuwtsz46KCHr5OyhWq00Rsdfl45mgnQAuEJ6CO0YrkyTl9FUf5iB0bwYR3g4EEFEHhtu6jFaqfMrBMBSz6itv9HQXkaR9OieKQ==)</td>
</tr>
<tr>
    <td><CopyableCode code="key_type" /></td>
    <td><code>string</code></td>
    <td>The type of encryption key used by the WARP client for the active key. Currently 'curve25519' for WireGuard and 'secp256r1' for MASQUE. (example: secp256r1)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was last seen. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policy" /></td>
    <td><code>object</code></td>
    <td>The device settings profile assigned to this registration.</td>
</tr>
<tr>
    <td><CopyableCode code="revoked_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was revoked. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_type" /></td>
    <td><code>string</code></td>
    <td>Type of the tunnel - wireguard or masque. (example: masque)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was last updated. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of registrations response.

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
    <td>The ID of the registration. (example: 11ffb86f-3f0c-4306-b4a2-e62f872b166a)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was created. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was deleted. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="device" /></td>
    <td><code>object</code></td>
    <td>Device details embedded inside of a registration.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>The public key used to connect to the Cloudflare network. (example: U+QTP50RsWfeLGHF4tlGDnmGeuwtsz46KCHr5OyhWq00Rsdfl45mgnQAuEJ6CO0YrkyTl9FUf5iB0bwYR3g4EEFEHhtu6jFaqfMrBMBSz6itv9HQXkaR9OieKQ==)</td>
</tr>
<tr>
    <td><CopyableCode code="key_type" /></td>
    <td><code>string</code></td>
    <td>The type of encryption key used by the WARP client for the active key. Currently 'curve25519' for WireGuard and 'secp256r1' for MASQUE. (example: secp256r1)</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was last seen. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policy" /></td>
    <td><code>object</code></td>
    <td>The device settings profile assigned to this registration.</td>
</tr>
<tr>
    <td><CopyableCode code="revoked_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was revoked. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_type" /></td>
    <td><code>string</code></td>
    <td>Type of the tunnel - wireguard or masque. (example: masque)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339 timestamp when the registration was last updated. (example: 2025-02-14T13:17:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="user" /></td>
    <td><code>object</code></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-registration_id"><code>registration_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-include"><code>include</code></a></td>
    <td>Fetches a single WARP registration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-user.id"><code>user.id</code></a>, <a href="#parameter-seen_after"><code>seen_after</code></a>, <a href="#parameter-seen_before"><code>seen_before</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a>, <a href="#parameter-sort_order"><code>sort_order</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-device.id"><code>device.id</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td>Lists WARP registrations.</td>
</tr>
<tr>
    <td><a href="#unrevoke"><CopyableCode code="unrevoke" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a></td>
    <td>Unrevokes a list of WARP registrations.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-registration_id"><code>registration_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a WARP registration.</td>
</tr>
<tr>
    <td><a href="#bulk_delete"><CopyableCode code="bulk_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a></td>
    <td>Deletes a list of WARP registrations.</td>
</tr>
<tr>
    <td><a href="#revoke"><CopyableCode code="revoke" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-id"><code>id</code></a></td>
    <td>Revokes a list of WARP registrations.</td>
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
<tr id="parameter-registration_id">
    <td><CopyableCode code="registration_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Opaque token indicating the starting position when requesting the next set of records. A cursor value can be obtained from the result_info.cursor field in the response.</td>
</tr>
<tr id="parameter-device.id">
    <td><CopyableCode code="device.id" /></td>
    <td><code>string</code></td>
    <td>Filter by WARP device ID.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>array</code></td>
    <td>A list of registration IDs to revoke.</td>
</tr>
<tr id="parameter-include">
    <td><CopyableCode code="include" /></td>
    <td><code>string</code></td>
    <td>Comma-separated list of additional information that should be included in the registration response. Supported values are: "policy".</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer (uint64)</code></td>
    <td>The maximum number of devices to return in a single response.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Filter by registration details.</td>
</tr>
<tr id="parameter-seen_after">
    <td><CopyableCode code="seen_after" /></td>
    <td><code>string</code></td>
    <td>Filter by the last_seen timestamp - returns only registrations last seen after this timestamp.</td>
</tr>
<tr id="parameter-seen_before">
    <td><CopyableCode code="seen_before" /></td>
    <td><code>string</code></td>
    <td>Filter by the last_seen timestamp - returns only registrations last seen before this timestamp.</td>
</tr>
<tr id="parameter-sort_by">
    <td><CopyableCode code="sort_by" /></td>
    <td><code>string</code></td>
    <td>The registration field to order results by.</td>
</tr>
<tr id="parameter-sort_order">
    <td><CopyableCode code="sort_order" /></td>
    <td><code>string</code></td>
    <td>Sort direction.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter by registration status. Defaults to 'active'.</td>
</tr>
<tr id="parameter-user.id">
    <td><CopyableCode code="user.id" /></td>
    <td><code>array</code></td>
    <td>Filter by user ID.</td>
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

Fetches a single WARP registration.

```sql
SELECT
id,
created_at,
deleted_at,
device,
key,
key_type,
last_seen_at,
policy,
revoked_at,
tunnel_type,
updated_at,
user
FROM cloudflare.zero_trust.registrations
WHERE registration_id = '{{ registration_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND include = '{{ include }}'
;
```
</TabItem>
<TabItem value="list">

Lists WARP registrations.

```sql
SELECT
id,
created_at,
deleted_at,
device,
key,
key_type,
last_seen_at,
policy,
revoked_at,
tunnel_type,
updated_at,
user
FROM cloudflare.zero_trust.registrations
WHERE account_id = '{{ account_id }}' -- required
AND user.id = '{{ user.id }}'
AND seen_after = '{{ seen_after }}'
AND seen_before = '{{ seen_before }}'
AND status = '{{ status }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
AND sort_by = '{{ sort_by }}'
AND sort_order = '{{ sort_order }}'
AND cursor = '{{ cursor }}'
AND id = '{{ id }}'
AND device.id = '{{ device.id }}'
AND include = '{{ include }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="unrevoke"
    values={[
        { label: 'unrevoke', value: 'unrevoke' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="unrevoke">

Unrevokes a list of WARP registrations.

```sql
INSERT INTO cloudflare.zero_trust.registrations (
account_id,
id
)
SELECT 
'{{ account_id }}',
'{{ id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: registrations
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the registrations resource.
    - name: id
      value: "{{ id }}"
      description: A list of registration IDs to unrevoke.
      description: A list of registration IDs to unrevoke.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'bulk_delete', value: 'bulk_delete' }
    ]}
>
<TabItem value="delete">

Deletes a WARP registration.

```sql
DELETE FROM cloudflare.zero_trust.registrations
WHERE registration_id = '{{ registration_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="bulk_delete">

Deletes a list of WARP registrations.

```sql
DELETE FROM cloudflare.zero_trust.registrations
WHERE account_id = '{{ account_id }}' --required
AND id = '{{ id }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoke"
    values={[
        { label: 'revoke', value: 'revoke' }
    ]}
>
<TabItem value="revoke">

Revokes a list of WARP registrations.

```sql
EXEC cloudflare.zero_trust.registrations.revoke 
@account_id='{{ account_id }}' --required, 
@id='{{ id }}'
;
```
</TabItem>
</Tabs>
