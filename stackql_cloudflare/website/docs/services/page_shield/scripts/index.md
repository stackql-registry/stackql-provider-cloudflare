--- 
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
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

Creates, updates, deletes, gets or lists a <code>scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scripts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.page_shield.scripts" /></td></tr>
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

Get a Page Shield script response

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
    <td><CopyableCode code="added_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-08-18T10:51:10.09615Z)</td>
</tr>
<tr>
    <td><CopyableCode code="cryptomining_score" /></td>
    <td><code>integer</code></td>
    <td>The cryptomining score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="dataflow_score" /></td>
    <td><code>integer</code></td>
    <td>The dataflow score of the JavaScript content. This field has been deprecated in favour of js_integrity_score.</td>
</tr>
<tr>
    <td><CopyableCode code="domain_reported_malicious" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="fetched_at" /></td>
    <td><code>string</code></td>
    <td>The timestamp of when the script was last fetched.</td>
</tr>
<tr>
    <td><CopyableCode code="first_page_url" /></td>
    <td><code>string</code></td>
    <td> (example: blog.cloudflare.com/page)</td>
</tr>
<tr>
    <td><CopyableCode code="first_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-08-18T10:51:08Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hash" /></td>
    <td><code>string</code></td>
    <td>The computed hash of the analyzed script.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td> (example: blog.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="js_integrity_score" /></td>
    <td><code>integer</code></td>
    <td>The integrity score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-09-02T09:57:54Z)</td>
</tr>
<tr>
    <td><CopyableCode code="magecart_score" /></td>
    <td><code>integer</code></td>
    <td>The magecart score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="malicious_domain_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="malicious_url_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="malware_score" /></td>
    <td><code>integer</code></td>
    <td>The malware score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="obfuscation_score" /></td>
    <td><code>integer</code></td>
    <td>The obfuscation score of the JavaScript content. This field has been deprecated in favour of js_integrity_score.</td>
</tr>
<tr>
    <td><CopyableCode code="page_urls" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td> (example: https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/js/bootstrap.min.js)</td>
</tr>
<tr>
    <td><CopyableCode code="url_contains_cdn_cgi_path" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="url_reported_malicious" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Page Shield scripts response

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
    <td><CopyableCode code="added_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-08-18T10:51:10.09615Z)</td>
</tr>
<tr>
    <td><CopyableCode code="cryptomining_score" /></td>
    <td><code>integer</code></td>
    <td>The cryptomining score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="dataflow_score" /></td>
    <td><code>integer</code></td>
    <td>The dataflow score of the JavaScript content. This field has been deprecated in favour of js_integrity_score.</td>
</tr>
<tr>
    <td><CopyableCode code="domain_reported_malicious" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="fetched_at" /></td>
    <td><code>string</code></td>
    <td>The timestamp of when the script was last fetched.</td>
</tr>
<tr>
    <td><CopyableCode code="first_page_url" /></td>
    <td><code>string</code></td>
    <td> (example: blog.cloudflare.com/page)</td>
</tr>
<tr>
    <td><CopyableCode code="first_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-08-18T10:51:08Z)</td>
</tr>
<tr>
    <td><CopyableCode code="hash" /></td>
    <td><code>string</code></td>
    <td>The computed hash of the analyzed script.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td> (example: blog.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="js_integrity_score" /></td>
    <td><code>integer</code></td>
    <td>The integrity score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="last_seen_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2021-09-02T09:57:54Z)</td>
</tr>
<tr>
    <td><CopyableCode code="magecart_score" /></td>
    <td><code>integer</code></td>
    <td>The magecart score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="malicious_domain_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="malicious_url_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="malware_score" /></td>
    <td><code>integer</code></td>
    <td>The malware score of the JavaScript content.</td>
</tr>
<tr>
    <td><CopyableCode code="obfuscation_score" /></td>
    <td><code>integer</code></td>
    <td>The obfuscation score of the JavaScript content. This field has been deprecated in favour of js_integrity_score.</td>
</tr>
<tr>
    <td><CopyableCode code="page_urls" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td> (example: https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/js/bootstrap.min.js)</td>
</tr>
<tr>
    <td><CopyableCode code="url_contains_cdn_cgi_path" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="url_reported_malicious" /></td>
    <td><code>boolean</code></td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-script_id"><code>script_id</code></a></td>
    <td></td>
    <td>Fetches a script detected by Page Shield by script ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-exclude_urls"><code>exclude_urls</code></a>, <a href="#parameter-urls"><code>urls</code></a>, <a href="#parameter-hosts"><code>hosts</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-prioritize_malicious"><code>prioritize_malicious</code></a>, <a href="#parameter-exclude_cdn_cgi"><code>exclude_cdn_cgi</code></a>, <a href="#parameter-exclude_duplicates"><code>exclude_duplicates</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-page_url"><code>page_url</code></a>, <a href="#parameter-export"><code>export</code></a></td>
    <td>Lists all scripts detected by Page Shield.</td>
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
<tr id="parameter-script_id">
    <td><CopyableCode code="script_id" /></td>
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
<tr id="parameter-exclude_cdn_cgi">
    <td><CopyableCode code="exclude_cdn_cgi" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-exclude_duplicates">
    <td><CopyableCode code="exclude_duplicates" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-exclude_urls">
    <td><CopyableCode code="exclude_urls" /></td>
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
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-prioritize_malicious">
    <td><CopyableCode code="prioritize_malicious" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-urls">
    <td><CopyableCode code="urls" /></td>
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

Fetches a script detected by Page Shield by script ID.

```sql
SELECT
id,
added_at,
cryptomining_score,
dataflow_score,
domain_reported_malicious,
fetched_at,
first_page_url,
first_seen_at,
hash,
host,
js_integrity_score,
last_seen_at,
magecart_score,
malicious_domain_categories,
malicious_url_categories,
malware_score,
obfuscation_score,
page_urls,
url,
url_contains_cdn_cgi_path,
url_reported_malicious,
versions
FROM cloudflare.page_shield.scripts
WHERE zone_id = '{{ zone_id }}' -- required
AND script_id = '{{ script_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all scripts detected by Page Shield.

```sql
SELECT
id,
added_at,
cryptomining_score,
dataflow_score,
domain_reported_malicious,
fetched_at,
first_page_url,
first_seen_at,
hash,
host,
js_integrity_score,
last_seen_at,
magecart_score,
malicious_domain_categories,
malicious_url_categories,
malware_score,
obfuscation_score,
page_urls,
url,
url_contains_cdn_cgi_path,
url_reported_malicious
FROM cloudflare.page_shield.scripts
WHERE zone_id = '{{ zone_id }}' -- required
AND exclude_urls = '{{ exclude_urls }}'
AND urls = '{{ urls }}'
AND hosts = '{{ hosts }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND order_by = '{{ order_by }}'
AND direction = '{{ direction }}'
AND prioritize_malicious = '{{ prioritize_malicious }}'
AND exclude_cdn_cgi = '{{ exclude_cdn_cgi }}'
AND exclude_duplicates = '{{ exclude_duplicates }}'
AND status = '{{ status }}'
AND page_url = '{{ page_url }}'
AND export = '{{ export }}'
;
```
</TabItem>
</Tabs>
