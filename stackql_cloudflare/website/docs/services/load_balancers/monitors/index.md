--- 
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
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

Creates, updates, deletes, gets or lists a <code>monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="monitors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.load_balancers.monitors" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'get_by_user', value: 'get_by_user' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="get_by_account">

Monitor Details response.

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
    <td> (example: f1aba936b94213e5b8dca0c0dbf1f9cc)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_insecure" /></td>
    <td><code>boolean</code></td>
    <td>Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_down" /></td>
    <td><code>integer</code></td>
    <td>To be marked unhealthy the monitored origin must fail this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_up" /></td>
    <td><code>integer</code></td>
    <td>To be marked healthy the monitored origin must pass this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Object description. (default: , example: Login page monitor)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_body" /></td>
    <td><code>string</code></td>
    <td>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: alive)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_codes" /></td>
    <td><code>string</code></td>
    <td>The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: 2xx)</td>
</tr>
<tr>
    <td><CopyableCode code="follow_redirects" /></td>
    <td><code>boolean</code></td>
    <td>Follow redirects if returned by the origin. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="header" /></td>
    <td><code>object</code></td>
    <td>The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="method" /></td>
    <td><code>string</code></td>
    <td>The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established' for TCP based health checks. (example: GET, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The endpoint path you want to conduct a health check against. This parameter is only valid for HTTP and HTTPS monitors. (example: /health, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port number to connect to for the health check. Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define the port when using a non-standard port (HTTP: default 80, HTTPS: default 443). (x-stainless-terraform-configurability: optional)</td>
</tr>
<tr>
    <td><CopyableCode code="probe_zone" /></td>
    <td><code>string</code></td>
    <td>Assign this monitor to emulate the specified zone while probing. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>integer</code></td>
    <td>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout (in seconds) before marking the health check as failed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The protocol to use for the health check. Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'. (http, https, tcp, udp_icmp, icmp_ping, smtp) (default: http, example: https)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List Monitors response.

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
    <td> (example: f1aba936b94213e5b8dca0c0dbf1f9cc)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_insecure" /></td>
    <td><code>boolean</code></td>
    <td>Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_down" /></td>
    <td><code>integer</code></td>
    <td>To be marked unhealthy the monitored origin must fail this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_up" /></td>
    <td><code>integer</code></td>
    <td>To be marked healthy the monitored origin must pass this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Object description. (default: , example: Login page monitor)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_body" /></td>
    <td><code>string</code></td>
    <td>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: alive)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_codes" /></td>
    <td><code>string</code></td>
    <td>The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: 2xx)</td>
</tr>
<tr>
    <td><CopyableCode code="follow_redirects" /></td>
    <td><code>boolean</code></td>
    <td>Follow redirects if returned by the origin. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="header" /></td>
    <td><code>object</code></td>
    <td>The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="method" /></td>
    <td><code>string</code></td>
    <td>The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established' for TCP based health checks. (example: GET, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The endpoint path you want to conduct a health check against. This parameter is only valid for HTTP and HTTPS monitors. (example: /health, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port number to connect to for the health check. Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define the port when using a non-standard port (HTTP: default 80, HTTPS: default 443). (x-stainless-terraform-configurability: optional)</td>
</tr>
<tr>
    <td><CopyableCode code="probe_zone" /></td>
    <td><code>string</code></td>
    <td>Assign this monitor to emulate the specified zone while probing. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>integer</code></td>
    <td>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout (in seconds) before marking the health check as failed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The protocol to use for the health check. Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'. (http, https, tcp, udp_icmp, icmp_ping, smtp) (default: http, example: https)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_user">

Monitor Details response.

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
    <td> (example: f1aba936b94213e5b8dca0c0dbf1f9cc)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_insecure" /></td>
    <td><code>boolean</code></td>
    <td>Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_down" /></td>
    <td><code>integer</code></td>
    <td>To be marked unhealthy the monitored origin must fail this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_up" /></td>
    <td><code>integer</code></td>
    <td>To be marked healthy the monitored origin must pass this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Object description. (default: , example: Login page monitor)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_body" /></td>
    <td><code>string</code></td>
    <td>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: alive)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_codes" /></td>
    <td><code>string</code></td>
    <td>The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: 2xx)</td>
</tr>
<tr>
    <td><CopyableCode code="follow_redirects" /></td>
    <td><code>boolean</code></td>
    <td>Follow redirects if returned by the origin. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="header" /></td>
    <td><code>object</code></td>
    <td>The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="method" /></td>
    <td><code>string</code></td>
    <td>The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established' for TCP based health checks. (example: GET, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The endpoint path you want to conduct a health check against. This parameter is only valid for HTTP and HTTPS monitors. (example: /health, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port number to connect to for the health check. Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define the port when using a non-standard port (HTTP: default 80, HTTPS: default 443). (x-stainless-terraform-configurability: optional)</td>
