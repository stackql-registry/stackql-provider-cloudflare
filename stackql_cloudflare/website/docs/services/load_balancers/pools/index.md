--- 
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.load_balancers.pools" /></td></tr>
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

Pool Details response.

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
    <td> (example: 17b5962d775c646f3f9725cbc7a53df4)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed. (example: primary-dc-1)</td>
</tr>
<tr>
    <td><CopyableCode code="check_regions" /></td>
    <td><code>array</code></td>
    <td>A list of regions from which to run health checks. Null means every Cloudflare data center.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the pool. (default: , example: Primary data center - Provider XYZ)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>This field shows up only if the pool is disabled. This field is set with the time the pool was disabled at.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>number</code></td>
    <td>The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="load_shedding" /></td>
    <td><code>object</code></td>
    <td>Configures load shedding policies and percentages for the pool. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>number</code></td>
    <td>The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="minimum_origins" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="monitor" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="monitor_group" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor Group to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>List of networks where Load Balancer or Pool is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notification_email" /></td>
    <td><code>string</code></td>
    <td>This field is now deprecated. It has been moved to Cloudflare's Centralized Notification service https://developers.cloudflare.com/fundamentals/notifications/. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list. (default: , example: someone@example.com,sometwo@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="notification_filter" /></td>
    <td><code>object</code></td>
    <td>Filter pool and origin health notifications by resource type or health status. Use null to reset. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_steering" /></td>
    <td><code>object</code></td>
    <td>Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. (x-stainless-collection-type: set)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List Pools response.

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
    <td> (example: 17b5962d775c646f3f9725cbc7a53df4)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed. (example: primary-dc-1)</td>
</tr>
<tr>
    <td><CopyableCode code="check_regions" /></td>
    <td><code>array</code></td>
    <td>A list of regions from which to run health checks. Null means every Cloudflare data center.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the pool. (default: , example: Primary data center - Provider XYZ)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>This field shows up only if the pool is disabled. This field is set with the time the pool was disabled at.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>number</code></td>
    <td>The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="load_shedding" /></td>
    <td><code>object</code></td>
    <td>Configures load shedding policies and percentages for the pool. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>number</code></td>
    <td>The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="minimum_origins" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="monitor" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="monitor_group" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor Group to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>List of networks where Load Balancer or Pool is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notification_email" /></td>
    <td><code>string</code></td>
    <td>This field is now deprecated. It has been moved to Cloudflare's Centralized Notification service https://developers.cloudflare.com/fundamentals/notifications/. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list. (default: , example: someone@example.com,sometwo@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="notification_filter" /></td>
    <td><code>object</code></td>
    <td>Filter pool and origin health notifications by resource type or health status. Use null to reset. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_steering" /></td>
    <td><code>object</code></td>
    <td>Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. (x-stainless-collection-type: set)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_user">

Pool Details response.

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
    <td> (example: 17b5962d775c646f3f9725cbc7a53df4)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed. (example: primary-dc-1)</td>
</tr>
<tr>
    <td><CopyableCode code="check_regions" /></td>
    <td><code>array</code></td>
    <td>A list of regions from which to run health checks. Null means every Cloudflare data center.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the pool. (default: , example: Primary data center - Provider XYZ)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>This field shows up only if the pool is disabled. This field is set with the time the pool was disabled at.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>number</code></td>
    <td>The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="load_shedding" /></td>
    <td><code>object</code></td>
    <td>Configures load shedding policies and percentages for the pool. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>number</code></td>
    <td>The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="minimum_origins" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="monitor" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="monitor_group" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor Group to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>List of networks where Load Balancer or Pool is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notification_email" /></td>
    <td><code>string</code></td>
    <td>This field is now deprecated. It has been moved to Cloudflare's Centralized Notification service https://developers.cloudflare.com/fundamentals/notifications/. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list. (default: , example: someone@example.com,sometwo@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="notification_filter" /></td>
    <td><code>object</code></td>
    <td>Filter pool and origin health notifications by resource type or health status. Use null to reset. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_steering" /></td>
    <td><code>object</code></td>
    <td>Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. (x-stainless-collection-type: set)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_user">

