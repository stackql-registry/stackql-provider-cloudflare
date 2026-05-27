--- 
title: cookies
hide_title: false
hide_table_of_contents: false
keywords:
  - cookies
  - page_shield
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

Creates, updates, deletes, gets or lists a <code>cookies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cookies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.page_shield.cookies" /></td></tr>
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

Get a Page Shield cookie response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: session_id)</td>
</tr>
<tr>
    <td><CopyableCode code="domain_attribute" /></td>
    <td><code>string</code></td>
    <td> (example: cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_attribute" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-10-02T09:57:54Z)</td>
</tr>
<tr>
    <td><CopyableCode code="first_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-08-18T10:51:08Z)</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td> (example: blog.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="http_only_attribute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-09-02T09:57:54Z)</td>
</tr>
<tr>
    <td><CopyableCode code="max_age_attribute" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="page_urls" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path_attribute" /></td>
    <td><code>string</code></td>
    <td> (example: /)</td>
</tr>
<tr>
    <td><CopyableCode code="same_site_attribute" /></td>
    <td><code>string</code></td>
    <td> (lax, strict, none) (example: strict)</td>
</tr>
<tr>
    <td><CopyableCode code="secure_attribute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (first_party, unknown) (example: first_party)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Page Shield cookies response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td> (example: session_id)</td>
</tr>
<tr>
    <td><CopyableCode code="domain_attribute" /></td>
    <td><code>string</code></td>
    <td> (example: cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_attribute" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-10-02T09:57:54Z)</td>
</tr>
<tr>
    <td><CopyableCode code="first_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-08-18T10:51:08Z)</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td> (example: blog.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="http_only_attribute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-09-02T09:57:54Z)</td>
</tr>
<tr>
    <td><CopyableCode code="max_age_attribute" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="page_urls" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="path_attribute" /></td>
    <td><code>string</code></td>
    <td> (example: /)</td>
</tr>
<tr>
    <td><CopyableCode code="same_site_attribute" /></td>
    <td><code>string</code></td>
    <td> (lax, strict, none) (example: strict)</td>
</tr>
<tr>
    <td><CopyableCode code="secure_attribute" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td> (first_party, unknown) (example: first_party)</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-cookie_id"><code>cookie_id</code></a></td>
    <td></td>
    <td>Fetches a cookie collected by Page Shield by cookie ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-hosts"><code>hosts</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-page_url"><code>page_url</code></a>, <a href="#parameter-export"><code>export</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-secure"><code>secure</code></a>, <a href="#parameter-http_only"><code>http_only</code></a>, <a href="#parameter-same_site"><code>same_site</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-domain"><code>domain</code></a></td>
    <td>Lists all cookies collected by Page Shield.</td>
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
<tr id="parameter-cookie_id">
    <td><CopyableCode code="cookie_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-export">
    <td><CopyableCode code="export" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-hosts">
    <td><CopyableCode code="hosts" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-http_only">
    <td><CopyableCode code="http_only" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page_url">
    <td><CopyableCode code="page_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-same_site">
    <td><CopyableCode code="same_site" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-secure">
    <td><CopyableCode code="secure" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
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

Fetches a cookie collected by Page Shield by cookie ID.

```sql
SELECT
id,
name,
domain_attribute,
expires_attribute,
first_seen_at,
host,
http_only_attribute,
last_seen_at,
max_age_attribute,
page_urls,
path_attribute,
same_site_attribute,
secure_attribute,
type
FROM cloudflare.page_shield.cookies
WHERE zone_id = '{{ zone_id }}' -- required
AND cookie_id = '{{ cookie_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all cookies collected by Page Shield.

```sql
SELECT
id,
name,
domain_attribute,
expires_attribute,
first_seen_at,
host,
http_only_attribute,
last_seen_at,
max_age_attribute,
page_urls,
path_attribute,
same_site_attribute,
secure_attribute,
type
FROM cloudflare.page_shield.cookies
WHERE zone_id = '{{ zone_id }}' -- required
AND hosts = '{{ hosts }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order_by = '{{ order_by }}'
AND direction = '{{ direction }}'
AND page_url = '{{ page_url }}'
AND export = '{{ export }}'
AND name = '{{ name }}'
AND secure = '{{ secure }}'
AND http_only = '{{ http_only }}'
AND same_site = '{{ same_site }}'
AND type = '{{ type }}'
AND path = '{{ path }}'
AND domain = '{{ domain }}'
;
```
</TabItem>
</Tabs>
