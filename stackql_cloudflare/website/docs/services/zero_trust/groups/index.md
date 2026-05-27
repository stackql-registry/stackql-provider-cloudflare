--- 
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.groups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get an Access group response

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access group. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match a policy, a user cannot meet any of the Exclude rules.</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match a policy, a user must meet all of the Require rules.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match a policy, a user must meet all of the Require rules.</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get an Access group response

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
    <td>UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access group. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match a policy, a user cannot meet any of the Exclude rules.</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match a policy, a user must meet all of the Require rules.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match a policy, a user must meet all of the Require rules.</td>
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
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a single Access group.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches a single Access group.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td></td>
    <td>Creates a new Access group.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td></td>
    <td>Creates a new Access group.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td></td>
    <td>Updates a configured Access group.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-include"><code>include</code></a></td>
    <td></td>
    <td>Updates a configured Access group.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an Access group.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an Access group.</td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The Access group ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches a single Access group.

```sql
SELECT
id,
name,
created_at,
exclude,
include,
is_default,
require,
updated_at
FROM cloudflare.zero_trust.groups
WHERE group_id = '{{ group_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches a single Access group.

```sql
SELECT
id,
name,
created_at,
exclude,
include,
is_default,
require,
updated_at
FROM cloudflare.zero_trust.groups
WHERE group_id = '{{ group_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'create_by_zone', value: 'create_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Creates a new Access group.

```sql
INSERT INTO cloudflare.zero_trust.groups (
exclude,
include,
is_default,
name,
require,
account_id
)
SELECT 
'{{ exclude }}',
'{{ include }}' /* required */,
{{ is_default }},
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
<TabItem value="create_by_zone">

Creates a new Access group.

```sql
INSERT INTO cloudflare.zero_trust.groups (
exclude,
include,
is_default,
name,
require,
zone_id
)
SELECT 
'{{ exclude }}',
'{{ include }}' /* required */,
{{ is_default }},
'{{ name }}' /* required */,
'{{ require }}',
'{{ zone_id }}'
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
- name: groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the groups resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the groups resource.
    - name: exclude
      description: |
        Rules evaluated with a NOT logical operator. To match a policy, a user cannot meet any of the Exclude rules.
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
    - name: is_default
      value: {{ is_default }}
      description: |
        Whether this is the default group
    - name: name
      value: "{{ name }}"
      description: |
        The name of the Access group.
    - name: require
      description: |
        Rules evaluated with an AND logical operator. To match a policy, a user must meet all of the Require rules.
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
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' },
        { label: 'update_by_zone', value: 'update_by_zone' }
    ]}
>
<TabItem value="update_by_account">

Updates a configured Access group.

```sql
REPLACE cloudflare.zero_trust.groups
SET 
exclude = '{{ exclude }}',
include = '{{ include }}',
is_default = {{ is_default }},
name = '{{ name }}',
require = '{{ require }}'
WHERE 
group_id = '{{ group_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND include = '{{ include }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates a configured Access group.

```sql
REPLACE cloudflare.zero_trust.groups
SET 
exclude = '{{ exclude }}',
include = '{{ include }}',
is_default = {{ is_default }},
name = '{{ name }}',
require = '{{ require }}'
WHERE 
group_id = '{{ group_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND include = '{{ include }}' --required
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
        { label: 'delete_by_account', value: 'delete_by_account' },
        { label: 'delete_by_zone', value: 'delete_by_zone' }
    ]}
>
<TabItem value="delete_by_account">

Deletes an Access group.

```sql
DELETE FROM cloudflare.zero_trust.groups
WHERE group_id = '{{ group_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an Access group.

```sql
DELETE FROM cloudflare.zero_trust.groups
WHERE group_id = '{{ group_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
