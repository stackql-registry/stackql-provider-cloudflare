--- 
title: keyless_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - keyless_certificates
  - keyless_certificates
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

Creates, updates, deletes, gets or lists a <code>keyless_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="keyless_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.keyless_certificates.keyless_certificates" /></td></tr>
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

Get Keyless SSL Configuration response

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
    <td>Keyless certificate identifier tag. (example: 4d2844d2ce78891c34d0b6c0535a291e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The keyless SSL name. (example: example.com Keyless SSL)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Keyless SSL was created. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the Keyless SSL is on or off.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string (hostname)</code></td>
    <td>The keyless SSL name. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Keyless SSL was last modified. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>Available permissions for the Keyless SSL for the current user requesting the item.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>number</code></td>
    <td>The keyless SSL port used to communicate between Cloudflare and the client's Keyless SSL server.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Keyless SSL. (active, deleted) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel" /></td>
    <td><code>object</code></td>
    <td>Configuration for using Keyless SSL through a Cloudflare Tunnel</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Keyless SSL Configurations response

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
    <td>Keyless certificate identifier tag. (example: 4d2844d2ce78891c34d0b6c0535a291e)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The keyless SSL name. (example: example.com Keyless SSL)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Keyless SSL was created. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the Keyless SSL is on or off.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string (hostname)</code></td>
    <td>The keyless SSL name. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Keyless SSL was last modified. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>Available permissions for the Keyless SSL for the current user requesting the item.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>number</code></td>
    <td>The keyless SSL port used to communicate between Cloudflare and the client's Keyless SSL server.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Keyless SSL. (active, deleted) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel" /></td>
    <td><code>object</code></td>
    <td>Configuration for using Keyless SSL through a Cloudflare Tunnel</td>
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
    <td><a href="#parameter-keyless_certificate_id"><code>keyless_certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Get details for one Keyless SSL configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>List all Keyless SSL configurations for a given zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-port"><code>port</code></a>, <a href="#parameter-certificate"><code>certificate</code></a></td>
    <td></td>
    <td>Creates a Keyless SSL configuration that allows SSL/TLS termination without exposing private keys to Cloudflare. Keys remain on your infrastructure.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-keyless_certificate_id"><code>keyless_certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>This will update attributes of a Keyless SSL. Consists of one or more of the following: host,name,port.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-keyless_certificate_id"><code>keyless_certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Removes a Keyless SSL configuration. SSL connections will no longer use the keyless server for cryptographic operations.</td>
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
<tr id="parameter-keyless_certificate_id">
    <td><CopyableCode code="keyless_certificate_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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

Get details for one Keyless SSL configuration.

```sql
SELECT
id,
name,
created_on,
enabled,
host,
modified_on,
permissions,
port,
status,
tunnel
FROM cloudflare.keyless_certificates.keyless_certificates
WHERE keyless_certificate_id = '{{ keyless_certificate_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Keyless SSL configurations for a given zone.

```sql
SELECT
id,
name,
created_on,
enabled,
host,
modified_on,
permissions,
port,
status,
tunnel
FROM cloudflare.keyless_certificates.keyless_certificates
WHERE zone_id = '{{ zone_id }}' -- required
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

Creates a Keyless SSL configuration that allows SSL/TLS termination without exposing private keys to Cloudflare. Keys remain on your infrastructure.

```sql
INSERT INTO cloudflare.keyless_certificates.keyless_certificates (
bundle_method,
certificate,
host,
name,
port,
tunnel,
zone_id
)
SELECT 
'{{ bundle_method }}',
'{{ certificate }}' /* required */,
'{{ host }}' /* required */,
'{{ name }}',
{{ port }} /* required */,
'{{ tunnel }}',
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
- name: keyless_certificates
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the keyless_certificates resource.
    - name: bundle_method
      value: "{{ bundle_method }}"
      description: |
        A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
      valid_values: ['ubiquitous', 'optimal', 'force']
      default: ubiquitous
    - name: certificate
      value: "{{ certificate }}"
      description: |
        The zone's SSL certificate or SSL certificate and intermediate(s).
    - name: host
      value: "{{ host }}"
      description: |
        The keyless SSL name.
    - name: name
      value: "{{ name }}"
      description: |
        The keyless SSL name.
    - name: port
      value: {{ port }}
      description: |
        The keyless SSL port used to communicate between Cloudflare and the client's Keyless SSL server.
      default: 24008
    - name: tunnel
      description: |
        Configuration for using Keyless SSL through a Cloudflare Tunnel
      value:
        private_ip: "{{ private_ip }}"
        vnet_id: "{{ vnet_id }}"
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

This will update attributes of a Keyless SSL. Consists of one or more of the following: host,name,port.

```sql
UPDATE cloudflare.keyless_certificates.keyless_certificates
SET 
enabled = {{ enabled }},
host = '{{ host }}',
name = '{{ name }}',
port = {{ port }},
tunnel = '{{ tunnel }}'
WHERE 
keyless_certificate_id = '{{ keyless_certificate_id }}' --required
AND zone_id = '{{ zone_id }}' --required
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

Removes a Keyless SSL configuration. SSL connections will no longer use the keyless server for cryptographic operations.

```sql
DELETE FROM cloudflare.keyless_certificates.keyless_certificates
WHERE keyless_certificate_id = '{{ keyless_certificate_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
