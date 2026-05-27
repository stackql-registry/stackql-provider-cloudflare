--- 
title: bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - bindings
  - workers_for_platforms
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

Creates, updates, deletes, gets or lists a <code>bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bindings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers_for_platforms.bindings" /></td></tr>
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

Fetch script bindings (Workers for Platforms).

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
    <td>Identifier of the D1 database to bind to. (example: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, x-stainless-deprecation-message: This property has been renamed to `database_id`.)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A JavaScript variable name for the binding. (example: myBinding)</td>
</tr>
<tr>
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>ID of the Flagship app to bind to for feature flag evaluation. (example: app-12345678-1234-1234-1234-123456789012)</td>
</tr>
<tr>
    <td><CopyableCode code="certificate_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the certificate to bind to. (example: efwu2n6s-q69d-2kr9-184j-4913e8h391k6)</td>
</tr>
<tr>
    <td><CopyableCode code="database_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the D1 database to bind to. (example: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)</td>
</tr>
<tr>
    <td><CopyableCode code="namespace_id" /></td>
    <td><code>string</code></td>
    <td>Namespace identifier tag. (x-stainless-terraform-configurability: computed_optional, example: 0f2ac74b498b48028cb68387c421e279)</td>
</tr>
<tr>
    <td><CopyableCode code="network_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the network to bind to. Only "cf1:network" is currently supported. Mutually exclusive with tunnel_id. (example: cf1:network)</td>
</tr>
<tr>
    <td><CopyableCode code="service_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the VPC service to bind to. (example: 8c8b1387108e49be85669169793e7bd2)</td>
</tr>
<tr>
    <td><CopyableCode code="store_id" /></td>
    <td><code>string</code></td>
    <td>ID of the store containing the secret. (example: 8c8b1387108e49be85669169793e7bd2)</td>
</tr>
<tr>
    <td><CopyableCode code="tunnel_id" /></td>
    <td><code>string</code></td>
    <td>UUID of the Cloudflare Tunnel to bind to. Mutually exclusive with network_id. (example: abcd1234-5678-90ef-ghij-klmnopqrstuv)</td>
