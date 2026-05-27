--- 
title: custom_ns
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_ns
  - custom_nameservers
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

Creates, updates, deletes, gets or lists a <code>custom_ns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_ns" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.custom_nameservers.custom_ns" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List Account Custom Nameservers response

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
    <td><CopyableCode code="ns_name" /></td>
    <td><code>string (hostname)</code></td>
    <td>The FQDN of the name server. (example: ns1.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_records" /></td>
    <td><code>array</code></td>
    <td>A and AAAA records associated with the nameserver. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="ns_set" /></td>
    <td><code>number</code></td>
    <td>The number of the set that this name server belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Verification status of the nameserver. (moved, pending, verified) (example: verified)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_tag" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List an account's custom nameservers.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ns_name"><code>ns_name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#account_level_custom_nameservers_delete_account_custom_nameserver"><CopyableCode code="account_level_custom_nameservers_delete_account_custom_nameserver" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_ns_id"><code>custom_ns_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-custom_ns_id">
    <td><CopyableCode code="custom_ns_id" /></td>
    <td><code>string (hostname)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List an account's custom nameservers.

```sql
SELECT
ns_name,
dns_records,
ns_set,
status,
zone_tag
FROM cloudflare.custom_nameservers.custom_ns
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

No description available.

```sql
INSERT INTO cloudflare.custom_nameservers.custom_ns (
ns_name,
ns_set,
account_id
)
SELECT 
'{{ ns_name }}' /* required */,
{{ ns_set }},
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
- name: custom_ns
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the custom_ns resource.
    - name: ns_name
      value: "{{ ns_name }}"
      description: |
        The FQDN of the name server.
    - name: ns_set
      value: {{ ns_set }}
      description: |
        The number of the set that this name server belongs to.
      default: 1
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="account_level_custom_nameservers_delete_account_custom_nameserver"
    values={[
        { label: 'account_level_custom_nameservers_delete_account_custom_nameserver', value: 'account_level_custom_nameservers_delete_account_custom_nameserver' }
    ]}
>
<TabItem value="account_level_custom_nameservers_delete_account_custom_nameserver">

No description available.

```sql
DELETE FROM cloudflare.custom_nameservers.custom_ns
WHERE custom_ns_id = '{{ custom_ns_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