List Pools response.

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
    <td> (example: 17b5962d775c646f3f9725cbc7a53df4)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed. (example: primary-dc-1)</td>
</tr>
<tr>
    <td><CopyableCode code="check_regions" /></td>
    <td><code>array</code></td>
    <td>A list of regions from which to run health checks. Null means every Cloudflare data center.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the pool. (default: , example: Primary data center - Provider XYZ)</td>
</tr>
<tr>
    <td><CopyableCode code="disabled_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>This field shows up only if the pool is disabled. This field is set with the time the pool was disabled at.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).</td>
</tr>
<tr>
    <td><CopyableCode code="latitude" /></td>
    <td><code>number</code></td>
    <td>The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="load_shedding" /></td>
    <td><code>object</code></td>
    <td>Configures load shedding policies and percentages for the pool. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="longitude" /></td>
    <td><code>number</code></td>
    <td>The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.</td>
</tr>
<tr>
    <td><CopyableCode code="minimum_origins" /></td>
    <td><code>integer</code></td>
    <td>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="monitor" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="monitor_group" /></td>
    <td><code>string</code></td>
    <td>The ID of the Monitor Group to use for checking the health of origins within this pool.</td>
</tr>
<tr>
    <td><CopyableCode code="networks" /></td>
    <td><code>array</code></td>
    <td>List of networks where Load Balancer or Pool is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notification_email" /></td>
    <td><code>string</code></td>
    <td>This field is now deprecated. It has been moved to Cloudflare's Centralized Notification service https://developers.cloudflare.com/fundamentals/notifications/. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list. (default: , example: someone@example.com,sometwo@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="notification_filter" /></td>
    <td><code>object</code></td>
    <td>Filter pool and origin health notifications by resource type or health status. Use null to reset. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_steering" /></td>
    <td><code>object</code></td>
    <td>Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="origins" /></td>
    <td><code>array</code></td>
    <td>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. (x-stainless-collection-type: set)</td>
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
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetch a single configured pool.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-monitor"><code>monitor</code></a></td>
    <td>List configured pools.</td>
</tr>
<tr>
    <td><a href="#get_by_user"><CopyableCode code="get_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a></td>
    <td></td>
    <td>Fetch a single configured pool.</td>
</tr>
<tr>
    <td><a href="#list_by_user"><CopyableCode code="list_by_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-monitor"><code>monitor</code></a></td>
    <td>List configured pools.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-origins"><code>origins</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a new pool.</td>
</tr>
<tr>
    <td><a href="#load_balancer_pools_create_pool"><CopyableCode code="load_balancer_pools_create_pool" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-origins"><code>origins</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a new pool.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Apply changes to an existing pool, overwriting the supplied properties.</td>
</tr>
<tr>
    <td><a href="#account_load_balancer_pools_patch_pools"><CopyableCode code="account_load_balancer_pools_patch_pools" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Apply changes to a number of existing pools, overwriting the supplied properties. Pools are ordered by ascending `name`. Returns the list of affected pools. Supports the standard pagination query parameters, either `limit`/`offset` or `per_page`/`page`.</td>
</tr>
<tr>
    <td><a href="#load_balancer_pools_patch_pool"><CopyableCode code="load_balancer_pools_patch_pool" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a></td>
    <td></td>
    <td>Apply changes to an existing pool, overwriting the supplied properties.</td>
</tr>
<tr>
    <td><a href="#load_balancer_pools_patch_pools"><CopyableCode code="load_balancer_pools_patch_pools" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Apply changes to a number of existing pools, overwriting the supplied properties. Pools are ordered by ascending `name`. Returns the list of affected pools. Supports the standard pagination query parameters, either `limit`/`offset` or `per_page`/`page`.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-origins"><code>origins</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Modify a configured pool.</td>
