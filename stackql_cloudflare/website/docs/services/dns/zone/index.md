--- 
title: zone
hide_title: false
hide_table_of_contents: false
keywords:
  - zone
  - dns
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

Creates, updates, deletes, gets or lists a <code>zone</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zone" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.zone" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Show DNS Settings response

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
    <td><CopyableCode code="flatten_all_cnames" /></td>
    <td><code>boolean</code></td>
    <td>Whether to flatten all CNAME records in the zone. Note that, due to DNS limitations, a CNAME record at the zone apex will always be flattened.</td>
</tr>
<tr>
    <td><CopyableCode code="foundation_dns" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable Foundation DNS Advanced Nameservers on the zone.</td>
</tr>
<tr>
    <td><CopyableCode code="internal_dns" /></td>
    <td><code>object</code></td>
    <td>Settings for this internal zone.</td>
</tr>
<tr>
    <td><CopyableCode code="multi_provider" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable multi-provider DNS, which causes Cloudflare to activate the zone even when non-Cloudflare NS records exist, and to respect NS records at the zone apex during outbound zone transfers.</td>
</tr>
<tr>
    <td><CopyableCode code="nameservers" /></td>
    <td><code>object</code></td>
    <td>Settings determining the nameservers through which the zone should be available.</td>
</tr>
<tr>
    <td><CopyableCode code="ns_ttl" /></td>
    <td><code>number</code></td>
    <td>The time to live (TTL) of the zone's nameserver (NS) records.</td>
</tr>
<tr>
    <td><CopyableCode code="secondary_overrides" /></td>
    <td><code>boolean</code></td>
    <td>Allows a Secondary DNS zone to use (proxied) override records and CNAME flattening at the zone apex.</td>
</tr>
<tr>
    <td><CopyableCode code="soa" /></td>
    <td><code>object</code></td>
    <td>Components of the zone's SOA record.</td>
</tr>
<tr>
    <td><CopyableCode code="zone_mode" /></td>
    <td><code>string</code></td>
    <td>Whether the zone mode is a regular or CDN/DNS only zone. (standard, cdn_only, dns_only) (example: dns_only)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Show DNS settings for a zone</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Update DNS settings for a zone</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Show DNS settings for a zone

```sql
SELECT
flatten_all_cnames,
foundation_dns,
internal_dns,
multi_provider,
nameservers,
ns_ttl,
secondary_overrides,
soa,
zone_mode
FROM cloudflare.dns.zone
WHERE zone_id = '{{ zone_id }}' -- required
;
```
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

Update DNS settings for a zone

```sql
UPDATE cloudflare.dns.zone
SET 
flatten_all_cnames = {{ flatten_all_cnames }},
foundation_dns = {{ foundation_dns }},
internal_dns = '{{ internal_dns }}',
multi_provider = {{ multi_provider }},
ns_ttl = {{ ns_ttl }},
secondary_overrides = {{ secondary_overrides }},
soa = '{{ soa }}',
zone_mode = '{{ zone_mode }}',
nameservers = '{{ nameservers }}'
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
