--- 
title: submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - submissions
  - email_security
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

Creates, updates, deletes, gets or lists a <code>submissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="submissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.submissions" /></td></tr>
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

List of submissions

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
    <td><CopyableCode code="escalated_submission_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="original_postfix_id" /></td>
    <td><code>string</code></td>
    <td>The postfix ID of the original message that was submitted</td>
</tr>
<tr>
    <td><CopyableCode code="submission_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="customer_status" /></td>
    <td><code>string</code></td>
    <td> (escalated, reviewed, unreviewed)</td>
</tr>
<tr>
    <td><CopyableCode code="escalated_as" /></td>
    <td><code>string</code></td>
    <td> (MALICIOUS, SUSPICIOUS, SPOOF, SPAM, BULK, NONE)</td>
</tr>
<tr>
    <td><CopyableCode code="escalated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="escalated_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="original_disposition" /></td>
    <td><code>string</code></td>
    <td> (MALICIOUS, SUSPICIOUS, SPOOF, SPAM, BULK, NONE)</td>
</tr>
<tr>
    <td><CopyableCode code="original_edf_hash" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="outcome" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="outcome_disposition" /></td>
    <td><code>string</code></td>
    <td> (MALICIOUS, SUSPICIOUS, SPOOF, SPAM, BULK, NONE)</td>
</tr>
<tr>
    <td><CopyableCode code="requested_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the submission was requested (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="requested_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="requested_disposition" /></td>
    <td><code>string</code></td>
    <td> (MALICIOUS, SUSPICIOUS, SPOOF, SPAM, BULK, NONE)</td>
</tr>
<tr>
    <td><CopyableCode code="requested_ts" /></td>
    <td><code>string</code></td>
    <td>Deprecated, use `requested_at` instead</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Whether the submission was created by a team member or an end user. (Team, User)</td>
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
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-end"><code>end</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-submission_id"><code>submission_id</code></a>, <a href="#parameter-original_disposition"><code>original_disposition</code></a>, <a href="#parameter-requested_disposition"><code>requested_disposition</code></a>, <a href="#parameter-outcome_disposition"><code>outcome_disposition</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Returns information for submissions made to reclassify emails. Shows the status, outcome, and disposition changes for reclassification requests made by users or the security team. Useful for tracking false positive/negative reports.</td>
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
<tr id="parameter-end">
    <td><CopyableCode code="end" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of the search date range. Defaults to `now`.</td>
</tr>
<tr id="parameter-original_disposition">
    <td><CopyableCode code="original_disposition" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-outcome_disposition">
    <td><CopyableCode code="outcome_disposition" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Current page within paginated list of results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The number of results per page. Maximum value is 1000.</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-requested_disposition">
    <td><CopyableCode code="requested_disposition" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string (date-time)</code></td>
    <td>The beginning of the search date range. Defaults to `now - 30 days`.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-submission_id">
    <td><CopyableCode code="submission_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td></td>
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

Returns information for submissions made to reclassify emails. Shows the status, outcome, and disposition changes for reclassification requests made by users or the security team. Useful for tracking false positive/negative reports.

```sql
SELECT
escalated_submission_id,
original_postfix_id,
submission_id,
customer_status,
escalated_as,
escalated_at,
escalated_by,
original_disposition,
original_edf_hash,
outcome,
outcome_disposition,
requested_at,
requested_by,
requested_disposition,
requested_ts,
status,
subject,
type
FROM cloudflare.email_security.submissions
WHERE account_id = '{{ account_id }}' -- required
AND start = '{{ start }}'
AND end = '{{ end }}'
AND type = '{{ type }}'
AND submission_id = '{{ submission_id }}'
AND original_disposition = '{{ original_disposition }}'
AND requested_disposition = '{{ requested_disposition }}'
AND outcome_disposition = '{{ outcome_disposition }}'
AND status = '{{ status }}'
AND query = '{{ query }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>
