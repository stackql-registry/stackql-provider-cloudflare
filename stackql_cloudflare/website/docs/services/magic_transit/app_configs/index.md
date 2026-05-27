--- 
title: app_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - app_configs
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

Creates, updates, deletes, gets or lists an <code>app_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.app_configs" /></td></tr>
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

List App Configs response

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
    <td><CopyableCode code="account_app_id" /></td>
    <td><code>string</code></td>
    <td>Magic account app ID. (example: ac60d3d0435248289d446cedd870bcf4)</td>
</tr>
<tr>
    <td><CopyableCode code="managed_app_id" /></td>
    <td><code>string</code></td>
    <td>Managed app ID. (example: cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="breakout" /></td>
    <td><code>boolean</code></td>
    <td>Whether to breakout traffic to the app's endpoints directly. Null preserves default behavior.</td>
</tr>
<tr>
    <td><CopyableCode code="preferred_wans" /></td>
    <td><code>array</code></td>
    <td>WAN interfaces to prefer over default WANs, highest-priority first. Can only be specified for breakout rules (breakout must be true).</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of traffic. 0 is default, anything greater is prioritized. (Currently only 0 and 1 are supported)</td>
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
    <td>Lists App Configs associated with a site.</td>
</tr>
<tr>
    <td><a href="#magic_site_app_configs_add_app_config"><CopyableCode code="magic_site_app_configs_add_app_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Creates a new App Config for a site</td>
</tr>
<tr>
    <td><a href="#magic_site_app_configs_patch_app_config"><CopyableCode code="magic_site_app_configs_patch_app_config" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-app_config_id"><code>app_config_id</code></a></td>
    <td></td>
    <td>Updates an App Config for a site</td>
</tr>
<tr>
    <td><a href="#magic_site_app_configs_update_app_config"><CopyableCode code="magic_site_app_configs_update_app_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-app_config_id"><code>app_config_id</code></a></td>
    <td></td>
    <td>Updates an App Config for a site</td>
</tr>
<tr>
    <td><a href="#magic_site_app_configs_delete_app_config"><CopyableCode code="magic_site_app_configs_delete_app_config" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-app_config_id"><code>app_config_id</code></a></td>
    <td></td>
    <td>Deletes specific App Config associated with a site.</td>
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
<tr id="parameter-app_config_id">
    <td><CopyableCode code="app_config_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Lists App Configs associated with a site.

```sql
SELECT
id,
account_app_id,
managed_app_id,
site_id,
breakout,
preferred_wans,
priority
FROM cloudflare.magic_transit.app_configs
WHERE account_id = '{{ account_id }}' -- required
AND site_id = '{{ site_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="magic_site_app_configs_add_app_config"
    values={[
        { label: 'magic_site_app_configs_add_app_config', value: 'magic_site_app_configs_add_app_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="magic_site_app_configs_add_app_config">

Creates a new App Config for a site

```sql
INSERT INTO cloudflare.magic_transit.app_configs (
breakout,
preferred_wans,
priority,
account_app_id,
managed_app_id,
account_id,
site_id
)
SELECT 
{{ breakout }},
'{{ preferred_wans }}',
{{ priority }},
'{{ account_app_id }}',
'{{ managed_app_id }}',
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
- name: app_configs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the app_configs resource.
    - name: site_id
      value: "{{ site_id }}"
      description: Required parameter for the app_configs resource.
    - name: breakout
      value: {{ breakout }}
      description: |
        Whether to breakout traffic to the app's endpoints directly. Null preserves default behavior.
    - name: preferred_wans
      value:
        - "{{ preferred_wans }}"
      description: |
        WAN interfaces to prefer over default WANs, highest-priority first. Can only be specified for breakout rules (breakout must be true).
    - name: priority
      value: {{ priority }}
      description: |
        Priority of traffic. 0 is default, anything greater is prioritized. (Currently only 0 and 1 are supported)
    - name: account_app_id
      value: "{{ account_app_id }}"
      description: |
        Magic account app ID.
    - name: managed_app_id
      value: "{{ managed_app_id }}"
      description: |
        Managed app ID.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="magic_site_app_configs_patch_app_config"
    values={[
        { label: 'magic_site_app_configs_patch_app_config', value: 'magic_site_app_configs_patch_app_config' }
    ]}
>
<TabItem value="magic_site_app_configs_patch_app_config">

Updates an App Config for a site

```sql
UPDATE cloudflare.magic_transit.app_configs
SET 
account_app_id = '{{ account_app_id }}',
breakout = {{ breakout }},
managed_app_id = '{{ managed_app_id }}',
preferred_wans = '{{ preferred_wans }}',
priority = {{ priority }}
WHERE 
account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
AND app_config_id = '{{ app_config_id }}' --required
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
    defaultValue="magic_site_app_configs_update_app_config"
    values={[
        { label: 'magic_site_app_configs_update_app_config', value: 'magic_site_app_configs_update_app_config' }
    ]}
>
<TabItem value="magic_site_app_configs_update_app_config">

Updates an App Config for a site

```sql
REPLACE cloudflare.magic_transit.app_configs
SET 
account_app_id = '{{ account_app_id }}',
breakout = {{ breakout }},
managed_app_id = '{{ managed_app_id }}',
preferred_wans = '{{ preferred_wans }}',
priority = {{ priority }}
WHERE 
account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
AND app_config_id = '{{ app_config_id }}' --required
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
    defaultValue="magic_site_app_configs_delete_app_config"
    values={[
        { label: 'magic_site_app_configs_delete_app_config', value: 'magic_site_app_configs_delete_app_config' }
    ]}
>
<TabItem value="magic_site_app_configs_delete_app_config">

Deletes specific App Config associated with a site.

```sql
DELETE FROM cloudflare.magic_transit.app_configs
WHERE account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
AND app_config_id = '{{ app_config_id }}' --required
;
```
</TabItem>
</Tabs>
