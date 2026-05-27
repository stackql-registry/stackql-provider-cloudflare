--- 
title: document_fingerprints
hide_title: false
hide_table_of_contents: false
keywords:
  - document_fingerprints
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

Creates, updates, deletes, gets or lists a <code>document_fingerprints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="document_fingerprints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.document_fingerprints" /></td></tr>
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

Document fingerprint read was successful.

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
    <td><CopyableCode code="entry_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
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
    <td> (default: )</td>
</tr>
<tr>
    <td><CopyableCode code="match_percent" /></td>
    <td><code>integer (int32)</code></td>
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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer (int64)</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Document fingerprint read was successful.

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
    <td><CopyableCode code="entry_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
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
    <td> (default: )</td>
</tr>
<tr>
    <td><CopyableCode code="match_percent" /></td>
    <td><code>integer (int32)</code></td>
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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer (int64)</code></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-document_fingerprint_id"><code>document_fingerprint_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all document fingerprints configured for DLP scanning in the account.</td>
</tr>
<tr>
    <td><a href="#dlp_document_fingerprints_update"><CopyableCode code="dlp_document_fingerprints_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-document_fingerprint_id"><code>document_fingerprint_id</code></a></td>
    <td></td>
    <td>Updates metadata for an existing document fingerprint, such as its name or description.</td>
</tr>
<tr>
    <td><a href="#dlp_document_fingerprints_create"><CopyableCode code="dlp_document_fingerprints_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-match_percent"><code>match_percent</code></a></td>
    <td></td>
    <td>Creates a new document fingerprint for DLP scanning. Document fingerprints detect documents that are structurally similar to the uploaded sample.</td>
</tr>
<tr>
    <td><a href="#dlp_document_fingerprints_upload"><CopyableCode code="dlp_document_fingerprints_upload" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-document_fingerprint_id"><code>document_fingerprint_id</code></a>, <a href="#parameter-file"><code>file</code></a></td>
    <td></td>
    <td>Uploads a new document to create or update a fingerprint. The document structure is analyzed to enable detection of similar documents.</td>
</tr>
<tr>
    <td><a href="#dlp_document_fingerprints_delete"><CopyableCode code="dlp_document_fingerprints_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-document_fingerprint_id"><code>document_fingerprint_id</code></a></td>
    <td></td>
    <td>Removes a document fingerprint from DLP configuration. Documents matching this fingerprint will no longer be detected.</td>
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
<tr id="parameter-document_fingerprint_id">
    <td><CopyableCode code="document_fingerprint_id" /></td>
    <td><code>string (uuid)</code></td>
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

Document fingerprint read was successful.

```sql
SELECT
id,
name,
entry_id,
file_name,
created_at,
description,
match_percent,
status,
updated_at,
version
FROM cloudflare.zero_trust.document_fingerprints
WHERE account_id = '{{ account_id }}' -- required
AND document_fingerprint_id = '{{ document_fingerprint_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all document fingerprints configured for DLP scanning in the account.

```sql
SELECT
id,
name,
entry_id,
file_name,
created_at,
description,
match_percent,
status,
updated_at,
version
FROM cloudflare.zero_trust.document_fingerprints
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="dlp_document_fingerprints_update"
    values={[
        { label: 'dlp_document_fingerprints_update', value: 'dlp_document_fingerprints_update' },
        { label: 'dlp_document_fingerprints_create', value: 'dlp_document_fingerprints_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="dlp_document_fingerprints_update">

Updates metadata for an existing document fingerprint, such as its name or description.

```sql
INSERT INTO cloudflare.zero_trust.document_fingerprints (
description,
match_percent,
name,
account_id,
document_fingerprint_id
)
SELECT 
'{{ description }}',
{{ match_percent }},
'{{ name }}',
'{{ account_id }}',
'{{ document_fingerprint_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="dlp_document_fingerprints_create">

Creates a new document fingerprint for DLP scanning. Document fingerprints detect documents that are structurally similar to the uploaded sample.

```sql
INSERT INTO cloudflare.zero_trust.document_fingerprints (
description,
match_percent,
name,
account_id
)
SELECT 
'{{ description }}',
{{ match_percent }} /* required */,
'{{ name }}' /* required */,
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
- name: document_fingerprints
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the document_fingerprints resource.
    - name: document_fingerprint_id
      value: "{{ document_fingerprint_id }}"
      description: Required parameter for the document_fingerprints resource.
    - name: description
      value: "{{ description }}"
      default: 
    - name: match_percent
      value: {{ match_percent }}
    - name: name
      value: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="dlp_document_fingerprints_upload"
    values={[
        { label: 'dlp_document_fingerprints_upload', value: 'dlp_document_fingerprints_upload' }
    ]}
>
<TabItem value="dlp_document_fingerprints_upload">

Uploads a new document to create or update a fingerprint. The document structure is analyzed to enable detection of similar documents.

```sql
REPLACE cloudflare.zero_trust.document_fingerprints
SET 
file = '{{ file }}'
WHERE 
account_id = '{{ account_id }}' --required
AND document_fingerprint_id = '{{ document_fingerprint_id }}' --required
AND file = '{{ file }}' --required
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
    defaultValue="dlp_document_fingerprints_delete"
    values={[
        { label: 'dlp_document_fingerprints_delete', value: 'dlp_document_fingerprints_delete' }
    ]}
>
<TabItem value="dlp_document_fingerprints_delete">

Removes a document fingerprint from DLP configuration. Documents matching this fingerprint will no longer be detected.

```sql
DELETE FROM cloudflare.zero_trust.document_fingerprints
WHERE account_id = '{{ account_id }}' --required
AND document_fingerprint_id = '{{ document_fingerprint_id }}' --required
;
```
</TabItem>
</Tabs>
