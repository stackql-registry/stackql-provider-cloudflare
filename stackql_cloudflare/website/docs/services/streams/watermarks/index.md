--- 
title: watermarks
hide_title: false
hide_table_of_contents: false
keywords:
  - watermarks
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

Creates, updates, deletes, gets or lists a <code>watermarks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="watermarks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.watermarks" /></td></tr>
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

Watermark profile details response.

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
    <td>A short description of the watermark profile. (default: , example: Marketing Videos)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and a time a watermark profile was created. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="downloadedFrom" /></td>
    <td><code>string</code></td>
    <td>The source URL for a downloaded image. If the watermark profile was created via direct upload, this field is null. (example: https://company.com/logo.png)</td>
</tr>
<tr>
    <td><CopyableCode code="height" /></td>
    <td><code>integer</code></td>
    <td>The height of the image in pixels.</td>
</tr>
<tr>
    <td><CopyableCode code="opacity" /></td>
    <td><code>number</code></td>
    <td>The translucency of the image. A value of `0.0` makes the image completely transparent, and `1.0` makes the image completely opaque. Note that if the image is already semi-transparent, setting this to `1.0` will not make the image completely opaque.</td>
</tr>
<tr>
    <td><CopyableCode code="padding" /></td>
    <td><code>number</code></td>
    <td>The whitespace between the adjacent edges (determined by position) of the video and the image. `0.0` indicates no padding, and `1.0` indicates a fully padded video width or length, as determined by the algorithm.</td>
</tr>
<tr>
    <td><CopyableCode code="position" /></td>
    <td><code>string</code></td>
    <td>The location of the image. Valid positions are: `upperRight`, `upperLeft`, `lowerLeft`, `lowerRight`, and `center`. Note that `center` ignores the `padding` parameter. (default: upperRight, example: center)</td>
</tr>
<tr>
    <td><CopyableCode code="scale" /></td>
    <td><code>number</code></td>
    <td>The size of the image relative to the overall size of the video. This parameter will adapt to horizontal and vertical videos automatically. `0.0` indicates no scaling (use the size of the image as-is), and `1.0 `fills the entire video.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>number</code></td>
    <td>The size of the image in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for a watermark profile. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="width" /></td>
    <td><code>integer</code></td>
    <td>The width of the image in pixels.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List watermark profiles response.

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
    <td>A short description of the watermark profile. (default: , example: Marketing Videos)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and a time a watermark profile was created. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="downloadedFrom" /></td>
    <td><code>string</code></td>
    <td>The source URL for a downloaded image. If the watermark profile was created via direct upload, this field is null. (example: https://company.com/logo.png)</td>
</tr>
<tr>
    <td><CopyableCode code="height" /></td>
    <td><code>integer</code></td>
    <td>The height of the image in pixels.</td>
</tr>
<tr>
    <td><CopyableCode code="opacity" /></td>
    <td><code>number</code></td>
    <td>The translucency of the image. A value of `0.0` makes the image completely transparent, and `1.0` makes the image completely opaque. Note that if the image is already semi-transparent, setting this to `1.0` will not make the image completely opaque.</td>
</tr>
<tr>
    <td><CopyableCode code="padding" /></td>
    <td><code>number</code></td>
    <td>The whitespace between the adjacent edges (determined by position) of the video and the image. `0.0` indicates no padding, and `1.0` indicates a fully padded video width or length, as determined by the algorithm.</td>
</tr>
<tr>
    <td><CopyableCode code="position" /></td>
    <td><code>string</code></td>
    <td>The location of the image. Valid positions are: `upperRight`, `upperLeft`, `lowerLeft`, `lowerRight`, and `center`. Note that `center` ignores the `padding` parameter. (default: upperRight, example: center)</td>
</tr>
<tr>
    <td><CopyableCode code="scale" /></td>
    <td><code>number</code></td>
    <td>The size of the image relative to the overall size of the video. This parameter will adapt to horizontal and vertical videos automatically. `0.0` indicates no scaling (use the size of the image as-is), and `1.0 `fills the entire video.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>number</code></td>
    <td>The size of the image in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for a watermark profile. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="width" /></td>
    <td><code>integer</code></td>
    <td>The width of the image in pixels.</td>
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
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves details for a single watermark profile.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all watermark profiles for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates watermark profiles using a single `HTTP POST multipart/form-data` request.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a watermark profile.</td>
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
<tr id="parameter-identifier">
    <td><CopyableCode code="identifier" /></td>
    <td><code>string</code></td>
    <td>Resource identifier.</td>
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

Retrieves details for a single watermark profile.

```sql
SELECT
name,
created,
downloadedFrom,
height,
opacity,
padding,
position,
scale,
size,
uid,
width
FROM cloudflare.streams.watermarks
WHERE identifier = '{{ identifier }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all watermark profiles for an account.

```sql
SELECT
name,
created,
downloadedFrom,
height,
opacity,
padding,
position,
scale,
size,
uid,
width
FROM cloudflare.streams.watermarks
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

Creates watermark profiles using a single `HTTP POST multipart/form-data` request.

```sql
INSERT INTO cloudflare.streams.watermarks (
name,
opacity,
padding,
position,
scale,
url,
account_id
)
SELECT 
'{{ name }}',
{{ opacity }},
{{ padding }},
'{{ position }}',
{{ scale }},
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
- name: watermarks
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the watermarks resource.
    - name: name
      value: "{{ name }}"
      description: |
        A short description of the watermark profile.
      default: 
    - name: opacity
      value: {{ opacity }}
      description: |
        The translucency of the image. A value of \`0.0\` makes the image completely transparent, and \`1.0\` makes the image completely opaque. Note that if the image is already semi-transparent, setting this to \`1.0\` will not make the image completely opaque.
      default: 1
    - name: padding
      value: {{ padding }}
      description: |
        The whitespace between the adjacent edges (determined by position) of the video and the image. \`0.0\` indicates no padding, and \`1.0\` indicates a fully padded video width or length, as determined by the algorithm.
      default: 0.05
    - name: position
      value: "{{ position }}"
      description: |
        The location of the image. Valid positions are: \`upperRight\`, \`upperLeft\`, \`lowerLeft\`, \`lowerRight\`, and \`center\`. Note that \`center\` ignores the \`padding\` parameter.
      default: upperRight
    - name: scale
      value: {{ scale }}
      description: |
        The size of the image relative to the overall size of the video. This parameter will adapt to horizontal and vertical videos automatically. \`0.0\` indicates no scaling (use the size of the image as-is), and \`1.0 \`fills the entire video.
      default: 0.15
    - name: url
      value: "{{ url }}"
      description: |
        URL of the watermark image to copy.
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

Deletes a watermark profile.

```sql
DELETE FROM cloudflare.streams.watermarks
WHERE identifier = '{{ identifier }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
