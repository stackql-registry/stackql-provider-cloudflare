--- 
title: cloud_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_providers
  - magic_cloud_networking
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

Creates, updates, deletes, gets or lists a <code>cloud_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_cloud_networking.cloud_providers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

OK.

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
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="azure_subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="azure_tenant_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gcp_project_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="friendly_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="aws_arn" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloud_type" /></td>
    <td><code>string</code></td>
    <td> (AWS, AZURE, GOOGLE, CLOUDFLARE)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gcp_service_account_email" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lifecycle_state" /></td>
    <td><code>string</code></td>
    <td> (ACTIVE, PENDING_SETUP, RETIRED)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td> (UNSPECIFIED, PENDING, DISCOVERING, FAILED, SUCCEEDED)</td>
</tr>
<tr>
    <td><CopyableCode code="state_v2" /></td>
    <td><code>string</code></td>
    <td> (UNSPECIFIED, PENDING, DISCOVERING, FAILED, SUCCEEDED)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td></td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-desc"><code>desc</code></a>, <a href="#parameter-cloudflare"><code>cloudflare</code></a></td>
    <td>List Cloud Integrations (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-friendly_name"><code>friendly_name</code></a>, <a href="#parameter-cloud_type"><code>cloud_type</code></a></td>
    <td><a href="#parameter-forwarded"><code>forwarded</code></a></td>
    <td>Create a new Cloud Integration (Closed Beta).</td>
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
<tr id="parameter-cloudflare">
    <td><CopyableCode code="cloudflare" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-desc">
    <td><CopyableCode code="desc" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-forwarded">
    <td><CopyableCode code="forwarded" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>One of ["updated_at", "id", "cloud_type", "name"].</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="list_by_account">

List Cloud Integrations (Closed Beta).

```sql
SELECT
id,
azure_subscription_id,
azure_tenant_id,
gcp_project_id,
friendly_name,
aws_arn,
cloud_type,
description,
gcp_service_account_email,
last_updated,
lifecycle_state,
state,
state_v2,
status
FROM cloudflare.magic_cloud_networking.cloud_providers
WHERE account_id = '{{ account_id }}' -- required
AND status = '{{ status }}'
AND order_by = '{{ order_by }}'
AND desc = '{{ desc }}'
AND cloudflare = '{{ cloudflare }}'
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

Create a new Cloud Integration (Closed Beta).

```sql
INSERT INTO cloudflare.magic_cloud_networking.cloud_providers (
cloud_type,
description,
friendly_name,
account_id,
forwarded
)
SELECT 
'{{ cloud_type }}' /* required */,
'{{ description }}',
'{{ friendly_name }}' /* required */,
'{{ account_id }}',
'{{ forwarded }}'
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
- name: cloud_providers
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the cloud_providers resource.
    - name: cloud_type
      value: "{{ cloud_type }}"
      valid_values: ['AWS', 'AZURE', 'GOOGLE', 'CLOUDFLARE']
    - name: description
      value: "{{ description }}"
    - name: friendly_name
      value: "{{ friendly_name }}"
    - name: forwarded
      value: "{{ forwarded }}"
`}</CodeBlock>

</TabItem>
</Tabs>
