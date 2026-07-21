--- 
title: requests
hide_title: false
hide_table_of_contents: false
keywords:
  - requests
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

Creates, updates, deletes, gets or lists a <code>requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.requests" /></td></tr>
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

Get request response.

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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific Cloudforce One intelligence request.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creating a request adds the request into the Cloudforce One queue for analysis. In addition to the content, a short title, type, priority, and releasability should be provided. If one is not provided, a default will be assigned.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a></td>
    <td></td>
    <td>Updating a request alters the request in the Cloudforce One queue. This API may be used to update any attributes of the request after the initial submission. Only fields that you choose to update need to be add to the request body.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a></td>
    <td></td>
    <td>Deletes a Cloudforce One intelligence request and all associated data.</td>
</tr>
<tr>
    <td><a href="#create_priority"><CopyableCode code="create_priority" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td></td>
    <td>Lists priority intelligence requests in Cloudforce One.</td>
</tr>
<tr>
    <td><a href="#create_asset"><CopyableCode code="create_asset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td></td>
    <td>Lists assets attached to a Cloudforce One intelligence request.</td>
</tr>
<tr>
    <td><a href="#create_message"><CopyableCode code="create_message" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td></td>
    <td>Lists messages in a Cloudforce One intelligence request conversation.</td>
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
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Retrieves details for a specific Cloudforce One intelligence request.

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
FROM cloudflare.cloudforce_one.requests
WHERE account_id = '{{ account_id }}' -- required
AND request_id = '{{ request_id }}' -- required
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

Creating a request adds the request into the Cloudforce One queue for analysis. In addition to the content, a short title, type, priority, and releasability should be provided. If one is not provided, a default will be assigned.

```sql
INSERT INTO cloudflare.cloudforce_one.requests (
content,
priority,
request_type,
summary,
tlp,
account_id
)
SELECT 
'{{ content }}',
'{{ priority }}',
'{{ request_type }}',
'{{ summary }}',
'{{ tlp }}',
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
- name: requests
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the requests resource.
    - name: content
      value: "{{ content }}"
      description: |
        Request content.
    - name: priority
      value: "{{ priority }}"
      description: |
        Priority for analyzing the request.
    - name: request_type
      value: "{{ request_type }}"
      description: |
        Requested information from request.
    - name: summary
      value: "{{ summary }}"
      description: |
        Brief description of the request.
    - name: tlp
      value: "{{ tlp }}"
      description: |
        The CISA defined Traffic Light Protocol (TLP).
      valid_values: ['clear', 'amber', 'amber-strict', 'green', 'red']
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

Updating a request alters the request in the Cloudforce One queue. This API may be used to update any attributes of the request after the initial submission. Only fields that you choose to update need to be add to the request body.

```sql
REPLACE cloudflare.cloudforce_one.requests
SET 
content = '{{ content }}',
priority = '{{ priority }}',
request_type = '{{ request_type }}',
summary = '{{ summary }}',
tlp = '{{ tlp }}'
WHERE 
account_id = '{{ account_id }}' --required
AND request_id = '{{ request_id }}' --required
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

Deletes a Cloudforce One intelligence request and all associated data.

```sql
DELETE FROM cloudflare.cloudforce_one.requests
WHERE account_id = '{{ account_id }}' --required
AND request_id = '{{ request_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_priority"
    values={[
        { label: 'create_priority', value: 'create_priority' },
        { label: 'create_asset', value: 'create_asset' },
        { label: 'create_message', value: 'create_message' }
    ]}
>
<TabItem value="create_priority">

Lists priority intelligence requests in Cloudforce One.

```sql
EXEC cloudflare.cloudforce_one.requests.create_priority 
@account_id='{{ account_id }}' --required 
@@json=
'{
"page": {{ page }}, 
"per_page": {{ per_page }}
}'
;
```
</TabItem>
<TabItem value="create_asset">

Lists assets attached to a Cloudforce One intelligence request.

```sql
EXEC cloudflare.cloudforce_one.requests.create_asset 
@account_id='{{ account_id }}' --required, 
@request_id='{{ request_id }}' --required 
@@json=
'{
"page": {{ page }}, 
"per_page": {{ per_page }}
}'
;
```
</TabItem>
<TabItem value="create_message">

Lists messages in a Cloudforce One intelligence request conversation.

```sql
EXEC cloudflare.cloudforce_one.requests.create_message 
@account_id='{{ account_id }}' --required, 
@request_id='{{ request_id }}' --required 
@@json=
'{
"after": "{{ after }}", 
"before": "{{ before }}", 
"page": {{ page }}, 
"per_page": {{ per_page }}, 
"sort_by": "{{ sort_by }}", 
"sort_order": "{{ sort_order }}"
}'
;
```
</TabItem>
</Tabs>
