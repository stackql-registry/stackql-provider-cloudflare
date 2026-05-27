--- 
title: scan
hide_title: false
hide_table_of_contents: false
keywords:
  - scan
  - url_scanner
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

Creates, updates, deletes, gets or lists a <code>scan</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scan" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.url_scanner.scan" /></td></tr>
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

Scan has finished. It may or may not have been successful.

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
    <td><CopyableCode code="scan" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Search results

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
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Alpha-2 country code</td>
</tr>
<tr>
    <td><CopyableCode code="success" /></td>
    <td><code>boolean</code></td>
    <td>Whether scan was successful or not</td>
</tr>
<tr>
    <td><CopyableCode code="time" /></td>
    <td><code>string (date-time)</code></td>
    <td>When scan was submitted (UTC)</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Scan url (after redirects)</td>
</tr>
<tr>
    <td><CopyableCode code="uuid" /></td>
    <td><code>string (uuid)</code></td>
    <td>Scan id</td>
</tr>
<tr>
    <td><CopyableCode code="visibility" /></td>
    <td><code>string</code></td>
    <td>Submitted visibility status. (public, unlisted)</td>
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
    <td><a href="#parameter-scan_id"><code>scan_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-full"><code>full</code></a></td>
    <td>Get URL scan by uuid</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-scan_id"><code>scan_id</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-next_cursor"><code>next_cursor</code></a>, <a href="#parameter-date_start"><code>date_start</code></a>, <a href="#parameter-date_end"><code>date_end</code></a>, <a href="#parameter-url"><code>url</code></a>, <a href="#parameter-hostname"><code>hostname</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-ip"><code>ip</code></a>, <a href="#parameter-hash"><code>hash</code></a>, <a href="#parameter-page_url"><code>page_url</code></a>, <a href="#parameter-page_hostname"><code>page_hostname</code></a>, <a href="#parameter-page_path"><code>page_path</code></a>, <a href="#parameter-page_asn"><code>page_asn</code></a>, <a href="#parameter-page_ip"><code>page_ip</code></a>, <a href="#parameter-account_scans"><code>account_scans</code></a>, <a href="#parameter-is_malicious"><code>is_malicious</code></a></td>
    <td>Search scans by date and webpages' requests, including full URL (after redirects), hostname, and path. <br /> A successful scan will appear in search results a few minutes after finishing but may take much longer if the system in under load. By default, only successfully completed scans will appear in search results, unless searching by `scanId`. Please take into account that older scans may be removed from the search index at an unspecified time.</td>
</tr>
<tr>
    <td><a href="#urlscanner_create_scan"><CopyableCode code="urlscanner_create_scan" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Submit a URL to scan. You can also set some options, like the visibility level and custom headers. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/.</td>
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
<tr id="parameter-scan_id">
    <td><CopyableCode code="scan_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Scan UUID.</td>
</tr>
<tr id="parameter-account_scans">
    <td><CopyableCode code="account_scans" /></td>
    <td><code>boolean</code></td>
    <td>Return only scans created by account.</td>
</tr>
<tr id="parameter-date_end">
    <td><CopyableCode code="date_end" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filter scans requested before date (inclusive).</td>
</tr>
<tr id="parameter-date_start">
    <td><CopyableCode code="date_start" /></td>
    <td><code>string (date-time)</code></td>
    <td>Filter scans requested after date (inclusive).</td>
</tr>
<tr id="parameter-full">
    <td><CopyableCode code="full" /></td>
    <td><code>boolean</code></td>
    <td>Whether to return full report (scan summary and network log).</td>
</tr>
<tr id="parameter-hash">
    <td><CopyableCode code="hash" /></td>
    <td><code>string</code></td>
    <td>Filter scans by hash of any html/js/css request made by the webpage.</td>
</tr>
<tr id="parameter-hostname">
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>Filter scans by hostname of _any_ request made by the webpage.</td>
</tr>
<tr id="parameter-ip">
    <td><CopyableCode code="ip" /></td>
    <td><code>string</code></td>
    <td>Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage.</td>
</tr>
<tr id="parameter-is_malicious">
    <td><CopyableCode code="is_malicious" /></td>
    <td><code>boolean</code></td>
    <td>Filter scans by malicious verdict.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Limit the number of objects in the response.</td>
</tr>
<tr id="parameter-next_cursor">
    <td><CopyableCode code="next_cursor" /></td>
    <td><code>string</code></td>
    <td>Pagination cursor to get the next set of results.</td>
</tr>
<tr id="parameter-page_asn">
    <td><CopyableCode code="page_asn" /></td>
    <td><code>string</code></td>
    <td>Filter scans by main page Autonomous System Number (ASN).</td>
</tr>
<tr id="parameter-page_hostname">
    <td><CopyableCode code="page_hostname" /></td>
    <td><code>string</code></td>
    <td>Filter scans by main page hostname (domain of effective URL).</td>
</tr>
<tr id="parameter-page_ip">
    <td><CopyableCode code="page_ip" /></td>
    <td><code>string</code></td>
    <td>Filter scans by main page IP address (IPv4 or IPv6).</td>
