--- 
title: priority
hide_title: false
hide_table_of_contents: false
keywords:
  - priority
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

Creates, updates, deletes, gets or lists a <code>priority</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="priority" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.priority" /></td></tr>
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

Get priority response.

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="readable_id" /></td>
    <td><code>string</code></td>
    <td>Readable Request ID. (example: RFI-2022-000001, title: Request Readable ID)</td>
</tr>
<tr>
    <td><CopyableCode code="completed" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2022-04-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>Request content. (example: What regions were most effected by the recent DoS?)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2022-04-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="message_tokens" /></td>
    <td><code>integer</code></td>
    <td>Tokens for the request messages.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2022-04-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>string</code></td>
    <td>Requested information from request. (example: Victomology)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Request Status. (open, accepted, reported, approved, completed, declined) (title: Request Status)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Brief description of the request. (example: DoS attack)</td>
</tr>
<tr>
    <td><CopyableCode code="tlp" /></td>
    <td><code>string</code></td>
    <td>The CISA defined Traffic Light Protocol (TLP). (clear, amber, amber-strict, green, red) (title: TLP)</td>
</tr>
<tr>
    <td><CopyableCode code="tokens" /></td>
    <td><code>integer</code></td>
    <td>Tokens for the request.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2022-04-01T05:20:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get priority quota response.

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
    <td><CopyableCode code="anniversary_date" /></td>
    <td><code>string (date-time)</code></td>
    <td>Anniversary date is when annual quota limit is refreshed. (example: 2022-04-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="quarter_anniversary_date" /></td>
    <td><code>string (date-time)</code></td>
    <td>Quarter anniversary date is when quota limit is refreshed each quarter. (example: 2022-04-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="quota" /></td>
    <td><code>integer</code></td>
    <td>Tokens for the quarter.</td>
</tr>
<tr>
    <td><CopyableCode code="remaining" /></td>
    <td><code>integer</code></td>
    <td>Tokens remaining for the quarter.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-priority_id"><code>priority_id</code></a></td>
    <td></td>
    <td>Retrieves a specific priority intelligence request from Cloudforce One.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieves quota usage for Cloudforce One priority requests.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-priority_id"><code>priority_id</code></a>, <a href="#parameter-labels"><code>labels</code></a>, <a href="#parameter-priority"><code>priority</code></a>, <a href="#parameter-requirement"><code>requirement</code></a>, <a href="#parameter-tlp"><code>tlp</code></a></td>
    <td></td>
    <td>Updates a priority intelligence request in Cloudforce One.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-priority_id"><code>priority_id</code></a></td>
    <td></td>
    <td>Deletes a priority intelligence request from Cloudforce One.</td>
</tr>
<tr>
    <td><a href="#new"><CopyableCode code="new" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-labels"><code>labels</code></a>, <a href="#parameter-priority"><code>priority</code></a>, <a href="#parameter-requirement"><code>requirement</code></a>, <a href="#parameter-tlp"><code>tlp</code></a></td>
    <td></td>
    <td>Creates a new priority intelligence request in Cloudforce One.</td>
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
<tr id="parameter-priority_id">
    <td><CopyableCode code="priority_id" /></td>
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

Retrieves a specific priority intelligence request from Cloudforce One.

```sql
SELECT
id,
readable_id,
completed,
content,
created,
message_tokens,
priority,
request,
status,
summary,
tlp,
tokens,
updated
FROM cloudflare.cloudforce_one.priority
WHERE account_id = '{{ account_id }}' -- required
AND priority_id = '{{ priority_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves quota usage for Cloudforce One priority requests.

```sql
SELECT
anniversary_date,
quarter_anniversary_date,
quota,
remaining
FROM cloudflare.cloudforce_one.priority
WHERE account_id = '{{ account_id }}' -- required
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

Updates a priority intelligence request in Cloudforce One.

```sql
REPLACE cloudflare.cloudforce_one.priority
SET 
labels = '{{ labels }}',
priority = {{ priority }},
requirement = '{{ requirement }}',
tlp = '{{ tlp }}'
WHERE 
account_id = '{{ account_id }}' --required
AND priority_id = '{{ priority_id }}' --required
AND labels = '{{ labels }}' --required
AND priority = '{{ priority }}' --required
AND requirement = '{{ requirement }}' --required
AND tlp = '{{ tlp }}' --required
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

Deletes a priority intelligence request from Cloudforce One.

```sql
DELETE FROM cloudflare.cloudforce_one.priority
WHERE account_id = '{{ account_id }}' --required
AND priority_id = '{{ priority_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="new"
    values={[
        { label: 'new', value: 'new' }
    ]}
>
<TabItem value="new">

Creates a new priority intelligence request in Cloudforce One.

```sql
EXEC cloudflare.cloudforce_one.priority.new 
@account_id='{{ account_id }}' --required 
@@json=
'{
"labels": "{{ labels }}", 
"priority": {{ priority }}, 
"requirement": "{{ requirement }}", 
"tlp": "{{ tlp }}"
}'
;
```
</TabItem>
</Tabs>
