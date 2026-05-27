--- 
title: downloads
hide_title: false
hide_table_of_contents: false
keywords:
  - downloads
  - streams
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

Creates, updates, deletes, gets or lists a <code>downloads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="downloads" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.downloads" /></td></tr>
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

List downloads response.

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
    <td><CopyableCode code="audio" /></td>
    <td><code>object</code></td>
    <td>The audio-only download. Only present if this download type has been created.</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><code>object</code></td>
    <td>The default video download. Only present if this download type has been created.</td>
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
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists the downloads created for a video.</td>
</tr>
<tr>
    <td><a href="#stream_downloads_create_type_specific_downloads"><CopyableCode code="stream_downloads_create_type_specific_downloads" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-download_type"><code>download_type</code></a></td>
    <td></td>
    <td>Creates a download for a video of specified type. For backwards-compatibility, POST requests to /downloads will enable the default download.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a download for a video when a video is ready to view. Use `/downloads/&#123;download_type&#125;` instead for type-specific downloads. Available types are `default` and `audio`.</td>
</tr>
<tr>
    <td><a href="#stream_downloads_delete_type_specific_downloads"><CopyableCode code="stream_downloads_delete_type_specific_downloads" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-download_type"><code>download_type</code></a></td>
    <td></td>
    <td>Delete specific type of download. For backwards-compatibility, DELETE requests to /downloads will delete the default download.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete the downloads for a video. Use `/downloads/&#123;download_type&#125;` instead for type-specific downloads. Available types are `default` and `audio`.</td>
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
<tr id="parameter-download_type">
    <td><CopyableCode code="download_type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-identifier">
    <td><CopyableCode code="identifier" /></td>
    <td><code>string</code></td>
    <td>Resource identifier.</td>
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

Lists the downloads created for a video.

```sql
SELECT
audio,
default
FROM cloudflare.streams.downloads
WHERE identifier = '{{ identifier }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="stream_downloads_create_type_specific_downloads"
    values={[
        { label: 'stream_downloads_create_type_specific_downloads', value: 'stream_downloads_create_type_specific_downloads' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="stream_downloads_create_type_specific_downloads">

Creates a download for a video of specified type. For backwards-compatibility, POST requests to /downloads will enable the default download.

```sql
INSERT INTO cloudflare.streams.downloads (
identifier,
account_id,
download_type
)
SELECT 
'{{ identifier }}',
'{{ account_id }}',
'{{ download_type }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="create">

Creates a download for a video when a video is ready to view. Use `/downloads/&#123;download_type&#125;` instead for type-specific downloads. Available types are `default` and `audio`.

```sql
INSERT INTO cloudflare.streams.downloads (
identifier,
account_id
)
SELECT 
'{{ identifier }}',
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
- name: downloads
  props:
    - name: identifier
      value: "{{ identifier }}"
      description: Required parameter for the downloads resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the downloads resource.
    - name: download_type
      value: "{{ download_type }}"
      description: Required parameter for the downloads resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="stream_downloads_delete_type_specific_downloads"
    values={[
        { label: 'stream_downloads_delete_type_specific_downloads', value: 'stream_downloads_delete_type_specific_downloads' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="stream_downloads_delete_type_specific_downloads">

Delete specific type of download. For backwards-compatibility, DELETE requests to /downloads will delete the default download.

```sql
DELETE FROM cloudflare.streams.downloads
WHERE identifier = '{{ identifier }}' --required
AND account_id = '{{ account_id }}' --required
AND download_type = '{{ download_type }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete the downloads for a video. Use `/downloads/&#123;download_type&#125;` instead for type-specific downloads. Available types are `default` and `audio`.

```sql
DELETE FROM cloudflare.streams.downloads
WHERE identifier = '{{ identifier }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
