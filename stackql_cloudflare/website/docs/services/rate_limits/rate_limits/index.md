--- 
title: rate_limits
hide_title: false
hide_table_of_contents: false
keywords:
  - rate_limits
  - rate_limits
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

Creates, updates, deletes, gets or lists a <code>rate_limits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rate_limits" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rate_limits.rate_limits" /></td></tr>
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

Get a rate limit response.

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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether the API call was successful. (true)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List rate limits response.

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
    <td>The unique identifier of the rate limit. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>object</code></td>
    <td>The action to perform when the threshold of matched traffic within the configured period is exceeded.</td>
</tr>
<tr>
    <td><CopyableCode code="bypass" /></td>
    <td><code>array</code></td>
    <td>Criteria specifying when the current rate limit should be bypassed. You can specify that the rate limit should not apply to one or more URLs.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule. This value is sanitized and any tags will be removed. (example: Prevent multiple login failures to mitigate brute force attacks)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the rate limit is currently disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="match" /></td>
    <td><code>object</code></td>
    <td>Determines which traffic the rate limit counts towards the threshold.</td>
</tr>
<tr>
    <td><CopyableCode code="period" /></td>
    <td><code>number</code></td>
    <td>The time in seconds (an integer value) to count matching traffic. If the count exceeds the configured threshold within this period, Cloudflare will perform the configured action.</td>
</tr>
<tr>
    <td><CopyableCode code="threshold" /></td>
    <td><code>number</code></td>
    <td>The threshold that will trigger the configured mitigation action. Configure this value along with the `period` property to establish a threshold per period.</td>
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
    <td><a href="#parameter-rate_limit_id"><code>rate_limit_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a rate limit.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetches the rate limits for a zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-threshold"><code>threshold</code></a>, <a href="#parameter-period"><code>period</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Creates a new rate limit for a zone. Refer to the object definition for a list of required attributes.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-rate_limit_id"><code>rate_limit_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-threshold"><code>threshold</code></a>, <a href="#parameter-period"><code>period</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Updates an existing rate limit.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rate_limit_id"><code>rate_limit_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing rate limit.</td>
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
<tr id="parameter-rate_limit_id">
    <td><CopyableCode code="rate_limit_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
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

Fetches the details of a rate limit.

```sql
SELECT
errors,
messages,
result,
success
FROM cloudflare.rate_limits.rate_limits
WHERE rate_limit_id = '{{ rate_limit_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches the rate limits for a zone.

```sql
SELECT
id,
action,
bypass,
description,
disabled,
match,
period,
threshold
FROM cloudflare.rate_limits.rate_limits
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new rate limit for a zone. Refer to the object definition for a list of required attributes.

```sql
INSERT INTO cloudflare.rate_limits.rate_limits (
action,
match,
period,
threshold,
zone_id
)
SELECT 
'{{ action }}' /* required */,
'{{ match }}' /* required */,
{{ period }} /* required */,
{{ threshold }} /* required */,
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: rate_limits
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the rate_limits resource.
    - name: action
      description: |
        The action to perform when the threshold of matched traffic within the configured period is exceeded.
      value:
        mode: "{{ mode }}"
        response:
          body: "{{ body }}"
          content_type: "{{ content_type }}"
        timeout: {{ timeout }}
    - name: match
      description: |
        Determines which traffic the rate limit counts towards the threshold.
      value:
        headers:
          - name: "{{ name }}"
            op: "{{ op }}"
            value: "{{ value }}"
        request:
          methods:
            - "{{ methods }}"
          schemes:
            - "{{ schemes }}"
          url: "{{ url }}"
        response:
          origin_traffic: {{ origin_traffic }}
    - name: period
      value: {{ period }}
      description: |
        The time in seconds (an integer value) to count matching traffic. If the count exceeds the configured threshold within this period, Cloudflare will perform the configured action.
    - name: threshold
      value: {{ threshold }}
      description: |
        The threshold that will trigger the configured mitigation action. Configure this value along with the \`period\` property to establish a threshold per period.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Updates an existing rate limit.

```sql
REPLACE cloudflare.rate_limits.rate_limits
SET 
action = '{{ action }}',
match = '{{ match }}',
period = {{ period }},
threshold = {{ threshold }}
WHERE 
rate_limit_id = '{{ rate_limit_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND match = '{{ match }}' --required
AND threshold = '{{ threshold }}' --required
AND period = '{{ period }}' --required
AND action = '{{ action }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes an existing rate limit.

```sql
DELETE FROM cloudflare.rate_limits.rate_limits
WHERE rate_limit_id = '{{ rate_limit_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
