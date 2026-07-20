--- 
title: investigate
hide_title: false
hide_table_of_contents: false
keywords:
  - investigate
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

Creates, updates, deletes, gets or lists an <code>investigate</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="investigate" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.investigate" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Email message details.

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
    <td>Unique identifier for a message retrieved from investigation (example: 4Njp3P0STMz2c02Q-2024-01-05T10:00:00-12345678)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="postfix_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the message (example: 4Njp3P0STMz2c02Q)</td>
</tr>
<tr>
    <td><CopyableCode code="from_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="to_name" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="action_log" /></td>
    <td><code>array</code></td>
    <td>Deprecated, use `GET /investigate/&#123;investigate_id&#125;/action_log` instead. End of life: November 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="client_recipients" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delivery_mode" /></td>
    <td><code>string</code></td>
    <td> (DIRECT, BCC, JOURNAL, REVIEW_SUBMISSION, DMARC_UNVERIFIED, DMARC_FAILURE_REPORT, DMARC_AGGREGATE_REPORT, THREAT_INTEL_SUBMISSION, SIMULATION_SUBMISSION, API, RETRO_SCAN)</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_status" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="detection_reasons" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="edf_hash" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="envelope_from" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="envelope_to" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="final_disposition" /></td>
    <td><code>string</code></td>
    <td> (MALICIOUS, MALICIOUS-BEC, SUSPICIOUS, SPOOF, SPAM, BULK, ENCRYPTED, EXTERNAL, UNKNOWN, NONE)</td>
</tr>
<tr>
    <td><CopyableCode code="findings" /></td>
    <td><code>array</code></td>
    <td>Deprecated, use the `findings` field from `GET /investigate/&#123;investigate_id&#125;/detections` instead. End of life: November 1, 2026. Detection findings for this message.</td>
</tr>
<tr>
    <td><CopyableCode code="from" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="htmltext_structure_hash" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_phish_submission" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_quarantined" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_delivery_operations" /></td>
    <td><code>array</code></td>
    <td>Post-delivery operations performed on this message</td>
</tr>
<tr>
    <td><CopyableCode code="postfix_id_outbound" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Message processing properties</td>
</tr>
<tr>
    <td><CopyableCode code="replyto" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="scanned_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the message was scanned (UTC)</td>
</tr>
<tr>
    <td><CopyableCode code="sent_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the message was sent (UTC)</td>
</tr>
<tr>
    <td><CopyableCode code="sent_date" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="threat_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="to" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ts" /></td>
    <td><code>string</code></td>
    <td>Deprecated, use `scanned_at` instead. End of life: November 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="validation" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Search results for the provided query.

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
    <td>Unique identifier for a message retrieved from investigation (example: 4Njp3P0STMz2c02Q-2024-01-05T10:00:00-12345678)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="postfix_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the message (example: 4Njp3P0STMz2c02Q)</td>
</tr>
<tr>
    <td><CopyableCode code="from_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="to_name" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="action_log" /></td>
    <td><code>array</code></td>
    <td>Deprecated, use `GET /investigate/&#123;investigate_id&#125;/action_log` instead. End of life: November 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="client_recipients" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="delivery_mode" /></td>
    <td><code>string</code></td>
    <td> (DIRECT, BCC, JOURNAL, REVIEW_SUBMISSION, DMARC_UNVERIFIED, DMARC_FAILURE_REPORT, DMARC_AGGREGATE_REPORT, THREAT_INTEL_SUBMISSION, SIMULATION_SUBMISSION, API, RETRO_SCAN)</td>
</tr>
<tr>
    <td><CopyableCode code="delivery_status" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="detection_reasons" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="edf_hash" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="envelope_from" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="envelope_to" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="final_disposition" /></td>
    <td><code>string</code></td>
    <td> (MALICIOUS, MALICIOUS-BEC, SUSPICIOUS, SPOOF, SPAM, BULK, ENCRYPTED, EXTERNAL, UNKNOWN, NONE)</td>
</tr>
<tr>
    <td><CopyableCode code="findings" /></td>
    <td><code>array</code></td>
    <td>Deprecated, use the `findings` field from `GET /investigate/&#123;investigate_id&#125;/detections` instead. End of life: November 1, 2026. Detection findings for this message.</td>
