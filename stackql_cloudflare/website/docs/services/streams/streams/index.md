--- 
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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

Creates, updates, deletes, gets or lists a <code>streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="streams" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.streams" /></td></tr>
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

Retrieve video details response.

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
    <td><CopyableCode code="allowedOrigins" /></td>
    <td><code>array</code></td>
    <td>Lists the origins allowed to display the video. Enter allowed origin domains in an array and use `*` for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.</td>
</tr>
<tr>
    <td><CopyableCode code="clippedFrom" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the source video this video was clipped from. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the media item was created. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td>A user-defined identifier for the media creator. (example: creator-id_abcde12345)</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>number</code></td>
    <td>The duration of the video in seconds. A value of `-1` means the duration is unknown. The duration becomes available after the upload and before the video is ready.</td>
</tr>
<tr>
    <td><CopyableCode code="input" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="liveInput" /></td>
    <td><code>string</code></td>
    <td>The live input ID used to upload a video with Stream Live. (example: fc0a8dc887b16759bfd9ad922230a014)</td>
</tr>
<tr>
    <td><CopyableCode code="maxDurationSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum duration in seconds for a video upload. Can be set for a video that is not yet uploaded to limit its duration. Uploads that exceed the specified duration will fail during processing. A value of `-1` means the value is unknown.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>The maximum size in bytes for the video upload.</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>A user modifiable key-value store used to reference other systems of record for managing videos.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the media item was last modified. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="playback" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>string (uri)</code></td>
    <td>The video's preview page URI. This field is omitted until encoding is complete. (example: https://customer-m033z5x00ks6nunl.cloudflarestream.com/ea95132c15732412d22c1476fa83f27a/watch)</td>
</tr>
<tr>
    <td><CopyableCode code="publicDetails" /></td>
    <td><code>object</code></td>
    <td>Public details for the video including title, share link, channel link, and logo.</td>
</tr>
<tr>
    <td><CopyableCode code="readyToStream" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the video is playable. The field is empty if the video is not ready for viewing or the live stream is still in progress.</td>
</tr>
<tr>
    <td><CopyableCode code="readyToStreamAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the time at which the video became playable. The field is empty if the video is not ready for viewing or the live stream is still in progress. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="requireSignedURLs" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the video can be a accessed using the UID. When set to `true`, a signed token must be generated with a signing key to view the video.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledDeletion" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the date and time at which the video will be deleted. Omit the field to indicate no change, or include with a `null` value to remove an existing scheduled deletion. If specified, must be at least 30 days from upload time. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>number</code></td>
    <td>The size of the media item in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Specifies a detailed status for a video. If the `state` is `inprogress` or `error`, the `step` field returns `encoding` or `manifest`. If the `state` is `inprogress`, `pctComplete` returns a number between 0 and 100 to indicate the approximate percent of completion. If the `state` is `error`, `errorReasonCode` and `errorReasonText` provide additional details.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbnail" /></td>
    <td><code>string (uri)</code></td>
    <td>The media item's thumbnail URI. This field is omitted until encoding is complete. (example: https://customer-m033z5x00ks6nunl.cloudflarestream.com/ea95132c15732412d22c1476fa83f27a/thumbnails/thumbnail.jpg)</td>
</tr>
<tr>
    <td><CopyableCode code="thumbnailTimestampPct" /></td>
    <td><code>number</code></td>
    <td>The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video. If this value is not set, the default thumbnail image is taken from 0s of the video.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>A Cloudflare-generated unique identifier for a media item. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="uploadExpiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the video upload URL is no longer valid for direct user uploads. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="uploaded" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the media item was uploaded. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="watermark" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List videos response.

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
    <td><CopyableCode code="allowedOrigins" /></td>
    <td><code>array</code></td>
    <td>Lists the origins allowed to display the video. Enter allowed origin domains in an array and use `*` for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.</td>
</tr>
<tr>
    <td><CopyableCode code="clippedFrom" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the source video this video was clipped from. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the media item was created. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td>A user-defined identifier for the media creator. (example: creator-id_abcde12345)</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>number</code></td>
    <td>The duration of the video in seconds. A value of `-1` means the duration is unknown. The duration becomes available after the upload and before the video is ready.</td>
