--- 
title: limits
hide_title: false
hide_table_of_contents: false
keywords:
  - limits
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

Creates, updates, deletes, gets or lists a <code>limits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="limits" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.limits" /></td></tr>
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

Limits retrieved successfully.

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
    <td><CopyableCode code="max_custom_regex_entries" /></td>
    <td><code>integer (int64)</code></td>
    <td>Maximum number of custom regex entries allowed for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="max_dataset_cells" /></td>
    <td><code>integer (int64)</code></td>
    <td>Maximum number of dataset cells allowed for the account, across all EDM and CWL datasets.</td>
</tr>
<tr>
    <td><CopyableCode code="max_document_fingerprints" /></td>
    <td><code>integer (int64)</code></td>
    <td>Maximum number of document fingerprints allowed for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="used_custom_regex_entries" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of custom regex entries currently configured for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="used_dataset_cells" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of dataset cells currently configured for the account, across all EDM and CWL datasets. Document fingerprints do not count towards this limit.</td>
</tr>
<tr>
    <td><CopyableCode code="used_document_fingerprints" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of document fingerprints currently configured for the account.</td>
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
    <td>Retrieves current DLP usage limits and quotas for the account, including maximum allowed counts and current usage for custom entries, dataset cells, and document fingerprints.</td>
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

Retrieves current DLP usage limits and quotas for the account, including maximum allowed counts and current usage for custom entries, dataset cells, and document fingerprints.

```sql
SELECT
max_custom_regex_entries,
max_dataset_cells,
max_document_fingerprints,
used_custom_regex_entries,
used_dataset_cells,
used_document_fingerprints
FROM cloudflare.zero_trust.limits
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
