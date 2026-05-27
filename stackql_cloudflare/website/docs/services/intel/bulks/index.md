--- 
title: bulks
hide_title: false
hide_table_of_contents: false
keywords:
  - bulks
  - intel
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

Creates, updates, deletes, gets or lists a <code>bulks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bulks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.intel.bulks" /></td></tr>
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

Get Multiple Domain Details response.

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
    <td><CopyableCode code="additional_information" /></td>
    <td><code>object</code></td>
    <td>Additional information related to the host name.</td>
</tr>
<tr>
    <td><CopyableCode code="application" /></td>
    <td><code>object</code></td>
    <td>Application that the hostname belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="content_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td> (example: cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="inherited_content_categories" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="inherited_from" /></td>
    <td><code>string</code></td>
    <td>Domain from which `inherited_content_categories` and `inherited_risk_types` are inherited, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="inherited_risk_types" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="popularity_rank" /></td>
    <td><code>integer</code></td>
    <td>Global Cloudflare 100k ranking for the last 30 days, if available for the hostname. The top ranked domain is 1, the lowest ranked domain is 100,000.</td>
</tr>
<tr>
    <td><CopyableCode code="risk_score" /></td>
    <td><code>number</code></td>
    <td>Hostname risk score, which is a value between 0 (lowest risk) to 1 (highest risk).</td>
</tr>
<tr>
    <td><CopyableCode code="risk_types" /></td>
    <td><code>array</code></td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-domain"><code>domain</code></a></td>
    <td>Same as summary.</td>
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
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>array</code></td>
    <td>Accepts multiple values like `?domain=cloudflare.com&domain=example.com`.</td>
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

Same as summary.

```sql
SELECT
additional_information,
application,
content_categories,
domain,
inherited_content_categories,
inherited_from,
inherited_risk_types,
popularity_rank,
risk_score,
risk_types
FROM cloudflare.intel.bulks
WHERE account_id = '{{ account_id }}' -- required
AND domain = '{{ domain }}'
;
```
</TabItem>
</Tabs>
