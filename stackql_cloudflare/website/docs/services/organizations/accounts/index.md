--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - organizations
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.organizations.accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

The request has succeeded.

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (standard, enterprise)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a></td>
    <td><a href="#parameter-account_pubname"><code>account_pubname</code></a>, <a href="#parameter-account_pubname.startsWith"><code>account_pubname.startsWith</code></a>, <a href="#parameter-account_pubname.endsWith"><code>account_pubname.endsWith</code></a>, <a href="#parameter-account_pubname.contains"><code>account_pubname.contains</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-name.startsWith"><code>name.startsWith</code></a>, <a href="#parameter-name.endsWith"><code>name.endsWith</code></a>, <a href="#parameter-name.contains"><code>name.contains</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Retrieve a list of accounts that belong to a specific organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)</td>
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
<tr id="parameter-organization_id">
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>The organization ID.</td>
</tr>
<tr id="parameter-account_pubname">
    <td><CopyableCode code="account_pubname" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the account_pubname is equal to a particular string.</td>
</tr>
<tr id="parameter-account_pubname.contains">
    <td><CopyableCode code="account_pubname.contains" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the account_pubname contains a particular string.</td>
</tr>
<tr id="parameter-account_pubname.endsWith">
    <td><CopyableCode code="account_pubname.endsWith" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the account_pubname ends with a particular string.</td>
</tr>
<tr id="parameter-account_pubname.startsWith">
    <td><CopyableCode code="account_pubname.startsWith" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the account_pubname starts with a particular string.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Sort direction for the order_by field. Valid values: `asc`, `desc`. Defaults to `asc` when order_by is specified.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the name is equal to a particular string.</td>
</tr>
<tr id="parameter-name.contains">
    <td><CopyableCode code="name.contains" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the name contains a particular string.</td>
</tr>
<tr id="parameter-name.endsWith">
    <td><CopyableCode code="name.endsWith" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the name ends with a particular string.</td>
</tr>
<tr id="parameter-name.startsWith">
    <td><CopyableCode code="name.startsWith" /></td>
    <td><code>string</code></td>
    <td>(case-insensitive) Filter the list of accounts to where the name starts with a particular string.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>Field to order results by. Currently supported values: `account_name`. When not specified, results are ordered by internal account ID.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The amount of items to return. Defaults to 10.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>An opaque token returned from the last list response that when provided will retrieve the next page. Parameters used to filter the retrieved list must remain in subsequent requests with a page token.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieve a list of accounts that belong to a specific organization. (Currently in Closed Beta - see https://developers.cloudflare.com/fundamentals/organizations/)

```sql
SELECT
id,
name,
created_on,
settings,
type
FROM cloudflare.organizations.accounts
WHERE organization_id = '{{ organization_id }}' -- required
AND account_pubname = '{{ account_pubname }}'
AND account_pubname.startsWith = '{{ account_pubname.startsWith }}'
AND account_pubname.endsWith = '{{ account_pubname.endsWith }}'
AND account_pubname.contains = '{{ account_pubname.contains }}'
AND name = '{{ name }}'
AND name.startsWith = '{{ name.startsWith }}'
AND name.endsWith = '{{ name.endsWith }}'
AND name.contains = '{{ name.contains }}'
AND order_by = '{{ order_by }}'
AND direction = '{{ direction }}'
AND page_token = '{{ page_token }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>
