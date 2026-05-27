--- 
title: custom_hostnames
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_hostnames
  - custom_hostnames
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

Creates, updates, deletes, gets or lists a <code>custom_hostnames</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_hostnames" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.custom_hostnames.custom_hostnames" /></td></tr>
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

Custom Hostname Details response

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
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the time the hostname was created. (example: 2020-02-06T18:11:23.531995Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_metadata" /></td>
    <td><code>object</code></td>
    <td>Unique key/value metadata for this hostname. These are per-hostname (customer) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_origin_server" /></td>
    <td><code>string</code></td>
    <td>a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record. (example: origin2.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_origin_sni" /></td>
    <td><code>string</code></td>
    <td>A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ':request_host_header:' which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server. (example: sni.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The custom hostname that will point to your hostname via CNAME. (example: app.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_verification" /></td>
    <td><code>object</code></td>
    <td>This is a record which can be placed to activate a hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_verification_http" /></td>
    <td><code>object</code></td>
    <td>This presents the token to be served by the given http url to activate a hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="ssl" /></td>
    <td><code>object</code></td>
    <td>SSL properties for the custom hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the hostname's activation. (active, pending, active_redeploying, moved, pending_deletion, deleted, pending_blocked, pending_migration, pending_provisioned, test_pending, test_active, test_active_apex, test_blocked, test_failed, provisioned, blocked) (example: pending)</td>
</tr>
<tr>
    <td><CopyableCode code="verification_errors" /></td>
    <td><code>array</code></td>
    <td>These are errors that were encountered while trying to activate a hostname.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Custom Hostnames response

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
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the time the hostname was created. (example: 2020-02-06T18:11:23.531995Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_metadata" /></td>
    <td><code>object</code></td>
    <td>Unique key/value metadata for this hostname. These are per-hostname (customer) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_origin_server" /></td>
    <td><code>string</code></td>
    <td>a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record. (example: origin2.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_origin_sni" /></td>
    <td><code>string</code></td>
    <td>A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ':request_host_header:' which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server. (example: sni.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The custom hostname that will point to your hostname via CNAME. (example: app.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_verification" /></td>
    <td><code>object</code></td>
    <td>This is a record which can be placed to activate a hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_verification_http" /></td>
    <td><code>object</code></td>
    <td>This presents the token to be served by the given http url to activate a hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="ssl" /></td>
    <td><code>object</code></td>
    <td>SSL properties for the custom hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the hostname's activation. (active, pending, active_redeploying, moved, pending_deletion, deleted, pending_blocked, pending_migration, pending_provisioned, test_pending, test_active, test_active_apex, test_blocked, test_failed, provisioned, blocked) (example: pending)</td>
</tr>
<tr>
    <td><CopyableCode code="verification_errors" /></td>
    <td><code>array</code></td>
    <td>These are errors that were encountered while trying to activate a hostname.</td>
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
    <td><a href="#parameter-custom_hostname_id"><code>custom_hostname_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Retrieves detailed information about a specific custom hostname, including SSL certificate status, ownership verification, and origin configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-hostname.contain"><code>hostname.contain</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-ssl_status"><code>ssl_status</code></a>, <a href="#parameter-hostname_status"><code>hostname_status</code></a>, <a href="#parameter-certificate_authority"><code>certificate_authority</code></a>, <a href="#parameter-wildcard"><code>wildcard</code></a>, <a href="#parameter-custom_origin_server"><code>custom_origin_server</code></a>, <a href="#parameter-ssl"><code>ssl</code></a></td>
    <td>List, search, sort, and filter all of your custom hostnames.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-hostname"><code>hostname</code></a></td>
    <td></td>
    <td>Add a new custom hostname and request that an SSL certificate be issued for it. One of three validation methods—http, txt, email—should be used, with 'http' recommended if the CNAME is already in place (or will be soon). Specifying 'email' will send an email to the WHOIS contacts on file for the base domain plus hostmaster, postmaster, webmaster, admin, administrator. If http is used and the domain is not already pointing to the Managed CNAME host, the PATCH method must be used once it is (to complete validation). Enable bundling of certificates using the custom_cert_bundle field. The bundling process requires the following condition One certificate in the bundle must use an RSA, and the other must use an ECDSA.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-custom_hostname_id"><code>custom_hostname_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Modify SSL configuration for a custom hostname. When sent with SSL config that matches existing config, used to indicate that hostname should pass domain control validation (DCV). Can also be used to change validation type, e.g., from 'http' to 'email'. Bundle an existing certificate with another certificate by using the "custom_cert_bundle" field. The bundling process supports combining certificates as long as the following condition is met. One certificate must use the RSA algorithm, and the other must use the ECDSA algorithm.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_hostname_id"><code>custom_hostname_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Permanently deletes a custom hostname and revokes any SSL certificates that were issued for it. This action cannot be undone.</td>
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
<tr id="parameter-custom_hostname_id">
    <td><CopyableCode code="custom_hostname_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-certificate_authority">
    <td><CopyableCode code="certificate_authority" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-custom_origin_server">
    <td><CopyableCode code="custom_origin_server" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-hostname.contain">
    <td><CopyableCode code="hostname.contain" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-hostname_status">
    <td><CopyableCode code="hostname_status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
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
<tr id="parameter-ssl">
    <td><CopyableCode code="ssl" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-ssl_status">
    <td><CopyableCode code="ssl_status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-wildcard">
    <td><CopyableCode code="wildcard" /></td>
    <td><code>boolean</code></td>
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

Retrieves detailed information about a specific custom hostname, including SSL certificate status, ownership verification, and origin configuration.

```sql
SELECT
id,
created_at,
custom_metadata,
custom_origin_server,
custom_origin_sni,
hostname,
ownership_verification,
ownership_verification_http,
ssl,
status,
verification_errors
FROM cloudflare.custom_hostnames.custom_hostnames
WHERE custom_hostname_id = '{{ custom_hostname_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List, search, sort, and filter all of your custom hostnames.

```sql
SELECT
id,
created_at,
custom_metadata,
custom_origin_server,
custom_origin_sni,
hostname,
ownership_verification,
ownership_verification_http,
ssl,
status,
verification_errors
FROM cloudflare.custom_hostnames.custom_hostnames
WHERE zone_id = '{{ zone_id }}' -- required
AND hostname = '{{ hostname }}'
AND hostname.contain = '{{ hostname.contain }}'
AND id = '{{ id }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order = '{{ order }}'
AND direction = '{{ direction }}'
AND ssl_status = '{{ ssl_status }}'
AND hostname_status = '{{ hostname_status }}'
AND certificate_authority = '{{ certificate_authority }}'
AND wildcard = '{{ wildcard }}'
AND custom_origin_server = '{{ custom_origin_server }}'
AND ssl = '{{ ssl }}'
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

Add a new custom hostname and request that an SSL certificate be issued for it. One of three validation methods—http, txt, email—should be used, with 'http' recommended if the CNAME is already in place (or will be soon). Specifying 'email' will send an email to the WHOIS contacts on file for the base domain plus hostmaster, postmaster, webmaster, admin, administrator. If http is used and the domain is not already pointing to the Managed CNAME host, the PATCH method must be used once it is (to complete validation). Enable bundling of certificates using the custom_cert_bundle field. The bundling process requires the following condition One certificate in the bundle must use an RSA, and the other must use an ECDSA.

```sql
INSERT INTO cloudflare.custom_hostnames.custom_hostnames (
custom_metadata,
hostname,
ssl,
zone_id
)
SELECT 
'{{ custom_metadata }}',
'{{ hostname }}' /* required */,
'{{ ssl }}',
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
- name: custom_hostnames
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the custom_hostnames resource.
    - name: custom_metadata
      value: "{{ custom_metadata }}"
      description: |
        Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
    - name: hostname
      value: "{{ hostname }}"
      description: |
        The custom hostname that will point to your hostname via CNAME.
    - name: ssl
      description: |
        SSL properties used when creating the custom hostname.
      value:
        bundle_method: "{{ bundle_method }}"
        certificate_authority: "{{ certificate_authority }}"
        cloudflare_branding: {{ cloudflare_branding }}
        custom_cert_bundle:
          - custom_certificate: "{{ custom_certificate }}"
            custom_key: "{{ custom_key }}"
        custom_certificate: "{{ custom_certificate }}"
        custom_csr_id: "{{ custom_csr_id }}"
        custom_key: "{{ custom_key }}"
        method: "{{ method }}"
        settings:
          ciphers:
            - "{{ ciphers }}"
          early_hints: "{{ early_hints }}"
          http2: "{{ http2 }}"
          min_tls_version: "{{ min_tls_version }}"
          tls_1_3: "{{ tls_1_3 }}"
        type: "{{ type }}"
        wildcard: {{ wildcard }}
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

Modify SSL configuration for a custom hostname. When sent with SSL config that matches existing config, used to indicate that hostname should pass domain control validation (DCV). Can also be used to change validation type, e.g., from 'http' to 'email'. Bundle an existing certificate with another certificate by using the "custom_cert_bundle" field. The bundling process supports combining certificates as long as the following condition is met. One certificate must use the RSA algorithm, and the other must use the ECDSA algorithm.

```sql
UPDATE cloudflare.custom_hostnames.custom_hostnames
SET 
custom_metadata = '{{ custom_metadata }}',
custom_origin_server = '{{ custom_origin_server }}',
custom_origin_sni = '{{ custom_origin_sni }}',
ssl = '{{ ssl }}'
WHERE 
custom_hostname_id = '{{ custom_hostname_id }}' --required
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

Permanently deletes a custom hostname and revokes any SSL certificates that were issued for it. This action cannot be undone.

```sql
DELETE FROM cloudflare.custom_hostnames.custom_hostnames
WHERE custom_hostname_id = '{{ custom_hostname_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
