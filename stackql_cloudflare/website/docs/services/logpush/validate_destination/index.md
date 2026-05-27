--- 
title: validate_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - validate_destination
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

Creates, updates, deletes, gets or lists a <code>validate_destination</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="validate_destination" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logpush.validate_destination" /></td></tr>
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
    <td><a href="#destination_by_account"><CopyableCode code="destination_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Validates destination.</td>
</tr>
<tr>
    <td><a href="#destination_by_zone"><CopyableCode code="destination_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Validates destination.</td>
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
    defaultValue="destination_by_account"
    values={[
        { label: 'destination_by_account', value: 'destination_by_account' },
        { label: 'destination_by_zone', value: 'destination_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="destination_by_account">

Validates destination.

```sql
INSERT INTO cloudflare.logpush.validate_destination (
destination_conf,
account_id
)
SELECT 
'{{ destination_conf }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="destination_by_zone">

Validates destination.

```sql
INSERT INTO cloudflare.logpush.validate_destination (
destination_conf,
zone_id
)
SELECT 
'{{ destination_conf }}' /* required */,
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
- name: validate_destination
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the validate_destination resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the validate_destination resource.
    - name: destination_conf
      value: "{{ destination_conf }}"
      description: |
        Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.
`}</CodeBlock>

</TabItem>
</Tabs>
