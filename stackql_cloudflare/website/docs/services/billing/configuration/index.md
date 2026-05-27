--- 
title: configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration
  - billing
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

Creates, updates, deletes, gets or lists a <code>configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.billing.configuration" /></td></tr>
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
    <td><CopyableCode code="bot_overrides" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="price_usd_microcents" /></td>
    <td><code>integer</code></td>
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
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Gets the pay-per-crawl config for a zone including the bot configuration.</td>
</tr>
<tr>
    <td><a href="#pay_per_crawl_create_config"><CopyableCode code="pay_per_crawl_create_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Creates the pay-per-crawl config for a zone.</td>
</tr>
<tr>
    <td><a href="#pay_per_crawl_patch_config"><CopyableCode code="pay_per_crawl_patch_config" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Changes the pay-per-crawl config for a zone.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets the pay-per-crawl config for a zone including the bot configuration.

```sql
SELECT
bot_overrides,
enabled,
price_usd_microcents
FROM cloudflare.billing.configuration
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="pay_per_crawl_create_config"
    values={[
        { label: 'pay_per_crawl_create_config', value: 'pay_per_crawl_create_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="pay_per_crawl_create_config">

Creates the pay-per-crawl config for a zone.

```sql
INSERT INTO cloudflare.billing.configuration (
bot_overrides,
enabled,
price_usd_microcents,
zone_id
)
SELECT 
'{{ bot_overrides }}',
{{ enabled }},
{{ price_usd_microcents }},
'{{ zone_id }}'
RETURNING
errors,
messages,
result,
result_info,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: configuration
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the configuration resource.
    - name: bot_overrides
      value: "{{ bot_overrides }}"
    - name: enabled
      value: {{ enabled }}
    - name: price_usd_microcents
      value: {{ price_usd_microcents }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="pay_per_crawl_patch_config"
    values={[
        { label: 'pay_per_crawl_patch_config', value: 'pay_per_crawl_patch_config' }
    ]}
>
<TabItem value="pay_per_crawl_patch_config">

Changes the pay-per-crawl config for a zone.

```sql
UPDATE cloudflare.billing.configuration
SET 
bot_overrides = '{{ bot_overrides }}',
enabled = {{ enabled }},
price_usd_microcents = {{ price_usd_microcents }}
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
result_info,
success;
```
</TabItem>
</Tabs>
