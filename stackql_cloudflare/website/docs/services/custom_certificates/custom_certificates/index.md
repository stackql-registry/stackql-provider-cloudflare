--- 
title: custom_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_certificates
  - custom_certificates
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

Creates, updates, deletes, gets or lists a <code>custom_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.custom_certificates.custom_certificates" /></td></tr>
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

SSL Configuration Details response

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
    <td><CopyableCode code="custom_csr_id" /></td>
    <td><code>string</code></td>
    <td>The identifier for the Custom CSR that was used. (example: 7b163417-1d2b-4c84-a38a-2fb7a0cd7752)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="bundle_method" /></td>
    <td><code>string</code></td>
    <td>A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. (ubiquitous, optimal, force) (default: ubiquitous, example: ubiquitous)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate from the authority expires. (example: 2016-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="geo_restrictions" /></td>
    <td><code>object</code></td>
    <td>Specify the region where your private key can be held locally for optimal TLS performance. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Options allow distribution to only to U.S. data centers, only to E.U. data centers, or only to highest security data centers. Default distribution is to all Cloudflare datacenters, for optimal performance.</td>
</tr>
<tr>
    <td><CopyableCode code="hosts" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The certificate authority that issued the certificate. (example: GlobalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="keyless_server" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate was last modified. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_restrictions" /></td>
    <td><code>string</code></td>
    <td>The policy restrictions returned by the API. This field is returned in responses when a policy has been set. The API accepts the "policy" field in requests but returns this field as "policy_restrictions" in responses. Specifies the region(s) where your private key can be held locally for optimal TLS performance. Format is a boolean expression, for example: "(country: US) or (region: EU)" (example: (country: US) or (region: EU))</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number</code></td>
    <td>The order/priority in which the certificate will be used in a request. The higher priority will break ties across overlapping 'legacy_custom' certificates, but 'legacy_custom' certificates will always supercede 'sni_custom' certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the certificate. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the zone's custom SSL. (active, expired, deleted, pending, initializing) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="uploaded_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate was uploaded to Cloudflare. (example: 2014-01-01T05:20:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List SSL Configurations response

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
    <td><CopyableCode code="custom_csr_id" /></td>
    <td><code>string</code></td>
    <td>The identifier for the Custom CSR that was used. (example: 7b163417-1d2b-4c84-a38a-2fb7a0cd7752)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="bundle_method" /></td>
    <td><code>string</code></td>
    <td>A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. (ubiquitous, optimal, force) (default: ubiquitous, example: ubiquitous)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate from the authority expires. (example: 2016-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="geo_restrictions" /></td>
    <td><code>object</code></td>
    <td>Specify the region where your private key can be held locally for optimal TLS performance. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Options allow distribution to only to U.S. data centers, only to E.U. data centers, or only to highest security data centers. Default distribution is to all Cloudflare datacenters, for optimal performance.</td>
</tr>
<tr>
    <td><CopyableCode code="hosts" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The certificate authority that issued the certificate. (example: GlobalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="keyless_server" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate was last modified. (example: 2014-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_restrictions" /></td>
    <td><code>string</code></td>
    <td>The policy restrictions returned by the API. This field is returned in responses when a policy has been set. The API accepts the "policy" field in requests but returns this field as "policy_restrictions" in responses. Specifies the region(s) where your private key can be held locally for optimal TLS performance. Format is a boolean expression, for example: "(country: US) or (region: EU)" (example: (country: US) or (region: EU))</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number</code></td>
    <td>The order/priority in which the certificate will be used in a request. The higher priority will break ties across overlapping 'legacy_custom' certificates, but 'legacy_custom' certificates will always supercede 'sni_custom' certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the certificate. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the zone's custom SSL. (active, expired, deleted, pending, initializing) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="uploaded_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate was uploaded to Cloudflare. (example: 2014-01-01T05:20:00Z)</td>
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
    <td><a href="#parameter-custom_certificate_id"><code>custom_certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific custom SSL certificate, including certificate metadata, bundle method, geographic restrictions, and associated keyless server configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-match"><code>match</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td>List, search, and filter all of your custom SSL certificates. The higher priority will break ties across overlapping 'legacy_custom' certificates, but 'legacy_custom' certificates will always supercede 'sni_custom' certificates.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-certificate"><code>certificate</code></a>, <a href="#parameter-private_key"><code>private_key</code></a></td>
    <td></td>
    <td>Upload a new SSL certificate for a zone.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-custom_certificate_id"><code>custom_certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Upload a new private key and/or PEM/CRT for the SSL certificate. Note: PATCHing a configuration for sni_custom certificates will result in a new resource id being returned, and the previous one being deleted.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_certificate_id"><code>custom_certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Remove a SSL certificate from a zone.</td>
</tr>
<tr>
    <td><a href="#update_prioritize"><CopyableCode code="update_prioritize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-certificates"><code>certificates</code></a></td>
    <td></td>
    <td>If a zone has multiple SSL certificates, you can set the order in which they should be used during a request. The higher priority will break ties across overlapping 'legacy_custom' certificates.</td>
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
<tr id="parameter-custom_certificate_id">
    <td><CopyableCode code="custom_certificate_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-match">
    <td><CopyableCode code="match" /></td>
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

Retrieves details for a specific custom SSL certificate, including certificate metadata, bundle method, geographic restrictions, and associated keyless server configuration.

```sql
SELECT
id,
custom_csr_id,
zone_id,
bundle_method,
expires_on,
geo_restrictions,
hosts,
issuer,
keyless_server,
modified_on,
policy_restrictions,
priority,
signature,
status,
uploaded_on
FROM cloudflare.custom_certificates.custom_certificates
WHERE custom_certificate_id = '{{ custom_certificate_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List, search, and filter all of your custom SSL certificates. The higher priority will break ties across overlapping 'legacy_custom' certificates, but 'legacy_custom' certificates will always supercede 'sni_custom' certificates.

```sql
SELECT
id,
custom_csr_id,
zone_id,
bundle_method,
expires_on,
geo_restrictions,
hosts,
issuer,
keyless_server,
modified_on,
policy_restrictions,
priority,
signature,
status,
uploaded_on
FROM cloudflare.custom_certificates.custom_certificates
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND match = '{{ match }}'
AND status = '{{ status }}'
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

Upload a new SSL certificate for a zone.

```sql
INSERT INTO cloudflare.custom_certificates.custom_certificates (
bundle_method,
certificate,
custom_csr_id,
deploy,
geo_restrictions,
policy,
private_key,
type,
zone_id
)
SELECT 
'{{ bundle_method }}',
'{{ certificate }}' /* required */,
'{{ custom_csr_id }}',
'{{ deploy }}',
'{{ geo_restrictions }}',
'{{ policy }}',
'{{ private_key }}' /* required */,
'{{ type }}',
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
- name: custom_certificates
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the custom_certificates resource.
    - name: bundle_method
      value: "{{ bundle_method }}"
      description: |
        A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
      valid_values: ['ubiquitous', 'optimal', 'force']
      default: ubiquitous
    - name: certificate
      value: "{{ certificate }}"
      description: |
        The zone's SSL certificate or certificate and the intermediate(s).
    - name: custom_csr_id
      value: "{{ custom_csr_id }}"
      description: |
        The identifier for the Custom CSR that was used.
    - name: deploy
      value: "{{ deploy }}"
      description: |
        The environment to deploy the certificate to, defaults to production
      valid_values: ['staging', 'production']
      default: production
    - name: geo_restrictions
      description: |
        Specify the region where your private key can be held locally for optimal TLS performance. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Options allow distribution to only to U.S. data centers, only to E.U. data centers, or only to highest security data centers. Default distribution is to all Cloudflare datacenters, for optimal performance.
      value:
        label: "{{ label }}"
    - name: policy
      value: "{{ policy }}"
      description: |
        Specify the policy that determines the region where your private key will be held locally. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Any combination of countries, specified by their two letter country code (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) can be chosen, such as 'country: IN', as well as 'region: EU' which refers to the EU region. If there are too few data centers satisfying the policy, it will be rejected. Note: The API accepts this field as either "policy" or "policy_restrictions" in requests. Responses return this field as "policy_restrictions".
    - name: private_key
      value: "{{ private_key }}"
      description: |
        The zone's private key.
    - name: type
      value: "{{ type }}"
      description: |
        The type 'legacy_custom' enables support for legacy clients which do not include SNI in the TLS handshake.
      valid_values: ['legacy_custom', 'sni_custom']
      default: legacy_custom
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

Upload a new private key and/or PEM/CRT for the SSL certificate. Note: PATCHing a configuration for sni_custom certificates will result in a new resource id being returned, and the previous one being deleted.

```sql
UPDATE cloudflare.custom_certificates.custom_certificates
SET 
bundle_method = '{{ bundle_method }}',
certificate = '{{ certificate }}',
custom_csr_id = '{{ custom_csr_id }}',
deploy = '{{ deploy }}',
geo_restrictions = '{{ geo_restrictions }}',
policy = '{{ policy }}',
private_key = '{{ private_key }}'
WHERE 
custom_certificate_id = '{{ custom_certificate_id }}' --required
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

Remove a SSL certificate from a zone.

```sql
DELETE FROM cloudflare.custom_certificates.custom_certificates
WHERE custom_certificate_id = '{{ custom_certificate_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_prioritize"
    values={[
        { label: 'update_prioritize', value: 'update_prioritize' }
    ]}
>
<TabItem value="update_prioritize">

If a zone has multiple SSL certificates, you can set the order in which they should be used during a request. The higher priority will break ties across overlapping 'legacy_custom' certificates.

```sql
EXEC cloudflare.custom_certificates.custom_certificates.update_prioritize 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"certificates": "{{ certificates }}"
}'
;
```
</TabItem>
</Tabs>
