--- 
title: delegations
hide_title: false
hide_table_of_contents: false
keywords:
  - delegations
  - addressing
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

Creates, updates, deletes, gets or lists a <code>delegations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delegations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.delegations" /></td></tr>
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

List Prefix Delegations response

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
    <td>Identifier of a Delegation. (example: d933b1530bc56c9953cf8ce166da8004)</td>
</tr>
<tr>
    <td><CopyableCode code="delegated_account_id" /></td>
    <td><code>string</code></td>
    <td>Account identifier for the account to which prefix is being delegated. (example: b1946ac92492d2347c6235b4d2611184)</td>
</tr>
<tr>
    <td><CopyableCode code="parent_prefix_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of an IP Prefix. (example: 2af39739cc4e3b5910c918468bb89828)</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all delegations for a given account IP prefix.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-cidr"><code>cidr</code></a>, <a href="#parameter-delegated_account_id"><code>delegated_account_id</code></a></td>
    <td></td>
    <td>Create a new account delegation for a given IP prefix.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-delegation_id"><code>delegation_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete an account delegation for a given IP prefix.</td>
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
<tr id="parameter-delegation_id">
    <td><CopyableCode code="delegation_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-prefix_id">
    <td><CopyableCode code="prefix_id" /></td>
    <td><code>string</code></td>
    <td>The IP prefix ID.</td>
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

List all delegations for a given account IP prefix.

```sql
SELECT
id,
delegated_account_id,
parent_prefix_id,
cidr,
created_at,
modified_at
FROM cloudflare.addressing.delegations
WHERE prefix_id = '{{ prefix_id }}' -- required
AND account_id = '{{ account_id }}' -- required
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

Create a new account delegation for a given IP prefix.

```sql
INSERT INTO cloudflare.addressing.delegations (
cidr,
delegated_account_id,
prefix_id,
account_id
)
SELECT 
'{{ cidr }}' /* required */,
'{{ delegated_account_id }}' /* required */,
'{{ prefix_id }}',
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
- name: delegations
  props:
    - name: prefix_id
      value: "{{ prefix_id }}"
      description: Required parameter for the delegations resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the delegations resource.
    - name: cidr
      value: "{{ cidr }}"
      description: |
        IP Prefix in Classless Inter-Domain Routing format.
    - name: delegated_account_id
      value: "{{ delegated_account_id }}"
      description: |
        Account identifier for the account to which prefix is being delegated.
`}</CodeBlock>

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

Delete an account delegation for a given IP prefix.

```sql
DELETE FROM cloudflare.addressing.delegations
WHERE delegation_id = '{{ delegation_id }}' --required
AND prefix_id = '{{ prefix_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
