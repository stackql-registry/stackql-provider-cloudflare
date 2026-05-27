--- 
title: accounts_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_pipelines
  - pipelines
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

Creates, updates, deletes, gets or lists an <code>accounts_pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="accounts_pipelines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.pipelines.accounts_pipelines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

[DEPRECATED] Describes the configuration of a pipeline.

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
    <td>Specifies the pipeline identifier. (example: 123f8a8258064ed892a347f173372359)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Defines the name of the pipeline. (example: sample_pipeline)</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Indicates the endpoint URL to send traffic. (example: https://123f8a8258064ed892a347f173372359.pipelines.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number</code></td>
    <td>Indicates the version number of last saved configuration.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

[DEPRECATED] Lists the pipelines. Use /pipelines/v1/pipelines instead.

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
    <td>Specifies the pipeline identifier. (example: 123f8a8258064ed892a347f173372359)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Defines the name of the pipeline. (example: sample_pipeline)</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Indicates the endpoint URL to send traffic. (example: https://123f8a8258064ed892a347f173372359.pipelines.cloudflare.com)</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number</code></td>
    <td>Indicates the version number of last saved configuration.</td>
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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-pipeline_name"><code>pipeline_name</code></a></td>
    <td></td>
    <td>[DEPRECATED] Get configuration of a pipeline. Use the new /pipelines/v1/pipelines endpoint instead.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-search"><code>search</code></a>, <a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>[DEPRECATED] List, filter, and paginate pipelines in an account. Use the new /pipelines/v1/pipelines endpoint instead.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>[DEPRECATED] Create a new pipeline. Use the new /pipelines/v1/pipelines endpoint instead.</td>
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
<tr id="parameter-pipeline_name">
    <td><CopyableCode code="pipeline_name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_account">

[DEPRECATED] Get configuration of a pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

```sql
SELECT
id,
name,
destination,
endpoint,
source,
version
FROM cloudflare.pipelines.accounts_pipelines
WHERE account_id = '{{ account_id }}' -- required
AND pipeline_name = '{{ pipeline_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

[DEPRECATED] List, filter, and paginate pipelines in an account. Use the new /pipelines/v1/pipelines endpoint instead.

```sql
SELECT
id,
name,
destination,
endpoint,
source,
version
FROM cloudflare.pipelines.accounts_pipelines
WHERE account_id = '{{ account_id }}' -- required
AND search = '{{ search }}'
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

[DEPRECATED] Create a new pipeline. Use the new /pipelines/v1/pipelines endpoint instead.

```sql
INSERT INTO cloudflare.pipelines.accounts_pipelines (
destination,
name,
source,
account_id
)
SELECT 
'{{ destination }}' /* required */,
'{{ name }}' /* required */,
'{{ source }}' /* required */,
'{{ account_id }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: accounts_pipelines
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the accounts_pipelines resource.
    - name: destination
      value:
        batch:
          max_bytes: {{ max_bytes }}
          max_duration_s: {{ max_duration_s }}
          max_rows: {{ max_rows }}
        compression:
          type: "{{ type }}"
        credentials:
          access_key_id: "{{ access_key_id }}"
          endpoint: "{{ endpoint }}"
          secret_access_key: "{{ secret_access_key }}"
        format: "{{ format }}"
        path:
          bucket: "{{ bucket }}"
          filename: "{{ filename }}"
          filepath: "{{ filepath }}"
          prefix: "{{ prefix }}"
        type: "{{ type }}"
    - name: name
      value: "{{ name }}"
      description: |
        Defines the name of the pipeline.
    - name: source
      value:
        - authentication: {{ authentication }}
          cors:
            origins:
              - "{{ origins }}"
          format: "{{ format }}"
          type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>
