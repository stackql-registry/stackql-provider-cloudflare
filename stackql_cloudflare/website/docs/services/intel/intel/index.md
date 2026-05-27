--- 
title: intel
hide_title: false
hide_table_of_contents: false
keywords:
  - intel
  - intel
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

Creates, updates, deletes, gets or lists an <code>intel</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="intel" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.intel.intel" /></td></tr>
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
    <td><a href="#dismiss"><CopyableCode code="dismiss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-issue_id"><code>issue_id</code></a></td>
    <td></td>
    <td>Deprecated endpoint for archiving Security Center insights. Use the newer archive-security-center-insight endpoint instead.</td>
</tr>
<tr>
    <td><a href="#create_miscategorization"><CopyableCode code="create_miscategorization" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Allows you to submit requests to change a domain’s category.</td>
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
<tr id="parameter-issue_id">
    <td><CopyableCode code="issue_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="dismiss"
    values={[
        { label: 'dismiss', value: 'dismiss' },
        { label: 'create_miscategorization', value: 'create_miscategorization' }
    ]}
>
<TabItem value="dismiss">

Deprecated endpoint for archiving Security Center insights. Use the newer archive-security-center-insight endpoint instead.

```sql
EXEC cloudflare.intel.intel.dismiss 
@account_id='{{ account_id }}' --required, 
@issue_id='{{ issue_id }}' --required 
@@json=
'{
"dismiss": {{ dismiss }}
}'
;
```
</TabItem>
<TabItem value="create_miscategorization">

Allows you to submit requests to change a domain’s category.

```sql
EXEC cloudflare.intel.intel.create_miscategorization 
@account_id='{{ account_id }}' --required 
@@json=
'{
"content_adds": "{{ content_adds }}", 
"content_removes": "{{ content_removes }}", 
"indicator_type": "{{ indicator_type }}", 
"ip": "{{ ip }}", 
"security_adds": "{{ security_adds }}", 
"security_removes": "{{ security_removes }}", 
"url": "{{ url }}"
}'
;
```
</TabItem>
</Tabs>
