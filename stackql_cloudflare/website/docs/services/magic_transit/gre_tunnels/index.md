--- 
title: gre_tunnels
hide_title: false
hide_table_of_contents: false
keywords:
  - gre_tunnels
  - magic_transit
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

Creates, updates, deletes, gets or lists a <code>gre_tunnels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gre_tunnels" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.gre_tunnels" /></td></tr>
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

List GRE Tunnel Details response

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
    <td><CopyableCode code="gre_tunnel" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List GRE tunnels response

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
    <td>Identifier (example: c4a7362d577a6c3019a474fd6f485821)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the tunnel. The name cannot contain spaces or special characters, must be 15 characters or less, and cannot share a name with another GRE tunnel. (example: GRE_1)</td>
</tr>
<tr>
    <td><CopyableCode code="automatic_return_routing" /></td>
    <td><code>boolean</code></td>
    <td>True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the `coupler_integration` account flag to be enabled; requests setting this to `true` without that flag will be rejected.</td>
</tr>
<tr>
    <td><CopyableCode code="bgp" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="bgp_status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloudflare_gre_endpoint" /></td>
    <td><code>string</code></td>
    <td>The IP address assigned to the Cloudflare side of the GRE tunnel. (example: 203.0.113.1)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the tunnel was created. (example: 2017-06-14T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="customer_gre_endpoint" /></td>
    <td><code>string</code></td>
    <td>The IP address assigned to the customer side of the GRE tunnel. (example: 203.0.113.1)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description of the GRE tunnel. (example: Tunnel for ISP X)</td>
</tr>
<tr>
    <td><CopyableCode code="health_check" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="interface_address" /></td>
    <td><code>string</code></td>
    <td>A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side of the tunnel. Select the subnet from the following private IP space: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255. (example: 192.0.2.0/31)</td>
</tr>
<tr>
    <td><CopyableCode code="interface_address6" /></td>
    <td><code>string</code></td>
    <td>A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127 (example: 2606:54c1:7:0:a9fe:12d2:1:200/127)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the tunnel was last modified. (example: 2017-06-14T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mtu" /></td>
    <td><code>integer</code></td>
    <td>Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value is 576.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>integer</code></td>
    <td>Time To Live (TTL) in number of hops of the GRE tunnel.</td>
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
    <td><a href="#parameter-gre_tunnel_id"><code>gre_tunnel_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Lists informtion for a specific GRE tunnel.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Lists GRE tunnels associated with an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-customer_gre_endpoint"><code>customer_gre_endpoint</code></a>, <a href="#parameter-cloudflare_gre_endpoint"><code>cloudflare_gre_endpoint</code></a>, <a href="#parameter-interface_address"><code>interface_address</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Creates a new GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-gre_tunnel_id"><code>gre_tunnel_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-customer_gre_endpoint"><code>customer_gre_endpoint</code></a>, <a href="#parameter-cloudflare_gre_endpoint"><code>cloudflare_gre_endpoint</code></a>, <a href="#parameter-interface_address"><code>interface_address</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Updates a specific GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.</td>
</tr>
<tr>
    <td><a href="#bulk_update"><CopyableCode code="bulk_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Updates multiple GRE tunnels. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-gre_tunnel_id"><code>gre_tunnel_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-x-magic-new-hc-target"><code>x-magic-new-hc-target</code></a></td>
    <td>Disables and removes a specific static GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.</td>
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
<tr id="parameter-gre_tunnel_id">
    <td><CopyableCode code="gre_tunnel_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-x-magic-new-hc-target">
    <td><CopyableCode code="x-magic-new-hc-target" /></td>
    <td><code>boolean</code></td>
    <td>If true, the health check target in the response body will be presented using the new object format. Defaults to false.</td>
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

Lists informtion for a specific GRE tunnel.

```sql
SELECT
gre_tunnel
FROM cloudflare.magic_transit.gre_tunnels
WHERE gre_tunnel_id = '{{ gre_tunnel_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND x-magic-new-hc-target = '{{ x-magic-new-hc-target }}'
;
```
</TabItem>
<TabItem value="list">

Lists GRE tunnels associated with an account.

```sql
SELECT
id,
name,
automatic_return_routing,
bgp,
bgp_status,
cloudflare_gre_endpoint,
created_on,
customer_gre_endpoint,
description,
health_check,
interface_address,
interface_address6,
modified_on,
mtu,
ttl
FROM cloudflare.magic_transit.gre_tunnels
WHERE account_id = '{{ account_id }}' -- required
AND x-magic-new-hc-target = '{{ x-magic-new-hc-target }}'
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

Creates a new GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

```sql
INSERT INTO cloudflare.magic_transit.gre_tunnels (
automatic_return_routing,
bgp,
cloudflare_gre_endpoint,
customer_gre_endpoint,
description,
health_check,
interface_address,
interface_address6,
mtu,
name,
ttl,
account_id,
x-magic-new-hc-target
)
SELECT 
{{ automatic_return_routing }},
'{{ bgp }}',
'{{ cloudflare_gre_endpoint }}' /* required */,
'{{ customer_gre_endpoint }}' /* required */,
'{{ description }}',
'{{ health_check }}',
'{{ interface_address }}' /* required */,
'{{ interface_address6 }}',
{{ mtu }},
'{{ name }}' /* required */,
{{ ttl }},
'{{ account_id }}',
'{{ x-magic-new-hc-target }}'
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
- name: gre_tunnels
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the gre_tunnels resource.
    - name: automatic_return_routing
      value: {{ automatic_return_routing }}
      description: |
        True if automatic stateful return routing should be enabled for a tunnel, false otherwise. Requires the \`coupler_integration\` account flag to be enabled; requests setting this to \`true\` without that flag will be rejected.
      default: false
    - name: bgp
      value:
        customer_asn: {{ customer_asn }}
        extra_prefixes:
          - "{{ extra_prefixes }}"
        md5_key: "{{ md5_key }}"
    - name: cloudflare_gre_endpoint
      value: "{{ cloudflare_gre_endpoint }}"
      description: |
        The IP address assigned to the Cloudflare side of the GRE tunnel.
    - name: customer_gre_endpoint
      value: "{{ customer_gre_endpoint }}"
      description: |
        The IP address assigned to the customer side of the GRE tunnel.
    - name: description
      value: "{{ description }}"
      description: |
        An optional description of the GRE tunnel.
    - name: health_check
      value:
        enabled: {{ enabled }}
        rate: "{{ rate }}"
        target:
          effective: "{{ effective }}"
          saved: "{{ saved }}"
        type: "{{ type }}"
        direction: "{{ direction }}"
    - name: interface_address
      value: "{{ interface_address }}"
      description: |
        A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side of the tunnel. Select the subnet from the following private IP space: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    - name: interface_address6
      value: "{{ interface_address6 }}"
      description: |
        A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
    - name: mtu
      value: {{ mtu }}
      description: |
        Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value is 576.
      default: 1476
    - name: name
      value: "{{ name }}"
      description: |
        The name of the tunnel. The name cannot contain spaces or special characters, must be 15 characters or less, and cannot share a name with another GRE tunnel.
    - name: ttl
      value: {{ ttl }}
      description: |
        Time To Live (TTL) in number of hops of the GRE tunnel.
      default: 64
    - name: x-magic-new-hc-target
      value: {{ x-magic-new-hc-target }}
      description: If true, the health check target in the request and response bodies will be presented using the new object format. Defaults to false.
      description: If true, the health check target in the request and response bodies will be presented using the new object format. Defaults to false.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'bulk_update', value: 'bulk_update' }
    ]}
>
<TabItem value="update">

Updates a specific GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

```sql
REPLACE cloudflare.magic_transit.gre_tunnels
SET 
automatic_return_routing = {{ automatic_return_routing }},
cloudflare_gre_endpoint = '{{ cloudflare_gre_endpoint }}',
customer_gre_endpoint = '{{ customer_gre_endpoint }}',
description = '{{ description }}',
health_check = '{{ health_check }}',
interface_address = '{{ interface_address }}',
interface_address6 = '{{ interface_address6 }}',
mtu = {{ mtu }},
name = '{{ name }}',
ttl = {{ ttl }}
WHERE 
gre_tunnel_id = '{{ gre_tunnel_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND customer_gre_endpoint = '{{ customer_gre_endpoint }}' --required
AND cloudflare_gre_endpoint = '{{ cloudflare_gre_endpoint }}' --required
AND interface_address = '{{ interface_address }}' --required
AND x-magic-new-hc-target = {{ x-magic-new-hc-target}}
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="bulk_update">

Updates multiple GRE tunnels. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

```sql
REPLACE cloudflare.magic_transit.gre_tunnels
SET 
-- No updatable properties
WHERE 
account_id = '{{ account_id }}' --required
AND x-magic-new-hc-target = {{ x-magic-new-hc-target}}
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

Disables and removes a specific static GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

```sql
DELETE FROM cloudflare.magic_transit.gre_tunnels
WHERE gre_tunnel_id = '{{ gre_tunnel_id }}' --required
AND account_id = '{{ account_id }}' --required
AND x-magic-new-hc-target = '{{ x-magic-new-hc-target }}'
;
```
</TabItem>
</Tabs>
