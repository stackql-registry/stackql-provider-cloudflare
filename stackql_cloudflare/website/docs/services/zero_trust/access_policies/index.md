--- 
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
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

Creates, updates, deletes, gets or lists an <code>access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.access_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get_by_account">

Get an Access reusable policy response.

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
    <td>The UUID of the policy (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access policy. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="app_count" /></td>
    <td><code>integer</code></td>
    <td>Number of access applications currently using this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="approval_groups" /></td>
    <td><code>array</code></td>
    <td>Administrators who can approve a temporary authentication request. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_required" /></td>
    <td><code>boolean</code></td>
    <td>Requires the user to request access from an administrator at the start of each session.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_rules" /></td>
    <td><code>object</code></td>
    <td>The rules that define how users may connect to targets secured by your application. (title: Connection Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action. (allow, deny, non_identity, bypass) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_required" /></td>
    <td><code>boolean</code></td>
    <td>Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_prompt" /></td>
    <td><code>string</code></td>
    <td>A custom message that will appear on the purpose justification screen. (example: Please enter a justification for entering this protected domain.)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_required" /></td>
    <td><code>boolean</code></td>
    <td>Require users to enter a justification when they log in to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="reusable" /></td>
    <td><code>boolean</code></td>
    <td> (true)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List Access reusable policies response.

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
    <td>The UUID of the policy (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access policy. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="app_count" /></td>
    <td><code>integer</code></td>
    <td>Number of access applications currently using this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="approval_groups" /></td>
    <td><code>array</code></td>
    <td>Administrators who can approve a temporary authentication request. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_required" /></td>
    <td><code>boolean</code></td>
    <td>Requires the user to request access from an administrator at the start of each session.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_rules" /></td>
    <td><code>object</code></td>
    <td>The rules that define how users may connect to targets secured by your application. (title: Connection Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action. (allow, deny, non_identity, bypass) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_required" /></td>
    <td><code>boolean</code></td>
    <td>Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_prompt" /></td>
    <td><code>string</code></td>
    <td>A custom message that will appear on the purpose justification screen. (example: Please enter a justification for entering this protected domain.)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_required" /></td>
    <td><code>boolean</code></td>
    <td>Require users to enter a justification when they log in to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="reusable" /></td>
    <td><code>boolean</code></td>
    <td> (true)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Fetches a single Access reusable policy.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists Access reusable policies.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-decision"><code>decision</code></a>, <a href="#parameter-include"><code>include</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new Access reusable policy.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-decision"><code>decision</code></a>, <a href="#parameter-include"><code>include</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Updates a Access reusable policy.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Deletes an Access reusable policy.</td>
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
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get_by_account">

Fetches a single Access reusable policy.

```sql
SELECT
id,
name,
app_count,
approval_groups,
approval_required,
connection_rules,
created_at,
decision,
exclude,
include,
isolation_required,
mfa_config,
purpose_justification_prompt,
purpose_justification_required,
require,
reusable,
session_duration,
updated_at
FROM cloudflare.zero_trust.access_policies
WHERE account_id = '{{ account_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Lists Access reusable policies.

```sql
SELECT
id,
name,
app_count,
approval_groups,
approval_required,
connection_rules,
created_at,
decision,
exclude,
include,
isolation_required,
mfa_config,
purpose_justification_prompt,
purpose_justification_required,
require,
reusable,
session_duration,
updated_at
FROM cloudflare.zero_trust.access_policies
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Creates a new Access reusable policy.

```sql
INSERT INTO cloudflare.zero_trust.access_policies (
approval_groups,
approval_required,
connection_rules,
isolation_required,
mfa_config,
purpose_justification_prompt,
purpose_justification_required,
session_duration,
decision,
exclude,
include,
name,
require,
account_id
)
SELECT 
'{{ approval_groups }}',
{{ approval_required }},
'{{ connection_rules }}',
{{ isolation_required }},
'{{ mfa_config }}',
'{{ purpose_justification_prompt }}',
{{ purpose_justification_required }},
'{{ session_duration }}',
'{{ decision }}' /* required */,
'{{ exclude }}',
'{{ include }}' /* required */,
'{{ name }}' /* required */,
'{{ require }}',
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
- name: access_policies
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the access_policies resource.
    - name: approval_groups
      description: |
        Administrators who can approve a temporary authentication request.
      value:
        - approvals_needed: {{ approvals_needed }}
          email_addresses: "{{ email_addresses }}"
          email_list_uuid: "{{ email_list_uuid }}"
    - name: approval_required
      value: {{ approval_required }}
      description: |
        Requires the user to request access from an administrator at the start of each session.
    - name: connection_rules
      description: |
        The rules that define how users may connect to targets secured by your application.
      value:
        rdp:
          allowed_clipboard_local_to_remote_formats:
            - "{{ allowed_clipboard_local_to_remote_formats }}"
          allowed_clipboard_remote_to_local_formats:
            - "{{ allowed_clipboard_remote_to_local_formats }}"
    - name: isolation_required
      value: {{ isolation_required }}
      description: |
        Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.
    - name: mfa_config
      description: |
        Configures multi-factor authentication (MFA) settings.
      value:
        allowed_authenticators:
          - "{{ allowed_authenticators }}"
        mfa_disabled: {{ mfa_disabled }}
        session_duration: "{{ session_duration }}"
    - name: purpose_justification_prompt
      value: "{{ purpose_justification_prompt }}"
      description: |
        A custom message that will appear on the purpose justification screen.
    - name: purpose_justification_required
      value: {{ purpose_justification_required }}
      description: |
        Require users to enter a justification when they log in to the application.
    - name: session_duration
      value: "{{ session_duration }}"
      description: |
        The amount of time that tokens issued for the application will be valid. Must be in the format \`300ms\` or \`2h45m\`. Valid time units are: ns, us (or µs), ms, s, m, h.
      default: 24h
    - name: decision
      value: "{{ decision }}"
      description: |
        The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action.
      valid_values: ['allow', 'deny', 'non_identity', 'bypass']
    - name: exclude
      description: |
        Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.
      value:
        - group:
            id: "{{ id }}"
          any_valid_service_token: "{{ any_valid_service_token }}"
          auth_context:
            ac_id: "{{ ac_id }}"
            id: "{{ id }}"
            identity_provider_id: "{{ identity_provider_id }}"
          auth_method:
            auth_method: "{{ auth_method }}"
          azureAD:
            id: "{{ id }}"
            identity_provider_id: "{{ identity_provider_id }}"
          certificate: "{{ certificate }}"
          common_name:
            common_name: "{{ common_name }}"
          geo:
            country_code: "{{ country_code }}"
          device_posture:
            integration_uid: "{{ integration_uid }}"
          email_domain:
            domain: "{{ domain }}"
          email_list:
            id: "{{ id }}"
          email:
            email: "{{ email }}"
          everyone: "{{ everyone }}"
          external_evaluation:
            evaluate_url: "{{ evaluate_url }}"
            keys_url: "{{ keys_url }}"
          github-organization:
            identity_provider_id: "{{ identity_provider_id }}"
            name: "{{ name }}"
            team: "{{ team }}"
          gsuite:
            email: "{{ email }}"
            identity_provider_id: "{{ identity_provider_id }}"
          login_method:
            id: "{{ id }}"
          ip_list:
            id: "{{ id }}"
          ip:
            ip: "{{ ip }}"
          okta:
            identity_provider_id: "{{ identity_provider_id }}"
            name: "{{ name }}"
          saml:
            attribute_name: "{{ attribute_name }}"
            attribute_value: "{{ attribute_value }}"
            identity_provider_id: "{{ identity_provider_id }}"
          oidc:
            claim_name: "{{ claim_name }}"
            claim_value: "{{ claim_value }}"
            identity_provider_id: "{{ identity_provider_id }}"
          service_token:
            token_id: "{{ token_id }}"
          linked_app_token:
            app_uid: "{{ app_uid }}"
          user_risk_score:
            user_risk_score:
              - "{{ user_risk_score }}"
      default: 
    - name: include
      description: |
        Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.
      value:
        - group:
            id: "{{ id }}"
          any_valid_service_token: "{{ any_valid_service_token }}"
          auth_context:
            ac_id: "{{ ac_id }}"
            id: "{{ id }}"
            identity_provider_id: "{{ identity_provider_id }}"
          auth_method:
            auth_method: "{{ auth_method }}"
          azureAD:
            id: "{{ id }}"
            identity_provider_id: "{{ identity_provider_id }}"
          certificate: "{{ certificate }}"
          common_name:
            common_name: "{{ common_name }}"
          geo:
            country_code: "{{ country_code }}"
          device_posture:
            integration_uid: "{{ integration_uid }}"
          email_domain:
            domain: "{{ domain }}"
          email_list:
            id: "{{ id }}"
          email:
            email: "{{ email }}"
          everyone: "{{ everyone }}"
          external_evaluation:
            evaluate_url: "{{ evaluate_url }}"
            keys_url: "{{ keys_url }}"
          github-organization:
            identity_provider_id: "{{ identity_provider_id }}"
            name: "{{ name }}"
            team: "{{ team }}"
          gsuite:
            email: "{{ email }}"
            identity_provider_id: "{{ identity_provider_id }}"
          login_method:
            id: "{{ id }}"
          ip_list:
            id: "{{ id }}"
          ip:
            ip: "{{ ip }}"
          okta:
            identity_provider_id: "{{ identity_provider_id }}"
            name: "{{ name }}"
          saml:
            attribute_name: "{{ attribute_name }}"
            attribute_value: "{{ attribute_value }}"
            identity_provider_id: "{{ identity_provider_id }}"
          oidc:
            claim_name: "{{ claim_name }}"
            claim_value: "{{ claim_value }}"
            identity_provider_id: "{{ identity_provider_id }}"
          service_token:
            token_id: "{{ token_id }}"
          linked_app_token:
            app_uid: "{{ app_uid }}"
          user_risk_score:
            user_risk_score:
              - "{{ user_risk_score }}"
      default: 
    - name: name
      value: "{{ name }}"
      description: |
        The name of the Access policy.
    - name: require
      description: |
        Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.
      value:
        - group:
            id: "{{ id }}"
          any_valid_service_token: "{{ any_valid_service_token }}"
          auth_context:
            ac_id: "{{ ac_id }}"
            id: "{{ id }}"
            identity_provider_id: "{{ identity_provider_id }}"
          auth_method:
            auth_method: "{{ auth_method }}"
          azureAD:
            id: "{{ id }}"
            identity_provider_id: "{{ identity_provider_id }}"
          certificate: "{{ certificate }}"
          common_name:
            common_name: "{{ common_name }}"
          geo:
            country_code: "{{ country_code }}"
          device_posture:
            integration_uid: "{{ integration_uid }}"
          email_domain:
            domain: "{{ domain }}"
          email_list:
            id: "{{ id }}"
          email:
            email: "{{ email }}"
          everyone: "{{ everyone }}"
          external_evaluation:
            evaluate_url: "{{ evaluate_url }}"
            keys_url: "{{ keys_url }}"
          github-organization:
            identity_provider_id: "{{ identity_provider_id }}"
            name: "{{ name }}"
            team: "{{ team }}"
          gsuite:
            email: "{{ email }}"
            identity_provider_id: "{{ identity_provider_id }}"
          login_method:
            id: "{{ id }}"
          ip_list:
            id: "{{ id }}"
          ip:
            ip: "{{ ip }}"
          okta:
            identity_provider_id: "{{ identity_provider_id }}"
            name: "{{ name }}"
          saml:
            attribute_name: "{{ attribute_name }}"
            attribute_value: "{{ attribute_value }}"
            identity_provider_id: "{{ identity_provider_id }}"
          oidc:
            claim_name: "{{ claim_name }}"
            claim_value: "{{ claim_value }}"
            identity_provider_id: "{{ identity_provider_id }}"
          service_token:
            token_id: "{{ token_id }}"
          linked_app_token:
            app_uid: "{{ app_uid }}"
          user_risk_score:
            user_risk_score:
              - "{{ user_risk_score }}"
      default: 
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' }
    ]}
>
<TabItem value="update_by_account">

Updates a Access reusable policy.

```sql
REPLACE cloudflare.zero_trust.access_policies
SET 
approval_groups = '{{ approval_groups }}',
approval_required = {{ approval_required }},
connection_rules = '{{ connection_rules }}',
isolation_required = {{ isolation_required }},
mfa_config = '{{ mfa_config }}',
purpose_justification_prompt = '{{ purpose_justification_prompt }}',
purpose_justification_required = {{ purpose_justification_required }},
session_duration = '{{ session_duration }}',
decision = '{{ decision }}',
exclude = '{{ exclude }}',
include = '{{ include }}',
name = '{{ name }}',
require = '{{ require }}'
WHERE 
account_id = '{{ account_id }}' --required
AND policy_id = '{{ policy_id }}' --required
AND decision = '{{ decision }}' --required
AND include = '{{ include }}' --required
AND name = '{{ name }}' --required
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
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' }
    ]}
>
<TabItem value="delete_by_account">

Deletes an Access reusable policy.

```sql
DELETE FROM cloudflare.zero_trust.access_policies
WHERE account_id = '{{ account_id }}' --required
AND policy_id = '{{ policy_id }}' --required
;
```
</TabItem>
</Tabs>
