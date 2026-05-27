--- 
title: feedback
hide_title: false
hide_table_of_contents: false
keywords:
  - feedback
  - bot_management
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

Creates, updates, deletes, gets or lists a <code>feedback</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feedback" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.bot_management.feedback" /></td></tr>
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

List of feedback reports

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
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="expression" /></td>
    <td><code>string</code></td>
    <td>Wirefilter expression describing the traffic being reported.</td>
</tr>
<tr>
    <td><CopyableCode code="first_request_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_request_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="requests_by_attribute" /></td>
    <td><code>object</code></td>
    <td>Top attributes contributing to the feedback sample. Keys include topASNs, topCountries, topHosts, topIPs, topJA3Hashes, topJA4s, topPaths, topUserAgents.</td>
</tr>
<tr>
    <td><CopyableCode code="requests_by_score" /></td>
    <td><code>object</code></td>
    <td>Map of bot scores (1-99) to request counts. Sum must equal `requests`.</td>
</tr>
<tr>
    <td><CopyableCode code="requests_by_score_src" /></td>
    <td><code>object</code></td>
    <td>Map of score source to request counts. Sum must equal `requests`.</td>
</tr>
<tr>
    <td><CopyableCode code="subtype" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of feedback report. (false_positive, false_negative) (example: false_positive)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Returns all feedback reports previously submitted for the specified zone. Feedback reports help improve detection by sharing samples of traffic that were misclassified as bots or humans.</td>
</tr>
<tr>
    <td><a href="#bot_management_zone_feedback_create"><CopyableCode code="bot_management_zone_feedback_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-expression"><code>expression</code></a>, <a href="#parameter-first_request_seen_at"><code>first_request_seen_at</code></a>, <a href="#parameter-last_request_seen_at"><code>last_request_seen_at</code></a>, <a href="#parameter-requests"><code>requests</code></a>, <a href="#parameter-requests_by_score"><code>requests_by_score</code></a>, <a href="#parameter-requests_by_score_src"><code>requests_by_score_src</code></a>, <a href="#parameter-requests_by_attribute"><code>requests_by_attribute</code></a></td>
    <td></td>
    <td>Submit a feedback report for the specified zone. Use `type` to indicate whether the report is a false positive (good traffic flagged as bot) or a false negative (bot traffic missed). Furthermore, you can also use `expression` as a wirefilter to identify the affected traffic sample. See more accepted API fields and expression types at https://developers.cloudflare.com/bots/concepts/feedback-loop/#api-fields and https://developers.cloudflare.com/bots/concepts/feedback-loop/#expression-fields, respectively.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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

Returns all feedback reports previously submitted for the specified zone. Feedback reports help improve detection by sharing samples of traffic that were misclassified as bots or humans.

```sql
SELECT
created_at,
description,
expression,
first_request_seen_at,
last_request_seen_at,
requests,
requests_by_attribute,
requests_by_score,
requests_by_score_src,
subtype,
type
FROM cloudflare.bot_management.feedback
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="bot_management_zone_feedback_create"
    values={[
        { label: 'bot_management_zone_feedback_create', value: 'bot_management_zone_feedback_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="bot_management_zone_feedback_create">

Submit a feedback report for the specified zone. Use `type` to indicate whether the report is a false positive (good traffic flagged as bot) or a false negative (bot traffic missed). Furthermore, you can also use `expression` as a wirefilter to identify the affected traffic sample. See more accepted API fields and expression types at https://developers.cloudflare.com/bots/concepts/feedback-loop/#api-fields and https://developers.cloudflare.com/bots/concepts/feedback-loop/#expression-fields, respectively.

```sql
INSERT INTO cloudflare.bot_management.feedback (
description,
expression,
first_request_seen_at,
last_request_seen_at,
requests,
requests_by_attribute,
requests_by_score,
requests_by_score_src,
subtype,
type,
zone_id
)
SELECT 
'{{ description }}' /* required */,
'{{ expression }}' /* required */,
'{{ first_request_seen_at }}' /* required */,
'{{ last_request_seen_at }}' /* required */,
{{ requests }} /* required */,
'{{ requests_by_attribute }}' /* required */,
'{{ requests_by_score }}' /* required */,
'{{ requests_by_score_src }}' /* required */,
'{{ subtype }}',
'{{ type }}' /* required */,
'{{ zone_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feedback
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the feedback resource.
    - name: description
      value: "{{ description }}"
    - name: expression
      value: "{{ expression }}"
      description: |
        Wirefilter expression describing the traffic being reported.
    - name: first_request_seen_at
      value: "{{ first_request_seen_at }}"
    - name: last_request_seen_at
      value: "{{ last_request_seen_at }}"
    - name: requests
      value: {{ requests }}
    - name: requests_by_attribute
      value: "{{ requests_by_attribute }}"
      description: |
        Top attributes contributing to the feedback sample. Keys include topASNs, topCountries, topHosts, topIPs, topJA3Hashes, topJA4s, topPaths, topUserAgents.
    - name: requests_by_score
      value: "{{ requests_by_score }}"
      description: |
        Map of bot scores (1-99) to request counts. Sum must equal \`requests\`.
    - name: requests_by_score_src
      value: "{{ requests_by_score_src }}"
      description: |
        Map of score source to request counts. Sum must equal \`requests\`.
    - name: subtype
      value: "{{ subtype }}"
    - name: type
      value: "{{ type }}"
      description: |
        Type of feedback report.
      valid_values: ['false_positive', 'false_negative']
`}</CodeBlock>

</TabItem>
</Tabs>
