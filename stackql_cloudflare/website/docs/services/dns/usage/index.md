--- 
title: usage
hide_title: false
hide_table_of_contents: false
keywords:
  - usage
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

Creates, updates, deletes, gets or lists a <code>usage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="usage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.usage" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

Get DNS Record Usage response

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
    <td><CopyableCode code="internal_record_quota" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of DNS records allowed across all internal zones in the account. Only present if internal DNS is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="internal_record_usage" /></td>
    <td><code>integer</code></td>
    <td>Current number of DNS records across all internal zones in the account. Only present if internal DNS is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="record_quota" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of DNS records allowed across all public zones in the account. Null if using zone-level quota.</td>
</tr>
<tr>
    <td><CopyableCode code="record_usage" /></td>
    <td><code>integer</code></td>
    <td>Current number of DNS records across all public zones in the account.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

Get DNS Record Usage response

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
    <td><CopyableCode code="internal_record_quota" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of DNS records allowed across all internal zones in the account. Only present if internal DNS is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="internal_record_usage" /></td>
    <td><code>integer</code></td>
    <td>Current number of DNS records across all internal zones in the account. Only present if internal DNS is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="record_quota" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of DNS records allowed across all public zones in the account. Null if using zone-level quota.</td>
</tr>
<tr>
    <td><CopyableCode code="record_usage" /></td>
    <td><code>integer</code></td>
    <td>Current number of DNS records across all public zones in the account.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get the current DNS record usage and quota for an account or zone. May include internal DNS usage and quota.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Get the current DNS record usage and quota for an account or zone. May include internal DNS usage and quota.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

Get the current DNS record usage and quota for an account or zone. May include internal DNS usage and quota.

```sql
SELECT
internal_record_quota,
internal_record_usage,
record_quota,
record_usage
FROM cloudflare.dns.usage
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Get the current DNS record usage and quota for an account or zone. May include internal DNS usage and quota.

```sql
SELECT
internal_record_quota,
internal_record_usage,
record_quota,
record_usage
FROM cloudflare.dns.usage
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>