</tr>
<tr>
    <td><a href="#load_balancer_pools_update_pool"><CopyableCode code="load_balancer_pools_update_pool" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-origins"><code>origins</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Modify a configured pool.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured pool.</td>
</tr>
<tr>
    <td><a href="#load_balancer_pools_delete_pool"><CopyableCode code="load_balancer_pools_delete_pool" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pool_id"><code>pool_id</code></a></td>
    <td></td>
    <td>Delete a configured pool.</td>
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
<tr id="parameter-monitor">
    <td><CopyableCode code="monitor" /></td>
    <td><code>string</code></td>
    <td></td>
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

Fetch a single configured pool.

```sql
SELECT
id,
name,
check_regions,
created_on,
description,
disabled_at,
enabled,
latitude,
load_shedding,
longitude,
minimum_origins,
modified_on,
monitor,
monitor_group,
networks,
notification_email,
notification_filter,
origin_steering,
origins
FROM cloudflare.load_balancers.pools
WHERE pool_id = '{{ pool_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

List configured pools.

```sql
SELECT
id,
name,
check_regions,
created_on,
description,
disabled_at,
enabled,
latitude,
load_shedding,
longitude,
minimum_origins,
modified_on,
monitor,
monitor_group,
networks,
notification_email,
notification_filter,
origin_steering,
origins
FROM cloudflare.load_balancers.pools
WHERE account_id = '{{ account_id }}' -- required
AND monitor = '{{ monitor }}'
;
```
</TabItem>
<TabItem value="get_by_user">

Fetch a single configured pool.

```sql
SELECT
id,
name,
check_regions,
created_on,
description,
disabled_at,
enabled,
latitude,
load_shedding,
longitude,
minimum_origins,
modified_on,
monitor,
monitor_group,
networks,
notification_email,
notification_filter,
origin_steering,
origins
FROM cloudflare.load_balancers.pools
WHERE pool_id = '{{ pool_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_user">

List configured pools.

```sql
SELECT
id,
name,
check_regions,
created_on,
description,
disabled_at,
enabled,
latitude,
load_shedding,
longitude,
minimum_origins,
modified_on,
monitor,
monitor_group,
networks,
notification_email,
notification_filter,
origin_steering,
origins
FROM cloudflare.load_balancers.pools
WHERE monitor = '{{ monitor }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'load_balancer_pools_create_pool', value: 'load_balancer_pools_create_pool' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a new pool.

```sql
INSERT INTO cloudflare.load_balancers.pools (
description,
enabled,
latitude,
load_shedding,
longitude,
minimum_origins,
monitor,
monitor_group,
name,
notification_email,
notification_filter,
origin_steering,
origins,
account_id
)
SELECT 
'{{ description }}',
{{ enabled }},
{{ latitude }},
'{{ load_shedding }}',
{{ longitude }},
{{ minimum_origins }},
'{{ monitor }}',
'{{ monitor_group }}',
'{{ name }}' /* required */,
'{{ notification_email }}',
'{{ notification_filter }}',
'{{ origin_steering }}',
'{{ origins }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="load_balancer_pools_create_pool">

Create a new pool.

