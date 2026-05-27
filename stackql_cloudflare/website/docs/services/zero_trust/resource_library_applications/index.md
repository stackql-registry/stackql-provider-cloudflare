--- 
title: resource_library_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_library_applications
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

Creates, updates, deletes, gets or lists a <code>resource_library_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="resource_library_applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.resource_library_applications" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Get the application response.

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
    <td>Returns the application ID. (example: 12345678-1234-1234-1234-123456789012)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Returns the application name. (example: HR)</td>
</tr>
<tr>
    <td><CopyableCode code="human_id" /></td>
    <td><code>string</code></td>
    <td>Returns the human readable ID. (example: HR)</td>
</tr>
<tr>
    <td><CopyableCode code="intel_id" /></td>
    <td><code>integer (int64)</code></td>
    <td>Returns the Intel API ID for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="application_confidence_score" /></td>
    <td><code>number (float)</code></td>
    <td>Confidence score for the application. Returns -1 when no score is available.</td>
</tr>
<tr>
    <td><CopyableCode code="application_score_composition" /></td>
    <td><code>object</code></td>
    <td>Returns the score composition breakdown for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="application_source" /></td>
    <td><code>string</code></td>
    <td>Returns the application source. (example: cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="application_type" /></td>
    <td><code>string</code></td>
    <td>Returns the application type. (example: Human Resources)</td>
</tr>
<tr>
    <td><CopyableCode code="application_type_description" /></td>
    <td><code>string</code></td>
    <td>Returns the application type description. (example: Applications used to manage employees and workforce tools.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>Returns the application creation time. (example: 2025-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="gen_ai_score" /></td>
    <td><code>number (float)</code></td>
    <td>GenAI score for the application. Returns -1 when no score is available.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnames" /></td>
    <td><code>array</code></td>
    <td>Returns the list of hostnames for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_subnets" /></td>
    <td><code>array</code></td>
    <td>Returns the list of IP subnets for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="port_protocols" /></td>
    <td><code>array</code></td>
    <td>Returns the list of port protocols for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="support_domains" /></td>
    <td><code>array</code></td>
    <td>Returns the list of support domains for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>Returns the application update time. (example: 2025-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Returns the application version. (example: 2025-01-01T00:00:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get the application response.

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
    <td>Returns the application ID. (example: 12345678-1234-1234-1234-123456789012)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Returns the application name. (example: HR)</td>
</tr>
<tr>
    <td><CopyableCode code="human_id" /></td>
    <td><code>string</code></td>
    <td>Returns the human readable ID. (example: HR)</td>
</tr>
<tr>
    <td><CopyableCode code="intel_id" /></td>
    <td><code>integer (int64)</code></td>
    <td>Returns the Intel API ID for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="application_confidence_score" /></td>
    <td><code>number (float)</code></td>
    <td>Confidence score for the application. Returns -1 when no score is available.</td>
</tr>
<tr>
    <td><CopyableCode code="application_score_composition" /></td>
    <td><code>object</code></td>
    <td>Returns the score composition breakdown for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="application_source" /></td>
    <td><code>string</code></td>
    <td>Returns the application source. (example: cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="application_type" /></td>
    <td><code>string</code></td>
    <td>Returns the application type. (example: Human Resources)</td>
</tr>
<tr>
    <td><CopyableCode code="application_type_description" /></td>
    <td><code>string</code></td>
    <td>Returns the application type description. (example: Applications used to manage employees and workforce tools.)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>Returns the application creation time. (example: 2025-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="gen_ai_score" /></td>
    <td><code>number (float)</code></td>
    <td>GenAI score for the application. Returns -1 when no score is available.</td>
</tr>
<tr>
    <td><CopyableCode code="hostnames" /></td>
    <td><code>array</code></td>
    <td>Returns the list of hostnames for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_subnets" /></td>
    <td><code>array</code></td>
    <td>Returns the list of IP subnets for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="port_protocols" /></td>
    <td><code>array</code></td>
    <td>Returns the list of port protocols for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="support_domains" /></td>
    <td><code>array</code></td>
    <td>Returns the list of support domains for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>Returns the application update time. (example: 2025-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Returns the application version. (example: 2025-01-01T00:00:00Z)</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Get application by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-order_by"><code>order_by</code></a></td>
    <td>List applications with different filters.</td>
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
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Filter applications using key:value format. Supported filter keys: - name: Filter by application name (e.g., name:HR) - id: Filter by application ID (e.g., id:0b63249c-95bf-4cc0-a7cc-d7faaaf1dac0) - human_id: Filter by human-readable ID (e.g., human_id:HR) - hostname: Filter by hostname or support domain (e.g., hostname:portal.example.com) - source: Filter by application source name (e.g., source:cloudflare) - ip_subnet: Filter by IP subnet using CIDR containment — returns applications where any stored subnet contains the search value (e.g., ip_subnet:10.0.1.5/32 matches apps with 10.0.0.0/16) - intel_id: Filter by Intel API ID (e.g., intel_id:498). .</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Limit of number of results to return (max 250).</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>Offset of results to return.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>Order by result by field name and order (e.g., name:asc).</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Get application by ID.

```sql
SELECT
id,
name,
human_id,
intel_id,
application_confidence_score,
application_score_composition,
application_source,
application_type,
application_type_description,
created_at,
gen_ai_score,
hostnames,
ip_subnets,
port_protocols,
support_domains,
updated_at,
version
FROM cloudflare.zero_trust.resource_library_applications
WHERE account_id = '{{ account_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List applications with different filters.

```sql
SELECT
id,
name,
human_id,
intel_id,
application_confidence_score,
application_score_composition,
application_source,
application_type,
application_type_description,
created_at,
gen_ai_score,
hostnames,
ip_subnets,
port_protocols,
support_domains,
updated_at,
version
FROM cloudflare.zero_trust.resource_library_applications
WHERE account_id = '{{ account_id }}' -- required
AND filter = '{{ filter }}'
AND limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND order_by = '{{ order_by }}'
;
```
</TabItem>
</Tabs>
