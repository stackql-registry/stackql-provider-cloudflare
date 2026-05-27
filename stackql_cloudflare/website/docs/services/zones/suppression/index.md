--- 
title: suppression
hide_title: false
hide_table_of_contents: false
keywords:
  - suppression
  - zones
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

Creates, updates, deletes, gets or lists a <code>suppression</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="suppression" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zones.suppression" /></td></tr>
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

Returns suppression.

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
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns suppressed emails.

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
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-suppression_id"><code>suppression_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#post_zones_zone_id_email_sending_suppression"><CopyableCode code="post_zones_zone_id_email_sending_suppression" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-email"><code>email</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_zones_zone_id_email_sending_suppression_suppression_id"><CopyableCode code="delete_zones_zone_id_email_sending_suppression_suppression_id" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-suppression_id"><code>suppression_id</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-suppression_id">
    <td><CopyableCode code="suppression_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns suppression.

```sql
SELECT
result
FROM cloudflare.zones.suppression
WHERE zone_id = '{{ zone_id }}' -- required
AND suppression_id = '{{ suppression_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns suppressed emails.

```sql
SELECT
id,
created_at,
email,
expires_at,
reason,
zones
FROM cloudflare.zones.suppression
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_zones_zone_id_email_sending_suppression"
    values={[
        { label: 'post_zones_zone_id_email_sending_suppression', value: 'post_zones_zone_id_email_sending_suppression' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_zones_zone_id_email_sending_suppression">

No description available.

```sql
INSERT INTO cloudflare.zones.suppression (
email,
expires_at,
zone_id
)
SELECT 
'{{ email }}' /* required */,
'{{ expires_at }}',
'{{ zone_id }}'
RETURNING
result
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: suppression
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the suppression resource.
    - name: email
      value: "{{ email }}"
    - name: expires_at
      value: "{{ expires_at }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_zones_zone_id_email_sending_suppression_suppression_id"
    values={[
        { label: 'delete_zones_zone_id_email_sending_suppression_suppression_id', value: 'delete_zones_zone_id_email_sending_suppression_suppression_id' }
    ]}
>
<TabItem value="delete_zones_zone_id_email_sending_suppression_suppression_id">

No description available.

```sql
DELETE FROM cloudflare.zones.suppression
WHERE zone_id = '{{ zone_id }}' --required
AND suppression_id = '{{ suppression_id }}' --required
;
```
</TabItem>
</Tabs>
