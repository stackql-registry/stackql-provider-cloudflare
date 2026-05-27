--- 
title: crawl
hide_title: false
hide_table_of_contents: false
keywords:
  - crawl
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

Creates, updates, deletes, gets or lists a <code>crawl</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="crawl" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.browser_rendering.crawl" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the result of a crawl job.

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
    <td>Crawl job ID.</td>
</tr>
<tr>
    <td><CopyableCode code="browserSecondsUsed" /></td>
    <td><code>number</code></td>
    <td>Total seconds spent in browser so far.</td>
</tr>
<tr>
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Cursor for pagination.</td>
</tr>
<tr>
    <td><CopyableCode code="finished" /></td>
    <td><code>number</code></td>
    <td>Total number of URLs that have been crawled so far.</td>
</tr>
<tr>
    <td><CopyableCode code="records" /></td>
    <td><code>array</code></td>
    <td>List of crawl job records.</td>
</tr>
<tr>
    <td><CopyableCode code="skipped" /></td>
    <td><code>number</code></td>
    <td>Total number of URLs that were skipped due to include/exclude/subdomain filters. Skipped URLs are included in records but are not counted toward total/finished.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current crawl job status.</td>
</tr>
<tr>
    <td><CopyableCode code="total" /></td>
    <td><code>number</code></td>
    <td>Total current number of URLs in the crawl job.</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>Returns the result of a crawl job.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Starts a crawl job for the provided URL and its children. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-job_id"><code>job_id</code></a></td>
    <td></td>
    <td>Cancels an ongoing crawl job by setting its status to cancelled and stopping all queued URLs.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job ID.</td>
</tr>
<tr id="parameter-cacheTTL">
    <td><CopyableCode code="cacheTTL" /></td>
    <td><code>number</code></td>
    <td>Cache TTL default is 5s. Set to 0 to disable.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>number</code></td>
    <td>Cursor for pagination.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td>Limit for pagination.</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter by URL status.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns the result of a crawl job.

