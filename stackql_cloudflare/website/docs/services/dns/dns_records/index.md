--- 
title: dns_records
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_records
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

Creates, updates, deletes, gets or lists a <code>dns_records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dns_records" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.dns_records" /></td></tr>
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

Export DNS Records response

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
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td>You can export your [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this endpoint. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records") for more information.</td>
</tr>
<tr>
    <td><a href="#batch"><CopyableCode code="batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Send a Batch of DNS Record API calls to be executed together. Notes: - Although Cloudflare will execute the batched operations in a single database transaction, Cloudflare's distributed KV store must treat each record change as a single key-value pair. This means that the propagation of changes is not atomic. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/ "Batch DNS records") for more information. - The operations you specify within the /batch request body are always executed in the following order: - Deletes - Patches - Puts - Posts</td>
</tr>
<tr>
    <td><a href="#import"><CopyableCode code="import" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>You can upload your [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this endpoint. It assumes that cURL is called from a location with bind_config.txt (valid BIND config) present. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records") for more information.</td>
</tr>
<tr>
    <td><a href="#scan"><CopyableCode code="scan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Scan for common DNS records on your domain and automatically add them to your zone. Useful if you haven't updated your nameservers yet.</td>
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

You can export your [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this endpoint. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records") for more information.

```sql
SELECT
contents
FROM cloudflare.dns.dns_records
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="batch"
    values={[
        { label: 'batch', value: 'batch' },
        { label: 'import', value: 'import' },
        { label: 'scan', value: 'scan' }
    ]}
>
<TabItem value="batch">

Send a Batch of DNS Record API calls to be executed together. Notes: - Although Cloudflare will execute the batched operations in a single database transaction, Cloudflare's distributed KV store must treat each record change as a single key-value pair. This means that the propagation of changes is not atomic. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/ "Batch DNS records") for more information. - The operations you specify within the /batch request body are always executed in the following order: - Deletes - Patches - Puts - Posts

```sql
EXEC cloudflare.dns.dns_records.batch 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"deletes": "{{ deletes }}", 
"patches": "{{ patches }}", 
"posts": "{{ posts }}", 
"puts": "{{ puts }}"
}'
;
```
</TabItem>
<TabItem value="import">

You can upload your [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this endpoint. It assumes that cURL is called from a location with bind_config.txt (valid BIND config) present. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records") for more information.

```sql
EXEC cloudflare.dns.dns_records.import 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"file": "{{ file }}", 
"proxied": "{{ proxied }}"
}'
;
```
</TabItem>
<TabItem value="scan">

Scan for common DNS records on your domain and automatically add them to your zone. Useful if you haven't updated your nameservers yet.

```sql
EXEC cloudflare.dns.dns_records.scan 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
