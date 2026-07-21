--- 
title: images_v1
hide_title: false
hide_table_of_contents: false
keywords:
  - images_v1
  - images
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

Creates, updates, deletes, gets or lists an <code>images_v1</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="images_v1" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.images.images_v1" /></td></tr>
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

Image details response

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
    <td>Image unique identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td>Can set the creator field with an internal user ID. (example: 107b9558-dd06-4bbd-5fef-9c2c16bb7900)</td>
</tr>
<tr>
    <td><CopyableCode code="filename" /></td>
    <td><code>string</code></td>
    <td>Image file name. (example: logo.png)</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>User modifiable key-value store. Can be used for keeping references to another system of record for managing images. Metadata must not exceed 1024 bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="requireSignedURLs" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the image can be a accessed only using it's UID. If set to true, a signed token needs to be generated with a signing key to view the image.</td>
</tr>
<tr>
    <td><CopyableCode code="uploaded" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the media item was uploaded. (example: 2014-01-02T02:20:00.123Z)</td>
</tr>
<tr>
    <td><CopyableCode code="variants" /></td>
    <td><code>array</code></td>
    <td>Object specifying available variants for an image.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List images response

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
    <td>Image unique identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td>Can set the creator field with an internal user ID. (example: 107b9558-dd06-4bbd-5fef-9c2c16bb7900)</td>
</tr>
<tr>
    <td><CopyableCode code="filename" /></td>
    <td><code>string</code></td>
    <td>Image file name. (example: logo.png)</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>User modifiable key-value store. Can be used for keeping references to another system of record for managing images. Metadata must not exceed 1024 bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="requireSignedURLs" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the image can be a accessed only using it's UID. If set to true, a signed token needs to be generated with a signing key to view the image.</td>
</tr>
<tr>
    <td><CopyableCode code="uploaded" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the media item was uploaded. (example: 2014-01-02T02:20:00.123Z)</td>
</tr>
<tr>
    <td><CopyableCode code="variants" /></td>
    <td><code>array</code></td>
    <td>Object specifying available variants for an image.</td>
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
    <td><a href="#parameter-image_id"><code>image_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch details for a single image.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-creator"><code>creator</code></a></td>
    <td>List up to 100 images with one request. Use the optional parameters below to get a specific range of images.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Upload an image with up to 10 Megabytes using a single HTTP POST (multipart/form-data) request. An image can be uploaded by sending an image file or passing an accessible to an API url.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-image_id"><code>image_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Update image access control. On access control change, all copies of the image are purged from cache.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-image_id"><code>image_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete an image on Cloudflare Images. On success, all copies of the image are deleted and purged from cache.</td>
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
<tr id="parameter-image_id">
    <td><CopyableCode code="image_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-creator">
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
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

Fetch details for a single image.

```sql
SELECT
id,
creator,
filename,
meta,
requireSignedURLs,
uploaded,
variants
FROM cloudflare.images.images_v1
WHERE image_id = '{{ image_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List up to 100 images with one request. Use the optional parameters below to get a specific range of images.

```sql
SELECT
id,
creator,
filename,
meta,
requireSignedURLs,
uploaded,
variants
FROM cloudflare.images.images_v1
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND creator = '{{ creator }}'
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

Upload an image with up to 10 Megabytes using a single HTTP POST (multipart/form-data) request. An image can be uploaded by sending an image file or passing an accessible to an API url.

```sql
INSERT INTO cloudflare.images.images_v1 (
creator,
file,
id,
metadata,
requireSignedURLs,
url,
account_id
)
SELECT 
'{{ creator }}',
'{{ file }}',
'{{ id }}',
'{{ metadata }}',
{{ requireSignedURLs }},
'{{ url }}',
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
- name: images_v1
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the images_v1 resource.
    - name: creator
      value: "{{ creator }}"
      description: |
        Can set the creator field with an internal user ID.
    - name: file
      value: "{{ file }}"
      description: |
        An image binary data. Only needed when type is uploading a file.
    - name: id
      value: "{{ id }}"
      description: |
        An optional custom unique identifier for your image.
    - name: metadata
      value: "{{ metadata }}"
      description: |
        User modifiable key-value store. Can use used for keeping references to another system of record for managing images.
    - name: requireSignedURLs
      value: {{ requireSignedURLs }}
      description: |
        Indicates whether the image requires a signature token for the access.
      default: false
    - name: url
      value: "{{ url }}"
      description: |
        A URL to fetch an image from origin. Only needed when type is uploading from a URL.
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

Update image access control. On access control change, all copies of the image are purged from cache.

```sql
UPDATE cloudflare.images.images_v1
SET 
creator = '{{ creator }}',
metadata = '{{ metadata }}',
requireSignedURLs = {{ requireSignedURLs }}
WHERE 
image_id = '{{ image_id }}' --required
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

Delete an image on Cloudflare Images. On success, all copies of the image are deleted and purged from cache.

```sql
DELETE FROM cloudflare.images.images_v1
WHERE image_id = '{{ image_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
