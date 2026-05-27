--- 
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get zone setting response

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
    <td>ID of the zone setting. (0rtt) (example: 0rtt)</td>
</tr>
<tr>
    <td><CopyableCode code="editable" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not this setting can be modified for this zone (based on your Cloudflare plan level). (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>ssl-recommender enrollment setting.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>last time this setting was modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="time_remaining" /></td>
    <td><code>number</code></td>
    <td>Value of the zone setting. Notes: The interval (in seconds) from when development mode expires (positive integer) or last expired (negative integer) for the domain. If development mode has never been enabled, this value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Current value of the zone setting. (on, off) (example: on, default: off)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-setting_id"><code>setting_id</code></a></td>
    <td></td>
    <td>Fetch a single zone setting by name</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-setting_id"><code>setting_id</code></a></td>
    <td></td>
    <td>Updates a single zone setting by the identifier</td>
</tr>
<tr>
    <td><a href="#zone_settings_edit_zone_settings_info"><CopyableCode code="zone_settings_edit_zone_settings_info" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Edit settings for a zone.</td>
</tr>
<tr>
    <td><a href="#firewall_for_ai_settings_put"><CopyableCode code="firewall_for_ai_settings_put" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Enable or disable Firewall for AI for a zone. Changes can take up to a minute to propagate to the zone.</td>
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
<tr id="parameter-setting_id">
    <td><CopyableCode code="setting_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Fetch a single zone setting by name

```sql
SELECT
id,
editable,
enabled,
modified_on,
time_remaining,
value
FROM cloudflare.zones.settings
WHERE zone_id = '{{ zone_id }}' -- required
AND setting_id = '{{ setting_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'zone_settings_edit_zone_settings_info', value: 'zone_settings_edit_zone_settings_info' }
    ]}
>
<TabItem value="edit">

Updates a single zone setting by the identifier

```sql
UPDATE cloudflare.zones.settings
SET 
enabled = {{ enabled }},
value = '{{ value }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND setting_id = '{{ setting_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="zone_settings_edit_zone_settings_info">

Edit settings for a zone.

```sql
UPDATE cloudflare.zones.settings
SET 
-- No updatable properties
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


## `REPLACE` examples

<Tabs
    defaultValue="firewall_for_ai_settings_put"
    values={[
        { label: 'firewall_for_ai_settings_put', value: 'firewall_for_ai_settings_put' }
    ]}
>
<TabItem value="firewall_for_ai_settings_put">

Enable or disable Firewall for AI for a zone. Changes can take up to a minute to propagate to the zone.

```sql
REPLACE cloudflare.zones.settings
SET 
enabled = {{ enabled }}
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
