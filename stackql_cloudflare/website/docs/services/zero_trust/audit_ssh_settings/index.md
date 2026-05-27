--- 
title: audit_ssh_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_ssh_settings
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

Creates, updates, deletes, gets or lists an <code>audit_ssh_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="audit_ssh_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.audit_ssh_settings" /></td></tr>
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

Get Zero Trust SSH settings response.

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
    <td><CopyableCode code="seed_id" /></td>
    <td><code>string</code></td>
    <td>Identify the seed ID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="public_key" /></td>
    <td><code>string</code></td>
    <td>Provide the Base64-encoded HPKE public key that encrypts SSH session logs. See https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/#enable-ssh-command-logging. (example: 1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td></td>
    <td>Retrieve all Zero Trust Audit SSH and SSH with Access for Infrastructure settings for an account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-public_key"><code>public_key</code></a></td>
    <td></td>
    <td>Update Zero Trust Audit SSH and SSH with Access for Infrastructure settings for an account.</td>
</tr>
<tr>
    <td><a href="#rotate_seed"><CopyableCode code="rotate_seed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Rotate the SSH account seed that generates the host key identity when connecting through the Cloudflare SSH Proxy.</td>
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

Retrieve all Zero Trust Audit SSH and SSH with Access for Infrastructure settings for an account.

```sql
SELECT
seed_id,
created_at,
public_key,
updated_at
FROM cloudflare.zero_trust.audit_ssh_settings
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update Zero Trust Audit SSH and SSH with Access for Infrastructure settings for an account.

```sql
REPLACE cloudflare.zero_trust.audit_ssh_settings
SET 
public_key = '{{ public_key }}'
WHERE 
account_id = '{{ account_id }}' --required
AND public_key = '{{ public_key }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rotate_seed"
    values={[
        { label: 'rotate_seed', value: 'rotate_seed' }
    ]}
>
<TabItem value="rotate_seed">

Rotate the SSH account seed that generates the host key identity when connecting through the Cloudflare SSH Proxy.

```sql
EXEC cloudflare.zero_trust.audit_ssh_settings.rotate_seed 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
