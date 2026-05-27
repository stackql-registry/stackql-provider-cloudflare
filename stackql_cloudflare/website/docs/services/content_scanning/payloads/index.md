--- 
title: payloads
hide_title: false
hide_table_of_contents: false
keywords:
  - payloads
  - content_scanning
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

Creates, updates, deletes, gets or lists a <code>payloads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="payloads" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.content_scanning.payloads" /></td></tr>
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

List existing Content Scan custom scan expressions response.

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
    <td>defines the unique ID for this custom scan expression. (example: a350a054caa840c9becd89c3b4f0195b)</td>
</tr>
<tr>
    <td><CopyableCode code="payload" /></td>
    <td><code>string</code></td>
    <td>Defines the ruleset expression to use in matching content objects. (example: lookup_json_string(http.request.body.raw, "file"))</td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Get a list of existing custom scan expressions for Content Scanning.</td>
</tr>
<tr>
    <td><a href="#waf_content_scanning_add_custom_scan_expressions"><CopyableCode code="waf_content_scanning_add_custom_scan_expressions" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Add custom scan expressions for Content Scanning.</td>
</tr>
<tr>
    <td><a href="#waf_content_scanning_delete_custom_scan_expressions"><CopyableCode code="waf_content_scanning_delete_custom_scan_expressions" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-expression_id"><code>expression_id</code></a></td>
    <td></td>
    <td>Delete a Content Scan Custom Expression.</td>
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
<tr id="parameter-expression_id">
    <td><CopyableCode code="expression_id" /></td>
    <td><code>string</code></td>
    <td></td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get a list of existing custom scan expressions for Content Scanning.

```sql
SELECT
id,
payload
FROM cloudflare.content_scanning.payloads
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="waf_content_scanning_add_custom_scan_expressions"
    values={[
        { label: 'waf_content_scanning_add_custom_scan_expressions', value: 'waf_content_scanning_add_custom_scan_expressions' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="waf_content_scanning_add_custom_scan_expressions">

Add custom scan expressions for Content Scanning.

```sql
INSERT INTO cloudflare.content_scanning.payloads (
zone_id
)
SELECT 
'{{ zone_id }}'
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
- name: payloads
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the payloads resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="waf_content_scanning_delete_custom_scan_expressions"
    values={[
        { label: 'waf_content_scanning_delete_custom_scan_expressions', value: 'waf_content_scanning_delete_custom_scan_expressions' }
    ]}
>
<TabItem value="waf_content_scanning_delete_custom_scan_expressions">

Delete a Content Scan Custom Expression.

```sql
DELETE FROM cloudflare.content_scanning.payloads
WHERE zone_id = '{{ zone_id }}' --required
AND expression_id = '{{ expression_id }}' --required
;
```
</TabItem>
</Tabs>
