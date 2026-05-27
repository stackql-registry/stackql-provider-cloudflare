--- 
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - google_tag_gateway
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

Creates, updates, deletes, gets or lists a <code>config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="config" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.google_tag_gateway.config" /></td></tr>
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

Get Google Tag Gateway configuration response.

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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Enables or disables Google Tag Gateway for this zone.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the endpoint path for proxying Google Tag Manager requests. Use an absolute path starting with '/', with no nested paths and alphanumeric characters only (e.g. /metrics). (example: /metrics)</td>
</tr>
<tr>
    <td><CopyableCode code="hideOriginalIp" /></td>
    <td><code>boolean</code></td>
    <td>Hides the original client IP address from Google when enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="measurementId" /></td>
    <td><code>string</code></td>
    <td>Specify the Google Tag Manager container or measurement ID (e.g. GTM-XXXXXXX or G-XXXXXXXXXX). (example: GTM-P2F3N47Q)</td>
</tr>
<tr>
    <td><CopyableCode code="setUpTag" /></td>
    <td><code>boolean</code></td>
    <td>Set up the associated Google Tag on the zone automatically when enabled.</td>
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
    <td></td>
    <td>Gets the Google Tag Gateway configuration for a zone.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-hideOriginalIp"><code>hideOriginalIp</code></a>, <a href="#parameter-measurementId"><code>measurementId</code></a></td>
    <td></td>
    <td>Updates the Google Tag Gateway configuration for a zone.</td>
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

Gets the Google Tag Gateway configuration for a zone.

```sql
SELECT
enabled,
endpoint,
hideOriginalIp,
measurementId,
setUpTag
FROM cloudflare.google_tag_gateway.config
WHERE zone_id = '{{ zone_id }}' -- required
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

Updates the Google Tag Gateway configuration for a zone.

```sql
REPLACE cloudflare.google_tag_gateway.config
SET 
enabled = {{ enabled }},
endpoint = '{{ endpoint }}',
hideOriginalIp = {{ hideOriginalIp }},
measurementId = '{{ measurementId }}',
setUpTag = {{ setUpTag }}
WHERE 
zone_id = '{{ zone_id }}' --required
AND enabled = {{ enabled }} --required
AND endpoint = '{{ endpoint }}' --required
AND hideOriginalIp = {{ hideOriginalIp }} --required
AND measurementId = '{{ measurementId }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
