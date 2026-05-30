--- 
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - spectrum
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

Creates, updates, deletes, gets or lists an <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.spectrum.apps" /></td></tr>
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

Get Spectrum application configuration response.

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
    <td>App identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="argo_smart_routing" /></td>
    <td><code>boolean</code></td>
    <td>Enables Argo Smart Routing for this application. Notes: Only available for TCP applications with traffic_type set to "direct".</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Application was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="dns" /></td>
    <td><code>object</code></td>
    <td>The name and type of DNS record for the Spectrum application.</td>
</tr>
<tr>
    <td><CopyableCode code="edge_ips" /></td>
    <td><code>object</code></td>
    <td>The anycast edge IP configuration for the hostname of this application.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_firewall" /></td>
    <td><code>boolean</code></td>
    <td>Enables IP Access Rules for this application. Notes: Only available for TCP applications.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Application was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_direct" /></td>
    <td><code>array</code></td>
    <td>List of origin IP addresses. Array may contain multiple IP addresses for load balancing.</td>
</tr>
<tr>
    <td><CopyableCode code="origin_dns" /></td>
    <td><code>object</code></td>
    <td>The name and type of DNS record for the Spectrum application.</td>
</tr>
<tr>
    <td><CopyableCode code="origin_port" /></td>
    <td><code>integer</code></td>
    <td>The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the "protocol" field.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The port configuration at Cloudflare's edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`. (example: tcp/22)</td>
</tr>
<tr>
    <td><CopyableCode code="proxy_protocol" /></td>
    <td><code>string</code></td>
    <td>Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol. (off, v1, v2, simple) (default: off, example: off)</td>
</tr>
<tr>
    <td><CopyableCode code="tls" /></td>
    <td><code>string</code></td>
    <td>The type of TLS termination associated with the application. (off, flexible, full, strict) (default: off, example: off)</td>
</tr>
<tr>
    <td><CopyableCode code="traffic_type" /></td>
    <td><code>string</code></td>
    <td>Determines how data travels from the edge to your origin. When set to "direct", Spectrum will send traffic directly to your origin, and the application's type is derived from the `protocol`. When set to "http" or "https", Spectrum will apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly. (direct, http, https) (default: direct, example: direct)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Spectrum applications response.

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
    <td>App identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="argo_smart_routing" /></td>
    <td><code>boolean</code></td>
    <td>Enables Argo Smart Routing for this application. Notes: Only available for TCP applications with traffic_type set to "direct".</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Application was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="dns" /></td>
    <td><code>object</code></td>
    <td>The name and type of DNS record for the Spectrum application.</td>
</tr>
<tr>
    <td><CopyableCode code="edge_ips" /></td>
    <td><code>object</code></td>
    <td>The anycast edge IP configuration for the hostname of this application.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_firewall" /></td>
    <td><code>boolean</code></td>
    <td>Enables IP Access Rules for this application. Notes: Only available for TCP applications.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the Application was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_direct" /></td>
    <td><code>array</code></td>
    <td>List of origin IP addresses. Array may contain multiple IP addresses for load balancing.</td>
</tr>
<tr>
    <td><CopyableCode code="origin_dns" /></td>
    <td><code>object</code></td>
    <td>The name and type of DNS record for the Spectrum application.</td>
</tr>
<tr>
    <td><CopyableCode code="origin_port" /></td>
    <td><code>integer</code></td>
    <td>The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example `1000`, or a string to specify a range of origin ports, for example `"1000-2000"`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the "protocol" field.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The port configuration at Cloudflare's edge. May specify a single port, for example `"tcp/1000"`, or a range of ports, for example `"tcp/1000-2000"`. (example: tcp/22)</td>
</tr>
<tr>
    <td><CopyableCode code="proxy_protocol" /></td>
    <td><code>string</code></td>
    <td>Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol. (off, v1, v2, simple) (default: off, example: off)</td>
</tr>
<tr>
    <td><CopyableCode code="tls" /></td>
    <td><code>string</code></td>
    <td>The type of TLS termination associated with the application. (off, flexible, full, strict) (default: off, example: off)</td>
</tr>
<tr>
    <td><CopyableCode code="traffic_type" /></td>
    <td><code>string</code></td>
    <td>Determines how data travels from the edge to your origin. When set to "direct", Spectrum will send traffic directly to your origin, and the application's type is derived from the `protocol`. When set to "http" or "https", Spectrum will apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly. (direct, http, https) (default: direct, example: direct)</td>
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
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Gets the application configuration of a specific application inside a zone.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-order"><code>order</code></a></td>
    <td>Retrieves a list of currently existing Spectrum applications inside a zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-dns"><code>dns</code></a>, <a href="#parameter-protocol"><code>protocol</code></a></td>
    <td></td>
    <td>Creates a new Spectrum application from a configuration using a name for the origin.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-dns"><code>dns</code></a>, <a href="#parameter-protocol"><code>protocol</code></a></td>
    <td></td>
    <td>Updates a previously existing application's configuration that uses a name for the origin.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes a previously existing application.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
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

