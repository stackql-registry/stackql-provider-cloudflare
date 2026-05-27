--- 
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - api_gateway
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.configurations" /></td></tr>
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

Retrieve information about specific configuration properties response

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
    <td>The name of the characteristic field, i.e., the header or cookie name. (example: authorization)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of characteristic. (header, cookie) (example: header)</td>
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
    <td><a href="#parameter-normalize"><code>normalize</code></a></td>
    <td>Gets the current API Shield configuration settings for a zone, including validation behavior and enforcement mode.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-auth_id_characteristics"><code>auth_id_characteristics</code></a></td>
    <td><a href="#parameter-normalize"><code>normalize</code></a></td>
    <td>Updates API Shield configuration settings for a zone. Can modify validation strictness, enforcement mode, and other global settings.</td>
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
<tr id="parameter-normalize">
    <td><CopyableCode code="normalize" /></td>
    <td><code>boolean</code></td>
    <td>Ensures that the configuration is written or retrieved in normalized fashion</td>
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

Gets the current API Shield configuration settings for a zone, including validation behavior and enforcement mode.

```sql
SELECT
name,
type
FROM cloudflare.api_gateway.configurations
WHERE zone_id = '{{ zone_id }}' -- required
AND normalize = '{{ normalize }}'
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

Updates API Shield configuration settings for a zone. Can modify validation strictness, enforcement mode, and other global settings.

```sql
REPLACE cloudflare.api_gateway.configurations
SET 
auth_id_characteristics = '{{ auth_id_characteristics }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND auth_id_characteristics = '{{ auth_id_characteristics }}' --required
AND normalize = {{ normalize}}
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
