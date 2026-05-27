--- 
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="locations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.locations" /></td></tr>
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

Gets Zero Trust Gateway location details response.

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
    <td> (example: ed35569b41ce4d1facfe683550f54086)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specify the location name. (example: Austin Office Location)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_destination_ips_id" /></td>
    <td><code>string</code></td>
    <td>Indicate the identifier of the pair of IPv4 addresses assigned to this location. (default: 0e4a32c6-6fb8-4858-9296-98f51631e8e6, example: 0e4a32c6-6fb8-4858-9296-98f51631e8e6, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_destination_ipv6_block_id" /></td>
    <td><code>string</code></td>
    <td>Specify the UUID of the IPv6 block brought to the gateway so that this location's IPv6 address is allocated from the Bring Your Own IPv6 (BYOIPv6) block rather than the standard Cloudflare IPv6 block. (example: b08f7231-d458-495c-98ef-190604c9ee83, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="client_default" /></td>
    <td><code>boolean</code></td>
    <td>Indicate whether this location is the default location.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="doh_subdomain" /></td>
    <td><code>string</code></td>
    <td>Specify the DNS over HTTPS domain that receives DNS requests. Gateway automatically generates this value. (example: oli3n9zkz5, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ecs_support" /></td>
    <td><code>boolean</code></td>
    <td>Indicate whether the location must resolve EDNS queries.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Configure the destination endpoints for this location. (x-stainless-terraform-configurability: optional)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Defines the automatically generated IPv6 destination IP assigned to this location. Gateway counts all DNS requests sent to this IP as requests under this location. (example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_destination" /></td>
    <td><code>string</code></td>
    <td>Show the primary destination IPv4 address from the pair identified dns_destination_ips_id. This field read-only. (example: 172.64.36.1, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_destination_backup" /></td>
    <td><code>string</code></td>
    <td>Show the backup destination IPv4 address from the pair identified dns_destination_ips_id. This field read-only. (example: 172.64.36.2, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>Specify the list of network ranges from which requests at this location originate. The list takes effect only if it is non-empty and the IPv4 endpoint is enabled for this location. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Lists Zero Trust Gateway locations response.

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
    <td> (example: ed35569b41ce4d1facfe683550f54086)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specify the location name. (example: Austin Office Location)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_destination_ips_id" /></td>
    <td><code>string</code></td>
    <td>Indicate the identifier of the pair of IPv4 addresses assigned to this location. (default: 0e4a32c6-6fb8-4858-9296-98f51631e8e6, example: 0e4a32c6-6fb8-4858-9296-98f51631e8e6, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_destination_ipv6_block_id" /></td>
    <td><code>string</code></td>
    <td>Specify the UUID of the IPv6 block brought to the gateway so that this location's IPv6 address is allocated from the Bring Your Own IPv6 (BYOIPv6) block rather than the standard Cloudflare IPv6 block. (example: b08f7231-d458-495c-98ef-190604c9ee83, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="client_default" /></td>
    <td><code>boolean</code></td>
    <td>Indicate whether this location is the default location.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="doh_subdomain" /></td>
    <td><code>string</code></td>
    <td>Specify the DNS over HTTPS domain that receives DNS requests. Gateway automatically generates this value. (example: oli3n9zkz5, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ecs_support" /></td>
    <td><code>boolean</code></td>
    <td>Indicate whether the location must resolve EDNS queries.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Configure the destination endpoints for this location. (x-stainless-terraform-configurability: optional)</td>
</tr>
<tr>
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Defines the automatically generated IPv6 destination IP assigned to this location. Gateway counts all DNS requests sent to this IP as requests under this location. (example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_destination" /></td>
    <td><code>string</code></td>
    <td>Show the primary destination IPv4 address from the pair identified dns_destination_ips_id. This field read-only. (example: 172.64.36.1, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_destination_backup" /></td>
    <td><code>string</code></td>
    <td>Show the backup destination IPv4 address from the pair identified dns_destination_ips_id. This field read-only. (example: 172.64.36.2, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>Specify the list of network ranges from which requests at this location originate. The list takes effect only if it is non-empty and the IPv4 endpoint is enabled for this location. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-location_id"><code>location_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get a single Zero Trust Gateway location.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List Zero Trust Gateway locations for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a new Zero Trust Gateway location.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-location_id"><code>location_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Update a configured Zero Trust Gateway location.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-location_id"><code>location_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured Zero Trust Gateway location.</td>
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
<tr id="parameter-location_id">
    <td><CopyableCode code="location_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get a single Zero Trust Gateway location.

```sql
SELECT
id,
name,
dns_destination_ips_id,
dns_destination_ipv6_block_id,
client_default,
created_at,
doh_subdomain,
ecs_support,
endpoints,
ip,
ipv4_destination,
ipv4_destination_backup,
networks,
updated_at
FROM cloudflare.zero_trust.locations
WHERE location_id = '{{ location_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Zero Trust Gateway locations for an account.

```sql
SELECT
id,
name,
dns_destination_ips_id,
dns_destination_ipv6_block_id,
client_default,
created_at,
doh_subdomain,
ecs_support,
endpoints,
ip,
ipv4_destination,
ipv4_destination_backup,
networks,
updated_at
FROM cloudflare.zero_trust.locations
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

Create a new Zero Trust Gateway location.

```sql
INSERT INTO cloudflare.zero_trust.locations (
client_default,
dns_destination_ips_id,
ecs_support,
endpoints,
name,
networks,
account_id
)
SELECT 
{{ client_default }},
'{{ dns_destination_ips_id }}',
{{ ecs_support }},
'{{ endpoints }}',
'{{ name }}' /* required */,
'{{ networks }}',
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
- name: locations
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the locations resource.
    - name: client_default
      value: {{ client_default }}
      description: |
        Indicate whether this location is the default location.
      default: false
    - name: dns_destination_ips_id
      value: "{{ dns_destination_ips_id }}"
      description: |
        Specify the identifier of the pair of IPv4 addresses assigned to this location. When creating a location, if this field is absent or set to null, the pair of shared IPv4 addresses (0e4a32c6-6fb8-4858-9296-98f51631e8e6) is auto-assigned. When updating a location, if this field is absent or set to null, the pre-assigned pair remains unchanged.
    - name: ecs_support
      value: {{ ecs_support }}
      description: |
        Indicate whether the location must resolve EDNS queries.
      default: false
    - name: endpoints
      description: |
        Configure the destination endpoints for this location.
      value:
        doh:
          enabled: {{ enabled }}
          networks:
            - network: "{{ network }}"
          require_token: {{ require_token }}
        dot:
          enabled: {{ enabled }}
          networks:
            - network: "{{ network }}"
        ipv4:
          enabled: {{ enabled }}
        ipv6:
          enabled: {{ enabled }}
          networks:
            - network: "{{ network }}"
    - name: name
      value: "{{ name }}"
      description: |
        Specify the location name.
    - name: networks
      description: |
        Specify the list of network ranges from which requests at this location originate. The list takes effect only if it is non-empty and the IPv4 endpoint is enabled for this location.
      value:
        - network: "{{ network }}"
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

Update a configured Zero Trust Gateway location.

```sql
REPLACE cloudflare.zero_trust.locations
SET 
client_default = {{ client_default }},
dns_destination_ips_id = '{{ dns_destination_ips_id }}',
ecs_support = {{ ecs_support }},
endpoints = '{{ endpoints }}',
name = '{{ name }}',
networks = '{{ networks }}'
WHERE 
location_id = '{{ location_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
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

Delete a configured Zero Trust Gateway location.

```sql
DELETE FROM cloudflare.zero_trust.locations
WHERE location_id = '{{ location_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
