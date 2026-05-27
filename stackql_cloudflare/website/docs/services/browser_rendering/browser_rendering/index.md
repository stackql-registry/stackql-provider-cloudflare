--- 
title: browser_rendering
hide_title: false
hide_table_of_contents: false
keywords:
  - browser_rendering
  - browser_rendering
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

Creates, updates, deletes, gets or lists a <code>browser_rendering</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="browser_rendering" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.browser_rendering.browser_rendering" /></td></tr>
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
    <td><a href="#create_content"><CopyableCode code="create_content" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Fetches rendered HTML content from provided URL or HTML. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.</td>
</tr>
<tr>
    <td><a href="#create_links"><CopyableCode code="create_links" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Get links from a web page.</td>
</tr>
<tr>
    <td><a href="#create_markdown"><CopyableCode code="create_markdown" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Gets markdown of a webpage from provided URL or HTML. Control page loading with `gotoOptions` and `waitFor*` options.</td>
</tr>
<tr>
    <td><a href="#create_pdf"><CopyableCode code="create_pdf" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Fetches rendered PDF from provided URL or HTML. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.</td>
</tr>
<tr>
    <td><a href="#create_scrape"><CopyableCode code="create_scrape" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-elements"><code>elements</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Get meta attributes like height, width, text and others of selected elements.</td>
</tr>
<tr>
    <td><a href="#create_screenshot"><CopyableCode code="create_screenshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Takes a screenshot of a webpage from provided URL or HTML. Control page loading with `gotoOptions` and `waitFor*` options. Customize screenshots with `viewport`, `fullPage`, `clip` and others.</td>
</tr>
<tr>
    <td><a href="#snapshot"><CopyableCode code="snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Returns the page's HTML content and screenshot. Control page loading with `gotoOptions` and `waitFor*` options. Customize screenshots with `viewport`, `fullPage`, `clip` and others.</td>
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
<tr id="parameter-cacheTTL">
    <td><CopyableCode code="cacheTTL" /></td>
    <td><code>number</code></td>
    <td>Cache TTL default is 5s. Set to 0 to disable.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="create_content"
    values={[
        { label: 'create_content', value: 'create_content' },
        { label: 'create_links', value: 'create_links' },
        { label: 'create_markdown', value: 'create_markdown' },
        { label: 'create_pdf', value: 'create_pdf' },
        { label: 'create_scrape', value: 'create_scrape' },
        { label: 'create_screenshot', value: 'create_screenshot' },
        { label: 'snapshot', value: 'snapshot' }
    ]}
>
<TabItem value="create_content">

Fetches rendered HTML content from provided URL or HTML. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.create_content 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"gotoOptions": "{{ gotoOptions }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"url": "{{ url }}", 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"html": "{{ html }}"
}'
;
```
</TabItem>
<TabItem value="create_links">

Get links from a web page.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.create_links 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"excludeExternalLinks": {{ excludeExternalLinks }}, 
"gotoOptions": "{{ gotoOptions }}", 
"html": "{{ html }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"visibleLinksOnly": {{ visibleLinksOnly }}, 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"url": "{{ url }}"
}'
;
```
</TabItem>
<TabItem value="create_markdown">

Gets markdown of a webpage from provided URL or HTML. Control page loading with `gotoOptions` and `waitFor*` options.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.create_markdown 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"gotoOptions": "{{ gotoOptions }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"url": "{{ url }}", 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"html": "{{ html }}"
}'
;
```
</TabItem>
<TabItem value="create_pdf">

Fetches rendered PDF from provided URL or HTML. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.create_pdf 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"gotoOptions": "{{ gotoOptions }}", 
"html": "{{ html }}", 
"pdfOptions": "{{ pdfOptions }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"url": "{{ url }}"
}'
;
```
</TabItem>
<TabItem value="create_scrape">

Get meta attributes like height, width, text and others of selected elements.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.create_scrape 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"elements": "{{ elements }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"gotoOptions": "{{ gotoOptions }}", 
"html": "{{ html }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"url": "{{ url }}"
}'
;
```
</TabItem>
<TabItem value="create_screenshot">

Takes a screenshot of a webpage from provided URL or HTML. Control page loading with `gotoOptions` and `waitFor*` options. Customize screenshots with `viewport`, `fullPage`, `clip` and others.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.create_screenshot 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"gotoOptions": "{{ gotoOptions }}", 
"html": "{{ html }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"screenshotOptions": "{{ screenshotOptions }}", 
"scrollPage": {{ scrollPage }}, 
"selector": "{{ selector }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"url": "{{ url }}"
}'
;
```
</TabItem>
<TabItem value="snapshot">

Returns the page's HTML content and screenshot. Control page loading with `gotoOptions` and `waitFor*` options. Customize screenshots with `viewport`, `fullPage`, `clip` and others.

```sql
EXEC cloudflare.browser_rendering.browser_rendering.snapshot 
@account_id='{{ account_id }}' --required, 
@cacheTTL='{{ cacheTTL }}' 
@@json=
'{
"actionTimeout": {{ actionTimeout }}, 
"addScriptTag": "{{ addScriptTag }}", 
"addStyleTag": "{{ addStyleTag }}", 
"allowRequestPattern": "{{ allowRequestPattern }}", 
"allowResourceTypes": "{{ allowResourceTypes }}", 
"authenticate": "{{ authenticate }}", 
"bestAttempt": {{ bestAttempt }}, 
"cookies": "{{ cookies }}", 
"emulateMediaType": "{{ emulateMediaType }}", 
"gotoOptions": "{{ gotoOptions }}", 
"html": "{{ html }}", 
"rejectRequestPattern": "{{ rejectRequestPattern }}", 
"rejectResourceTypes": "{{ rejectResourceTypes }}", 
"screenshotOptions": "{{ screenshotOptions }}", 
"setExtraHTTPHeaders": "{{ setExtraHTTPHeaders }}", 
"setJavaScriptEnabled": {{ setJavaScriptEnabled }}, 
"userAgent": "{{ userAgent }}", 
"viewport": "{{ viewport }}", 
"waitForSelector": "{{ waitForSelector }}", 
"waitForTimeout": {{ waitForTimeout }}, 
"url": "{{ url }}"
}'
;
```
</TabItem>
</Tabs>