```sql
SELECT
id,
browserSecondsUsed,
cursor,
finished,
records,
skipped,
status,
total
FROM cloudflare.browser_rendering.crawl
WHERE account_id = '{{ account_id }}' -- required
AND job_id = '{{ job_id }}' -- required
AND cacheTTL = '{{ cacheTTL }}'
AND status = '{{ status }}'
AND cursor = '{{ cursor }}'
AND limit = '{{ limit }}'
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

Starts a crawl job for the provided URL and its children. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.

```sql
INSERT INTO cloudflare.browser_rendering.crawl (
actionTimeout,
addScriptTag,
addStyleTag,
allowRequestPattern,
allowResourceTypes,
authenticate,
bestAttempt,
cookies,
crawlPurposes,
depth,
emulateMediaType,
formats,
gotoOptions,
jsonOptions,
limit,
maxAge,
modifiedSince,
options,
rejectRequestPattern,
rejectResourceTypes,
render,
setExtraHTTPHeaders,
setJavaScriptEnabled,
source,
url,
viewport,
waitForSelector,
waitForTimeout,
account_id,
cacheTTL
)
SELECT 
{{ actionTimeout }},
'{{ addScriptTag }}',
'{{ addStyleTag }}',
'{{ allowRequestPattern }}',
'{{ allowResourceTypes }}',
'{{ authenticate }}',
{{ bestAttempt }},
'{{ cookies }}',
'{{ crawlPurposes }}',
{{ depth }},
'{{ emulateMediaType }}',
'{{ formats }}',
'{{ gotoOptions }}',
'{{ jsonOptions }}',
{{ limit }},
{{ maxAge }},
{{ modifiedSince }},
'{{ options }}',
'{{ rejectRequestPattern }}',
'{{ rejectResourceTypes }}',
{{ render }},
'{{ setExtraHTTPHeaders }}',
{{ setJavaScriptEnabled }},
'{{ source }}',
'{{ url }}' /* required */,
'{{ viewport }}',
'{{ waitForSelector }}',
{{ waitForTimeout }},
'{{ account_id }}',
'{{ cacheTTL }}'
RETURNING
errors,
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: crawl
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the crawl resource.
    - name: actionTimeout
      value: {{ actionTimeout }}
      description: |
        The maximum duration allowed for the browser action to complete after the page has loaded (such as taking screenshots, extracting content, or generating PDFs). If this time limit is exceeded, the action stops and returns a timeout error.
    - name: addScriptTag
      description: |
        Adds a \`<script>\` tag into the page with the desired URL or content.
      value:
        - content: "{{ content }}"
          id: "{{ id }}"
          type: "{{ type }}"
          url: "{{ url }}"
    - name: addStyleTag
      description: |
        Adds a \`<link rel="stylesheet">\` tag into the page with the desired URL or a \`<style type="text/css">\` tag with the content.
      value:
        - content: "{{ content }}"
          url: "{{ url }}"
    - name: allowRequestPattern
      value:
        - "{{ allowRequestPattern }}"
      description: |
        Only allow requests that match the provided regex patterns, eg. '/^.*\.(css)'.
    - name: allowResourceTypes
      value:
        - "{{ allowResourceTypes }}"
      description: |
        Only allow requests that match the provided resource types, eg. 'image' or 'script'.
    - name: authenticate
      description: |
        Provide credentials for HTTP authentication.
      value:
        password: "{{ password }}"
        username: "{{ username }}"
    - name: bestAttempt
      value: {{ bestAttempt }}
      description: |
        Attempt to proceed when 'awaited' events fail or timeout.
    - name: cookies
      description: |
        Check [options](https://pptr.dev/api/puppeteer.page.setcookie).
      value:
        - domain: "{{ domain }}"
          expires: {{ expires }}
          httpOnly: {{ httpOnly }}
          name: "{{ name }}"
          partitionKey: "{{ partitionKey }}"
          path: "{{ path }}"
          priority: "{{ priority }}"
          sameParty: {{ sameParty }}
          sameSite: "{{ sameSite }}"
          secure: {{ secure }}
          sourcePort: {{ sourcePort }}
          sourceScheme: "{{ sourceScheme }}"
          url: "{{ url }}"
          value: "{{ value }}"
    - name: crawlPurposes
      value:
        - "{{ crawlPurposes }}"
      description: |
        List of crawl purposes to respect Content-Signal directives in robots.txt. Allowed values: 'search', 'ai-input', 'ai-train'. Learn more: https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].
      default: search,ai-input,ai-train
    - name: depth
      value: {{ depth }}
      description: |
        Maximum number of levels deep the crawler will traverse from the starting URL.
      default: 100000
    - name: emulateMediaType
      value: "{{ emulateMediaType }}"
    - name: formats
      value:
        - "{{ formats }}"
      description: |
        Formats to return. Default is \`html\`.
      default: html
    - name: gotoOptions
      description: |
        Check [options](https://pptr.dev/api/puppeteer.gotooptions).
      value:
        referer: "{{ referer }}"
        referrerPolicy: "{{ referrerPolicy }}"
        timeout: {{ timeout }}
        waitUntil: "{{ waitUntil }}"
      default: [object Object]
    - name: jsonOptions
      description: |
        Options for JSON extraction.
      value:
        custom_ai:
          - authorization: "{{ authorization }}"
            model: "{{ model }}"
        prompt: "{{ prompt }}"
        response_format:
          json_schema: "{{ json_schema }}"
          type: "{{ type }}"
    - name: limit
      value: {{ limit }}
      description: |
        Maximum number of URLs to crawl.
      default: 10
    - name: maxAge
      value: {{ maxAge }}
      description: |
        Maximum age of a resource that can be returned from cache in seconds. Default is 1 day.
      default: 86400
    - name: modifiedSince
      value: {{ modifiedSince }}
      description: |
        Unix timestamp (seconds since epoch) indicating to only crawl pages that were modified since this time. For sitemap URLs with a lastmod field, this is compared directly. For other URLs, the crawler will use If-Modified-Since header when fetching. URLs without modification information (no lastmod in sitemap and no Last-Modified header support) will be crawled. Note: This works in conjunction with maxAge - both filters must pass for a cached resource to be used. Must be within the last year and not in the future.
    - name: options
      description: |
        Additional options for the crawler.
      value:
        excludePatterns:
          - "{{ excludePatterns }}"
        includeExternalLinks: {{ includeExternalLinks }}
        includePatterns:
          - "{{ includePatterns }}"
        includeSubdomains: {{ includeSubdomains }}
      default: [object Object]
    - name: rejectRequestPattern
      value:
        - "{{ rejectRequestPattern }}"
      description: |
        Block undesired requests that match the provided regex patterns, eg. '/^.*\.(css)'.
    - name: rejectResourceTypes
      value:
        - "{{ rejectResourceTypes }}"
      description: |
        Block undesired requests that match the provided resource types, eg. 'image' or 'script'.
    - name: render
      value: {{ render }}
      description: |
        Whether to render the page or fetch static content. True by default.
      valid_values: ['true']
      default: true
    - name: setExtraHTTPHeaders
      value: "{{ setExtraHTTPHeaders }}"
    - name: setJavaScriptEnabled
      value: {{ setJavaScriptEnabled }}
    - name: source
      value: "{{ source }}"
      description: |
        Source of links to crawl. 'sitemaps' - only crawl URLs from sitemaps, 'links' - only crawl URLs scraped from pages, 'all' - crawl both sitemap and scraped links (default).
      valid_values: ['sitemaps']
      default: all
    - name: url
      value: "{{ url }}"
      description: |
        URL to navigate to, eg. \`https://example.com\`.
    - name: viewport
      description: |
        Check [options](https://pptr.dev/api/puppeteer.page.setviewport).
      value:
        deviceScaleFactor: {{ deviceScaleFactor }}
        hasTouch: {{ hasTouch }}
        height: {{ height }}
        isLandscape: {{ isLandscape }}
        isMobile: {{ isMobile }}
        width: {{ width }}
      default: [object Object]
    - name: waitForSelector
      description: |
        Wait for the selector to appear in page. Check [options](https://pptr.dev/api/puppeteer.page.waitforselector).
      value:
        hidden: {{ hidden }}
        selector: "{{ selector }}"
        timeout: {{ timeout }}
        visible: {{ visible }}
    - name: waitForTimeout
      value: {{ waitForTimeout }}
      description: |
        Waits for a specified timeout before continuing.
    - name: cacheTTL
      value: {{ cacheTTL }}
      description: Cache TTL default is 5s. Set to 0 to disable.
      description: Cache TTL default is 5s. Set to 0 to disable.
`}</CodeBlock>

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

Cancels an ongoing crawl job by setting its status to cancelled and stopping all queued URLs.

```sql
DELETE FROM cloudflare.browser_rendering.crawl
WHERE account_id = '{{ account_id }}' --required
AND job_id = '{{ job_id }}' --required
;
```
</TabItem>
</Tabs>
