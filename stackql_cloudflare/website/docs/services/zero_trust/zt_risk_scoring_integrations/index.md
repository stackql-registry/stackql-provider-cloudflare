--- 
title: zt_risk_scoring_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - zt_risk_scoring_integrations
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

Creates, updates, deletes, gets or lists a <code>zt_risk_scoring_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zt_risk_scoring_integrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.zt_risk_scoring_integrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get response.

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
    <td><code>string (uuid)</code></td>
    <td>The id of the integration, a UUIDv4.</td>
</tr>
<tr>
    <td><CopyableCode code="reference_id" /></td>
    <td><code>string</code></td>
    <td>A reference ID defined by the client. Should be set to the Access-Okta IDP integration ID. Useful when the risk-score integration needs to be associated with a secondary asset and recalled using that ID.</td>
</tr>
<tr>
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account tag.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Whether this integration is enabled and should export changes in risk score.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the integration was created in RFC3339 format.</td>
</tr>
<tr>
    <td><CopyableCode code="integration_type" /></td>
    <td><code>string</code></td>
    <td> (Okta)</td>
</tr>
<tr>
    <td><CopyableCode code="tenant_url" /></td>
    <td><code>string</code></td>
    <td>The base URL for the tenant. E.g. "https://tenant.okta.com".</td>
</tr>
<tr>
    <td><CopyableCode code="well_known_url" /></td>
    <td><code>string</code></td>
    <td>The URL for the Shared Signals Framework configuration, e.g. "/.well-known/sse-configuration/&#123;integration_uuid&#125;/". https://openid.net/specs/openid-sse-framework-1_0.html#rfc.section.6.2.1.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List response.

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
    <td><code>string (uuid)</code></td>
    <td>The id of the integration, a UUIDv4.</td>
</tr>
<tr>
    <td><CopyableCode code="reference_id" /></td>
    <td><code>string</code></td>
    <td>A reference ID defined by the client. Should be set to the Access-Okta IDP integration ID. Useful when the risk-score integration needs to be associated with a secondary asset and recalled using that ID.</td>
</tr>
<tr>
    <td><CopyableCode code="account_tag" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare account tag.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Whether this integration is enabled and should export changes in risk score.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the integration was created in RFC3339 format.</td>
</tr>
<tr>
    <td><CopyableCode code="integration_type" /></td>
    <td><code>string</code></td>
    <td> (Okta)</td>
</tr>
<tr>
    <td><CopyableCode code="tenant_url" /></td>
    <td><code>string</code></td>
    <td>The base URL for the tenant. E.g. "https://tenant.okta.com".</td>
</tr>
<tr>
    <td><CopyableCode code="well_known_url" /></td>
    <td><code>string</code></td>
    <td>The URL for the Shared Signals Framework configuration, e.g. "/.well-known/sse-configuration/&#123;integration_uuid&#125;/". https://openid.net/specs/openid-sse-framework-1_0.html#rfc.section.6.2.1.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists all configured Zero Trust risk score integrations for the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_type"><code>integration_type</code></a>, <a href="#parameter-tenant_url"><code>tenant_url</code></a></td>
    <td></td>
    <td>Creates a new Zero Trust risk score integration, connecting external risk signals to Cloudflare's risk scoring system.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a></td>
    <td></td>
    <td>Removes a Zero Trust risk score integration, disconnecting the external risk signal source.</td>
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
<tr id="parameter-integration_id">
    <td><CopyableCode code="integration_id" /></td>
    <td><code>string (uuid)</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get response.

```sql
SELECT
id,
reference_id,
account_tag,
active,
created_at,
integration_type,
tenant_url,
well_known_url
FROM cloudflare.zero_trust.zt_risk_scoring_integrations
WHERE account_id = '{{ account_id }}' -- required
AND integration_id = '{{ integration_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all configured Zero Trust risk score integrations for the account.

```sql
SELECT
id,
reference_id,
account_tag,
active,
created_at,
integration_type,
tenant_url,
well_known_url
FROM cloudflare.zero_trust.zt_risk_scoring_integrations
WHERE account_id = '{{ account_id }}' -- required
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

Creates a new Zero Trust risk score integration, connecting external risk signals to Cloudflare's risk scoring system.

```sql
INSERT INTO cloudflare.zero_trust.zt_risk_scoring_integrations (
integration_type,
reference_id,
tenant_url,
account_id
)
SELECT 
'{{ integration_type }}' /* required */,
'{{ reference_id }}',
'{{ tenant_url }}' /* required */,
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
- name: zt_risk_scoring_integrations
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the zt_risk_scoring_integrations resource.
    - name: integration_type
      value: "{{ integration_type }}"
      valid_values: ['Okta']
    - name: reference_id
      value: "{{ reference_id }}"
      description: |
        A reference id that can be supplied by the client. Currently this should be set to the Access-Okta IDP ID (a UUIDv4). https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider
    - name: tenant_url
      value: "{{ tenant_url }}"
      description: |
        The base url of the tenant, e.g. "https://tenant.okta.com".
`}</CodeBlock>

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

Removes a Zero Trust risk score integration, disconnecting the external risk signal source.

```sql
DELETE FROM cloudflare.zero_trust.zt_risk_scoring_integrations
WHERE account_id = '{{ account_id }}' --required
AND integration_id = '{{ integration_id }}' --required
;
```
</TabItem>
</Tabs>