```sql
INSERT INTO cloudflare.load_balancers.pools (
check_regions,
description,
enabled,
latitude,
load_shedding,
longitude,
minimum_origins,
monitor,
monitor_group,
name,
networks,
notification_email,
notification_filter,
origin_steering,
origins
)
SELECT 
'{{ check_regions }}',
'{{ description }}',
{{ enabled }},
{{ latitude }},
'{{ load_shedding }}',
{{ longitude }},
{{ minimum_origins }},
'{{ monitor }}',
'{{ monitor_group }}',
'{{ name }}' /* required */,
'{{ networks }}',
'{{ notification_email }}',
'{{ notification_filter }}',
'{{ origin_steering }}',
'{{ origins }}' /* required */
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
- name: pools
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the pools resource.
    - name: description
      value: "{{ description }}"
      description: |
        A human-readable description of the pool.
      default: 
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether to enable (the default) or disable this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any).
      default: true
    - name: latitude
      value: {{ latitude }}
      description: |
        The latitude of the data center containing the origins used in this pool in decimal degrees. If this is set, longitude must also be set.
    - name: load_shedding
      description: |
        Configures load shedding policies and percentages for the pool.
      value:
        default_percent: {{ default_percent }}
        default_policy: "{{ default_policy }}"
        session_percent: {{ session_percent }}
        session_policy: "{{ session_policy }}"
    - name: longitude
      value: {{ longitude }}
      description: |
        The longitude of the data center containing the origins used in this pool in decimal degrees. If this is set, latitude must also be set.
    - name: minimum_origins
      value: {{ minimum_origins }}
      description: |
        The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and will failover to the next available pool.
      default: 1
    - name: monitor
      value: "{{ monitor }}"
      description: |
        The ID of the Monitor to use for checking the health of origins within this pool.
    - name: monitor_group
      value: "{{ monitor_group }}"
      description: |
        The ID of the Monitor Group to use for checking the health of origins within this pool.
    - name: name
      value: "{{ name }}"
      description: |
        A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed.
    - name: notification_email
      value: "{{ notification_email }}"
      description: |
        This field is now deprecated. It has been moved to Cloudflare's Centralized Notification service https://developers.cloudflare.com/fundamentals/notifications/. The email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.
      default: 
    - name: notification_filter
      description: |
        Filter pool and origin health notifications by resource type or health status. Use null to reset.
      value:
        origin:
          disable: {{ disable }}
          healthy: {{ healthy }}
        pool:
          disable: {{ disable }}
          healthy: {{ healthy }}
    - name: origin_steering
      description: |
        Configures origin steering for the pool. Controls how origins are selected for new sessions and traffic without session affinity.
      value:
        policy: "{{ policy }}"
    - name: origins
      description: |
        The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy.
      value:
        - address: "{{ address }}"
          disabled_at: "{{ disabled_at }}"
          enabled: {{ enabled }}
          flatten_cname: {{ flatten_cname }}
          header:
            Host:
              - "{{ Host }}"
          name: "{{ name }}"
          port: {{ port }}
          virtual_network_id: "{{ virtual_network_id }}"
          weight: {{ weight }}
    - name: check_regions
      value:
        - "{{ check_regions }}"
      description: |
        A list of regions from which to run health checks. Null means every Cloudflare data center.
    - name: networks
      value:
        - "{{ networks }}"
      description: |
        List of networks where Load Balancer or Pool is enabled.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'account_load_balancer_pools_patch_pools', value: 'account_load_balancer_pools_patch_pools' },
        { label: 'load_balancer_pools_patch_pool', value: 'load_balancer_pools_patch_pool' },
        { label: 'load_balancer_pools_patch_pools', value: 'load_balancer_pools_patch_pools' }
    ]}
>
<TabItem value="edit">

Apply changes to an existing pool, overwriting the supplied properties.

```sql
UPDATE cloudflare.load_balancers.pools
SET 
check_regions = '{{ check_regions }}',
description = '{{ description }}',
enabled = {{ enabled }},
latitude = {{ latitude }},
load_shedding = '{{ load_shedding }}',
longitude = {{ longitude }},
minimum_origins = {{ minimum_origins }},
monitor = '{{ monitor }}',
monitor_group = '{{ monitor_group }}',
name = '{{ name }}',
notification_email = '{{ notification_email }}',
notification_filter = '{{ notification_filter }}',
origin_steering = '{{ origin_steering }}',
origins = '{{ origins }}'
WHERE 
pool_id = '{{ pool_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="account_load_balancer_pools_patch_pools">

