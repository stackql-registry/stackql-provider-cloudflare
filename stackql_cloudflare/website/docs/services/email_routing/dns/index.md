--- 
title: dns
hide_title: false
hide_table_of_contents: false
keywords:
  - dns
  - email_routing
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

Creates, updates, deletes, gets or lists a <code>dns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dns" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_routing.dns" /></td></tr>
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

Email Routing - DNS settings response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>DNS record name (or @ for the zone apex). (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string</code></td>
    <td>DNS record content. (example: route1.mx.cloudflare.net)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number</code></td>
    <td>Required for MX, SRV and URI records. Unused by other record types. Records with lower priorities are preferred.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>number</code></td>
    <td>Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for 'automatic'. (1)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>DNS record type. (A, AAAA, CNAME, HTTPS, TXT, SRV, LOC, MX, NS, CERT, DNSKEY, DS, NAPTR, SMIMEA, SSHFP, SVCB, TLSA, URI) (example: NS)</td>
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
    <td><a href="#parameter-subdomain"><code>subdomain</code></a></td>
    <td>Show the DNS records needed to configure your Email Routing zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Enable you Email Routing zone. Add and lock the necessary MX and SPF records.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Unlock MX Records previously locked by Email Routing.</td>
</tr>
<tr>
    <td><a href="#email_routing_settings_disable_email_routing_dns"><CopyableCode code="email_routing_settings_disable_email_routing_dns" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Disable your Email Routing zone. Also removes additional MX records previously required for Email Routing to work.</td>
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
<tr id="parameter-subdomain">
    <td><CopyableCode code="subdomain" /></td>
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

Show the DNS records needed to configure your Email Routing zone.

```sql
SELECT
name,
content,
priority,
ttl,
type
FROM cloudflare.email_routing.dns
WHERE zone_id = '{{ zone_id }}' -- required
AND subdomain = '{{ subdomain }}'
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

Enable you Email Routing zone. Add and lock the necessary MX and SPF records.

```sql
INSERT INTO cloudflare.email_routing.dns (
name,
zone_id
)
SELECT 
'{{ name }}',
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
- name: dns
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the dns resource.
    - name: name
      value: "{{ name }}"
      description: |
        Domain of your zone.
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

Unlock MX Records previously locked by Email Routing.

```sql
UPDATE cloudflare.email_routing.dns
SET 
name = '{{ name }}'
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


## `DELETE` examples

<Tabs
    defaultValue="email_routing_settings_disable_email_routing_dns"
    values={[
        { label: 'email_routing_settings_disable_email_routing_dns', value: 'email_routing_settings_disable_email_routing_dns' }
    ]}
>
<TabItem value="email_routing_settings_disable_email_routing_dns">

Disable your Email Routing zone. Also removes additional MX records previously required for Email Routing to work.

```sql
DELETE FROM cloudflare.email_routing.dns
WHERE zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
