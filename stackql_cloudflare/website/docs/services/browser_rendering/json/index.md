--- 
title: json
hide_title: false
hide_table_of_contents: false
keywords:
  - json
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

Creates, updates, deletes, gets or lists a <code>json</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="json" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.browser_rendering.json" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List of targets.

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
    <td>Target ID.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Target description.</td>
</tr>
<tr>
    <td><CopyableCode code="devtoolsFrontendUrl" /></td>
    <td><code>string</code></td>
    <td>DevTools frontend URL.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title of the target.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Target type (page, background_page, worker, etc.).</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>URL of the target.</td>
</tr>
<tr>
    <td><CopyableCode code="webSocketDebuggerUrl" /></td>
    <td><code>string</code></td>
    <td>WebSocket URL for debugging this target.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a></td>
    <td></td>
    <td>Returns a list of all debuggable targets including tabs, pages, service workers, and other browser contexts.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cacheTTL"><code>cacheTTL</code></a></td>
    <td>Gets json from a webpage from a provided URL or HTML. Pass `prompt` or `schema` in the body. Control page loading with `gotoOptions` and `waitFor*` options.</td>
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
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The session ID.</td>
</tr>
<tr id="parameter-cacheTTL">
    <td><CopyableCode code="cacheTTL" /></td>
    <td><code>number</code></td>
    <td>Cache TTL default is 5s. Set to 0 to disable.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Returns a list of all debuggable targets including tabs, pages, service workers, and other browser contexts.

```sql
SELECT
id,
description,
devtoolsFrontendUrl,
title,
type,
url,
webSocketDebuggerUrl
FROM cloudflare.browser_rendering.json
WHERE account_id = '{{ account_id }}' -- required
AND session_id = '{{ session_id }}' -- required
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

Gets json from a webpage from a provided URL or HTML. Pass `prompt` or `schema` in the body. Control page loading with `gotoOptions` and `waitFor*` options.

```sql
INSERT INTO cloudflare.browser_rendering.json (
actionTimeout,
addScriptTag,
addStyleTag,
allowRequestPattern,
allowResourceTypes,
authenticate,
bestAttempt,
cookies,
custom_ai,
emulateMediaType,
gotoOptions,
html,
prompt,
rejectRequestPattern,
rejectResourceTypes,
response_format,
setExtraHTTPHeaders,
setJavaScriptEnabled,
userAgent,
viewport,
waitForSelector,
waitForTimeout,
url,
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
'{{ custom_ai }}',
'{{ emulateMediaType }}',
'{{ gotoOptions }}',
'{{ html }}',
'{{ prompt }}',
'{{ rejectRequestPattern }}',
'{{ rejectResourceTypes }}',
'{{ response_format }}',
'{{ setExtraHTTPHeaders }}',
{{ setJavaScriptEnabled }},
'{{ userAgent }}',
'{{ viewport }}',
'{{ waitForSelector }}',
{{ waitForTimeout }},
'{{ url }}',
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
- name: json
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the json resource.
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
    - name: custom_ai
      description: |
        Optional list of custom AI models to use for the request. The models will be tried in the order provided, and in case a model returns an error, the next one will be used as fallback.
      value:
        - authorization: "{{ authorization }}"
          model: "{{ model }}"
    - name: emulateMediaType
      value: "{{ emulateMediaType }}"
    - name: gotoOptions
      description: |
        Check [options](https://pptr.dev/api/puppeteer.gotooptions).
      value:
        referer: "{{ referer }}"
        referrerPolicy: "{{ referrerPolicy }}"
        timeout: {{ timeout }}
        waitUntil: "{{ waitUntil }}"
      default: [object Object]
    - name: html
      value: "{{ html }}"
      description: |
        Set the content of the page, eg: \`<h1>Hello World!!</h1>\`. Either \`html\` or \`url\` must be set.
    - name: prompt
      value: "{{ prompt }}"
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
    - name: response_format
      value:
        json_schema: "{{ json_schema }}"
        type: "{{ type }}"
    - name: setExtraHTTPHeaders
      value: "{{ setExtraHTTPHeaders }}"
    - name: setJavaScriptEnabled
      value: {{ setJavaScriptEnabled }}
    - name: userAgent
      value: "{{ userAgent }}"
      default: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
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
    - name: url
      value: "{{ url }}"
      description: |
        URL to navigate to, eg. \`https://example.com\`.
    - name: cacheTTL
      value: {{ cacheTTL }}
      description: Cache TTL default is 5s. Set to 0 to disable.
      description: Cache TTL default is 5s. Set to 0 to disable.
`}</CodeBlock>

</TabItem>
</Tabs>