</tr>
<tr>
    <td><CopyableCode code="from" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="htmltext_structure_hash" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_phish_submission" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_quarantined" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_delivery_operations" /></td>
    <td><code>array</code></td>
    <td>Post-delivery operations performed on this message</td>
</tr>
<tr>
    <td><CopyableCode code="postfix_id_outbound" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Message processing properties</td>
</tr>
<tr>
    <td><CopyableCode code="replyto" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="scanned_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the message was scanned (UTC)</td>
</tr>
<tr>
    <td><CopyableCode code="sent_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the message was sent (UTC)</td>
</tr>
<tr>
    <td><CopyableCode code="sent_date" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="threat_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="to" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ts" /></td>
    <td><code>string</code></td>
    <td>Deprecated, use `scanned_at` instead. End of life: November 1, 2026.</td>
</tr>
<tr>
    <td><CopyableCode code="validation" /></td>
    <td><code>object</code></td>
    <td></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-investigate_id"><code>investigate_id</code></a></td>
    <td><a href="#parameter-submission"><code>submission</code></a></td>
    <td>Retrieves comprehensive details for a specific email message including headers, recipients, sender information, and current quarantine status. Use the investigate_id from search results to fetch detailed information.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-start"><code>start</code></a>, <a href="#parameter-end"><code>end</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-detections_only"><code>detections_only</code></a>, <a href="#parameter-action_log"><code>action_log</code></a>, <a href="#parameter-final_disposition"><code>final_disposition</code></a>, <a href="#parameter-metric"><code>metric</code></a>, <a href="#parameter-message_action"><code>message_action</code></a>, <a href="#parameter-recipient"><code>recipient</code></a>, <a href="#parameter-sender"><code>sender</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a>, <a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-message_id"><code>message_id</code></a>, <a href="#parameter-subject"><code>subject</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a></td>
    <td>Returns information for each email that matches the search parameter(s).</td>
</tr>
<tr>
    <td><a href="#bulk_move"><CopyableCode code="bulk_move" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>Moves multiple messages to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.</td>
</tr>
<tr>
    <td><a href="#release"><CopyableCode code="release" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Releases one or more quarantined messages, delivering them to the intended recipients. Use when a message was incorrectly quarantined. Returns delivery status for each recipient.</td>
</tr>
<tr>
    <td><a href="#move_message"><CopyableCode code="move_message" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-investigate_id"><code>investigate_id</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>Moves a single message to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.</td>
</tr>
<tr>
    <td><a href="#reclassify"><CopyableCode code="reclassify" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-investigate_id"><code>investigate_id</code></a>, <a href="#parameter-expected_disposition"><code>expected_disposition</code></a></td>
    <td></td>
    <td>Submits a request to reclassify an email's disposition. Use for reporting false positives or false negatives. Optionally provide the raw EML content for reanalysis. The reclassification is processed asynchronously.</td>
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
<tr id="parameter-investigate_id">
    <td><CopyableCode code="investigate_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-action_log">
    <td><CopyableCode code="action_log" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include the message action log in the response.</td>
</tr>
<tr id="parameter-alert_id">
    <td><CopyableCode code="alert_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-detections_only">
    <td><CopyableCode code="detections_only" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include only detections in search results.</td>
</tr>
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Sender domains to filter by.</td>
</tr>
<tr id="parameter-end">
    <td><CopyableCode code="end" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end of the search date range. Defaults to `now`.</td>
</tr>
<tr id="parameter-final_disposition">
    <td><CopyableCode code="final_disposition" /></td>
    <td><code>string</code></td>
    <td>Dispositions to filter by.</td>
</tr>
<tr id="parameter-message_action">
    <td><CopyableCode code="message_action" /></td>
    <td><code>string</code></td>
    <td>Message actions to filter by.</td>
</tr>
<tr id="parameter-message_id">
    <td><CopyableCode code="message_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-metric">
    <td><CopyableCode code="metric" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Deprecated: Use cursor pagination instead. End of life: November 1, 2026.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The number of results per page. Maximum value is 1000.</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>Space-delimited search term. Case-insensitive.</td>
</tr>
<tr id="parameter-recipient">
    <td><CopyableCode code="recipient" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-sender">
    <td><CopyableCode code="sender" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-start">
    <td><CopyableCode code="start" /></td>
    <td><code>string (date-time)</code></td>
    <td>The beginning of the search date range. Defaults to `now - 30 days`.</td>
