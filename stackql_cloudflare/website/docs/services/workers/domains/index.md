--- 
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - workers
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.domains" /></td></tr>
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

Get domain response.

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
    <td>Immutable ID of the domain. (example: dbe10b4bc17c295377eabd600e1787fd)</td>
</tr>
<tr>
    <td><CopyableCode code="cert_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>ID of the TLS certificate issued for the domain. (example: 9fdf92c8-64c2-4a3d-b1af-e15304961145)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>ID of the zone containing the domain hostname. (example: 593c9c94de529bbbfaac7c53ced0447d, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_name" /></td>
    <td><code>string</code></td>
    <td>Name of the zone containing the domain hostname. (example: example.com, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Worker environment associated with the domain. (example: production, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>Hostname of the domain. Can be either the zone apex or a subdomain of the zone. Requests to this hostname will be routed to the configured Worker. (example: app.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td>Name of the Worker associated with the domain. Requests to the configured hostname will be routed to this Worker. (example: my-worker)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List domains response.

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
    <td>Immutable ID of the domain. (example: dbe10b4bc17c295377eabd600e1787fd)</td>
</tr>
<tr>
    <td><CopyableCode code="cert_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>ID of the TLS certificate issued for the domain. (example: 9fdf92c8-64c2-4a3d-b1af-e15304961145)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>ID of the zone containing the domain hostname. (example: 593c9c94de529bbbfaac7c53ced0447d, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="zone_name" /></td>
    <td><code>string</code></td>
    <td>Name of the zone containing the domain hostname. (example: example.com, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>Worker environment associated with the domain. (example: production, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>Hostname of the domain. Can be either the zone apex or a subdomain of the zone. Requests to this hostname will be routed to the configured Worker. (example: app.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td>Name of the Worker associated with the domain. Requests to the configured hostname will be routed to this Worker. (example: my-worker)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td></td>
    <td>Gets information about a domain.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-service"><code>service</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-environment"><code>environment</code></a></td>
    <td>Lists all domains for an account.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-zone_name"><code>zone_name</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-service"><code>service</code></a>, <a href="#parameter-environment"><code>environment</code></a></td>
    <td></td>
    <td>Attaches a domain that routes traffic to a Worker.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td></td>
    <td>Detaches a domain from a Worker. Both the Worker and all of its previews are no longer routable using this domain.</td>
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
<tr id="parameter-domain_id">
    <td><CopyableCode code="domain_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-environment">
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-service">
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_name">
    <td><CopyableCode code="zone_name" /></td>
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

Gets information about a domain.

```sql
SELECT
id,
cert_id,
zone_id,
zone_name,
environment,
hostname,
service
FROM cloudflare.workers.domains
WHERE account_id = '{{ account_id }}' -- required
AND domain_id = '{{ domain_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all domains for an account.

```sql
SELECT
id,
cert_id,
zone_id,
zone_name,
environment,
hostname,
service
FROM cloudflare.workers.domains
WHERE account_id = '{{ account_id }}' -- required
AND zone_id = '{{ zone_id }}'
AND zone_name = '{{ zone_name }}'
AND service = '{{ service }}'
AND hostname = '{{ hostname }}'
AND environment = '{{ environment }}'
;
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

Attaches a domain that routes traffic to a Worker.

```sql
REPLACE cloudflare.workers.domains
SET 
environment = '{{ environment }}',
hostname = '{{ hostname }}',
service = '{{ service }}',
zone_id = '{{ zone_id }}',
zone_name = '{{ zone_name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND zone_name = '{{ zone_name }}' --required
AND hostname = '{{ hostname }}' --required
AND service = '{{ service }}' --required
AND environment = '{{ environment }}' --required
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

Detaches a domain from a Worker. Both the Worker and all of its previews are no longer routable using this domain.

```sql
DELETE FROM cloudflare.workers.domains
WHERE account_id = '{{ account_id }}' --required
AND domain_id = '{{ domain_id }}' --required
;
```
</TabItem>
</Tabs>
