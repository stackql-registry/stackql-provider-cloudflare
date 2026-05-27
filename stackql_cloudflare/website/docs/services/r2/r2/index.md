--- 
title: r2
hide_title: false
hide_table_of_contents: false
keywords:
  - r2
  - r2
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

Creates, updates, deletes, gets or lists a <code>r2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="r2" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.r2" /></td></tr>
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
    <td><a href="#create_temp_access_credentials"><CopyableCode code="create_temp_access_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket"><code>bucket</code></a>, <a href="#parameter-permission"><code>permission</code></a>, <a href="#parameter-ttlSeconds"><code>ttlSeconds</code></a>, <a href="#parameter-parentAccessKeyId"><code>parentAccessKeyId</code></a></td>
    <td></td>
    <td>Creates temporary access credentials on a bucket that can be optionally scoped to prefixes or objects.</td>
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
    defaultValue="create_temp_access_credentials"
    values={[
        { label: 'create_temp_access_credentials', value: 'create_temp_access_credentials' }
    ]}
>
<TabItem value="create_temp_access_credentials">

Creates temporary access credentials on a bucket that can be optionally scoped to prefixes or objects.

```sql
EXEC cloudflare.r2.r2.create_temp_access_credentials 
@account_id='{{ account_id }}' --required 
@@json=
'{
"bucket": "{{ bucket }}", 
"objects": "{{ objects }}", 
"parentAccessKeyId": "{{ parentAccessKeyId }}", 
"permission": "{{ permission }}", 
"prefixes": "{{ prefixes }}", 
"ttlSeconds": {{ ttlSeconds }}
}'
;
```
</TabItem>
</Tabs>
