--- 
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.custom_hostnames.certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-custom_hostname_id"><code>custom_hostname_id</code></a>, <a href="#parameter-certificate_pack_id"><code>certificate_pack_id</code></a>, <a href="#parameter-certificate_id"><code>certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-custom_certificate"><code>custom_certificate</code></a>, <a href="#parameter-custom_key"><code>custom_key</code></a></td>
    <td></td>
    <td>Replace a single custom certificate within a certificate pack that contains two bundled certificates. The replacement must adhere to the following constraints. You can only replace an RSA certificate with another RSA certificate or an ECDSA certificate with another ECDSA certificate.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_hostname_id"><code>custom_hostname_id</code></a>, <a href="#parameter-certificate_pack_id"><code>certificate_pack_id</code></a>, <a href="#parameter-certificate_id"><code>certificate_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Delete a single custom certificate from a certificate pack that contains two bundled certificates. Deletion is subject to the following constraints. You cannot delete a certificate if it is the only remaining certificate in the pack. At least one certificate must remain in the pack.</td>
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
<tr id="parameter-certificate_id">
    <td><CopyableCode code="certificate_id" /></td>
    <td><code>string</code></td>
    <td>The certificate ID.</td>
</tr>
<tr id="parameter-certificate_pack_id">
    <td><CopyableCode code="certificate_pack_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
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
</tbody>
</table>

## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Replace a single custom certificate within a certificate pack that contains two bundled certificates. The replacement must adhere to the following constraints. You can only replace an RSA certificate with another RSA certificate or an ECDSA certificate with another ECDSA certificate.

```sql
REPLACE cloudflare.custom_hostnames.certificates
SET 
custom_certificate = '{{ custom_certificate }}',
custom_key = '{{ custom_key }}'
WHERE 
custom_hostname_id = '{{ custom_hostname_id }}' --required
AND certificate_pack_id = '{{ certificate_pack_id }}' --required
AND certificate_id = '{{ certificate_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND custom_certificate = '{{ custom_certificate }}' --required
AND custom_key = '{{ custom_key }}' --required
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

Delete a single custom certificate from a certificate pack that contains two bundled certificates. Deletion is subject to the following constraints. You cannot delete a certificate if it is the only remaining certificate in the pack. At least one certificate must remain in the pack.

```sql
DELETE FROM cloudflare.custom_hostnames.certificates
WHERE custom_hostname_id = '{{ custom_hostname_id }}' --required
AND certificate_pack_id = '{{ certificate_pack_id }}' --required
AND certificate_id = '{{ certificate_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
