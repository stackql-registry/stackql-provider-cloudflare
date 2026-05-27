--- 
title: identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_providers
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

Creates, updates, deletes, gets or lists an <code>identity_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="identity_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.identity_providers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get an Access identity provider response

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
    <td>The name of the identity provider, shown to users on the login page. (example: Widget Corps IDP)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).</td>
</tr>
<tr>
    <td><CopyableCode code="scim_config" /></td>
    <td><code>object</code></td>
    <td>The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of identity provider. To determine the value for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/). (onetimepin, azureAD, saml, centrify, facebook, github, google-apps, google, linkedin, oidc, okta, onelogin, pingone, yandex) (example: onetimepin)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get an Access identity provider response

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
    <td>The name of the identity provider, shown to users on the login page. (example: Widget Corps IDP)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).</td>
</tr>
<tr>
    <td><CopyableCode code="scim_config" /></td>
    <td><code>object</code></td>
    <td>The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of identity provider. To determine the value for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/). (onetimepin, azureAD, saml, centrify, facebook, github, google-apps, google, linkedin, oidc, okta, onelogin, pingone, yandex) (example: onetimepin)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List Access identity providers response

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
    <td>The name of the identity provider, shown to users on the login page. (example: Widget Corps IDP)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).</td>
</tr>
<tr>
    <td><CopyableCode code="scim_config" /></td>
    <td><code>object</code></td>
    <td>The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of identity provider. To determine the value for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/). (onetimepin, azureAD, saml, centrify, facebook, github, google-apps, google, linkedin, oidc, okta, onelogin, pingone, yandex) (example: onetimepin)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List Access identity providers response

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
    <td>The name of the identity provider, shown to users on the login page. (example: Widget Corps IDP)</td>
</tr>
<tr>
    <td><CopyableCode code="config" /></td>
    <td><code>object</code></td>
    <td>The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).</td>
</tr>
<tr>
    <td><CopyableCode code="scim_config" /></td>
    <td><code>object</code></td>
    <td>The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of identity provider. To determine the value for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/). (onetimepin, azureAD, saml, centrify, facebook, github, google-apps, google, linkedin, oidc, okta, onelogin, pingone, yandex) (example: onetimepin)</td>
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
    <td><a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a configured identity provider.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches a configured identity provider.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-scim_enabled"><code>scim_enabled</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all configured identity providers.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-scim_enabled"><code>scim_enabled</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists all configured identity providers.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-config"><code>config</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Adds a new identity provider to Access.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-config"><code>config</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Adds a new identity provider to Access.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-config"><code>config</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates a configured identity provider.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-config"><code>config</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates a configured identity provider.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an identity provider from Access.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an identity provider from Access.</td>
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
<tr id="parameter-identity_provider_id">
    <td><CopyableCode code="identity_provider_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
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
<tr id="parameter-scim_enabled">
    <td><CopyableCode code="scim_enabled" /></td>
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
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches a configured identity provider.

```sql
SELECT
id,
name,
config,
scim_config,
type
FROM cloudflare.zero_trust.identity_providers
WHERE identity_provider_id = '{{ identity_provider_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches a configured identity provider.

```sql
SELECT
id,
name,
config,
scim_config,
type
FROM cloudflare.zero_trust.identity_providers
WHERE identity_provider_id = '{{ identity_provider_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Lists all configured identity providers.

```sql
SELECT
id,
name,
config,
scim_config,
type
FROM cloudflare.zero_trust.identity_providers
WHERE account_id = '{{ account_id }}' -- required
AND scim_enabled = '{{ scim_enabled }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Lists all configured identity providers.

```sql
SELECT
id,
name,
config,
scim_config,
type
FROM cloudflare.zero_trust.identity_providers
WHERE zone_id = '{{ zone_id }}' -- required
AND scim_enabled = '{{ scim_enabled }}'
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

Adds a new identity provider to Access.

```sql
INSERT INTO cloudflare.zero_trust.identity_providers (
config,
name,
scim_config,
type,
account_id
)
SELECT 
'{{ config }}' /* required */,
'{{ name }}' /* required */,
'{{ scim_config }}',
'{{ type }}' /* required */,
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

Adds a new identity provider to Access.

```sql
INSERT INTO cloudflare.zero_trust.identity_providers (
config,
name,
scim_config,
type,
zone_id
)
SELECT 
'{{ config }}' /* required */,
'{{ name }}' /* required */,
'{{ scim_config }}',
'{{ type }}' /* required */,
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
- name: identity_providers
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the identity_providers resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the identity_providers resource.
    - name: config
      description: |
        The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
      value:
        client_id: "{{ client_id }}"
        client_secret: "{{ client_secret }}"
        claims:
          - "{{ claims }}"
        email_claim_name: "{{ email_claim_name }}"
        conditional_access_enabled: {{ conditional_access_enabled }}
        directory_id: "{{ directory_id }}"
        prompt: "{{ prompt }}"
        support_groups: {{ support_groups }}
    - name: name
      value: "{{ name }}"
      description: |
        The name of the identity provider, shown to users on the login page.
    - name: scim_config
      description: |
        The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
      value:
        enabled: {{ enabled }}
        identity_update_behavior: "{{ identity_update_behavior }}"
        scim_base_url: "{{ scim_base_url }}"
        seat_deprovision: {{ seat_deprovision }}
        secret: "{{ secret }}"
        user_deprovision: {{ user_deprovision }}
    - name: type
      value: "{{ type }}"
      description: |
        The type of identity provider. To determine the value for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
      valid_values: ['onetimepin', 'azureAD', 'saml', 'centrify', 'facebook', 'github', 'google-apps', 'google', 'linkedin', 'oidc', 'okta', 'onelogin', 'pingone', 'yandex']
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

Updates a configured identity provider.

```sql
REPLACE cloudflare.zero_trust.identity_providers
SET 
config = '{{ config }}',
name = '{{ name }}',
scim_config = '{{ scim_config }}',
type = '{{ type }}'
WHERE 
identity_provider_id = '{{ identity_provider_id }}' --required
AND account_id = '{{ account_id }}' --required
AND config = '{{ config }}' --required
AND name = '{{ name }}' --required
AND type = '{{ type }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates a configured identity provider.

```sql
REPLACE cloudflare.zero_trust.identity_providers
SET 
config = '{{ config }}',
name = '{{ name }}',
scim_config = '{{ scim_config }}',
type = '{{ type }}'
WHERE 
identity_provider_id = '{{ identity_provider_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND config = '{{ config }}' --required
AND name = '{{ name }}' --required
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

Deletes an identity provider from Access.

```sql
DELETE FROM cloudflare.zero_trust.identity_providers
WHERE identity_provider_id = '{{ identity_provider_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an identity provider from Access.

```sql
DELETE FROM cloudflare.zero_trust.identity_providers
WHERE identity_provider_id = '{{ identity_provider_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
