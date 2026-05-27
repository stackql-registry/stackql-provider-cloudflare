--- 
title: target_connectivity_precheck
hide_title: false
hide_table_of_contents: false
keywords:
  - target_connectivity_precheck
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

Creates, updates, deletes, gets or lists a <code>target_connectivity_precheck</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="target_connectivity_precheck" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.target_connectivity_precheck" /></td></tr>
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
    <td><a href="#update_connectivity_precheck"><CopyableCode code="update_connectivity_precheck" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-vendor"><code>vendor</code></a>, <a href="#parameter-bucket"><code>bucket</code></a>, <a href="#parameter-secret"><code>secret</code></a></td>
    <td></td>
    <td>Check whether tokens are valid against the target bucket</td>
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
    defaultValue="update_connectivity_precheck"
    values={[
        { label: 'update_connectivity_precheck', value: 'update_connectivity_precheck' }
    ]}
>
<TabItem value="update_connectivity_precheck">

Check whether tokens are valid against the target bucket

```sql
EXEC cloudflare.r2.target_connectivity_precheck.update_connectivity_precheck 
@account_id='{{ account_id }}' --required 
@@json=
'{
"bucket": "{{ bucket }}", 
"jurisdiction": "{{ jurisdiction }}", 
"secret": "{{ secret }}", 
"vendor": "{{ vendor }}"
}'
;
```
</TabItem>
</Tabs>
