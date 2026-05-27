--- 
title: settings_schema_validation
hide_title: false
hide_table_of_contents: false
keywords:
  - settings_schema_validation
  - api_gateway
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

Creates, updates, deletes, gets or lists a <code>settings_schema_validation</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="settings_schema_validation" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.api_gateway.settings_schema_validation" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_zone"
    values={[
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_zone">

Zone level schema validation settings response

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
    <td><CopyableCode code="validation_default_mitigation_action" /></td>
    <td><code>string</code></td>
    <td>The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request does not conform to schema A special value of of `none` will skip running schema validation entirely for the request when there is no mitigation action defined on the operation (none, log, block) (example: block)</td>
</tr>
<tr>
    <td><CopyableCode code="validation_override_mitigation_action" /></td>
    <td><code>string</code></td>
    <td>When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema validation entirely for the request - `null` indicates that no override is in place (none, )</td>
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
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Retrieves zone level schema validation settings currently set on the zone</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates zone level schema validation settings on the zone</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-validation_default_mitigation_action"><code>validation_default_mitigation_action</code></a></td>
    <td></td>
    <td>Updates zone level schema validation settings on the zone</td>
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
    defaultValue="list_by_zone"
    values={[
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_zone">

Retrieves zone level schema validation settings currently set on the zone

```sql
SELECT
validation_default_mitigation_action,
validation_override_mitigation_action
FROM cloudflare.api_gateway.settings_schema_validation
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Updates zone level schema validation settings on the zone

```sql
UPDATE cloudflare.api_gateway.settings_schema_validation
SET 
validation_default_mitigation_action = '{{ validation_default_mitigation_action }}',
validation_override_mitigation_action = '{{ validation_override_mitigation_action }}'
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
validation_default_mitigation_action,
validation_override_mitigation_action;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_zone"
    values={[
        { label: 'update_by_zone', value: 'update_by_zone' }
    ]}
>
<TabItem value="update_by_zone">

Updates zone level schema validation settings on the zone

```sql
REPLACE cloudflare.api_gateway.settings_schema_validation
SET 
validation_default_mitigation_action = '{{ validation_default_mitigation_action }}',
validation_override_mitigation_action = '{{ validation_override_mitigation_action }}'
WHERE 
zone_id = '{{ zone_id }}' --required
AND validation_default_mitigation_action = '{{ validation_default_mitigation_action }}' --required
RETURNING
validation_default_mitigation_action,
validation_override_mitigation_action;
```
</TabItem>
</Tabs>
