--- 
title: deployment_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_groups
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

Creates, updates, deletes, gets or lists a <code>deployment_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.deployment_groups" /></td></tr>
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

Gets deployment group response.

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
    <td>The ID of the deployment group. (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the deployment group. (example: Engineering Ring 0)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the deployment group was created. (example: 2026-02-14T13:17:00.123456789Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_ids" /></td>
    <td><code>array</code></td>
    <td>Contains a list of policy IDs assigned to this deployment group.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the deployment group was last updated. (example: 2026-02-14T13:17:00.123456789Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version_config" /></td>
    <td><code>array</code></td>
    <td>Contains version configurations for different target environments.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Lists deployment group response.

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
    <td>The ID of the deployment group. (example: 550e8400-e29b-41d4-a716-446655440000)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A user-friendly name for the deployment group. (example: Engineering Ring 0)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the deployment group was created. (example: 2026-02-14T13:17:00.123456789Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policy_ids" /></td>
    <td><code>array</code></td>
    <td>Contains a list of policy IDs assigned to this deployment group.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string</code></td>
    <td>The RFC3339Nano timestamp when the deployment group was last updated. (example: 2026-02-14T13:17:00.123456789Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version_config" /></td>
    <td><code>array</code></td>
    <td>Contains version configurations for different target environments.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Fetches a single deployment group by its ID. This endpoint is in Beta.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all deployment groups for an account. Use deployment groups to assign target WARP client versions to specific devices. This endpoint is in Beta.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-version_config"><code>version_config</code></a></td>
    <td></td>
    <td>Creates a new deployment group. Policy IDs must be unique across all deployment groups. This endpoint is in Beta.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Updates a deployment group. Returns 409 if any newly added policy IDs already belong to another deployment group. This endpoint is in Beta.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Deletes a deployment group. Associated policies no longer apply and devices stop receiving version targets. This endpoint is in Beta.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The Access group ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>The page number to return.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of deployment groups to return per page.</td>
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

Fetches a single deployment group by its ID. This endpoint is in Beta.

```sql
SELECT
id,
name,
created_at,
policy_ids,
updated_at,
version_config
FROM cloudflare.zero_trust.deployment_groups
WHERE account_id = '{{ account_id }}' -- required
AND group_id = '{{ group_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all deployment groups for an account. Use deployment groups to assign target WARP client versions to specific devices. This endpoint is in Beta.

```sql
SELECT
id,
name,
created_at,
policy_ids,
updated_at,
version_config
FROM cloudflare.zero_trust.deployment_groups
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Creates a new deployment group. Policy IDs must be unique across all deployment groups. This endpoint is in Beta.

```sql
INSERT INTO cloudflare.zero_trust.deployment_groups (
name,
policy_ids,
version_config,
account_id
)
SELECT 
'{{ name }}' /* required */,
'{{ policy_ids }}',
'{{ version_config }}' /* required */,
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
- name: deployment_groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the deployment_groups resource.
    - name: name
      value: "{{ name }}"
      description: |
        A user-friendly name for the deployment group.
    - name: policy_ids
      value:
        - "{{ policy_ids }}"
      description: |
        Contains an optional list of policy IDs assigned to a group.
    - name: version_config
      description: |
        Contains at least one version configuration.
      value:
        - target_environment: "{{ target_environment }}"
          version: "{{ version }}"
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

Updates a deployment group. Returns 409 if any newly added policy IDs already belong to another deployment group. This endpoint is in Beta.

```sql
UPDATE cloudflare.zero_trust.deployment_groups
SET 
name = '{{ name }}',
policy_ids = '{{ policy_ids }}',
version_config = '{{ version_config }}'
WHERE 
account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
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

Deletes a deployment group. Associated policies no longer apply and devices stop receiving version targets. This endpoint is in Beta.

```sql
DELETE FROM cloudflare.zero_trust.deployment_groups
WHERE account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
;
```
</TabItem>
</Tabs>
