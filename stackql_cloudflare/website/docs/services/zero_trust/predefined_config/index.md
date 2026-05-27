--- 
title: predefined_config
hide_title: false
hide_table_of_contents: false
keywords:
  - predefined_config
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

Creates, updates, deletes, gets or lists a <code>predefined_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="predefined_config" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.predefined_config" /></td></tr>
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

Predefined profile response.

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
    <td><code>string (uuid)</code></td>
    <td>The id of the predefined profile (uuid).</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the predefined profile.</td>
</tr>
<tr>
    <td><CopyableCode code="ai_context_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="allowed_match_count" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="confidence_threshold" /></td>
    <td><code>string</code></td>
    <td> (default: low)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled_entries" /></td>
    <td><code>array</code></td>
    <td>Entries to enable for this predefined profile. Any entries not provided will be disabled.</td>
</tr>
<tr>
    <td><CopyableCode code="entries" /></td>
    <td><code>array</code></td>
    <td>This field has been deprecated for `enabled_entries`.</td>
</tr>
<tr>
    <td><CopyableCode code="ocr_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="open_access" /></td>
    <td><code>boolean</code></td>
    <td>Whether this profile can be accessed by anyone.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>This is similar to `get_predefined` but only returns entries that are enabled. This is needed for our terraform API Fetches a predefined DLP profile by id.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>This is similar to `update_predefined` but only returns entries that are enabled. This is needed for our terraform API Updates a DLP predefined profile. Only supports enabling/disabling entries.</td>
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
<tr id="parameter-profile_id">
    <td><CopyableCode code="profile_id" /></td>
    <td><code>string (uuid)</code></td>
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

This is similar to `get_predefined` but only returns entries that are enabled. This is needed for our terraform API Fetches a predefined DLP profile by id.

```sql
SELECT
id,
name,
ai_context_enabled,
allowed_match_count,
confidence_threshold,
enabled_entries,
entries,
ocr_enabled,
open_access
FROM cloudflare.zero_trust.predefined_config
WHERE account_id = '{{ account_id }}' -- required
AND profile_id = '{{ profile_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' }
    ]}
>
<TabItem value="update_by_account">

This is similar to `update_predefined` but only returns entries that are enabled. This is needed for our terraform API Updates a DLP predefined profile. Only supports enabling/disabling entries.

```sql
REPLACE cloudflare.zero_trust.predefined_config
SET 
ai_context_enabled = {{ ai_context_enabled }},
allowed_match_count = {{ allowed_match_count }},
confidence_threshold = '{{ confidence_threshold }}',
enabled_entries = '{{ enabled_entries }}',
entries = '{{ entries }}',
ocr_enabled = {{ ocr_enabled }}
WHERE 
account_id = '{{ account_id }}' --required
AND profile_id = '{{ profile_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
