--- 
title: policy_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_tests
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

Creates, updates, deletes, gets or lists a <code>policy_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policy_tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.policy_tests" /></td></tr>
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

Get an Access policy test update response.

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
    <td>The UUID of the policy test. (example: f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6)</td>
</tr>
<tr>
    <td><CopyableCode code="percent_approved" /></td>
    <td><code>integer</code></td>
    <td>The percentage of (processed) users approved based on policy evaluation results.</td>
</tr>
<tr>
    <td><CopyableCode code="percent_blocked" /></td>
    <td><code>integer</code></td>
    <td>The percentage of (processed) users blocked based on policy evaluation results.</td>
</tr>
<tr>
    <td><CopyableCode code="percent_errored" /></td>
    <td><code>integer</code></td>
    <td>The percentage of (processed) users errored based on policy evaluation results.</td>
</tr>
<tr>
    <td><CopyableCode code="percent_users_processed" /></td>
    <td><code>integer</code></td>
    <td>The percentage of users processed so far (of the entire user base).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the policy test. (blocked, processing, exceeded time, complete) (example: complete)</td>
</tr>
<tr>
    <td><CopyableCode code="total_users" /></td>
    <td><code>integer</code></td>
    <td>The total number of users in the user base.</td>
</tr>
<tr>
    <td><CopyableCode code="users_approved" /></td>
    <td><code>integer</code></td>
    <td>The number of (processed) users approved based on policy evaluation results.</td>
</tr>
<tr>
    <td><CopyableCode code="users_blocked" /></td>
    <td><code>integer</code></td>
    <td>The number of (processed) users blocked based on policy evaluation results.</td>
</tr>
<tr>
    <td><CopyableCode code="users_errored" /></td>
    <td><code>integer</code></td>
    <td>The number of (processed) users errored based on policy evaluation results.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_test_id"><code>policy_test_id</code></a></td>
    <td></td>
    <td>Fetches the current status of a given Access policy test.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Starts an Access policy test.</td>
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
<tr id="parameter-policy_test_id">
    <td><CopyableCode code="policy_test_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Fetches the current status of a given Access policy test.

```sql
SELECT
id,
percent_approved,
percent_blocked,
percent_errored,
percent_users_processed,
status,
total_users,
users_approved,
users_blocked,
users_errored
FROM cloudflare.zero_trust.policy_tests
WHERE account_id = '{{ account_id }}' -- required
AND policy_test_id = '{{ policy_test_id }}' -- required
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

Starts an Access policy test.

```sql
INSERT INTO cloudflare.zero_trust.policy_tests (
policies,
account_id
)
SELECT 
'{{ policies }}',
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
- name: policy_tests
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the policy_tests resource.
    - name: policies
      value:
        - approval_groups: "{{ approval_groups }}"
          approval_required: {{ approval_required }}
          connection_rules:
            rdp:
              allowed_clipboard_local_to_remote_formats:
                - "{{ allowed_clipboard_local_to_remote_formats }}"
              allowed_clipboard_remote_to_local_formats:
                - "{{ allowed_clipboard_remote_to_local_formats }}"
          isolation_required: {{ isolation_required }}
          mfa_config:
            allowed_authenticators:
              - "{{ allowed_authenticators }}"
            mfa_disabled: {{ mfa_disabled }}
            session_duration: "{{ session_duration }}"
          purpose_justification_prompt: "{{ purpose_justification_prompt }}"
          purpose_justification_required: {{ purpose_justification_required }}
          session_duration: "{{ session_duration }}"
          decision: "{{ decision }}"
          exclude: "{{ exclude }}"
          include: "{{ include }}"
          name: "{{ name }}"
          require: "{{ require }}"
`}</CodeBlock>

</TabItem>
</Tabs>
