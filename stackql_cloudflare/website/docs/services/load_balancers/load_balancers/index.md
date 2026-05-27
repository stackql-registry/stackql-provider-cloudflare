--- 
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
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

Creates, updates, deletes, gets or lists a <code>load_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="load_balancers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.load_balancers.load_balancers" /></td></tr>
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

Load Balancer Details response.

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
    <td> (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The DNS hostname to associate with your Load Balancer. If this hostname already exists as a DNS record in Cloudflare's DNS, the Load Balancer will take precedence and the DNS record will not be used. (example: www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_name" /></td>
    <td><code>string</code></td>
    <td> (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="adaptive_routing" /></td>
    <td><code>object</code></td>
    <td>Controls features that modify the routing of requests to pools and origins in response to dynamic conditions, such as during the interval between active health monitoring requests. For example, zero-downtime failover occurs immediately when an origin becomes unavailable due to HTTP 521, 522, or 523 response codes. If there is another healthy origin in the same pool, the request is retried once against this alternate origin.</td>
</tr>
<tr>
    <td><CopyableCode code="country_pools" /></td>
    <td><code>object</code></td>
    <td>A mapping of country codes to a list of pool IDs (ordered by their failover priority) for the given country. Any country not explicitly defined will fall back to using the corresponding region_pool mapping if it exists else to default_pools.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="default_pools" /></td>
    <td><code>array</code></td>
    <td>A list of pool IDs ordered by their failover priority. Pools defined here are used by default, or when region_pools are not configured for a given region.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Object description. (example: Load Balancer for www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable (the default) this load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="fallback_pool" /></td>
    <td><code>string</code></td>
    <td>The pool ID to use when all other pools are detected as unhealthy.</td>
</tr>
<tr>
    <td><CopyableCode code="location_strategy" /></td>
    <td><code>object</code></td>
    <td>Controls location-based steering for non-proxied requests. See `steering_policy` to learn how steering is affected.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>List of networks where Load Balancer or Pool is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="pop_pools" /></td>
    <td><code>object</code></td>
    <td>Enterprise only: A mapping of Cloudflare PoP identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). Any PoPs not explicitly defined will fall back to using the corresponding country_pool, then region_pool mapping if it exists else to default_pools.</td>
</tr>
<tr>
    <td><CopyableCode code="proxied" /></td>
    <td><code>boolean</code></td>
    <td>Whether the hostname should be gray clouded (false) or orange clouded (true).</td>
</tr>
<tr>
    <td><CopyableCode code="random_steering" /></td>
    <td><code>object</code></td>
    <td>Configures pool weights. - `steering_policy="random"`: A random pool is selected with probability proportional to pool weights. - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each pool's outstanding requests. - `steering_policy="least_connections"`: Use pool weights to scale each pool's open connections.</td>
</tr>
<tr>
    <td><CopyableCode code="region_pools" /></td>
    <td><code>object</code></td>
    <td>A mapping of region codes to a list of pool IDs (ordered by their failover priority) for the given region. Any regions not explicitly defined will fall back to using default_pools.</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>BETA Field Not General Access: A list of rules for this load balancer to execute.</td>
</tr>
<tr>
    <td><CopyableCode code="session_affinity" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of session affinity the load balancer should use unless specified as `"none"`. The supported types are: - `"cookie"`: On the first request to a proxied load balancer, a cookie is generated, encoding information of which origin the request will be forwarded to. Subsequent requests, by the same client to the same load balancer, will be sent to the origin server the cookie encodes, for the duration of the cookie and as long as the origin server remains healthy. If the cookie has expired or the origin server is unhealthy, then a new origin server is calculated and used. - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin selection is stable and based on the client's ip address. - `"header"`: On the first request to a proxied load balancer, a session key based on the configured HTTP headers (see `session_affinity_attributes.headers`) is generated, encoding the request headers used for storing in the load balancer session state which origin the request will be forwarded to. Subsequent requests to the load balancer with the same headers will be sent to the same origin server, for the duration of the session and as long as the origin server remains healthy. If the session has been idle for the duration of `session_affinity_ttl` seconds or the origin server is unhealthy, then a new origin server is calculated and used. See `headers` in `session_affinity_attributes` for additional required configuration. (none, cookie, ip_cookie, header) (default: none, example: cookie)</td>
</tr>
<tr>
    <td><CopyableCode code="session_affinity_attributes" /></td>
    <td><code>object</code></td>
    <td>Configures attributes for session affinity.</td>
</tr>
<tr>
    <td><CopyableCode code="session_affinity_ttl" /></td>
    <td><code>number</code></td>
    <td>Time, in seconds, until a client's session expires after being created. Once the expiry time has been reached, subsequent requests may get sent to a different origin server. The accepted ranges per `session_affinity` policy are: - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used unless explicitly set. The accepted range of values is between [1800, 604800]. - `"header"`: The current default of 1800 seconds will be used unless explicitly set. The accepted range of values is between [30, 3600]. Note: With session affinity by header, sessions only expire after they haven't been used for the number of seconds specified.</td>
</tr>
<tr>
    <td><CopyableCode code="steering_policy" /></td>
    <td><code>string</code></td>
    <td>Steering Policy for this load balancer. - `"off"`: Use `default_pools`. - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied requests, the country for `country_pools` is determined by `location_strategy`. - `"random"`: Select a pool randomly. - `"dynamic_latency"`: Use round trip time to select the closest pool in default_pools (requires pool health checks). - `"proximity"`: Use the pools' latitude and longitude to select the closest pool using the Cloudflare PoP location for proxied requests or the location determined by `location_strategy` for non-proxied requests. - `"least_outstanding_requests"`: Select a pool by taking into consideration `random_steering` weights, as well as each pool's number of outstanding requests. Pools with more pending requests are weighted proportionately less relative to others. - `"least_connections"`: Select a pool by taking into consideration `random_steering` weights, as well as each pool's number of open connections. Pools with more open connections are weighted proportionately less relative to others. Supported for HTTP/1 and HTTP/2 connections. - `""`: Will map to `"geo"` if you use `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`. (off, geo, random, dynamic_latency, proximity, least_outstanding_requests, least_connections, ) (default: , example: dynamic_latency)</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>number</code></td>
    <td>Time to live (TTL) of the DNS entry for the IP address returned by this load balancer. This only applies to gray-clouded (unproxied) load balancers.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Load Balancers response.

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
    <td> (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The DNS hostname to associate with your Load Balancer. If this hostname already exists as a DNS record in Cloudflare's DNS, the Load Balancer will take precedence and the DNS record will not be used. (example: www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_name" /></td>
    <td><code>string</code></td>
    <td> (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="adaptive_routing" /></td>
    <td><code>object</code></td>
    <td>Controls features that modify the routing of requests to pools and origins in response to dynamic conditions, such as during the interval between active health monitoring requests. For example, zero-downtime failover occurs immediately when an origin becomes unavailable due to HTTP 521, 522, or 523 response codes. If there is another healthy origin in the same pool, the request is retried once against this alternate origin.</td>
</tr>
<tr>
    <td><CopyableCode code="country_pools" /></td>
    <td><code>object</code></td>
    <td>A mapping of country codes to a list of pool IDs (ordered by their failover priority) for the given country. Any country not explicitly defined will fall back to using the corresponding region_pool mapping if it exists else to default_pools.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="default_pools" /></td>
    <td><code>array</code></td>
    <td>A list of pool IDs ordered by their failover priority. Pools defined here are used by default, or when region_pools are not configured for a given region.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Object description. (example: Load Balancer for www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable (the default) this load balancer.</td>
</tr>
<tr>
    <td><CopyableCode code="fallback_pool" /></td>
    <td><code>string</code></td>
    <td>The pool ID to use when all other pools are detected as unhealthy.</td>
</tr>
<tr>
    <td><CopyableCode code="location_strategy" /></td>
    <td><code>object</code></td>
    <td>Controls location-based steering for non-proxied requests. See `steering_policy` to learn how steering is affected.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>List of networks where Load Balancer or Pool is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="pop_pools" /></td>
    <td><code>object</code></td>
    <td>Enterprise only: A mapping of Cloudflare PoP identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). Any PoPs not explicitly defined will fall back to using the corresponding country_pool, then region_pool mapping if it exists else to default_pools.</td>
</tr>
<tr>
    <td><CopyableCode code="proxied" /></td>
    <td><code>boolean</code></td>
    <td>Whether the hostname should be gray clouded (false) or orange clouded (true).</td>
</tr>
<tr>
    <td><CopyableCode code="random_steering" /></td>
    <td><code>object</code></td>
    <td>Configures pool weights. - `steering_policy="random"`: A random pool is selected with probability proportional to pool weights. - `steering_policy="least_outstanding_requests"`: Use pool weights to scale each pool's outstanding requests. - `steering_policy="least_connections"`: Use pool weights to scale each pool's open connections.</td>
</tr>
<tr>
    <td><CopyableCode code="region_pools" /></td>
    <td><code>object</code></td>
    <td>A mapping of region codes to a list of pool IDs (ordered by their failover priority) for the given region. Any regions not explicitly defined will fall back to using default_pools.</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>BETA Field Not General Access: A list of rules for this load balancer to execute.</td>
</tr>
<tr>
    <td><CopyableCode code="session_affinity" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of session affinity the load balancer should use unless specified as `"none"`. The supported types are: - `"cookie"`: On the first request to a proxied load balancer, a cookie is generated, encoding information of which origin the request will be forwarded to. Subsequent requests, by the same client to the same load balancer, will be sent to the origin server the cookie encodes, for the duration of the cookie and as long as the origin server remains healthy. If the cookie has expired or the origin server is unhealthy, then a new origin server is calculated and used. - `"ip_cookie"`: Behaves the same as `"cookie"` except the initial origin selection is stable and based on the client's ip address. - `"header"`: On the first request to a proxied load balancer, a session key based on the configured HTTP headers (see `session_affinity_attributes.headers`) is generated, encoding the request headers used for storing in the load balancer session state which origin the request will be forwarded to. Subsequent requests to the load balancer with the same headers will be sent to the same origin server, for the duration of the session and as long as the origin server remains healthy. If the session has been idle for the duration of `session_affinity_ttl` seconds or the origin server is unhealthy, then a new origin server is calculated and used. See `headers` in `session_affinity_attributes` for additional required configuration. (none, cookie, ip_cookie, header) (default: none, example: cookie)</td>
</tr>
<tr>
    <td><CopyableCode code="session_affinity_attributes" /></td>
    <td><code>object</code></td>
    <td>Configures attributes for session affinity.</td>
</tr>
<tr>
    <td><CopyableCode code="session_affinity_ttl" /></td>
    <td><code>number</code></td>
    <td>Time, in seconds, until a client's session expires after being created. Once the expiry time has been reached, subsequent requests may get sent to a different origin server. The accepted ranges per `session_affinity` policy are: - `"cookie"` / `"ip_cookie"`: The current default of 23 hours will be used unless explicitly set. The accepted range of values is between [1800, 604800]. - `"header"`: The current default of 1800 seconds will be used unless explicitly set. The accepted range of values is between [30, 3600]. Note: With session affinity by header, sessions only expire after they haven't been used for the number of seconds specified.</td>
</tr>
<tr>
    <td><CopyableCode code="steering_policy" /></td>
    <td><code>string</code></td>
    <td>Steering Policy for this load balancer. - `"off"`: Use `default_pools`. - `"geo"`: Use `region_pools`/`country_pools`/`pop_pools`. For non-proxied requests, the country for `country_pools` is determined by `location_strategy`. - `"random"`: Select a pool randomly. - `"dynamic_latency"`: Use round trip time to select the closest pool in default_pools (requires pool health checks). - `"proximity"`: Use the pools' latitude and longitude to select the closest pool using the Cloudflare PoP location for proxied requests or the location determined by `location_strategy` for non-proxied requests. - `"least_outstanding_requests"`: Select a pool by taking into consideration `random_steering` weights, as well as each pool's number of outstanding requests. Pools with more pending requests are weighted proportionately less relative to others. - `"least_connections"`: Select a pool by taking into consideration `random_steering` weights, as well as each pool's number of open connections. Pools with more open connections are weighted proportionately less relative to others. Supported for HTTP/1 and HTTP/2 connections. - `""`: Will map to `"geo"` if you use `region_pools`/`country_pools`/`pop_pools` otherwise `"off"`. (off, geo, random, dynamic_latency, proximity, least_outstanding_requests, least_connections, ) (default: , example: dynamic_latency)</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>number</code></td>
    <td>Time to live (TTL) of the DNS entry for the IP address returned by this load balancer. This only applies to gray-clouded (unproxied) load balancers.</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-load_balancer_id"><code>load_balancer_id</code></a></td>
    <td></td>
    <td>Fetch a single configured load balancer.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>List configured load balancers.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-default_pools"><code>default_pools</code></a>, <a href="#parameter-fallback_pool"><code>fallback_pool</code></a></td>
    <td></td>
    <td>Create a new load balancer.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-load_balancer_id"><code>load_balancer_id</code></a></td>
    <td></td>
    <td>Apply changes to an existing load balancer, overwriting the supplied properties.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-load_balancer_id"><code>load_balancer_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-default_pools"><code>default_pools</code></a>, <a href="#parameter-fallback_pool"><code>fallback_pool</code></a></td>
    <td></td>
    <td>Update a configured load balancer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-load_balancer_id"><code>load_balancer_id</code></a></td>
    <td></td>
    <td>Delete a configured load balancer.</td>
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
<tr id="parameter-load_balancer_id">
    <td><CopyableCode code="load_balancer_id" /></td>
    <td><code>string</code></td>
    <td>The Load Balancer ID.</td>
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

Fetch a single configured load balancer.

```sql
SELECT
id,
name,
zone_name,
adaptive_routing,
country_pools,
created_on,
default_pools,
description,
enabled,
fallback_pool,
location_strategy,
modified_on,
networks,
pop_pools,
proxied,
random_steering,
region_pools,
rules,
session_affinity,
session_affinity_attributes,
session_affinity_ttl,
steering_policy,
ttl
FROM cloudflare.load_balancers.load_balancers
WHERE zone_id = '{{ zone_id }}' -- required
AND load_balancer_id = '{{ load_balancer_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List configured load balancers.

```sql
SELECT
id,
name,
zone_name,
adaptive_routing,
country_pools,
created_on,
default_pools,
description,
enabled,
fallback_pool,
location_strategy,
modified_on,
networks,
pop_pools,
proxied,
random_steering,
region_pools,
rules,
session_affinity,
session_affinity_attributes,
session_affinity_ttl,
steering_policy,
ttl
FROM cloudflare.load_balancers.load_balancers
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

Create a new load balancer.

```sql
INSERT INTO cloudflare.load_balancers.load_balancers (
adaptive_routing,
country_pools,
default_pools,
description,
fallback_pool,
location_strategy,
name,
networks,
pop_pools,
proxied,
random_steering,
region_pools,
rules,
session_affinity,
session_affinity_attributes,
session_affinity_ttl,
steering_policy,
ttl,
zone_id
)
SELECT 
'{{ adaptive_routing }}',
'{{ country_pools }}',
'{{ default_pools }}' /* required */,
'{{ description }}',
'{{ fallback_pool }}' /* required */,
'{{ location_strategy }}',
'{{ name }}' /* required */,
'{{ networks }}',
'{{ pop_pools }}',
{{ proxied }},
'{{ random_steering }}',
'{{ region_pools }}',
'{{ rules }}',
'{{ session_affinity }}',
'{{ session_affinity_attributes }}',
{{ session_affinity_ttl }},
'{{ steering_policy }}',
{{ ttl }},
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
- name: load_balancers
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the load_balancers resource.
    - name: adaptive_routing
      description: |
        Controls features that modify the routing of requests to pools and origins in response to dynamic conditions, such as during the interval between active health monitoring requests. For example, zero-downtime failover occurs immediately when an origin becomes unavailable due to HTTP 521, 522, or 523 response codes. If there is another healthy origin in the same pool, the request is retried once against this alternate origin.
      value:
        failover_across_pools: {{ failover_across_pools }}
    - name: country_pools
      value: "{{ country_pools }}"
      description: |
        A mapping of country codes to a list of pool IDs (ordered by their failover priority) for the given country. Any country not explicitly defined will fall back to using the corresponding region_pool mapping if it exists else to default_pools.
    - name: default_pools
      value:
        - "{{ default_pools }}"
      description: |
        A list of pool IDs ordered by their failover priority. Pools defined here are used by default, or when region_pools are not configured for a given region.
    - name: description
      value: "{{ description }}"
      description: |
        Object description.
    - name: fallback_pool
      value: "{{ fallback_pool }}"
      description: |
        The pool ID to use when all other pools are detected as unhealthy.
    - name: location_strategy
      description: |
        Controls location-based steering for non-proxied requests. See \`steering_policy\` to learn how steering is affected.
      value:
        mode: "{{ mode }}"
        prefer_ecs: "{{ prefer_ecs }}"
    - name: name
      value: "{{ name }}"
      description: |
        The DNS hostname to associate with your Load Balancer. If this hostname already exists as a DNS record in Cloudflare's DNS, the Load Balancer will take precedence and the DNS record will not be used.
    - name: networks
      value:
        - "{{ networks }}"
      description: |
        List of networks where Load Balancer or Pool is enabled.
    - name: pop_pools
      value: "{{ pop_pools }}"
      description: |
        Enterprise only: A mapping of Cloudflare PoP identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). Any PoPs not explicitly defined will fall back to using the corresponding country_pool, then region_pool mapping if it exists else to default_pools.
    - name: proxied
      value: {{ proxied }}
      description: |
        Whether the hostname should be gray clouded (false) or orange clouded (true).
      default: false
    - name: random_steering
      description: |
        Configures pool weights. - \`steering_policy="random"\`: A random pool is selected with probability proportional to pool weights. - \`steering_policy="least_outstanding_requests"\`: Use pool weights to scale each pool's outstanding requests. - \`steering_policy="least_connections"\`: Use pool weights to scale each pool's open connections.
      value:
        default_weight: {{ default_weight }}
        pool_weights: "{{ pool_weights }}"
    - name: region_pools
      value: "{{ region_pools }}"
      description: |
        A mapping of region codes to a list of pool IDs (ordered by their failover priority) for the given region. Any regions not explicitly defined will fall back to using default_pools.
    - name: rules
      description: |
        BETA Field Not General Access: A list of rules for this load balancer to execute.
      value:
        - condition: "{{ condition }}"
          disabled: {{ disabled }}
          fixed_response:
            content_type: "{{ content_type }}"
            location: "{{ location }}"
            message_body: "{{ message_body }}"
            status_code: {{ status_code }}
          name: "{{ name }}"
          overrides:
            adaptive_routing:
              failover_across_pools: {{ failover_across_pools }}
            country_pools: "{{ country_pools }}"
            default_pools:
              - "{{ default_pools }}"
            fallback_pool: "{{ fallback_pool }}"
            location_strategy:
              mode: "{{ mode }}"
              prefer_ecs: "{{ prefer_ecs }}"
            pop_pools: "{{ pop_pools }}"
            random_steering:
              default_weight: {{ default_weight }}
              pool_weights: "{{ pool_weights }}"
            region_pools: "{{ region_pools }}"
            session_affinity: "{{ session_affinity }}"
            session_affinity_attributes:
              drain_duration: {{ drain_duration }}
              headers:
                - "{{ headers }}"
              require_all_headers: {{ require_all_headers }}
              samesite: "{{ samesite }}"
              secure: "{{ secure }}"
              zero_downtime_failover: "{{ zero_downtime_failover }}"
            session_affinity_ttl: {{ session_affinity_ttl }}
            steering_policy: "{{ steering_policy }}"
            ttl: {{ ttl }}
          priority: {{ priority }}
          terminates: {{ terminates }}
    - name: session_affinity
      value: "{{ session_affinity }}"
      description: |
        Specifies the type of session affinity the load balancer should use unless specified as \`"none"\`. The supported types are: - \`"cookie"\`: On the first request to a proxied load balancer, a cookie is generated, encoding information of which origin the request will be forwarded to. Subsequent requests, by the same client to the same load balancer, will be sent to the origin server the cookie encodes, for the duration of the cookie and as long as the origin server remains healthy. If the cookie has expired or the origin server is unhealthy, then a new origin server is calculated and used. - \`"ip_cookie"\`: Behaves the same as \`"cookie"\` except the initial origin selection is stable and based on the client's ip address. - \`"header"\`: On the first request to a proxied load balancer, a session key based on the configured HTTP headers (see \`session_affinity_attributes.headers\`) is generated, encoding the request headers used for storing in the load balancer session state which origin the request will be forwarded to. Subsequent requests to the load balancer with the same headers will be sent to the same origin server, for the duration of the session and as long as the origin server remains healthy. If the session has been idle for the duration of \`session_affinity_ttl\` seconds or the origin server is unhealthy, then a new origin server is calculated and used. See \`headers\` in \`session_affinity_attributes\` for additional required configuration.
      valid_values: ['none', 'cookie', 'ip_cookie', 'header']
      default: none
    - name: session_affinity_attributes
      description: |
        Configures attributes for session affinity.
      value:
        drain_duration: {{ drain_duration }}
        headers:
          - "{{ headers }}"
        require_all_headers: {{ require_all_headers }}
        samesite: "{{ samesite }}"
        secure: "{{ secure }}"
        zero_downtime_failover: "{{ zero_downtime_failover }}"
    - name: session_affinity_ttl
      value: {{ session_affinity_ttl }}
      description: |
        Time, in seconds, until a client's session expires after being created. Once the expiry time has been reached, subsequent requests may get sent to a different origin server. The accepted ranges per \`session_affinity\` policy are: - \`"cookie"\` / \`"ip_cookie"\`: The current default of 23 hours will be used unless explicitly set. The accepted range of values is between [1800, 604800]. - \`"header"\`: The current default of 1800 seconds will be used unless explicitly set. The accepted range of values is between [30, 3600]. Note: With session affinity by header, sessions only expire after they haven't been used for the number of seconds specified.
    - name: steering_policy
      value: "{{ steering_policy }}"
      description: |
        Steering Policy for this load balancer. - \`"off"\`: Use \`default_pools\`. - \`"geo"\`: Use \`region_pools\`/\`country_pools\`/\`pop_pools\`. For non-proxied requests, the country for \`country_pools\` is determined by \`location_strategy\`. - \`"random"\`: Select a pool randomly. - \`"dynamic_latency"\`: Use round trip time to select the closest pool in default_pools (requires pool health checks). - \`"proximity"\`: Use the pools' latitude and longitude to select the closest pool using the Cloudflare PoP location for proxied requests or the location determined by \`location_strategy\` for non-proxied requests. - \`"least_outstanding_requests"\`: Select a pool by taking into consideration \`random_steering\` weights, as well as each pool's number of outstanding requests. Pools with more pending requests are weighted proportionately less relative to others. - \`"least_connections"\`: Select a pool by taking into consideration \`random_steering\` weights, as well as each pool's number of open connections. Pools with more open connections are weighted proportionately less relative to others. Supported for HTTP/1 and HTTP/2 connections. - \`""\`: Will map to \`"geo"\` if you use \`region_pools\`/\`country_pools\`/\`pop_pools\` otherwise \`"off"\`.
      valid_values: ['off', 'geo', 'random', 'dynamic_latency', 'proximity', 'least_outstanding_requests', 'least_connections', '']
      default: 
    - name: ttl
      value: {{ ttl }}
      description: |
        Time to live (TTL) of the DNS entry for the IP address returned by this load balancer. This only applies to gray-clouded (unproxied) load balancers.
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

Apply changes to an existing load balancer, overwriting the supplied properties.

```sql
UPDATE cloudflare.load_balancers.load_balancers
SET 
adaptive_routing = '{{ adaptive_routing }}',
country_pools = '{{ country_pools }}',
default_pools = '{{ default_pools }}',
description = '{{ description }}',
enabled = {{ enabled }},
fallback_pool = '{{ fallback_pool }}',
location_strategy = '{{ location_strategy }}',
name = '{{ name }}',
pop_pools = '{{ pop_pools }}',
proxied = {{ proxied }},
random_steering = '{{ random_steering }}',
region_pools = '{{ region_pools }}',
rules = '{{ rules }}',
session_affinity = '{{ session_affinity }}',
session_affinity_attributes = '{{ session_affinity_attributes }}',
session_affinity_ttl = {{ session_affinity_ttl }},
steering_policy = '{{ steering_policy }}',
ttl = {{ ttl }}
WHERE 
zone_id = '{{ zone_id }}' --required
AND load_balancer_id = '{{ load_balancer_id }}' --required
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

Update a configured load balancer.

```sql
REPLACE cloudflare.load_balancers.load_balancers
SET 
adaptive_routing = '{{ adaptive_routing }}',
country_pools = '{{ country_pools }}',
default_pools = '{{ default_pools }}',
description = '{{ description }}',
enabled = {{ enabled }},
fallback_pool = '{{ fallback_pool }}',
location_strategy = '{{ location_strategy }}',
name = '{{ name }}',
networks = '{{ networks }}',
pop_pools = '{{ pop_pools }}',
proxied = {{ proxied }},
random_steering = '{{ random_steering }}',
region_pools = '{{ region_pools }}',
rules = '{{ rules }}',
session_affinity = '{{ session_affinity }}',
session_affinity_attributes = '{{ session_affinity_attributes }}',
session_affinity_ttl = {{ session_affinity_ttl }},
steering_policy = '{{ steering_policy }}',
ttl = {{ ttl }}
WHERE 
zone_id = '{{ zone_id }}' --required
AND load_balancer_id = '{{ load_balancer_id }}' --required
AND name = '{{ name }}' --required
AND default_pools = '{{ default_pools }}' --required
AND fallback_pool = '{{ fallback_pool }}' --required
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

Delete a configured load balancer.

```sql
DELETE FROM cloudflare.load_balancers.load_balancers
WHERE zone_id = '{{ zone_id }}' --required
AND load_balancer_id = '{{ load_balancer_id }}' --required
;
```
</TabItem>
</Tabs>
