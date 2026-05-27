--- 
title: mitigations
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigations
  - abuse_reports
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

Creates, updates, deletes, gets or lists a <code>mitigations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mitigations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.abuse_reports.mitigations" /></td></tr>
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

List abuse report mitigations successful

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
    <td>ID of remediation.</td>
</tr>
<tr>
    <td><CopyableCode code="entity_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="effective_date" /></td>
    <td><code>string</code></td>
    <td>Date when the mitigation will become active. Time in RFC 3339 format (https://www.rfc-editor.org/rfc/rfc3339.html) (example: 2009-11-10T23:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="entity_type" /></td>
    <td><code>string</code></td>
    <td> (url_pattern, account, zone)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of a mitigation (pending, active, in_review, cancelled, removed)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of mitigation (legal_block, misleading_interstitial, phishing_interstitial, network_block, rate_limit_cache, account_suspend, redirect_video_stream)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-report_id"><code>report_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-sort"><code>sort</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-effective_before"><code>effective_before</code></a>, <a href="#parameter-effective_after"><code>effective_after</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-entity_type"><code>entity_type</code></a></td>
    <td>List mitigations done to remediate the abuse report.</td>
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
<tr id="parameter-report_id">
    <td><CopyableCode code="report_id" /></td>
    <td><code>string</code></td>
    <td>Abuse Report ID</td>
</tr>
<tr id="parameter-effective_after">
    <td><CopyableCode code="effective_after" /></td>
    <td><code>string</code></td>
    <td>Returns mitigation that were dispatched after the given date</td>
</tr>
<tr id="parameter-effective_before">
    <td><CopyableCode code="effective_before" /></td>
    <td><code>string</code></td>
    <td>Returns mitigations that were dispatched before the given date</td>
</tr>
<tr id="parameter-entity_type">
    <td><CopyableCode code="entity_type" /></td>
    <td><code>string</code></td>
    <td>Filter by the type of entity the mitigation impacts.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Where in pagination to start listing abuse reports</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>How many abuse reports per page to list</td>
</tr>
<tr id="parameter-sort">
    <td><CopyableCode code="sort" /></td>
    <td><code>string</code></td>
    <td>A property to sort by, followed by the order</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter by the status of the mitigation.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Filter by the type of mitigation. This filter parameter can be specified multiple times to include multiple types of mitigations in the result set, e.g. ?type=rate_limit_cache&type=legal_block.</td>
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

List mitigations done to remediate the abuse report.

```sql
SELECT
id,
entity_id,
effective_date,
entity_type,
status,
type
FROM cloudflare.abuse_reports.mitigations
WHERE account_id = '{{ account_id }}' -- required
AND report_id = '{{ report_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND sort = '{{ sort }}'
AND type = '{{ type }}'
AND effective_before = '{{ effective_before }}'
AND effective_after = '{{ effective_after }}'
AND status = '{{ status }}'
AND entity_type = '{{ entity_type }}'
;
```
</TabItem>
</Tabs>
