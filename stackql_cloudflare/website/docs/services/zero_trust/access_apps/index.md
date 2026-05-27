--- 
title: access_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - access_apps
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

Creates, updates, deletes, gets or lists an <code>access_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.access_apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Get an Access application response

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
<TabItem value="get_by_zone">

Get an Access application response

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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches information about an Access application.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches information about an Access application.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-aud"><code>aud</code></a>, <a href="#parameter-target_attributes"><code>target_attributes</code></a>, <a href="#parameter-exact"><code>exact</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all Access applications in an account or zone.</td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

Fetches information about an Access application.

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
FROM cloudflare.zero_trust.access_apps
WHERE app_id = '{{ app_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches information about an Access application.

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
FROM cloudflare.zero_trust.access_apps
WHERE app_id = '{{ app_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
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
FROM cloudflare.zero_trust.access_apps
WHERE account_id = '{{ account_id }}' -- required
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
