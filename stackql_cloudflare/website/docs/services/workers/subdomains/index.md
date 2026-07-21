--- 
title: subdomains
hide_title: false
hide_table_of_contents: false
keywords:
  - subdomains
  - workers
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

Creates, updates, deletes, gets or lists a <code>subdomains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subdomains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.workers.subdomains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_script_subdomain"
    values={[
        { label: 'get_script_subdomain', value: 'get_script_subdomain' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_script_subdomain">

Get subdomain response.

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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Worker is available on the workers.dev subdomain.</td>
</tr>
<tr>
    <td><CopyableCode code="previews_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the Worker's Preview URLs are available on the workers.dev subdomain. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get Subdomain response.

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
    <td><CopyableCode code="subdomain" /></td>
    <td><code>string</code></td>
    <td> (example: my-subdomain)</td>
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
    <td><a href="#get_script_subdomain"><CopyableCode code="get_script_subdomain" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Get if the Worker is available on the workers.dev subdomain.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns a Workers subdomain for an account.</td>
</tr>
<tr>
    <td><a href="#create_script_subdomain"><CopyableCode code="create_script_subdomain" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a>, <a href="#parameter-enabled"><code>enabled</code></a></td>
    <td></td>
    <td>Enable or disable the Worker on the workers.dev subdomain.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-subdomain"><code>subdomain</code></a></td>
    <td></td>
    <td>Creates a Workers subdomain for an account.</td>
</tr>
<tr>
    <td><a href="#delete_script_subdomain"><CopyableCode code="delete_script_subdomain" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-script_name"><code>script_name</code></a></td>
    <td></td>
    <td>Disable all workers.dev subdomains for a Worker.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a Workers subdomain for an account.</td>
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
<tr id="parameter-script_name">
    <td><CopyableCode code="script_name" /></td>
    <td><code>string</code></td>
    <td>The Worker script name.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_script_subdomain"
    values={[
        { label: 'get_script_subdomain', value: 'get_script_subdomain' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_script_subdomain">

Get if the Worker is available on the workers.dev subdomain.

```sql
SELECT
enabled,
previews_enabled
FROM cloudflare.workers.subdomains
WHERE account_id = '{{ account_id }}' -- required
AND script_name = '{{ script_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a Workers subdomain for an account.

```sql
SELECT
subdomain
FROM cloudflare.workers.subdomains
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_script_subdomain"
    values={[
        { label: 'create_script_subdomain', value: 'create_script_subdomain' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_script_subdomain">

Enable or disable the Worker on the workers.dev subdomain.

```sql
INSERT INTO cloudflare.workers.subdomains (
enabled,
previews_enabled,
account_id,
script_name
)
SELECT 
{{ enabled }} /* required */,
{{ previews_enabled }},
'{{ account_id }}',
'{{ script_name }}'
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
- name: subdomains
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the subdomains resource.
    - name: script_name
      value: "{{ script_name }}"
      description: Required parameter for the subdomains resource.
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether the Worker should be available on the workers.dev subdomain.
    - name: previews_enabled
      value: {{ previews_enabled }}
      description: |
        Whether the Worker's Preview URLs should be available on the workers.dev subdomain.
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

Creates a Workers subdomain for an account.

```sql
REPLACE cloudflare.workers.subdomains
SET 
subdomain = '{{ subdomain }}'
WHERE 
account_id = '{{ account_id }}' --required
AND subdomain = '{{ subdomain }}' --required
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
    defaultValue="delete_script_subdomain"
    values={[
        { label: 'delete_script_subdomain', value: 'delete_script_subdomain' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_script_subdomain">

Disable all workers.dev subdomains for a Worker.

```sql
DELETE FROM cloudflare.workers.subdomains
WHERE account_id = '{{ account_id }}' --required
AND script_name = '{{ script_name }}' --required
;
```
</TabItem>
<TabItem value="delete">

Deletes a Workers subdomain for an account.

```sql
DELETE FROM cloudflare.workers.subdomains
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
