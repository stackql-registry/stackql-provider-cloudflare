--- 
title: cas
hide_title: false
hide_table_of_contents: false
keywords:
  - cas
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>cas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.cas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get a short-lived certificate CA response

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
    <td>The ID of the CA. (example: 7eddae4619b50ab1361ba8ae9bd72269a432fea041529ed9)</td>
</tr>
<tr>
    <td><CopyableCode code="aud" /></td>
    <td><code>string</code></td>
    <td>The Application Audience (AUD) tag. Identifies the application associated with the CA. (example: 737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893)</td>
</tr>
<tr>
    <td><CopyableCode code="public_key" /></td>
    <td><code>string</code></td>
    <td>The public key to add to your SSH server configuration. (example: ecdsa-sha2-nistp256 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx= open-ssh-ca@cloudflareaccess.org)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get a short-lived certificate CA response

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
    <td>The ID of the CA. (example: 7eddae4619b50ab1361ba8ae9bd72269a432fea041529ed9)</td>
</tr>
<tr>
    <td><CopyableCode code="aud" /></td>
    <td><code>string</code></td>
    <td>The Application Audience (AUD) tag. Identifies the application associated with the CA. (example: 737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893)</td>
</tr>
<tr>
    <td><CopyableCode code="public_key" /></td>
    <td><code>string</code></td>
    <td>The public key to add to your SSH server configuration. (example: ecdsa-sha2-nistp256 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx= open-ssh-ca@cloudflareaccess.org)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List short-lived certificate CAs response

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
    <td>The ID of the CA. (example: 7eddae4619b50ab1361ba8ae9bd72269a432fea041529ed9)</td>
</tr>
<tr>
    <td><CopyableCode code="aud" /></td>
    <td><code>string</code></td>
    <td>The Application Audience (AUD) tag. Identifies the application associated with the CA. (example: 737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893)</td>
</tr>
<tr>
    <td><CopyableCode code="public_key" /></td>
    <td><code>string</code></td>
    <td>The public key to add to your SSH server configuration. (example: ecdsa-sha2-nistp256 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx= open-ssh-ca@cloudflareaccess.org)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List short-lived certificate CAs response

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
    <td>The ID of the CA. (example: 7eddae4619b50ab1361ba8ae9bd72269a432fea041529ed9)</td>
</tr>
<tr>
    <td><CopyableCode code="aud" /></td>
    <td><code>string</code></td>
    <td>The Application Audience (AUD) tag. Identifies the application associated with the CA. (example: 737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893)</td>
</tr>
<tr>
    <td><CopyableCode code="public_key" /></td>
    <td><code>string</code></td>
    <td>The public key to add to your SSH server configuration. (example: ecdsa-sha2-nistp256 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx= open-ssh-ca@cloudflareaccess.org)</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a short-lived certificate CA and its public key.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches a short-lived certificate CA and its public key.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists short-lived certificate CAs and their public keys.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists short-lived certificate CAs and their public keys.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Generates a new short-lived certificate CA and public key.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Generates a new short-lived certificate CA and public key.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a short-lived certificate CA.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes a short-lived certificate CA.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches a short-lived certificate CA and its public key.

```sql
SELECT
id,
aud,
public_key
FROM cloudflare.zero_trust.cas
WHERE app_id = '{{ app_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches a short-lived certificate CA and its public key.

```sql
SELECT
id,
aud,
public_key
FROM cloudflare.zero_trust.cas
WHERE app_id = '{{ app_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Lists short-lived certificate CAs and their public keys.

```sql
SELECT
id,
aud,
public_key
FROM cloudflare.zero_trust.cas
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Lists short-lived certificate CAs and their public keys.

```sql
SELECT
id,
aud,
public_key
FROM cloudflare.zero_trust.cas
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'create_by_zone', value: 'create_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Generates a new short-lived certificate CA and public key.

```sql
INSERT INTO cloudflare.zero_trust.cas (
app_id,
account_id
)
SELECT 
'{{ app_id }}',
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="create_by_zone">

Generates a new short-lived certificate CA and public key.

```sql
INSERT INTO cloudflare.zero_trust.cas (
app_id,
zone_id
)
SELECT 
'{{ app_id }}',
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
- name: cas
  props:
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the cas resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the cas resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the cas resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' },
        { label: 'delete_by_zone', value: 'delete_by_zone' }
    ]}
>
<TabItem value="delete_by_account">

Deletes a short-lived certificate CA.

```sql
DELETE FROM cloudflare.zero_trust.cas
WHERE app_id = '{{ app_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes a short-lived certificate CA.

```sql
DELETE FROM cloudflare.zero_trust.cas
WHERE app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
