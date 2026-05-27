--- 
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - zones
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

Creates, updates, deletes, gets or lists a <code>zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zones" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.zones" /></td></tr>
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

Zone Details response.

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The domain name. Per [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-2.3.4) the overall zone name can be up to 253 characters, with each segment ("label") not exceeding 63 characters. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="account" /></td>
    <td><code>object</code></td>
    <td>The account the zone belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="activated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time proof of ownership was detected and the zone was made active. (example: 2014-01-02T00:01:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="cname_suffix" /></td>
    <td><code>string</code></td>
    <td>Allows the customer to use a custom apex. *Tenants Only Configuration*. (example: cdn.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the zone was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="development_mode" /></td>
    <td><code>number</code></td>
    <td>The interval (in seconds) from when development mode expires (positive integer) or last expired (negative integer) for the domain. If development mode has never been enabled, this value is 0.</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Metadata about the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the zone was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="name_servers" /></td>
    <td><code>array</code></td>
    <td>The name servers Cloudflare assigns to a zone.</td>
</tr>
<tr>
    <td><CopyableCode code="original_dnshost" /></td>
    <td><code>string</code></td>
    <td>DNS host at the time of switching to Cloudflare. (example: NameCheap)</td>
</tr>
<tr>
    <td><CopyableCode code="original_name_servers" /></td>
    <td><code>array</code></td>
    <td>Original name servers before moving to Cloudflare.</td>
</tr>
<tr>
    <td><CopyableCode code="original_registrar" /></td>
    <td><code>string</code></td>
    <td>Registrar for the domain at the time of switching to Cloudflare. (example: GoDaddy)</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>object</code></td>
    <td>The owner of the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the zone is only using Cloudflare DNS services. A true value means the zone will not receive security or performance benefits.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>Legacy permissions based on legacy user membership information. (x-stainless-deprecation-message: This has been replaced by Account memberships.)</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>A Zones subscription information. (x-stainless-deprecation-message: Please use the `/zones/&#123;zone_id&#125;/subscription` API<br />to update a zone's plan. Changing this value will create/cancel<br />associated subscriptions. To view available plans for this zone,<br />see [Zone Plans](https://developers.cloudflare.com/api/resources/zones/subresources/plans/).)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The zone status on Cloudflare. (initializing, pending, active, moved) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="tenant" /></td>
    <td><code>object</code></td>
    <td>The root organizational unit that this zone belongs to (such as a tenant or organization).</td>
</tr>
<tr>
    <td><CopyableCode code="tenant_unit" /></td>
    <td><code>object</code></td>
    <td>The immediate parent organizational unit that this zone belongs to (such as under a tenant or sub-organization).</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. (full, partial, secondary, internal) (default: full, example: full)</td>
</tr>
<tr>
    <td><CopyableCode code="vanity_name_servers" /></td>
    <td><code>array</code></td>
    <td>An array of domains used for custom name servers. This is only available for Business and Enterprise plans.</td>
</tr>
<tr>
    <td><CopyableCode code="verification_key" /></td>
    <td><code>string</code></td>
    <td>Verification key for partial zone setup. (example: 284344499-1084221259)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Zones response.

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The domain name. Per [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-2.3.4) the overall zone name can be up to 253 characters, with each segment ("label") not exceeding 63 characters. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="account" /></td>
    <td><code>object</code></td>
    <td>The account the zone belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="activated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time proof of ownership was detected and the zone was made active. (example: 2014-01-02T00:01:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="cname_suffix" /></td>
    <td><code>string</code></td>
    <td>Allows the customer to use a custom apex. *Tenants Only Configuration*. (example: cdn.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the zone was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="development_mode" /></td>
    <td><code>number</code></td>
    <td>The interval (in seconds) from when development mode expires (positive integer) or last expired (negative integer) for the domain. If development mode has never been enabled, this value is 0.</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Metadata about the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the zone was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="name_servers" /></td>
    <td><code>array</code></td>
    <td>The name servers Cloudflare assigns to a zone.</td>
</tr>
<tr>
    <td><CopyableCode code="original_dnshost" /></td>
    <td><code>string</code></td>
    <td>DNS host at the time of switching to Cloudflare. (example: NameCheap)</td>
</tr>
<tr>
    <td><CopyableCode code="original_name_servers" /></td>
    <td><code>array</code></td>
    <td>Original name servers before moving to Cloudflare.</td>
</tr>
<tr>
    <td><CopyableCode code="original_registrar" /></td>
    <td><code>string</code></td>
    <td>Registrar for the domain at the time of switching to Cloudflare. (example: GoDaddy)</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>object</code></td>
    <td>The owner of the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the zone is only using Cloudflare DNS services. A true value means the zone will not receive security or performance benefits.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>Legacy permissions based on legacy user membership information. (x-stainless-deprecation-message: This has been replaced by Account memberships.)</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>A Zones subscription information. (x-stainless-deprecation-message: Please use the `/zones/&#123;zone_id&#125;/subscription` API<br />to update a zone's plan. Changing this value will create/cancel<br />associated subscriptions. To view available plans for this zone,<br />see [Zone Plans](https://developers.cloudflare.com/api/resources/zones/subresources/plans/).)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The zone status on Cloudflare. (initializing, pending, active, moved) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="tenant" /></td>
    <td><code>object</code></td>
    <td>The root organizational unit that this zone belongs to (such as a tenant or organization).</td>
</tr>
<tr>
    <td><CopyableCode code="tenant_unit" /></td>
    <td><code>object</code></td>
    <td>The immediate parent organizational unit that this zone belongs to (such as under a tenant or sub-organization).</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. (full, partial, secondary, internal) (default: full, example: full)</td>
</tr>
<tr>
    <td><CopyableCode code="vanity_name_servers" /></td>
    <td><code>array</code></td>
    <td>An array of domains used for custom name servers. This is only available for Business and Enterprise plans.</td>
</tr>
<tr>
    <td><CopyableCode code="verification_key" /></td>
    <td><code>string</code></td>
    <td>Verification key for partial zone setup. (example: 284344499-1084221259)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-account.id"><code>account.id</code></a>, <a href="#parameter-account.name"><code>account.name</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-match"><code>match</code></a></td>
    <td>Lists, searches, sorts, and filters your zones. Listing zones across more than 500 accounts is currently not allowed.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-account"><code>account</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Edits a zone. Only one zone property can be changed at a time.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing zone.</td>
</tr>
<tr>
    <td><a href="#trigger_activation_check"><CopyableCode code="trigger_activation_check" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Triggeres a new activation check for a PENDING Zone. This can be triggered every 5 min for paygo/ent customers, every hour for FREE Zones.</td>
</tr>
<tr>
    <td><a href="#update_custom_ns"><CopyableCode code="update_custom_ns" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Set metadata for account-level custom nameservers on a zone. If you would like new zones in the account to use account custom nameservers by default, use PUT /accounts/:identifier to set the account setting use_account_custom_ns_by_default to true. Deprecated in favor of [Update DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-update-dns-settings).</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-account.id">
    <td><CopyableCode code="account.id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-account.name">
    <td><CopyableCode code="account.name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-match">
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
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
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
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

Zone Details response.

```sql
SELECT
id,
name,
account,
activated_on,
cname_suffix,
created_on,
development_mode,
meta,
modified_on,
name_servers,
original_dnshost,
original_name_servers,
original_registrar,
owner,
paused,
permissions,
plan,
status,
tenant,
tenant_unit,
type,
vanity_name_servers,
verification_key
FROM cloudflare.zones.zones
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists, searches, sorts, and filters your zones. Listing zones across more than 500 accounts is currently not allowed.

```sql
SELECT
id,
name,
account,
activated_on,
cname_suffix,
created_on,
development_mode,
meta,
modified_on,
name_servers,
original_dnshost,
original_name_servers,
original_registrar,
owner,
paused,
permissions,
plan,
status,
tenant,
tenant_unit,
type,
vanity_name_servers,
verification_key
FROM cloudflare.zones.zones
WHERE name = '{{ name }}'
AND status = '{{ status }}'
AND account.id = '{{ account.id }}'
AND account.name = '{{ account.name }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND match = '{{ match }}'
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

No description available.

```sql
INSERT INTO cloudflare.zones.zones (
account,
name,
type
)
SELECT 
'{{ account }}' /* required */,
'{{ name }}' /* required */,
'{{ type }}'
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
- name: zones
  props:
    - name: account
      value:
        id: "{{ id }}"
    - name: name
      value: "{{ name }}"
      description: |
        The domain name. Per [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-2.3.4) the overall zone name can be up to 253 characters, with each segment ("label") not exceeding 63 characters.
    - name: type
      value: "{{ type }}"
      description: |
        A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.
      valid_values: ['full', 'partial', 'secondary', 'internal']
      default: full
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Edits a zone. Only one zone property can be changed at a time.

```sql
UPDATE cloudflare.zones.zones
SET 
paused = {{ paused }},
type = '{{ type }}',
vanity_name_servers = '{{ vanity_name_servers }}'
WHERE 
zone_id = '{{ zone_id }}' --required
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

Deletes an existing zone.

```sql
DELETE FROM cloudflare.zones.zones
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="trigger_activation_check"
    values={[
        { label: 'trigger_activation_check', value: 'trigger_activation_check' },
        { label: 'update_custom_ns', value: 'update_custom_ns' }
    ]}
>
<TabItem value="trigger_activation_check">

Triggeres a new activation check for a PENDING Zone. This can be triggered every 5 min for paygo/ent customers, every hour for FREE Zones.

```sql
EXEC cloudflare.zones.zones.trigger_activation_check 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
<TabItem value="update_custom_ns">

Set metadata for account-level custom nameservers on a zone. If you would like new zones in the account to use account custom nameservers by default, use PUT /accounts/:identifier to set the account setting use_account_custom_ns_by_default to true. Deprecated in favor of [Update DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-update-dns-settings).

```sql
EXEC cloudflare.zones.zones.update_custom_ns 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"enabled": {{ enabled }}, 
"ns_set": {{ ns_set }}
}'
;
```
</TabItem>
</Tabs>