</tr>
<tr>
    <td><CopyableCode code="input" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="liveInput" /></td>
    <td><code>string</code></td>
    <td>The live input ID used to upload a video with Stream Live. (example: fc0a8dc887b16759bfd9ad922230a014)</td>
</tr>
<tr>
    <td><CopyableCode code="maxDurationSeconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum duration in seconds for a video upload. Can be set for a video that is not yet uploaded to limit its duration. Uploads that exceed the specified duration will fail during processing. A value of `-1` means the value is unknown.</td>
</tr>
<tr>
    <td><CopyableCode code="maxSizeBytes" /></td>
    <td><code>integer (int64)</code></td>
    <td>The maximum size in bytes for the video upload.</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>A user modifiable key-value store used to reference other systems of record for managing videos.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the media item was last modified. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="playback" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="preview" /></td>
    <td><code>string (uri)</code></td>
    <td>The video's preview page URI. This field is omitted until encoding is complete. (example: https://customer-m033z5x00ks6nunl.cloudflarestream.com/ea95132c15732412d22c1476fa83f27a/watch)</td>
</tr>
<tr>
    <td><CopyableCode code="publicDetails" /></td>
    <td><code>object</code></td>
    <td>Public details for the video including title, share link, channel link, and logo.</td>
</tr>
<tr>
    <td><CopyableCode code="readyToStream" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the video is playable. The field is empty if the video is not ready for viewing or the live stream is still in progress.</td>
</tr>
<tr>
    <td><CopyableCode code="readyToStreamAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the time at which the video became playable. The field is empty if the video is not ready for viewing or the live stream is still in progress. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="requireSignedURLs" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the video can be a accessed using the UID. When set to `true`, a signed token must be generated with a signing key to view the video.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledDeletion" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the date and time at which the video will be deleted. Omit the field to indicate no change, or include with a `null` value to remove an existing scheduled deletion. If specified, must be at least 30 days from upload time. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>number</code></td>
    <td>The size of the media item in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Specifies a detailed status for a video. If the `state` is `inprogress` or `error`, the `step` field returns `encoding` or `manifest`. If the `state` is `inprogress`, `pctComplete` returns a number between 0 and 100 to indicate the approximate percent of completion. If the `state` is `error`, `errorReasonCode` and `errorReasonText` provide additional details.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbnail" /></td>
    <td><code>string (uri)</code></td>
    <td>The media item's thumbnail URI. This field is omitted until encoding is complete. (example: https://customer-m033z5x00ks6nunl.cloudflarestream.com/ea95132c15732412d22c1476fa83f27a/thumbnails/thumbnail.jpg)</td>
</tr>
<tr>
    <td><CopyableCode code="thumbnailTimestampPct" /></td>
    <td><code>number</code></td>
    <td>The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video. If this value is not set, the default thumbnail image is taken from 0s of the video.</td>
</tr>
<tr>
    <td><CopyableCode code="uid" /></td>
    <td><code>string</code></td>
    <td>A Cloudflare-generated unique identifier for a media item. (example: ea95132c15732412d22c1476fa83f27a)</td>
</tr>
<tr>
    <td><CopyableCode code="uploadExpiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the video upload URL is no longer valid for direct user uploads. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="uploaded" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the media item was uploaded. (example: 2014-01-02T02:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="watermark" /></td>
    <td><code>object</code></td>
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
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches details for a single video.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-creator"><code>creator</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-asc"><code>asc</code></a>, <a href="#parameter-video_name"><code>video_name</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-start"><code>start</code></a>, <a href="#parameter-end"><code>end</code></a>, <a href="#parameter-include_counts"><code>include_counts</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-live_input_id"><code>live_input_id</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>Lists up to 1000 videos from a single request. For a specific range, refer to the optional parameters.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Edit details for a single video.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-Tus-Resumable"><code>Tus-Resumable</code></a>, <a href="#parameter-Upload-Creator"><code>Upload-Creator</code></a>, <a href="#parameter-Upload-Length"><code>Upload-Length</code></a>, <a href="#parameter-Upload-Metadata"><code>Upload-Metadata</code></a>, <a href="#parameter-direct_user"><code>direct_user</code></a></td>
    <td>Initiates a video upload using the TUS protocol. On success, the server responds with a status code 201 (created) and includes a `location` header to indicate where the content should be uploaded. Refer to https://tus.io for protocol details.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a video and its copies from Cloudflare Stream.</td>
