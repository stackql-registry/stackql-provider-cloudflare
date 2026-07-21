--- 
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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

Creates, updates, deletes, gets or lists a <code>datasets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="datasets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.datasets" /></td></tr>
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

Dataset read successfully.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="case_sensitive" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="encoding_version" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_cells" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="secret" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (empty, uploading, pending, processing, failed, complete)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Stores when the dataset was last updated. This includes name or description changes as well as uploads.</td>
</tr>
<tr>
    <td><CopyableCode code="uploads" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Datasets read successfully.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="case_sensitive" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the dataset.</td>
</tr>
<tr>
    <td><CopyableCode code="encoding_version" /></td>
    <td><code>integer (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="num_cells" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="secret" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (empty, uploading, pending, processing, failed, complete)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Stores when the dataset was last updated. This includes name or description changes as well as uploads.</td>
</tr>
<tr>
    <td><CopyableCode code="uploads" /></td>
    <td><code>array</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all DLP datasets configured for the account, including custom word lists and EDM datasets.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new DLP (Data Loss Prevention) dataset for storing custom detection patterns. Datasets can contain exact match data, word lists, or EDM (Exact Data Match) configurations.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td>Updates the configuration of an existing DLP dataset, such as its name, description, or detection settings.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td>This deletes all versions of the dataset.</td>
</tr>
<tr>
    <td><a href="#upload_version"><CopyableCode code="upload_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td>Creates a new version of a DLP dataset, allowing you to stage changes before activation. Used for single-column EDM and custom word lists.</td>
</tr>
<tr>
    <td><a href="#upload_version_data"><CopyableCode code="upload_version_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-version"><code>version</code></a></td>
    <td></td>
    <td>This is used for single-column EDMv1 and Custom Word Lists. The EDM format can only be created in the Cloudflare dashboard. For other clients, this operation can only be used for non-secret Custom Word Lists. The body must be a UTF-8 encoded, newline (NL or CRNL) separated list of words to be matched.</td>
</tr>
<tr>
    <td><a href="#dlp_datasets_define_columns"><CopyableCode code="dlp_datasets_define_columns" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-version"><code>version</code></a></td>
    <td></td>
    <td>This is used for multi-column EDMv2 datasets. The EDMv2 format can only be created in the Cloudflare dashboard. The columns in the response appear in the same order as in the request.</td>
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
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>integer (int64)</code></td>
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

Dataset read successfully.

```sql
SELECT
id,
name,
case_sensitive,
columns,
created_at,
description,
encoding_version,
num_cells,
secret,
status,
updated_at,
uploads
FROM cloudflare.zero_trust.datasets
WHERE account_id = '{{ account_id }}' -- required
AND dataset_id = '{{ dataset_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all DLP datasets configured for the account, including custom word lists and EDM datasets.

```sql
SELECT
id,
name,
case_sensitive,
columns,
created_at,
description,
encoding_version,
num_cells,
secret,
status,
updated_at,
uploads
FROM cloudflare.zero_trust.datasets
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

Creates a new DLP (Data Loss Prevention) dataset for storing custom detection patterns. Datasets can contain exact match data, word lists, or EDM (Exact Data Match) configurations.

```sql
INSERT INTO cloudflare.zero_trust.datasets (
case_sensitive,
description,
encoding_version,
name,
secret,
account_id
)
SELECT 
{{ case_sensitive }},
'{{ description }}',
{{ encoding_version }},
'{{ name }}' /* required */,
{{ secret }},
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
- name: datasets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the datasets resource.
    - name: case_sensitive
      value: {{ case_sensitive }}
      description: |
        Only applies to custom word lists. Determines if the words should be matched in a case-sensitive manner Cannot be set to false if \`secret\` is true or undefined
    - name: description
      value: "{{ description }}"
      description: |
        The description of the dataset.
    - name: encoding_version
      value: {{ encoding_version }}
      description: |
        Dataset encoding version Non-secret custom word lists with no header are always version 1. Secret EDM lists with no header are version 1. Multicolumn CSV with headers are version 2. Omitting this field provides the default value 0, which is interpreted the same as 1.
    - name: name
      value: "{{ name }}"
    - name: secret
      value: {{ secret }}
      description: |
        Generate a secret dataset. If true, the response will include a secret to use with the EDM encoder. If false, the response has no secret and the dataset is uploaded in plaintext.
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

Updates the configuration of an existing DLP dataset, such as its name, description, or detection settings.

```sql
REPLACE cloudflare.zero_trust.datasets
SET 
case_sensitive = {{ case_sensitive }},
description = '{{ description }}',
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
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

This deletes all versions of the dataset.

```sql
DELETE FROM cloudflare.zero_trust.datasets
WHERE account_id = '{{ account_id }}' --required
AND dataset_id = '{{ dataset_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upload_version"
    values={[
        { label: 'upload_version', value: 'upload_version' },
        { label: 'upload_version_data', value: 'upload_version_data' },
        { label: 'dlp_datasets_define_columns', value: 'dlp_datasets_define_columns' }
    ]}
>
<TabItem value="upload_version">

Creates a new version of a DLP dataset, allowing you to stage changes before activation. Used for single-column EDM and custom word lists.

```sql
EXEC cloudflare.zero_trust.datasets.upload_version 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required
;
```
</TabItem>
<TabItem value="upload_version_data">

This is used for single-column EDMv1 and Custom Word Lists. The EDM format can only be created in the Cloudflare dashboard. For other clients, this operation can only be used for non-secret Custom Word Lists. The body must be a UTF-8 encoded, newline (NL or CRNL) separated list of words to be matched.

```sql
EXEC cloudflare.zero_trust.datasets.upload_version_data 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required, 
@version='{{ version }}' --required
;
```
</TabItem>
<TabItem value="dlp_datasets_define_columns">

This is used for multi-column EDMv2 datasets. The EDMv2 format can only be created in the Cloudflare dashboard. The columns in the response appear in the same order as in the request.

```sql
EXEC cloudflare.zero_trust.datasets.dlp_datasets_define_columns 
@account_id='{{ account_id }}' --required, 
@dataset_id='{{ dataset_id }}' --required, 
@version='{{ version }}' --required
;
```
</TabItem>
</Tabs>
