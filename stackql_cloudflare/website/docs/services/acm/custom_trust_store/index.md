--- 
title: custom_trust_store
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_trust_store
  - acm
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

Creates, updates, deletes, gets or lists a <code>custom_trust_store</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_trust_store" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.acm.custom_trust_store" /></td></tr>
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

Custom Origin Trust Store Details response

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
    <td><CopyableCode code="certificate" /></td>
    <td><code>string</code></td>
    <td>The zone's SSL certificate or certificate and the intermediate(s). (example: -----BEGIN CERTIFICATE-----<br />MIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...<br />-----END CERTIFICATE-----<br />)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate expires. (example: 2122-10-29T16:59:47Z)</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The certificate authority that issued the certificate. (example: GlobalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the certificate. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the zone's custom SSL. (initializing, pending_deployment, active, pending_deletion, deleted, expired) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate was last modified. (example: 2014-01-01T05:20:00Z)</td>
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

Custom Origin Trust Store Details response

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
    <td><CopyableCode code="certificate" /></td>
    <td><code>string</code></td>
    <td>The zone's SSL certificate or certificate and the intermediate(s). (example: -----BEGIN CERTIFICATE-----<br />MIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...<br />-----END CERTIFICATE-----<br />)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate expires. (example: 2122-10-29T16:59:47Z)</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The certificate authority that issued the certificate. (example: GlobalSign)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>The type of hash used for the certificate. (example: SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the zone's custom SSL. (initializing, pending_deployment, active, pending_deletion, deleted, expired) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the certificate was last modified. (example: 2014-01-01T05:20:00Z)</td>
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
    <td><a href="#parameter-custom_origin_trust_store_id"><code>custom_origin_trust_store_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Retrieves details about a specific certificate in the custom origin trust store, including expiration and subject information.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a></td>
    <td>Get Custom Origin Trust Store for a Zone.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-certificate"><code>certificate</code></a></td>
    <td></td>
    <td>Add Custom Origin Trust Store for a Zone.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_origin_trust_store_id"><code>custom_origin_trust_store_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Removes a CA certificate from the custom origin trust store. Origins using certificates signed by this CA will no longer be trusted.</td>
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
<tr id="parameter-custom_origin_trust_store_id">
    <td><CopyableCode code="custom_origin_trust_store_id" /></td>
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

Retrieves details about a specific certificate in the custom origin trust store, including expiration and subject information.

```sql
SELECT
id,
certificate,
expires_on,
issuer,
signature,
status,
updated_at,
uploaded_on
FROM cloudflare.acm.custom_trust_store
WHERE custom_origin_trust_store_id = '{{ custom_origin_trust_store_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get Custom Origin Trust Store for a Zone.

```sql
SELECT
id,
certificate,
expires_on,
issuer,
signature,
status,
updated_at,
uploaded_on
FROM cloudflare.acm.custom_trust_store
WHERE zone_id = '{{ zone_id }}' -- required
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

Add Custom Origin Trust Store for a Zone.

```sql
INSERT INTO cloudflare.acm.custom_trust_store (
certificate,
zone_id
)
SELECT 
'{{ certificate }}' /* required */,
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
- name: custom_trust_store
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the custom_trust_store resource.
    - name: certificate
      value: "{{ certificate }}"
      description: |
        The zone's SSL certificate or certificate and the intermediate(s).
`}</CodeBlock>

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

Removes a CA certificate from the custom origin trust store. Origins using certificates signed by this CA will no longer be trusted.

```sql
DELETE FROM cloudflare.acm.custom_trust_store
WHERE custom_origin_trust_store_id = '{{ custom_origin_trust_store_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
