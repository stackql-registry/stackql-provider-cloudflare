--- 
title: videos
hide_title: false
hide_table_of_contents: false
keywords:
  - videos
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

Creates, updates, deletes, gets or lists a <code>videos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="videos" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.streams.videos" /></td></tr>
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

Returns information about an account's storage use response.

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
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td>A user-defined identifier for the media creator. (example: creator-id_abcde12345)</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageMinutes" /></td>
    <td><code>number (float)</code></td>
    <td>The total minutes of video content stored in the account. May contain decimal values.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageMinutesLimit" /></td>
    <td><code>integer</code></td>
    <td>The storage capacity alloted for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="videoCount" /></td>
    <td><code>integer</code></td>
    <td>The total count of videos associated with the account.</td>
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
    <td><a href="#parameter-creator"><code>creator</code></a></td>
    <td>Returns information about an account's storage use.</td>
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
<tr id="parameter-creator">
    <td><CopyableCode code="creator" /></td>
    <td><code>string</code></td>
    <td></td>
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

Returns information about an account's storage use.

```sql
SELECT
creator,
totalStorageMinutes,
totalStorageMinutesLimit,
videoCount
FROM cloudflare.streams.videos
WHERE account_id = '{{ account_id }}' -- required
AND creator = '{{ creator }}'
;
```
</TabItem>
</Tabs>
