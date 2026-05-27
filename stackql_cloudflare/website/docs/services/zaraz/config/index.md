--- 
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - zaraz
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

Creates, updates, deletes, gets or lists a <code>config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="config" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zaraz.config" /></td></tr>
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

Get Zaraz configuration response.

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
    <td><CopyableCode code="analytics" /></td>
    <td><code>object</code></td>
    <td>Cloudflare Monitoring settings.</td>
</tr>
<tr>
    <td><CopyableCode code="consent" /></td>
    <td><code>object</code></td>
    <td>Consent management configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="dataLayer" /></td>
    <td><code>boolean</code></td>
    <td>Data layer compatibility mode enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="debugKey" /></td>
    <td><code>string</code></td>
    <td>The key for Zaraz debug mode.</td>
</tr>
<tr>
    <td><CopyableCode code="historyChange" /></td>
    <td><code>boolean</code></td>
    <td>Single Page Application support enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td>General Zaraz settings.</td>
</tr>
<tr>
    <td><CopyableCode code="tools" /></td>
    <td><code>object</code></td>
    <td>Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID and value is the tool configuration object.</td>
</tr>
<tr>
    <td><CopyableCode code="triggers" /></td>
    <td><code>object</code></td>
    <td>Triggers set up under Zaraz configuration, where key is the trigger alpha-numeric ID and value is the trigger configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="variables" /></td>
    <td><code>object</code></td>
    <td>Variables set up under Zaraz configuration, where key is the variable alpha-numeric ID and value is the variable configuration. Values of variables of type secret are not included.</td>
</tr>
<tr>
    <td><CopyableCode code="zarazVersion" /></td>
    <td><code>integer</code></td>
    <td>Zaraz internal version of the config.</td>
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
    <td>Gets latest Zaraz configuration for a zone. It can be preview or published configuration, whichever was the last updated. Secret variables values will not be included.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-tools"><code>tools</code></a>, <a href="#parameter-triggers"><code>triggers</code></a>, <a href="#parameter-variables"><code>variables</code></a>, <a href="#parameter-settings"><code>settings</code></a>, <a href="#parameter-dataLayer"><code>dataLayer</code></a>, <a href="#parameter-debugKey"><code>debugKey</code></a>, <a href="#parameter-zarazVersion"><code>zarazVersion</code></a></td>
    <td></td>
    <td>Updates Zaraz configuration for a zone.</td>
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

Gets latest Zaraz configuration for a zone. It can be preview or published configuration, whichever was the last updated. Secret variables values will not be included.

```sql
SELECT
analytics,
consent,
dataLayer,
debugKey,
historyChange,
settings,
tools,
triggers,
variables,
zarazVersion
FROM cloudflare.zaraz.config
WHERE zone_id = '{{ zone_id }}' -- required
;
```
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

Updates Zaraz configuration for a zone.

```sql
REPLACE cloudflare.zaraz.config
SET 
analytics = '{{ analytics }}',
consent = '{{ consent }}',
dataLayer = {{ dataLayer }},
debugKey = '{{ debugKey }}',
historyChange = {{ historyChange }},
settings = '{{ settings }}',
triggers = '{{ triggers }}',
variables = '{{ variables }}',
zarazVersion = {{ zarazVersion }},
tools = '{{ tools }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND tools = '{{ tools }}' --required
AND triggers = '{{ triggers }}' --required
AND variables = '{{ variables }}' --required
AND settings = '{{ settings }}' --required
AND dataLayer = {{ dataLayer }} --required
AND debugKey = '{{ debugKey }}' --required
AND zarazVersion = '{{ zarazVersion }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
