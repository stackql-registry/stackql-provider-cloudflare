--- 
title: health
hide_title: false
hide_table_of_contents: false
keywords:
  - health
  - load_balancers
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

Creates, updates, deletes, gets or lists a <code>health</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="health" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.load_balancers.health" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="list_by_account">

Pool Health Details response.

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
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>Pool ID. (example: 17b5962d775c646f3f9725cbc7a53df4)</td>
</tr>
<tr>
    <td><CopyableCode code="pop_health" /></td>
    <td><code>object</code></td>
    <td>List of regions and associated health status.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_user">

Pool Health Details response.

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
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>Pool ID. (example: 17b5962d775c646f3f9725cbc7a53df4)</td>
</tr>
<tr>
    <td><CopyableCode code="pop_health" /></td>
    <td><code>object</code></td>
    <td>List of regions and associated health status.</td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch the latest pool health status for a single pool.</td>
</tr>
<tr>
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a></td>
    <td></td>
    <td>Fetch the latest pool health status for a single pool.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Preview pool health using provided monitor details. The returned preview_id can be used in the preview endpoint to retrieve the results.</td>
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
<tr id="parameter-pool_id">
    <td><CopyableCode code="pool_id" /></td>
    <td><code>string</code></td>
    <td>The Load Balancer pool ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="list_by_account">

Fetch the latest pool health status for a single pool.

```sql
SELECT
pool_id,
pop_health
FROM cloudflare.load_balancers.health
WHERE pool_id = '{{ pool_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_user">

Fetch the latest pool health status for a single pool.

```sql
SELECT
pool_id,
pop_health
FROM cloudflare.load_balancers.health
WHERE pool_id = '{{ pool_id }}' -- required
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

Preview pool health using provided monitor details. The returned preview_id can be used in the preview endpoint to retrieve the results.

```sql
INSERT INTO cloudflare.load_balancers.health (
allow_insecure,
consecutive_down,
consecutive_up,
description,
expected_body,
expected_codes,
follow_redirects,
header,
interval,
method,
path,
port,
probe_zone,
retries,
timeout,
type,
pool_id,
account_id
)
SELECT 
{{ allow_insecure }},
{{ consecutive_down }},
{{ consecutive_up }},
'{{ description }}',
'{{ expected_body }}',
'{{ expected_codes }}',
{{ follow_redirects }},
'{{ header }}',
{{ interval }},
'{{ method }}',
'{{ path }}',
{{ port }},
'{{ probe_zone }}',
{{ retries }},
{{ timeout }},
'{{ type }}',
'{{ pool_id }}',
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
- name: health
  props:
    - name: pool_id
      value: "{{ pool_id }}"
      description: Required parameter for the health resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the health resource.
    - name: allow_insecure
      value: {{ allow_insecure }}
      description: |
        Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTP and HTTPS monitors.
      default: false
    - name: consecutive_down
      value: {{ consecutive_down }}
      description: |
        To be marked unhealthy the monitored origin must fail this healthcheck N consecutive times.
    - name: consecutive_up
      value: {{ consecutive_up }}
      description: |
        To be marked healthy the monitored origin must pass this healthcheck N consecutive times.
    - name: description
      value: "{{ description }}"
      description: |
        Object description.
      default: 
    - name: expected_body
      value: "{{ expected_body }}"
      description: |
        A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. This parameter is only valid for HTTP and HTTPS monitors.
      default: 
    - name: expected_codes
      value: "{{ expected_codes }}"
      description: |
        The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS monitors.
      default: 
    - name: follow_redirects
      value: {{ follow_redirects }}
      description: |
        Follow redirects if returned by the origin. This parameter is only valid for HTTP and HTTPS monitors.
      default: false
    - name: header
      value: "{{ header }}"
      description: |
        The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. This parameter is only valid for HTTP and HTTPS monitors.
    - name: interval
      value: {{ interval }}
      description: |
        The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations.
      default: 60
    - name: method
      value: "{{ method }}"
      description: |
        The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established' for TCP based health checks.
    - name: path
      value: "{{ path }}"
      description: |
        The endpoint path you want to conduct a health check against. This parameter is only valid for HTTP and HTTPS monitors.
    - name: port
      value: {{ port }}
      description: |
        The port number to connect to for the health check. Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define the port when using a non-standard port (HTTP: default 80, HTTPS: default 443).
    - name: probe_zone
      value: "{{ probe_zone }}"
      description: |
        Assign this monitor to emulate the specified zone while probing. This parameter is only valid for HTTP and HTTPS monitors.
      default: 
    - name: retries
      value: {{ retries }}
      description: |
        The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.
      default: 2
    - name: timeout
      value: {{ timeout }}
      description: |
        The timeout (in seconds) before marking the health check as failed.
      default: 5
    - name: type
      value: "{{ type }}"
      description: |
        The protocol to use for the health check. Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'.
      valid_values: ['http', 'https', 'tcp', 'udp_icmp', 'icmp_ping', 'smtp']
      default: http
`}</CodeBlock>

</TabItem>
</Tabs>
