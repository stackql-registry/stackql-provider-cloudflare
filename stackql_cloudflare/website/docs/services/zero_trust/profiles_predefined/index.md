--- 
title: profiles_predefined
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_predefined
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

Creates, updates, deletes, gets or lists a <code>profiles_predefined</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="profiles_predefined" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.profiles_predefined" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

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
    <td>Fetches a predefined DLP profile by id.</td>
</tr>
<tr>
    <td><a href="#dlp_profiles_create_predefined_profile"><CopyableCode code="dlp_profiles_create_predefined_profile" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Creates a DLP predefined profile. Only supports enabling/disabling entries.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>This is a no-op as predefined profiles can't be deleted but is needed for our generated terraform API.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Fetches a predefined DLP profile by id.

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
FROM cloudflare.zero_trust.profiles_predefined
WHERE account_id = '{{ account_id }}' -- required
AND profile_id = '{{ profile_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="dlp_profiles_create_predefined_profile"
    values={[
        { label: 'dlp_profiles_create_predefined_profile', value: 'dlp_profiles_create_predefined_profile' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="dlp_profiles_create_predefined_profile">

Creates a DLP predefined profile. Only supports enabling/disabling entries.

```sql
INSERT INTO cloudflare.zero_trust.profiles_predefined (
ai_context_enabled,
allowed_match_count,
confidence_threshold,
context_awareness,
entries,
ocr_enabled,
profile_id,
account_id
)
SELECT 
{{ ai_context_enabled }},
{{ allowed_match_count }},
'{{ confidence_threshold }}',
'{{ context_awareness }}',
'{{ entries }}',
{{ ocr_enabled }},
'{{ profile_id }}' /* required */,
'{{ account_id }}'
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
- name: profiles_predefined
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the profiles_predefined resource.
    - name: ai_context_enabled
      value: {{ ai_context_enabled }}
      default: false
    - name: allowed_match_count
      value: {{ allowed_match_count }}
      default: 0
    - name: confidence_threshold
      value: "{{ confidence_threshold }}"
      default: low
    - name: context_awareness
      description: |
        Scan the context of predefined entries to only return matches surrounded by keywords.
      value:
        enabled: {{ enabled }}
        skip:
          files: {{ files }}
    - name: entries
      value:
        - enabled: {{ enabled }}
          id: "{{ id }}"
    - name: ocr_enabled
      value: {{ ocr_enabled }}
      default: false
    - name: profile_id
      value: "{{ profile_id }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' }
    ]}
>
<TabItem value="delete_by_account">

This is a no-op as predefined profiles can't be deleted but is needed for our generated terraform API.

```sql
DELETE FROM cloudflare.zero_trust.profiles_predefined
WHERE account_id = '{{ account_id }}' --required
AND profile_id = '{{ profile_id }}' --required
;
```
</TabItem>
</Tabs>
