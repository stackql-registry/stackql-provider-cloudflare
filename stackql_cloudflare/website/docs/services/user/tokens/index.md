--- 
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - user
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

Creates, updates, deletes, gets or lists a <code>tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tokens" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.user.tokens" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Token Details response

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
    <td>Token identifier tag. (example: ed17574386854bf78a67040be0a770b0)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Token name. (example: readonly token)</td>
</tr>
<tr>
    <td><CopyableCode code="condition" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="expires_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration time on or after which the JWT MUST NOT be accepted for processing. (example: 2020-01-01T00:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="issued_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time on which the token was created. (example: 2018-07-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="last_used_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the token was used. (example: 2020-01-02T12:34:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the token was modified. (example: 2018-07-02T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="not_before" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time before which the token MUST NOT be accepted for processing. (example: 2018-07-01T05:20:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td>List of access policies assigned to the token.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the token. (active, disabled, expired) (example: active, x-stainless-terraform-configurability: computed_optional)</td>
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
    <td><a href="#parameter-token_id"><code>token_id</code></a></td>
    <td></td>
    <td>Get information about a specific token.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-policies"><code>policies</code></a></td>
    <td></td>
    <td>Create a new access token.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-token_id"><code>token_id</code></a></td>
    <td></td>
    <td>Update an existing token.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-token_id"><code>token_id</code></a></td>
    <td></td>
    <td>Destroy a token.</td>
</tr>
<tr>
    <td><a href="#update_value"><CopyableCode code="update_value" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-token_id"><code>token_id</code></a></td>
    <td></td>
    <td>Roll the token secret.</td>
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
<tr id="parameter-token_id">
    <td><CopyableCode code="token_id" /></td>
    <td><code>string</code></td>
    <td>The API token ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get information about a specific token.

```sql
SELECT
id,
name,
condition,
expires_on,
issued_on,
last_used_on,
modified_on,
not_before,
policies,
status
FROM cloudflare.user.tokens
WHERE token_id = '{{ token_id }}' -- required
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

Create a new access token.

```sql
INSERT INTO cloudflare.user.tokens (
condition,
expires_on,
name,
not_before,
policies
)
SELECT 
'{{ condition }}',
'{{ expires_on }}',
'{{ name }}' /* required */,
'{{ not_before }}',
'{{ policies }}' /* required */
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
- name: tokens
  props:
    - name: condition
      value:
        request_ip:
          in:
            - "{{ in }}"
          not_in:
            - "{{ not_in }}"
    - name: expires_on
      value: "{{ expires_on }}"
      description: |
        The expiration time on or after which the JWT MUST NOT be accepted for processing.
    - name: name
      value: "{{ name }}"
      description: |
        Token name.
    - name: not_before
      value: "{{ not_before }}"
      description: |
        The time before which the token MUST NOT be accepted for processing.
    - name: policies
      description: |
        List of access policies assigned to the token.
      value:
        - effect: "{{ effect }}"
          id: "{{ id }}"
          permission_groups: "{{ permission_groups }}"
          resources: "{{ resources }}"
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

Update an existing token.

```sql
REPLACE cloudflare.user.tokens
SET 
condition = '{{ condition }}',
expires_on = '{{ expires_on }}',
name = '{{ name }}',
not_before = '{{ not_before }}',
policies = '{{ policies }}',
status = '{{ status }}'
WHERE 
token_id = '{{ token_id }}' --required
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

Destroy a token.

```sql
DELETE FROM cloudflare.user.tokens
WHERE token_id = '{{ token_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_value"
    values={[
        { label: 'update_value', value: 'update_value' }
    ]}
>
<TabItem value="update_value">

Roll the token secret.

```sql
EXEC cloudflare.user.tokens.update_value 
@token_id='{{ token_id }}' --required
;
```
</TabItem>
</Tabs>
