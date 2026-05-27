--- 
title: netflow_config
hide_title: false
hide_table_of_contents: false
keywords:
  - netflow_config
  - magic_transit
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

Creates, updates, deletes, gets or lists a <code>netflow_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="netflow_config" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.netflow_config" /></td></tr>
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

Get NetFlow Configuration response

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
    <td><CopyableCode code="active_timeout" /></td>
    <td><code>integer</code></td>
    <td>Timeout in seconds for active flows (defaults to 30).</td>
</tr>
<tr>
    <td><CopyableCode code="collector_ip" /></td>
    <td><code>string</code></td>
    <td>IPv4 address of the NetFlow collector. (example: 162.159.65.1)</td>
</tr>
<tr>
    <td><CopyableCode code="collector_port" /></td>
    <td><code>integer</code></td>
    <td>UDP port of the NetFlow collector (defaults to 2055).</td>
</tr>
<tr>
    <td><CopyableCode code="inactive_timeout" /></td>
    <td><code>integer</code></td>
    <td>Timeout in seconds for inactive flows (defaults to 15).</td>
</tr>
<tr>
    <td><CopyableCode code="sampling_rate" /></td>
    <td><code>integer</code></td>
    <td>Sampling rate for NetFlow records (1 = every packet, 1000 = 1 in 1000 packets). Defaults to 1.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Get NetFlow configuration for a site.</td>
</tr>
<tr>
    <td><a href="#magic_site_netflow_config_create_netflow_config"><CopyableCode code="magic_site_netflow_config_create_netflow_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Creates a NetFlow configuration for a site.</td>
</tr>
<tr>
    <td><a href="#magic_site_netflow_config_patch_netflow_config"><CopyableCode code="magic_site_netflow_config_patch_netflow_config" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Updates NetFlow configuration for a site.</td>
</tr>
<tr>
    <td><a href="#magic_site_netflow_config_update_netflow_config"><CopyableCode code="magic_site_netflow_config_update_netflow_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Updates NetFlow configuration for a site (partial update).</td>
</tr>
<tr>
    <td><a href="#magic_site_netflow_config_delete_netflow_config"><CopyableCode code="magic_site_netflow_config_delete_netflow_config" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Remove NetFlow configuration for a site.</td>
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
<tr id="parameter-site_id">
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>The site ID.</td>
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

Get NetFlow configuration for a site.

```sql
SELECT
active_timeout,
collector_ip,
collector_port,
inactive_timeout,
sampling_rate
FROM cloudflare.magic_transit.netflow_config
WHERE account_id = '{{ account_id }}' -- required
AND site_id = '{{ site_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="magic_site_netflow_config_create_netflow_config"
    values={[
        { label: 'magic_site_netflow_config_create_netflow_config', value: 'magic_site_netflow_config_create_netflow_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="magic_site_netflow_config_create_netflow_config">

Creates a NetFlow configuration for a site.

```sql
INSERT INTO cloudflare.magic_transit.netflow_config (
active_timeout,
collector_ip,
collector_port,
inactive_timeout,
sampling_rate,
account_id,
site_id
)
SELECT 
{{ active_timeout }},
'{{ collector_ip }}',
{{ collector_port }},
{{ inactive_timeout }},
{{ sampling_rate }},
'{{ account_id }}',
'{{ site_id }}'
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
- name: netflow_config
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the netflow_config resource.
    - name: site_id
      value: "{{ site_id }}"
      description: Required parameter for the netflow_config resource.
    - name: active_timeout
      value: {{ active_timeout }}
      description: |
        Timeout in seconds for active flows.
    - name: collector_ip
      value: "{{ collector_ip }}"
      description: |
        IPv4 address of the NetFlow collector.
    - name: collector_port
      value: {{ collector_port }}
      description: |
        UDP port of the NetFlow collector.
    - name: inactive_timeout
      value: {{ inactive_timeout }}
      description: |
        Timeout in seconds for inactive flows.
    - name: sampling_rate
      value: {{ sampling_rate }}
      description: |
        Sampling rate for NetFlow records (1 = every packet).
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="magic_site_netflow_config_patch_netflow_config"
    values={[
        { label: 'magic_site_netflow_config_patch_netflow_config', value: 'magic_site_netflow_config_patch_netflow_config' }
    ]}
>
<TabItem value="magic_site_netflow_config_patch_netflow_config">

Updates NetFlow configuration for a site.

```sql
UPDATE cloudflare.magic_transit.netflow_config
SET 
active_timeout = {{ active_timeout }},
collector_ip = '{{ collector_ip }}',
collector_port = {{ collector_port }},
inactive_timeout = {{ inactive_timeout }},
sampling_rate = {{ sampling_rate }}
WHERE 
account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
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
    defaultValue="magic_site_netflow_config_update_netflow_config"
    values={[
        { label: 'magic_site_netflow_config_update_netflow_config', value: 'magic_site_netflow_config_update_netflow_config' }
    ]}
>
<TabItem value="magic_site_netflow_config_update_netflow_config">

Updates NetFlow configuration for a site (partial update).

```sql
REPLACE cloudflare.magic_transit.netflow_config
SET 
active_timeout = {{ active_timeout }},
collector_ip = '{{ collector_ip }}',
collector_port = {{ collector_port }},
inactive_timeout = {{ inactive_timeout }},
sampling_rate = {{ sampling_rate }}
WHERE 
account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
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
    defaultValue="magic_site_netflow_config_delete_netflow_config"
    values={[
        { label: 'magic_site_netflow_config_delete_netflow_config', value: 'magic_site_netflow_config_delete_netflow_config' }
    ]}
>
<TabItem value="magic_site_netflow_config_delete_netflow_config">

Remove NetFlow configuration for a site.

```sql
DELETE FROM cloudflare.magic_transit.netflow_config
WHERE account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
;
```
</TabItem>
</Tabs>
