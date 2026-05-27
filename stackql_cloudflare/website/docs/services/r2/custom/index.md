--- 
title: custom
hide_title: false
hide_table_of_contents: false
keywords:
  - custom
  - r2
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

Creates, updates, deletes, gets or lists a <code>custom</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.r2.custom" /></td></tr>
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

Get Custom Domain Configuration response.

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
    <td><CopyableCode code="ciphers" /></td>
    <td><code>array</code></td>
    <td>An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain name of the custom domain to be added.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether this bucket is publicly accessible at the specified custom domain.</td>
</tr>
<tr>
    <td><CopyableCode code="minTLS" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS Version the custom domain will accept for incoming connections. If not set, defaults to 1.0. (1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="zoneId" /></td>
    <td><code>string</code></td>
    <td>Zone ID of the custom domain resides in.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneName" /></td>
    <td><code>string</code></td>
    <td>Zone that the custom domain resides in.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Custom Domains response.

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
    <td><CopyableCode code="ciphers" /></td>
    <td><code>array</code></td>
    <td>An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain name of the custom domain to be added.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether this bucket is publicly accessible at the specified custom domain.</td>
</tr>
<tr>
    <td><CopyableCode code="minTLS" /></td>
    <td><code>string</code></td>
    <td>Minimum TLS Version the custom domain will accept for incoming connections. If not set, defaults to 1.0. (1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="zoneId" /></td>
    <td><code>string</code></td>
    <td>Zone ID of the custom domain resides in.</td>
</tr>
<tr>
    <td><CopyableCode code="zoneName" /></td>
    <td><code>string</code></td>
    <td>Zone that the custom domain resides in.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-domain"><code>domain</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Get the configuration for a custom domain on an existing R2 bucket.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Gets a list of all custom domains registered with an existing R2 bucket.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-zoneId"><code>zoneId</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Register a new custom domain for an existing R2 bucket.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-domain"><code>domain</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Edit the configuration for a custom domain on an existing R2 bucket.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain"><code>domain</code></a></td>
    <td><a href="#parameter-cf-r2-jurisdiction"><code>cf-r2-jurisdiction</code></a></td>
    <td>Remove custom domain registration from an existing R2 bucket.</td>
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
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account ID.</td>
</tr>
<tr id="parameter-bucket_name">
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>The R2 bucket name.</td>
</tr>
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-cf-r2-jurisdiction">
    <td><CopyableCode code="cf-r2-jurisdiction" /></td>
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

Get the configuration for a custom domain on an existing R2 bucket.

```sql
SELECT
ciphers,
domain,
enabled,
minTLS,
status,
zoneId,
zoneName
FROM cloudflare.r2.custom
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND domain = '{{ domain }}' -- required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
<TabItem value="list">

Gets a list of all custom domains registered with an existing R2 bucket.

```sql
SELECT
ciphers,
domain,
enabled,
minTLS,
status,
zoneId,
zoneName
FROM cloudflare.r2.custom
WHERE account_id = '{{ account_id }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
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

Register a new custom domain for an existing R2 bucket.

```sql
INSERT INTO cloudflare.r2.custom (
ciphers,
domain,
enabled,
minTLS,
zoneId,
account_id,
bucket_name,
cf-r2-jurisdiction
)
SELECT 
'{{ ciphers }}',
'{{ domain }}' /* required */,
{{ enabled }} /* required */,
'{{ minTLS }}',
'{{ zoneId }}' /* required */,
'{{ account_id }}',
'{{ bucket_name }}',
'{{ cf-r2-jurisdiction }}'
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
- name: custom
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the custom resource.
    - name: bucket_name
      value: "{{ bucket_name }}"
      description: Required parameter for the custom resource.
    - name: ciphers
      value:
        - "{{ ciphers }}"
      description: |
        An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
    - name: domain
      value: "{{ domain }}"
      description: |
        Name of the custom domain to be added.
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether to enable public bucket access at the custom domain. If undefined, the domain will be enabled.
    - name: minTLS
      value: "{{ minTLS }}"
      description: |
        Minimum TLS Version the custom domain will accept for incoming connections. If not set, defaults to 1.0.
      valid_values: ['1.0', '1.1', '1.2', '1.3']
    - name: zoneId
      value: "{{ zoneId }}"
      description: |
        Zone ID of the custom domain.
    - name: cf-r2-jurisdiction
      value: "{{ cf-r2-jurisdiction }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Edit the configuration for a custom domain on an existing R2 bucket.

```sql
REPLACE cloudflare.r2.custom
SET 
ciphers = '{{ ciphers }}',
enabled = {{ enabled }},
minTLS = '{{ minTLS }}'
WHERE 
account_id = '{{ account_id }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND domain = '{{ domain }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction}}'
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

Remove custom domain registration from an existing R2 bucket.

```sql
DELETE FROM cloudflare.r2.custom
WHERE bucket_name = '{{ bucket_name }}' --required
AND account_id = '{{ account_id }}' --required
AND domain = '{{ domain }}' --required
AND cf-r2-jurisdiction = '{{ cf-r2-jurisdiction }}'
;
```
</TabItem>
</Tabs>
