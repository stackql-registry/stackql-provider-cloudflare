--- 
title: zone_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - zone_tags
  - resource_tagging
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

Creates, updates, deletes, gets or lists a <code>zone_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zone_tags" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.resource_tagging.zone_tags" /></td></tr>
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

Get tags for single resource response.

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
    <td>Identifies the unique resource. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Human-readable name of the resource. (example: my-worker-script)</td>
</tr>
<tr>
    <td><CopyableCode code="access_application_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Access application ID is required only for access_application_policy resources (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="worker_id" /></td>
    <td><code>string</code></td>
    <td>Worker ID is required only for worker_version resources (example: 3f72a691-44b3-4c11-8642-c18a88ddaa5e)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>Zone ID is required only for zone-level resources (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>ETag identifier for optimistic concurrency control. Formatted as "v1:&lt;hash&gt;" where the hash is the base64url-encoded SHA-256 (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON Canonicalization Scheme). Clients should treat ETags as opaque strings and pass them back via the If-Match header on write operations. (example: v1:RBNvo1WzZ4oRRq0W9-hkng)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Contains key-value pairs of tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (access_application)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-access_application_id"><code>access_application_id</code></a></td>
    <td>Retrieves tags for a specific zone-level resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates tags for a specific zone-level resource. Replaces all existing tags for the resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Removes all tags from a specific zone-level resource.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag value for optimistic concurrency control. When provided, the server will verify the current resource ETag matches before applying the write. Returns 412 Precondition Failed if the resource has been modified since the ETag was obtained. Omit this header for unconditional writes.</td>
</tr>
<tr id="parameter-access_application_id">
    <td><CopyableCode code="access_application_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Access application ID identifier. Required for access_application_policy resources.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the resource to retrieve tags for.</td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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

Retrieves tags for a specific zone-level resource.

```sql
SELECT
id,
name,
access_application_id,
worker_id,
zone_id,
etag,
tags,
type
FROM cloudflare.resource_tagging.zone_tags
WHERE zone_id = '{{ zone_id }}' -- required
AND resource_id = '{{ resource_id }}'
AND resource_type = '{{ resource_type }}'
AND access_application_id = '{{ access_application_id }}'
;
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

Creates or updates tags for a specific zone-level resource. Replaces all existing tags for the resource.

```sql
REPLACE cloudflare.resource_tagging.zone_tags
SET 
resource_id = '{{ resource_id }}',
resource_type = '{{ resource_type }}',
tags = '{{ tags }}',
access_application_id = '{{ access_application_id }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND resource_id = '{{ resource_id }}' --required
AND resource_type = '{{ resource_type }}' --required
AND If-Match = '{{ If-Match}}'
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

Removes all tags from a specific zone-level resource.

```sql
DELETE FROM cloudflare.resource_tagging.zone_tags
WHERE zone_id = '{{ zone_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
