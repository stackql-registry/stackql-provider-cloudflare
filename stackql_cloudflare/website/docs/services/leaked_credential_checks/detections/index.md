--- 
title: detections
hide_title: false
hide_table_of_contents: false
keywords:
  - detections
  - leaked_credential_checks
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

Creates, updates, deletes, gets or lists a <code>detections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="detections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.leaked_credential_checks.detections" /></td></tr>
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

Get Leaked Credential Checks custom detection response.

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
    <td>Defines the unique ID for this custom detection. (example: 18a14bafaa8eb1df04ce683ec18c765e)</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Defines ehe ruleset expression to use in matching the password in a request. (example: lookup_json_string(http.request.body.raw, "secret"))</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>Defines the ruleset expression to use in matching the username in a request. (example: lookup_json_string(http.request.body.raw, "user"))</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Leaked Credential Checks custom detections response.

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
    <td>Defines the unique ID for this custom detection. (example: 18a14bafaa8eb1df04ce683ec18c765e)</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Defines ehe ruleset expression to use in matching the password in a request. (example: lookup_json_string(http.request.body.raw, "secret"))</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>Defines the ruleset expression to use in matching the username in a request. (example: lookup_json_string(http.request.body.raw, "user"))</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-detection_id"><code>detection_id</code></a></td>
    <td></td>
    <td>Get user-defined detection pattern for Leaked Credential Checks.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>List user-defined detection patterns for Leaked Credential Checks.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Create user-defined detection pattern for Leaked Credential Checks.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-detection_id"><code>detection_id</code></a></td>
    <td></td>
    <td>Update user-defined detection pattern for Leaked Credential Checks.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-detection_id"><code>detection_id</code></a></td>
    <td></td>
    <td>Remove user-defined detection pattern for Leaked Credential Checks.</td>
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
<tr id="parameter-detection_id">
    <td><CopyableCode code="detection_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get user-defined detection pattern for Leaked Credential Checks.

```sql
SELECT
id,
password,
username
FROM cloudflare.leaked_credential_checks.detections
WHERE zone_id = '{{ zone_id }}' -- required
AND detection_id = '{{ detection_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List user-defined detection patterns for Leaked Credential Checks.

```sql
SELECT
id,
password,
username
FROM cloudflare.leaked_credential_checks.detections
WHERE zone_id = '{{ zone_id }}' -- required
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

Create user-defined detection pattern for Leaked Credential Checks.

```sql
INSERT INTO cloudflare.leaked_credential_checks.detections (
password,
username,
zone_id
)
SELECT 
'{{ password }}',
'{{ username }}',
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
- name: detections
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the detections resource.
    - name: password
      value: "{{ password }}"
      description: |
        Defines ehe ruleset expression to use in matching the password in a request.
    - name: username
      value: "{{ username }}"
      description: |
        Defines the ruleset expression to use in matching the username in a request.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update user-defined detection pattern for Leaked Credential Checks.

```sql
REPLACE cloudflare.leaked_credential_checks.detections
SET 
password = '{{ password }}',
username = '{{ username }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND detection_id = '{{ detection_id }}' --required
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

Remove user-defined detection pattern for Leaked Credential Checks.

```sql
DELETE FROM cloudflare.leaked_credential_checks.detections
WHERE zone_id = '{{ zone_id }}' --required
AND detection_id = '{{ detection_id }}' --required
;
```
</TabItem>
</Tabs>
