--- 
title: move
hide_title: false
hide_table_of_contents: false
keywords:
  - move
  - email_security
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

Creates, updates, deletes, gets or lists a <code>move</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="move" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.email_security.move" /></td></tr>
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
    <td><a href="#email_security_post_message_move"><CopyableCode code="email_security_post_message_move" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-investigate_id"><code>investigate_id</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>Moves a single message to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.</td>
</tr>
<tr>
    <td><a href="#email_security_post_bulk_move"><CopyableCode code="email_security_post_bulk_move" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>Moves multiple messages to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.</td>
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
<tr id="parameter-investigate_id">
    <td><CopyableCode code="investigate_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="email_security_post_message_move"
    values={[
        { label: 'email_security_post_message_move', value: 'email_security_post_message_move' },
        { label: 'email_security_post_bulk_move', value: 'email_security_post_bulk_move' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="email_security_post_message_move">

Moves a single message to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.

```sql
INSERT INTO cloudflare.email_security.move (
destination,
account_id,
investigate_id
)
SELECT 
'{{ destination }}' /* required */,
'{{ account_id }}',
'{{ investigate_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="email_security_post_bulk_move">

Moves multiple messages to a specified mailbox folder (Inbox, JunkEmail, DeletedItems, RecoverableItemsDeletions, or RecoverableItemsPurges). Requires active integration.

```sql
INSERT INTO cloudflare.email_security.move (
destination,
ids,
postfix_ids,
account_id
)
SELECT 
'{{ destination }}' /* required */,
'{{ ids }}',
'{{ postfix_ids }}',
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
- name: move
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the move resource.
    - name: investigate_id
      value: "{{ investigate_id }}"
      description: Required parameter for the move resource.
    - name: destination
      value: "{{ destination }}"
      valid_values: ['Inbox', 'JunkEmail', 'DeletedItems', 'RecoverableItemsDeletions', 'RecoverableItemsPurges']
    - name: ids
      value:
        - "{{ ids }}"
      description: |
        List of message IDs to move
    - name: postfix_ids
      value:
        - "{{ postfix_ids }}"
      description: |
        Deprecated, use \`ids\` instead. End of life: November 1, 2026. List of message IDs to move.
`}</CodeBlock>

</TabItem>
</Tabs>
