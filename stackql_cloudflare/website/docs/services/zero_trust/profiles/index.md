--- 
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.profiles" /></td></tr>
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

Get profile response.

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
    <td>The id of the profile (uuid).</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the profile.</td>
</tr>
<tr>
    <td><CopyableCode code="ai_context_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="allowed_match_count" /></td>
    <td><code>integer (int32)</code></td>
    <td>Related DLP policies will trigger when the match count exceeds the number set.</td>
</tr>
<tr>
    <td><CopyableCode code="confidence_threshold" /></td>
    <td><code>string</code></td>
    <td> (low, medium, high, very_high) (default: low)</td>
</tr>
<tr>
    <td><CopyableCode code="context_awareness" /></td>
    <td><code>object</code></td>
    <td>Scan the context of predefined entries to only return matches surrounded by keywords.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the profile was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_classes" /></td>
    <td><code>array</code></td>
    <td>Data classes associated with this profile.</td>
</tr>
<tr>
    <td><CopyableCode code="data_tags" /></td>
    <td><code>array</code></td>
    <td>Data tags associated with this profile.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the profile.</td>
</tr>
<tr>
    <td><CopyableCode code="entries" /></td>
    <td><code>array</code></td>
    <td></td>
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
<tr>
    <td><CopyableCode code="sensitivity_levels" /></td>
    <td><code>array</code></td>
    <td>Sensitivity levels associated with this profile.</td>
</tr>
<tr>
    <td><CopyableCode code="shared_entries" /></td>
    <td><code>array</code></td>
    <td> (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (custom)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the profile was lasted updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List all profiles response.

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
    <td>The id of the profile (uuid).</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the profile.</td>
</tr>
<tr>
    <td><CopyableCode code="ai_context_enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="allowed_match_count" /></td>
    <td><code>integer (int32)</code></td>
    <td>Related DLP policies will trigger when the match count exceeds the number set.</td>
</tr>
<tr>
    <td><CopyableCode code="confidence_threshold" /></td>
    <td><code>string</code></td>
    <td> (low, medium, high, very_high) (default: low)</td>
</tr>
<tr>
    <td><CopyableCode code="context_awareness" /></td>
    <td><code>object</code></td>
    <td>Scan the context of predefined entries to only return matches surrounded by keywords.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the profile was created.</td>
</tr>
<tr>
    <td><CopyableCode code="data_classes" /></td>
    <td><code>array</code></td>
    <td>Data classes associated with this profile.</td>
</tr>
<tr>
    <td><CopyableCode code="data_tags" /></td>
    <td><code>array</code></td>
    <td>Data tags associated with this profile.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the profile.</td>
</tr>
<tr>
    <td><CopyableCode code="entries" /></td>
    <td><code>array</code></td>
    <td></td>
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
<tr>
    <td><CopyableCode code="sensitivity_levels" /></td>
    <td><code>array</code></td>
    <td>Sensitivity levels associated with this profile.</td>
</tr>
<tr>
    <td><CopyableCode code="shared_entries" /></td>
    <td><code>array</code></td>
    <td> (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (custom)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the profile was lasted updated.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Fetches a DLP profile by ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-all"><code>all</code></a></td>
    <td>Lists all DLP profiles in an account.</td>
</tr>
<tr>
    <td><a href="#update_predefined"><CopyableCode code="update_predefined" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Updates a DLP predefined profile. Only supports enabling/disabling entries.</td>
</tr>
<tr>
    <td><a href="#create_config"><CopyableCode code="create_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>This is similar to `update_predefined` but only returns entries that are enabled. This is needed for our terraform API Creates a DLP predefined profile. Only supports enabling/disabling entries.</td>
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
<tr id="parameter-all">
    <td><CopyableCode code="all" /></td>
    <td><code>boolean</code></td>
    <td>Return all profiles, including those that current account does not have access to.</td>
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

Fetches a DLP profile by ID.

```sql
SELECT
id,
name,
ai_context_enabled,
allowed_match_count,
confidence_threshold,
context_awareness,
created_at,
data_classes,
data_tags,
description,
entries,
ocr_enabled,
open_access,
sensitivity_levels,
shared_entries,
type,
updated_at
FROM cloudflare.zero_trust.profiles
WHERE account_id = '{{ account_id }}' -- required
AND profile_id = '{{ profile_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all DLP profiles in an account.

```sql
SELECT
id,
name,
ai_context_enabled,
allowed_match_count,
confidence_threshold,
context_awareness,
created_at,
data_classes,
data_tags,
description,
entries,
ocr_enabled,
open_access,
sensitivity_levels,
shared_entries,
type,
updated_at
FROM cloudflare.zero_trust.profiles
WHERE account_id = '{{ account_id }}' -- required
AND all = '{{ all }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_predefined"
    values={[
        { label: 'update_predefined', value: 'update_predefined' },
        { label: 'create_config', value: 'create_config' }
    ]}
>
<TabItem value="update_predefined">

Updates a DLP predefined profile. Only supports enabling/disabling entries.

```sql
EXEC cloudflare.zero_trust.profiles.update_predefined 
@account_id='{{ account_id }}' --required, 
@profile_id='{{ profile_id }}' --required 
@@json=
'{
"ai_context_enabled": {{ ai_context_enabled }}, 
"allowed_match_count": {{ allowed_match_count }}, 
"confidence_threshold": "{{ confidence_threshold }}", 
"context_awareness": "{{ context_awareness }}", 
"entries": "{{ entries }}", 
"ocr_enabled": {{ ocr_enabled }}
}'
;
```
</TabItem>
<TabItem value="create_config">

This is similar to `update_predefined` but only returns entries that are enabled. This is needed for our terraform API Creates a DLP predefined profile. Only supports enabling/disabling entries.

```sql
EXEC cloudflare.zero_trust.profiles.create_config 
@account_id='{{ account_id }}' --required, 
@profile_id='{{ profile_id }}' --required 
@@json=
'{
"ai_context_enabled": {{ ai_context_enabled }}, 
"allowed_match_count": {{ allowed_match_count }}, 
"confidence_threshold": "{{ confidence_threshold }}", 
"enabled_entries": "{{ enabled_entries }}", 
"entries": "{{ entries }}", 
"ocr_enabled": {{ ocr_enabled }}
}'
;
```
</TabItem>
</Tabs>
