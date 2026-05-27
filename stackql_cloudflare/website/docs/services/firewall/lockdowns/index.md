--- 
title: lockdowns
hide_title: false
hide_table_of_contents: false
keywords:
  - lockdowns
  - firewall
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

Creates, updates, deletes, gets or lists a <code>lockdowns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lockdowns" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.firewall.lockdowns" /></td></tr>
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

Get a Zone Lockdown rule response

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
    <td>The unique identifier of the Zone Lockdown rule. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="configurations" /></td>
    <td><code>array</code></td>
    <td>A list of IP addresses or CIDR ranges that will be allowed to access the URLs specified in the Zone Lockdown rule. You can include any number of `ip` or `ip_range` configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule. (example: Restrict access to these endpoints to requests from a known IP address)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the rule is currently paused.</td>
</tr>
<tr>
    <td><CopyableCode code="urls" /></td>
    <td><code>array</code></td>
    <td>The URLs to include in the rule definition. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Zone Lockdown rules response

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
    <td>The unique identifier of the Zone Lockdown rule. (example: 372e67954025e0ba6aaa6d586b9e0b59)</td>
</tr>
<tr>
    <td><CopyableCode code="configurations" /></td>
    <td><code>array</code></td>
    <td>A list of IP addresses or CIDR ranges that will be allowed to access the URLs specified in the Zone Lockdown rule. You can include any number of `ip` or `ip_range` configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was created. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative summary of the rule. (example: Restrict access to these endpoints to requests from a known IP address)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the rule was last modified. (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="paused" /></td>
    <td><code>boolean</code></td>
    <td>When true, indicates that the rule is currently paused.</td>
</tr>
<tr>
    <td><CopyableCode code="urls" /></td>
    <td><code>array</code></td>
    <td>The URLs to include in the rule definition. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.</td>
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
    <td><a href="#parameter-lock_downs_id"><code>lock_downs_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a Zone Lockdown rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-description"><code>description</code></a>, <a href="#parameter-modified_on"><code>modified_on</code></a>, <a href="#parameter-ip"><code>ip</code></a>, <a href="#parameter-priority"><code>priority</code></a>, <a href="#parameter-uri_search"><code>uri_search</code></a>, <a href="#parameter-ip_range_search"><code>ip_range_search</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-created_on"><code>created_on</code></a>, <a href="#parameter-description_search"><code>description_search</code></a>, <a href="#parameter-ip_search"><code>ip_search</code></a></td>
    <td>Fetches Zone Lockdown rules. You can filter the results using several optional parameters.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-urls"><code>urls</code></a>, <a href="#parameter-configurations"><code>configurations</code></a></td>
    <td></td>
    <td>Creates a new Zone Lockdown rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-lock_downs_id"><code>lock_downs_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-urls"><code>urls</code></a>, <a href="#parameter-configurations"><code>configurations</code></a></td>
    <td></td>
    <td>Updates an existing Zone Lockdown rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-lock_downs_id"><code>lock_downs_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an existing Zone Lockdown rule.</td>
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
<tr id="parameter-lock_downs_id">
    <td><CopyableCode code="lock_downs_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-created_on">
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-description">
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-description_search">
    <td><CopyableCode code="description_search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-ip">
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-ip_range_search">
    <td><CopyableCode code="ip_range_search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-ip_search">
    <td><CopyableCode code="ip_search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-modified_on">
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-priority">
    <td><CopyableCode code="priority" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-uri_search">
    <td><CopyableCode code="uri_search" /></td>
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

Fetches the details of a Zone Lockdown rule.

```sql
SELECT
id,
configurations,
created_on,
description,
modified_on,
paused,
urls
FROM cloudflare.firewall.lockdowns
WHERE lock_downs_id = '{{ lock_downs_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches Zone Lockdown rules. You can filter the results using several optional parameters.

```sql
SELECT
id,
configurations,
created_on,
description,
modified_on,
paused,
urls
FROM cloudflare.firewall.lockdowns
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND description = '{{ description }}'
AND modified_on = '{{ modified_on }}'
AND ip = '{{ ip }}'
AND priority = '{{ priority }}'
AND uri_search = '{{ uri_search }}'
AND ip_range_search = '{{ ip_range_search }}'
AND per_page = '{{ per_page }}'
AND created_on = '{{ created_on }}'
AND description_search = '{{ description_search }}'
AND ip_search = '{{ ip_search }}'
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

Creates a new Zone Lockdown rule.

```sql
INSERT INTO cloudflare.firewall.lockdowns (
configurations,
description,
paused,
priority,
urls,
zone_id
)
SELECT 
'{{ configurations }}' /* required */,
'{{ description }}',
{{ paused }},
{{ priority }},
'{{ urls }}' /* required */,
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
- name: lockdowns
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the lockdowns resource.
    - name: configurations
      description: |
        A list of IP addresses or CIDR ranges that will be allowed to access the URLs specified in the Zone Lockdown rule. You can include any number of \`ip\` or \`ip_range\` configurations.
      value:
        - target: "{{ target }}"
          value: "{{ value }}"
    - name: description
      value: "{{ description }}"
      description: |
        An informative summary of the rule. This value is sanitized and any tags will be removed.
    - name: paused
      value: {{ paused }}
      description: |
        When true, indicates that the rule is currently paused.
      default: false
    - name: priority
      value: {{ priority }}
      description: |
        The priority of the rule to control the processing order. A lower number indicates higher priority. If not provided, any rules with a configured priority will be processed before rules without a priority.
    - name: urls
      value:
        - "{{ urls }}"
      description: |
        The URLs to include in the current WAF override. You can use wildcards. Each entered URL will be escaped before use, which means you can only use simple wildcard patterns.
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

Updates an existing Zone Lockdown rule.

```sql
REPLACE cloudflare.firewall.lockdowns
SET 
configurations = '{{ configurations }}',
urls = '{{ urls }}'
WHERE 
lock_downs_id = '{{ lock_downs_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND urls = '{{ urls }}' --required
AND configurations = '{{ configurations }}' --required
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

Deletes an existing Zone Lockdown rule.

```sql
DELETE FROM cloudflare.firewall.lockdowns
WHERE lock_downs_id = '{{ lock_downs_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
