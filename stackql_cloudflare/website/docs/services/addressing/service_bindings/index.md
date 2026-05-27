--- 
title: service_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - service_bindings
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

Creates, updates, deletes, gets or lists a <code>service_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_bindings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.service_bindings" /></td></tr>
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

The Service Binding with the requested ID

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
    <td>Identifier of a Service Binding. (example: 0429b49b6a5155297b78e75a44b09e14)</td>
</tr>
<tr>
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint. (example: 2db684ee7ca04e159946fd05b99e1bcd)</td>
</tr>
<tr>
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>Name of a service running on the Cloudflare network (example: Magic Transit)</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioning" /></td>
    <td><code>object</code></td>
    <td>Status of a Service Binding's deployment to the Cloudflare network</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Service Bindings attached to the Prefix

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
    <td>Identifier of a Service Binding. (example: 0429b49b6a5155297b78e75a44b09e14)</td>
</tr>
<tr>
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint. (example: 2db684ee7ca04e159946fd05b99e1bcd)</td>
</tr>
<tr>
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>Name of a service running on the Cloudflare network (example: Magic Transit)</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioning" /></td>
    <td><code>object</code></td>
    <td>Status of a Service Binding's deployment to the Cloudflare network</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-binding_id"><code>binding_id</code></a></td>
    <td></td>
    <td>Fetch a single Service Binding</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a></td>
    <td></td>
    <td>List the Cloudflare services this prefix is currently bound to. Traffic sent to an address within an IP prefix will be routed to the Cloudflare service of the most-specific Service Binding matching the address. **Example:** binding `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other IPs in the prefix to Cloudflare Magic Transit.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-cidr"><code>cidr</code></a>, <a href="#parameter-service_id"><code>service_id</code></a></td>
    <td></td>
    <td>Creates a new Service Binding, routing traffic to IPs within the given CIDR to a service running on Cloudflare's network. **NOTE:** The first Service Binding created for an IP Prefix must exactly match the IP Prefix's CIDR. Subsequent Service Bindings may be created with a more-specific CIDR. Refer to the [Service Bindings Documentation](https://developers.cloudflare.com/byoip/service-bindings/) for compatibility details.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-binding_id"><code>binding_id</code></a></td>
    <td></td>
    <td>Delete a Service Binding</td>
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
<tr id="parameter-binding_id">
    <td><CopyableCode code="binding_id" /></td>
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

Fetch a single Service Binding

```sql
SELECT
id,
service_id,
service_name,
cidr,
provisioning
FROM cloudflare.addressing.service_bindings
WHERE account_id = '{{ account_id }}' -- required
AND prefix_id = '{{ prefix_id }}' -- required
AND binding_id = '{{ binding_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the Cloudflare services this prefix is currently bound to. Traffic sent to an address within an IP prefix will be routed to the Cloudflare service of the most-specific Service Binding matching the address. **Example:** binding `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other IPs in the prefix to Cloudflare Magic Transit.

```sql
SELECT
id,
service_id,
service_name,
cidr,
provisioning
FROM cloudflare.addressing.service_bindings
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

Creates a new Service Binding, routing traffic to IPs within the given CIDR to a service running on Cloudflare's network. **NOTE:** The first Service Binding created for an IP Prefix must exactly match the IP Prefix's CIDR. Subsequent Service Bindings may be created with a more-specific CIDR. Refer to the [Service Bindings Documentation](https://developers.cloudflare.com/byoip/service-bindings/) for compatibility details.

```sql
INSERT INTO cloudflare.addressing.service_bindings (
cidr,
service_id,
account_id,
prefix_id
)
SELECT 
'{{ cidr }}' /* required */,
'{{ service_id }}' /* required */,
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
- name: service_bindings
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the service_bindings resource.
    - name: prefix_id
      value: "{{ prefix_id }}"
      description: Required parameter for the service_bindings resource.
    - name: cidr
      value: "{{ cidr }}"
      description: |
        IP Prefix in Classless Inter-Domain Routing format.
    - name: service_id
      value: "{{ service_id }}"
      description: |
        Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the **List Services** endpoint.
`}</CodeBlock>

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

Delete a Service Binding

```sql
DELETE FROM cloudflare.addressing.service_bindings
WHERE account_id = '{{ account_id }}' --required
AND prefix_id = '{{ prefix_id }}' --required
AND binding_id = '{{ binding_id }}' --required
;
```
</TabItem>
</Tabs>
