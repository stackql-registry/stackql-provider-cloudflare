--- 
title: cloud_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_resources
  - magic_cloud_networking
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

Creates, updates, deletes, gets or lists a <code>cloud_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_cloud_networking.cloud_resources" /></td></tr>
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

OK.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="native_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provider_names_by_id" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><code>string</code></td>
    <td> (AWS, AZURE, GOOGLE, CLOUDFLARE)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deployment_provider" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="managed_by" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="monthly_cost_estimate" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="observations" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provider_ids" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resource_type" /></td>
    <td><code>string</code></td>
    <td> (aws_customer_gateway, aws_egress_only_internet_gateway, aws_internet_gateway, aws_instance, aws_network_interface, aws_route, aws_route_table, aws_route_table_association, aws_subnet, aws_vpc, aws_vpc_ipv4_cidr_block_association, aws_vpn_connection, aws_vpn_connection_route, aws_vpn_gateway, aws_security_group, aws_vpc_security_group_ingress_rule, aws_vpc_security_group_egress_rule, aws_ec2_managed_prefix_list, aws_ec2_transit_gateway, aws_ec2_transit_gateway_prefix_list_reference, aws_ec2_transit_gateway_vpc_attachment, azurerm_application_security_group, azurerm_lb, azurerm_lb_backend_address_pool, azurerm_lb_nat_pool, azurerm_lb_nat_rule, azurerm_lb_rule, azurerm_local_network_gateway, azurerm_network_interface, azurerm_network_interface_application_security_group_association, azurerm_network_interface_backend_address_pool_association, azurerm_network_interface_security_group_association, azurerm_network_security_group, azurerm_public_ip, azurerm_route, azurerm_route_table, azurerm_subnet, azurerm_subnet_route_table_association, azurerm_virtual_machine, azurerm_virtual_network_gateway_connection, azurerm_virtual_network, azurerm_virtual_network_gateway, google_compute_network, google_compute_subnetwork, google_compute_vpn_gateway, google_compute_vpn_tunnel, google_compute_route, google_compute_address, google_compute_global_address, google_compute_router, google_compute_interconnect_attachment, google_compute_ha_vpn_gateway, google_compute_forwarding_rule, google_compute_network_firewall_policy, google_compute_network_firewall_policy_rule, cloudflare_static_route, cloudflare_ipsec_tunnel)</td>
</tr>
<tr>
    <td><CopyableCode code="sections" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-provider_id"><code>provider_id</code></a>, <a href="#parameter-resource_type"><code>resource_type</code></a>, <a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-region"><code>region</code></a>, <a href="#parameter-resource_group"><code>resource_group</code></a>, <a href="#parameter-managed"><code>managed</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-desc"><code>desc</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-cloudflare"><code>cloudflare</code></a>, <a href="#parameter-v2"><code>v2</code></a></td>
    <td>List resources in the Resource Catalog (Closed Beta).</td>
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
<tr id="parameter-cloudflare">
    <td><CopyableCode code="cloudflare" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-desc">
    <td><CopyableCode code="desc" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-managed">
    <td><CopyableCode code="managed" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>One of ["id", "resource_type", "region"].</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-provider_id">
    <td><CopyableCode code="provider_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-region">
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_group">
    <td><CopyableCode code="resource_group" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-resource_type">
    <td><CopyableCode code="resource_type" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr id="parameter-v2">
    <td><CopyableCode code="v2" /></td>
    <td><code>boolean</code></td>
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

List resources in the Resource Catalog (Closed Beta).

```sql
SELECT
id,
name,
account_id,
native_id,
provider_names_by_id,
cloud_type,
config,
deployment_provider,
managed,
managed_by,
monthly_cost_estimate,
observations,
provider_ids,
region,
resource_group,
resource_type,
sections,
state,
tags,
updated_at,
url
FROM cloudflare.magic_cloud_networking.cloud_resources
WHERE account_id = '{{ account_id }}' -- required
AND provider_id = '{{ provider_id }}'
AND resource_type = '{{ resource_type }}'
AND resource_id = '{{ resource_id }}'
AND region = '{{ region }}'
AND resource_group = '{{ resource_group }}'
AND managed = '{{ managed }}'
AND search = '{{ search }}'
AND order_by = '{{ order_by }}'
AND desc = '{{ desc }}'
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
AND cloudflare = '{{ cloudflare }}'
AND v2 = '{{ v2 }}'
;
```
</TabItem>
</Tabs>
