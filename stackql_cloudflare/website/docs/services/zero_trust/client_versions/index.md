--- 
title: client_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - client_versions
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

Creates, updates, deletes, gets or lists a <code>client_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="client_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.client_versions" /></td></tr>
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

List client versions response.

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
    <td><CopyableCode code="package_size" /></td>
    <td><code>integer (int64)</code></td>
    <td>Size of the package in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="package_url" /></td>
    <td><code>string</code></td>
    <td>URL to download the package. (example: https://downloads.cloudflareclient.com/v1/download/windows/version/2024.11.309.0)</td>
</tr>
<tr>
    <td><CopyableCode code="release_date" /></td>
    <td><code>string</code></td>
    <td>The release date timestamp. (example: 2024-11-18T21:57:58.478Z)</td>
</tr>
<tr>
    <td><CopyableCode code="release_notes" /></td>
    <td><code>string</code></td>
    <td>Release notes for this version. (example: This release contains minor fixes and improvements.)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The client version string. (example: 2024.11.309.0)</td>
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
    <td><a href="#parameter-target_environment"><code>target_environment</code></a>, <a href="#parameter-release_track"><code>release_track</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists available WARP client versions for a specific target environment and release track. This endpoint is in Beta.</td>
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
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>The page number to return.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of versions to return per page.</td>
</tr>
<tr id="parameter-release_track">
    <td><CopyableCode code="release_track" /></td>
    <td><code>string</code></td>
    <td>The release track (ga for General Availability, beta for Beta releases).</td>
</tr>
<tr id="parameter-target_environment">
    <td><CopyableCode code="target_environment" /></td>
    <td><code>string</code></td>
    <td>The target environment for the client version (e.g., windows, macos).</td>
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

Lists available WARP client versions for a specific target environment and release track. This endpoint is in Beta.

```sql
SELECT
package_size,
package_url,
release_date,
release_notes,
version
FROM cloudflare.zero_trust.client_versions
WHERE account_id = '{{ account_id }}' -- required
AND target_environment = '{{ target_environment }}'
AND release_track = '{{ release_track }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>
