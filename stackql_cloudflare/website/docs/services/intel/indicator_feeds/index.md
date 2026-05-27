--- 
title: indicator_feeds
hide_title: false
hide_table_of_contents: false
keywords:
  - indicator_feeds
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

Creates, updates, deletes, gets or lists an <code>indicator_feeds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="indicator_feeds" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.intel.indicator_feeds" /></td></tr>
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

Get indicator feed metadata

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
    <td><code>integer</code></td>
    <td>The unique identifier for the indicator feed</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the indicator feed</td>
</tr>
<tr>
    <td><CopyableCode code="provider_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the provider</td>
</tr>
<tr>
    <td><CopyableCode code="provider_name" /></td>
    <td><code>string</code></td>
    <td>The provider of the indicator feed</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the data entry was created</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the example test</td>
</tr>
<tr>
    <td><CopyableCode code="is_attributable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the indicator feed can be attributed to a provider</td>
</tr>
<tr>
    <td><CopyableCode code="is_downloadable" /></td>
    <td><code>boolean</code></td>
    <td>Whether the indicator feed can be downloaded</td>
</tr>
<tr>
    <td><CopyableCode code="is_public" /></td>
    <td><code>boolean</code></td>
    <td>Whether the indicator feed is exposed to customers</td>
</tr>
<tr>
    <td><CopyableCode code="latest_upload_status" /></td>
    <td><code>string</code></td>
    <td>Status of the latest snapshot uploaded (Mirroring, Unifying, Loading, Provisioning, Complete, Error)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the data entry was last modified</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-feed_id"><code>feed_id</code></a></td>
    <td></td>
    <td>Retrieves details for a specific custom threat indicator feed.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a new custom threat indicator feed for sharing threat intelligence data.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-feed_id"><code>feed_id</code></a></td>
    <td></td>
    <td>Revises details for a specific custom threat indicator feed.</td>
</tr>
<tr>
    <td><a href="#snapshot"><CopyableCode code="snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-feed_id"><code>feed_id</code></a></td>
    <td></td>
    <td>Revises the raw data entries in a custom threat indicator feed.</td>
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
<tr id="parameter-feed_id">
    <td><CopyableCode code="feed_id" /></td>
    <td><code>string</code></td>
    <td>The Intel indicator feed ID.</td>
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

Retrieves details for a specific custom threat indicator feed.

```sql
SELECT
id,
name,
provider_id,
provider_name,
created_on,
description,
is_attributable,
is_downloadable,
is_public,
latest_upload_status,
modified_on
FROM cloudflare.intel.indicator_feeds
WHERE account_id = '{{ account_id }}' -- required
AND feed_id = '{{ feed_id }}' -- required
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

Creates a new custom threat indicator feed for sharing threat intelligence data.

```sql
INSERT INTO cloudflare.intel.indicator_feeds (
description,
name,
account_id
)
SELECT 
'{{ description }}',
'{{ name }}',
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
- name: indicator_feeds
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the indicator_feeds resource.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the example test
    - name: name
      value: "{{ name }}"
      description: |
        The name of the indicator feed
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Revises details for a specific custom threat indicator feed.

```sql
REPLACE cloudflare.intel.indicator_feeds
SET 
description = '{{ description }}',
is_attributable = {{ is_attributable }},
is_downloadable = {{ is_downloadable }},
is_public = {{ is_public }},
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND feed_id = '{{ feed_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="snapshot"
    values={[
        { label: 'snapshot', value: 'snapshot' }
    ]}
>
<TabItem value="snapshot">

Revises the raw data entries in a custom threat indicator feed.

```sql
EXEC cloudflare.intel.indicator_feeds.snapshot 
@account_id='{{ account_id }}' --required, 
@feed_id='{{ feed_id }}' --required 
@@json=
'{
"source": "{{ source }}"
}'
;
```
</TabItem>
</Tabs>
