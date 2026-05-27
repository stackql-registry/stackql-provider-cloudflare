--- 
title: site_info
hide_title: false
hide_table_of_contents: false
keywords:
  - site_info
  - rum
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

Creates, updates, deletes, gets or lists a <code>site_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="site_info" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rum.site_info" /></td></tr>
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

Web Analytics site.

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
    <td><CopyableCode code="auto_install" /></td>
    <td><code>boolean</code></td>
    <td>If enabled, the JavaScript snippet is automatically injected for orange-clouded sites.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>A list of rules.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleset" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="site_tag" /></td>
    <td><code>string</code></td>
    <td>The Web Analytics site identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="site_token" /></td>
    <td><code>string</code></td>
    <td>The Web Analytics site token. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="snippet" /></td>
    <td><code>string</code></td>
    <td>Encoded JavaScript snippet. (example: &lt;!-- Cloudflare Web Analytics --&gt;&lt;script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='&#123;"token": "bc40a2d1b5834453aba85c1b9a3054da"&#125;'&gt;&lt;/script&gt;&lt;!-- End Cloudflare Web Analytics --&gt;)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of Web Analytics sites.

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
    <td><CopyableCode code="auto_install" /></td>
    <td><code>boolean</code></td>
    <td>If enabled, the JavaScript snippet is automatically injected for orange-clouded sites.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>A list of rules.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleset" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="site_tag" /></td>
    <td><code>string</code></td>
    <td>The Web Analytics site identifier. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="site_token" /></td>
    <td><code>string</code></td>
    <td>The Web Analytics site token. (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="snippet" /></td>
    <td><code>string</code></td>
    <td>Encoded JavaScript snippet. (example: &lt;!-- Cloudflare Web Analytics --&gt;&lt;script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='&#123;"token": "bc40a2d1b5834453aba85c1b9a3054da"&#125;'&gt;&lt;/script&gt;&lt;!-- End Cloudflare Web Analytics --&gt;)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Retrieves a Web Analytics site.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-order_by"><code>order_by</code></a></td>
    <td>Lists all Web Analytics sites of an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new Web Analytics site.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Updates an existing Web Analytics site.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-site_id"><code>site_id</code></a></td>
    <td></td>
    <td>Deletes an existing Web Analytics site.</td>
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
<tr id="parameter-site_id">
    <td><CopyableCode code="site_id" /></td>
    <td><code>string</code></td>
    <td>The site ID.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
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

Retrieves a Web Analytics site.

```sql
SELECT
auto_install,
created,
rules,
ruleset,
site_tag,
site_token,
snippet
FROM cloudflare.rum.site_info
WHERE account_id = '{{ account_id }}' -- required
AND site_id = '{{ site_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Web Analytics sites of an account.

```sql
SELECT
auto_install,
created,
rules,
ruleset,
site_tag,
site_token,
snippet
FROM cloudflare.rum.site_info
WHERE account_id = '{{ account_id }}' -- required
AND per_page = '{{ per_page }}'
AND page = '{{ page }}'
AND order_by = '{{ order_by }}'
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

Creates a new Web Analytics site.

```sql
INSERT INTO cloudflare.rum.site_info (
auto_install,
host,
zone_tag,
account_id
)
SELECT 
{{ auto_install }},
'{{ host }}',
'{{ zone_tag }}',
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
- name: site_info
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the site_info resource.
    - name: auto_install
      value: {{ auto_install }}
      description: |
        If enabled, the JavaScript snippet is automatically injected for orange-clouded sites.
    - name: host
      value: "{{ host }}"
      description: |
        The hostname to use for gray-clouded sites.
    - name: zone_tag
      value: "{{ zone_tag }}"
      description: |
        The zone identifier.
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

Updates an existing Web Analytics site.

```sql
REPLACE cloudflare.rum.site_info
SET 
auto_install = {{ auto_install }},
enabled = {{ enabled }},
host = '{{ host }}',
lite = {{ lite }},
zone_tag = '{{ zone_tag }}'
WHERE 
account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
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

Deletes an existing Web Analytics site.

```sql
DELETE FROM cloudflare.rum.site_info
WHERE account_id = '{{ account_id }}' --required
AND site_id = '{{ site_id }}' --required
;
```
</TabItem>
</Tabs>
