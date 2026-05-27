--- 
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - cloudforce_one
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

Creates, updates, deletes, gets or lists a <code>queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="queries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.queries" /></td></tr>
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

Returns the event query.

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
    <td><code>integer</code></td>
    <td>Unique identifier for the saved query</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the saved query</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>integer</code></td>
    <td>Account ID</td>
</tr>
<tr>
    <td><CopyableCode code="custom_threat_feed_id" /></td>
    <td><code>integer</code></td>
    <td>Intel Indicator Feed ID (numeric)</td>
</tr>
<tr>
    <td><CopyableCode code="rule_list_id" /></td>
    <td><code>string</code></td>
    <td>WAF rules list ID for blocking</td>
</tr>
<tr>
    <td><CopyableCode code="alert_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether alerts are enabled</td>
</tr>
<tr>
    <td><CopyableCode code="alert_rollup_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether alert rollup is enabled</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>Creation timestamp</td>
</tr>
<tr>
    <td><CopyableCode code="query_json" /></td>
    <td><code>string</code></td>
    <td>JSON string containing the query parameters</td>
</tr>
<tr>
    <td><CopyableCode code="rule_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether rule is enabled</td>
</tr>
<tr>
    <td><CopyableCode code="rule_scope" /></td>
    <td><code>string</code></td>
    <td>Scope for the rule</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>Last update timestamp</td>
</tr>
<tr>
    <td><CopyableCode code="user_email" /></td>
    <td><code>string</code></td>
    <td>Email of the user who created the query</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns a list of event queries.

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
    <td><code>integer</code></td>
    <td>Unique identifier for the saved query</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the saved query</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>integer</code></td>
    <td>Account ID</td>
</tr>
<tr>
    <td><CopyableCode code="custom_threat_feed_id" /></td>
    <td><code>integer</code></td>
    <td>Intel Indicator Feed ID (numeric)</td>
</tr>
<tr>
    <td><CopyableCode code="rule_list_id" /></td>
    <td><code>string</code></td>
    <td>WAF rules list ID for blocking</td>
</tr>
<tr>
    <td><CopyableCode code="alert_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether alerts are enabled</td>
</tr>
<tr>
    <td><CopyableCode code="alert_rollup_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether alert rollup is enabled</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>Creation timestamp</td>
</tr>
<tr>
    <td><CopyableCode code="query_json" /></td>
    <td><code>string</code></td>
    <td>JSON string containing the query parameters</td>
</tr>
<tr>
    <td><CopyableCode code="rule_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether rule is enabled</td>
</tr>
<tr>
    <td><CopyableCode code="rule_scope" /></td>
    <td><code>string</code></td>
    <td>Scope for the rule</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>Last update timestamp</td>
</tr>
<tr>
    <td><CopyableCode code="user_email" /></td>
    <td><code>string</code></td>
    <td>Email of the user who created the query</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Retrieve a saved event query by its ID</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Retrieve all saved event queries for the account</td>
</tr>
<tr>
    <td><a href="#post_event_query_update"><CopyableCode code="post_event_query_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Update an existing saved event query by its ID</td>
</tr>
<tr>
    <td><a href="#patch_event_query_update"><CopyableCode code="patch_event_query_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Update an existing saved event query by its ID</td>
</tr>
<tr>
    <td><a href="#delete_event_query_delete"><CopyableCode code="delete_event_query_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-query_id"><code>query_id</code></a></td>
    <td></td>
    <td>Delete a saved event query by its ID</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-query_json"><code>query_json</code></a>, <a href="#parameter-alert_enabled"><code>alert_enabled</code></a>, <a href="#parameter-alert_rollup_enabled"><code>alert_rollup_enabled</code></a>, <a href="#parameter-rule_enabled"><code>rule_enabled</code></a></td>
    <td></td>
    <td>Create a new saved event query for the account</td>
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
<tr id="parameter-query_id">
    <td><CopyableCode code="query_id" /></td>
    <td><code>integer</code></td>
    <td>Event query ID</td>
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

Retrieve a saved event query by its ID

