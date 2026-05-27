--- 
title: origin_cloud_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_cloud_regions
  - cache
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

Creates, updates, deletes, gets or lists an <code>origin_cloud_regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="origin_cloud_regions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cache.origin_cloud_regions" /></td></tr>
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

Get origin cloud region mapping response.

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
    <td> (origin_public_cloud_region) (example: origin_public_cloud_region)</td>
</tr>
<tr>
    <td><CopyableCode code="editable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the setting can be modified by the current user.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the mapping was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>object</code></td>
    <td>A single origin IP-to-cloud-region mapping.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List origin cloud region mappings response.

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
    <td> (origin_public_cloud_region) (example: origin_public_cloud_region)</td>
</tr>
<tr>
    <td><CopyableCode code="editable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the setting can be modified by the current user.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the mapping set was last modified. Null when no mappings exist.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-origin_ip"><code>origin_ip</code></a></td>
    <td></td>
    <td>Returns the cloud region mapping for a single origin IP address. The IP path parameter is normalized before lookup (RFC 5952 for IPv6). Returns 404 (code 1142) if the zone has no mappings or if the specified IP has no mapping.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Returns all IP-to-cloud-region mappings configured for the zone. Each mapping tells Cloudflare which cloud vendor and region hosts the origin at that IP, enabling the edge to route via the nearest Tiered Cache upper-tier co-located with that cloud provider. Returns an empty array when no mappings exist.</td>
</tr>
<tr>
    <td><a href="#origin_cloud_regions_create"><CopyableCode code="origin_cloud_regions_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-ip"><code>ip</code></a>, <a href="#parameter-vendor"><code>vendor</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td></td>
    <td>Adds a single IP-to-cloud-region mapping for the zone. The IP must be a valid IPv4 or IPv6 address and is normalized to canonical form before storage (RFC 5952 for IPv6). Returns 400 (code 1145) if a mapping for that IP already exists — use PATCH to update an existing entry. The vendor and region are validated against the list from `GET /zones/&#123;zone_id&#125;/cache/origin_cloud_regions/supported_regions`.</td>
</tr>
<tr>
    <td><a href="#origin_cloud_regions_upsert"><CopyableCode code="origin_cloud_regions_upsert" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-ip"><code>ip</code></a>, <a href="#parameter-vendor"><code>vendor</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td></td>
    <td>Adds or updates a single IP-to-cloud-region mapping for the zone. Unlike POST, this operation is idempotent — if a mapping for the IP already exists it is overwritten. Returns the complete updated list of all mappings for the zone. Returns 403 (code 1164) when the zone has reached the limit of 3,500 IP mappings.</td>
</tr>
<tr>
    <td><a href="#origin_cloud_regions_delete"><CopyableCode code="origin_cloud_regions_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-origin_ip"><code>origin_ip</code></a></td>
    <td></td>
    <td>Removes the cloud region mapping for a single origin IP address. The IP path parameter is normalized before lookup. Returns the deleted entry on success. Returns 404 (code 1163) if no mapping exists for the specified IP. When the last mapping for the zone is removed the underlying rule record is also deleted.</td>
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
<tr id="parameter-origin_ip">
    <td><CopyableCode code="origin_ip" /></td>
    <td><code>string</code></td>
    <td>Origin IP address whose mapping should be deleted.</td>
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

Returns the cloud region mapping for a single origin IP address. The IP path parameter is normalized before lookup (RFC 5952 for IPv6). Returns 404 (code 1142) if the zone has no mappings or if the specified IP has no mapping.

```sql
SELECT
id,
editable,
modified_on,
value
FROM cloudflare.cache.origin_cloud_regions
WHERE zone_id = '{{ zone_id }}' -- required
AND origin_ip = '{{ origin_ip }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all IP-to-cloud-region mappings configured for the zone. Each mapping tells Cloudflare which cloud vendor and region hosts the origin at that IP, enabling the edge to route via the nearest Tiered Cache upper-tier co-located with that cloud provider. Returns an empty array when no mappings exist.

```sql
SELECT
id,
editable,
modified_on,
value
FROM cloudflare.cache.origin_cloud_regions
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="origin_cloud_regions_create"
    values={[
        { label: 'origin_cloud_regions_create', value: 'origin_cloud_regions_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="origin_cloud_regions_create">

Adds a single IP-to-cloud-region mapping for the zone. The IP must be a valid IPv4 or IPv6 address and is normalized to canonical form before storage (RFC 5952 for IPv6). Returns 400 (code 1145) if a mapping for that IP already exists — use PATCH to update an existing entry. The vendor and region are validated against the list from `GET /zones/&#123;zone_id&#125;/cache/origin_cloud_regions/supported_regions`.

```sql
INSERT INTO cloudflare.cache.origin_cloud_regions (
ip,
region,
vendor,
zone_id
)
SELECT 
'{{ ip }}' /* required */,
'{{ region }}' /* required */,
'{{ vendor }}' /* required */,
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
- name: origin_cloud_regions
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the origin_cloud_regions resource.
    - name: ip
      value: "{{ ip }}"
      description: |
        Origin IP address (IPv4 or IPv6). Normalized to canonical form before storage (RFC 5952 for IPv6).
    - name: region
      value: "{{ region }}"
      description: |
        Cloud vendor region identifier. Must be a valid region for the specified vendor as returned by the supported_regions endpoint.
    - name: vendor
      value: "{{ vendor }}"
      description: |
        Cloud vendor hosting the origin. Must be one of the supported vendors.
      valid_values: ['aws', 'azure', 'gcp', 'oci']
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="origin_cloud_regions_upsert"
    values={[
        { label: 'origin_cloud_regions_upsert', value: 'origin_cloud_regions_upsert' }
    ]}
>
<TabItem value="origin_cloud_regions_upsert">

Adds or updates a single IP-to-cloud-region mapping for the zone. Unlike POST, this operation is idempotent — if a mapping for the IP already exists it is overwritten. Returns the complete updated list of all mappings for the zone. Returns 403 (code 1164) when the zone has reached the limit of 3,500 IP mappings.

```sql
UPDATE cloudflare.cache.origin_cloud_regions
SET 
ip = '{{ ip }}',
region = '{{ region }}',
vendor = '{{ vendor }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND ip = '{{ ip }}' --required
AND vendor = '{{ vendor }}' --required
AND region = '{{ region }}' --required
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
    defaultValue="origin_cloud_regions_delete"
    values={[
        { label: 'origin_cloud_regions_delete', value: 'origin_cloud_regions_delete' }
    ]}
>
<TabItem value="origin_cloud_regions_delete">

Removes the cloud region mapping for a single origin IP address. The IP path parameter is normalized before lookup. Returns the deleted entry on success. Returns 404 (code 1163) if no mapping exists for the specified IP. When the last mapping for the zone is removed the underlying rule record is also deleted.

```sql
DELETE FROM cloudflare.cache.origin_cloud_regions
WHERE zone_id = '{{ zone_id }}' --required
AND origin_ip = '{{ origin_ip }}' --required
;
```
</TabItem>
</Tabs>
