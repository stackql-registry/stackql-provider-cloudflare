--- 
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
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

Creates, updates, deletes, gets or lists an <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="organizations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.organizations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

Get your Zero Trust organization response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of your Zero Trust organization. (example: Widget Corps Internal Applications)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_authenticate_via_warp" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, users can authenticate via WARP for any application in your organization. Application settings will take precedence over this value.</td>
</tr>
<tr>
    <td><CopyableCode code="auth_domain" /></td>
    <td><code>string</code></td>
    <td>The unique subdomain assigned to your Zero Trust organization. (example: test.cloudflareaccess.com)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_redirect_to_identity" /></td>
    <td><code>boolean</code></td>
    <td>When set to `true`, users skip the identity provider selection step during login.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_pages" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deny_unmatched_requests" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether to deny all requests to Cloudflare-protected resources that lack an associated Access application. If enabled, you must explicitly configure an Access application and policy to allow traffic to your Cloudflare-protected resources. For domains you want to be public across all subdomains, add the domain to the `deny_unmatched_requests_exempted_zone_names` array.</td>
</tr>
<tr>
    <td><CopyableCode code="deny_unmatched_requests_exempted_zone_names" /></td>
    <td><code>array</code></td>
    <td>Contains zone names to exempt from the `deny_unmatched_requests` feature. Requests to a subdomain in an exempted zone will block unauthenticated traffic by default if there is a configured Access application and policy that matches the request.</td>
