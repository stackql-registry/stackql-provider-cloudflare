--- 
title: profiles_custom
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_custom
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

Creates, updates, deletes, gets or lists a <code>profiles_custom</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="profiles_custom" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.profiles_custom" /></td></tr>
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

Custom profile response.

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

List all custom profiles response.

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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Fetches a custom DLP profile by id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all DLP custom profiles in an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a DLP custom profile.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Updates a DLP custom profile.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-profile_id"><code>profile_id</code></a></td>
    <td></td>
    <td>Deletes a DLP custom profile.</td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Fetches a custom DLP profile by id.

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
FROM cloudflare.zero_trust.profiles_custom
WHERE account_id = '{{ account_id }}' -- required
AND profile_id = '{{ profile_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all DLP custom profiles in an account.

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
sensitivity_levels,
shared_entries,
updated_at
FROM cloudflare.zero_trust.profiles_custom
WHERE account_id = '{{ account_id }}' -- required
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

Creates a DLP custom profile.

```sql
INSERT INTO cloudflare.zero_trust.profiles_custom (
ai_context_enabled,
allowed_match_count,
confidence_threshold,
context_awareness,
data_classes,
data_tags,
description,
entries,
name,
ocr_enabled,
sensitivity_levels,
shared_entries,
account_id
)
SELECT 
{{ ai_context_enabled }},
{{ allowed_match_count }},
'{{ confidence_threshold }}',
'{{ context_awareness }}',
'{{ data_classes }}',
'{{ data_tags }}',
'{{ description }}',
'{{ entries }}',
'{{ name }}' /* required */,
{{ ocr_enabled }},
'{{ sensitivity_levels }}',
'{{ shared_entries }}',
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
- name: profiles_custom
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the profiles_custom resource.
    - name: ai_context_enabled
      value: {{ ai_context_enabled }}
      default: false
    - name: allowed_match_count
      value: {{ allowed_match_count }}
      description: |
        Related DLP policies will trigger when the match count exceeds the number set.
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
    - name: data_classes
      value:
        - "{{ data_classes }}"
      description: |
        Data class IDs to associate with the profile.
    - name: data_tags
      value:
        - "{{ data_tags }}"
      description: |
        Data tag IDs to associate with the profile.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the profile.
    - name: entries
      value:
        - description: "{{ description }}"
          enabled: {{ enabled }}
          name: "{{ name }}"
          pattern:
            regex: "{{ regex }}"
            validation: "{{ validation }}"
          words: "{{ words }}"
    - name: name
      value: "{{ name }}"
    - name: ocr_enabled
      value: {{ ocr_enabled }}
      default: false
    - name: sensitivity_levels
      description: |
        Sensitivity levels to associate with the profile.
      value:
        - group_id: "{{ group_id }}"
          level_id: "{{ level_id }}"
    - name: shared_entries
      description: |
        Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
      value:
        - enabled: {{ enabled }}
          entry_id: "{{ entry_id }}"
`}</CodeBlock>

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

Updates a DLP custom profile.

```sql
REPLACE cloudflare.zero_trust.profiles_custom
SET 
ai_context_enabled = {{ ai_context_enabled }},
allowed_match_count = {{ allowed_match_count }},
confidence_threshold = '{{ confidence_threshold }}',
context_awareness = '{{ context_awareness }}',
data_classes = '{{ data_classes }}',
data_tags = '{{ data_tags }}',
description = '{{ description }}',
entries = '{{ entries }}',
name = '{{ name }}',
ocr_enabled = {{ ocr_enabled }},
sensitivity_levels = '{{ sensitivity_levels }}',
shared_entries = '{{ shared_entries }}'
WHERE 
account_id = '{{ account_id }}' --required
AND profile_id = '{{ profile_id }}' --required
AND name = '{{ name }}' --required
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
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' }
    ]}
>
<TabItem value="delete_by_account">

Deletes a DLP custom profile.

```sql
DELETE FROM cloudflare.zero_trust.profiles_custom
WHERE account_id = '{{ account_id }}' --required
AND profile_id = '{{ profile_id }}' --required
;
```
</TabItem>
</Tabs>
