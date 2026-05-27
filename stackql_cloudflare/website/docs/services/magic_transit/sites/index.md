--- 
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
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

Creates, updates, deletes, gets or lists a <code>sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sites" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.sites" /></td></tr>
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

Site Details response

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
    <td>The name of the site. (example: site_1)</td>
</tr>
<tr>
    <td><CopyableCode code="connector_id" /></td>
    <td><code>string</code></td>
    <td>Magic Connector identifier tag. (example: ac60d3d0435248289d446cedd870bcf4)</td>
</tr>
<tr>
    <td><CopyableCode code="secondary_connector_id" /></td>
    <td><code>string</code></td>
    <td>Magic Connector identifier tag. Used when high availability mode is on. (example: 8d67040d3835dbcf46ce29da440dc482)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ha_mode" /></td>
    <td><code>boolean</code></td>
    <td>Site high availability mode. If set to true, the site can have two connectors and runs in high availability mode.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>object</code></td>
    <td>Location of site in latitude and longitude.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Sites response

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
    <td>The name of the site. (example: site_1)</td>
</tr>
<tr>
    <td><CopyableCode code="connector_id" /></td>
    <td><code>string</code></td>
    <td>Magic Connector identifier tag. (example: ac60d3d0435248289d446cedd870bcf4)</td>
</tr>
<tr>
    <td><CopyableCode code="secondary_connector_id" /></td>
    <td><code>string</code></td>
    <td>Magic Connector identifier tag. Used when high availability mode is on. (example: 8d67040d3835dbcf46ce29da440dc482)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ha_mode" /></td>
    <td><code>boolean</code></td>
    <td>Site high availability mode. If set to true, the site can have two connectors and runs in high availability mode.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>object</code></td>
    <td>Location of site in latitude and longitude.</td>
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
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Get a specific Site.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-connectorid"><code>connectorid</code></a></td>
    <td>Lists Sites associated with an account. Use connectorid query param to return sites where connectorid matches either site.ConnectorID or site.SecondaryConnectorID.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new Site</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Patch a specific Site.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Update a specific Site.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Remove a specific Site.</td>
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
<tr id="parameter-connectorid">
    <td><CopyableCode code="connectorid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-magic-new-hc-target">
    <td><CopyableCode code="x-magic-new-hc-target" /></td>
    <td><code>boolean</code></td>
    <td>If true, the health check target in the response body will be presented using the new object format. Defaults to false.</td>
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

Get a specific Site.

```sql
SELECT
id,
name,
connector_id,
secondary_connector_id,
description,
ha_mode,
location
FROM cloudflare.magic_transit.sites
WHERE site_id = '{{ site_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND x-magic-new-hc-target = '{{ x-magic-new-hc-target }}'
;
```
</TabItem>
<TabItem value="list">

Lists Sites associated with an account. Use connectorid query param to return sites where connectorid matches either site.ConnectorID or site.SecondaryConnectorID.

```sql
SELECT
id,
name,
connector_id,
secondary_connector_id,
description,
ha_mode,
location
FROM cloudflare.magic_transit.sites
WHERE account_id = '{{ account_id }}' -- required
AND connectorid = '{{ connectorid }}'
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

Creates a new Site

```sql
INSERT INTO cloudflare.magic_transit.sites (
connector_id,
description,
ha_mode,
location,
name,
secondary_connector_id,
account_id
)
SELECT 
'{{ connector_id }}',
'{{ description }}',
{{ ha_mode }},
'{{ location }}',
'{{ name }}' /* required */,
'{{ secondary_connector_id }}',
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
- name: sites
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the sites resource.
    - name: connector_id
      value: "{{ connector_id }}"
      description: |
        Magic Connector identifier tag.
    - name: description
      value: "{{ description }}"
    - name: ha_mode
      value: {{ ha_mode }}
      description: |
        Site high availability mode. If set to true, the site can have two connectors and runs in high availability mode.
    - name: location
      description: |
        Location of site in latitude and longitude.
      value:
        lat: "{{ lat }}"
        lon: "{{ lon }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the site.
    - name: secondary_connector_id
      value: "{{ secondary_connector_id }}"
      description: |
        Magic Connector identifier tag. Used when high availability mode is on.
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

Patch a specific Site.

```sql
UPDATE cloudflare.magic_transit.sites
SET 
connector_id = '{{ connector_id }}',
description = '{{ description }}',
location = '{{ location }}',
name = '{{ name }}',
secondary_connector_id = '{{ secondary_connector_id }}'
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Update a specific Site.

```sql
REPLACE cloudflare.magic_transit.sites
SET 
connector_id = '{{ connector_id }}',
description = '{{ description }}',
location = '{{ location }}',
name = '{{ name }}',
secondary_connector_id = '{{ secondary_connector_id }}'
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Remove a specific Site.

```sql
DELETE FROM cloudflare.magic_transit.sites
WHERE site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
