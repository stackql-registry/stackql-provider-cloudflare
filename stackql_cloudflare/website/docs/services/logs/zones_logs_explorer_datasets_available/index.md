--- 
title: zones_logs_explorer_datasets_available
hide_title: false
hide_table_of_contents: false
keywords:
  - zones_logs_explorer_datasets_available
  - logs
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

Creates, updates, deletes, gets or lists a <code>zones_logs_explorer_datasets_available</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zones_logs_explorer_datasets_available" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logs.zones_logs_explorer_datasets_available" /></td></tr>
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

List of dataset types available to create.

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
    <td><CopyableCode code="dataset" /></td>
    <td><code>string</code></td>
    <td>Dataset type name (e.g. `http_requests`).</td>
</tr>
<tr>
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>Whether this dataset type is account-scoped or zone-scoped. (account, zone)</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code>object</code></td>
    <td>JSON Schema that describes the fields this dataset exposes.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp_field" /></td>
    <td><code>string</code></td>
    <td>The primary timestamp field name for this dataset.</td>
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
    <td>Returns all dataset types that this account or zone can create. Each entry includes the dataset schema and timestamp field. The schema shows all possible fields for a dataset. However, not all fields may be available for your account or zone. When creating or updating a dataset, only fields available to your account or zone can be enabled. If you request a field that is not available, you will receive an error.</td>
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

Returns all dataset types that this account or zone can create. Each entry includes the dataset schema and timestamp field. The schema shows all possible fields for a dataset. However, not all fields may be available for your account or zone. When creating or updating a dataset, only fields available to your account or zone can be enabled. If you request a field that is not available, you will receive an error.

```sql
SELECT
dataset,
object_type,
schema,
timestamp_field
FROM cloudflare.logs.zones_logs_explorer_datasets_available
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