</tr>
<tr>
    <td><a href="#create_clip"><CopyableCode code="create_clip" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-clippedFromVideoUID"><code>clippedFromVideoUID</code></a>, <a href="#parameter-startTimeSeconds"><code>startTimeSeconds</code></a>, <a href="#parameter-endTimeSeconds"><code>endTimeSeconds</code></a></td>
    <td></td>
    <td>Clips a video based on the specified start and end times provided in seconds.</td>
</tr>
<tr>
    <td><a href="#copy"><CopyableCode code="copy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-Upload-Creator"><code>Upload-Creator</code></a></td>
    <td>Uploads a video to Stream from a provided URL.</td>
</tr>
<tr>
    <td><a href="#create_direct_upload"><CopyableCode code="create_direct_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-maxDurationSeconds"><code>maxDurationSeconds</code></a></td>
    <td><a href="#parameter-Upload-Creator"><code>Upload-Creator</code></a></td>
    <td>Creates a direct upload that allows video uploads without an API key.</td>
</tr>
<tr>
    <td><a href="#create_token"><CopyableCode code="create_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a signed URL token for a video. If a body is not provided in the request, a token is created with default values.</td>
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
<tr id="parameter-Tus-Resumable">
    <td><CopyableCode code="Tus-Resumable" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-Upload-Creator">
    <td><CopyableCode code="Upload-Creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-Upload-Length">
    <td><CopyableCode code="Upload-Length" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-Upload-Metadata">
    <td><CopyableCode code="Upload-Metadata" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string (date-time)</code></td>
    <td>Alias for 'start'. Returns videos created after this date/time (RFC 3339 format).</td>
</tr>
<tr id="parameter-asc">
    <td><CopyableCode code="asc" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string (date-time)</code></td>
    <td>Alias for 'end'. Returns videos created before this date/time (RFC 3339 format).</td>
</tr>
<tr id="parameter-creator">
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direct_user">
    <td><CopyableCode code="direct_user" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-end">
    <td><CopyableCode code="end" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Filter by video ID(s). Can be a single ID or a comma-separated list of IDs.</td>
</tr>
<tr id="parameter-include_counts">
    <td><CopyableCode code="include_counts" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of videos to return (default 1000, max 1000).</td>
</tr>
<tr id="parameter-live_input_id">
    <td><CopyableCode code="live_input_id" /></td>
    <td><code>string</code></td>
    <td>Filter by live input ID to find videos associated with a specific live stream.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Filter by video name/UID(s). Can be a single name or a comma-separated list.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-video_name">
    <td><CopyableCode code="video_name" /></td>
    <td><code>string</code></td>
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

Fetches details for a single video.

```sql
SELECT
allowedOrigins,
clippedFrom,
created,
creator,
duration,
input,
liveInput,
maxDurationSeconds,
maxSizeBytes,
meta,
modified,
playback,
preview,
publicDetails,
readyToStream,
readyToStreamAt,
requireSignedURLs,
scheduledDeletion,
size,
status,
thumbnail,
thumbnailTimestampPct,
uid,
uploadExpiry,
uploaded,
watermark
FROM cloudflare.streams.streams
WHERE identifier = '{{ identifier }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists up to 1000 videos from a single request. For a specific range, refer to the optional parameters.

```sql
SELECT
allowedOrigins,
clippedFrom,
created,
creator,
duration,
input,
liveInput,
maxDurationSeconds,
maxSizeBytes,
meta,
modified,
playback,
preview,
publicDetails,
readyToStream,
readyToStreamAt,
requireSignedURLs,
scheduledDeletion,
size,
status,
thumbnail,
thumbnailTimestampPct,
uid,
uploadExpiry,
uploaded,
watermark
FROM cloudflare.streams.streams
WHERE account_id = '{{ account_id }}' -- required
AND status = '{{ status }}'
AND creator = '{{ creator }}'
AND type = '{{ type }}'
AND asc = '{{ asc }}'
AND video_name = '{{ video_name }}'
AND search = '{{ search }}'
AND start = '{{ start }}'
AND end = '{{ end }}'
AND include_counts = '{{ include_counts }}'
AND id = '{{ id }}'
AND name = '{{ name }}'
AND live_input_id = '{{ live_input_id }}'
AND before = '{{ before }}'
AND after = '{{ after }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="edit">