Apply changes to a number of existing pools, overwriting the supplied properties. Pools are ordered by ascending `name`. Returns the list of affected pools. Supports the standard pagination query parameters, either `limit`/`offset` or `per_page`/`page`.

```sql
UPDATE cloudflare.load_balancers.pools
SET 
notification_email = '{{ notification_email }}'
WHERE 
account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
<TabItem value="load_balancer_pools_patch_pool">

Apply changes to an existing pool, overwriting the supplied properties.

```sql
UPDATE cloudflare.load_balancers.pools
SET 
check_regions = '{{ check_regions }}',
description = '{{ description }}',
enabled = {{ enabled }},
latitude = {{ latitude }},
load_shedding = '{{ load_shedding }}',
longitude = {{ longitude }},
minimum_origins = {{ minimum_origins }},
monitor = '{{ monitor }}',
monitor_group = '{{ monitor_group }}',
name = '{{ name }}',
notification_email = '{{ notification_email }}',
notification_filter = '{{ notification_filter }}',
origin_steering = '{{ origin_steering }}',
origins = '{{ origins }}'
WHERE 
pool_id = '{{ pool_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="load_balancer_pools_patch_pools">

Apply changes to a number of existing pools, overwriting the supplied properties. Pools are ordered by ascending `name`. Returns the list of affected pools. Supports the standard pagination query parameters, either `limit`/`offset` or `per_page`/`page`.

```sql
UPDATE cloudflare.load_balancers.pools
SET 
notification_email = '{{ notification_email }}'
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'load_balancer_pools_update_pool', value: 'load_balancer_pools_update_pool' }
    ]}
>
<TabItem value="update">

Modify a configured pool.

```sql
REPLACE cloudflare.load_balancers.pools
SET 
check_regions = '{{ check_regions }}',
description = '{{ description }}',
enabled = {{ enabled }},
latitude = {{ latitude }},
load_shedding = '{{ load_shedding }}',
longitude = {{ longitude }},
minimum_origins = {{ minimum_origins }},
monitor = '{{ monitor }}',
monitor_group = '{{ monitor_group }}',
name = '{{ name }}',
notification_email = '{{ notification_email }}',
notification_filter = '{{ notification_filter }}',
origin_steering = '{{ origin_steering }}',
origins = '{{ origins }}'
WHERE 
pool_id = '{{ pool_id }}' --required
AND account_id = '{{ account_id }}' --required
AND origins = '{{ origins }}' --required
AND name = '{{ name }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="load_balancer_pools_update_pool">

Modify a configured pool.

```sql
REPLACE cloudflare.load_balancers.pools
SET 
check_regions = '{{ check_regions }}',
description = '{{ description }}',
enabled = {{ enabled }},
latitude = {{ latitude }},
load_shedding = '{{ load_shedding }}',
longitude = {{ longitude }},
minimum_origins = {{ minimum_origins }},
monitor = '{{ monitor }}',
monitor_group = '{{ monitor_group }}',
name = '{{ name }}',
networks = '{{ networks }}',
notification_email = '{{ notification_email }}',
notification_filter = '{{ notification_filter }}',
origin_steering = '{{ origin_steering }}',
origins = '{{ origins }}'
WHERE 
pool_id = '{{ pool_id }}' --required
AND origins = '{{ origins }}' --required
AND name = '{{ name }}' --required
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
        { label: 'load_balancer_pools_delete_pool', value: 'load_balancer_pools_delete_pool' }
    ]}
>
<TabItem value="delete">

Delete a configured pool.

```sql
DELETE FROM cloudflare.load_balancers.pools
WHERE pool_id = '{{ pool_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="load_balancer_pools_delete_pool">

Delete a configured pool.

```sql
DELETE FROM cloudflare.load_balancers.pools
WHERE pool_id = '{{ pool_id }}' --required
;
```
</TabItem>
</Tabs>
