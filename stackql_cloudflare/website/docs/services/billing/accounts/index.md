--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - billing
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.billing.accounts" /></td></tr>
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
    <td><a href="#set_pay_per_crawl_zones"><CopyableCode code="set_pay_per_crawl_zones" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Allows an account admin to set the can_be_enabled setting on a list of zones.</td>
</tr>
<tr>
    <td><a href="#query_pay_per_crawl_zones"><CopyableCode code="query_pay_per_crawl_zones" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Provided a list of pay-per-crawl configured zones this method will return whether they can enable PPC or not.</td>
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
    defaultValue="set_pay_per_crawl_zones"
    values={[
        { label: 'set_pay_per_crawl_zones', value: 'set_pay_per_crawl_zones' },
        { label: 'query_pay_per_crawl_zones', value: 'query_pay_per_crawl_zones' }
    ]}
>
<TabItem value="set_pay_per_crawl_zones">

Allows an account admin to set the can_be_enabled setting on a list of zones.

```sql
EXEC cloudflare.billing.accounts.set_pay_per_crawl_zones 
@account_id='{{ account_id }}' --required 
@@json=
'{
"zones": "{{ zones }}"
}'
;
```
</TabItem>
<TabItem value="query_pay_per_crawl_zones">

Provided a list of pay-per-crawl configured zones this method will return whether they can enable PPC or not.

```sql
EXEC cloudflare.billing.accounts.query_pay_per_crawl_zones 
@account_id='{{ account_id }}' --required 
@@json=
'{
"zones": "{{ zones }}"
}'
;
```
</TabItem>
</Tabs>
