--- 
title: zones_dns_records
hide_title: false
hide_table_of_contents: false
keywords:
  - zones_dns_records
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

Creates, updates, deletes, gets or lists a <code>zones_dns_records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zones_dns_records" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.dns.zones_dns_records" /></td></tr>
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

List DNS Records response

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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-name.exact"><code>name.exact</code></a>, <a href="#parameter-name.contains"><code>name.contains</code></a>, <a href="#parameter-name.startswith"><code>name.startswith</code></a>, <a href="#parameter-name.endswith"><code>name.endswith</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-content"><code>content</code></a>, <a href="#parameter-content.exact"><code>content.exact</code></a>, <a href="#parameter-content.contains"><code>content.contains</code></a>, <a href="#parameter-content.startswith"><code>content.startswith</code></a>, <a href="#parameter-content.endswith"><code>content.endswith</code></a>, <a href="#parameter-proxied"><code>proxied</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-comment"><code>comment</code></a>, <a href="#parameter-comment.present"><code>comment.present</code></a>, <a href="#parameter-comment.absent"><code>comment.absent</code></a>, <a href="#parameter-comment.exact"><code>comment.exact</code></a>, <a href="#parameter-comment.contains"><code>comment.contains</code></a>, <a href="#parameter-comment.startswith"><code>comment.startswith</code></a>, <a href="#parameter-comment.endswith"><code>comment.endswith</code></a>, <a href="#parameter-tag"><code>tag</code></a>, <a href="#parameter-tag.present"><code>tag.present</code></a>, <a href="#parameter-tag.absent"><code>tag.absent</code></a>, <a href="#parameter-tag.exact"><code>tag.exact</code></a>, <a href="#parameter-tag.contains"><code>tag.contains</code></a>, <a href="#parameter-tag.startswith"><code>tag.startswith</code></a>, <a href="#parameter-tag.endswith"><code>tag.endswith</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-tag_match"><code>tag_match</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a></td>
    <td>List, search, sort, and filter a zones' DNS records.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-ttl"><code>ttl</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Create a new DNS record for a zone. Notes: - A/AAAA records cannot exist on the same name as CNAME records. - NS records cannot exist on the same name as any other record type. - Domain names are always represented in Punycode, even if Unicode characters were used when creating the record.</td>
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
<tr id="parameter-comment">
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment.absent">
    <td><CopyableCode code="comment.absent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment.contains">
    <td><CopyableCode code="comment.contains" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment.endswith">
    <td><CopyableCode code="comment.endswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment.exact">
    <td><CopyableCode code="comment.exact" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment.present">
    <td><CopyableCode code="comment.present" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-comment.startswith">
    <td><CopyableCode code="comment.startswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-content">
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-content.contains">
    <td><CopyableCode code="content.contains" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-content.endswith">
    <td><CopyableCode code="content.endswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-content.exact">
    <td><CopyableCode code="content.exact" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-content.startswith">
    <td><CopyableCode code="content.startswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-match">
    <td><CopyableCode code="match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.contains">
    <td><CopyableCode code="name.contains" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.endswith">
    <td><CopyableCode code="name.endswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.exact">
    <td><CopyableCode code="name.exact" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name.startswith">
    <td><CopyableCode code="name.startswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
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
<tr id="parameter-proxied">
    <td><CopyableCode code="proxied" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag">
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag.absent">
    <td><CopyableCode code="tag.absent" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag.contains">
    <td><CopyableCode code="tag.contains" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag.endswith">
    <td><CopyableCode code="tag.endswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag.exact">
    <td><CopyableCode code="tag.exact" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag.present">
    <td><CopyableCode code="tag.present" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag.startswith">
    <td><CopyableCode code="tag.startswith" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tag_match">
    <td><CopyableCode code="tag_match" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td></td>
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

List, search, sort, and filter a zones' DNS records.

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
FROM cloudflare.dns.zones_dns_records
WHERE zone_id = '{{ zone_id }}' -- required
AND name = '{{ name }}'
AND name.exact = '{{ name.exact }}'
AND name.contains = '{{ name.contains }}'
AND name.startswith = '{{ name.startswith }}'
AND name.endswith = '{{ name.endswith }}'
AND type = '{{ type }}'
AND content = '{{ content }}'
AND content.exact = '{{ content.exact }}'
AND content.contains = '{{ content.contains }}'
AND content.startswith = '{{ content.startswith }}'
AND content.endswith = '{{ content.endswith }}'
AND proxied = '{{ proxied }}'
AND match = '{{ match }}'
AND comment = '{{ comment }}'
AND comment.present = '{{ comment.present }}'
AND comment.absent = '{{ comment.absent }}'
AND comment.exact = '{{ comment.exact }}'
AND comment.contains = '{{ comment.contains }}'
AND comment.startswith = '{{ comment.startswith }}'
AND comment.endswith = '{{ comment.endswith }}'
AND tag = '{{ tag }}'
AND tag.present = '{{ tag.present }}'
AND tag.absent = '{{ tag.absent }}'
AND tag.exact = '{{ tag.exact }}'
AND tag.contains = '{{ tag.contains }}'
AND tag.startswith = '{{ tag.startswith }}'
AND tag.endswith = '{{ tag.endswith }}'
AND search = '{{ search }}'
AND tag_match = '{{ tag_match }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
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

Create a new DNS record for a zone. Notes: - A/AAAA records cannot exist on the same name as CNAME records. - NS records cannot exist on the same name as any other record type. - Domain names are always represented in Punycode, even if Unicode characters were used when creating the record.

```sql
INSERT INTO cloudflare.dns.zones_dns_records (
comment,
name,
proxied,
settings,
tags,
ttl,
content,
private_routing,
type,
priority,
data,
zone_id
)
SELECT 
'{{ comment }}',
'{{ name }}' /* required */,
{{ proxied }},
'{{ settings }}',
'{{ tags }}',
{{ ttl }} /* required */,
'{{ content }}',
{{ private_routing }},
'{{ type }}' /* required */,
{{ priority }},
'{{ data }}',
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
- name: zones_dns_records
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the zones_dns_records resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        Comments or notes about the DNS record. This field has no effect on DNS responses.
    - name: name
      value: "{{ name }}"
      description: |
        Complete DNS record name, including the zone name, in Punycode.
    - name: proxied
      value: {{ proxied }}
      description: |
        Whether the record is receiving the performance and security benefits of Cloudflare.
      default: false
    - name: settings
      description: |
        Settings for the DNS record.
      value:
        ipv4_only: {{ ipv4_only }}
        ipv6_only: {{ ipv6_only }}
    - name: tags
      value:
        - "{{ tags }}"
      description: |
        Custom tags for the DNS record. This field has no effect on DNS responses.
      default: 
    - name: ttl
      value: {{ ttl }}
      description: |
        Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the minimum reduced to 30 for Enterprise zones.
      valid_values: ['1']
      default: 1
    - name: content
      value: "{{ content }}"
      description: |
        A valid IPv4 address.
    - name: private_routing
      value: {{ private_routing }}
      description: |
        Enables private network routing to the origin.
      default: false
    - name: type
      value: "{{ type }}"
      description: |
        Record type.
      valid_values: ['A']
    - name: priority
      value: {{ priority }}
      description: |
        Required for MX and URI records; ignored for other record types (but may still be returned by the API). Records with lower priorities are preferred. This field is to be deprecated in favor of the priority field within the data map.
    - name: data
      description: |
        Components of a CAA record.
      value:
        flags: {{ flags }}
        tag: "{{ tag }}"
        value: "{{ value }}"
`}</CodeBlock>

</TabItem>
</Tabs>
