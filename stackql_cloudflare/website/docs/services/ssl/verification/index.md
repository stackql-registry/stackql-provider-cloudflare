--- 
title: verification
hide_title: false
hide_table_of_contents: false
keywords:
  - verification
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

Creates, updates, deletes, gets or lists a <code>verification</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="verification" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ssl.verification" /></td></tr>
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

SSL Verification Details response

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
    <td><CopyableCode code="brand_check" /></td>
    <td><code>boolean</code></td>
    <td>Certificate Authority is manually reviewing the order.</td>
</tr>
<tr>
    <td><CopyableCode code="cert_pack_uuid" /></td>
    <td><code>string</code></td>
    <td>Certificate Pack UUID. (example: a77f8bd7-3b47-46b4-a6f1-75cf98109948)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate_status" /></td>
    <td><code>string</code></td>
    <td>Current status of certificate. (initializing, authorizing, active, expired, issuing, timing_out, pending_deployment) (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="signature" /></td>
    <td><code>string</code></td>
    <td>Certificate's signature algorithm. (ECDSAWithSHA256, SHA1WithRSA, SHA256WithRSA)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_method" /></td>
    <td><code>string</code></td>
    <td>Validation method in use for a certificate pack order. (http, cname, txt) (example: txt)</td>
</tr>
<tr>
    <td><CopyableCode code="verification_info" /></td>
    <td><code>object</code></td>
    <td>Certificate's required verification information.</td>
</tr>
<tr>
    <td><CopyableCode code="verification_status" /></td>
    <td><code>boolean</code></td>
    <td>Status of the required verification information, omitted if verification status is unknown.</td>
</tr>
<tr>
    <td><CopyableCode code="verification_type" /></td>
    <td><code>string</code></td>
    <td>Method of verification. (cname, meta tag) (example: cname)</td>
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
    <td><a href="#parameter-retry"><code>retry</code></a></td>
    <td>Get SSL Verification Info for a Zone.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificate_pack_id"><code>certificate_pack_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-validation_method"><code>validation_method</code></a></td>
    <td></td>
    <td>Edit SSL validation method for a certificate pack. A PATCH request will request an immediate validation check on any certificate, and return the updated status. If a validation method is provided, the validation will be immediately attempted using that method.</td>
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
<tr id="parameter-retry">
    <td><CopyableCode code="retry" /></td>
    <td><code>boolean</code></td>
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

Get SSL Verification Info for a Zone.

```sql
SELECT
brand_check,
cert_pack_uuid,
certificate_status,
signature,
validation_method,
verification_info,
verification_status,
verification_type
FROM cloudflare.ssl.verification
WHERE zone_id = '{{ zone_id }}' -- required
AND retry = '{{ retry }}'
;
```
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

Edit SSL validation method for a certificate pack. A PATCH request will request an immediate validation check on any certificate, and return the updated status. If a validation method is provided, the validation will be immediately attempted using that method.

```sql
UPDATE cloudflare.ssl.verification
SET 
validation_method = '{{ validation_method }}'
WHERE 
certificate_pack_id = '{{ certificate_pack_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND validation_method = '{{ validation_method }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
