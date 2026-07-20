--- 
title: upload
hide_title: false
hide_table_of_contents: false
keywords:
  - upload
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

Creates, updates, deletes, gets or lists a <code>upload</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="upload" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.upload" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-version"><code>version</code></a></td>
    <td></td>
    <td>This is used for single-column EDMv1 and Custom Word Lists. The EDM format can only be created in the Cloudflare dashboard. For other clients, this operation can only be used for non-secret Custom Word Lists. The body must be a UTF-8 encoded, newline (NL or CRNL) separated list of words to be matched.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-dataset_id"><code>dataset_id</code></a></td>
    <td></td>
    <td>Creates a new version of a DLP dataset, allowing you to stage changes before activation. Used for single-column EDM and custom word lists.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="edit">

This is used for single-column EDMv1 and Custom Word Lists. The EDM format can only be created in the Cloudflare dashboard. For other clients, this operation can only be used for non-secret Custom Word Lists. The body must be a UTF-8 encoded, newline (NL or CRNL) separated list of words to be matched.

```sql
INSERT INTO cloudflare.zero_trust.upload (
data__value,
account_id,
dataset_id,
version
)
SELECT 
'{{ value }}' /* required */,
'{{ account_id }}',
'{{ dataset_id }}',
'{{ version }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="create">

Creates a new version of a DLP dataset, allowing you to stage changes before activation. Used for single-column EDM and custom word lists.

```sql
INSERT INTO cloudflare.zero_trust.upload (
account_id,
dataset_id
)
SELECT 
'{{ account_id }}',
'{{ dataset_id }}'
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
- name: upload
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the upload resource.
    - name: dataset_id
      value: "{{ dataset_id }}"
      description: Required parameter for the upload resource.
    - name: version
      value: "{{ version }}"
      description: Required parameter for the upload resource.
`}</CodeBlock>

</TabItem>
</Tabs>
