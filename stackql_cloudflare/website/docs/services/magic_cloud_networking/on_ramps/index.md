--- 
title: on_ramps
hide_title: false
hide_table_of_contents: false
keywords:
  - on_ramps
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

Creates, updates, deletes, gets or lists an <code>on_ramps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="on_ramps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_cloud_networking.on_ramps" /></td></tr>
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
    <td><CopyableCode code="vpcs_by_id" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attached_hubs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attached_vpcs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud_asn" /></td>
    <td><code>integer (uint32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><code>string</code></td>
    <td> (AWS, AZURE, GOOGLE)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dynamic_routing" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="hub" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="install_routes_in_cloud" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="install_routes_in_magic_wan" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_applied_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_exported_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_planned_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="manage_hub_to_hub_attachments" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="manage_vpc_to_hub_attachments" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="planned_monthly_cost_estimate" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="planned_resources" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="planned_resources_unavailable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_apply_monthly_cost_estimate" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_apply_resources" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_apply_resources_unavailable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (OnrampTypeSingle, OnrampTypeHub)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="vpc" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="vpcs_by_id_unavailable" /></td>
    <td><code>array</code></td>
    <td>The list of vpc IDs for which resource details failed to generate.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="vpcs_by_id" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attached_hubs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="attached_vpcs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud_asn" /></td>
    <td><code>integer (uint32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><code>string</code></td>
    <td> (AWS, AZURE, GOOGLE)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="dynamic_routing" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="hub" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="install_routes_in_cloud" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="install_routes_in_magic_wan" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_applied_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_exported_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_planned_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="manage_hub_to_hub_attachments" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="manage_vpc_to_hub_attachments" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="planned_monthly_cost_estimate" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="planned_resources" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="planned_resources_unavailable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_apply_monthly_cost_estimate" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_apply_resources" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="post_apply_resources_unavailable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (OnrampTypeSingle, OnrampTypeHub)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="vpc" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="vpcs_by_id_unavailable" /></td>
    <td><code>array</code></td>
    <td>The list of vpc IDs for which resource details failed to generate.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-vpcs"><code>vpcs</code></a>, <a href="#parameter-post_apply_resources"><code>post_apply_resources</code></a>, <a href="#parameter-planned_resources"><code>planned_resources</code></a></td>
    <td>Read an On-ramp (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-desc"><code>desc</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-vpcs"><code>vpcs</code></a></td>
    <td>List On-ramps (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-cloud_type"><code>cloud_type</code></a>, <a href="#parameter-install_routes_in_cloud"><code>install_routes_in_cloud</code></a>, <a href="#parameter-install_routes_in_magic_wan"><code>install_routes_in_magic_wan</code></a>, <a href="#parameter-dynamic_routing"><code>dynamic_routing</code></a></td>
    <td><a href="#parameter-forwarded"><code>forwarded</code></a></td>
    <td>Create a new On-ramp (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td></td>
    <td>Update an On-ramp (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td></td>
    <td>Update an On-ramp (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-onramp_id"><code>onramp_id</code></a></td>
    <td><a href="#parameter-destroy"><code>destroy</code></a>, <a href="#parameter-force"><code>force</code></a></td>
    <td>Delete an On-ramp (Closed Beta).</td>
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
<tr id="parameter-onramp_id">
    <td><CopyableCode code="onramp_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-desc">
    <td><CopyableCode code="desc" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-destroy">
    <td><CopyableCode code="destroy" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-forwarded">
    <td><CopyableCode code="forwarded" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>One of ["updated_at", "id", "cloud_type", "name"].</td>
</tr>
<tr id="parameter-planned_resources">
    <td><CopyableCode code="planned_resources" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-post_apply_resources">
    <td><CopyableCode code="post_apply_resources" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-vpcs">
    <td><CopyableCode code="vpcs" /></td>
    <td><code>boolean</code></td>
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

Read an On-ramp (Closed Beta).

```sql
SELECT
id,
name,
vpcs_by_id,
attached_hubs,
attached_vpcs,
cloud_asn,
cloud_type,
description,
dynamic_routing,
hub,
install_routes_in_cloud,
install_routes_in_magic_wan,
last_applied_at,
last_exported_at,
last_planned_at,
manage_hub_to_hub_attachments,
manage_vpc_to_hub_attachments,
planned_monthly_cost_estimate,
planned_resources,
planned_resources_unavailable,
post_apply_monthly_cost_estimate,
post_apply_resources,
post_apply_resources_unavailable,
region,
status,
type,
updated_at,
vpc,
vpcs_by_id_unavailable
FROM cloudflare.magic_cloud_networking.on_ramps
WHERE account_id = '{{ account_id }}' -- required
AND onramp_id = '{{ onramp_id }}' -- required
AND status = '{{ status }}'
AND vpcs = '{{ vpcs }}'
AND post_apply_resources = '{{ post_apply_resources }}'
AND planned_resources = '{{ planned_resources }}'
;
```
</TabItem>
<TabItem value="list">

List On-ramps (Closed Beta).

```sql
SELECT
id,
name,
vpcs_by_id,
attached_hubs,
attached_vpcs,
cloud_asn,
cloud_type,
description,
dynamic_routing,
hub,
install_routes_in_cloud,
install_routes_in_magic_wan,
last_applied_at,
last_exported_at,
last_planned_at,
manage_hub_to_hub_attachments,
manage_vpc_to_hub_attachments,
planned_monthly_cost_estimate,
planned_resources,
planned_resources_unavailable,
post_apply_monthly_cost_estimate,
post_apply_resources,
post_apply_resources_unavailable,
region,
status,
type,
updated_at,
vpc,
vpcs_by_id_unavailable
FROM cloudflare.magic_cloud_networking.on_ramps
WHERE account_id = '{{ account_id }}' -- required
AND order_by = '{{ order_by }}'
AND desc = '{{ desc }}'
AND status = '{{ status }}'
AND vpcs = '{{ vpcs }}'
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

Create a new On-ramp (Closed Beta).

```sql
INSERT INTO cloudflare.magic_cloud_networking.on_ramps (
adopted_hub_id,
attached_hubs,
attached_vpcs,
cloud_asn,
cloud_type,
description,
dynamic_routing,
hub_provider_id,
install_routes_in_cloud,
install_routes_in_magic_wan,
manage_hub_to_hub_attachments,
manage_vpc_to_hub_attachments,
name,
region,
type,
vpc,
account_id,
forwarded
)
SELECT 
'{{ adopted_hub_id }}',
'{{ attached_hubs }}',
'{{ attached_vpcs }}',
{{ cloud_asn }},
'{{ cloud_type }}' /* required */,
'{{ description }}',
{{ dynamic_routing }} /* required */,
'{{ hub_provider_id }}',
{{ install_routes_in_cloud }} /* required */,
{{ install_routes_in_magic_wan }} /* required */,
{{ manage_hub_to_hub_attachments }},
{{ manage_vpc_to_hub_attachments }},
'{{ name }}' /* required */,
'{{ region }}',
'{{ type }}' /* required */,
'{{ vpc }}',
'{{ account_id }}',
'{{ forwarded }}'
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
- name: on_ramps
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the on_ramps resource.
    - name: adopted_hub_id
      value: "{{ adopted_hub_id }}"
    - name: attached_hubs
      value:
        - "{{ attached_hubs }}"
    - name: attached_vpcs
      value:
        - "{{ attached_vpcs }}"
    - name: cloud_asn
      value: {{ cloud_asn }}
      description: |
        Sets the cloud-side ASN. If unset or zero, the cloud's default ASN takes effect.
    - name: cloud_type
      value: "{{ cloud_type }}"
      valid_values: ['AWS', 'AZURE', 'GOOGLE']
    - name: description
      value: "{{ description }}"
    - name: dynamic_routing
      value: {{ dynamic_routing }}
      description: |
        Enables BGP routing. When enabling this feature, set both install_routes_in_cloud and install_routes_in_magic_wan to false.
    - name: hub_provider_id
      value: "{{ hub_provider_id }}"
    - name: install_routes_in_cloud
      value: {{ install_routes_in_cloud }}
    - name: install_routes_in_magic_wan
      value: {{ install_routes_in_magic_wan }}
    - name: manage_hub_to_hub_attachments
      value: {{ manage_hub_to_hub_attachments }}
    - name: manage_vpc_to_hub_attachments
      value: {{ manage_vpc_to_hub_attachments }}
    - name: name
      value: "{{ name }}"
    - name: region
      value: "{{ region }}"
    - name: type
      value: "{{ type }}"
      valid_values: ['OnrampTypeSingle', 'OnrampTypeHub']
    - name: vpc
      value: "{{ vpc }}"
    - name: forwarded
      value: "{{ forwarded }}"
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

Update an On-ramp (Closed Beta).

```sql
UPDATE cloudflare.magic_cloud_networking.on_ramps
SET 
attached_hubs = '{{ attached_hubs }}',
attached_vpcs = '{{ attached_vpcs }}',
description = '{{ description }}',
install_routes_in_cloud = {{ install_routes_in_cloud }},
install_routes_in_magic_wan = {{ install_routes_in_magic_wan }},
manage_hub_to_hub_attachments = {{ manage_hub_to_hub_attachments }},
manage_vpc_to_hub_attachments = {{ manage_vpc_to_hub_attachments }},
name = '{{ name }}',
vpc = '{{ vpc }}'
WHERE 
account_id = '{{ account_id }}' --required
AND onramp_id = '{{ onramp_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
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

Update an On-ramp (Closed Beta).

```sql
REPLACE cloudflare.magic_cloud_networking.on_ramps
SET 
attached_hubs = '{{ attached_hubs }}',
attached_vpcs = '{{ attached_vpcs }}',
description = '{{ description }}',
install_routes_in_cloud = {{ install_routes_in_cloud }},
install_routes_in_magic_wan = {{ install_routes_in_magic_wan }},
manage_hub_to_hub_attachments = {{ manage_hub_to_hub_attachments }},
manage_vpc_to_hub_attachments = {{ manage_vpc_to_hub_attachments }},
name = '{{ name }}',
vpc = '{{ vpc }}'
WHERE 
account_id = '{{ account_id }}' --required
AND onramp_id = '{{ onramp_id }}' --required
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

Delete an On-ramp (Closed Beta).

```sql
DELETE FROM cloudflare.magic_cloud_networking.on_ramps
WHERE account_id = '{{ account_id }}' --required
AND onramp_id = '{{ onramp_id }}' --required
AND destroy = '{{ destroy }}'
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
