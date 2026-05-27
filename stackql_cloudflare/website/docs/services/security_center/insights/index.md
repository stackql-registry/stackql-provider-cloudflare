--- 
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
  - security_center
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

Creates, updates, deletes, gets or lists an <code>insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="insights" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.security_center.insights" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

The request was successful.

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
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Indicates the total number of results.</td>
</tr>
<tr>
    <td><CopyableCode code="issues" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Specifies the current page within paginated list of results.</td>
</tr>
<tr>
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Sets the number of results per page of results.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

The request was successful.

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
    <td><CopyableCode code="count" /></td>
    <td><code>integer</code></td>
    <td>Indicates the total number of results.</td>
</tr>
<tr>
    <td><CopyableCode code="issues" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Specifies the current page within paginated list of results.</td>
</tr>
<tr>
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Sets the number of results per page of results.</td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-dismissed"><code>dismissed</code></a>, <a href="#parameter-issue_class"><code>issue_class</code></a>, <a href="#parameter-issue_type"><code>issue_type</code></a>, <a href="#parameter-product"><code>product</code></a>, <a href="#parameter-severity"><code>severity</code></a>, <a href="#parameter-subject"><code>subject</code></a>, <a href="#parameter-issue_class~neq"><code>issue_class&#126;neq</code></a>, <a href="#parameter-issue_type~neq"><code>issue_type&#126;neq</code></a>, <a href="#parameter-product~neq"><code>product&#126;neq</code></a>, <a href="#parameter-severity~neq"><code>severity&#126;neq</code></a>, <a href="#parameter-subject~neq"><code>subject&#126;neq</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all Security Center insights for the account or zone, showing security findings and recommendations.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-dismissed"><code>dismissed</code></a>, <a href="#parameter-issue_class"><code>issue_class</code></a>, <a href="#parameter-issue_type"><code>issue_type</code></a>, <a href="#parameter-product"><code>product</code></a>, <a href="#parameter-severity"><code>severity</code></a>, <a href="#parameter-subject"><code>subject</code></a>, <a href="#parameter-issue_class~neq"><code>issue_class&#126;neq</code></a>, <a href="#parameter-issue_type~neq"><code>issue_type&#126;neq</code></a>, <a href="#parameter-product~neq"><code>product&#126;neq</code></a>, <a href="#parameter-severity~neq"><code>severity&#126;neq</code></a>, <a href="#parameter-subject~neq"><code>subject&#126;neq</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all Security Center insights for the account or zone, showing security findings and recommendations.</td>
</tr>
<tr>
    <td><a href="#dismiss_by_account"><CopyableCode code="dismiss_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-issue_id"><code>issue_id</code></a></td>
    <td></td>
    <td>Archives a Security Center insight for an account or zone, removing it from the active insights list while preserving historical data.</td>
</tr>
<tr>
    <td><a href="#dismiss_by_zone"><CopyableCode code="dismiss_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-issue_id"><code>issue_id</code></a></td>
    <td></td>
    <td>Archives a Security Center insight for an account or zone, removing it from the active insights list while preserving historical data.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-dismissed">
    <td><CopyableCode code="dismissed" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-issue_class">
    <td><CopyableCode code="issue_class" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-issue_class~neq">
    <td><CopyableCode code="issue_class~neq" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-issue_type">
    <td><CopyableCode code="issue_type" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-issue_type~neq">
    <td><CopyableCode code="issue_type~neq" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-product">
    <td><CopyableCode code="product" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-product~neq">
    <td><CopyableCode code="product~neq" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-severity">
    <td><CopyableCode code="severity" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-severity~neq">
    <td><CopyableCode code="severity~neq" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-subject">
    <td><CopyableCode code="subject" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-subject~neq">
    <td><CopyableCode code="subject~neq" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

Lists all Security Center insights for the account or zone, showing security findings and recommendations.

```sql
SELECT
count,
issues,
page,
per_page
FROM cloudflare.security_center.insights
WHERE account_id = '{{ account_id }}' -- required
AND dismissed = '{{ dismissed }}'
AND issue_class = '{{ issue_class }}'
AND issue_type = '{{ issue_type }}'
AND product = '{{ product }}'
AND severity = '{{ severity }}'
AND subject = '{{ subject }}'
AND issue_class~neq = '{{ issue_class~neq }}'
AND issue_type~neq = '{{ issue_type~neq }}'
AND product~neq = '{{ product~neq }}'
AND severity~neq = '{{ severity~neq }}'
AND subject~neq = '{{ subject~neq }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Lists all Security Center insights for the account or zone, showing security findings and recommendations.

```sql
SELECT
count,
issues,
page,
per_page
FROM cloudflare.security_center.insights
WHERE zone_id = '{{ zone_id }}' -- required
AND dismissed = '{{ dismissed }}'
AND issue_class = '{{ issue_class }}'
AND issue_type = '{{ issue_type }}'
AND product = '{{ product }}'
AND severity = '{{ severity }}'
AND subject = '{{ subject }}'
AND issue_class~neq = '{{ issue_class~neq }}'
AND issue_type~neq = '{{ issue_type~neq }}'
AND product~neq = '{{ product~neq }}'
AND severity~neq = '{{ severity~neq }}'
AND subject~neq = '{{ subject~neq }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="dismiss_by_account"
    values={[
        { label: 'dismiss_by_account', value: 'dismiss_by_account' },
        { label: 'dismiss_by_zone', value: 'dismiss_by_zone' }
    ]}
>
<TabItem value="dismiss_by_account">

Archives a Security Center insight for an account or zone, removing it from the active insights list while preserving historical data.

```sql
REPLACE cloudflare.security_center.insights
SET 
dismiss = {{ dismiss }}
WHERE 
account_id = '{{ account_id }}' --required
AND issue_id = '{{ issue_id }}' --required
RETURNING
errors,
messages,
success;
```
</TabItem>
<TabItem value="dismiss_by_zone">

Archives a Security Center insight for an account or zone, removing it from the active insights list while preserving historical data.

```sql
REPLACE cloudflare.security_center.insights
SET 
dismiss = {{ dismiss }}
WHERE 
zone_id = '{{ zone_id }}' --required
AND issue_id = '{{ issue_id }}' --required
RETURNING
errors,
messages,
success;
```
</TabItem>
</Tabs>
