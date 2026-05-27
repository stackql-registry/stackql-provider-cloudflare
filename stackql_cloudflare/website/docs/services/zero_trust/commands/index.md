--- 
title: commands
hide_title: false
hide_table_of_contents: false
keywords:
  - commands
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

Creates, updates, deletes, gets or lists a <code>commands</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="commands" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.commands" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_downloads"
    values={[
        { label: 'get_downloads', value: 'get_downloads' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_downloads">

Get command artifacts response

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
    <td><CopyableCode code="contents" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Get commands response

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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="device_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="registration_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the device registration</td>
</tr>
<tr>
    <td><CopyableCode code="completed_date" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="created_date" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="filename" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="user_email" /></td>
    <td><code>string</code></td>
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
    <td><a href="#get_downloads"><CopyableCode code="get_downloads" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-command_id"><code>command_id</code></a>, <a href="#parameter-filename"><code>filename</code></a></td>
    <td></td>
    <td>Downloads artifacts for an executed command. Bulk downloads are not supported</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a>, <a href="#parameter-device_id"><code>device_id</code></a>, <a href="#parameter-user_email"><code>user_email</code></a>, <a href="#parameter-command_type"><code>command_type</code></a>, <a href="#parameter-status"><code>status</code></a></td>
    <td>Retrieves a paginated list of commands issued to devices under the specified account, optionally filtered by time range, device, or other parameters</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-commands"><code>commands</code></a></td>
    <td></td>
    <td>Initiate commands for up to 10 devices per account</td>
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
<tr id="parameter-command_id">
    <td><CopyableCode code="command_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for command</td>
</tr>
<tr id="parameter-filename">
    <td><CopyableCode code="filename" /></td>
    <td><code>string</code></td>
    <td>The name of the file to be downloaded, including the `.zip` extension</td>
</tr>
<tr id="parameter-command_type">
    <td><CopyableCode code="command_type" /></td>
    <td><code>string</code></td>
    <td>Optionally filter executed commands by command type</td>
</tr>
<tr id="parameter-device_id">
    <td><CopyableCode code="device_id" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for a device</td>
</tr>
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time for the query in ISO (RFC3339 - ISO 8601) format</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td>Page number for pagination</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Number of results per page</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Optionally filter executed commands by status</td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time for the query in ISO (RFC3339 - ISO 8601) format</td>
</tr>
<tr id="parameter-user_email">
    <td><CopyableCode code="user_email" /></td>
    <td><code>string</code></td>
    <td>Email tied to the device</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_downloads"
    values={[
        { label: 'get_downloads', value: 'get_downloads' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_downloads">

Downloads artifacts for an executed command. Bulk downloads are not supported

```sql
SELECT
contents
FROM cloudflare.zero_trust.commands
WHERE account_id = '{{ account_id }}' -- required
AND command_id = '{{ command_id }}' -- required
AND filename = '{{ filename }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves a paginated list of commands issued to devices under the specified account, optionally filtered by time range, device, or other parameters

```sql
SELECT
id,
device_id,
registration_id,
completed_date,
created_date,
filename,
status,
type,
user_email
FROM cloudflare.zero_trust.commands
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND from = '{{ from }}'
AND to = '{{ to }}'
AND device_id = '{{ device_id }}'
AND user_email = '{{ user_email }}'
AND command_type = '{{ command_type }}'
AND status = '{{ status }}'
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

Initiate commands for up to 10 devices per account

```sql
INSERT INTO cloudflare.zero_trust.commands (
commands,
account_id
)
SELECT 
'{{ commands }}' /* required */,
'{{ account_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: commands
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the commands resource.
    - name: commands
      description: |
        List of device-level commands to execute
      value:
        - command_args:
            interfaces:
              - "{{ interfaces }}"
            max-file-size-mb: {{ max-file-size-mb }}
            packet-size-bytes: {{ packet-size-bytes }}
            test-all-routes: {{ test-all-routes }}
            time-limit-min: {{ time-limit-min }}
          command_type: "{{ command_type }}"
          device_id: "{{ device_id }}"
          registration_id: "{{ registration_id }}"
          user_email: "{{ user_email }}"
`}</CodeBlock>

</TabItem>
</Tabs>
