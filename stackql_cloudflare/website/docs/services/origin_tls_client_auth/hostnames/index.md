--- 
title: hostnames
hide_title: false
hide_table_of_contents: false
keywords:
  - hostnames
  - origin_tls_client_auth
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

Creates, updates, deletes, gets or lists a <code>hostnames</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="hostnames" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.origin_tls_client_auth.hostnames" /></td></tr>
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

Get the Hostname Status for Client Authentication response

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
    <td><CopyableCode code="cert_id" /></td>
    <td><code>string</code></td>
    <td>Identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="cert_status" /></td>
    <td><code>string</code></td>
    <td>Status of the certificate or the association. (initializing, pending_deployment, pending_deletion, active, deleted, deployment_timed_out, deletion_timed_out) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="cert_updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was updated. (example: 2100-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="cert_uploaded_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was uploaded. (example: 2019-10-28T18:11:23.37411Z)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>string</code></td>
    <td>The hostname certificate. (example: -----BEGIN CERTIFICATE-----<br />MIIDtTCCAp2gAwIBAgIJAMHAwfXZ5/PWMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV<br />BAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRlMSEwHwYDVQQKExhJbnRlcm5ldCBX<br />aWRnaXRzIFB0eSBMdGQwHhcNMTYwODI0MTY0MzAxWhcNMTYxMTIyMTY0MzAxWjBF<br />MQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50<br />ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB<br />CgKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmGdtcGbg/1<br />CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKnabIRuGvB<br />KwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpidtnKX/a+5<br />0GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+pyFxIXjbEI<br />dZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pEewooaeO2<br />izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABo4GnMIGkMB0GA1UdDgQWBBT/LbE4<br />9rWf288N6sJA5BRb6FJIGDB1BgNVHSMEbjBsgBT/LbE49rWf288N6sJA5BRb6FJI<br />GKFJpEcwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgTClNvbWUtU3RhdGUxITAfBgNV<br />BAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZIIJAMHAwfXZ5/PWMAwGA1UdEwQF<br />MAMBAf8wDQYJKoZIhvcNAQELBQADggEBAHHFwl0tH0quUYZYO0dZYt4R7SJ0pCm2<br />2satiyzHl4OnXcHDpekAo7/a09c6Lz6AU83cKy/+x3/djYHXWba7HpEu0dR3ugQP<br />Mlr4zrhd9xKZ0KZKiYmtJH+ak4OM4L3FbT0owUZPyjLSlhMtJVcoRp5CJsjAMBUG<br />SvD8RX+T01wzox/Qb+lnnNnOlaWpqu8eoOenybxKp1a9ULzIVvN/LAcc+14vioFq<br />2swRWtmocBAs8QR9n4uvbpiYvS8eYueDCWMM4fvFfBhaDZ3N9IbtySh3SpFdQDhw<br />YbjM2rxXiyLGxB4Bol7QTv4zHif7Zt89FReT/NBy4rzaskDJY5L6xmY=<br />-----END CERTIFICATE-----<br />)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was created. (example: 2100-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether hostname-level authenticated origin pulls is enabled. A null value voids the association.</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the certificate expires. (example: 2100-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname on the origin for which the client certificate uploaded will be used. (example: app.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The certificate authority that issued the certificate. (example: GlobalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="serial_number" /></td>
    <td><code>string</code></td>
    <td>The serial number on the uploaded certificate. (example: 6743787633689793699141714808227354901)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the certificate. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the certificate or the association. (initializing, pending_deployment, pending_deletion, active, deleted, deployment_timed_out, deletion_timed_out) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was updated. (example: 2100-01-01T05:20:00Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Hostname Associations response

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
    <td><CopyableCode code="cert_id" /></td>
    <td><code>string</code></td>
    <td>Certificate identifier tag. (example: 2458ce5a-0c35-4c7f-82c7-8e9487d3ff60)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was created. (example: 2100-01-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether hostname-level authenticated origin pulls is enabled. A null value voids the association.</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname on the origin for which the client certificate uploaded will be used. (example: app.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the certificate or the association. (initializing, pending_deployment, pending_deletion, active, deleted, deployment_timed_out, deletion_timed_out) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the certificate was updated. (example: 2100-01-01T05:20:00Z)</td>
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
    <td><a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Retrieves the client certificate authentication status for a specific hostname, showing whether authenticated origin pulls are enabled.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td>List certificate ID - hostname associations for the given zone. Shows which hostnames are associated to which certificates for authenticated origin pulls.</td>
</tr>
<tr>
    <td><a href="#per_hostname_authenticated_origin_pull_enable_or_disable_a_hostname_for_client_authentication"><CopyableCode code="per_hostname_authenticated_origin_pull_enable_or_disable_a_hostname_for_client_authentication" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-config"><code>config</code></a></td>
    <td></td>
    <td>Associate a hostname to a certificate and enable, disable or invalidate the association. If disabled, client certificate will not be sent to the hostname even if activated at the zone level. 100 maximum associations on a single certificate are allowed. Note: Use a null value for parameter *enabled* to invalidate the association.</td>
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
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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

Retrieves the client certificate authentication status for a specific hostname, showing whether authenticated origin pulls are enabled.

```sql
SELECT
cert_id,
cert_status,
cert_updated_at,
cert_uploaded_on,
certificate,
created_at,
enabled,
expires_on,
hostname,
issuer,
serial_number,
signature,
status,
updated_at
FROM cloudflare.origin_tls_client_auth.hostnames
WHERE hostname = '{{ hostname }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List certificate ID - hostname associations for the given zone. Shows which hostnames are associated to which certificates for authenticated origin pulls.

```sql
SELECT
cert_id,
created_at,
enabled,
hostname,
status,
updated_at
FROM cloudflare.origin_tls_client_auth.hostnames
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND status = '{{ status }}'
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="per_hostname_authenticated_origin_pull_enable_or_disable_a_hostname_for_client_authentication"
    values={[
        { label: 'per_hostname_authenticated_origin_pull_enable_or_disable_a_hostname_for_client_authentication', value: 'per_hostname_authenticated_origin_pull_enable_or_disable_a_hostname_for_client_authentication' }
    ]}
>
<TabItem value="per_hostname_authenticated_origin_pull_enable_or_disable_a_hostname_for_client_authentication">

Associate a hostname to a certificate and enable, disable or invalidate the association. If disabled, client certificate will not be sent to the hostname even if activated at the zone level. 100 maximum associations on a single certificate are allowed. Note: Use a null value for parameter *enabled* to invalidate the association.

```sql
REPLACE cloudflare.origin_tls_client_auth.hostnames
SET 
config = '{{ config }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND config = '{{ config }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>
