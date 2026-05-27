--- 
title: validate
hide_title: false
hide_table_of_contents: false
keywords:
  - validate
  - addressing
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

Creates, updates, deletes, gets or lists a <code>validate</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="validate" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.validate" /></td></tr>
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
    <td><a href="#ip_address_management_prefixes_validate_prefix"><CopyableCode code="ip_address_management_prefixes_validate_prefix" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Triggers a new prefix validation. The checks are run asynchronously and include IRR, RPKI, and prefix ownership.</td>
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
<tr id="parameter-prefix_id">
    <td><CopyableCode code="prefix_id" /></td>
    <td><code>string</code></td>
    <td>The IP prefix ID.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="ip_address_management_prefixes_validate_prefix"
    values={[
        { label: 'ip_address_management_prefixes_validate_prefix', value: 'ip_address_management_prefixes_validate_prefix' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="ip_address_management_prefixes_validate_prefix">

Triggers a new prefix validation. The checks are run asynchronously and include IRR, RPKI, and prefix ownership.

```sql
INSERT INTO cloudflare.addressing.validate (
prefix_id,
account_id
)
SELECT 
'{{ prefix_id }}',
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
- name: validate
  props:
    - name: prefix_id
      value: "{{ prefix_id }}"
      description: Required parameter for the validate resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the validate resource.
`}</CodeBlock>

</TabItem>
</Tabs>
