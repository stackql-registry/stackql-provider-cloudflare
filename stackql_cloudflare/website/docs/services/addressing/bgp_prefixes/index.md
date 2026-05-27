--- 
title: bgp_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - bgp_prefixes
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

Creates, updates, deletes, gets or lists a <code>bgp_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bgp_prefixes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.bgp_prefixes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Fetch BGP Prefix response

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
    <td><code>string</code></td>
    <td>Identifier of BGP Prefix. (example: 7009ba364c7a5760798ceb430e603b74)</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Autonomous System Number (ASN) the prefix will be advertised under.</td>
</tr>
<tr>
    <td><CopyableCode code="asn_prepend_count" /></td>
    <td><code>integer</code></td>
    <td>Number of times to prepend the Cloudflare ASN to the BGP AS-Path attribute</td>
</tr>
<tr>
    <td><CopyableCode code="auto_advertise_withdraw" /></td>
    <td><code>boolean</code></td>
    <td>Determines if Cloudflare advertises a BYOIP BGP prefix even when there is no matching BGP prefix in the Magic routing table. When true, Cloudflare will automatically withdraw the BGP prefix when there are no matching BGP routes, and will resume advertising when there is at least one matching BGP route.</td>
</tr>
<tr>
    <td><CopyableCode code="bgp_signal_opts" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="on_demand" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List BGP Prefixes response

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
    <td><code>string</code></td>
    <td>Identifier of BGP Prefix. (example: 7009ba364c7a5760798ceb430e603b74)</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Autonomous System Number (ASN) the prefix will be advertised under.</td>
</tr>
<tr>
    <td><CopyableCode code="asn_prepend_count" /></td>
    <td><code>integer</code></td>
    <td>Number of times to prepend the Cloudflare ASN to the BGP AS-Path attribute</td>
</tr>
<tr>
    <td><CopyableCode code="auto_advertise_withdraw" /></td>
    <td><code>boolean</code></td>
    <td>Determines if Cloudflare advertises a BYOIP BGP prefix even when there is no matching BGP prefix in the Magic routing table. When true, Cloudflare will automatically withdraw the BGP prefix when there are no matching BGP routes, and will resume advertising when there is at least one matching BGP route.</td>
</tr>
<tr>
    <td><CopyableCode code="bgp_signal_opts" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="on_demand" /></td>
    <td><code>object</code></td>
    <td></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-bgp_prefix_id"><code>bgp_prefix_id</code></a></td>
    <td></td>
    <td>Retrieve a single BGP Prefix according to its identifier</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a></td>
    <td></td>
    <td>List all BGP Prefixes within the specified IP Prefix. BGP Prefixes are used to control which specific subnets are advertised to the Internet. It is possible to advertise subnets more specific than an IP Prefix by creating more specific BGP Prefixes.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-cidr"><code>cidr</code></a></td>
    <td></td>
    <td>Create a BGP prefix, controlling the BGP advertisement status of a specific subnet. When created, BGP prefixes are initially withdrawn, and can be advertised with the Update BGP Prefix API.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-bgp_prefix_id"><code>bgp_prefix_id</code></a></td>
    <td></td>
    <td>Update the properties of a BGP Prefix, such as the on demand advertisement status (advertised or withdrawn).</td>
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
<tr id="parameter-bgp_prefix_id">
    <td><CopyableCode code="bgp_prefix_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-prefix_id">
    <td><CopyableCode code="prefix_id" /></td>
    <td><code>string</code></td>
    <td>The IP prefix ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieve a single BGP Prefix according to its identifier

```sql
SELECT
id,
asn,
asn_prepend_count,
auto_advertise_withdraw,
bgp_signal_opts,
cidr,
created_at,
modified_at,
on_demand
FROM cloudflare.addressing.bgp_prefixes
WHERE account_id = '{{ account_id }}' -- required
AND prefix_id = '{{ prefix_id }}' -- required
AND bgp_prefix_id = '{{ bgp_prefix_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all BGP Prefixes within the specified IP Prefix. BGP Prefixes are used to control which specific subnets are advertised to the Internet. It is possible to advertise subnets more specific than an IP Prefix by creating more specific BGP Prefixes.

```sql
SELECT
id,
asn,
asn_prepend_count,
auto_advertise_withdraw,
bgp_signal_opts,
cidr,
created_at,
modified_at,
on_demand
FROM cloudflare.addressing.bgp_prefixes
WHERE account_id = '{{ account_id }}' -- required
AND prefix_id = '{{ prefix_id }}' -- required
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

Create a BGP prefix, controlling the BGP advertisement status of a specific subnet. When created, BGP prefixes are initially withdrawn, and can be advertised with the Update BGP Prefix API.

```sql
INSERT INTO cloudflare.addressing.bgp_prefixes (
cidr,
account_id,
prefix_id
)
SELECT 
'{{ cidr }}' /* required */,
'{{ account_id }}',
'{{ prefix_id }}'
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
- name: bgp_prefixes
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the bgp_prefixes resource.
    - name: prefix_id
      value: "{{ prefix_id }}"
      description: Required parameter for the bgp_prefixes resource.
    - name: cidr
      value: "{{ cidr }}"
      description: |
        IP Prefix in Classless Inter-Domain Routing format.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Update the properties of a BGP Prefix, such as the on demand advertisement status (advertised or withdrawn).

```sql
UPDATE cloudflare.addressing.bgp_prefixes
SET 
asn_prepend_count = {{ asn_prepend_count }},
auto_advertise_withdraw = {{ auto_advertise_withdraw }},
on_demand = '{{ on_demand }}'
WHERE 
account_id = '{{ account_id }}' --required
AND prefix_id = '{{ prefix_id }}' --required
AND bgp_prefix_id = '{{ bgp_prefix_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
