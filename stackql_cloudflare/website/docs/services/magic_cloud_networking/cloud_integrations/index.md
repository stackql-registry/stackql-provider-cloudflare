--- 
title: cloud_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_integrations
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

Creates, updates, deletes, gets or lists a <code>cloud_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cloud_integrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_cloud_networking.cloud_integrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a></td>
    <td><a href="#parameter-status"><code>status</code></a></td>
    <td>Read a Cloud Integration (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#discover"><CopyableCode code="discover" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a></td>
    <td><a href="#parameter-v2"><code>v2</code></a></td>
    <td>Run discovery for a Cloud Integration (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a></td>
    <td></td>
    <td>Update a Cloud Integration (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a></td>
    <td></td>
    <td>Update a Cloud Integration (Closed Beta).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-provider_id"><code>provider_id</code></a></td>
    <td></td>
    <td>Delete a Cloud Integration (Closed Beta).</td>
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
<tr id="parameter-provider_id">
    <td><CopyableCode code="provider_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-v2">
    <td><CopyableCode code="v2" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Read a Cloud Integration (Closed Beta).

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
FROM cloudflare.magic_cloud_networking.cloud_integrations
WHERE account_id = '{{ account_id }}' -- required
AND provider_id = '{{ provider_id }}' -- required
AND status = '{{ status }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="discover"
    values={[
        { label: 'discover', value: 'discover' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="discover">

Run discovery for a Cloud Integration (Closed Beta).

```sql
INSERT INTO cloudflare.magic_cloud_networking.cloud_integrations (
account_id,
provider_id,
v2
)
SELECT 
'{{ account_id }}',
'{{ provider_id }}',
'{{ v2 }}'
RETURNING
errors,
messages,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cloud_integrations
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the cloud_integrations resource.
    - name: provider_id
      value: "{{ provider_id }}"
      description: Required parameter for the cloud_integrations resource.
    - name: v2
      value: {{ v2 }}
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

Update a Cloud Integration (Closed Beta).

```sql
UPDATE cloudflare.magic_cloud_networking.cloud_integrations
SET 
aws_arn = '{{ aws_arn }}',
azure_subscription_id = '{{ azure_subscription_id }}',
azure_tenant_id = '{{ azure_tenant_id }}',
description = '{{ description }}',
friendly_name = '{{ friendly_name }}',
gcp_project_id = '{{ gcp_project_id }}',
gcp_service_account_email = '{{ gcp_service_account_email }}'
WHERE 
account_id = '{{ account_id }}' --required
AND provider_id = '{{ provider_id }}' --required
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

Update a Cloud Integration (Closed Beta).

```sql
REPLACE cloudflare.magic_cloud_networking.cloud_integrations
SET 
aws_arn = '{{ aws_arn }}',
azure_subscription_id = '{{ azure_subscription_id }}',
azure_tenant_id = '{{ azure_tenant_id }}',
description = '{{ description }}',
friendly_name = '{{ friendly_name }}',
gcp_project_id = '{{ gcp_project_id }}',
gcp_service_account_email = '{{ gcp_service_account_email }}'
WHERE 
account_id = '{{ account_id }}' --required
AND provider_id = '{{ provider_id }}' --required
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

Delete a Cloud Integration (Closed Beta).

```sql
DELETE FROM cloudflare.magic_cloud_networking.cloud_integrations
WHERE account_id = '{{ account_id }}' --required
AND provider_id = '{{ provider_id }}' --required
;
```
</TabItem>
</Tabs>
