--- 
title: ownership_validate
hide_title: false
hide_table_of_contents: false
keywords:
  - ownership_validate
  - logpush
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

Creates, updates, deletes, gets or lists an <code>ownership_validate</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ownership_validate" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logpush.ownership_validate" /></td></tr>
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
    <td><a href="#validate_by_account"><CopyableCode code="validate_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a>, <a href="#parameter-ownership_challenge"><code>ownership_challenge</code></a></td>
    <td></td>
    <td>Validates ownership challenge of the destination.</td>
</tr>
<tr>
    <td><a href="#validate_by_zone"><CopyableCode code="validate_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a>, <a href="#parameter-ownership_challenge"><code>ownership_challenge</code></a></td>
    <td></td>
    <td>Validates ownership challenge of the destination.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="validate_by_account"
    values={[
        { label: 'validate_by_account', value: 'validate_by_account' },
        { label: 'validate_by_zone', value: 'validate_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="validate_by_account">

Validates ownership challenge of the destination.

```sql
INSERT INTO cloudflare.logpush.ownership_validate (
destination_conf,
ownership_challenge,
account_id
)
SELECT 
'{{ destination_conf }}' /* required */,
'{{ ownership_challenge }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="validate_by_zone">

Validates ownership challenge of the destination.

```sql
INSERT INTO cloudflare.logpush.ownership_validate (
destination_conf,
ownership_challenge,
zone_id
)
SELECT 
'{{ destination_conf }}' /* required */,
'{{ ownership_challenge }}' /* required */,
'{{ zone_id }}'
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
- name: ownership_validate
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the ownership_validate resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the ownership_validate resource.
    - name: destination_conf
      value: "{{ destination_conf }}"
      description: |
        Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.
    - name: ownership_challenge
      value: "{{ ownership_challenge }}"
      description: |
        Ownership challenge token to prove destination ownership.
`}</CodeBlock>

</TabItem>
</Tabs>
