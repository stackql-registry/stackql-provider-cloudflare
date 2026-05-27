--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - connectivity
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.connectivity.services" /></td></tr>
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

Successfully retrieved Workers VPC connectivity service

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: web-server)</td>
</tr>
<tr>
    <td><CopyableCode code="service_id" /></td>
    <td><code>string (uuid)</code></td>
    <td> (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="app_protocol" /></td>
    <td><code>string</code></td>
    <td> (postgresql, mysql) (example: postgresql)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2024-01-15T09:30:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="http_port" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="https_port" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tcp_port" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tls_settings" /></td>
    <td><code>object</code></td>
    <td>TLS settings for a connectivity service. If omitted, the default mode (`verify_full`) is used.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (tcp, http)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2024-01-15T10:45:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Successfully retrieved Workers VPC connectivity services

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: web-server)</td>
</tr>
<tr>
    <td><CopyableCode code="service_id" /></td>
    <td><code>string (uuid)</code></td>
    <td> (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="app_protocol" /></td>
    <td><code>string</code></td>
    <td> (postgresql, mysql) (example: postgresql)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2024-01-15T09:30:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="http_port" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="https_port" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tcp_port" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tls_settings" /></td>
    <td><code>object</code></td>
    <td>TLS settings for a connectivity service. If omitted, the default mode (`verify_full`) is used.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (tcp, http)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2024-01-15T10:45:00Z)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_id"><code>service_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_id"><code>service_id</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-service_id"><code>service_id</code></a></td>
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
<tr id="parameter-service_id">
    <td><CopyableCode code="service_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer (int32)</code></td>
    <td>Current page in the response</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer (int32)</code></td>
    <td>Max amount of entries returned per page</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
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

Successfully retrieved Workers VPC connectivity service

```sql
SELECT
name,
service_id,
app_protocol,
created_at,
host,
http_port,
https_port,
tcp_port,
tls_settings,
type,
updated_at
FROM cloudflare.connectivity.services
WHERE account_id = '{{ account_id }}' -- required
AND service_id = '{{ service_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Successfully retrieved Workers VPC connectivity services

```sql
SELECT
name,
service_id,
app_protocol,
created_at,
host,
http_port,
https_port,
tcp_port,
tls_settings,
type,
updated_at
FROM cloudflare.connectivity.services
WHERE account_id = '{{ account_id }}' -- required
AND type = '{{ type }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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
INSERT INTO cloudflare.connectivity.services (
host,
name,
tls_settings,
type,
http_port,
https_port,
app_protocol,
tcp_port,
account_id
)
SELECT 
'{{ host }}' /* required */,
'{{ name }}' /* required */,
'{{ tls_settings }}',
'{{ type }}' /* required */,
{{ http_port }},
{{ https_port }},
'{{ app_protocol }}',
{{ tcp_port }},
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
- name: services
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the services resource.
    - name: host
      value:
        ipv4: "{{ ipv4 }}"
        network:
          tunnel_id: "{{ tunnel_id }}"
        ipv6: "{{ ipv6 }}"
        hostname: "{{ hostname }}"
        resolver_network:
          resolver_ips:
            - "{{ resolver_ips }}"
          tunnel_id: "{{ tunnel_id }}"
    - name: name
      value: "{{ name }}"
    - name: tls_settings
      description: |
        TLS settings for a connectivity service. If omitted, the default mode (\`verify_full\`) is used.
      value:
        cert_verification_mode: "{{ cert_verification_mode }}"
    - name: type
      value: "{{ type }}"
      valid_values: ['tcp', 'http']
    - name: http_port
      value: {{ http_port }}
    - name: https_port
      value: {{ https_port }}
    - name: app_protocol
      value: "{{ app_protocol }}"
      valid_values: ['postgresql', 'mysql']
    - name: tcp_port
      value: {{ tcp_port }}
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
REPLACE cloudflare.connectivity.services
SET 
host = '{{ host }}',
name = '{{ name }}',
tls_settings = '{{ tls_settings }}',
type = '{{ type }}',
http_port = {{ http_port }},
https_port = {{ https_port }},
app_protocol = '{{ app_protocol }}',
tcp_port = {{ tcp_port }}
WHERE 
account_id = '{{ account_id }}' --required
AND service_id = '{{ service_id }}' --required
AND host = '{{ host }}' --required
AND name = '{{ name }}' --required
AND type = '{{ type }}' --required
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

No description available.

```sql
DELETE FROM cloudflare.connectivity.services
WHERE account_id = '{{ account_id }}' --required
AND service_id = '{{ service_id }}' --required
;
```
</TabItem>
</Tabs>