</tr>
<tr id="parameter-subject">
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-submission">
    <td><CopyableCode code="submission" /></td>
    <td><code>boolean</code></td>
    <td>When true, search the submissions datastore only. When false or omitted, search the regular datastore only.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves comprehensive details for a specific email message including headers, recipients, sender information, and current quarantine status. Use the investigate_id from search results to fetch detailed information.

```sql
SELECT
id,
alert_id,
message_id,
postfix_id,
from_name,
to_name,
action_log,
client_recipients,
delivery_mode,
delivery_status,
detection_reasons,
edf_hash,
envelope_from,
envelope_to,
final_disposition,
findings,
from,
htmltext_structure_hash,
is_phish_submission,
is_quarantined,
post_delivery_operations,
postfix_id_outbound,
properties,
replyto,
scanned_at,
sent_at,
sent_date,
subject,
threat_categories,
to,
ts,
validation
FROM cloudflare.email_security.investigate
WHERE account_id = '{{ account_id }}' -- required
AND investigate_id = '{{ investigate_id }}' -- required
AND submission = '{{ submission }}'
;
```
</TabItem>
<TabItem value="list">

Returns information for each email that matches the search parameter(s).

```sql
SELECT
id,
alert_id,
message_id,
postfix_id,
from_name,
to_name,
action_log,
client_recipients,
delivery_mode,
delivery_status,
detection_reasons,
edf_hash,
envelope_from,
envelope_to,
final_disposition,
findings,
from,
htmltext_structure_hash,
is_phish_submission,
is_quarantined,
post_delivery_operations,
postfix_id_outbound,
properties,
replyto,
scanned_at,
sent_at,
sent_date,
subject,
threat_categories,
to,
ts,
validation
FROM cloudflare.email_security.investigate
WHERE account_id = '{{ account_id }}' -- required
AND start = '{{ start }}'
AND end = '{{ end }}'
AND query = '{{ query }}'
AND detections_only = '{{ detections_only }}'
AND action_log = '{{ action_log }}'
AND final_disposition = '{{ final_disposition }}'
AND metric = '{{ metric }}'
AND message_action = '{{ message_action }}'
AND recipient = '{{ recipient }}'
AND sender = '{{ sender }}'
AND alert_id = '{{ alert_id }}'
AND domain = '{{ domain }}'
AND message_id = '{{ message_id }}'
AND subject = '{{ subject }}'
AND cursor = '{{ cursor }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="bulk_move"
    values={[
        { label: 'bulk_move', value: 'bulk_move' },
        { label: 'release', value: 'release' },
        { label: 'move_message', value: 'move_message' },
        { label: 'reclassify', value: 'reclassify' }
    ]}
>
<TabItem value="bulk_move">

Moves multiple messages to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.

```sql
EXEC cloudflare.email_security.investigate.bulk_move 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination": "{{ destination }}", 
"ids": "{{ ids }}", 
"postfix_ids": "{{ postfix_ids }}"
}'
;
```
</TabItem>
<TabItem value="release">

Releases one or more quarantined messages, delivering them to the intended recipients. Use when a message was incorrectly quarantined. Returns delivery status for each recipient.

```sql
EXEC cloudflare.email_security.investigate.release 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="move_message">

Moves a single message to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.

```sql
EXEC cloudflare.email_security.investigate.move_message 
@account_id='{{ account_id }}' --required, 
@investigate_id='{{ investigate_id }}' --required 
@@json=
'{
"destination": "{{ destination }}"
}'
;
```
</TabItem>
<TabItem value="reclassify">

Submits a request to reclassify an email's disposition. Use for reporting false positives or false negatives. Optionally provide the raw EML content for reanalysis. The reclassification is processed asynchronously.

```sql
EXEC cloudflare.email_security.investigate.reclassify 
@account_id='{{ account_id }}' --required, 
@investigate_id='{{ investigate_id }}' --required 
@@json=
'{
"eml_content": "{{ eml_content }}", 
"escalated_submission_id": "{{ escalated_submission_id }}", 
"expected_disposition": "{{ expected_disposition }}"
}'
;
```
</TabItem>
</Tabs>
