--- 
title: relays
hide_title: false
hide_table_of_contents: false
keywords:
  - relays
  - realtime_kit
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

Creates, updates, deletes, gets or lists a <code>relays</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="relays" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.realtime_kit.relays" /></td></tr>
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

Relay retrieved successfully.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: Production Live Stream)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>origin_fallback and lingering_subscribe are mutually exclusive.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>"connected" when active, omitted otherwise. (connected)</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td> (example: a1b2c3d4e5f67890a1b2c3d4e5f67890)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Relay list retrieved successfully.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td> (example: a1b2c3d4e5f67890a1b2c3d4e5f67890)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-relay_id"><code>relay_id</code></a></td>
    <td></td>
    <td>Retrieves a single MoQ relay including config and status. Tokens are NOT included.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all MoQ relays for the account. Returns only metadata. Config, status, and tokens are omitted.</td>
</tr>
<tr>
    <td><a href="#post_accounts_account_id_moq_relays"><CopyableCode code="post_accounts_account_id_moq_relays" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Provisions a new MoQ relay instance. Auto-creates a publish+subscribe token and a subscribe-only token. Token values are included in the response (shown once). Config is set to defaults (lingering subscribe enabled, 30s ceiling, origin fallback off). Use PUT to modify.</td>
</tr>
<tr>
    <td><a href="#put_accounts_account_id_moq_relays_relay_id"><CopyableCode code="put_accounts_account_id_moq_relays_relay_id" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-relay_id"><code>relay_id</code></a></td>
    <td></td>
    <td>Updates a relay's name and/or configuration. Partial updates: omitted fields are preserved. Config sub-objects replace as whole objects when present. origin_fallback and lingering_subscribe are mutually exclusive.</td>
</tr>
<tr>
    <td><a href="#delete_accounts_account_id_moq_relays_relay_id"><CopyableCode code="delete_accounts_account_id_moq_relays_relay_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-relay_id"><code>relay_id</code></a></td>
    <td></td>
    <td>Soft-deletes a MoQ relay.</td>
</tr>
<tr>
    <td><a href="#rotate"><CopyableCode code="rotate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-relay_id"><code>relay_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Generates a new token for the specified type. The old token is immediately invalidated. Token value is shown once in the response.</td>
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
<tr id="parameter-relay_id">
    <td><CopyableCode code="relay_id" /></td>
    <td><code>string</code></td>
    <td>Relay unique identifier (32 hex characters).</td>
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

Retrieves a single MoQ relay including config and status. Tokens are NOT included.

```sql
SELECT
name,
config,
created,
modified,
status,
uid
FROM cloudflare.realtime_kit.relays
WHERE account_id = '{{ account_id }}' -- required
AND relay_id = '{{ relay_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all MoQ relays for the account. Returns only metadata. Config, status, and tokens are omitted.

```sql
SELECT
name,
created,
modified,
uid
FROM cloudflare.realtime_kit.relays
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_accounts_account_id_moq_relays"
    values={[
        { label: 'post_accounts_account_id_moq_relays', value: 'post_accounts_account_id_moq_relays' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_accounts_account_id_moq_relays">

Provisions a new MoQ relay instance. Auto-creates a publish+subscribe token and a subscribe-only token. Token values are included in the response (shown once). Config is set to defaults (lingering subscribe enabled, 30s ceiling, origin fallback off). Use PUT to modify.

```sql
INSERT INTO cloudflare.realtime_kit.relays (
name,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ account_id }}'
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
- name: relays
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the relays resource.
    - name: name
      value: "{{ name }}"
      description: |
        Human-readable name for the relay.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_accounts_account_id_moq_relays_relay_id"
    values={[
        { label: 'put_accounts_account_id_moq_relays_relay_id', value: 'put_accounts_account_id_moq_relays_relay_id' }
    ]}
>
<TabItem value="put_accounts_account_id_moq_relays_relay_id">

Updates a relay's name and/or configuration. Partial updates: omitted fields are preserved. Config sub-objects replace as whole objects when present. origin_fallback and lingering_subscribe are mutually exclusive.

```sql
REPLACE cloudflare.realtime_kit.relays
SET 
config = '{{ config }}',
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND relay_id = '{{ relay_id }}' --required
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
    defaultValue="delete_accounts_account_id_moq_relays_relay_id"
    values={[
        { label: 'delete_accounts_account_id_moq_relays_relay_id', value: 'delete_accounts_account_id_moq_relays_relay_id' }
    ]}
>
<TabItem value="delete_accounts_account_id_moq_relays_relay_id">

Soft-deletes a MoQ relay.

```sql
DELETE FROM cloudflare.realtime_kit.relays
WHERE account_id = '{{ account_id }}' --required
AND relay_id = '{{ relay_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rotate"
    values={[
        { label: 'rotate', value: 'rotate' }
    ]}
>
<TabItem value="rotate">

Generates a new token for the specified type. The old token is immediately invalidated. Token value is shown once in the response.

```sql
EXEC cloudflare.realtime_kit.relays.rotate 
@account_id='{{ account_id }}' --required, 
@relay_id='{{ relay_id }}' --required 
@@json=
'{
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