Edit details for a single video.

```sql
INSERT INTO cloudflare.streams.streams (
allowedOrigins,
creator,
maxDurationSeconds,
meta,
publicDetails,
requireSignedURLs,
scheduledDeletion,
thumbnailTimestampPct,
uid,
uploadExpiry,
identifier,
account_id
)
SELECT 
'{{ allowedOrigins }}',
'{{ creator }}',
{{ maxDurationSeconds }},
'{{ meta }}',
'{{ publicDetails }}',
{{ requireSignedURLs }},
'{{ scheduledDeletion }}',
{{ thumbnailTimestampPct }},
'{{ uid }}',
'{{ uploadExpiry }}',
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
<TabItem value="create">

Initiates a video upload using the TUS protocol. On success, the server responds with a status code 201 (created) and includes a `location` header to indicate where the content should be uploaded. Refer to https://tus.io for protocol details.

```sql
INSERT INTO cloudflare.streams.streams (
account_id,
Tus-Resumable,
Upload-Creator,
Upload-Length,
Upload-Metadata,
direct_user
)
SELECT 
'{{ account_id }}',
'{{ Tus-Resumable }}',
'{{ Upload-Creator }}',
'{{ Upload-Length }}',
'{{ Upload-Metadata }}',
'{{ direct_user }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: streams
  props:
    - name: identifier
      value: "{{ identifier }}"
      description: Required parameter for the streams resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the streams resource.
    - name: allowedOrigins
      value:
        - "{{ allowedOrigins }}"
      description: |
        Lists the origins allowed to display the video. Enter allowed origin domains in an array and use \`*\` for wildcard subdomains. Empty arrays allow the video to be viewed on any origin.
    - name: creator
      value: "{{ creator }}"
      description: |
        A user-defined identifier for the media creator.
    - name: maxDurationSeconds
      value: {{ maxDurationSeconds }}
      description: |
        The maximum duration in seconds for a video upload. Can be set for a video that is not yet uploaded to limit its duration. Uploads that exceed the specified duration will fail during processing. A value of \`-1\` means the value is unknown.
    - name: meta
      value: "{{ meta }}"
      description: |
        A user modifiable key-value store used to reference other systems of record for managing videos.
    - name: publicDetails
      description: |
        Public details for the video including title, share link, channel link, and logo.
      value:
        channel_link: "{{ channel_link }}"
        logo: "{{ logo }}"
        share_link: "{{ share_link }}"
        title: "{{ title }}"
    - name: requireSignedURLs
      value: {{ requireSignedURLs }}
      description: |
        Indicates whether the video can be a accessed using the UID. When set to \`true\`, a signed token must be generated with a signing key to view the video.
      default: false
    - name: scheduledDeletion
      value: "{{ scheduledDeletion }}"
      description: |
        Indicates the date and time at which the video will be deleted. Omit the field to indicate no change, or include with a \`null\` value to remove an existing scheduled deletion. If specified, must be at least 30 days from upload time.
    - name: thumbnailTimestampPct
      value: {{ thumbnailTimestampPct }}
      description: |
        The timestamp for a thumbnail image calculated as a percentage value of the video's duration. To convert from a second-wise timestamp to a percentage, divide the desired timestamp by the total duration of the video. If this value is not set, the default thumbnail image is taken from 0s of the video.
      default: 0
    - name: uid
      value: "{{ uid }}"
      description: |
        The unique identifier for the video. Can be used to verify the video being updated.
    - name: uploadExpiry
      value: "{{ uploadExpiry }}"
      description: |
        The date and time when the video upload URL is no longer valid for direct user uploads.
    - name: Tus-Resumable
      value: "{{ Tus-Resumable }}"
    - name: Upload-Creator
      value: "{{ Upload-Creator }}"
    - name: Upload-Length
      value: {{ Upload-Length }}
    - name: Upload-Metadata
      value: "{{ Upload-Metadata }}"
    - name: direct_user
      value: {{ direct_user }}
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

Deletes a video and its copies from Cloudflare Stream.

```sql
DELETE FROM cloudflare.streams.streams
WHERE identifier = '{{ identifier }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_clip"
    values={[
        { label: 'create_clip', value: 'create_clip' },
        { label: 'copy', value: 'copy' },
        { label: 'create_direct_upload', value: 'create_direct_upload' },
        { label: 'create_token', value: 'create_token' }
    ]}
