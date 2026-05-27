--- 
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.settings" /></td></tr>
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

List mTLS hostname settings response

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
    <td><CopyableCode code="china_network" /></td>
    <td><code>boolean</code></td>
    <td>Request client certificates for this hostname in China. Can only be set to true if this zone is china network enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="client_certificate_forwarding" /></td>
    <td><code>boolean</code></td>
    <td>Client Certificate Forwarding is a feature that takes the client cert provided by the eyeball to the edge, and forwards it to the origin as a HTTP header to allow logging on the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname that these settings apply to. (example: admin.example.com)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>List all mTLS hostname settings for this account or zone.</td>
</tr>
<tr>
    <td><a href="#edit_by_account"><CopyableCode code="edit_by_account" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates Access application settings.</td>
</tr>
<tr>
    <td><a href="#edit_by_zone"><CopyableCode code="edit_by_zone" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates Access application settings.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates Access application settings.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates Access application settings.</td>
</tr>
<tr>
    <td><a href="#put_accounts_account_id_access_certificates_settings"><CopyableCode code="put_accounts_account_id_access_certificates_settings" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-settings"><code>settings</code></a></td>
    <td></td>
    <td>Updates an mTLS certificate's hostname settings.</td>
</tr>
<tr>
    <td><a href="#put_zones_zone_id_access_certificates_settings"><CopyableCode code="put_zones_zone_id_access_certificates_settings" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-settings"><code>settings</code></a></td>
    <td></td>
    <td>Updates an mTLS certificate's hostname settings.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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

List all mTLS hostname settings for this account or zone.

```sql
SELECT
china_network,
client_certificate_forwarding,
hostname
FROM cloudflare.zero_trust.settings
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit_by_account"
    values={[
        { label: 'edit_by_account', value: 'edit_by_account' },
        { label: 'edit_by_zone', value: 'edit_by_zone' }
    ]}
>
<TabItem value="edit_by_account">

Updates Access application settings.

```sql
UPDATE cloudflare.zero_trust.settings
SET 
allow_iframe = {{ allow_iframe }},
skip_interstitial = {{ skip_interstitial }}
WHERE 
app_id = '{{ app_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="edit_by_zone">

Updates Access application settings.

```sql
UPDATE cloudflare.zero_trust.settings
SET 
allow_iframe = {{ allow_iframe }},
skip_interstitial = {{ skip_interstitial }}
WHERE 
app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' },
        { label: 'update_by_zone', value: 'update_by_zone' },
        { label: 'put_accounts_account_id_access_certificates_settings', value: 'put_accounts_account_id_access_certificates_settings' },
        { label: 'put_zones_zone_id_access_certificates_settings', value: 'put_zones_zone_id_access_certificates_settings' }
    ]}
>
<TabItem value="update_by_account">

Updates Access application settings.

```sql
REPLACE cloudflare.zero_trust.settings
SET 
allow_iframe = {{ allow_iframe }},
skip_interstitial = {{ skip_interstitial }}
WHERE 
app_id = '{{ app_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates Access application settings.

```sql
REPLACE cloudflare.zero_trust.settings
SET 
allow_iframe = {{ allow_iframe }},
skip_interstitial = {{ skip_interstitial }}
WHERE 
app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="put_accounts_account_id_access_certificates_settings">

Updates an mTLS certificate's hostname settings.

```sql
REPLACE cloudflare.zero_trust.settings
SET 
settings = '{{ settings }}'
WHERE 
account_id = '{{ account_id }}' --required
AND settings = '{{ settings }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
<TabItem value="put_zones_zone_id_access_certificates_settings">

Updates an mTLS certificate's hostname settings.

```sql
REPLACE cloudflare.zero_trust.settings
SET 
settings = '{{ settings }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND settings = '{{ settings }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>
