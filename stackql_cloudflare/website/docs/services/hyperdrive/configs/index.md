--- 
title: configs
hide_title: false
hide_table_of_contents: false
keywords:
  - configs
  - hyperdrive
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

Creates, updates, deletes, gets or lists a <code>configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.hyperdrive.configs" /></td></tr>
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

Get Hyperdrive Response.

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
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Return the status of the API call success. (true)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Hyperdrives Response.

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
    <td>Define configurations using a unique string identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Hyperdrive configuration. Used to identify the configuration in the Cloudflare dashboard and API. (example: example-hyperdrive)</td>
</tr>
<tr>
    <td><CopyableCode code="caching" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Defines the creation time of the Hyperdrive configuration. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Defines the last modified time of the Hyperdrive configuration. (example: 2017-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="mtls" /></td>
    <td><code>object</code></td>
    <td>mTLS configuration for the origin connection. Cannot be used with VPC Service origins; TLS must be managed on the VPC Service. (title: mTLS)</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>object</code></td>
    <td> (title: Public Database)</td>
</tr>
<tr>
    <td><CopyableCode code="origin_connection_limit" /></td>
    <td><code>integer</code></td>
    <td>The (soft) maximum number of connections the Hyperdrive is allowed to make to the origin database. Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not specified, defaults to 20 for free tier and 60 for paid tier. Contact Cloudflare if you need a higher limit.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hyperdrive_id"><code>hyperdrive_id</code></a></td>
    <td></td>
    <td>Returns the specified Hyperdrive configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns a list of Hyperdrives.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-origin"><code>origin</code></a></td>
    <td></td>
    <td>Creates and returns a new Hyperdrive configuration.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hyperdrive_id"><code>hyperdrive_id</code></a></td>
    <td></td>
    <td>Patches and returns the specified Hyperdrive configuration. Custom caching settings are not kept if caching is disabled.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hyperdrive_id"><code>hyperdrive_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-origin"><code>origin</code></a></td>
    <td></td>
    <td>Updates and returns the specified Hyperdrive configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-hyperdrive_id"><code>hyperdrive_id</code></a></td>
    <td></td>
    <td>Deletes the specified Hyperdrive.</td>
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
<tr id="parameter-hyperdrive_id">
    <td><CopyableCode code="hyperdrive_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the Hyperdrive configuration.</td>
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

Returns the specified Hyperdrive configuration.

```sql
SELECT
errors,
messages,
result,
success
FROM cloudflare.hyperdrive.configs
WHERE account_id = '{{ account_id }}' -- required
AND hyperdrive_id = '{{ hyperdrive_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a list of Hyperdrives.

```sql
SELECT
id,
name,
caching,
created_on,
modified_on,
mtls,
origin,
origin_connection_limit
FROM cloudflare.hyperdrive.configs
WHERE account_id = '{{ account_id }}' -- required
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

Creates and returns a new Hyperdrive configuration.

```sql
INSERT INTO cloudflare.hyperdrive.configs (
caching,
mtls,
name,
origin,
origin_connection_limit,
account_id
)
SELECT 
'{{ caching }}',
'{{ mtls }}',
'{{ name }}' /* required */,
'{{ origin }}' /* required */,
{{ origin_connection_limit }},
'{{ account_id }}'
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
- name: configs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the configs resource.
    - name: caching
      value:
        disabled: {{ disabled }}
        max_age: {{ max_age }}
        stale_while_revalidate: {{ stale_while_revalidate }}
    - name: mtls
      description: |
        mTLS configuration for the origin connection. Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
      value:
        ca_certificate_id: "{{ ca_certificate_id }}"
        mtls_certificate_id: "{{ mtls_certificate_id }}"
        sslmode: "{{ sslmode }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the Hyperdrive configuration. Used to identify the configuration in the Cloudflare dashboard and API.
    - name: origin
      value:
        database: "{{ database }}"
        password: "{{ password }}"
        scheme: "{{ scheme }}"
        user: "{{ user }}"
        host: "{{ host }}"
        port: {{ port }}
        access_client_id: "{{ access_client_id }}"
        access_client_secret: "{{ access_client_secret }}"
        service_id: "{{ service_id }}"
    - name: origin_connection_limit
      value: {{ origin_connection_limit }}
      description: |
        The (soft) maximum number of connections the Hyperdrive is allowed to make to the origin database. Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not specified, defaults to 20 for free tier and 60 for paid tier. Contact Cloudflare if you need a higher limit.
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

Patches and returns the specified Hyperdrive configuration. Custom caching settings are not kept if caching is disabled.

```sql
UPDATE cloudflare.hyperdrive.configs
SET 
caching = '{{ caching }}',
mtls = '{{ mtls }}',
name = '{{ name }}',
origin = '{{ origin }}',
origin_connection_limit = {{ origin_connection_limit }}
WHERE 
account_id = '{{ account_id }}' --required
AND hyperdrive_id = '{{ hyperdrive_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
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

Updates and returns the specified Hyperdrive configuration.

```sql
REPLACE cloudflare.hyperdrive.configs
SET 
caching = '{{ caching }}',
mtls = '{{ mtls }}',
name = '{{ name }}',
origin = '{{ origin }}',
origin_connection_limit = {{ origin_connection_limit }}
WHERE 
account_id = '{{ account_id }}' --required
AND hyperdrive_id = '{{ hyperdrive_id }}' --required
AND name = '{{ name }}' --required
AND origin = '{{ origin }}' --required
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

Deletes the specified Hyperdrive.

```sql
DELETE FROM cloudflare.hyperdrive.configs
WHERE account_id = '{{ account_id }}' --required
AND hyperdrive_id = '{{ hyperdrive_id }}' --required
;
```
</TabItem>
</Tabs>
