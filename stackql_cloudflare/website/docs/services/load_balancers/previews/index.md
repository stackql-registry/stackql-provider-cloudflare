--- 
title: previews
hide_title: false
hide_table_of_contents: false
keywords:
  - previews
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

Creates, updates, deletes, gets or lists a <code>previews</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="previews" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.load_balancers.previews" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Preview Result response.

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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td>Resulting health data from a preview operation.</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Whether the API call was successful. (true)</td>
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
    <td><a href="#parameter-preview_id"><code>preview_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get the result of a previous preview operation using the provided preview_id.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Preview pools using the specified monitor with provided monitor details. The returned preview_id can be used in the preview endpoint to retrieve the results.</td>
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
<tr id="parameter-monitor_id">
    <td><CopyableCode code="monitor_id" /></td>
    <td><code>string</code></td>
    <td>The Load Balancer monitor ID.</td>
</tr>
<tr id="parameter-preview_id">
    <td><CopyableCode code="preview_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the result of a previous preview operation using the provided preview_id.

```sql
SELECT
errors,
messages,
result,
success
FROM cloudflare.load_balancers.previews
WHERE preview_id = '{{ preview_id }}' -- required
AND account_id = '{{ account_id }}' -- required
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

Preview pools using the specified monitor with provided monitor details. The returned preview_id can be used in the preview endpoint to retrieve the results.

```sql
INSERT INTO cloudflare.load_balancers.previews (
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
monitor_id,
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
'{{ monitor_id }}',
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
- name: previews
  props:
    - name: monitor_id
      value: "{{ monitor_id }}"
      description: Required parameter for the previews resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the previews resource.
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