>
<TabItem value="create_clip">

Clips a video based on the specified start and end times provided in seconds.

```sql
EXEC cloudflare.streams.streams.create_clip 
@account_id='{{ account_id }}' --required 
@@json=
'{
"allowedOrigins": "{{ allowedOrigins }}", 
"clippedFromVideoUID": "{{ clippedFromVideoUID }}", 
"creator": "{{ creator }}", 
"endTimeSeconds": {{ endTimeSeconds }}, 
"input": "{{ input }}", 
"meta": "{{ meta }}", 
"name": "{{ name }}", 
"requireSignedURLs": {{ requireSignedURLs }}, 
"scheduledDeletion": "{{ scheduledDeletion }}", 
"startTimeSeconds": {{ startTimeSeconds }}, 
"thumbnailTimestampPct": {{ thumbnailTimestampPct }}, 
"url": "{{ url }}", 
"watermark": "{{ watermark }}"
}'
;
```
</TabItem>
<TabItem value="copy">

Uploads a video to Stream from a provided URL.

```sql
EXEC cloudflare.streams.streams.copy 
@account_id='{{ account_id }}' --required, 
@Upload-Creator='{{ Upload-Creator }}' 
@@json=
'{
"allowedOrigins": "{{ allowedOrigins }}", 
"creator": "{{ creator }}", 
"input": "{{ input }}", 
"meta": "{{ meta }}", 
"name": "{{ name }}", 
"requireSignedURLs": {{ requireSignedURLs }}, 
"scheduledDeletion": "{{ scheduledDeletion }}", 
"thumbnailTimestampPct": {{ thumbnailTimestampPct }}, 
"url": "{{ url }}", 
"watermark": "{{ watermark }}"
}'
;
```
</TabItem>
<TabItem value="create_direct_upload">

Creates a direct upload that allows video uploads without an API key.

```sql
EXEC cloudflare.streams.streams.create_direct_upload 
@account_id='{{ account_id }}' --required, 
@Upload-Creator='{{ Upload-Creator }}' 
@@json=
'{
"allowedOrigins": "{{ allowedOrigins }}", 
"creator": "{{ creator }}", 
"expiry": "{{ expiry }}", 
"maxDurationSeconds": {{ maxDurationSeconds }}, 
"meta": "{{ meta }}", 
"requireSignedURLs": {{ requireSignedURLs }}, 
"scheduledDeletion": "{{ scheduledDeletion }}", 
"thumbnailTimestampPct": {{ thumbnailTimestampPct }}, 
"watermark": "{{ watermark }}"
}'
;
```
</TabItem>
<TabItem value="create_token">

Creates a signed URL token for a video. If a body is not provided in the request, a token is created with default values.

```sql
EXEC cloudflare.streams.streams.create_token 
@identifier='{{ identifier }}' --required, 
@account_id='{{ account_id }}' --required 
@@json=
'{
"accessRules": "{{ accessRules }}", 
"downloadable": {{ downloadable }}, 
"exp": {{ exp }}, 
"flags": "{{ flags }}", 
"id": "{{ id }}", 
"nbf": {{ nbf }}, 
"pem": "{{ pem }}"
}'
;
```
</TabItem>
</Tabs>
