--- 
title: certificate_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_packs
  - ssl
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

Creates, updates, deletes, gets or lists a <code>certificate_packs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_packs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ssl.certificate_packs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get Certificate Pack response

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
    <td><CopyableCode code="certificate_authority" /></td>
    <td><code>string</code></td>
    <td>Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities) (google, lets_encrypt, ssl_com) (example: lets_encrypt)</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>Array of certificates in this pack.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudflare_branding" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="dcv_delegation_records" /></td>
    <td><code>array</code></td>
    <td>DCV Delegation records for domain validation.</td>
</tr>
<tr>
    <td><CopyableCode code="hosts" /></td>
    <td><code>array</code></td>
    <td>Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty. (x-stainless-collection-type: set, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="primary_certificate" /></td>
    <td><code>string</code></td>
    <td>Identifier of the primary certificate in a pack. (example: 7e7b8deba8538af625850b7b2530034c)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of certificate pack. (initializing, pending_validation, deleted, pending_issuance, pending_deployment, pending_deletion, pending_expiration, expired, active, initializing_timed_out, validation_timed_out, issuance_timed_out, deployment_timed_out, deletion_timed_out, pending_cleanup, staging_deployment, staging_active, deactivating, inactive, backup_issued, holding_deployment) (example: initializing)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of certificate pack. (mh_custom, managed_hostname, sni_custom, universal, advanced, total_tls, keyless, legacy_custom) (example: universal)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_errors" /></td>
    <td><code>array</code></td>
    <td>Domain validation errors that have been received by the certificate authority (CA).</td>
</tr>
<tr>
    <td><CopyableCode code="validation_method" /></td>
    <td><code>string</code></td>
    <td>Validation Method selected for the order. (txt, http, email) (example: txt)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_records" /></td>
    <td><code>array</code></td>
    <td>Certificates' validation records.</td>
</tr>
<tr>
    <td><CopyableCode code="validity_days" /></td>
    <td><code>integer</code></td>
    <td>Validity Days selected for the order. (14, 30, 90, 365)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Certificate Packs response

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
    <td><CopyableCode code="certificate_authority" /></td>
    <td><code>string</code></td>
    <td>Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities) (google, lets_encrypt, ssl_com) (example: lets_encrypt)</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>Array of certificates in this pack.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudflare_branding" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="dcv_delegation_records" /></td>
    <td><code>array</code></td>
    <td>DCV Delegation records for domain validation.</td>
</tr>
<tr>
    <td><CopyableCode code="hosts" /></td>
    <td><code>array</code></td>
    <td>Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty. (x-stainless-collection-type: set, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="primary_certificate" /></td>
    <td><code>string</code></td>
    <td>Identifier of the primary certificate in a pack. (example: 7e7b8deba8538af625850b7b2530034c)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of certificate pack. (initializing, pending_validation, deleted, pending_issuance, pending_deployment, pending_deletion, pending_expiration, expired, active, initializing_timed_out, validation_timed_out, issuance_timed_out, deployment_timed_out, deletion_timed_out, pending_cleanup, staging_deployment, staging_active, deactivating, inactive, backup_issued, holding_deployment) (example: initializing)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of certificate pack. (mh_custom, managed_hostname, sni_custom, universal, advanced, total_tls, keyless, legacy_custom) (example: universal)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_errors" /></td>
    <td><code>array</code></td>
    <td>Domain validation errors that have been received by the certificate authority (CA).</td>
</tr>
<tr>
    <td><CopyableCode code="validation_method" /></td>
    <td><code>string</code></td>
    <td>Validation Method selected for the order. (txt, http, email) (example: txt)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_records" /></td>
    <td><code>array</code></td>
    <td>Certificates' validation records.</td>
</tr>
<tr>
    <td><CopyableCode code="validity_days" /></td>
    <td><code>integer</code></td>
    <td>Validity Days selected for the order. (14, 30, 90, 365)</td>
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
    <td><a href="#parameter-certificate_pack_id"><code>certificate_pack_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>For a given zone, get a certificate pack.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-deploy"><code>deploy</code></a></td>
    <td>For a given zone, list all active certificate packs.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-hosts"><code>hosts</code></a>, <a href="#parameter-validation_method"><code>validation_method</code></a>, <a href="#parameter-validity_days"><code>validity_days</code></a>, <a href="#parameter-certificate_authority"><code>certificate_authority</code></a></td>
    <td></td>
    <td>For a given zone, order an advanced certificate pack.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificate_pack_id"><code>certificate_pack_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>For a given zone, restart validation or add cloudflare branding for an advanced certificate pack. The former is only a validation operation for a Certificate Pack in a validation_timed_out status.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-certificate_pack_id"><code>certificate_pack_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>For a given zone, delete an advanced certificate pack.</td>
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
<tr id="parameter-certificate_pack_id">
    <td><CopyableCode code="certificate_pack_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-deploy">
    <td><CopyableCode code="deploy" /></td>
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
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

For a given zone, get a certificate pack.

```sql
SELECT
id,
certificate_authority,
certificates,
cloudflare_branding,
dcv_delegation_records,
hosts,
primary_certificate,
status,
type,
validation_errors,
validation_method,
validation_records,
validity_days
FROM cloudflare.ssl.certificate_packs
WHERE certificate_pack_id = '{{ certificate_pack_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

For a given zone, list all active certificate packs.

```sql
SELECT
id,
certificate_authority,
certificates,
cloudflare_branding,
dcv_delegation_records,
hosts,
primary_certificate,
status,
type,
validation_errors,
validation_method,
validation_records,
validity_days
FROM cloudflare.ssl.certificate_packs
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND status = '{{ status }}'
AND deploy = '{{ deploy }}'
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

For a given zone, order an advanced certificate pack.

```sql
INSERT INTO cloudflare.ssl.certificate_packs (
certificate_authority,
cloudflare_branding,
hosts,
type,
validation_method,
validity_days,
zone_id
)
SELECT 
'{{ certificate_authority }}' /* required */,
{{ cloudflare_branding }},
'{{ hosts }}' /* required */,
'{{ type }}' /* required */,
'{{ validation_method }}' /* required */,
{{ validity_days }} /* required */,
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
- name: certificate_packs
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the certificate_packs resource.
    - name: certificate_authority
      value: "{{ certificate_authority }}"
      description: |
        Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)
      valid_values: ['google', 'lets_encrypt', 'ssl_com']
    - name: cloudflare_branding
      value: {{ cloudflare_branding }}
      description: |
        Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.
    - name: hosts
      value:
        - "{{ hosts }}"
      description: |
        Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.
    - name: type
      value: "{{ type }}"
      description: |
        Type of certificate pack.
      valid_values: ['advanced']
    - name: validation_method
      value: "{{ validation_method }}"
      description: |
        Validation Method selected for the order.
      valid_values: ['txt', 'http', 'email']
    - name: validity_days
      value: {{ validity_days }}
      description: |
        Validity Days selected for the order.
      valid_values: ['14', '30', '90', '365']
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

For a given zone, restart validation or add cloudflare branding for an advanced certificate pack. The former is only a validation operation for a Certificate Pack in a validation_timed_out status.

```sql
UPDATE cloudflare.ssl.certificate_packs
SET 
cloudflare_branding = {{ cloudflare_branding }}
WHERE 
certificate_pack_id = '{{ certificate_pack_id }}' --required
AND zone_id = '{{ zone_id }}' --required
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

For a given zone, delete an advanced certificate pack.

```sql
DELETE FROM cloudflare.ssl.certificate_packs
WHERE certificate_pack_id = '{{ certificate_pack_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
