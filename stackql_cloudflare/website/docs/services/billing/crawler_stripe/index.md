--- 
title: crawler_stripe
hide_title: false
hide_table_of_contents: false
keywords:
  - crawler_stripe
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

Creates, updates, deletes, gets or lists a <code>crawler_stripe</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="crawler_stripe" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.billing.crawler_stripe" /></td></tr>
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
    <td><CopyableCode code="stripe_account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="connect_status" /></td>
    <td><code>string</code></td>
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
    <td></td>
    <td>Gets the stripe config for a crawler.</td>
</tr>
<tr>
    <td><a href="#pay_per_crawl_crawler_create_stripe_config"><CopyableCode code="pay_per_crawl_crawler_create_stripe_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates the stripe config for a crawler.</td>
</tr>
<tr>
    <td><a href="#pay_per_crawl_crawler_delete_stripe_config"><CopyableCode code="pay_per_crawl_crawler_delete_stripe_config" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes the stripe config for a crawler.</td>
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

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets the stripe config for a crawler.

```sql
SELECT
stripe_account_id,
connect_status
FROM cloudflare.billing.crawler_stripe
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="pay_per_crawl_crawler_create_stripe_config"
    values={[
        { label: 'pay_per_crawl_crawler_create_stripe_config', value: 'pay_per_crawl_crawler_create_stripe_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="pay_per_crawl_crawler_create_stripe_config">

Creates the stripe config for a crawler.

```sql
INSERT INTO cloudflare.billing.crawler_stripe (
account_id
)
SELECT 
'{{ account_id }}'
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
- name: crawler_stripe
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the crawler_stripe resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="pay_per_crawl_crawler_delete_stripe_config"
    values={[
        { label: 'pay_per_crawl_crawler_delete_stripe_config', value: 'pay_per_crawl_crawler_delete_stripe_config' }
    ]}
>
<TabItem value="pay_per_crawl_crawler_delete_stripe_config">

Deletes the stripe config for a crawler.

```sql
DELETE FROM cloudflare.billing.crawler_stripe
WHERE account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
