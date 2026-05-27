--- 
title: raw
hide_title: false
hide_table_of_contents: false
keywords:
  - raw
  - cloudforce_one
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

Creates, updates, deletes, gets or lists a <code>raw</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="raw" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.raw" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the raw event.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accountId" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tlp" /></td>
    <td><code>string</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-raw_id"><code>raw_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#post_event_raw_update"><CopyableCode code="post_event_raw_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-raw_id"><code>raw_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-event_id"><code>event_id</code></a>, <a href="#parameter-raw_id"><code>raw_id</code></a></td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account ID.</td>
</tr>
<tr id="parameter-event_id">
    <td><CopyableCode code="event_id" /></td>
    <td><code>string</code></td>
    <td>The event ID.</td>
</tr>
<tr id="parameter-raw_id">
    <td><CopyableCode code="raw_id" /></td>
    <td><code>string</code></td>
    <td>Raw Event UUID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the raw event.

```sql
SELECT
id,
accountId,
created,
data,
source,
tlp
FROM cloudflare.cloudforce_one.raw
WHERE account_id = '{{ account_id }}' -- required
AND event_id = '{{ event_id }}' -- required
AND raw_id = '{{ raw_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_event_raw_update"
    values={[
        { label: 'post_event_raw_update', value: 'post_event_raw_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_event_raw_update">

No description available.

```sql
INSERT INTO cloudflare.cloudforce_one.raw (
data,
source,
tlp,
account_id,
event_id,
raw_id
)
SELECT 
'{{ data }}',
'{{ source }}',
'{{ tlp }}',
'{{ account_id }}',
'{{ event_id }}',
'{{ raw_id }}'
RETURNING
id,
data
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: raw
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the raw resource.
    - name: event_id
      value: "{{ event_id }}"
      description: Required parameter for the raw resource.
    - name: raw_id
      value: "{{ raw_id }}"
      description: Required parameter for the raw resource.
    - name: data
      value: "{{ data }}"
    - name: source
      value: "{{ source }}"
    - name: tlp
      value: "{{ tlp }}"
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

No description available.

```sql
UPDATE cloudflare.cloudforce_one.raw
SET 
data = '{{ data }}',
source = '{{ source }}',
tlp = '{{ tlp }}'
WHERE 
account_id = '{{ account_id }}' --required
AND event_id = '{{ event_id }}' --required
AND raw_id = '{{ raw_id }}' --required
RETURNING
id,
data;
```
</TabItem>
</Tabs>
