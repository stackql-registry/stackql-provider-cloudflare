--- 
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tags" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cloudforce_one.tags" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td></td>
    <td>Creates a new tag to be used accross threat events.</td>
</tr>
<tr>
    <td><a href="#patch_tag_update"><CopyableCode code="patch_tag_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tag_uuid"><code>tag_uuid</code></a></td>
    <td></td>
    <td>Updates a Source-of-Truth tag by UUID.</td>
</tr>
<tr>
    <td><a href="#delete_tag_delete"><CopyableCode code="delete_tag_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-tag_uuid"><code>tag_uuid</code></a></td>
    <td></td>
    <td>Deletes a Source-of-Truth tag by UUID.</td>
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
<tr id="parameter-tag_uuid">
    <td><CopyableCode code="tag_uuid" /></td>
    <td><code>string</code></td>
    <td>Tag UUID.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a new tag to be used accross threat events.

```sql
INSERT INTO cloudflare.cloudforce_one.tags (
activeDuration,
actorCategory,
aliasGroupNames,
aliasGroupNamesInternal,
analyticPriority,
attributionConfidence,
attributionOrganization,
categoryUuid,
externalReferenceLinks,
internalDescription,
motive,
opsecLevel,
originCountryISO,
priority,
sophisticationLevel,
value,
account_id
)
SELECT 
'{{ activeDuration }}',
'{{ actorCategory }}',
'{{ aliasGroupNames }}',
'{{ aliasGroupNamesInternal }}',
{{ analyticPriority }},
'{{ attributionConfidence }}',
'{{ attributionOrganization }}',
'{{ categoryUuid }}',
'{{ externalReferenceLinks }}',
'{{ internalDescription }}',
'{{ motive }}',
'{{ opsecLevel }}',
'{{ originCountryISO }}',
{{ priority }},
'{{ sophisticationLevel }}',
'{{ value }}' /* required */,
'{{ account_id }}'
RETURNING
activeDuration,
actorCategory,
aliasGroupNames,
aliasGroupNamesInternal,
analyticPriority,
attributionConfidence,
attributionOrganization,
categoryName,
categoryUuid,
externalReferenceLinks,
internalDescription,
motive,
opsecLevel,
originCountryISO,
priority,
sophisticationLevel,
uuid,
value
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tags
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the tags resource.
    - name: activeDuration
      value: "{{ activeDuration }}"
    - name: actorCategory
      value: "{{ actorCategory }}"
    - name: aliasGroupNames
      value:
        - "{{ aliasGroupNames }}"
    - name: aliasGroupNamesInternal
      value:
        - "{{ aliasGroupNamesInternal }}"
    - name: analyticPriority
      value: {{ analyticPriority }}
    - name: attributionConfidence
      value: "{{ attributionConfidence }}"
    - name: attributionOrganization
      value: "{{ attributionOrganization }}"
    - name: categoryUuid
      value: "{{ categoryUuid }}"
    - name: externalReferenceLinks
      value:
        - "{{ externalReferenceLinks }}"
    - name: internalDescription
      value: "{{ internalDescription }}"
    - name: motive
      value: "{{ motive }}"
    - name: opsecLevel
      value: "{{ opsecLevel }}"
    - name: originCountryISO
      value: "{{ originCountryISO }}"
    - name: priority
      value: {{ priority }}
    - name: sophisticationLevel
      value: "{{ sophisticationLevel }}"
    - name: value
      value: "{{ value }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="patch_tag_update"
    values={[
        { label: 'patch_tag_update', value: 'patch_tag_update' }
    ]}
>
<TabItem value="patch_tag_update">

Updates a Source-of-Truth tag by UUID.

```sql
UPDATE cloudflare.cloudforce_one.tags
SET 
activeDuration = '{{ activeDuration }}',
actorCategory = '{{ actorCategory }}',
aliasGroupNames = '{{ aliasGroupNames }}',
aliasGroupNamesInternal = '{{ aliasGroupNamesInternal }}',
analyticPriority = {{ analyticPriority }},
attributionConfidence = '{{ attributionConfidence }}',
attributionOrganization = '{{ attributionOrganization }}',
categoryUuid = '{{ categoryUuid }}',
externalReferenceLinks = '{{ externalReferenceLinks }}',
internalDescription = '{{ internalDescription }}',
motive = '{{ motive }}',
opsecLevel = '{{ opsecLevel }}',
originCountryISO = '{{ originCountryISO }}',
priority = {{ priority }},
sophisticationLevel = '{{ sophisticationLevel }}',
value = '{{ value }}'
WHERE 
account_id = '{{ account_id }}' --required
AND tag_uuid = '{{ tag_uuid }}' --required
RETURNING
activeDuration,
actorCategory,
aliasGroupNames,
aliasGroupNamesInternal,
analyticPriority,
attributionConfidence,
attributionOrganization,
categoryName,
categoryUuid,
externalReferenceLinks,
internalDescription,
motive,
opsecLevel,
originCountryISO,
priority,
sophisticationLevel,
uuid,
value;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_tag_delete"
    values={[
        { label: 'delete_tag_delete', value: 'delete_tag_delete' }
    ]}
>
<TabItem value="delete_tag_delete">

Deletes a Source-of-Truth tag by UUID.

```sql
DELETE FROM cloudflare.cloudforce_one.tags
WHERE account_id = '{{ account_id }}' --required
AND tag_uuid = '{{ tag_uuid }}' --required
;
```
</TabItem>
</Tabs>