</tr>
<tr>
    <td><CopyableCode code="is_ui_read_only" /></td>
    <td><code>boolean</code></td>
    <td>Lock all settings as Read-Only in the Dashboard, regardless of user permission. Updates may only be made via the API or Terraform for this account when enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="login_design" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings for an organization.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_required_for_all_apps" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether global MFA settings apply to applications by default. The organization must have MFA enabled with at least one authentication method and a session duration configured.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_ssh_piv_key_requirements" /></td>
    <td><code>object</code></td>
    <td>Configures SSH PIV key requirements for MFA using hardware security keys.</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for applications will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="ui_read_only_toggle_reason" /></td>
    <td><code>string</code></td>
    <td>A description of the reason why the UI read only field is being toggled. (example: Temporarily turn off the UI read only lock to make a change via the UI, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="user_seat_expiration_inactive_time" /></td>
    <td><code>string</code></td>
    <td>The amount of time a user seat is inactive before it expires. When the user seat exceeds the set time of inactivity, the user is removed as an active seat and no longer counts against your Teams seat count. Minimum value for this setting is 1 month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. (example: 730h)</td>
</tr>
<tr>
    <td><CopyableCode code="warp_auth_session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for applications will be valid. Must be in the format `30m` or `2h45m`. Valid time units are: m, h. (example: 24h)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

Get your Zero Trust organization response

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of your Zero Trust organization. (example: Widget Corps Internal Applications)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_authenticate_via_warp" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, users can authenticate via WARP for any application in your organization. Application settings will take precedence over this value.</td>
</tr>
<tr>
    <td><CopyableCode code="auth_domain" /></td>
    <td><code>string</code></td>
    <td>The unique subdomain assigned to your Zero Trust organization. (example: test.cloudflareaccess.com)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_redirect_to_identity" /></td>
    <td><code>boolean</code></td>
    <td>When set to `true`, users skip the identity provider selection step during login.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_pages" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deny_unmatched_requests" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether to deny all requests to Cloudflare-protected resources that lack an associated Access application. If enabled, you must explicitly configure an Access application and policy to allow traffic to your Cloudflare-protected resources. For domains you want to be public across all subdomains, add the domain to the `deny_unmatched_requests_exempted_zone_names` array.</td>
</tr>
<tr>
    <td><CopyableCode code="deny_unmatched_requests_exempted_zone_names" /></td>
    <td><code>array</code></td>
    <td>Contains zone names to exempt from the `deny_unmatched_requests` feature. Requests to a subdomain in an exempted zone will block unauthenticated traffic by default if there is a configured Access application and policy that matches the request.</td>
</tr>
<tr>
    <td><CopyableCode code="is_ui_read_only" /></td>
    <td><code>boolean</code></td>
    <td>Lock all settings as Read-Only in the Dashboard, regardless of user permission. Updates may only be made via the API or Terraform for this account when enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="login_design" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings for an organization.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_required_for_all_apps" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether global MFA settings apply to applications by default. The organization must have MFA enabled with at least one authentication method and a session duration configured.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_ssh_piv_key_requirements" /></td>
    <td><code>object</code></td>
    <td>Configures SSH PIV key requirements for MFA using hardware security keys.</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for applications will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="ui_read_only_toggle_reason" /></td>
    <td><code>string</code></td>
    <td>A description of the reason why the UI read only field is being toggled. (example: Temporarily turn off the UI read only lock to make a change via the UI, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="user_seat_expiration_inactive_time" /></td>
    <td><code>string</code></td>
    <td>The amount of time a user seat is inactive before it expires. When the user seat exceeds the set time of inactivity, the user is removed as an active seat and no longer counts against your Teams seat count. Minimum value for this setting is 1 month (730h). Must be in the format `300ms` or `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. (example: 730h)</td>
</tr>
<tr>
    <td><CopyableCode code="warp_auth_session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for applications will be valid. Must be in the format `30m` or `2h45m`. Valid time units are: m, h. (example: 24h)</td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns the configuration for your Zero Trust organization.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Returns the configuration for your Zero Trust organization.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-auth_domain"><code>auth_domain</code></a></td>
    <td></td>
    <td>Sets up a Zero Trust organization for your account or zone.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-auth_domain"><code>auth_domain</code></a></td>
    <td></td>
    <td>Sets up a Zero Trust organization for your account or zone.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates the configuration for your Zero Trust organization.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates the configuration for your Zero Trust organization.</td>
</tr>
<tr>
    <td><a href="#revoke_users_by_account"><CopyableCode code="revoke_users_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-email"><code>email</code></a></td>
    <td><a href="#parameter-devices"><code>devices</code></a></td>
    <td>Revokes a user's access across all applications.</td>
</tr>
<tr>
    <td><a href="#revoke_users_by_zone"><CopyableCode code="revoke_users_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-email"><code>email</code></a></td>
    <td><a href="#parameter-devices"><code>devices</code></a></td>
    <td>Revokes a user's access across all applications.</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-devices">
    <td><CopyableCode code="devices" /></td>
    <td><code>boolean</code></td>
    <td>When set to `true`, all devices associated with the user will be revoked.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

Returns the configuration for your Zero Trust organization.

```sql
SELECT
name,
allow_authenticate_via_warp,
auth_domain,
auto_redirect_to_identity,
created_at,
custom_pages,
deny_unmatched_requests,
deny_unmatched_requests_exempted_zone_names,
is_ui_read_only,
login_design,
mfa_config,
mfa_required_for_all_apps,
mfa_ssh_piv_key_requirements,
session_duration,
ui_read_only_toggle_reason,
updated_at,
user_seat_expiration_inactive_time,
warp_auth_session_duration
FROM cloudflare.zero_trust.organizations
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Returns the configuration for your Zero Trust organization.

```sql
SELECT
name,
allow_authenticate_via_warp,
auth_domain,
auto_redirect_to_identity,
created_at,
custom_pages,
deny_unmatched_requests,
deny_unmatched_requests_exempted_zone_names,
is_ui_read_only,
login_design,
mfa_config,
mfa_required_for_all_apps,
mfa_ssh_piv_key_requirements,
session_duration,
ui_read_only_toggle_reason,
updated_at,
user_seat_expiration_inactive_time,
warp_auth_session_duration
FROM cloudflare.zero_trust.organizations
WHERE zone_id = '{{ zone_id }}' -- required
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

Sets up a Zero Trust organization for your account or zone.

```sql
INSERT INTO cloudflare.zero_trust.organizations (
allow_authenticate_via_warp,
auth_domain,
auto_redirect_to_identity,
deny_unmatched_requests,
deny_unmatched_requests_exempted_zone_names,
is_ui_read_only,
login_design,
mfa_config,
mfa_required_for_all_apps,
mfa_ssh_piv_key_requirements,
name,
session_duration,
ui_read_only_toggle_reason,
user_seat_expiration_inactive_time,
warp_auth_session_duration,
account_id
)
SELECT 
{{ allow_authenticate_via_warp }},
'{{ auth_domain }}' /* required */,
{{ auto_redirect_to_identity }},
{{ deny_unmatched_requests }},
'{{ deny_unmatched_requests_exempted_zone_names }}',
{{ is_ui_read_only }},
'{{ login_design }}',
'{{ mfa_config }}',
{{ mfa_required_for_all_apps }},
'{{ mfa_ssh_piv_key_requirements }}',
'{{ name }}' /* required */,
'{{ session_duration }}',
'{{ ui_read_only_toggle_reason }}',
'{{ user_seat_expiration_inactive_time }}',
'{{ warp_auth_session_duration }}',
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

Sets up a Zero Trust organization for your account or zone.

```sql
INSERT INTO cloudflare.zero_trust.organizations (
allow_authenticate_via_warp,
auth_domain,
auto_redirect_to_identity,
deny_unmatched_requests,
deny_unmatched_requests_exempted_zone_names,
is_ui_read_only,
login_design,
mfa_config,
mfa_required_for_all_apps,
mfa_ssh_piv_key_requirements,
name,
session_duration,
ui_read_only_toggle_reason,
user_seat_expiration_inactive_time,
warp_auth_session_duration,
zone_id
)
SELECT 
{{ allow_authenticate_via_warp }},
'{{ auth_domain }}' /* required */,
{{ auto_redirect_to_identity }},
{{ deny_unmatched_requests }},
'{{ deny_unmatched_requests_exempted_zone_names }}',
{{ is_ui_read_only }},
'{{ login_design }}',
'{{ mfa_config }}',
{{ mfa_required_for_all_apps }},
'{{ mfa_ssh_piv_key_requirements }}',
'{{ name }}' /* required */,
'{{ session_duration }}',
'{{ ui_read_only_toggle_reason }}',
'{{ user_seat_expiration_inactive_time }}',
'{{ warp_auth_session_duration }}',
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
- name: organizations
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the organizations resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the organizations resource.
    - name: allow_authenticate_via_warp
      value: {{ allow_authenticate_via_warp }}
      description: |
        When set to true, users can authenticate via WARP for any application in your organization. Application settings will take precedence over this value.
      default: false
    - name: auth_domain
      value: "{{ auth_domain }}"
      description: |
        The unique subdomain assigned to your Zero Trust organization.
    - name: auto_redirect_to_identity
      value: {{ auto_redirect_to_identity }}
      description: |
        When set to \`true\`, users skip the identity provider selection step during login.
      default: false
    - name: deny_unmatched_requests
      value: {{ deny_unmatched_requests }}
      description: |
        Determines whether to deny all requests to Cloudflare-protected resources that lack an associated Access application. If enabled, you must explicitly configure an Access application and policy to allow traffic to your Cloudflare-protected resources. For domains you want to be public across all subdomains, add the domain to the \`deny_unmatched_requests_exempted_zone_names\` array.
    - name: deny_unmatched_requests_exempted_zone_names
      value:
        - "{{ deny_unmatched_requests_exempted_zone_names }}"
      description: |
        Contains zone names to exempt from the \`deny_unmatched_requests\` feature. Requests to a subdomain in an exempted zone will block unauthenticated traffic by default if there is a configured Access application and policy that matches the request.
    - name: is_ui_read_only
      value: {{ is_ui_read_only }}
      description: |
        Lock all settings as Read-Only in the Dashboard, regardless of user permission. Updates may only be made via the API or Terraform for this account when enabled.
      default: false
    - name: login_design
      value:
        background_color: "{{ background_color }}"
        footer_text: "{{ footer_text }}"
        header_text: "{{ header_text }}"
        logo_path: "{{ logo_path }}"
        text_color: "{{ text_color }}"
    - name: mfa_config
      description: |
        Configures multi-factor authentication (MFA) settings for an organization.
      value:
        allowed_authenticators:
          - "{{ allowed_authenticators }}"
        amr_matching_session_duration: "{{ amr_matching_session_duration }}"
        required_aaguids: "{{ required_aaguids }}"
        session_duration: "{{ session_duration }}"
    - name: mfa_required_for_all_apps
      value: {{ mfa_required_for_all_apps }}
      description: |
        Determines whether global MFA settings apply to applications by default. The organization must have MFA enabled with at least one authentication method and a session duration configured.
      default: false
    - name: mfa_ssh_piv_key_requirements
      description: |
        Configures SSH PIV key requirements for MFA using hardware security keys.
      value:
        pin_policy: "{{ pin_policy }}"
        require_fips_device: {{ require_fips_device }}
        ssh_key_size:
          - {{ ssh_key_size }}
        ssh_key_type:
          - "{{ ssh_key_type }}"
        touch_policy: "{{ touch_policy }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of your Zero Trust organization.
    - name: session_duration
      value: "{{ session_duration }}"
      description: |
        The amount of time that tokens issued for applications will be valid. Must be in the format \`300ms\` or \`2h45m\`. Valid time units are: ns, us (or µs), ms, s, m, h.
    - name: ui_read_only_toggle_reason
      value: "{{ ui_read_only_toggle_reason }}"
      description: |
        A description of the reason why the UI read only field is being toggled.
    - name: user_seat_expiration_inactive_time
      value: "{{ user_seat_expiration_inactive_time }}"
      description: |
        The amount of time a user seat is inactive before it expires. When the user seat exceeds the set time of inactivity, the user is removed as an active seat and no longer counts against your Teams seat count. Minimum value for this setting is 1 month (730h). Must be in the format \`300ms\` or \`2h45m\`. Valid time units are: \`ns\`, \`us\` (or \`µs\`), \`ms\`, \`s\`, \`m\`, \`h\`.
    - name: warp_auth_session_duration
      value: "{{ warp_auth_session_duration }}"
      description: |
        The amount of time that tokens issued for applications will be valid. Must be in the format \`30m\` or \`2h45m\`. Valid time units are: m, h.
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

Updates the configuration for your Zero Trust organization.

```sql
REPLACE cloudflare.zero_trust.organizations
SET 
allow_authenticate_via_warp = {{ allow_authenticate_via_warp }},
auth_domain = '{{ auth_domain }}',
auto_redirect_to_identity = {{ auto_redirect_to_identity }},
custom_pages = '{{ custom_pages }}',
deny_unmatched_requests = {{ deny_unmatched_requests }},
deny_unmatched_requests_exempted_zone_names = '{{ deny_unmatched_requests_exempted_zone_names }}',
is_ui_read_only = {{ is_ui_read_only }},
login_design = '{{ login_design }}',
mfa_config = '{{ mfa_config }}',
mfa_required_for_all_apps = {{ mfa_required_for_all_apps }},
mfa_ssh_piv_key_requirements = '{{ mfa_ssh_piv_key_requirements }}',
name = '{{ name }}',
session_duration = '{{ session_duration }}',
ui_read_only_toggle_reason = '{{ ui_read_only_toggle_reason }}',
user_seat_expiration_inactive_time = '{{ user_seat_expiration_inactive_time }}',
warp_auth_session_duration = '{{ warp_auth_session_duration }}'
WHERE 
account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates the configuration for your Zero Trust organization.

```sql
REPLACE cloudflare.zero_trust.organizations
SET 
allow_authenticate_via_warp = {{ allow_authenticate_via_warp }},
auth_domain = '{{ auth_domain }}',
auto_redirect_to_identity = {{ auto_redirect_to_identity }},
custom_pages = '{{ custom_pages }}',
deny_unmatched_requests = {{ deny_unmatched_requests }},
deny_unmatched_requests_exempted_zone_names = '{{ deny_unmatched_requests_exempted_zone_names }}',
is_ui_read_only = {{ is_ui_read_only }},
login_design = '{{ login_design }}',
mfa_config = '{{ mfa_config }}',
mfa_required_for_all_apps = {{ mfa_required_for_all_apps }},
mfa_ssh_piv_key_requirements = '{{ mfa_ssh_piv_key_requirements }}',
name = '{{ name }}',
session_duration = '{{ session_duration }}',
ui_read_only_toggle_reason = '{{ ui_read_only_toggle_reason }}',
user_seat_expiration_inactive_time = '{{ user_seat_expiration_inactive_time }}',
warp_auth_session_duration = '{{ warp_auth_session_duration }}'
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoke_users_by_account"
    values={[
        { label: 'revoke_users_by_account', value: 'revoke_users_by_account' },
        { label: 'revoke_users_by_zone', value: 'revoke_users_by_zone' }
    ]}
>
<TabItem value="revoke_users_by_account">

Revokes a user's access across all applications.

```sql
EXEC cloudflare.zero_trust.organizations.revoke_users_by_account 
@account_id='{{ account_id }}' --required, 
@devices={{ devices }} 
@@json=
'{
"devices": {{ devices }}, 
"email": "{{ email }}", 
"user_uid": "{{ user_uid }}", 
"warp_session_reauth": {{ warp_session_reauth }}
}'
;
```
</TabItem>
<TabItem value="revoke_users_by_zone">

Revokes a user's access across all applications.

```sql
EXEC cloudflare.zero_trust.organizations.revoke_users_by_zone 
@zone_id='{{ zone_id }}' --required, 
@devices={{ devices }} 
@@json=
'{
"devices": {{ devices }}, 
"email": "{{ email }}", 
"user_uid": "{{ user_uid }}", 
"warp_session_reauth": {{ warp_session_reauth }}
}'
;
```
</TabItem>
</Tabs>
