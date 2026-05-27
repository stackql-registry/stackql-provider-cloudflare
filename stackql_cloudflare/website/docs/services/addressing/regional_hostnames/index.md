--- 
title: regional_hostnames
hide_title: false
hide_table_of_contents: false
keywords:
  - regional_hostnames
  - addressing
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

Creates, updates, deletes, gets or lists a <code>regional_hostnames</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="regional_hostnames" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.regional_hostnames" /></td></tr>
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

Fetch hostname response

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
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the regional hostname was created (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g `*.example.com` (example: foo.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="region_key" /></td>
    <td><code>string</code></td>
    <td>Identifying key for the region (example: ca)</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>string</code></td>
    <td>Configure which routing method to use for the regional hostname (default: dns, example: dns)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List hostnames response

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
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the regional hostname was created (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g `*.example.com` (example: foo.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="region_key" /></td>
    <td><code>string</code></td>
    <td>Identifying key for the region (example: ca)</td>
</tr>
<tr>
    <td><CopyableCode code="routing" /></td>
    <td><code>string</code></td>
    <td>Configure which routing method to use for the regional hostname (default: dns, example: dns)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a></td>
    <td></td>
    <td>Fetch the configuration for a specific Regional Hostname, within a zone.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>List all Regional Hostnames within a zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-region_key"><code>region_key</code></a></td>
    <td></td>
    <td>Create a new Regional Hostname entry. Cloudflare will only use data centers that are physically located within the chosen region to decrypt and service HTTPS traffic. Learn more about [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/get-started/).</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-region_key"><code>region_key</code></a></td>
    <td></td>
    <td>Update the configuration for a specific Regional Hostname. Only the region_key of a hostname is mutable.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a></td>
    <td></td>
    <td>Delete the region configuration for a specific Regional Hostname.</td>
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
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Fetch the configuration for a specific Regional Hostname, within a zone.

```sql
SELECT
created_on,
hostname,
region_key,
routing
FROM cloudflare.addressing.regional_hostnames
WHERE zone_id = '{{ zone_id }}' -- required
AND hostname = '{{ hostname }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Regional Hostnames within a zone.

```sql
SELECT
created_on,
hostname,
region_key,
routing
FROM cloudflare.addressing.regional_hostnames
WHERE zone_id = '{{ zone_id }}' -- required
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

Create a new Regional Hostname entry. Cloudflare will only use data centers that are physically located within the chosen region to decrypt and service HTTPS traffic. Learn more about [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/get-started/).

```sql
INSERT INTO cloudflare.addressing.regional_hostnames (
hostname,
region_key,
routing,
zone_id
)
SELECT 
'{{ hostname }}' /* required */,
'{{ region_key }}' /* required */,
'{{ routing }}',
'{{ zone_id }}'
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
- name: regional_hostnames
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the regional_hostnames resource.
    - name: hostname
      value: "{{ hostname }}"
      description: |
        DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g \`*.example.com\`
    - name: region_key
      value: "{{ region_key }}"
      description: |
        Identifying key for the region
    - name: routing
      value: "{{ routing }}"
      description: |
        Configure which routing method to use for the regional hostname
      default: dns
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

Update the configuration for a specific Regional Hostname. Only the region_key of a hostname is mutable.

```sql
UPDATE cloudflare.addressing.regional_hostnames
SET 
region_key = '{{ region_key }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND hostname = '{{ hostname }}' --required
AND region_key = '{{ region_key }}' --required
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

Delete the region configuration for a specific Regional Hostname.

```sql
DELETE FROM cloudflare.addressing.regional_hostnames
WHERE zone_id = '{{ zone_id }}' --required
AND hostname = '{{ hostname }}' --required
;
```
</TabItem>
</Tabs>
