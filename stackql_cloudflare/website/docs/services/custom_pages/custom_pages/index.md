--- 
title: custom_pages
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_pages
  - custom_pages
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

Creates, updates, deletes, gets or lists a <code>custom_pages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_pages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.custom_pages.custom_pages" /></td></tr>
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

Get a custom page response

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
    <td> (example: basic_challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Basic Challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="preview_target" /></td>
    <td><code>string</code></td>
    <td> (example: block:basic-sec-captcha)</td>
</tr>
<tr>
    <td><CopyableCode code="required_tokens" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The custom page state. (default, customized) (example: default)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL associated with the custom page. (example: http://www.example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get a custom page response

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
    <td> (example: basic_challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Basic Challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="preview_target" /></td>
    <td><code>string</code></td>
    <td> (example: block:basic-sec-captcha)</td>
</tr>
<tr>
    <td><CopyableCode code="required_tokens" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The custom page state. (default, customized) (example: default)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL associated with the custom page. (example: http://www.example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List custom pages response

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
    <td> (example: basic_challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Basic Challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="preview_target" /></td>
    <td><code>string</code></td>
    <td> (example: block:basic-sec-captcha)</td>
</tr>
<tr>
    <td><CopyableCode code="required_tokens" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The custom page state. (default, customized) (example: default)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL associated with the custom page. (example: http://www.example.com)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List custom pages response

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
    <td> (example: basic_challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td> (example: Basic Challenge)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="preview_target" /></td>
    <td><code>string</code></td>
    <td> (example: block:basic-sec-captcha)</td>
</tr>
<tr>
    <td><CopyableCode code="required_tokens" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The custom page state. (default, customized) (example: default)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string (uri)</code></td>
    <td>The URL associated with the custom page. (example: http://www.example.com)</td>
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
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the details of a custom page.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the details of a custom page.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches all the custom pages.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches all the custom pages.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-state"><code>state</code></a></td>
    <td></td>
    <td>Updates the configuration of an existing custom page.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-state"><code>state</code></a></td>
    <td></td>
    <td>Updates the configuration of an existing custom page.</td>
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
<tr id="parameter-identifier">
    <td><CopyableCode code="identifier" /></td>
    <td><code>string</code></td>
    <td>Resource identifier.</td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches the details of a custom page.

```sql
SELECT
id,
created_on,
description,
modified_on,
preview_target,
required_tokens,
state,
url
FROM cloudflare.custom_pages.custom_pages
WHERE identifier = '{{ identifier }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches the details of a custom page.

```sql
SELECT
id,
created_on,
description,
modified_on,
preview_target,
required_tokens,
state,
url
FROM cloudflare.custom_pages.custom_pages
WHERE identifier = '{{ identifier }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Fetches all the custom pages.

```sql
SELECT
id,
created_on,
description,
modified_on,
preview_target,
required_tokens,
state,
url
FROM cloudflare.custom_pages.custom_pages
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Fetches all the custom pages.

```sql
SELECT
id,
created_on,
description,
modified_on,
preview_target,
required_tokens,
state,
url
FROM cloudflare.custom_pages.custom_pages
WHERE zone_id = '{{ zone_id }}' -- required
;
```
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

Updates the configuration of an existing custom page.

```sql
REPLACE cloudflare.custom_pages.custom_pages
SET 
state = '{{ state }}',
url = '{{ url }}'
WHERE 
identifier = '{{ identifier }}' --required
AND account_id = '{{ account_id }}' --required
AND url = '{{ url }}' --required
AND state = '{{ state }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates the configuration of an existing custom page.

```sql
REPLACE cloudflare.custom_pages.custom_pages
SET 
state = '{{ state }}',
url = '{{ url }}'
WHERE 
identifier = '{{ identifier }}' --required
AND zone_id = '{{ zone_id }}' --required
AND url = '{{ url }}' --required
AND state = '{{ state }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
