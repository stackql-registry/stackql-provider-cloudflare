--- 
title: acls
hide_title: false
hide_table_of_contents: false
keywords:
  - acls
  - magic_transit
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

Creates, updates, deletes, gets or lists an <code>acls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="acls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.acls" /></td></tr>
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

Site ACL Details response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the ACL. (example: PIN Pad - Cash Register)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the ACL. (example: Allows local traffic between PIN pads and cash register.)</td>
</tr>
<tr>
    <td><CopyableCode code="forward_locally" /></td>
    <td><code>boolean</code></td>
    <td>The desired forwarding action for this ACL policy. If set to "false", the policy will forward traffic to Cloudflare. If set to "true", the policy will forward traffic locally on the Magic Connector. If not included in request, will default to false.</td>
</tr>
<tr>
    <td><CopyableCode code="lan_1" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lan_2" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="protocols" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="unidirectional" /></td>
    <td><code>boolean</code></td>
    <td>The desired traffic direction for this ACL policy. If set to "false", the policy will allow bidirectional traffic. If set to "true", the policy will only allow traffic in one direction. If not included in request, will default to false.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Site ACLs response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the ACL. (example: PIN Pad - Cash Register)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the ACL. (example: Allows local traffic between PIN pads and cash register.)</td>
</tr>
<tr>
    <td><CopyableCode code="forward_locally" /></td>
    <td><code>boolean</code></td>
    <td>The desired forwarding action for this ACL policy. If set to "false", the policy will forward traffic to Cloudflare. If set to "true", the policy will forward traffic locally on the Magic Connector. If not included in request, will default to false.</td>
</tr>
<tr>
    <td><CopyableCode code="lan_1" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lan_2" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="protocols" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="unidirectional" /></td>
    <td><code>boolean</code></td>
    <td>The desired traffic direction for this ACL policy. If set to "false", the policy will allow bidirectional traffic. If set to "true", the policy will only allow traffic in one direction. If not included in request, will default to false.</td>
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
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-acl_id"><code>acl_id</code></a></td>
    <td></td>
    <td>Get a specific Site ACL.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Lists Site ACLs associated with an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-lan_1"><code>lan_1</code></a>, <a href="#parameter-lan_2"><code>lan_2</code></a></td>
    <td></td>
    <td>Creates a new Site ACL.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-acl_id"><code>acl_id</code></a></td>
    <td></td>
    <td>Patch a specific Site ACL.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-acl_id"><code>acl_id</code></a></td>
    <td></td>
    <td>Update a specific Site ACL.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-site_id"><code>site_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-acl_id"><code>acl_id</code></a></td>
    <td></td>
    <td>Remove a specific Site ACL.</td>
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
<tr id="parameter-acl_id">
    <td><CopyableCode code="acl_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-site_id">
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>The site ID.</td>
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

Get a specific Site ACL.

```sql
SELECT
id,
name,
description,
forward_locally,
lan_1,
lan_2,
protocols,
unidirectional
FROM cloudflare.magic_transit.acls
WHERE site_id = '{{ site_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND acl_id = '{{ acl_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Site ACLs associated with an account.

```sql
SELECT
id,
name,
description,
forward_locally,
lan_1,
lan_2,
protocols,
unidirectional
FROM cloudflare.magic_transit.acls
WHERE account_id = '{{ account_id }}' -- required
AND site_id = '{{ site_id }}' -- required
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

Creates a new Site ACL.

```sql
INSERT INTO cloudflare.magic_transit.acls (
description,
forward_locally,
lan_1,
lan_2,
name,
protocols,
unidirectional,
account_id,
site_id
)
SELECT 
'{{ description }}',
{{ forward_locally }},
'{{ lan_1 }}' /* required */,
'{{ lan_2 }}' /* required */,
'{{ name }}' /* required */,
'{{ protocols }}',
{{ unidirectional }},
'{{ account_id }}',
'{{ site_id }}'
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
- name: acls
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the acls resource.
    - name: site_id
      value: "{{ site_id }}"
      description: Required parameter for the acls resource.
    - name: description
      value: "{{ description }}"
      description: |
        Description for the ACL.
    - name: forward_locally
      value: {{ forward_locally }}
      description: |
        The desired forwarding action for this ACL policy. If set to "false", the policy will forward traffic to Cloudflare. If set to "true", the policy will forward traffic locally on the Magic Connector. If not included in request, will default to false.
    - name: lan_1
      value:
        lan_id: "{{ lan_id }}"
        lan_name: "{{ lan_name }}"
        port_ranges:
          - "{{ port_ranges }}"
        ports:
          - {{ ports }}
        subnets:
          - "{{ subnets }}"
    - name: lan_2
      value:
        lan_id: "{{ lan_id }}"
        lan_name: "{{ lan_name }}"
        port_ranges:
          - "{{ port_ranges }}"
        ports:
          - {{ ports }}
        subnets:
          - "{{ subnets }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the ACL.
    - name: protocols
      value:
        - "{{ protocols }}"
    - name: unidirectional
      value: {{ unidirectional }}
      description: |
        The desired traffic direction for this ACL policy. If set to "false", the policy will allow bidirectional traffic. If set to "true", the policy will only allow traffic in one direction. If not included in request, will default to false.
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

Patch a specific Site ACL.

```sql
UPDATE cloudflare.magic_transit.acls
SET 
description = '{{ description }}',
forward_locally = {{ forward_locally }},
lan_1 = '{{ lan_1 }}',
lan_2 = '{{ lan_2 }}',
name = '{{ name }}',
protocols = '{{ protocols }}',
unidirectional = {{ unidirectional }}
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND acl_id = '{{ acl_id }}' --required
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

Update a specific Site ACL.

```sql
REPLACE cloudflare.magic_transit.acls
SET 
description = '{{ description }}',
forward_locally = {{ forward_locally }},
lan_1 = '{{ lan_1 }}',
lan_2 = '{{ lan_2 }}',
name = '{{ name }}',
protocols = '{{ protocols }}',
unidirectional = {{ unidirectional }}
WHERE 
site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND acl_id = '{{ acl_id }}' --required
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

Remove a specific Site ACL.

```sql
DELETE FROM cloudflare.magic_transit.acls
WHERE site_id = '{{ site_id }}' --required
AND account_id = '{{ account_id }}' --required
AND acl_id = '{{ acl_id }}' --required
;
```
</TabItem>
</Tabs>
