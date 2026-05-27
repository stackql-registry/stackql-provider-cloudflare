--- 
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
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

Creates, updates, deletes, gets or lists a <code>records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="records" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.records" /></td></tr>
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

DNS Record Details response

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
    <td>Complete DNS record name, including the zone name, in Punycode. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comments or notes about the DNS record. This field has no effect on DNS responses. (example: Domain verification record)</td>
</tr>
<tr>
    <td><CopyableCode code="comment_modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the record comment was last modified. Omitted if there is no comment. (example: 2024-01-01T05:20:00.12345Z, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string (ipv4)</code></td>
    <td>A valid IPv4 address. (example: 198.51.100.4)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the record was created. (example: 2014-01-01T05:20:00.12345Z, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>Components of a CAA record.</td>
</tr>
<tr>
    <td><CopyableCode code="meta" /></td>
    <td><code>object</code></td>
    <td>Extra Cloudflare-specific information about the record. (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the record was last modified. (example: 2014-01-01T05:20:00.12345Z, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number</code></td>
    <td>Required for MX and URI records; ignored for other record types (but may still be returned by the API). Records with lower priorities are preferred. This field is to be deprecated in favor of the priority field within the data map.</td>
</tr>
<tr>
    <td><CopyableCode code="private_routing" /></td>
    <td><code>boolean</code></td>
    <td>Enables private network routing to the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="proxiable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the record can be proxied by Cloudflare or not. (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="proxied" /></td>
    <td><code>boolean</code></td>
    <td>Whether the record is receiving the performance and security benefits of Cloudflare.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>Settings for the DNS record.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Custom tags for the DNS record. This field has no effect on DNS responses. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="tags_modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the record tags were last modified. Omitted if there are no tags. (example: 2025-01-01T05:20:00.12345Z, x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>number</code></td>
    <td>Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the minimum reduced to 30 for Enterprise zones. (1)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Record type. (A) (example: A)</td>
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
    <td><a href="#parameter-dns_record_id"><code>dns_record_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-dns_record_id"><code>dns_record_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-ttl"><code>ttl</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Update an existing DNS record. Notes: - A/AAAA records cannot exist on the same name as CNAME records. - NS records cannot exist on the same name as any other record type. - Domain names are always represented in Punycode, even if Unicode characters were used when creating the record.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-dns_record_id"><code>dns_record_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-ttl"><code>ttl</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Overwrite an existing DNS record. Notes: - A/AAAA records cannot exist on the same name as CNAME records. - NS records cannot exist on the same name as any other record type. - Domain names are always represented in Punycode, even if Unicode characters were used when creating the record.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-dns_record_id"><code>dns_record_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#scan_trigger"><CopyableCode code="scan_trigger" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Initiates an asynchronous scan for common DNS records on your domain. Note that this **does not** automatically add records to your zone. The scan runs in the background, and results can be reviewed later using the `/scan/review` endpoints. Useful if you haven't updated your nameservers yet.</td>
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
<tr id="parameter-dns_record_id">
    <td><CopyableCode code="dns_record_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

DNS Record Details response

```sql
SELECT
id,
name,
comment,
comment_modified_on,
content,
created_on,
data,
meta,
modified_on,
priority,
private_routing,
proxiable,
proxied,
settings,
tags,
tags_modified_on,
ttl,
type
FROM cloudflare.dns.records
WHERE dns_record_id = '{{ dns_record_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
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

Update an existing DNS record. Notes: - A/AAAA records cannot exist on the same name as CNAME records. - NS records cannot exist on the same name as any other record type. - Domain names are always represented in Punycode, even if Unicode characters were used when creating the record.

```sql
UPDATE cloudflare.dns.records
SET 
comment = '{{ comment }}',
name = '{{ name }}',
proxied = {{ proxied }},
settings = '{{ settings }}',
tags = '{{ tags }}',
ttl = {{ ttl }},
content = '{{ content }}',
private_routing = {{ private_routing }},
type = '{{ type }}',
priority = {{ priority }},
data = '{{ data }}'
WHERE 
dns_record_id = '{{ dns_record_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND ttl = '{{ ttl }}' --required
AND type = '{{ type }}' --required
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

Overwrite an existing DNS record. Notes: - A/AAAA records cannot exist on the same name as CNAME records. - NS records cannot exist on the same name as any other record type. - Domain names are always represented in Punycode, even if Unicode characters were used when creating the record.

```sql
REPLACE cloudflare.dns.records
SET 
comment = '{{ comment }}',
name = '{{ name }}',
proxied = {{ proxied }},
settings = '{{ settings }}',
tags = '{{ tags }}',
ttl = {{ ttl }},
content = '{{ content }}',
private_routing = {{ private_routing }},
type = '{{ type }}',
priority = {{ priority }},
data = '{{ data }}'
WHERE 
dns_record_id = '{{ dns_record_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND ttl = '{{ ttl }}' --required
AND type = '{{ type }}' --required
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

No description available.

```sql
DELETE FROM cloudflare.dns.records
WHERE dns_record_id = '{{ dns_record_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="scan_trigger"
    values={[
        { label: 'scan_trigger', value: 'scan_trigger' }
    ]}
>
<TabItem value="scan_trigger">

Initiates an asynchronous scan for common DNS records on your domain. Note that this **does not** automatically add records to your zone. The scan runs in the background, and results can be reviewed later using the `/scan/review` endpoints. Useful if you haven't updated your nameservers yet.

```sql
EXEC cloudflare.dns.records.scan_trigger 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
