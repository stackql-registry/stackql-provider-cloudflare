--- 
title: dns
hide_title: false
hide_table_of_contents: false
keywords:
  - dns
  - email_sending
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
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_sending.dns" /></td></tr>
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

Get sending subdomain DNS records response

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
    <td><a href="#parameter-subdomain_id"><code>subdomain_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Returns the expected DNS records for a sending subdomain.</td>
</tr>
<tr>
    <td><a href="#email_sending_subdomains_fix_sending_subdomain_dns"><CopyableCode code="email_sending_subdomains_fix_sending_subdomain_dns" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-subdomain_id"><code>subdomain_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Idempotently re-applies the sending DNS records (creates missing records, re-applies the email_routing lock on records whose lock has been cleared). Refuses with a 409 if foreign MX, multiple SPF, multiple DMARC, or multiple DKIM records exist at the relevant DNS names — those require manual cleanup.</td>
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
<tr id="parameter-subdomain_id">
    <td><CopyableCode code="subdomain_id" /></td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns the expected DNS records for a sending subdomain.

```sql
SELECT
name,
content,
priority,
ttl,
type
FROM cloudflare.email_sending.dns
WHERE subdomain_id = '{{ subdomain_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="email_sending_subdomains_fix_sending_subdomain_dns"
    values={[
        { label: 'email_sending_subdomains_fix_sending_subdomain_dns', value: 'email_sending_subdomains_fix_sending_subdomain_dns' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="email_sending_subdomains_fix_sending_subdomain_dns">

Idempotently re-applies the sending DNS records (creates missing records, re-applies the email_routing lock on records whose lock has been cleared). Refuses with a 409 if foreign MX, multiple SPF, multiple DMARC, or multiple DKIM records exist at the relevant DNS names — those require manual cleanup.

```sql
INSERT INTO cloudflare.email_sending.dns (
subdomain_id,
zone_id
)
SELECT 
'{{ subdomain_id }}',
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
    - name: subdomain_id
      value: "{{ subdomain_id }}"
      description: Required parameter for the dns resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the dns resource.
`}</CodeBlock>

</TabItem>
</Tabs>
