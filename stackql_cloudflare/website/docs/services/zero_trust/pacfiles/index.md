--- 
title: pacfiles
hide_title: false
hide_table_of_contents: false
keywords:
  - pacfiles
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

Creates, updates, deletes, gets or lists a <code>pacfiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="pacfiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.pacfiles" /></td></tr>
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

Returns a PAC file response.

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
    <td> (example: ed35569b41ce4d1facfe683550f54086)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the PAC file. (example: Devops team)</td>
</tr>
<tr>
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
    <td>Actual contents of the PAC file (example: function FindProxyForURL(url, host) &#123; return "DIRECT"; &#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the PAC file. (example: PAC file for Devops team)</td>
</tr>
<tr>
    <td><CopyableCode code="slug" /></td>
    <td><code>string</code></td>
    <td>URL-friendly version of the PAC file name. (example: pac_devops)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Unique URL to download the PAC file. (example: https://pac.cloudflare-gateway.com/699d98642c564d2e855e9661899b7252/pac_devops)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Returns a list of PAC files response.

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
    <td> (example: ed35569b41ce4d1facfe683550f54086)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the PAC file. (example: Devops team)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the PAC file. (example: PAC file for Devops team)</td>
</tr>
<tr>
    <td><CopyableCode code="slug" /></td>
    <td><code>string</code></td>
    <td>URL-friendly version of the PAC file name. (example: pac_devops)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Unique URL to download the PAC file. (example: https://pac.cloudflare-gateway.com/699d98642c564d2e855e9661899b7252/pac_devops)</td>
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
    <td><a href="#parameter-pacfile_id"><code>pacfile_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get a single Zero Trust Gateway PAC file.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all Zero Trust Gateway PAC files for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-contents"><code>contents</code></a></td>
    <td></td>
    <td>Create a new Zero Trust Gateway PAC file.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-pacfile_id"><code>pacfile_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-contents"><code>contents</code></a></td>
    <td></td>
    <td>Update a configured Zero Trust Gateway PAC file.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-pacfile_id"><code>pacfile_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a configured Zero Trust Gateway PAC file.</td>
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
<tr id="parameter-pacfile_id">
    <td><CopyableCode code="pacfile_id" /></td>
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

Get a single Zero Trust Gateway PAC file.

```sql
SELECT
id,
name,
contents,
created_at,
description,
slug,
updated_at,
url
FROM cloudflare.zero_trust.pacfiles
WHERE pacfile_id = '{{ pacfile_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Zero Trust Gateway PAC files for an account.

```sql
SELECT
id,
name,
created_at,
description,
slug,
updated_at,
url
FROM cloudflare.zero_trust.pacfiles
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

Create a new Zero Trust Gateway PAC file.

```sql
INSERT INTO cloudflare.zero_trust.pacfiles (
contents,
description,
name,
slug,
account_id
)
SELECT 
'{{ contents }}' /* required */,
'{{ description }}',
'{{ name }}' /* required */,
'{{ slug }}',
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
- name: pacfiles
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the pacfiles resource.
    - name: contents
      value: "{{ contents }}"
      description: |
        Actual contents of the PAC file
    - name: description
      value: "{{ description }}"
      description: |
        Detailed description of the PAC file.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the PAC file.
    - name: slug
      value: "{{ slug }}"
      description: |
        URL-friendly version of the PAC file name. If not provided, it will be auto-generated
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

Update a configured Zero Trust Gateway PAC file.

```sql
REPLACE cloudflare.zero_trust.pacfiles
SET 
contents = '{{ contents }}',
description = '{{ description }}',
name = '{{ name }}'
WHERE 
pacfile_id = '{{ pacfile_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND description = '{{ description }}' --required
AND contents = '{{ contents }}' --required
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

Delete a configured Zero Trust Gateway PAC file.

```sql
DELETE FROM cloudflare.zero_trust.pacfiles
WHERE pacfile_id = '{{ pacfile_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
