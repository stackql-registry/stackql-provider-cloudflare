--- 
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
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

Creates, updates, deletes, gets or lists a <code>connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connectors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.connectors" /></td></tr>
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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activated" /></td>
    <td><code>boolean</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="device" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_days_of_week" /></td>
    <td><code>array</code></td>
    <td>Allowed days of the week for upgrades. Default is all days. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_duration_hours" /></td>
    <td><code>number</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_embargo_dates" /></td>
    <td><code>array</code></td>
    <td>List of dates (YYYY-MM-DD) when upgrades are blocked. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_hour_of_day" /></td>
    <td><code>number</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="last_heartbeat" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="license_key" /></td>
    <td><code>string</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="timezone" /></td>
    <td><code>string</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="activated" /></td>
    <td><code>boolean</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="device" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_days_of_week" /></td>
    <td><code>array</code></td>
    <td>Allowed days of the week for upgrades. Default is all days. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_duration_hours" /></td>
    <td><code>number</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_embargo_dates" /></td>
    <td><code>array</code></td>
    <td>List of dates (YYYY-MM-DD) when upgrades are blocked. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="interrupt_window_hour_of_day" /></td>
    <td><code>number</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="last_heartbeat" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="license_key" /></td>
    <td><code>string</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="timezone" /></td>
    <td><code>string</code></td>
    <td> (x-stainless-terraform-configurability: computed_optional)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-device_type"><code>device_type</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-device"><code>device</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-connector_id">
    <td><CopyableCode code="connector_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-device_type">
    <td><CopyableCode code="device_type" /></td>
    <td><code>string</code></td>
    <td>Filter connectors by device type.</td>
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

OK

```sql
SELECT
id,
activated,
device,
interrupt_window_days_of_week,
interrupt_window_duration_hours,
interrupt_window_embargo_dates,
interrupt_window_hour_of_day,
last_heartbeat,
last_seen_version,
last_updated,
license_key,
notes,
timezone
FROM cloudflare.magic_transit.connectors
WHERE account_id = '{{ account_id }}' -- required
AND connector_id = '{{ connector_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

OK

```sql
SELECT
id,
activated,
device,
interrupt_window_days_of_week,
interrupt_window_duration_hours,
interrupt_window_embargo_dates,
interrupt_window_hour_of_day,
last_heartbeat,
last_seen_version,
last_updated,
license_key,
notes,
timezone
FROM cloudflare.magic_transit.connectors
WHERE account_id = '{{ account_id }}' -- required
AND device_type = '{{ device_type }}'
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
INSERT INTO cloudflare.magic_transit.connectors (
device,
activated,
interrupt_window_days_of_week,
interrupt_window_duration_hours,
interrupt_window_embargo_dates,
interrupt_window_hour_of_day,
notes,
timezone,
account_id
)
SELECT 
'{{ device }}' /* required */,
{{ activated }},
'{{ interrupt_window_days_of_week }}',
{{ interrupt_window_duration_hours }},
'{{ interrupt_window_embargo_dates }}',
{{ interrupt_window_hour_of_day }},
'{{ notes }}',
'{{ timezone }}',
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
- name: connectors
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the connectors resource.
    - name: device
      description: |
        Exactly one of id, serial_number, or provision_license must be provided.
      value:
        id: "{{ id }}"
        provision_license: {{ provision_license }}
        serial_number: "{{ serial_number }}"
    - name: activated
      value: {{ activated }}
    - name: interrupt_window_days_of_week
      value:
        - "{{ interrupt_window_days_of_week }}"
      description: |
        Allowed days of the week for upgrades. Default is all days.
    - name: interrupt_window_duration_hours
      value: {{ interrupt_window_duration_hours }}
    - name: interrupt_window_embargo_dates
      value:
        - "{{ interrupt_window_embargo_dates }}"
      description: |
        List of dates (YYYY-MM-DD) when upgrades are blocked.
    - name: interrupt_window_hour_of_day
      value: {{ interrupt_window_hour_of_day }}
    - name: notes
      value: "{{ notes }}"
    - name: timezone
      value: "{{ timezone }}"
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

No description available.

```sql
UPDATE cloudflare.magic_transit.connectors
SET 
activated = {{ activated }},
interrupt_window_days_of_week = '{{ interrupt_window_days_of_week }}',
interrupt_window_duration_hours = {{ interrupt_window_duration_hours }},
interrupt_window_embargo_dates = '{{ interrupt_window_embargo_dates }}',
interrupt_window_hour_of_day = {{ interrupt_window_hour_of_day }},
notes = '{{ notes }}',
timezone = '{{ timezone }}',
provision_license = {{ provision_license }}
WHERE 
account_id = '{{ account_id }}' --required
AND connector_id = '{{ connector_id }}' --required
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

No description available.

```sql
REPLACE cloudflare.magic_transit.connectors
SET 
activated = {{ activated }},
interrupt_window_days_of_week = '{{ interrupt_window_days_of_week }}',
interrupt_window_duration_hours = {{ interrupt_window_duration_hours }},
interrupt_window_embargo_dates = '{{ interrupt_window_embargo_dates }}',
interrupt_window_hour_of_day = {{ interrupt_window_hour_of_day }},
notes = '{{ notes }}',
timezone = '{{ timezone }}',
provision_license = {{ provision_license }}
WHERE 
account_id = '{{ account_id }}' --required
AND connector_id = '{{ connector_id }}' --required
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

No description available.

```sql
DELETE FROM cloudflare.magic_transit.connectors
WHERE account_id = '{{ account_id }}' --required
AND connector_id = '{{ connector_id }}' --required
;
```
</TabItem>
</Tabs>
