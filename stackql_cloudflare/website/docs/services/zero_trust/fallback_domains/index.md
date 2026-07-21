--- 
title: fallback_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - fallback_domains
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>fallback_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fallback_domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.fallback_domains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_policy"
    values={[
        { label: 'list_by_policy', value: 'list_by_policy' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_policy">

Get the Local Domain Fallback list for a device settings profile response.

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the fallback domain, displayed in the client UI. (example: Domain bypass for local development)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_server" /></td>
    <td><code>array</code></td>
    <td>A list of IP addresses to handle domain resolution.</td>
</tr>
<tr>
    <td><CopyableCode code="suffix" /></td>
    <td><code>string</code></td>
    <td>The domain suffix to match when resolving locally. (example: example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

Get your Local Domain Fallback list response.

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the fallback domain, displayed in the client UI. (example: Domain bypass for local development)</td>
</tr>
<tr>
    <td><CopyableCode code="dns_server" /></td>
    <td><code>array</code></td>
    <td>A list of IP addresses to handle domain resolution.</td>
</tr>
<tr>
    <td><CopyableCode code="suffix" /></td>
    <td><code>string</code></td>
    <td>The domain suffix to match when resolving locally. (example: example.com)</td>
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
    <td><a href="#list_by_policy"><CopyableCode code="list_by_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the list of domains to bypass Gateway DNS resolution from a specified device settings profile. These domains will use the specified local DNS resolver instead.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead.</td>
</tr>
<tr>
    <td><a href="#set_by_policy"><CopyableCode code="set_by_policy" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Sets the list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead. This will only apply to the specified device settings profile.</td>
</tr>
<tr>
    <td><a href="#set"><CopyableCode code="set" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Sets the list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_policy"
    values={[
        { label: 'list_by_policy', value: 'list_by_policy' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_policy">

Fetches the list of domains to bypass Gateway DNS resolution from a specified device settings profile. These domains will use the specified local DNS resolver instead.

```sql
SELECT
description,
dns_server,
suffix
FROM cloudflare.zero_trust.fallback_domains
WHERE policy_id = '{{ policy_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Fetches a list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead.

```sql
SELECT
description,
dns_server,
suffix
FROM cloudflare.zero_trust.fallback_domains
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="set_by_policy"
    values={[
        { label: 'set_by_policy', value: 'set_by_policy' },
        { label: 'set', value: 'set' }
    ]}
>
<TabItem value="set_by_policy">

Sets the list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead. This will only apply to the specified device settings profile.

```sql
REPLACE cloudflare.zero_trust.fallback_domains
SET 
-- No updatable properties
WHERE 
policy_id = '{{ policy_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
<TabItem value="set">

Sets the list of domains to bypass Gateway DNS resolution. These domains will use the specified local DNS resolver instead.

```sql
REPLACE cloudflare.zero_trust.fallback_domains
SET 
-- No updatable properties
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
</Tabs>
