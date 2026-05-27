--- 
title: phases
hide_title: false
hide_table_of_contents: false
keywords:
  - phases
  - rulesets
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

Creates, updates, deletes, gets or lists a <code>phases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="phases" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rulesets.phases" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

A ruleset response.

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
    <td>The unique ID of the ruleset. (example: 2f2feab2026849078ba485f918791bdc, title: Ruleset ID)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The human-readable name of the ruleset. (title: Name)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative description of the ruleset. (default: , title: Description)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the ruleset. (managed, custom, root, zone) (example: root, title: Kind)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the ruleset was last modified. (title: Last Updated)</td>
</tr>
<tr>
    <td><CopyableCode code="phase" /></td>
    <td><code>string</code></td>
    <td>The phase of the ruleset. (ddos_l4, ddos_l7, http_config_settings, http_custom_errors, http_log_custom_fields, http_ratelimit, http_request_cache_settings, http_request_dynamic_redirect, http_request_firewall_custom, http_request_firewall_managed, http_request_late_transform, http_request_origin, http_request_redirect, http_request_sanitize, http_request_sbfm, http_request_transform, http_response_cache_settings, http_response_compression, http_response_firewall_managed, http_response_headers_transform, magic_transit, magic_transit_ids_managed, magic_transit_managed, magic_transit_ratelimit) (example: http_request_firewall_custom, title: Phase)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>The list of rules in the ruleset. (title: Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the ruleset. (example: 1, title: Version)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

A ruleset response.

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
    <td>The unique ID of the ruleset. (example: 2f2feab2026849078ba485f918791bdc, title: Ruleset ID)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The human-readable name of the ruleset. (title: Name)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An informative description of the ruleset. (default: , title: Description)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the ruleset. (managed, custom, root, zone) (example: root, title: Kind)</td>
</tr>
<tr>
    <td><CopyableCode code="last_updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp of when the ruleset was last modified. (title: Last Updated)</td>
</tr>
<tr>
    <td><CopyableCode code="phase" /></td>
    <td><code>string</code></td>
    <td>The phase of the ruleset. (ddos_l4, ddos_l7, http_config_settings, http_custom_errors, http_log_custom_fields, http_ratelimit, http_request_cache_settings, http_request_dynamic_redirect, http_request_firewall_custom, http_request_firewall_managed, http_request_late_transform, http_request_origin, http_request_redirect, http_request_sanitize, http_request_sbfm, http_request_transform, http_response_cache_settings, http_response_compression, http_response_firewall_managed, http_response_headers_transform, magic_transit, magic_transit_ids_managed, magic_transit_managed, magic_transit_ratelimit) (example: http_request_firewall_custom, title: Phase)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>The list of rules in the ruleset. (title: Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the ruleset. (example: 1, title: Version)</td>
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
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ruleset_phase"><code>ruleset_phase</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the latest version of the account or zone entry point ruleset for a given phase.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ruleset_phase"><code>ruleset_phase</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the latest version of the account or zone entry point ruleset for a given phase.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-ruleset_phase"><code>ruleset_phase</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-last_updated"><code>last_updated</code></a></td>
    <td></td>
    <td>Updates an account or zone entry point ruleset, creating a new version.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-ruleset_phase"><code>ruleset_phase</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-version"><code>version</code></a>, <a href="#parameter-last_updated"><code>last_updated</code></a></td>
    <td></td>
    <td>Updates an account or zone entry point ruleset, creating a new version.</td>
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
<tr id="parameter-ruleset_phase">
    <td><CopyableCode code="ruleset_phase" /></td>
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
    defaultValue="list_by_account"
    values={[
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_by_account">

Fetches the latest version of the account or zone entry point ruleset for a given phase.

```sql
SELECT
id,
name,
description,
kind,
last_updated,
phase,
rules,
version
FROM cloudflare.rulesets.phases
WHERE ruleset_phase = '{{ ruleset_phase }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Fetches the latest version of the account or zone entry point ruleset for a given phase.

```sql
SELECT
id,
name,
description,
kind,
last_updated,
phase,
rules,
version
FROM cloudflare.rulesets.phases
WHERE ruleset_phase = '{{ ruleset_phase }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update_by_account"
    values={[
        { label: 'update_by_account', value: 'update_by_account' },
        { label: 'update_by_zone', value: 'update_by_zone' }
    ]}
>
<TabItem value="update_by_account">

Updates an account or zone entry point ruleset, creating a new version.

```sql
REPLACE cloudflare.rulesets.phases
SET 
description = '{{ description }}',
name = '{{ name }}',
rules = '{{ rules }}'
WHERE 
ruleset_phase = '{{ ruleset_phase }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates an account or zone entry point ruleset, creating a new version.

```sql
REPLACE cloudflare.rulesets.phases
SET 
description = '{{ description }}',
name = '{{ name }}',
rules = '{{ rules }}'
WHERE 
ruleset_phase = '{{ ruleset_phase }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
