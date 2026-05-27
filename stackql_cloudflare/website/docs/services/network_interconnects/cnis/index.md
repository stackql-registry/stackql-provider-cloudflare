--- 
title: cnis
hide_title: false
hide_table_of_contents: false
keywords:
  - cnis
  - network_interconnects
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

Creates, updates, deletes, gets or lists a <code>cnis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cnis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.network_interconnects.cnis" /></td></tr>
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

CNI's associated data

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Customer account tag</td>
</tr>
<tr>
    <td><CopyableCode code="bgp" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cust_ip" /></td>
    <td><code>string (A.B.C.D/N)</code></td>
    <td>Customer end of the point-to-point link This should always be inside the same prefix as `p2p_ip`. (example: 192.168.3.4/31)</td>
</tr>
<tr>
    <td><CopyableCode code="interconnect" /></td>
    <td><code>string</code></td>
    <td>Interconnect identifier hosting this CNI</td>
</tr>
<tr>
    <td><CopyableCode code="magic" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="p2p_ip" /></td>
    <td><code>string (A.B.C.D/N)</code></td>
    <td>Cloudflare end of the point-to-point link (example: 192.168.3.4/31)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of matching CNI objects

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="account" /></td>
    <td><code>string</code></td>
    <td>Customer account tag</td>
</tr>
<tr>
    <td><CopyableCode code="bgp" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cust_ip" /></td>
    <td><code>string (A.B.C.D/N)</code></td>
    <td>Customer end of the point-to-point link This should always be inside the same prefix as `p2p_ip`. (example: 192.168.3.4/31)</td>
</tr>
<tr>
    <td><CopyableCode code="interconnect" /></td>
    <td><code>string</code></td>
    <td>Interconnect identifier hosting this CNI</td>
</tr>
<tr>
    <td><CopyableCode code="magic" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="p2p_ip" /></td>
    <td><code>string (A.B.C.D/N)</code></td>
    <td>Cloudflare end of the point-to-point link (example: 192.168.3.4/31)</td>
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
    <td><a href="#parameter-cni"><code>cni</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-tunnel_id"><code>tunnel_id</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-interconnect"><code>interconnect</code></a>, <a href="#parameter-account"><code>account</code></a>, <a href="#parameter-magic"><code>magic</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-cni"><code>cni</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-interconnect"><code>interconnect</code></a>, <a href="#parameter-account"><code>account</code></a>, <a href="#parameter-p2p_ip"><code>p2p_ip</code></a>, <a href="#parameter-cust_ip"><code>cust_ip</code></a>, <a href="#parameter-magic"><code>magic</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-cni"><code>cni</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
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
<tr id="parameter-cni">
    <td><CopyableCode code="cni" /></td>
    <td><code>string (uuid)</code></td>
    <td>CNI ID to retrieve information about</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-slot">
    <td><CopyableCode code="slot" /></td>
    <td><code>string</code></td>
    <td>If specified, only show CNIs associated with the specified slot</td>
</tr>
<tr id="parameter-tunnel_id">
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string</code></td>
    <td>If specified, only show cnis associated with the specified tunnel id</td>
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

CNI's associated data

```sql
SELECT
id,
account,
bgp,
cust_ip,
interconnect,
magic,
p2p_ip
FROM cloudflare.network_interconnects.cnis
WHERE cni = '{{ cni }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List of matching CNI objects

```sql
SELECT
id,
account,
bgp,
cust_ip,
interconnect,
magic,
p2p_ip
FROM cloudflare.network_interconnects.cnis
WHERE account_id = '{{ account_id }}' -- required
AND slot = '{{ slot }}'
AND tunnel_id = '{{ tunnel_id }}'
AND cursor = '{{ cursor }}'
AND limit = '{{ limit }}'
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
INSERT INTO cloudflare.network_interconnects.cnis (
account,
bgp,
interconnect,
magic,
account_id
)
SELECT 
'{{ account }}' /* required */,
'{{ bgp }}',
'{{ interconnect }}' /* required */,
'{{ magic }}' /* required */,
'{{ account_id }}'
RETURNING
id,
account,
bgp,
cust_ip,
interconnect,
magic,
p2p_ip
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cnis
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the cnis resource.
    - name: account
      value: "{{ account }}"
      description: |
        Customer account tag
    - name: bgp
      value:
        customer_asn: {{ customer_asn }}
        extra_prefixes:
          - "{{ extra_prefixes }}"
        md5_key: "{{ md5_key }}"
    - name: interconnect
      value: "{{ interconnect }}"
    - name: magic
      value:
        conduit_name: "{{ conduit_name }}"
        description: "{{ description }}"
        mtu: {{ mtu }}
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

No description available.

```sql
REPLACE cloudflare.network_interconnects.cnis
SET 
account = '{{ account }}',
bgp = '{{ bgp }}',
cust_ip = '{{ cust_ip }}',
id = '{{ id }}',
interconnect = '{{ interconnect }}',
magic = '{{ magic }}',
p2p_ip = '{{ p2p_ip }}'
WHERE 
cni = '{{ cni }}' --required
AND account_id = '{{ account_id }}' --required
AND id = '{{ id }}' --required
AND interconnect = '{{ interconnect }}' --required
AND account = '{{ account }}' --required
AND p2p_ip = '{{ p2p_ip }}' --required
AND cust_ip = '{{ cust_ip }}' --required
AND magic = '{{ magic }}' --required
RETURNING
id,
account,
bgp,
cust_ip,
interconnect,
magic,
p2p_ip;
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

No description available.

```sql
DELETE FROM cloudflare.network_interconnects.cnis
WHERE cni = '{{ cni }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
