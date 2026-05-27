--- 
title: integration
hide_title: false
hide_table_of_contents: false
keywords:
  - integration
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

Creates, updates, deletes, gets or lists an <code>integration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.integration" /></td></tr>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-entry_id"><code>entry_id</code></a></td>
    <td></td>
    <td>Integration entries can't be created, this will update an existing integration entry. This is needed for our generated terraform API.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-entry_id"><code>entry_id</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Updates a DLP entry.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-entry_id"><code>entry_id</code></a></td>
    <td></td>
    <td>This is a no-op as integration entires can't be deleted but is needed for our generated terraform API.</td>
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
<tr id="parameter-entry_id">
    <td><CopyableCode code="entry_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
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

Integration entries can't be created, this will update an existing integration entry. This is needed for our generated terraform API.

```sql
INSERT INTO cloudflare.zero_trust.integration (
enabled,
entry_id,
profile_id,
account_id
)
SELECT 
{{ enabled }} /* required */,
'{{ entry_id }}' /* required */,
'{{ profile_id }}',
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
- name: integration
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the integration resource.
    - name: enabled
      value: {{ enabled }}
    - name: entry_id
      value: "{{ entry_id }}"
    - name: profile_id
      value: "{{ profile_id }}"
      description: |
        This field is not used as the owning profile. For predefined entries it is already set to a predefined profile.
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

Updates a DLP entry.

```sql
REPLACE cloudflare.zero_trust.integration
SET 
enabled = {{ enabled }}
WHERE 
account_id = '{{ account_id }}' --required
AND entry_id = '{{ entry_id }}' --required
AND enabled = {{ enabled }} --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

This is a no-op as integration entires can't be deleted but is needed for our generated terraform API.

```sql
DELETE FROM cloudflare.zero_trust.integration
WHERE account_id = '{{ account_id }}' --required
AND entry_id = '{{ entry_id }}' --required
;
```
</TabItem>
</Tabs>
