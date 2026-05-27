--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.applications" /></td></tr>
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

List Access applications response

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
    <td>The name of the application. (example: Admin Site)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_authenticate_via_warp" /></td>
    <td><code>boolean</code></td>
    <td>When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="allow_iframe" /></td>
    <td><code>boolean</code></td>
    <td>Enables loading application content in an iFrame.</td>
</tr>
<tr>
    <td><CopyableCode code="allowed_idps" /></td>
    <td><code>array</code></td>
    <td>The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.</td>
</tr>
<tr>
    <td><CopyableCode code="app_launcher_logo_url" /></td>
    <td><code>string</code></td>
    <td>The image URL of the logo shown in the App Launcher header. (example: https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg)</td>
</tr>
<tr>
    <td><CopyableCode code="app_launcher_visible" /></td>
    <td><code>boolean</code></td>
    <td>Displays the application in the App Launcher.</td>
</tr>
<tr>
    <td><CopyableCode code="aud" /></td>
    <td><code>string</code></td>
    <td>Audience tag. (example: 737646a56ab1df6ec9bddc7e5ca84eaf3b0768850f3ffb5d74f1534911fe3893)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_redirect_to_identity" /></td>
    <td><code>boolean</code></td>
    <td>When set to `true`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.</td>
</tr>
<tr>
    <td><CopyableCode code="bg_color" /></td>
    <td><code>string</code></td>
    <td>The background color of the App Launcher page. (example: #ff0000)</td>
</tr>
<tr>
    <td><CopyableCode code="cors_headers" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_deny_message" /></td>
    <td><code>string</code></td>
    <td>The custom error message shown to a user when they are denied access to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_deny_url" /></td>
    <td><code>string</code></td>
    <td>The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_non_identity_deny_url" /></td>
    <td><code>string</code></td>
    <td>The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.</td>
</tr>
<tr>
    <td><CopyableCode code="custom_pages" /></td>
    <td><code>array</code></td>
    <td>The custom pages that will be displayed when applicable for this application</td>
</tr>
<tr>
    <td><CopyableCode code="destinations" /></td>
    <td><code>array</code></td>
    <td>List of destinations secured by Access. This supersedes `self_hosted_domains` to allow for more flexibility in defining different types of domains. If `destinations` are provided, then `self_hosted_domains` will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher. (example: test.example.com/admin)</td>
</tr>
<tr>
    <td><CopyableCode code="enable_binding_cookie" /></td>
    <td><code>boolean</code></td>
    <td>Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="footer_links" /></td>
    <td><code>array</code></td>
    <td>The links in the App Launcher footer.</td>
</tr>
<tr>
    <td><CopyableCode code="header_bg_color" /></td>
    <td><code>string</code></td>
    <td>The background color of the App Launcher header. (example: #ff0000)</td>
</tr>
<tr>
    <td><CopyableCode code="http_only_cookie_attribute" /></td>
    <td><code>boolean</code></td>
    <td>Enables the HttpOnly cookie attribute, which increases security against XSS attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="landing_page_design" /></td>
    <td><code>object</code></td>
    <td>The design of the App Launcher landing page shown to users when they log in.</td>
</tr>
<tr>
    <td><CopyableCode code="logo_url" /></td>
    <td><code>string</code></td>
    <td>The image URL for the logo shown in the App Launcher dashboard. (example: https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg)</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth_configuration" /></td>
    <td><code>object</code></td>
    <td>**Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.</td>
</tr>
<tr>
    <td><CopyableCode code="options_preflight_bypass" /></td>
    <td><code>boolean</code></td>
    <td>Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.</td>
</tr>
<tr>
    <td><CopyableCode code="path_cookie_attribute" /></td>
    <td><code>boolean</code></td>
    <td>Enables cookie paths to scope an application's JWT to the application path. If disabled, the JWT will scope to the hostname by default</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="read_service_tokens_from_header" /></td>
    <td><code>string</code></td>
    <td>Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: &#123; "cf-access-client-id": "88bf3b6d86161464f6509f7219099e57.access.example.com", "cf-access-client-secret": "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" &#125; (example: Authorization)</td>
</tr>
<tr>
    <td><CopyableCode code="saas_app" /></td>
    <td><code>object</code></td>
    <td> (title: SAML SaaS App)</td>
</tr>
<tr>
    <td><CopyableCode code="same_site_cookie_attribute" /></td>
    <td><code>string</code></td>
    <td>Sets the SameSite cookie setting, which provides increased security against CSRF attacks. (example: strict)</td>
</tr>
<tr>
    <td><CopyableCode code="scim_config" /></td>
    <td><code>object</code></td>
    <td>Configuration for provisioning to this application via SCIM. This is currently in closed beta.</td>
</tr>
<tr>
    <td><CopyableCode code="self_hosted_domains" /></td>
    <td><code>array</code></td>
    <td>List of public domains that Access will secure. This field is deprecated in favor of `destinations` and will be supported until **November 21, 2025.** If `destinations` are provided, then `self_hosted_domains` will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="service_auth_401_redirect" /></td>
    <td><code>boolean</code></td>
    <td>Returns a 401 status code when the request is blocked by a Service Auth policy.</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for this application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="skip_app_launcher_login_page" /></td>
    <td><code>boolean</code></td>
    <td>Determines when to skip the App Launcher landing page.</td>
</tr>
<tr>
    <td><CopyableCode code="skip_interstitial" /></td>
    <td><code>boolean</code></td>
    <td>Enables automatic authentication through cloudflared.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="target_criteria" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The application type. (self_hosted, saas, ssh, vnc, app_launcher, warp, biso, bookmark, dash_sso, infrastructure, rdp, mcp, mcp_portal, proxy_endpoint) (example: self_hosted)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="use_clientless_isolation_app_launcher_url" /></td>
    <td><code>boolean</code></td>
    <td>Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-aud"><code>aud</code></a>, <a href="#parameter-target_attributes"><code>target_attributes</code></a>, <a href="#parameter-exact"><code>exact</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all Access applications in an account or zone.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Adds a new application to Access.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Adds a new application to Access.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates an Access application.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates an Access application.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an application from Access.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an application from Access.</td>
</tr>
<tr>
    <td><a href="#revoke_tokens_by_account"><CopyableCode code="revoke_tokens_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Revokes all tokens issued for an application.</td>
</tr>
<tr>
    <td><a href="#revoke_tokens_by_zone"><CopyableCode code="revoke_tokens_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Revokes all tokens issued for an application.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-aud">
    <td><CopyableCode code="aud" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-exact">
    <td><CopyableCode code="exact" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
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
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-target_attributes">
    <td><CopyableCode code="target_attributes" /></td>
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

Lists all Access applications in an account or zone.

```sql
SELECT
id,
name,
allow_authenticate_via_warp,
allow_iframe,
allowed_idps,
app_launcher_logo_url,
app_launcher_visible,
aud,
auto_redirect_to_identity,
bg_color,
cors_headers,
created_at,
custom_deny_message,
custom_deny_url,
custom_non_identity_deny_url,
custom_pages,
destinations,
domain,
enable_binding_cookie,
footer_links,
header_bg_color,
http_only_cookie_attribute,
landing_page_design,
logo_url,
mfa_config,
oauth_configuration,
options_preflight_bypass,
path_cookie_attribute,
policies,
read_service_tokens_from_header,
saas_app,
same_site_cookie_attribute,
scim_config,
self_hosted_domains,
service_auth_401_redirect,
session_duration,
skip_app_launcher_login_page,
skip_interstitial,
tags,
target_criteria,
type,
updated_at,
use_clientless_isolation_app_launcher_url
FROM cloudflare.zero_trust.applications
WHERE zone_id = '{{ zone_id }}' -- required
AND name = '{{ name }}'
AND domain = '{{ domain }}'
AND aud = '{{ aud }}'
AND target_attributes = '{{ target_attributes }}'
AND exact = '{{ exact }}'
AND search = '{{ search }}'
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
        { label: 'create_by_zone', value: 'create_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Adds a new application to Access.

```sql
INSERT INTO cloudflare.zero_trust.applications (
allow_authenticate_via_warp,
allow_iframe,
allowed_idps,
app_launcher_visible,
auto_redirect_to_identity,
cors_headers,
custom_deny_message,
custom_deny_url,
custom_non_identity_deny_url,
custom_pages,
destinations,
domain,
enable_binding_cookie,
http_only_cookie_attribute,
logo_url,
mfa_config,
name,
oauth_configuration,
options_preflight_bypass,
path_cookie_attribute,
read_service_tokens_from_header,
same_site_cookie_attribute,
scim_config,
self_hosted_domains,
service_auth_401_redirect,
session_duration,
skip_interstitial,
tags,
type,
use_clientless_isolation_app_launcher_url,
policies,
saas_app,
app_launcher_logo_url,
bg_color,
footer_links,
header_bg_color,
landing_page_design,
skip_app_launcher_login_page,
target_criteria,
account_id
)
SELECT 
{{ allow_authenticate_via_warp }},
{{ allow_iframe }},
'{{ allowed_idps }}',
{{ app_launcher_visible }},
{{ auto_redirect_to_identity }},
'{{ cors_headers }}',
'{{ custom_deny_message }}',
'{{ custom_deny_url }}',
'{{ custom_non_identity_deny_url }}',
'{{ custom_pages }}',
'{{ destinations }}',
'{{ domain }}',
{{ enable_binding_cookie }},
{{ http_only_cookie_attribute }},
'{{ logo_url }}',
'{{ mfa_config }}',
'{{ name }}',
'{{ oauth_configuration }}',
{{ options_preflight_bypass }},
{{ path_cookie_attribute }},
'{{ read_service_tokens_from_header }}',
'{{ same_site_cookie_attribute }}',
'{{ scim_config }}',
'{{ self_hosted_domains }}',
{{ service_auth_401_redirect }},
'{{ session_duration }}',
{{ skip_interstitial }},
'{{ tags }}',
'{{ type }}' /* required */,
{{ use_clientless_isolation_app_launcher_url }},
'{{ policies }}',
'{{ saas_app }}',
'{{ app_launcher_logo_url }}',
'{{ bg_color }}',
'{{ footer_links }}',
'{{ header_bg_color }}',
'{{ landing_page_design }}',
{{ skip_app_launcher_login_page }},
'{{ target_criteria }}',
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

Adds a new application to Access.

```sql
INSERT INTO cloudflare.zero_trust.applications (
allow_authenticate_via_warp,
allow_iframe,
allowed_idps,
app_launcher_visible,
auto_redirect_to_identity,
cors_headers,
custom_deny_message,
custom_deny_url,
custom_non_identity_deny_url,
custom_pages,
destinations,
domain,
enable_binding_cookie,
http_only_cookie_attribute,
logo_url,
mfa_config,
name,
oauth_configuration,
options_preflight_bypass,
path_cookie_attribute,
read_service_tokens_from_header,
same_site_cookie_attribute,
scim_config,
self_hosted_domains,
service_auth_401_redirect,
session_duration,
skip_interstitial,
tags,
type,
use_clientless_isolation_app_launcher_url,
policies,
saas_app,
app_launcher_logo_url,
bg_color,
footer_links,
header_bg_color,
landing_page_design,
skip_app_launcher_login_page,
target_criteria,
zone_id
)
SELECT 
{{ allow_authenticate_via_warp }},
{{ allow_iframe }},
'{{ allowed_idps }}',
{{ app_launcher_visible }},
{{ auto_redirect_to_identity }},
'{{ cors_headers }}',
'{{ custom_deny_message }}',
'{{ custom_deny_url }}',
'{{ custom_non_identity_deny_url }}',
'{{ custom_pages }}',
'{{ destinations }}',
'{{ domain }}',
{{ enable_binding_cookie }},
{{ http_only_cookie_attribute }},
'{{ logo_url }}',
'{{ mfa_config }}',
'{{ name }}',
'{{ oauth_configuration }}',
{{ options_preflight_bypass }},
{{ path_cookie_attribute }},
'{{ read_service_tokens_from_header }}',
'{{ same_site_cookie_attribute }}',
'{{ scim_config }}',
'{{ self_hosted_domains }}',
{{ service_auth_401_redirect }},
'{{ session_duration }}',
{{ skip_interstitial }},
'{{ tags }}',
'{{ type }}' /* required */,
{{ use_clientless_isolation_app_launcher_url }},
'{{ policies }}',
'{{ saas_app }}',
'{{ app_launcher_logo_url }}',
'{{ bg_color }}',
'{{ footer_links }}',
'{{ header_bg_color }}',
'{{ landing_page_design }}',
{{ skip_app_launcher_login_page }},
'{{ target_criteria }}',
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
- name: applications
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the applications resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the applications resource.
    - name: allow_authenticate_via_warp
      value: {{ allow_authenticate_via_warp }}
      description: |
        When set to true, users can authenticate to this application using their WARP session. When set to false this application will always require direct IdP authentication. This setting always overrides the organization setting for WARP authentication.
    - name: allow_iframe
      value: {{ allow_iframe }}
      description: |
        Enables loading application content in an iFrame.
    - name: allowed_idps
      value:
        - "{{ allowed_idps }}"
      description: |
        The identity providers your users can select when connecting to this application. Defaults to all IdPs configured in your account.
    - name: app_launcher_visible
      value: {{ app_launcher_visible }}
      description: |
        Displays the application in the App Launcher.
      default: true
    - name: auto_redirect_to_identity
      value: {{ auto_redirect_to_identity }}
      description: |
        When set to \`true\`, users skip the identity provider selection step during login. You must specify only one identity provider in allowed_idps.
      default: false
    - name: cors_headers
      value:
        allow_all_headers: {{ allow_all_headers }}
        allow_all_methods: {{ allow_all_methods }}
        allow_all_origins: {{ allow_all_origins }}
        allow_credentials: {{ allow_credentials }}
        allowed_headers:
          - "{{ allowed_headers }}"
        allowed_methods:
          - "{{ allowed_methods }}"
        allowed_origins:
          - "{{ allowed_origins }}"
        max_age: {{ max_age }}
    - name: custom_deny_message
      value: "{{ custom_deny_message }}"
      description: |
        The custom error message shown to a user when they are denied access to the application.
    - name: custom_deny_url
      value: "{{ custom_deny_url }}"
      description: |
        The custom URL a user is redirected to when they are denied access to the application when failing identity-based rules.
    - name: custom_non_identity_deny_url
      value: "{{ custom_non_identity_deny_url }}"
      description: |
        The custom URL a user is redirected to when they are denied access to the application when failing non-identity rules.
    - name: custom_pages
      value:
        - "{{ custom_pages }}"
      description: |
        The custom pages that will be displayed when applicable for this application
    - name: destinations
      description: |
        List of destinations secured by Access. This supersedes \`self_hosted_domains\` to allow for more flexibility in defining different types of domains. If \`destinations\` are provided, then \`self_hosted_domains\` will be ignored.
      value:
        - type: "{{ type }}"
          uri: "{{ uri }}"
          cidr: "{{ cidr }}"
          hostname: "{{ hostname }}"
          l4_protocol: "{{ l4_protocol }}"
          port_range: "{{ port_range }}"
          vnet_id: "{{ vnet_id }}"
          mcp_server_id: "{{ mcp_server_id }}"
      default: 
    - name: domain
      value: "{{ domain }}"
      description: |
        The primary hostname and path secured by Access. This domain will be displayed if the app is visible in the App Launcher.
    - name: enable_binding_cookie
      value: {{ enable_binding_cookie }}
      description: |
        Enables the binding cookie, which increases security against compromised authorization tokens and CSRF attacks.
      default: false
    - name: http_only_cookie_attribute
      value: {{ http_only_cookie_attribute }}
      description: |
        Enables the HttpOnly cookie attribute, which increases security against XSS attacks.
      default: true
    - name: logo_url
      value: "{{ logo_url }}"
      description: |
        The image URL for the logo shown in the App Launcher dashboard.
    - name: mfa_config
      description: |
        Configures multi-factor authentication (MFA) settings.
      value:
        allowed_authenticators:
          - "{{ allowed_authenticators }}"
        mfa_disabled: {{ mfa_disabled }}
        session_duration: "{{ session_duration }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the application.
    - name: oauth_configuration
      description: |
        **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
      value:
        dynamic_client_registration:
          allow_any_on_localhost: {{ allow_any_on_localhost }}
          allow_any_on_loopback: {{ allow_any_on_loopback }}
          allowed_uris:
            - "{{ allowed_uris }}"
          enabled: {{ enabled }}
        enabled: {{ enabled }}
        grant:
          access_token_lifetime: "{{ access_token_lifetime }}"
          session_duration: "{{ session_duration }}"
    - name: options_preflight_bypass
      value: {{ options_preflight_bypass }}
      description: |
        Allows options preflight requests to bypass Access authentication and go directly to the origin. Cannot turn on if cors_headers is set.
    - name: path_cookie_attribute
      value: {{ path_cookie_attribute }}
      description: |
        Enables cookie paths to scope an application's JWT to the application path. If disabled, the JWT will scope to the hostname by default
      default: false
    - name: read_service_tokens_from_header
      value: "{{ read_service_tokens_from_header }}"
      description: |
        Allows matching Access Service Tokens passed HTTP in a single header with this name. This works as an alternative to the (CF-Access-Client-Id, CF-Access-Client-Secret) pair of headers. The header value will be interpreted as a json object similar to: { "cf-access-client-id": "88bf3b6d86161464f6509f7219099e57.access.example.com", "cf-access-client-secret": "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
    - name: same_site_cookie_attribute
      value: "{{ same_site_cookie_attribute }}"
      description: |
        Sets the SameSite cookie setting, which provides increased security against CSRF attacks.
    - name: scim_config
      description: |
        Configuration for provisioning to this application via SCIM. This is currently in closed beta.
      value:
        authentication:
          password: "{{ password }}"
          scheme: "{{ scheme }}"
          user: "{{ user }}"
          token: "{{ token }}"
          authorization_url: "{{ authorization_url }}"
          client_id: "{{ client_id }}"
          client_secret: "{{ client_secret }}"
          scopes:
            - "{{ scopes }}"
          token_url: "{{ token_url }}"
        deactivate_on_delete: {{ deactivate_on_delete }}
        enabled: {{ enabled }}
        idp_uid: "{{ idp_uid }}"
        mappings:
          - enabled: {{ enabled }}
            filter: "{{ filter }}"
            operations:
              create: {{ create }}
              delete: {{ delete }}
              update: {{ update }}
            schema: "{{ schema }}"
            strictness: "{{ strictness }}"
            transform_jsonata: "{{ transform_jsonata }}"
        remote_uri: "{{ remote_uri }}"
    - name: self_hosted_domains
      value:
        - "{{ self_hosted_domains }}"
      description: |
        List of public domains that Access will secure. This field is deprecated in favor of \`destinations\` and will be supported until **November 21, 2025.** If \`destinations\` are provided, then \`self_hosted_domains\` will be ignored.
      default: 
    - name: service_auth_401_redirect
      value: {{ service_auth_401_redirect }}
      description: |
        Returns a 401 status code when the request is blocked by a Service Auth policy.
    - name: session_duration
      value: "{{ session_duration }}"
      description: |
        The amount of time that tokens issued for this application will be valid. Must be in the format \`300ms\` or \`2h45m\`. Valid time units are: ns, us (or µs), ms, s, m, h. Note: unsupported for infrastructure type applications.
      default: 24h
    - name: skip_interstitial
      value: {{ skip_interstitial }}
      description: |
        Enables automatic authentication through cloudflared.
    - name: tags
      value:
        - "{{ tags }}"
      description: |
        The tags you want assigned to an application. Tags are used to filter applications in the App Launcher dashboard.
      default: 
    - name: type
      value: "{{ type }}"
      description: |
        The application type.
      valid_values: ['self_hosted', 'saas', 'ssh', 'vnc', 'app_launcher', 'warp', 'biso', 'bookmark', 'dash_sso', 'infrastructure', 'rdp', 'mcp', 'mcp_portal', 'proxy_endpoint']
    - name: use_clientless_isolation_app_launcher_url
      value: {{ use_clientless_isolation_app_launcher_url }}
      description: |
        Determines if users can access this application via a clientless browser isolation URL. This allows users to access private domains without connecting to Gateway. The option requires Clientless Browser Isolation to be set up with policies that allow users of this application.
      default: false
    - name: policies
      description: |
        The policies that Access applies to the application, in ascending order of precedence. Items can reference existing policies or create new policies exclusive to the application. Reusable and inline policies are mutually exclusive.
      value:
        - id: "{{ id }}"
          precedence: {{ precedence }}
          approval_groups: "{{ approval_groups }}"
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
    - name: saas_app
      value:
        auth_type: "{{ auth_type }}"
        consumer_service_url: "{{ consumer_service_url }}"
        created_at: "{{ created_at }}"
        custom_attributes:
          - friendly_name: "{{ friendly_name }}"
            name: "{{ name }}"
            name_format: "{{ name_format }}"
            source:
              name: "{{ name }}"
              name_by_idp:
                - idp_id: "{{ idp_id }}"
                  source_name: "{{ source_name }}"
        default_relay_state: "{{ default_relay_state }}"
        idp_entity_id: "{{ idp_entity_id }}"
        name_id_format: "{{ name_id_format }}"
        name_id_transform_jsonata: "{{ name_id_transform_jsonata }}"
        public_key: "{{ public_key }}"
        saml_attribute_transform_jsonata: "{{ saml_attribute_transform_jsonata }}"
        sp_entity_id: "{{ sp_entity_id }}"
        sso_endpoint: "{{ sso_endpoint }}"
        updated_at: "{{ updated_at }}"
        access_token_lifetime: "{{ access_token_lifetime }}"
        allow_pkce_without_client_secret: {{ allow_pkce_without_client_secret }}
        app_launcher_url: "{{ app_launcher_url }}"
        client_id: "{{ client_id }}"
        client_secret: "{{ client_secret }}"
        custom_claims:
          - name: "{{ name }}"
            scope: "{{ scope }}"
            source:
              name: "{{ name }}"
              name_by_idp: "{{ name_by_idp }}"
        grant_types:
          - "{{ grant_types }}"
        group_filter_regex: "{{ group_filter_regex }}"
        hybrid_and_implicit_options:
          return_access_token_from_authorization_endpoint: {{ return_access_token_from_authorization_endpoint }}
          return_id_token_from_authorization_endpoint: {{ return_id_token_from_authorization_endpoint }}
        redirect_uris:
          - "{{ redirect_uris }}"
        refresh_token_options:
          lifetime: "{{ lifetime }}"
        scopes:
          - "{{ scopes }}"
    - name: app_launcher_logo_url
      value: "{{ app_launcher_logo_url }}"
      description: |
        The image URL of the logo shown in the App Launcher header.
    - name: bg_color
      value: "{{ bg_color }}"
      description: |
        The background color of the App Launcher page.
    - name: footer_links
      description: |
        The links in the App Launcher footer.
      value:
        - name: "{{ name }}"
          url: "{{ url }}"
    - name: header_bg_color
      value: "{{ header_bg_color }}"
      description: |
        The background color of the App Launcher header.
    - name: landing_page_design
      description: |
        The design of the App Launcher landing page shown to users when they log in.
      value:
        button_color: "{{ button_color }}"
        button_text_color: "{{ button_text_color }}"
        image_url: "{{ image_url }}"
        message: "{{ message }}"
        title: "{{ title }}"
    - name: skip_app_launcher_login_page
      value: {{ skip_app_launcher_login_page }}
      description: |
        Determines when to skip the App Launcher landing page.
      default: false
    - name: target_criteria
      value:
        - port: {{ port }}
          target_attributes: "{{ target_attributes }}"
          protocol: "{{ protocol }}"
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

Updates an Access application.

```sql
REPLACE cloudflare.zero_trust.applications
SET 
allow_authenticate_via_warp = {{ allow_authenticate_via_warp }},
allow_iframe = {{ allow_iframe }},
allowed_idps = '{{ allowed_idps }}',
app_launcher_visible = {{ app_launcher_visible }},
auto_redirect_to_identity = {{ auto_redirect_to_identity }},
cors_headers = '{{ cors_headers }}',
custom_deny_message = '{{ custom_deny_message }}',
custom_deny_url = '{{ custom_deny_url }}',
custom_non_identity_deny_url = '{{ custom_non_identity_deny_url }}',
custom_pages = '{{ custom_pages }}',
destinations = '{{ destinations }}',
domain = '{{ domain }}',
enable_binding_cookie = {{ enable_binding_cookie }},
http_only_cookie_attribute = {{ http_only_cookie_attribute }},
logo_url = '{{ logo_url }}',
mfa_config = '{{ mfa_config }}',
name = '{{ name }}',
oauth_configuration = '{{ oauth_configuration }}',
options_preflight_bypass = {{ options_preflight_bypass }},
path_cookie_attribute = {{ path_cookie_attribute }},
read_service_tokens_from_header = '{{ read_service_tokens_from_header }}',
same_site_cookie_attribute = '{{ same_site_cookie_attribute }}',
scim_config = '{{ scim_config }}',
self_hosted_domains = '{{ self_hosted_domains }}',
service_auth_401_redirect = {{ service_auth_401_redirect }},
session_duration = '{{ session_duration }}',
skip_interstitial = {{ skip_interstitial }},
tags = '{{ tags }}',
type = '{{ type }}',
use_clientless_isolation_app_launcher_url = {{ use_clientless_isolation_app_launcher_url }},
policies = '{{ policies }}',
saas_app = '{{ saas_app }}',
app_launcher_logo_url = '{{ app_launcher_logo_url }}',
bg_color = '{{ bg_color }}',
footer_links = '{{ footer_links }}',
header_bg_color = '{{ header_bg_color }}',
landing_page_design = '{{ landing_page_design }}',
skip_app_launcher_login_page = {{ skip_app_launcher_login_page }},
target_criteria = '{{ target_criteria }}'
WHERE 
app_id = '{{ app_id }}' --required
AND account_id = '{{ account_id }}' --required
AND type = '{{ type }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates an Access application.

```sql
REPLACE cloudflare.zero_trust.applications
SET 
allow_authenticate_via_warp = {{ allow_authenticate_via_warp }},
allow_iframe = {{ allow_iframe }},
allowed_idps = '{{ allowed_idps }}',
app_launcher_visible = {{ app_launcher_visible }},
auto_redirect_to_identity = {{ auto_redirect_to_identity }},
cors_headers = '{{ cors_headers }}',
custom_deny_message = '{{ custom_deny_message }}',
custom_deny_url = '{{ custom_deny_url }}',
custom_non_identity_deny_url = '{{ custom_non_identity_deny_url }}',
custom_pages = '{{ custom_pages }}',
destinations = '{{ destinations }}',
domain = '{{ domain }}',
enable_binding_cookie = {{ enable_binding_cookie }},
http_only_cookie_attribute = {{ http_only_cookie_attribute }},
logo_url = '{{ logo_url }}',
mfa_config = '{{ mfa_config }}',
name = '{{ name }}',
oauth_configuration = '{{ oauth_configuration }}',
options_preflight_bypass = {{ options_preflight_bypass }},
path_cookie_attribute = {{ path_cookie_attribute }},
read_service_tokens_from_header = '{{ read_service_tokens_from_header }}',
same_site_cookie_attribute = '{{ same_site_cookie_attribute }}',
scim_config = '{{ scim_config }}',
self_hosted_domains = '{{ self_hosted_domains }}',
service_auth_401_redirect = {{ service_auth_401_redirect }},
session_duration = '{{ session_duration }}',
skip_interstitial = {{ skip_interstitial }},
tags = '{{ tags }}',
type = '{{ type }}',
use_clientless_isolation_app_launcher_url = {{ use_clientless_isolation_app_launcher_url }},
policies = '{{ policies }}',
saas_app = '{{ saas_app }}',
app_launcher_logo_url = '{{ app_launcher_logo_url }}',
bg_color = '{{ bg_color }}',
footer_links = '{{ footer_links }}',
header_bg_color = '{{ header_bg_color }}',
landing_page_design = '{{ landing_page_design }}',
skip_app_launcher_login_page = {{ skip_app_launcher_login_page }},
target_criteria = '{{ target_criteria }}'
WHERE 
app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND type = '{{ type }}' --required
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

Deletes an application from Access.

```sql
DELETE FROM cloudflare.zero_trust.applications
WHERE app_id = '{{ app_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an application from Access.

```sql
DELETE FROM cloudflare.zero_trust.applications
WHERE app_id = '{{ app_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoke_tokens_by_account"
    values={[
        { label: 'revoke_tokens_by_account', value: 'revoke_tokens_by_account' },
        { label: 'revoke_tokens_by_zone', value: 'revoke_tokens_by_zone' }
    ]}
>
<TabItem value="revoke_tokens_by_account">

Revokes all tokens issued for an application.

```sql
EXEC cloudflare.zero_trust.applications.revoke_tokens_by_account 
@app_id='{{ app_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="revoke_tokens_by_zone">

Revokes all tokens issued for an application.

```sql
EXEC cloudflare.zero_trust.applications.revoke_tokens_by_zone 
@app_id='{{ app_id }}' --required, 
@zone_id='{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
