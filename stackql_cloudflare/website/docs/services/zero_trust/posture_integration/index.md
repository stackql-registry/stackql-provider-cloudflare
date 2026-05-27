--- 
title: posture_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - posture_integration
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

Creates, updates, deletes, gets or lists a <code>posture_integration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="posture_integration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.posture_integration" /></td></tr>
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

Get device posture integration details response.

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
    <td>API UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the device posture integration. (example: My Workspace One Integration)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>The configuration object containing third-party integration information.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval between each posture check with the third-party API. Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`). (example: 10m)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of device posture integration. (workspace_one, crowdstrike_s2s, uptycs, intune, kolide, tanium_s2s, sentinelone_s2s, custom_s2s) (example: workspace_one)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List your device posture integrations response.

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
    <td>API UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the device posture integration. (example: My Workspace One Integration)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>The configuration object containing third-party integration information.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>The interval between each posture check with the third-party API. Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`). (example: 10m)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of device posture integration. (workspace_one, crowdstrike_s2s, uptycs, intune, kolide, tanium_s2s, sentinelone_s2s, custom_s2s) (example: workspace_one)</td>
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
    <td><a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches details for a single device posture integration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the list of device posture integrations for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-interval"><code>interval</code></a>, <a href="#parameter-config"><code>config</code></a></td>
    <td></td>
    <td>Create a new device posture integration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured device posture integration.</td>
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
<tr id="parameter-integration_id">
    <td><CopyableCode code="integration_id" /></td>
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

Fetches details for a single device posture integration.

```sql
SELECT
id,
name,
config,
interval,
type
FROM cloudflare.zero_trust.posture_integration
WHERE integration_id = '{{ integration_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches the list of device posture integrations for an account.

```sql
SELECT
id,
name,
config,
interval,
type
FROM cloudflare.zero_trust.posture_integration
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

Create a new device posture integration.

```sql
INSERT INTO cloudflare.zero_trust.posture_integration (
config,
interval,
name,
type,
account_id
)
SELECT 
'{{ config }}' /* required */,
'{{ interval }}' /* required */,
'{{ name }}' /* required */,
'{{ type }}' /* required */,
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
- name: posture_integration
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the posture_integration resource.
    - name: config
      description: |
        The configuration object containing third-party integration information.
      value:
        api_url: "{{ api_url }}"
        auth_url: "{{ auth_url }}"
        client_id: "{{ client_id }}"
        client_secret: "{{ client_secret }}"
        customer_id: "{{ customer_id }}"
        client_key: "{{ client_key }}"
        access_client_id: "{{ access_client_id }}"
        access_client_secret: "{{ access_client_secret }}"
    - name: interval
      value: "{{ interval }}"
      description: |
        The interval between each posture check with the third-party API. Use \`m\` for minutes (e.g. \`5m\`) and \`h\` for hours (e.g. \`12h\`).
    - name: name
      value: "{{ name }}"
      description: |
        The name of the device posture integration.
    - name: type
      value: "{{ type }}"
      description: |
        The type of device posture integration.
      valid_values: ['workspace_one', 'crowdstrike_s2s', 'uptycs', 'intune', 'kolide', 'tanium_s2s', 'sentinelone_s2s', 'custom_s2s']
`}</CodeBlock>

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

Delete a configured device posture integration.

```sql
DELETE FROM cloudflare.zero_trust.posture_integration
WHERE integration_id = '{{ integration_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
