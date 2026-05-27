--- 
title: email
hide_title: false
hide_table_of_contents: false
keywords:
  - email
  - email_sending
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

Creates, updates, deletes, gets or lists an <code>email</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="email" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_sending.email" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#send"><CopyableCode code="send" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a>, <a href="#parameter-subject"><code>subject</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#send_raw"><CopyableCode code="send_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-recipients"><code>recipients</code></a>, <a href="#parameter-mime_message"><code>mime_message</code></a></td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="send"
    values={[
        { label: 'send', value: 'send' },
        { label: 'send_raw', value: 'send_raw' }
    ]}
>
<TabItem value="send">

Email sending results.

```sql
EXEC cloudflare.email_sending.email.send 
@account_id='{{ account_id }}' --required 
@@json=
'{
"attachments": "{{ attachments }}", 
"bcc": "{{ bcc }}", 
"cc": "{{ cc }}", 
"from": "{{ from }}", 
"headers": "{{ headers }}", 
"html": "{{ html }}", 
"reply_to": "{{ reply_to }}", 
"subject": "{{ subject }}", 
"text": "{{ text }}", 
"to": "{{ to }}"
}'
;
```
</TabItem>
<TabItem value="send_raw">

Email sending results.

```sql
EXEC cloudflare.email_sending.email.send_raw 
@account_id='{{ account_id }}' --required 
@@json=
'{
"from": "{{ from }}", 
"mime_message": "{{ mime_message }}", 
"recipients": "{{ recipients }}"
}'
;
```
</TabItem>
</Tabs>
