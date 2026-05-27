--- 
title: client_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - client_certificates
  - client_certificates
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

Creates, updates, deletes, gets or lists a <code>client_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="client_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.client_certificates.client_certificates" /></td></tr>
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

Client Certificate Details Response

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
    <td><CopyableCode code="common_name" /></td>
    <td><code>string</code></td>
    <td>Common Name of the Client Certificate (example: Cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>string</code></td>
    <td>The Client Certificate PEM (example: -----BEGIN CERTIFICATE-----<br />MIIDmDCCAoC...dhDDE<br />-----END CERTIFICATE-----)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate_authority" /></td>
    <td><code>object</code></td>
    <td>Certificate Authority used to issue the Client Certificate</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country, provided by the CSR (example: US)</td>
</tr>
<tr>
    <td><CopyableCode code="csr" /></td>
    <td><code>string</code></td>
    <td>The Certificate Signing Request (CSR). Must be newline-encoded. (example: -----BEGIN CERTIFICATE REQUEST-----<br />MIICY....<br />-----END CERTIFICATE REQUEST-----)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string</code></td>
    <td>Date that the Client Certificate expires (example: 2033-02-20T23:18:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="fingerprint_sha256" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the Client Certificate (example: 256c24690243359fb8cf139a125bd05ebf1d968b71e4caf330718e9f5c8a89ea)</td>
</tr>
<tr>
    <td><CopyableCode code="issued_on" /></td>
    <td><code>string</code></td>
    <td>Date that the Client Certificate was issued by the Certificate Authority (example: 2023-02-23T23:18:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location, provided by the CSR (example: Somewhere)</td>
</tr>
<tr>
    <td><CopyableCode code="organization" /></td>
    <td><code>string</code></td>
    <td>Organization, provided by the CSR (example: Organization)</td>
</tr>
<tr>
    <td><CopyableCode code="organizational_unit" /></td>
    <td><code>string</code></td>
    <td>Organizational Unit, provided by the CSR (example: Organizational Unit)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The serial number on the created Client Certificate. (example: 3bb94ff144ac567b9f75ad664b6c55f8d5e48182)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the Client Certificate.. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="ski" /></td>
    <td><code>string</code></td>
    <td>Subject Key Identifier (example: 8e375af1389a069a0f921f8cc8e1eb12d784b949)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State, provided by the CSR (example: CA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Client Certificates may be active or revoked, and the pending_reactivation or pending_revocation represent in-progress asynchronous transitions (active, pending_reactivation, pending_revocation, revoked) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="validity_days" /></td>
    <td><code>integer</code></td>
    <td>The number of days the Client Certificate will be valid after the issued_on date</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Client Certificates Response

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
    <td><CopyableCode code="common_name" /></td>
    <td><code>string</code></td>
    <td>Common Name of the Client Certificate (example: Cloudflare)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>string</code></td>
    <td>The Client Certificate PEM (example: -----BEGIN CERTIFICATE-----<br />MIIDmDCCAoC...dhDDE<br />-----END CERTIFICATE-----)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate_authority" /></td>
    <td><code>object</code></td>
    <td>Certificate Authority used to issue the Client Certificate</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country, provided by the CSR (example: US)</td>
</tr>
<tr>
    <td><CopyableCode code="csr" /></td>
    <td><code>string</code></td>
    <td>The Certificate Signing Request (CSR). Must be newline-encoded. (example: -----BEGIN CERTIFICATE REQUEST-----<br />MIICY....<br />-----END CERTIFICATE REQUEST-----)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string</code></td>
    <td>Date that the Client Certificate expires (example: 2033-02-20T23:18:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="fingerprint_sha256" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the Client Certificate (example: 256c24690243359fb8cf139a125bd05ebf1d968b71e4caf330718e9f5c8a89ea)</td>
</tr>
<tr>
    <td><CopyableCode code="issued_on" /></td>
    <td><code>string</code></td>
    <td>Date that the Client Certificate was issued by the Certificate Authority (example: 2023-02-23T23:18:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location, provided by the CSR (example: Somewhere)</td>
</tr>
<tr>
    <td><CopyableCode code="organization" /></td>
    <td><code>string</code></td>
    <td>Organization, provided by the CSR (example: Organization)</td>
</tr>
<tr>
    <td><CopyableCode code="organizational_unit" /></td>
    <td><code>string</code></td>
    <td>Organizational Unit, provided by the CSR (example: Organizational Unit)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The serial number on the created Client Certificate. (example: 3bb94ff144ac567b9f75ad664b6c55f8d5e48182)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the Client Certificate.. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="ski" /></td>
    <td><code>string</code></td>
    <td>Subject Key Identifier (example: 8e375af1389a069a0f921f8cc8e1eb12d784b949)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State, provided by the CSR (example: CA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Client Certificates may be active or revoked, and the pending_reactivation or pending_revocation represent in-progress asynchronous transitions (active, pending_reactivation, pending_revocation, revoked) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="validity_days" /></td>
    <td><code>integer</code></td>
    <td>The number of days the Client Certificate will be valid after the issued_on date</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-client_certificate_id"><code>client_certificate_id</code></a></td>
    <td></td>
    <td>Get Details for a single mTLS API Shield Client Certificate</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a></td>
    <td>List all of your Zone's API Shield mTLS Client Certificates by Status and/or using Pagination</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-csr"><code>csr</code></a>, <a href="#parameter-validity_days"><code>validity_days</code></a></td>
    <td></td>
    <td>Create a new API Shield mTLS Client Certificate</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-client_certificate_id"><code>client_certificate_id</code></a></td>
    <td></td>
    <td>If a API Shield mTLS Client Certificate is in a pending_revocation state, you may reactivate it with this endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-client_certificate_id"><code>client_certificate_id</code></a></td>
    <td></td>
    <td>Set a API Shield mTLS Client Certificate to pending_revocation status for processing to revoked status.</td>
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
<tr id="parameter-client_certificate_id">
    <td><CopyableCode code="client_certificate_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
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

Get Details for a single mTLS API Shield Client Certificate

```sql
SELECT
id,
common_name,
certificate,
certificate_authority,
country,
csr,
expires_on,
fingerprint_sha256,
issued_on,
location,
organization,
organizational_unit,
serial_number,
signature,
ski,
state,
status,
validity_days
FROM cloudflare.client_certificates.client_certificates
WHERE zone_id = '{{ zone_id }}' -- required
AND client_certificate_id = '{{ client_certificate_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all of your Zone's API Shield mTLS Client Certificates by Status and/or using Pagination

```sql
SELECT
id,
common_name,
certificate,
certificate_authority,
country,
csr,
expires_on,
fingerprint_sha256,
issued_on,
location,
organization,
organizational_unit,
serial_number,
signature,
ski,
state,
status,
validity_days
FROM cloudflare.client_certificates.client_certificates
WHERE zone_id = '{{ zone_id }}' -- required
AND status = '{{ status }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND limit = '{{ limit }}'
AND offset = '{{ offset }}'
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

Create a new API Shield mTLS Client Certificate

```sql
INSERT INTO cloudflare.client_certificates.client_certificates (
csr,
validity_days,
zone_id
)
SELECT 
'{{ csr }}' /* required */,
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
- name: client_certificates
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the client_certificates resource.
    - name: csr
      value: "{{ csr }}"
      description: |
        The Certificate Signing Request (CSR). Must be newline-encoded.
    - name: validity_days
      value: {{ validity_days }}
      description: |
        The number of days the Client Certificate will be valid after the issued_on date
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

If a API Shield mTLS Client Certificate is in a pending_revocation state, you may reactivate it with this endpoint.

```sql
UPDATE cloudflare.client_certificates.client_certificates
SET 
reactivate = {{ reactivate }}
WHERE 
zone_id = '{{ zone_id }}' --required
AND client_certificate_id = '{{ client_certificate_id }}' --required
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

Set a API Shield mTLS Client Certificate to pending_revocation status for processing to revoked status.

```sql
DELETE FROM cloudflare.client_certificates.client_certificates
WHERE zone_id = '{{ zone_id }}' --required
AND client_certificate_id = '{{ client_certificate_id }}' --required
;
```
</TabItem>
</Tabs>
