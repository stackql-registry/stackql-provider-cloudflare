--- 
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - magic_network_monitoring
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

Creates, updates, deletes, gets or lists a <code>configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_network_monitoring.configs" /></td></tr>
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

List account configuration response

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
    <td>The account name. (example: cloudflare user's account)</td>
</tr>
<tr>
    <td><CopyableCode code="default_sampling" /></td>
    <td><code>number</code></td>
    <td>Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate configured on the router.</td>
</tr>
<tr>
    <td><CopyableCode code="router_ips" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="warp_devices" /></td>
    <td><code>array</code></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists default sampling, router IPs and warp devices for account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-default_sampling"><code>default_sampling</code></a></td>
    <td></td>
    <td>Create a new network monitoring configuration.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Update fields in an existing network monitoring configuration.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-default_sampling"><code>default_sampling</code></a></td>
    <td></td>
    <td>Update an existing network monitoring configuration, requires the entire configuration to be updated at once.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete an existing network monitoring configuration.</td>
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

Lists default sampling, router IPs and warp devices for account.

```sql
SELECT
name,
default_sampling,
router_ips,
warp_devices
FROM cloudflare.magic_network_monitoring.configs
WHERE account_id = '{{ account_id }}' -- required
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

Create a new network monitoring configuration.

```sql
INSERT INTO cloudflare.magic_network_monitoring.configs (
default_sampling,
name,
router_ips,
warp_devices,
account_id
)
SELECT 
{{ default_sampling }} /* required */,
'{{ name }}' /* required */,
'{{ router_ips }}',
'{{ warp_devices }}',
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
- name: configs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the configs resource.
    - name: default_sampling
      value: {{ default_sampling }}
      description: |
        Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate configured on the router.
      default: 1
    - name: name
      value: "{{ name }}"
      description: |
        The account name.
    - name: router_ips
      value:
        - "{{ router_ips }}"
    - name: warp_devices
      value:
        - id: "{{ id }}"
          name: "{{ name }}"
          router_ip: "{{ router_ip }}"
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

Update fields in an existing network monitoring configuration.

```sql
UPDATE cloudflare.magic_network_monitoring.configs
SET 
default_sampling = {{ default_sampling }},
name = '{{ name }}',
router_ips = '{{ router_ips }}',
warp_devices = '{{ warp_devices }}'
WHERE 
account_id = '{{ account_id }}' --required
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
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an existing network monitoring configuration, requires the entire configuration to be updated at once.

```sql
REPLACE cloudflare.magic_network_monitoring.configs
SET 
default_sampling = {{ default_sampling }},
name = '{{ name }}',
router_ips = '{{ router_ips }}',
warp_devices = '{{ warp_devices }}'
WHERE 
account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND default_sampling = '{{ default_sampling }}' --required
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

Delete an existing network monitoring configuration.

```sql
DELETE FROM cloudflare.magic_network_monitoring.configs
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
