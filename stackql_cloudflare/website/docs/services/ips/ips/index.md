--- 
title: ips
hide_title: false
hide_table_of_contents: false
keywords:
  - ips
  - ips
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

Creates, updates, deletes, gets or lists an <code>ips</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ips" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ips.ips" /></td></tr>
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

Cloudflare IP Details response

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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A digest of the IP data. Useful for determining if the data has changed. (example: a8e453d9d129a3769407127936edfdb0)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_cidrs" /></td>
    <td><code>array</code></td>
    <td>List of Cloudflare IPv4 CIDR addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6_cidrs" /></td>
    <td><code>array</code></td>
    <td>List of Cloudflare IPv6 CIDR addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="jdcloud_cidrs" /></td>
    <td><code>array</code></td>
    <td>List IPv4 and IPv6 CIDRs, only populated if `?networks=jdcloud` is used.</td>
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
    <td></td>
    <td><a href="#parameter-networks"><code>networks</code></a></td>
    <td>Get IPs used on the Cloudflare/JD Cloud network, see https://www.cloudflare.com/ips for Cloudflare IPs or https://developers.cloudflare.com/china-network/reference/infrastructure/ for JD Cloud IPs.</td>
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
<tr id="parameter-networks">
    <td><CopyableCode code="networks" /></td>
    <td><code>string</code></td>
    <td>Specified as `jdcloud` to list IPs used by JD Cloud data centers.</td>
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

Get IPs used on the Cloudflare/JD Cloud network, see https://www.cloudflare.com/ips for Cloudflare IPs or https://developers.cloudflare.com/china-network/reference/infrastructure/ for JD Cloud IPs.

```sql
SELECT
etag,
ipv4_cidrs,
ipv6_cidrs,
jdcloud_cidrs
FROM cloudflare.ips.ips
WHERE networks = '{{ networks }}'
;
```
</TabItem>
</Tabs>