</tr>
<tr>
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for the version to inherit the binding from, which can be the version ID or the literal "latest" to inherit from the latest version. Defaults to inheriting the binding from the latest version. (default: latest, example: 8969331f-7192-434c-9938-6aea24ed58bf)</td>
</tr>
<tr>
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>R2 bucket to bind to. (example: my-r2-bucket)</td>
</tr>
<tr>
    <td><CopyableCode code="class_name" /></td>
    <td><code>string</code></td>
    <td>The exported class name of the Durable Object. (example: MyDurableObject, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="index_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Vectorize index to bind to. (example: my-index-name)</td>
</tr>
<tr>
    <td><CopyableCode code="instance_name" /></td>
    <td><code>string</code></td>
    <td>The user-chosen instance name. Must exist at deploy time. The worker can search, chat, update, and manage items/jobs on this instance. (example: cloudflare-blog)</td>
</tr>
<tr>
    <td><CopyableCode code="old_name" /></td>
    <td><code>string</code></td>
    <td>The old name of the inherited binding. If set, the binding will be renamed from `old_name` to `name` in the new version. If not set, the binding will keep the same name between versions. (example: MY_OLD_BINDING)</td>
</tr>
<tr>
    <td><CopyableCode code="queue_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Queue to bind to. (example: my-queue)</td>
</tr>
<tr>
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The script where the Durable Object is defined, if it is external to this Worker. (example: my-other-worker, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="secret_name" /></td>
    <td><code>string</code></td>
    <td>Name of the secret in the store. (example: my_secret)</td>
</tr>
<tr>
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Workflow to bind to. (example: my-workflow)</td>
</tr>
<tr>
    <td><CopyableCode code="algorithm" /></td>
    <td><code>object</code></td>
    <td>Algorithm-specific key parameters. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm).</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_destination_addresses" /></td>
    <td><code>array</code></td>
    <td>List of allowed destination addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_sender_addresses" /></td>
    <td><code>array</code></td>
    <td>List of allowed sender addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>string</code></td>
    <td>The name of the dataset to bind to. (example: some_dataset)</td>
</tr>
<tr>
    <td><CopyableCode code="destination_address" /></td>
    <td><code>string (email)</code></td>
    <td>Destination address for the email. (example: user@example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="dispatch_namespace" /></td>
    <td><code>string</code></td>
    <td>The dispatch namespace the Durable Object script belongs to. (example: my-dispatch-namespace)</td>
</tr>
<tr>
    <td><CopyableCode code="entrypoint" /></td>
    <td><code>string</code></td>
    <td>Entrypoint to invoke on the target Worker. (example: MyHandler)</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>The environment of the script_name to bind to. (example: production)</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Data format of the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format). (raw, pkcs8, spki, jwk) (example: raw)</td>
</tr>
<tr>
    <td><CopyableCode code="json" /></td>
    <td><code>object</code></td>
    <td>JSON data to use.</td>
</tr>
<tr>
    <td><CopyableCode code="jurisdiction" /></td>
    <td><code>string</code></td>
    <td>The [jurisdiction](https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions) of the R2 bucket. (eu, fedramp, fedramp-high) (example: eu)</td>
</tr>
<tr>
    <td><CopyableCode code="key_base64" /></td>
    <td><code>string</code></td>
    <td>Base64-encoded key data. Required if `format` is "raw", "pkcs8", or "spki".</td>
</tr>
<tr>
    <td><CopyableCode code="key_jwk" /></td>
    <td><code>object</code></td>
    <td>Key data in [JSON Web Key](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key) format. Required if `format` is "jwk".</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace the instance belongs to. Defaults to "default" if omitted. Customers who don't use namespaces can simply omit this field. (example: production)</td>
</tr>
<tr>
    <td><CopyableCode code="outbound" /></td>
    <td><code>object</code></td>
    <td>Outbound worker.</td>
</tr>
<tr>
    <td><CopyableCode code="part" /></td>
    <td><code>string</code></td>
    <td>The name of the file containing the data content. Only accepted for `service worker syntax` Workers. (example: my-module.bin)</td>
</tr>
<tr>
    <td><CopyableCode code="pipeline" /></td>
    <td><code>string</code></td>
    <td>Name of the Pipeline to bind to. (example: my-pipeline)</td>
</tr>
<tr>
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td>Name of Worker to bind to. (example: my-worker)</td>
</tr>
<tr>
    <td><CopyableCode code="simple" /></td>
    <td><code>object</code></td>
    <td>The rate limit configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>The text value to use. (example: Hello, world!)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The kind of resource that the binding provides. (ai)</td>
</tr>
<tr>
    <td><CopyableCode code="usages" /></td>
    <td><code>array</code></td>
    <td>Allowed operations with the key. [Learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages). (x-stainless-collection-type: set)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dispatch_namespace"><code>dispatch_namespace</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Fetch script bindings from a script uploaded to a Workers for Platforms namespace.</td>
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
<tr id="parameter-dispatch_namespace">
    <td><CopyableCode code="dispatch_namespace" /></td>
    <td><code>string</code></td>
    <td>The Workers-for-Platforms dispatch namespace.</td>
</tr>
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
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

Fetch script bindings from a script uploaded to a Workers for Platforms namespace.

```sql
SELECT
id,
name,
app_id,
certificate_id,
database_id,
namespace_id,
network_id,
service_id,
store_id,
tunnel_id,
version_id,
bucket_name,
class_name,
index_name,
instance_name,
old_name,
queue_name,
script_name,
secret_name,
workflow_name,
algorithm,
allowed_destination_addresses,
allowed_sender_addresses,
dataset,
destination_address,
dispatch_namespace,
entrypoint,
environment,
format,
json,
jurisdiction,
key_base64,
key_jwk,
namespace,
outbound,
part,
pipeline,
service,
simple,
text,
type,
usages
FROM cloudflare.workers_for_platforms.bindings
WHERE account_id = '{{ account_id }}' -- required
AND dispatch_namespace = '{{ dispatch_namespace }}' -- required
AND script_name = '{{ script_name }}' -- required
;
```
</TabItem>
</Tabs>
