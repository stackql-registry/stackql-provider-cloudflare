--- 
title: namespaces_instance_search
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_instance_search
  - aisearch
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

Creates, updates, deletes, gets or lists a <code>namespaces_instance_search</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="namespaces_instance_search" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.aisearch.namespaces_instance_search" /></td></tr>
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
    <td><a href="#search_by_account"><CopyableCode code="search_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Executes a semantic search query against an AI Search instance to find relevant indexed content.</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Resource ID.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="search_by_account"
    values={[
        { label: 'search_by_account', value: 'search_by_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="search_by_account">

Executes a semantic search query against an AI Search instance to find relevant indexed content.

```sql
INSERT INTO cloudflare.aisearch.namespaces_instance_search (
ai_search_options,
messages,
query,
id,
account_id,
name
)
SELECT 
'{{ ai_search_options }}',
'{{ messages }}',
'{{ query }}',
'{{ id }}',
'{{ account_id }}',
'{{ name }}'
RETURNING
result,
success
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: namespaces_instance_search
  props:
    - name: id
      value: "{{ id }}"
      description: Required parameter for the namespaces_instance_search resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the namespaces_instance_search resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the namespaces_instance_search resource.
    - name: ai_search_options
      value:
        cache:
          cache_threshold: "{{ cache_threshold }}"
          enabled: {{ enabled }}
        query_rewrite:
          enabled: {{ enabled }}
          model: "{{ model }}"
          rewrite_prompt: "{{ rewrite_prompt }}"
        reranking:
          enabled: {{ enabled }}
          match_threshold: {{ match_threshold }}
          model: "{{ model }}"
        retrieval:
          boost_by:
            - direction: "{{ direction }}"
              field: "{{ field }}"
          context_expansion: {{ context_expansion }}
          filters: "{{ filters }}"
          fusion_method: "{{ fusion_method }}"
          keyword_match_mode: "{{ keyword_match_mode }}"
          match_threshold: {{ match_threshold }}
          max_num_results: {{ max_num_results }}
          retrieval_type: "{{ retrieval_type }}"
          return_on_failure: {{ return_on_failure }}
    - name: messages
      value:
        - content: "{{ content }}"
          role: "{{ role }}"
    - name: query
      value: "{{ query }}"
      description: |
        A simple text query string. Alternative to 'messages' — provide either this or 'messages', not both.
`}</CodeBlock>

</TabItem>
</Tabs>
