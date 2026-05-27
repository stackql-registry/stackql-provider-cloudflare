--- 
title: unsubscribe
hide_title: false
hide_table_of_contents: false
keywords:
  - unsubscribe
  - alerting
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

Creates, updates, deletes, gets or lists an <code>unsubscribe</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="unsubscribe" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.alerting.unsubscribe" /></td></tr>
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

Show email unsubscribe details response

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
    <td>The unique identifier of a notification policy (example: 0da2b59ef118439d8097bdfb215203c9)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the policy. (example: SSL Notification Event Policy)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The account id (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td><a href="#parameter-email"><code>email</code></a>, <a href="#parameter-token"><code>token</code></a></td>
    <td>Shows details for unsubscribing an email address from a notification policy.</td>
</tr>
<tr>
    <td><a href="#notification_policies_unsubscribe_email_from_notification_policy"><CopyableCode code="notification_policies_unsubscribe_email_from_notification_policy" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td><a href="#parameter-email"><code>email</code></a>, <a href="#parameter-token"><code>token</code></a></td>
    <td>Unsubscribes an email address from a notification policy.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
<tr id="parameter-email">
    <td><CopyableCode code="email" /></td>
    <td><code>string (email)</code></td>
    <td></td>
</tr>
<tr id="parameter-token">
    <td><CopyableCode code="token" /></td>
    <td><code>string</code></td>
    <td></td>
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

Shows details for unsubscribing an email address from a notification policy.

```sql
SELECT
id,
name,
account_id,
email,
token
FROM cloudflare.alerting.unsubscribe
WHERE account_id = '{{ account_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
AND email = '{{ email }}'
AND token = '{{ token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="notification_policies_unsubscribe_email_from_notification_policy"
    values={[
        { label: 'notification_policies_unsubscribe_email_from_notification_policy', value: 'notification_policies_unsubscribe_email_from_notification_policy' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="notification_policies_unsubscribe_email_from_notification_policy">

Unsubscribes an email address from a notification policy.

```sql
INSERT INTO cloudflare.alerting.unsubscribe (
account_id,
policy_id,
email,
token
)
SELECT 
'{{ account_id }}',
'{{ policy_id }}',
'{{ email }}',
'{{ token }}'
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
- name: unsubscribe
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the unsubscribe resource.
    - name: policy_id
      value: "{{ policy_id }}"
      description: Required parameter for the unsubscribe resource.
    - name: email
      value: "{{ email }}"
    - name: token
      value: "{{ token }}"
`}</CodeBlock>

</TabItem>
</Tabs>
