--- 
title: sso
hide_title: false
hide_table_of_contents: false
keywords:
  - sso
  - iam
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

Creates, updates, deletes, gets or lists a <code>sso</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sso" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.iam.sso" /></td></tr>
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

Get SSO connector response

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
    <td>SSO Connector identifier tag. (title: SSO Connector Identifier, example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the creation of the SSO connector (example: 2025-01-01T12:21:02.0000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="email_domain" /></td>
    <td><code>string</code></td>
    <td> (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the last update of the SSO connector (example: 2025-01-01T12:21:02.0000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="use_fedramp_language" /></td>
    <td><code>boolean</code></td>
    <td>Controls the display of FedRAMP language to the user during SSO login (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="verification" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get all SSO connectors response

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
    <td>SSO Connector identifier tag. (title: SSO Connector Identifier, example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the creation of the SSO connector (example: 2025-01-01T12:21:02.0000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="email_domain" /></td>
    <td><code>string</code></td>
    <td> (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="updated_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for the last update of the SSO connector (example: 2025-01-01T12:21:02.0000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="use_fedramp_language" /></td>
    <td><code>boolean</code></td>
    <td>Controls the display of FedRAMP language to the user during SSO login (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="verification" /></td>
    <td><code>object</code></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sso_connector_id"><code>sso_connector_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#begin_verification"><CopyableCode code="begin_verification" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sso_connector_id"><code>sso_connector_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-email_domain"><code>email_domain</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sso_connector_id"><code>sso_connector_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-sso_connector_id"><code>sso_connector_id</code></a></td>
    <td></td>
    <td></td>
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
<tr id="parameter-sso_connector_id">
    <td><CopyableCode code="sso_connector_id" /></td>
    <td><code>string</code></td>
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

Get SSO connector response

```sql
SELECT
id,
created_on,
email_domain,
enabled,
updated_on,
use_fedramp_language,
verification
FROM cloudflare.iam.sso
WHERE account_id = '{{ account_id }}' -- required
AND sso_connector_id = '{{ sso_connector_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all SSO connectors response

```sql
SELECT
id,
created_on,
email_domain,
enabled,
updated_on,
use_fedramp_language,
verification
FROM cloudflare.iam.sso
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="begin_verification"
    values={[
        { label: 'begin_verification', value: 'begin_verification' },
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="begin_verification">

No description available.

```sql
INSERT INTO cloudflare.iam.sso (
account_id,
sso_connector_id
)
SELECT 
'{{ account_id }}',
'{{ sso_connector_id }}'
RETURNING
errors,
messages,
success
;
```
</TabItem>
<TabItem value="create">

No description available.

```sql
INSERT INTO cloudflare.iam.sso (
begin_verification,
email_domain,
use_fedramp_language,
account_id
)
SELECT 
{{ begin_verification }},
'{{ email_domain }}' /* required */,
{{ use_fedramp_language }},
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
- name: sso
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the sso resource.
    - name: sso_connector_id
      value: "{{ sso_connector_id }}"
      description: Required parameter for the sso resource.
    - name: begin_verification
      value: {{ begin_verification }}
      description: |
        Begin the verification process after creation
      default: true
    - name: email_domain
      value: "{{ email_domain }}"
      description: |
        Email domain of the new SSO connector
    - name: use_fedramp_language
      value: {{ use_fedramp_language }}
      description: |
        Controls the display of FedRAMP language to the user during SSO login
      default: false
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

No description available.

```sql
UPDATE cloudflare.iam.sso
SET 
enabled = {{ enabled }},
use_fedramp_language = {{ use_fedramp_language }}
WHERE 
account_id = '{{ account_id }}' --required
AND sso_connector_id = '{{ sso_connector_id }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

No description available.

```sql
DELETE FROM cloudflare.iam.sso
WHERE account_id = '{{ account_id }}' --required
AND sso_connector_id = '{{ sso_connector_id }}' --required
;
```
</TabItem>
</Tabs>
