--- 
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - ai_gateway
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

Creates, updates, deletes, gets or lists a <code>gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai_gateway.gateways" /></td></tr>
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

Returns a single object if found

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
    <td>gateway id</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authentication" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cache_invalidate_on_update" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cache_ttl" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="collect_logs" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dlp" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="log_management" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="log_management_strategy" /></td>
    <td><code>string</code></td>
    <td> (STOP_INSERTING, DELETE_OLDEST)</td>
</tr>
<tr>
    <td><CopyableCode code="logpush" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="logpush_public_key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="otel" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limiting_interval" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limiting_limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limiting_technique" /></td>
    <td><code>string</code></td>
    <td> (fixed, sliding)</td>
</tr>
<tr>
    <td><CopyableCode code="retry_backoff" /></td>
    <td><code>string</code></td>
    <td>Backoff strategy for retry delays (constant, linear, exponential)</td>
</tr>
<tr>
    <td><CopyableCode code="retry_delay" /></td>
    <td><code>integer</code></td>
    <td>Delay between retry attempts in milliseconds (0-5000)</td>
</tr>
<tr>
    <td><CopyableCode code="retry_max_attempts" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of retry attempts for failed requests (1-5)</td>
</tr>
<tr>
    <td><CopyableCode code="stripe" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workers_ai_billing_mode" /></td>
    <td><code>string</code></td>
    <td>Controls how Workers AI inference calls routed through this gateway are billed. Only 'postpaid' is currently supported. (postpaid) (default: postpaid)</td>
</tr>
<tr>
    <td><CopyableCode code="zdr" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List objects

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
    <td>gateway id</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authentication" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cache_invalidate_on_update" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cache_ttl" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="collect_logs" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dlp" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="log_management" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="log_management_strategy" /></td>
    <td><code>string</code></td>
    <td> (STOP_INSERTING, DELETE_OLDEST)</td>
</tr>
<tr>
    <td><CopyableCode code="logpush" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="logpush_public_key" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="otel" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limiting_interval" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limiting_limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limiting_technique" /></td>
    <td><code>string</code></td>
    <td> (fixed, sliding)</td>
</tr>
<tr>
    <td><CopyableCode code="retry_backoff" /></td>
    <td><code>string</code></td>
    <td>Backoff strategy for retry delays (constant, linear, exponential)</td>
</tr>
<tr>
    <td><CopyableCode code="retry_delay" /></td>
    <td><code>integer</code></td>
    <td>Delay between retry attempts in milliseconds (0-5000)</td>
</tr>
<tr>
    <td><CopyableCode code="retry_max_attempts" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of retry attempts for failed requests (1-5)</td>
</tr>
<tr>
    <td><CopyableCode code="stripe" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="workers_ai_billing_mode" /></td>
    <td><code>string</code></td>
    <td>Controls how Workers AI inference calls routed through this gateway are billed. Only 'postpaid' is currently supported. (postpaid) (default: postpaid)</td>
</tr>
<tr>
    <td><CopyableCode code="zdr" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific AI Gateway dataset.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-search"><code>search</code></a></td>
    <td>Lists all AI Gateway evaluator types configured for the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-rate_limiting_interval"><code>rate_limiting_interval</code></a>, <a href="#parameter-rate_limiting_limit"><code>rate_limiting_limit</code></a>, <a href="#parameter-collect_logs"><code>collect_logs</code></a>, <a href="#parameter-cache_ttl"><code>cache_ttl</code></a>, <a href="#parameter-cache_invalidate_on_update"><code>cache_invalidate_on_update</code></a></td>
    <td></td>
    <td>Creates a new AI Gateway.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-rate_limiting_interval"><code>rate_limiting_interval</code></a>, <a href="#parameter-rate_limiting_limit"><code>rate_limiting_limit</code></a>, <a href="#parameter-collect_logs"><code>collect_logs</code></a>, <a href="#parameter-cache_ttl"><code>cache_ttl</code></a>, <a href="#parameter-cache_invalidate_on_update"><code>cache_invalidate_on_update</code></a></td>
    <td></td>
    <td>Updates an existing AI Gateway dataset.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Deletes an AI Gateway dataset.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
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
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
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

Retrieves details for a specific AI Gateway dataset.

```sql
SELECT
id,
store_id,
authentication,
cache_invalidate_on_update,
cache_ttl,
collect_logs,
created_at,
dlp,
is_default,
log_management,
log_management_strategy,
logpush,
logpush_public_key,
modified_at,
otel,
rate_limiting_interval,
rate_limiting_limit,
rate_limiting_technique,
retry_backoff,
retry_delay,
retry_max_attempts,
stripe,
workers_ai_billing_mode,
zdr
FROM cloudflare.ai_gateway.gateways
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all AI Gateway evaluator types configured for the account.

```sql
SELECT
id,
store_id,
authentication,
cache_invalidate_on_update,
cache_ttl,
collect_logs,
created_at,
dlp,
is_default,
log_management,
log_management_strategy,
logpush,
logpush_public_key,
modified_at,
otel,
rate_limiting_interval,
rate_limiting_limit,
rate_limiting_technique,
retry_backoff,
retry_delay,
retry_max_attempts,
stripe,
workers_ai_billing_mode,
zdr
FROM cloudflare.ai_gateway.gateways
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND search = '{{ search }}'
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

