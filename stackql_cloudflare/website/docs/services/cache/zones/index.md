--- 
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - cache
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

Creates, updates, deletes, gets or lists a <code>zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="zones" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.cache.zones" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#purge_cache"><CopyableCode code="purge_cache" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>**Purge All Cached Content:** Removes ALL files from Cloudflare's cache. All tiers can purge everything. ``` &#123;"purge_everything": true&#125; ``` **Purge Cached Content by URL:** Granularly removes one or more files from Cloudflare's cache by specifying URLs. All tiers can purge by URL. To purge files with custom cache keys, include the headers used to compute the cache key as in the example. If you have a device type or geo in your cache key, you will need to include the CF-Device-Type or CF-IPCountry headers. If you have lang in your cache key, you will need to include the Accept-Language header. **NB:** When including the Origin header, be sure to include the **scheme** and **hostname**. The port number can be omitted if it is the default port (80 for http, 443 for https), but must be included otherwise. Single file purge example with files: ``` &#123;"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]&#125; ``` Single file purge example with url and header pairs: ``` &#123;"files": [&#123;url: "http://www.example.com/cat_picture.jpg", headers: &#123; "CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN" &#125;&#125;, &#123;url: "http://www.example.com/dog_picture.jpg", headers: &#123; "CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US" &#125;&#125;]&#125; ``` **Purge Cached Content by Tag, Host or Prefix:** Granularly removes one or more files from Cloudflare's cache either by specifying the host, the associated Cache-Tag, or a Prefix. Flex purge with tags: ``` &#123;"tags": ["a-cache-tag", "another-cache-tag"]&#125; ``` Flex purge with hosts: ``` &#123;"hosts": ["www.example.com", "images.example.com"]&#125; ``` Flex purge with prefixes: ``` &#123;"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]&#125; ``` **Availability and limits:** please refer to [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).</td>
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
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="purge_cache"
    values={[
        { label: 'purge_cache', value: 'purge_cache' }
    ]}
>
<TabItem value="purge_cache">

**Purge All Cached Content:** Removes ALL files from Cloudflare's cache. All tiers can purge everything. ``` &#123;"purge_everything": true&#125; ``` **Purge Cached Content by URL:** Granularly removes one or more files from Cloudflare's cache by specifying URLs. All tiers can purge by URL. To purge files with custom cache keys, include the headers used to compute the cache key as in the example. If you have a device type or geo in your cache key, you will need to include the CF-Device-Type or CF-IPCountry headers. If you have lang in your cache key, you will need to include the Accept-Language header. **NB:** When including the Origin header, be sure to include the **scheme** and **hostname**. The port number can be omitted if it is the default port (80 for http, 443 for https), but must be included otherwise. Single file purge example with files: ``` &#123;"files": ["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"]&#125; ``` Single file purge example with url and header pairs: ``` &#123;"files": [&#123;url: "http://www.example.com/cat_picture.jpg", headers: &#123; "CF-IPCountry": "US", "CF-Device-Type": "desktop", "Accept-Language": "zh-CN" &#125;&#125;, &#123;url: "http://www.example.com/dog_picture.jpg", headers: &#123; "CF-IPCountry": "EU", "CF-Device-Type": "mobile", "Accept-Language": "en-US" &#125;&#125;]&#125; ``` **Purge Cached Content by Tag, Host or Prefix:** Granularly removes one or more files from Cloudflare's cache either by specifying the host, the associated Cache-Tag, or a Prefix. Flex purge with tags: ``` &#123;"tags": ["a-cache-tag", "another-cache-tag"]&#125; ``` Flex purge with hosts: ``` &#123;"hosts": ["www.example.com", "images.example.com"]&#125; ``` Flex purge with prefixes: ``` &#123;"prefixes": ["www.example.com/foo", "images.example.com/bar/baz"]&#125; ``` **Availability and limits:** please refer to [purge cache availability and limits documentation page](https://developers.cloudflare.com/cache/how-to/purge-cache/#availability-and-limits).

```sql
EXEC cloudflare.cache.zones.purge_cache 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"hosts": "{{ hosts }}", 
"prefixes": "{{ prefixes }}", 
"purge_everything": {{ purge_everything }}, 
"files": "{{ files }}"
}'
;
```
</TabItem>
</Tabs>
