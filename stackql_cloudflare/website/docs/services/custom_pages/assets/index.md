--- 
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - custom_pages
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

Creates, updates, deletes, gets or lists an <code>assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.custom_pages.assets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get a custom asset response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_). (example: my_custom_error_page)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short description of the custom asset. (example: Custom 500 error page)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="size_bytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the asset content in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL where the asset content is fetched from. (example: https://example.com/error.html)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get a custom asset response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_). (example: my_custom_error_page)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short description of the custom asset. (example: Custom 500 error page)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="size_bytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the asset content in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL where the asset content is fetched from. (example: https://example.com/error.html)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List custom assets response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_). (example: my_custom_error_page)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short description of the custom asset. (example: Custom 500 error page)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="size_bytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the asset content in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL where the asset content is fetched from. (example: https://example.com/error.html)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List custom assets response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_). (example: my_custom_error_page)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short description of the custom asset. (example: Custom 500 error page)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="size_bytes" /></td>
    <td><code>integer</code></td>
    <td>The size of the asset content in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL where the asset content is fetched from. (example: https://example.com/error.html)</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asset_name"><code>asset_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the details of a custom asset.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asset_name"><code>asset_name</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a custom asset.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetches all the custom assets.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetches all the custom assets.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Creates a new custom asset.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Creates a new custom asset.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-asset_name"><code>asset_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Updates the configuration of an existing custom asset.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-asset_name"><code>asset_name</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Updates the configuration of an existing custom asset.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-asset_name"><code>asset_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an existing custom asset.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-asset_name"><code>asset_name</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing custom asset.</td>
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
<tr id="parameter-asset_name">
    <td><CopyableCode code="asset_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches the details of a custom asset.

```sql
SELECT
name,
description,
last_updated,
size_bytes,
url
FROM cloudflare.custom_pages.assets
WHERE asset_name = '{{ asset_name }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches the details of a custom asset.

```sql
SELECT
name,
description,
last_updated,
size_bytes,
url
FROM cloudflare.custom_pages.assets
WHERE asset_name = '{{ asset_name }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Fetches all the custom assets.

```sql
SELECT
name,
description,
last_updated,
size_bytes,
url
FROM cloudflare.custom_pages.assets
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Fetches all the custom assets.

```sql
SELECT
name,
description,
last_updated,
size_bytes,
url
FROM cloudflare.custom_pages.assets
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'create_by_zone', value: 'create_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Creates a new custom asset.

```sql
INSERT INTO cloudflare.custom_pages.assets (
description,
name,
url,
account_id
)
SELECT 
'{{ description }}' /* required */,
'{{ name }}' /* required */,
'{{ url }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="create_by_zone">

Creates a new custom asset.

```sql
INSERT INTO cloudflare.custom_pages.assets (
description,
name,
url,
zone_id
)
SELECT 
'{{ description }}' /* required */,
'{{ name }}' /* required */,
'{{ url }}' /* required */,
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
- name: assets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the assets resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the assets resource.
    - name: description
      value: "{{ description }}"
      description: |
        A short description of the custom asset.
    - name: name
      value: "{{ name }}"
      description: |
        The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_).
    - name: url
      value: "{{ url }}"
      description: |
        The URL where the asset content is fetched from.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' },
        { label: 'update_by_zone', value: 'update_by_zone' }
    ]}
>
<TabItem value="update_by_account">

Updates the configuration of an existing custom asset.

```sql
REPLACE cloudflare.custom_pages.assets
SET 
description = '{{ description }}',
url = '{{ url }}'
WHERE 
asset_name = '{{ asset_name }}' --required
AND account_id = '{{ account_id }}' --required
AND description = '{{ description }}' --required
AND url = '{{ url }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates the configuration of an existing custom asset.

```sql
REPLACE cloudflare.custom_pages.assets
SET 
description = '{{ description }}',
url = '{{ url }}'
WHERE 
asset_name = '{{ asset_name }}' --required
AND zone_id = '{{ zone_id }}' --required
AND description = '{{ description }}' --required
AND url = '{{ url }}' --required
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
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' },
        { label: 'delete_by_zone', value: 'delete_by_zone' }
    ]}
>
<TabItem value="delete_by_account">

Deletes an existing custom asset.

```sql
DELETE FROM cloudflare.custom_pages.assets
WHERE asset_name = '{{ asset_name }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an existing custom asset.

```sql
DELETE FROM cloudflare.custom_pages.assets
WHERE asset_name = '{{ asset_name }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