</tr>
<tr>
    <td><CopyableCode code="probe_zone" /></td>
    <td><code>string</code></td>
    <td>Assign this monitor to emulate the specified zone while probing. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>integer</code></td>
    <td>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout (in seconds) before marking the health check as failed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The protocol to use for the health check. Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'. (http, https, tcp, udp_icmp, icmp_ping, smtp) (default: http, example: https)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_user">

Successful list monitors response.

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
    <td> (example: f1aba936b94213e5b8dca0c0dbf1f9cc)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_insecure" /></td>
    <td><code>boolean</code></td>
    <td>Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_down" /></td>
    <td><code>integer</code></td>
    <td>To be marked unhealthy the monitored origin must fail this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_up" /></td>
    <td><code>integer</code></td>
    <td>To be marked healthy the monitored origin must pass this healthcheck N consecutive times.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Object description. (default: , example: Login page monitor)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_body" /></td>
    <td><code>string</code></td>
    <td>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: alive)</td>
</tr>
<tr>
    <td><CopyableCode code="expected_codes" /></td>
    <td><code>string</code></td>
    <td>The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: 2xx)</td>
</tr>
<tr>
    <td><CopyableCode code="follow_redirects" /></td>
    <td><code>boolean</code></td>
    <td>Follow redirects if returned by the origin. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="header" /></td>
    <td><code>object</code></td>
    <td>The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. This parameter is only valid for HTTP and HTTPS monitors.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="method" /></td>
    <td><code>string</code></td>
    <td>The method to use for the health check. This defaults to 'GET' for HTTP/HTTPS based checks and 'connection_established' for TCP based health checks. (example: GET, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The endpoint path you want to conduct a health check against. This parameter is only valid for HTTP and HTTPS monitors. (example: /health, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port number to connect to for the health check. Required for TCP, UDP, and SMTP checks. HTTP and HTTPS checks should only define the port when using a non-standard port (HTTP: default 80, HTTPS: default 443). (x-stainless-terraform-configurability: optional)</td>
</tr>
<tr>
    <td><CopyableCode code="probe_zone" /></td>
    <td><code>string</code></td>
    <td>Assign this monitor to emulate the specified zone while probing. This parameter is only valid for HTTP and HTTPS monitors. (default: , example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>integer</code></td>
    <td>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout (in seconds) before marking the health check as failed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The protocol to use for the health check. Currently supported protocols are 'HTTP','HTTPS', 'TCP', 'ICMP-PING', 'UDP-ICMP', and 'SMTP'. (http, https, tcp, udp_icmp, icmp_ping, smtp) (default: http, example: https)</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List a single configured monitor for an account.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List configured monitors for an account.</td>
</tr>
<tr>
    <td><a href="#get_by_user"><CopyableCode code="get_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a></td>
    <td></td>
    <td>List a single configured monitor for a user.</td>
</tr>
<tr>
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>List configured monitors for a user.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create a configured monitor.</td>
</tr>
<tr>
    <td><a href="#load_balancer_monitors_create_monitor"><CopyableCode code="load_balancer_monitors_create_monitor" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a configured monitor.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Apply changes to an existing monitor, overwriting the supplied properties.</td>
</tr>
<tr>
    <td><a href="#load_balancer_monitors_patch_monitor"><CopyableCode code="load_balancer_monitors_patch_monitor" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a></td>
    <td></td>
    <td>Apply changes to an existing monitor, overwriting the supplied properties.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Modify a configured monitor.</td>
</tr>
<tr>
    <td><a href="#load_balancer_monitors_update_monitor"><CopyableCode code="load_balancer_monitors_update_monitor" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a></td>
    <td></td>
    <td>Modify a configured monitor.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured monitor.</td>
</tr>
<tr>
    <td><a href="#load_balancer_monitors_delete_monitor"><CopyableCode code="load_balancer_monitors_delete_monitor" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-monitor_id"><code>monitor_id</code></a></td>
    <td></td>
    <td>Delete a configured monitor.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'get_by_user', value: 'get_by_user' },
        { label: 'list_by_user', value: 'list_by_user' }
    ]}
>
<TabItem value="get_by_account">

List a single configured monitor for an account.

```sql
SELECT
id,
allow_insecure,
consecutive_down,
consecutive_up,
created_on,
description,
expected_body,
expected_codes,
follow_redirects,
header,
interval,
method,
modified_on,
path,
port,
probe_zone,
retries,
timeout,
type
FROM cloudflare.load_balancers.monitors
WHERE monitor_id = '{{ monitor_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

List configured monitors for an account.

```sql
SELECT
id,
allow_insecure,
consecutive_down,
consecutive_up,
created_on,
description,
expected_body,
expected_codes,
follow_redirects,
header,
interval,
method,
modified_on,
path,
port,
probe_zone,
retries,
timeout,
type
FROM cloudflare.load_balancers.monitors
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_user">

List a single configured monitor for a user.

