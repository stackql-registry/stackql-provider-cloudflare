--- 
title: magic
hide_title: false
hide_table_of_contents: false
keywords:
  - magic
  - magic_cloud_networking
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

Creates, updates, deletes, gets or lists a <code>magic</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="magic" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_cloud_networking.magic" /></td></tr>
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
    <td><a href="#apply"><CopyableCode code="apply" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td></td>
    <td>Apply an On-ramp (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td></td>
    <td>Export an On-ramp to terraform ready file(s) (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#plan"><CopyableCode code="plan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td></td>
    <td>Plan an On-ramp (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#discover"><CopyableCode code="discover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Run discovery for all Cloud Integrations in an account (Closed Beta).</td>
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
<tr id="parameter-onramp_id">
    <td><CopyableCode code="onramp_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="apply"
    values={[
        { label: 'apply', value: 'apply' },
        { label: 'export', value: 'export' },
        { label: 'plan', value: 'plan' },
        { label: 'discover', value: 'discover' }
    ]}
>
<TabItem value="apply">

Apply an On-ramp (Closed Beta).

```sql
EXEC cloudflare.magic_cloud_networking.magic.apply 
@account_id='{{ account_id }}' --required, 
@onramp_id='{{ onramp_id }}' --required
;
```
</TabItem>
<TabItem value="export">

Export an On-ramp to terraform ready file(s) (Closed Beta).

```sql
EXEC cloudflare.magic_cloud_networking.magic.export 
@account_id='{{ account_id }}' --required, 
@onramp_id='{{ onramp_id }}' --required
;
```
</TabItem>
<TabItem value="plan">

Plan an On-ramp (Closed Beta).

```sql
EXEC cloudflare.magic_cloud_networking.magic.plan 
@account_id='{{ account_id }}' --required, 
@onramp_id='{{ onramp_id }}' --required
;
```
</TabItem>
<TabItem value="discover">

Run discovery for all Cloud Integrations in an account (Closed Beta).

```sql
EXEC cloudflare.magic_cloud_networking.magic.discover 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