Gets the application configuration of a specific application inside a zone.

```sql
SELECT
id,
argo_smart_routing,
created_on,
dns,
edge_ips,
ip_firewall,
modified_on,
origin_direct,
origin_dns,
origin_port,
protocol,
proxy_protocol,
tls,
traffic_type
FROM cloudflare.spectrum.apps
WHERE app_id = '{{ app_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of currently existing Spectrum applications inside a zone.

```sql
SELECT
id,
argo_smart_routing,
created_on,
dns,
edge_ips,
ip_firewall,
modified_on,
origin_direct,
origin_dns,
origin_port,
protocol,
proxy_protocol,
tls,
traffic_type
FROM cloudflare.spectrum.apps
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND direction = '{{ direction }}'
AND order = '{{ order }}'
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

Creates a new Spectrum application from a configuration using a name for the origin.

```sql
INSERT INTO cloudflare.spectrum.apps (
argo_smart_routing,
dns,
edge_ips,
ip_firewall,
origin_direct,
origin_dns,
origin_port,
protocol,
proxy_protocol,
tls,
traffic_type,
zone_id
)
SELECT 
{{ argo_smart_routing }},
'{{ dns }}' /* required */,
'{{ edge_ips }}',
{{ ip_firewall }},
'{{ origin_direct }}',
'{{ origin_dns }}',
{{ origin_port }},
'{{ protocol }}' /* required */,
'{{ proxy_protocol }}',
'{{ tls }}',
'{{ traffic_type }}',
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
- name: apps
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the apps resource.
    - name: argo_smart_routing
      value: {{ argo_smart_routing }}
      description: |
        Enables Argo Smart Routing for this application. Notes: Only available for TCP applications with traffic_type set to "direct".
      default: false
    - name: dns
      description: |
        The name and type of DNS record for the Spectrum application.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: edge_ips
      description: |
        The anycast edge IP configuration for the hostname of this application.
      value:
        connectivity: "{{ connectivity }}"
        type: "{{ type }}"
        ips:
          - "{{ ips }}"
      default: [object Object]
    - name: ip_firewall
      value: {{ ip_firewall }}
      description: |
        Enables IP Access Rules for this application. Notes: Only available for TCP applications.
      default: false
    - name: origin_direct
      value:
        - "{{ origin_direct }}"
      description: |
        List of origin IP addresses. Array may contain multiple IP addresses for load balancing.
    - name: origin_dns
      description: |
        The name and type of DNS record for the Spectrum application.
      value:
        name: "{{ name }}"
        ttl: {{ ttl }}
        type: "{{ type }}"
    - name: origin_port
      value: {{ origin_port }}
      description: |
        The destination port at the origin. Only specified in conjunction with origin_dns. May use an integer to specify a single origin port, for example \`1000\`, or a string to specify a range of origin ports, for example \`"1000-2000"\`. Notes: If specifying a port range, the number of ports in the range must match the number of ports specified in the "protocol" field.
    - name: protocol
      value: "{{ protocol }}"
      description: |
        The port configuration at Cloudflare's edge. May specify a single port, for example \`"tcp/1000"\`, or a range of ports, for example \`"tcp/1000-2000"\`.
    - name: proxy_protocol
      value: "{{ proxy_protocol }}"
      description: |
        Enables Proxy Protocol to the origin. Refer to [Enable Proxy protocol](https://developers.cloudflare.com/spectrum/getting-started/proxy-protocol/) for implementation details on PROXY Protocol V1, PROXY Protocol V2, and Simple Proxy Protocol.
      valid_values: ['off', 'v1', 'v2', 'simple']
      default: off
    - name: tls
      value: "{{ tls }}"
      description: |
        The type of TLS termination associated with the application.
      valid_values: ['off', 'flexible', 'full', 'strict']
      default: off
    - name: traffic_type
      value: "{{ traffic_type }}"
      description: |
        Determines how data travels from the edge to your origin. When set to "direct", Spectrum will send traffic directly to your origin, and the application's type is derived from the \`protocol\`. When set to "http" or "https", Spectrum will apply Cloudflare's HTTP/HTTPS features as it sends traffic to your origin, and the application type matches this property exactly.
      valid_values: ['direct', 'http', 'https']
      default: direct
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

Updates a previously existing application's configuration that uses a name for the origin.

```sql
REPLACE cloudflare.spectrum.apps
SET 
argo_smart_routing = {{ argo_smart_routing }},
dns = '{{ dns }}',
edge_ips = '{{ edge_ips }}',
ip_firewall = {{ ip_firewall }},
origin_direct = '{{ origin_direct }}',
origin_dns = '{{ origin_dns }}',
origin_port = {{ origin_port }},
protocol = '{{ protocol }}',
proxy_protocol = '{{ proxy_protocol }}',
tls = '{{ tls }}',
traffic_type = '{{ traffic_type }}'
WHERE 
app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND dns = '{{ dns }}' --required
AND protocol = '{{ protocol }}' --required
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

Deletes a previously existing application.

```sql
DELETE FROM cloudflare.spectrum.apps
WHERE app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
