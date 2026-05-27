--- 
title: urlscanner
hide_title: false
hide_table_of_contents: false
keywords:
  - urlscanner
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

Creates, updates, deletes, gets or lists a <code>urlscanner</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="urlscanner" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.url_scanner.urlscanner" /></td></tr>
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
    <td><a href="#bulk_v2"><CopyableCode code="bulk_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Submit URLs to scan. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/ and take into account scans submitted in bulk have lower priority and may take longer to finish.</td>
</tr>
<tr>
    <td><a href="#scan_v2"><CopyableCode code="scan_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-url"><code>url</code></a></td>
    <td></td>
    <td>Submit a URL to scan. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/.</td>
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
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="bulk_v2"
    values={[
        { label: 'bulk_v2', value: 'bulk_v2' },
        { label: 'scan_v2', value: 'scan_v2' }
    ]}
>
<TabItem value="bulk_v2">

Submit URLs to scan. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/ and take into account scans submitted in bulk have lower priority and may take longer to finish.

```sql
EXEC cloudflare.url_scanner.urlscanner.bulk_v2 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="scan_v2">

Submit a URL to scan. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/.

```sql
EXEC cloudflare.url_scanner.urlscanner.scan_v2 
@account_id='{{ account_id }}' --required 
@@json=
'{
"agentReadiness": {{ agentReadiness }}, 
"country": "{{ country }}", 
"customHeaders": "{{ customHeaders }}", 
"customagent": "{{ customagent }}", 
"referer": "{{ referer }}", 
"screenshotsResolutions": "{{ screenshotsResolutions }}", 
"url": "{{ url }}", 
"visibility": "{{ visibility }}"
}'
;
```
</TabItem>
</Tabs>
