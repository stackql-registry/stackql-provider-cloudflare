--- 
title: review_status
hide_title: false
hide_table_of_contents: false
keywords:
  - review_status
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>review_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="review_status" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.review_status" /></td></tr>
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

List applications review status response.

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
    <td><CopyableCode code="approved_apps" /></td>
    <td><code>array</code></td>
    <td>Contains the ids of the approved applications. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="in_review_apps" /></td>
    <td><code>array</code></td>
    <td>Contains the ids of the applications in review. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="unapproved_apps" /></td>
    <td><code>array</code></td>
    <td>Contains the ids of the unapproved applications. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieve the statuses of your applications.</td>
</tr>
<tr>
    <td><a href="#zero_trust_applications_review_status_update"><CopyableCode code="zero_trust_applications_review_status_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-approved_apps"><code>approved_apps</code></a>, <a href="#parameter-unapproved_apps"><code>unapproved_apps</code></a>, <a href="#parameter-in_review_apps"><code>in_review_apps</code></a></td>
    <td></td>
    <td>Update the statuses of your applications.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieve the statuses of your applications.

```sql
SELECT
approved_apps,
created_at,
in_review_apps,
unapproved_apps,
updated_at
FROM cloudflare.zero_trust.review_status
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="zero_trust_applications_review_status_update"
    values={[
        { label: 'zero_trust_applications_review_status_update', value: 'zero_trust_applications_review_status_update' }
    ]}
>
<TabItem value="zero_trust_applications_review_status_update">

Update the statuses of your applications.

```sql
REPLACE cloudflare.zero_trust.review_status
SET 
approved_apps = '{{ approved_apps }}',
in_review_apps = '{{ in_review_apps }}',
unapproved_apps = '{{ unapproved_apps }}'
WHERE 
account_id = '{{ account_id }}' --required
AND approved_apps = '{{ approved_apps }}' --required
AND unapproved_apps = '{{ unapproved_apps }}' --required
AND in_review_apps = '{{ in_review_apps }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
