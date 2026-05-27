--- 
title: scan_review
hide_title: false
hide_table_of_contents: false
keywords:
  - scan_review
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

Creates, updates, deletes, gets or lists a <code>scan_review</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scan_review" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.scan_review" /></td></tr>
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

List of discovered DNS records

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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Retrieves the list of DNS records discovered up to this point by the asynchronous scan. These records are temporary until explicitly accepted or rejected via `POST /scan/review`. Additional records may be discovered by the scan later.</td>
</tr>
<tr>
    <td><a href="#scan_review"><CopyableCode code="scan_review" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Accept or reject DNS records found by the DNS records scan. Accepted records will be permanently added to the zone, while rejected records will be permanently deleted.</td>
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

Retrieves the list of DNS records discovered up to this point by the asynchronous scan. These records are temporary until explicitly accepted or rejected via `POST /scan/review`. Additional records may be discovered by the scan later.

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
FROM cloudflare.dns.scan_review
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="scan_review"
    values={[
        { label: 'scan_review', value: 'scan_review' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="scan_review">

Accept or reject DNS records found by the DNS records scan. Accepted records will be permanently added to the zone, while rejected records will be permanently deleted.

```sql
INSERT INTO cloudflare.dns.scan_review (
accepts,
rejects,
zone_id
)
SELECT 
'{{ accepts }}',
'{{ rejects }}',
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
- name: scan_review
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the scan_review resource.
    - name: accepts
      value:
        - comment: "{{ comment }}"
          name: "{{ name }}"
          proxied: {{ proxied }}
          settings:
            ipv4_only: {{ ipv4_only }}
            ipv6_only: {{ ipv6_only }}
          tags: "{{ tags }}"
          ttl: {{ ttl }}
          content: "{{ content }}"
          private_routing: {{ private_routing }}
          type: "{{ type }}"
          priority: {{ priority }}
          data:
            flags: {{ flags }}
            tag: "{{ tag }}"
            value: "{{ value }}"
    - name: rejects
      value:
        - id: "{{ id }}"
`}</CodeBlock>

</TabItem>
</Tabs>
