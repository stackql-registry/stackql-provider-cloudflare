--- 
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.resource_tagging.resources" /></td></tr>
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

List tagged resources response.

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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-tag"><code>tag</code></a>, <a href="#parameter-cursor"><code>cursor</code></a></td>
    <td>Lists all tagged resources for an account.</td>
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
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Cursor for pagination.</td>
</tr>
<tr id="parameter-tag">
    <td><CopyableCode code="tag" /></td>
    <td><code>array</code></td>
    <td>Filter resources by tag criteria. This parameter can be repeated multiple times, with AND logic between parameters. Supported syntax: - **Key-only**: `tag=<key>` - Resource must have the tag key (e.g., `tag=production`) - **Key-value**: `tag=<key>=<value>` - Resource must have the tag with specific value (e.g., `tag=env=prod`) - **Multiple values (OR)**: `tag=<key>=<v1>,<v2>` - Resource must have tag with any of the values (e.g., `tag=env=prod,staging`) - **Negate key-only**: `tag=!<key>` - Resource must not have the tag key (e.g., `tag=!archived`) - **Negate key-value**: `tag=<key>!=<value>` - Resource must not have the tag with specific value (e.g., `tag=region!=us-west-1`) Multiple tag parameters are combined with AND logic.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>array</code></td>
    <td>Filter by resource type. Can be repeated to filter by multiple types (OR logic). Example: ?type=zone&type=worker</td>
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

Lists all tagged resources for an account.

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
FROM cloudflare.resource_tagging.resources
WHERE account_id = '{{ account_id }}' -- required
AND type = '{{ type }}'
AND tag = '{{ tag }}'
AND cursor = '{{ cursor }}'
;
```
</TabItem>
</Tabs>
