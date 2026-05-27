--- 
title: dns_firewall
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_firewall
  - dns_firewall
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

Creates, updates, deletes, gets or lists a <code>dns_firewall</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dns_firewall" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns_firewall.dns_firewall" /></td></tr>
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

DNS Firewall Cluster Details response

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
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>DNS Firewall cluster name (example: My Awesome DNS Firewall cluster)</td>
</tr>
<tr>
    <td><CopyableCode code="attack_mitigation" /></td>
    <td><code>object</code></td>
    <td>Attack mitigation settings</td>
</tr>
<tr>
    <td><CopyableCode code="deprecate_any_requests" /></td>
    <td><code>boolean</code></td>
    <td>Whether to refuse to answer queries for the ANY type</td>
</tr>
<tr>
    <td><CopyableCode code="dns_firewall_ips" /></td>
    <td><code>array</code></td>
    <td> (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="ecs_fallback" /></td>
    <td><code>boolean</code></td>
    <td>Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent</td>
</tr>
<tr>
    <td><CopyableCode code="maximum_cache_ttl" /></td>
    <td><code>number</code></td>
    <td>By default, Cloudflare attempts to cache responses for as long as indicated by the TTL received from upstream nameservers. This setting sets an upper bound on this duration. For caching purposes, higher TTLs will be decreased to the maximum value defined by this setting. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers.</td>
</tr>
<tr>
    <td><CopyableCode code="minimum_cache_ttl" /></td>
    <td><code>number</code></td>
    <td>By default, Cloudflare attempts to cache responses for as long as indicated by the TTL received from upstream nameservers. This setting sets a lower bound on this duration. For caching purposes, lower TTLs will be increased to the minimum value defined by this setting. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers. Note that, even with this setting, there is no guarantee that a response will be cached for at least the specified duration. Cached responses may be removed earlier for capacity or other operational reasons.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last modification of DNS Firewall cluster (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="negative_cache_ttl" /></td>
    <td><code>number</code></td>
    <td>This setting controls how long DNS Firewall should cache negative responses (e.g., NXDOMAIN) from the upstream servers. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers.</td>
</tr>
<tr>
    <td><CopyableCode code="ratelimit" /></td>
    <td><code>number</code></td>
    <td>Ratelimit in queries per second per datacenter (applies to DNS queries sent to the upstream nameservers configured on the cluster)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>number</code></td>
    <td>Number of retries for fetching DNS responses from upstream nameservers (not counting the initial attempt)</td>
</tr>
<tr>
    <td><CopyableCode code="upstream_ips" /></td>
    <td><code>array</code></td>
    <td> (x-stainless-collection-type: set)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List DNS Firewall Clusters response

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
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>DNS Firewall cluster name (example: My Awesome DNS Firewall cluster)</td>
</tr>
<tr>
    <td><CopyableCode code="attack_mitigation" /></td>
    <td><code>object</code></td>
    <td>Attack mitigation settings</td>
</tr>
<tr>
    <td><CopyableCode code="deprecate_any_requests" /></td>
    <td><code>boolean</code></td>
    <td>Whether to refuse to answer queries for the ANY type</td>
</tr>
<tr>
    <td><CopyableCode code="dns_firewall_ips" /></td>
    <td><code>array</code></td>
    <td> (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="ecs_fallback" /></td>
    <td><code>boolean</code></td>
    <td>Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent</td>
</tr>
<tr>
    <td><CopyableCode code="maximum_cache_ttl" /></td>
    <td><code>number</code></td>
    <td>By default, Cloudflare attempts to cache responses for as long as indicated by the TTL received from upstream nameservers. This setting sets an upper bound on this duration. For caching purposes, higher TTLs will be decreased to the maximum value defined by this setting. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers.</td>
</tr>
<tr>
    <td><CopyableCode code="minimum_cache_ttl" /></td>
    <td><code>number</code></td>
    <td>By default, Cloudflare attempts to cache responses for as long as indicated by the TTL received from upstream nameservers. This setting sets a lower bound on this duration. For caching purposes, lower TTLs will be increased to the minimum value defined by this setting. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers. Note that, even with this setting, there is no guarantee that a response will be cached for at least the specified duration. Cached responses may be removed earlier for capacity or other operational reasons.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last modification of DNS Firewall cluster (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="negative_cache_ttl" /></td>
    <td><code>number</code></td>
    <td>This setting controls how long DNS Firewall should cache negative responses (e.g., NXDOMAIN) from the upstream servers. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers.</td>
</tr>
<tr>
    <td><CopyableCode code="ratelimit" /></td>
    <td><code>number</code></td>
    <td>Ratelimit in queries per second per datacenter (applies to DNS queries sent to the upstream nameservers configured on the cluster)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>number</code></td>
    <td>Number of retries for fetching DNS responses from upstream nameservers (not counting the initial attempt)</td>
</tr>
<tr>
    <td><CopyableCode code="upstream_ips" /></td>
    <td><code>array</code></td>
    <td> (x-stainless-collection-type: set)</td>
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
    <td><a href="#parameter-dns_firewall_id"><code>dns_firewall_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Show a single DNS Firewall cluster for an account</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List DNS Firewall clusters for an account</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Create a DNS Firewall cluster</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-dns_firewall_id"><code>dns_firewall_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Modify the configuration of a DNS Firewall cluster</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dns_firewall_id"><code>dns_firewall_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a DNS Firewall cluster</td>
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
<tr id="parameter-dns_firewall_id">
    <td><CopyableCode code="dns_firewall_id" /></td>
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

Show a single DNS Firewall cluster for an account

```sql
SELECT
id,
name,
attack_mitigation,
deprecate_any_requests,
dns_firewall_ips,
ecs_fallback,
maximum_cache_ttl,
minimum_cache_ttl,
modified_on,
negative_cache_ttl,
ratelimit,
retries,
upstream_ips
FROM cloudflare.dns_firewall.dns_firewall
WHERE dns_firewall_id = '{{ dns_firewall_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List DNS Firewall clusters for an account

```sql
SELECT
id,
name,
attack_mitigation,
deprecate_any_requests,
dns_firewall_ips,
ecs_fallback,
maximum_cache_ttl,
minimum_cache_ttl,
modified_on,
negative_cache_ttl,
ratelimit,
retries,
upstream_ips
FROM cloudflare.dns_firewall.dns_firewall
WHERE account_id = '{{ account_id }}' -- required
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

Create a DNS Firewall cluster

```sql
INSERT INTO cloudflare.dns_firewall.dns_firewall (
attack_mitigation,
deprecate_any_requests,
ecs_fallback,
maximum_cache_ttl,
minimum_cache_ttl,
name,
negative_cache_ttl,
ratelimit,
retries,
upstream_ips,
account_id
)
SELECT 
'{{ attack_mitigation }}',
{{ deprecate_any_requests }},
{{ ecs_fallback }},
{{ maximum_cache_ttl }},
{{ minimum_cache_ttl }},
'{{ name }}',
{{ negative_cache_ttl }},
{{ ratelimit }},
{{ retries }},
'{{ upstream_ips }}',
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
- name: dns_firewall
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the dns_firewall resource.
    - name: attack_mitigation
      description: |
        Attack mitigation settings
      value:
        enabled: {{ enabled }}
        only_when_upstream_unhealthy: {{ only_when_upstream_unhealthy }}
    - name: deprecate_any_requests
      value: {{ deprecate_any_requests }}
      description: |
        Whether to refuse to answer queries for the ANY type
    - name: ecs_fallback
      value: {{ ecs_fallback }}
      description: |
        Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent
    - name: maximum_cache_ttl
      value: {{ maximum_cache_ttl }}
      description: |
        By default, Cloudflare attempts to cache responses for as long as indicated by the TTL received from upstream nameservers. This setting sets an upper bound on this duration. For caching purposes, higher TTLs will be decreased to the maximum value defined by this setting. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers.
      default: 900
    - name: minimum_cache_ttl
      value: {{ minimum_cache_ttl }}
      description: |
        By default, Cloudflare attempts to cache responses for as long as indicated by the TTL received from upstream nameservers. This setting sets a lower bound on this duration. For caching purposes, lower TTLs will be increased to the minimum value defined by this setting. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers. Note that, even with this setting, there is no guarantee that a response will be cached for at least the specified duration. Cached responses may be removed earlier for capacity or other operational reasons.
      default: 60
    - name: name
      value: "{{ name }}"
      description: |
        DNS Firewall cluster name
    - name: negative_cache_ttl
      value: {{ negative_cache_ttl }}
      description: |
        This setting controls how long DNS Firewall should cache negative responses (e.g., NXDOMAIN) from the upstream servers. This setting does not affect the TTL value in the DNS response Cloudflare returns to clients. Cloudflare will always forward the TTL value received from upstream nameservers.
    - name: ratelimit
      value: {{ ratelimit }}
      description: |
        Ratelimit in queries per second per datacenter (applies to DNS queries sent to the upstream nameservers configured on the cluster)
    - name: retries
      value: {{ retries }}
      description: |
        Number of retries for fetching DNS responses from upstream nameservers (not counting the initial attempt)
      default: 2
    - name: upstream_ips
      value:
        - "{{ upstream_ips }}"
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

Modify the configuration of a DNS Firewall cluster

```sql
UPDATE cloudflare.dns_firewall.dns_firewall
SET 
attack_mitigation = '{{ attack_mitigation }}',
deprecate_any_requests = {{ deprecate_any_requests }},
ecs_fallback = {{ ecs_fallback }},
maximum_cache_ttl = {{ maximum_cache_ttl }},
minimum_cache_ttl = {{ minimum_cache_ttl }},
name = '{{ name }}',
negative_cache_ttl = {{ negative_cache_ttl }},
ratelimit = {{ ratelimit }},
retries = {{ retries }},
upstream_ips = '{{ upstream_ips }}'
WHERE 
dns_firewall_id = '{{ dns_firewall_id }}' --required
AND account_id = '{{ account_id }}' --required
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

Delete a DNS Firewall cluster

```sql
DELETE FROM cloudflare.dns_firewall.dns_firewall
WHERE dns_firewall_id = '{{ dns_firewall_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