</tr>
<tr id="parameter-page_path">
    <td><CopyableCode code="page_path" /></td>
    <td><code>string</code></td>
    <td>Filter scans by exact match of effective URL path (also supports suffix search).</td>
</tr>
<tr id="parameter-page_url">
    <td><CopyableCode code="page_url" /></td>
    <td><code>string</code></td>
    <td>Filter scans by submitted or scanned URL</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Filter scans by url path of _any_ request made by the webpage.</td>
</tr>
<tr id="parameter-scan_id">
    <td><CopyableCode code="scan_id" /></td>
    <td><code>string (uuid)</code></td>
    <td>Scan UUID.</td>
</tr>
<tr id="parameter-url">
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Filter scans by URL of _any_ request made by the webpage</td>
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

Get URL scan by uuid

```sql
SELECT
scan
FROM cloudflare.url_scanner.scan
WHERE scan_id = '{{ scan_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND full = '{{ full }}'
;
```
</TabItem>
<TabItem value="list">

Search scans by date and webpages' requests, including full URL (after redirects), hostname, and path. <br /> A successful scan will appear in search results a few minutes after finishing but may take much longer if the system in under load. By default, only successfully completed scans will appear in search results, unless searching by `scanId`. Please take into account that older scans may be removed from the search index at an unspecified time.

```sql
SELECT
country,
success,
time,
url,
uuid,
visibility
FROM cloudflare.url_scanner.scan
WHERE account_id = '{{ account_id }}' -- required
AND scan_id = '{{ scan_id }}'
AND limit = '{{ limit }}'
AND next_cursor = '{{ next_cursor }}'
AND date_start = '{{ date_start }}'
AND date_end = '{{ date_end }}'
AND url = '{{ url }}'
AND hostname = '{{ hostname }}'
AND path = '{{ path }}'
AND ip = '{{ ip }}'
AND hash = '{{ hash }}'
AND page_url = '{{ page_url }}'
AND page_hostname = '{{ page_hostname }}'
AND page_path = '{{ page_path }}'
AND page_asn = '{{ page_asn }}'
AND page_ip = '{{ page_ip }}'
AND account_scans = '{{ account_scans }}'
AND is_malicious = '{{ is_malicious }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="urlscanner_create_scan"
    values={[
        { label: 'urlscanner_create_scan', value: 'urlscanner_create_scan' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="urlscanner_create_scan">

Submit a URL to scan. You can also set some options, like the visibility level and custom headers. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/.

```sql
INSERT INTO cloudflare.url_scanner.scan (
country,
customHeaders,
screenshotsResolutions,
url,
visibility,
account_id
)
SELECT 
'{{ country }}',
'{{ customHeaders }}',
'{{ screenshotsResolutions }}',
'{{ url }}' /* required */,
'{{ visibility }}',
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
- name: scan
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the scan resource.
    - name: country
      value: "{{ country }}"
      description: |
        Country to geo egress from
      valid_values: ['AF', 'AL', 'DZ', 'AD', 'AO', 'AG', 'AR', 'AM', 'AU', 'AT', 'AZ', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CO', 'KM', 'CG', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'CD', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'SZ', 'ET', 'FJ', 'FI', 'FR', 'GA', 'GE', 'DE', 'GH', 'GR', 'GL', 'GD', 'GT', 'GN', 'GW', 'GY', 'HT', 'HN', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IL', 'IT', 'JM', 'JP', 'JO', 'KZ', 'KE', 'KI', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MR', 'MU', 'MX', 'FM', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NZ', 'NI', 'NE', 'NG', 'KP', 'MK', 'NO', 'OM', 'PK', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PL', 'PT', 'QA', 'RO', 'RU', 'RW', 'SH', 'KN', 'LC', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SK', 'SI', 'SB', 'SO', 'ZA', 'KR', 'SS', 'ES', 'LK', 'SD', 'SR', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'BS', 'GM', 'TL', 'TG', 'TO', 'TT', 'TN', 'TR', 'TM', 'UG', 'UA', 'AE', 'GB', 'US', 'UY', 'UZ', 'VU', 'VE', 'VN', 'YE', 'ZM', 'ZW']
    - name: customHeaders
      value: "{{ customHeaders }}"
      description: |
        Set custom headers.
    - name: screenshotsResolutions
      value:
        - "{{ screenshotsResolutions }}"
      description: |
        Take multiple screenshots targeting different device types.
      default: desktop
    - name: url
      value: "{{ url }}"
    - name: visibility
      value: "{{ visibility }}"
      description: |
        The option \`Public\` means it will be included in listings like recent scans and search results. \`Unlisted\` means it will not be included in the aforementioned listings, users will need to have the scan's ID to access it. A a scan will be automatically marked as unlisted if it fails, if it contains potential PII or other sensitive material.
      valid_values: ['Public', 'Unlisted']
      default: Public
`}</CodeBlock>

</TabItem>
</Tabs>
