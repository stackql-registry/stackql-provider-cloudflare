--- 
title: validate_origin
hide_title: false
hide_table_of_contents: false
keywords:
  - validate_origin
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

Creates, updates, deletes, gets or lists a <code>validate_origin</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="validate_origin" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logpush.validate_origin" /></td></tr>
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
    <td><a href="#origin_by_account"><CopyableCode code="origin_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-logpull_options"><code>logpull_options</code></a></td>
    <td></td>
    <td>Validates logpull origin with logpull_options.</td>
</tr>
<tr>
    <td><a href="#origin_by_zone"><CopyableCode code="origin_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-logpull_options"><code>logpull_options</code></a></td>
    <td></td>
    <td>Validates logpull origin with logpull_options.</td>
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
    defaultValue="origin_by_account"
    values={[
        { label: 'origin_by_account', value: 'origin_by_account' },
        { label: 'origin_by_zone', value: 'origin_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="origin_by_account">

Validates logpull origin with logpull_options.

```sql
INSERT INTO cloudflare.logpush.validate_origin (
logpull_options,
account_id
)
SELECT 
'{{ logpull_options }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="origin_by_zone">

Validates logpull origin with logpull_options.

```sql
INSERT INTO cloudflare.logpush.validate_origin (
logpull_options,
zone_id
)
SELECT 
'{{ logpull_options }}' /* required */,
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
- name: validate_origin
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the validate_origin resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the validate_origin resource.
    - name: logpull_options
      value: "{{ logpull_options }}"
      description: |
        This field is deprecated. Use \`output_options\` instead. Configuration string. It specifies things like requested fields and timestamp formats. If migrating from the logpull api, copy the url (full url or just the query string) of your call here, and logpush will keep on making this call for you, setting start and end times appropriately.
`}</CodeBlock>

</TabItem>
</Tabs>
