--- 
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
  - web3
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

Creates, updates, deletes, gets or lists an <code>entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.web3.entries" /></td></tr>
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

IPFS Universal Path Gateway Content List Entry Details response.

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
    <td>Specify the identifier of the hostname. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>Specify the CID or content path of content to block. (example: QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Specify an optional description of the content list entry. (example: this is my content list entry)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specify the type of content list entry to block. (cid, content_path) (example: cid)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List IPFS Universal Path Gateway Content List Entries response.

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
    <td>Specify the identifier of the hostname. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>Specify the CID or content path of content to block. (example: QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Specify an optional description of the content list entry. (example: this is my content list entry)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Specify the type of content list entry to block. (cid, content_path) (example: cid)</td>
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
    <td><a href="#parameter-content_list_entry_identifier"><code>content_list_entry_identifier</code></a>, <a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-content_list_entry_identifier"><code>content_list_entry_identifier</code></a>, <a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-content_list_entry_identifier"><code>content_list_entry_identifier</code></a>, <a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
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
<tr id="parameter-content_list_entry_identifier">
    <td><CopyableCode code="content_list_entry_identifier" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-identifier">
    <td><CopyableCode code="identifier" /></td>
    <td><code>string</code></td>
    <td>Resource identifier.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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

IPFS Universal Path Gateway Content List Entry Details response.

```sql
SELECT
id,
content,
created_on,
description,
modified_on,
type
FROM cloudflare.web3.entries
WHERE content_list_entry_identifier = '{{ content_list_entry_identifier }}' -- required
AND identifier = '{{ identifier }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List IPFS Universal Path Gateway Content List Entries response.

```sql
SELECT
id,
content,
created_on,
description,
modified_on,
type
FROM cloudflare.web3.entries
WHERE identifier = '{{ identifier }}' -- required
AND zone_id = '{{ zone_id }}' -- required
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

No description available.

```sql
INSERT INTO cloudflare.web3.entries (
content,
description,
type,
identifier,
zone_id
)
SELECT 
'{{ content }}' /* required */,
'{{ description }}',
'{{ type }}' /* required */,
'{{ identifier }}',
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entries
  props:
    - name: identifier
      value: "{{ identifier }}"
      description: Required parameter for the entries resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the entries resource.
    - name: content
      value: "{{ content }}"
      description: |
        Specify the CID or content path of content to block.
    - name: description
      value: "{{ description }}"
      description: |
        Specify an optional description of the content list entry.
    - name: type
      value: "{{ type }}"
      description: |
        Specify the type of content list entry to block.
      valid_values: ['cid', 'content_path']
`}</CodeBlock>

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

No description available.

```sql
REPLACE cloudflare.web3.entries
SET 
content = '{{ content }}',
description = '{{ description }}',
type = '{{ type }}'
WHERE 
content_list_entry_identifier = '{{ content_list_entry_identifier }}' --required
AND identifier = '{{ identifier }}' --required
AND zone_id = '{{ zone_id }}' --required
AND type = '{{ type }}' --required
AND content = '{{ content }}' --required
RETURNING
errors,
messages,
result,
result_info,
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

No description available.

```sql
DELETE FROM cloudflare.web3.entries
WHERE content_list_entry_identifier = '{{ content_list_entry_identifier }}' --required
AND identifier = '{{ identifier }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
