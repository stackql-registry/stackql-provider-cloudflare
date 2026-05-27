--- 
title: bulk
hide_title: false
hide_table_of_contents: false
keywords:
  - bulk
  - token_validation
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

Creates, updates, deletes, gets or lists a <code>bulk</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bulk" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.token_validation.bulk" /></td></tr>
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
    <td><a href="#token_validation_rules_bulk_create"><CopyableCode code="token_validation_rules_bulk_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Create zone token validation rules. A request can create multiple Token Validation Rules.</td>
</tr>
<tr>
    <td><a href="#token_validation_rules_bulk_edit"><CopyableCode code="token_validation_rules_bulk_edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Edit token validation rules. A request can update multiple Token Validation Rules. Rules can be re-ordered using the `position` field. Returns all updated rules.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="token_validation_rules_bulk_create"
    values={[
        { label: 'token_validation_rules_bulk_create', value: 'token_validation_rules_bulk_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="token_validation_rules_bulk_create">

Create zone token validation rules. A request can create multiple Token Validation Rules.

```sql
INSERT INTO cloudflare.token_validation.bulk (
zone_id
)
SELECT 
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: bulk
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the bulk resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="token_validation_rules_bulk_edit"
    values={[
        { label: 'token_validation_rules_bulk_edit', value: 'token_validation_rules_bulk_edit' }
    ]}
>
<TabItem value="token_validation_rules_bulk_edit">

Edit token validation rules. A request can update multiple Token Validation Rules. Rules can be re-ordered using the `position` field. Returns all updated rules.

```sql
UPDATE cloudflare.token_validation.bulk
SET 
-- No updatable properties
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>