```sql
SELECT
id,
name,
account_id,
custom_threat_feed_id,
rule_list_id,
alert_enabled,
alert_rollup_enabled,
created_at,
query_json,
rule_enabled,
rule_scope,
updated_at,
user_email
FROM cloudflare.cloudforce_one.queries
WHERE account_id = '{{ account_id }}' -- required
AND query_id = '{{ query_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve all saved event queries for the account

```sql
SELECT
id,
name,
account_id,
custom_threat_feed_id,
rule_list_id,
alert_enabled,
alert_rollup_enabled,
created_at,
query_json,
rule_enabled,
rule_scope,
updated_at,
user_email
FROM cloudflare.cloudforce_one.queries
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_event_query_update"
    values={[
        { label: 'post_event_query_update', value: 'post_event_query_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_event_query_update">

Update an existing saved event query by its ID

```sql
INSERT INTO cloudflare.cloudforce_one.queries (
alert_enabled,
alert_rollup_enabled,
name,
query_json,
rule_enabled,
rule_scope,
account_id,
query_id
)
SELECT 
{{ alert_enabled }},
{{ alert_rollup_enabled }},
'{{ name }}',
'{{ query_json }}',
{{ rule_enabled }},
'{{ rule_scope }}',
'{{ account_id }}',
'{{ query_id }}'
RETURNING
id,
name,
account_id,
custom_threat_feed_id,
rule_list_id,
alert_enabled,
alert_rollup_enabled,
created_at,
query_json,
rule_enabled,
rule_scope,
updated_at,
user_email
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: queries
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the queries resource.
    - name: query_id
      value: {{ query_id }}
      description: Required parameter for the queries resource.
    - name: alert_enabled
      value: {{ alert_enabled }}
      description: |
        Enable alerts for this query
    - name: alert_rollup_enabled
      value: {{ alert_rollup_enabled }}
      description: |
        Enable alert rollup for this query
    - name: name
      value: "{{ name }}"
      description: |
        Unique name for the saved query
    - name: query_json
      value: "{{ query_json }}"
      description: |
        JSON string containing the query parameters
    - name: rule_enabled
      value: {{ rule_enabled }}
      description: |
        Enable rule for this query
    - name: rule_scope
      value: "{{ rule_scope }}"
      description: |
        Scope for the rule
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="patch_event_query_update"
    values={[
        { label: 'patch_event_query_update', value: 'patch_event_query_update' }
    ]}
>
<TabItem value="patch_event_query_update">

Update an existing saved event query by its ID

```sql
UPDATE cloudflare.cloudforce_one.queries
SET 
alert_enabled = {{ alert_enabled }},
alert_rollup_enabled = {{ alert_rollup_enabled }},
name = '{{ name }}',
query_json = '{{ query_json }}',
rule_enabled = {{ rule_enabled }},
rule_scope = '{{ rule_scope }}'
WHERE 
account_id = '{{ account_id }}' --required
AND query_id = '{{ query_id }}' --required
RETURNING
id,
name,
account_id,
custom_threat_feed_id,
rule_list_id,
alert_enabled,
alert_rollup_enabled,
created_at,
query_json,
rule_enabled,
rule_scope,
updated_at,
user_email;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_event_query_delete"
    values={[
        { label: 'delete_event_query_delete', value: 'delete_event_query_delete' }
    ]}
>
<TabItem value="delete_event_query_delete">

Delete a saved event query by its ID

```sql
DELETE FROM cloudflare.cloudforce_one.queries
WHERE account_id = '{{ account_id }}' --required
AND query_id = '{{ query_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' }
    ]}
>
<TabItem value="create">

Create a new saved event query for the account

```sql
EXEC cloudflare.cloudforce_one.queries.create 
@account_id='{{ account_id }}' --required 
@@json=
'{
"alert_enabled": {{ alert_enabled }}, 
"alert_rollup_enabled": {{ alert_rollup_enabled }}, 
"name": "{{ name }}", 
"query_json": "{{ query_json }}", 
"rule_enabled": {{ rule_enabled }}, 
"rule_scope": "{{ rule_scope }}"
}'
;
```
</TabItem>
</Tabs>
