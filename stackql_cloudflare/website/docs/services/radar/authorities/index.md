--- 
title: authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - authorities
  - radar
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

Creates, updates, deletes, gets or lists an <code>authorities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authorities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.radar.authorities" /></td></tr>
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

Successful response.

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
    <td><CopyableCode code="certificateAuthority" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Successful response.

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
    <td>The full name of the certificate authority (CA).</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRecordType" /></td>
    <td><code>string</code></td>
    <td>Specifies the type of certificate in the trust chain. (ROOT_CERTIFICATE, INTERMEDIATE_CERTIFICATE)</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The two-letter ISO country code where the CA organization is based.</td>
</tr>
<tr>
    <td><CopyableCode code="countryName" /></td>
    <td><code>string</code></td>
    <td>The full country name corresponding to the country code.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>The organization that owns and operates the CA.</td>
</tr>
<tr>
    <td><CopyableCode code="parentName" /></td>
    <td><code>string</code></td>
    <td>The name of the parent/root certificate authority that issued this intermediate certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="parentSha256Fingerprint" /></td>
    <td><code>string</code></td>
    <td>The SHA-256 fingerprint of the parent certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="revocationStatus" /></td>
    <td><code>string</code></td>
    <td>The current revocation status of a Certificate Authority (CA) certificate. (NOT_REVOKED, REVOKED, PARENT_CERT_REVOKED)</td>
</tr>
<tr>
    <td><CopyableCode code="sha256Fingerprint" /></td>
    <td><code>string</code></td>
    <td>The SHA-256 fingerprint of the intermediate certificate.</td>
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
    <td><a href="#parameter-ca_slug"><code>ca_slug</code></a></td>
    <td><a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves the requested CA information.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-offset"><code>offset</code></a>, <a href="#parameter-format"><code>format</code></a></td>
    <td>Retrieves a list of certificate authorities.</td>
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
<tr id="parameter-ca_slug">
    <td><CopyableCode code="ca_slug" /></td>
    <td><code>string</code></td>
    <td>Certificate authority SHA256 fingerprint.</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Format in which results will be returned.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Limits the number of objects returned in the response.</td>
</tr>
<tr id="parameter-offset">
    <td><CopyableCode code="offset" /></td>
    <td><code>integer</code></td>
    <td>Skips the specified number of objects before fetching the results.</td>
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

Retrieves the requested CA information.

```sql
SELECT
certificateAuthority
FROM cloudflare.radar.authorities
WHERE ca_slug = '{{ ca_slug }}' -- required
AND format = '{{ format }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of certificate authorities.

```sql
SELECT
name,
certificateRecordType,
country,
countryName,
owner,
parentName,
parentSha256Fingerprint,
revocationStatus,
sha256Fingerprint
FROM cloudflare.radar.authorities
WHERE limit = '{{ limit }}'
AND offset = '{{ offset }}'
AND format = '{{ format }}'
;
```
</TabItem>
</Tabs>