```sql
SELECT
id,
allow_insecure,
consecutive_down,
consecutive_up,
created_on,
description,
expected_body,
expected_codes,
follow_redirects,
header,
interval,
method,
modified_on,
path,
port,
probe_zone,
retries,
timeout,
type
FROM cloudflare.load_balancers.monitors
WHERE monitor_id = '{{ monitor_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_user">

List configured monitors for a user.

```sql
SELECT
id,
allow_insecure,
consecutive_down,
consecutive_up,
created_on,
description,
expected_body,
expected_codes,
follow_redirects,
header,
interval,
method,
modified_on,
path,
port,
probe_zone,
retries,
timeout,
type
FROM cloudflare.load_balancers.monitors
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'load_balancer_monitors_create_monitor', value: 'load_balancer_monitors_create_monitor' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a configured monitor.

```sql
INSERT INTO cloudflare.load_balancers.monitors (
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
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="load_balancer_monitors_create_monitor">

Create a configured monitor.

```sql
INSERT INTO cloudflare.load_balancers.monitors (
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
type
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
'{{ type }}'
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
- name: monitors
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the monitors resource.
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


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'load_balancer_monitors_patch_monitor', value: 'load_balancer_monitors_patch_monitor' }
    ]}
>
<TabItem value="edit">

Apply changes to an existing monitor, overwriting the supplied properties.

```sql
UPDATE cloudflare.load_balancers.monitors
SET 
allow_insecure = {{ allow_insecure }},
consecutive_down = {{ consecutive_down }},
consecutive_up = {{ consecutive_up }},
description = '{{ description }}',
expected_body = '{{ expected_body }}',
expected_codes = '{{ expected_codes }}',
follow_redirects = {{ follow_redirects }},
header = '{{ header }}',
interval = {{ interval }},
method = '{{ method }}',
path = '{{ path }}',
port = {{ port }},
probe_zone = '{{ probe_zone }}',
retries = {{ retries }},
timeout = {{ timeout }},
type = '{{ type }}'
WHERE 
monitor_id = '{{ monitor_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="load_balancer_monitors_patch_monitor">

Apply changes to an existing monitor, overwriting the supplied properties.

```sql
UPDATE cloudflare.load_balancers.monitors
SET 
allow_insecure = {{ allow_insecure }},
consecutive_down = {{ consecutive_down }},
consecutive_up = {{ consecutive_up }},
description = '{{ description }}',
expected_body = '{{ expected_body }}',
expected_codes = '{{ expected_codes }}',
follow_redirects = {{ follow_redirects }},
header = '{{ header }}',
interval = {{ interval }},
method = '{{ method }}',
path = '{{ path }}',
port = {{ port }},
probe_zone = '{{ probe_zone }}',
retries = {{ retries }},
timeout = {{ timeout }},
type = '{{ type }}'
WHERE 
monitor_id = '{{ monitor_id }}' --required
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
        { label: 'update', value: 'update' },
        { label: 'load_balancer_monitors_update_monitor', value: 'load_balancer_monitors_update_monitor' }
    ]}
>
<TabItem value="update">

Modify a configured monitor.

```sql
REPLACE cloudflare.load_balancers.monitors
SET 
allow_insecure = {{ allow_insecure }},
consecutive_down = {{ consecutive_down }},
consecutive_up = {{ consecutive_up }},
description = '{{ description }}',
expected_body = '{{ expected_body }}',
expected_codes = '{{ expected_codes }}',
follow_redirects = {{ follow_redirects }},
header = '{{ header }}',
interval = {{ interval }},
method = '{{ method }}',
path = '{{ path }}',
port = {{ port }},
probe_zone = '{{ probe_zone }}',
retries = {{ retries }},
timeout = {{ timeout }},
type = '{{ type }}'
WHERE 
monitor_id = '{{ monitor_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="load_balancer_monitors_update_monitor">

Modify a configured monitor.

```sql
REPLACE cloudflare.load_balancers.monitors
SET 
allow_insecure = {{ allow_insecure }},
consecutive_down = {{ consecutive_down }},
consecutive_up = {{ consecutive_up }},
description = '{{ description }}',
expected_body = '{{ expected_body }}',
expected_codes = '{{ expected_codes }}',
follow_redirects = {{ follow_redirects }},
header = '{{ header }}',
interval = {{ interval }},
method = '{{ method }}',
path = '{{ path }}',
port = {{ port }},
probe_zone = '{{ probe_zone }}',
retries = {{ retries }},
timeout = {{ timeout }},
type = '{{ type }}'
WHERE 
monitor_id = '{{ monitor_id }}' --required
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
        { label: 'delete', value: 'delete' },
        { label: 'load_balancer_monitors_delete_monitor', value: 'load_balancer_monitors_delete_monitor' }
    ]}
>
<TabItem value="delete">

Delete a configured monitor.

```sql
DELETE FROM cloudflare.load_balancers.monitors
WHERE monitor_id = '{{ monitor_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="load_balancer_monitors_delete_monitor">

Delete a configured monitor.

```sql
DELETE FROM cloudflare.load_balancers.monitors
WHERE monitor_id = '{{ monitor_id }}' --required
;
```
</TabItem>
</Tabs>