Creates a new AI Gateway.

```sql
INSERT INTO cloudflare.ai_gateway.gateways (
authentication,
cache_invalidate_on_update,
cache_ttl,
collect_logs,
id,
log_management,
log_management_strategy,
logpush,
logpush_public_key,
rate_limiting_interval,
rate_limiting_limit,
rate_limiting_technique,
retry_backoff,
retry_delay,
retry_max_attempts,
workers_ai_billing_mode,
zdr,
account_id
)
SELECT 
{{ authentication }},
{{ cache_invalidate_on_update }} /* required */,
{{ cache_ttl }} /* required */,
{{ collect_logs }} /* required */,
'{{ id }}' /* required */,
{{ log_management }},
'{{ log_management_strategy }}',
{{ logpush }},
'{{ logpush_public_key }}',
{{ rate_limiting_interval }} /* required */,
{{ rate_limiting_limit }} /* required */,
'{{ rate_limiting_technique }}',
'{{ retry_backoff }}',
{{ retry_delay }},
{{ retry_max_attempts }},
'{{ workers_ai_billing_mode }}',
{{ zdr }},
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: gateways
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the gateways resource.
    - name: authentication
      value: {{ authentication }}
    - name: cache_invalidate_on_update
      value: {{ cache_invalidate_on_update }}
    - name: cache_ttl
      value: {{ cache_ttl }}
    - name: collect_logs
      value: {{ collect_logs }}
    - name: id
      value: "{{ id }}"
      description: |
        gateway id
    - name: log_management
      value: {{ log_management }}
    - name: log_management_strategy
      value: "{{ log_management_strategy }}"
      valid_values: ['STOP_INSERTING', 'DELETE_OLDEST']
    - name: logpush
      value: {{ logpush }}
    - name: logpush_public_key
      value: "{{ logpush_public_key }}"
    - name: rate_limiting_interval
      value: {{ rate_limiting_interval }}
    - name: rate_limiting_limit
      value: {{ rate_limiting_limit }}
    - name: rate_limiting_technique
      value: "{{ rate_limiting_technique }}"
      valid_values: ['fixed', 'sliding']
    - name: retry_backoff
      value: "{{ retry_backoff }}"
      description: |
        Backoff strategy for retry delays
      valid_values: ['constant', 'linear', 'exponential']
    - name: retry_delay
      value: {{ retry_delay }}
      description: |
        Delay between retry attempts in milliseconds (0-5000)
    - name: retry_max_attempts
      value: {{ retry_max_attempts }}
      description: |
        Maximum number of retry attempts for failed requests (1-5)
    - name: workers_ai_billing_mode
      value: "{{ workers_ai_billing_mode }}"
      description: |
        Controls how Workers AI inference calls routed through this gateway are billed. Only 'postpaid' is currently supported.
      valid_values: ['postpaid']
      default: postpaid
    - name: zdr
      value: {{ zdr }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates an existing AI Gateway dataset.

```sql
REPLACE cloudflare.ai_gateway.gateways
SET 
authentication = {{ authentication }},
cache_invalidate_on_update = {{ cache_invalidate_on_update }},
cache_ttl = {{ cache_ttl }},
collect_logs = {{ collect_logs }},
dlp = '{{ dlp }}',
log_management = {{ log_management }},
log_management_strategy = '{{ log_management_strategy }}',
logpush = {{ logpush }},
logpush_public_key = '{{ logpush_public_key }}',
otel = '{{ otel }}',
rate_limiting_interval = {{ rate_limiting_interval }},
rate_limiting_limit = {{ rate_limiting_limit }},
rate_limiting_technique = '{{ rate_limiting_technique }}',
retry_backoff = '{{ retry_backoff }}',
retry_delay = {{ retry_delay }},
retry_max_attempts = {{ retry_max_attempts }},
store_id = '{{ store_id }}',
stripe = '{{ stripe }}',
workers_ai_billing_mode = '{{ workers_ai_billing_mode }}',
zdr = {{ zdr }}
WHERE 
account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
AND rate_limiting_interval = '{{ rate_limiting_interval }}' --required
AND rate_limiting_limit = '{{ rate_limiting_limit }}' --required
AND collect_logs = {{ collect_logs }} --required
AND cache_ttl = '{{ cache_ttl }}' --required
AND cache_invalidate_on_update = {{ cache_invalidate_on_update }} --required
RETURNING
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

Deletes an AI Gateway dataset.

```sql
DELETE FROM cloudflare.ai_gateway.gateways
WHERE account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
;
```
</TabItem>
</Tabs>
