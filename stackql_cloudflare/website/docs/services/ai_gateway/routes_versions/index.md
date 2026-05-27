--- 
title: routes_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - routes_versions
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

Creates, updates, deletes, gets or lists a <code>routes_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="routes_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai_gateway.routes_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="gateway_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>string</code></td>
    <td> (true, false)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="elements" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a></td>
    <td></td>
    <td>Get an AI Gateway Dynamic Route Version.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-id"><code>id</code></a></td>
    <td></td>
    <td>List all AI Gateway Dynamic Route Versions.</td>
</tr>
<tr>
    <td><a href="#create_version"><CopyableCode code="create_version" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-elements"><code>elements</code></a></td>
    <td></td>
    <td>Create a new AI Gateway Dynamic Route Version.</td>
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
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Get an AI Gateway Dynamic Route Version.

```sql
SELECT
id,
name,
gateway_id,
version_id,
active,
created_at,
data,
elements,
modified_at
FROM cloudflare.ai_gateway.routes_versions
WHERE account_id = '{{ account_id }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
AND id = '{{ id }}' -- required
AND version_id = '{{ version_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all AI Gateway Dynamic Route Versions.

```sql
SELECT
data,
success
FROM cloudflare.ai_gateway.routes_versions
WHERE account_id = '{{ account_id }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
AND id = '{{ id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_version"
    values={[
        { label: 'create_version', value: 'create_version' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_version">

Create a new AI Gateway Dynamic Route Version.

```sql
INSERT INTO cloudflare.ai_gateway.routes_versions (
elements,
account_id,
gateway_id,
id
)
SELECT 
'{{ elements }}' /* required */,
'{{ account_id }}',
'{{ gateway_id }}',
'{{ id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: routes_versions
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the routes_versions resource.
    - name: gateway_id
      value: "{{ gateway_id }}"
      description: Required parameter for the routes_versions resource.
    - name: id
      value: "{{ id }}"
      description: Required parameter for the routes_versions resource.
    - name: elements
      value:
        - id: "{{ id }}"
          outputs:
            next:
              elementId: "{{ elementId }}"
          type: "{{ type }}"
          properties:
            conditions: "{{ conditions }}"
`}</CodeBlock>

</TabItem>
</Tabs>
