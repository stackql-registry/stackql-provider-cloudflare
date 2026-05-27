--- 
title: provider_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_configs
  - ai_gateway
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

Creates, updates, deletes, gets or lists a <code>provider_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai_gateway.provider_configs" /></td></tr>
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

List objects

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gateway_id" /></td>
    <td><code>string</code></td>
    <td>gateway id</td>
</tr>
<tr>
    <td><CopyableCode code="secret_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="alias" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="default_config" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provider_slug" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rate_limit_period" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="secret_preview" /></td>
    <td><code>string</code></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all AI Gateway evaluator types configured for the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-provider_slug"><code>provider_slug</code></a>, <a href="#parameter-default_config"><code>default_config</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-secret_id"><code>secret_id</code></a>, <a href="#parameter-secret"><code>secret</code></a></td>
    <td></td>
    <td>Creates a new AI Gateway.</td>
</tr>
<tr>
    <td><a href="#aig_config_update_providers"><CopyableCode code="aig_config_update_providers" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-secret"><code>secret</code></a></td>
    <td></td>
    <td>Updates an existing AI Gateway dataset.</td>
</tr>
<tr>
    <td><a href="#aig_config_delete_providers"><CopyableCode code="aig_config_delete_providers" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>Deletes an AI Gateway dataset.</td>
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
<tr id="parameter-gateway_id">
    <td><CopyableCode code="gateway_id" /></td>
    <td><code>string</code></td>
    <td>The AI Gateway ID.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists all AI Gateway evaluator types configured for the account.

```sql
SELECT
id,
gateway_id,
secret_id,
alias,
default_config,
modified_at,
provider_slug,
rate_limit,
rate_limit_period,
secret_preview
FROM cloudflare.ai_gateway.provider_configs
WHERE account_id = '{{ account_id }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
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

Creates a new AI Gateway.

```sql
INSERT INTO cloudflare.ai_gateway.provider_configs (
alias,
default_config,
provider_slug,
rate_limit,
rate_limit_period,
secret,
secret_id,
account_id,
gateway_id
)
SELECT 
'{{ alias }}' /* required */,
{{ default_config }} /* required */,
'{{ provider_slug }}' /* required */,
{{ rate_limit }},
{{ rate_limit_period }},
'{{ secret }}' /* required */,
'{{ secret_id }}' /* required */,
'{{ account_id }}',
'{{ gateway_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: provider_configs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the provider_configs resource.
    - name: gateway_id
      value: "{{ gateway_id }}"
      description: Required parameter for the provider_configs resource.
    - name: alias
      value: "{{ alias }}"
    - name: default_config
      value: {{ default_config }}
    - name: provider_slug
      value: "{{ provider_slug }}"
    - name: rate_limit
      value: {{ rate_limit }}
    - name: rate_limit_period
      value: {{ rate_limit_period }}
      default: 60
    - name: secret
      value: "{{ secret }}"
    - name: secret_id
      value: "{{ secret_id }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="aig_config_update_providers"
    values={[
        { label: 'aig_config_update_providers', value: 'aig_config_update_providers' }
    ]}
>
<TabItem value="aig_config_update_providers">

Updates an existing AI Gateway dataset.

```sql
REPLACE cloudflare.ai_gateway.provider_configs
SET 
secret = '{{ secret }}'
WHERE 
account_id = '{{ account_id }}' --required
AND gateway_id = '{{ gateway_id }}' --required
AND id = '{{ id }}' --required
AND secret = '{{ secret }}' --required
RETURNING
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="aig_config_delete_providers"
    values={[
        { label: 'aig_config_delete_providers', value: 'aig_config_delete_providers' }
    ]}
>
<TabItem value="aig_config_delete_providers">

Deletes an AI Gateway dataset.

```sql
DELETE FROM cloudflare.ai_gateway.provider_configs
WHERE account_id = '{{ account_id }}' --required
AND gateway_id = '{{ gateway_id }}' --required
AND id = '{{ id }}' --required
;
```
</TabItem>
</Tabs>
