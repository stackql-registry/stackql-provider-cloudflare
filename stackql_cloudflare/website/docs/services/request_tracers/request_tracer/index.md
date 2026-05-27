--- 
title: request_tracer
hide_title: false
hide_table_of_contents: false
keywords:
  - request_tracer
  - request_tracers
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

Creates, updates, deletes, gets or lists a <code>request_tracer</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="request_tracer" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.request_tracers.request_tracer" /></td></tr>
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
    <td><a href="#create_trace"><CopyableCode code="create_trace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-method"><code>method</code></a></td>
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
    defaultValue="create_trace"
    values={[
        { label: 'create_trace', value: 'create_trace' }
    ]}
>
<TabItem value="create_trace">

Request Trace response

```sql
EXEC cloudflare.request_tracers.request_tracer.create_trace 
@account_id='{{ account_id }}' --required 
@@json=
'{
"body": "{{ body }}", 
"context": "{{ context }}", 
"cookies": "{{ cookies }}", 
"headers": "{{ headers }}", 
"method": "{{ method }}", 
"protocol": "{{ protocol }}", 
"skip_response": {{ skip_response }}, 
"url": "{{ url }}"
}'
;
```
</TabItem>
</Tabs>
