--- 
title: accounts_logs_explorer_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_logs_explorer_datasets
  - logs
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

Creates, updates, deletes, gets or lists an <code>accounts_logs_explorer_datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts_logs_explorer_datasets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logs.accounts_logs_explorer_datasets" /></td></tr>
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

Dataset details, including the fields active for ingestion.

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
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>Unique dataset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td>Public ID of the account or zone that owns this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>RFC3339 timestamp recording when the API created this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>string</code></td>
    <td>Dataset type name (e.g. `http_requests`).</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether log ingest is currently active for this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="fields" /></td>
    <td><code>array</code></td>
    <td>The field configuration for this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>Whether this dataset belongs to an account or a zone. (account, zone)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>RFC3339 timestamp recording when the API last updated this dataset.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

The datasets the account or zone has configured.

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
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>Unique dataset ID.</td>
</tr>
<tr>
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td>Public ID of the account or zone that owns this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>RFC3339 timestamp recording when the API created this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>string</code></td>
    <td>Dataset type name (e.g. `http_requests`).</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether log ingest is currently active for this dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>Whether this dataset belongs to an account or a zone. (account, zone)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>RFC3339 timestamp recording when the API last updated this dataset.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td>Retrieve a single Log Explorer dataset by ID for the account or zone.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-include_zones"><code>include_zones</code></a></td>
    <td>Returns all Log Explorer datasets configured for the account or zone. Pass `include_zones=true` to also include zone-level datasets that belong to this account or zone. List responses omit the `fields` property; use the single-dataset endpoint to retrieve field configuration.</td>
</tr>
<tr>
    <td><a href="#post_accounts_account_id_logs_explorer_datasets"><CopyableCode code="post_accounts_account_id_logs_explorer_datasets" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset"><code>dataset</code></a></td>
    <td></td>
    <td>Create a new Log Explorer dataset for the account or zone. Use the `/account or zones/&#123;account or zone_id&#125;/logs/explorer/datasets/available` endpoint to list dataset types you can create along with their available fields. The `fields` property is optional. If not specified, all available fields will be enabled.</td>
</tr>
<tr>
    <td><a href="#put_accounts_account_id_logs_explorer_datasets_dataset_id"><CopyableCode code="put_accounts_account_id_logs_explorer_datasets_dataset_id" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Updates the enabled state and/or field configuration of an account or zone dataset.</td>
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
<tr id="parameter-dataset_id">
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>The dataset ID.</td>
</tr>
<tr id="parameter-include_zones">
    <td><CopyableCode code="include_zones" /></td>
    <td><code>boolean</code></td>
    <td>Set to true to include zone-scoped datasets belonging to this account.</td>
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

Retrieve a single Log Explorer dataset by ID for the account or zone.

```sql
SELECT
dataset_id,
object_id,
created_at,
dataset,
enabled,
fields,
object_type,
updated_at
FROM cloudflare.logs.accounts_logs_explorer_datasets
WHERE account_id = '{{ account_id }}' -- required
AND dataset_id = '{{ dataset_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns all Log Explorer datasets configured for the account or zone. Pass `include_zones=true` to also include zone-level datasets that belong to this account or zone. List responses omit the `fields` property; use the single-dataset endpoint to retrieve field configuration.

```sql
SELECT
dataset_id,
object_id,
created_at,
dataset,
enabled,
object_type,
updated_at
FROM cloudflare.logs.accounts_logs_explorer_datasets
WHERE account_id = '{{ account_id }}' -- required
AND include_zones = '{{ include_zones }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_accounts_account_id_logs_explorer_datasets"
    values={[
        { label: 'post_accounts_account_id_logs_explorer_datasets', value: 'post_accounts_account_id_logs_explorer_datasets' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_accounts_account_id_logs_explorer_datasets">

Create a new Log Explorer dataset for the account or zone. Use the `/account or zones/&#123;account or zone_id&#125;/logs/explorer/datasets/available` endpoint to list dataset types you can create along with their available fields. The `fields` property is optional. If not specified, all available fields will be enabled.

```sql
INSERT INTO cloudflare.logs.accounts_logs_explorer_datasets (
dataset,
fields,
account_id
)
SELECT 
'{{ dataset }}' /* required */,
'{{ fields }}',
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
- name: accounts_logs_explorer_datasets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the accounts_logs_explorer_datasets resource.
    - name: dataset
      value: "{{ dataset }}"
      description: |
        Dataset type name to create (e.g. \`http_requests\`).
    - name: fields
      description: |
        Controls which fields the API ingests. Defaults to all available fields when absent.
      value:
        - enabled: {{ enabled }}
          name: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_accounts_account_id_logs_explorer_datasets_dataset_id"
    values={[
        { label: 'put_accounts_account_id_logs_explorer_datasets_dataset_id', value: 'put_accounts_account_id_logs_explorer_datasets_dataset_id' }
    ]}
>
<TabItem value="put_accounts_account_id_logs_explorer_datasets_dataset_id">

Updates the enabled state and/or field configuration of an account or zone dataset.

```sql
REPLACE cloudflare.logs.accounts_logs_explorer_datasets
SET 
enabled = {{ enabled }},
fields = '{{ fields }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
AND enabled = {{ enabled }} --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
