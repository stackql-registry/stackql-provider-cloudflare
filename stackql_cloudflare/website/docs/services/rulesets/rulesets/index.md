--- 
title: rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - rulesets
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

Creates, updates, deletes, gets or lists a <code>rulesets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rulesets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.rulesets.rulesets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_rules_by_tag_by_account"
    values={[
        { label: 'list_rules_by_tag_by_account', value: 'list_rules_by_tag_by_account' },
        { label: 'list_rules_by_tag_by_zone', value: 'list_rules_by_tag_by_zone' },
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_rules_by_tag_by_account">

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
<TabItem value="list_rules_by_tag_by_zone">

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
<TabItem value="get_by_account">

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
<TabItem value="get_by_zone">

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
<TabItem value="list_by_account">

A rulesets response.

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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of the ruleset. (example: 1, title: Version)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

A rulesets response.

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
    <td><a href="#list_rules_by_tag_by_account"><CopyableCode code="list_rules_by_tag_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-rule_tag"><code>rule_tag</code></a>, <a href="#parameter-ruleset_version"><code>ruleset_version</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the rules of a managed account or zone ruleset version for a given tag.</td>
</tr>
<tr>
    <td><a href="#list_rules_by_tag_by_zone"><CopyableCode code="list_rules_by_tag_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-rule_tag"><code>rule_tag</code></a>, <a href="#parameter-ruleset_version"><code>ruleset_version</code></a>, <a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the rules of a managed account or zone ruleset version for a given tag.</td>
</tr>
<tr>
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches the latest version of an account or zone ruleset.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches the latest version of an account or zone ruleset.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetches all rulesets.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Fetches all rulesets.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-phase"><code>phase</code></a></td>
    <td></td>
    <td>Creates a ruleset.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-phase"><code>phase</code></a></td>
    <td></td>
    <td>Creates a ruleset.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates an account or zone ruleset, creating a new version.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates an account or zone ruleset, creating a new version.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes all versions of an existing account or zone ruleset.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-ruleset_id"><code>ruleset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes all versions of an existing account or zone ruleset.</td>
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
<tr id="parameter-rule_tag">
    <td><CopyableCode code="rule_tag" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-ruleset_id">
    <td><CopyableCode code="ruleset_id" /></td>
    <td><code>string</code></td>
    <td>The ruleset ID.</td>
</tr>
<tr id="parameter-ruleset_version">
    <td><CopyableCode code="ruleset_version" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_rules_by_tag_by_account"
    values={[
        { label: 'list_rules_by_tag_by_account', value: 'list_rules_by_tag_by_account' },
        { label: 'list_rules_by_tag_by_zone', value: 'list_rules_by_tag_by_zone' },
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="list_rules_by_tag_by_account">

Fetches the rules of a managed account or zone ruleset version for a given tag.

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
FROM cloudflare.rulesets.rulesets
WHERE rule_tag = '{{ rule_tag }}' -- required
AND ruleset_version = '{{ ruleset_version }}' -- required
AND ruleset_id = '{{ ruleset_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_rules_by_tag_by_zone">

Fetches the rules of a managed account or zone ruleset version for a given tag.

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
FROM cloudflare.rulesets.rulesets
WHERE rule_tag = '{{ rule_tag }}' -- required
AND ruleset_version = '{{ ruleset_version }}' -- required
AND ruleset_id = '{{ ruleset_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_account">

Fetches the latest version of an account or zone ruleset.

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
FROM cloudflare.rulesets.rulesets
WHERE ruleset_id = '{{ ruleset_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches the latest version of an account or zone ruleset.

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
FROM cloudflare.rulesets.rulesets
WHERE ruleset_id = '{{ ruleset_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Fetches all rulesets.

```sql
SELECT
id,
name,
description,
kind,
last_updated,
phase,
version
FROM cloudflare.rulesets.rulesets
WHERE account_id = '{{ account_id }}' -- required
AND cursor = '{{ cursor }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Fetches all rulesets.

```sql
SELECT
id,
name,
description,
kind,
last_updated,
phase,
version
FROM cloudflare.rulesets.rulesets
WHERE zone_id = '{{ zone_id }}' -- required
AND cursor = '{{ cursor }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_account"
    values={[
        { label: 'create_by_account', value: 'create_by_account' },
        { label: 'create_by_zone', value: 'create_by_zone' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_account">

Creates a ruleset.

```sql
INSERT INTO cloudflare.rulesets.rulesets (
description,
name,
kind,
phase,
rules,
account_id
)
SELECT 
'{{ description }}',
'{{ name }}' /* required */,
'{{ kind }}' /* required */,
'{{ phase }}' /* required */,
'{{ rules }}',
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="create_by_zone">

Creates a ruleset.

```sql
INSERT INTO cloudflare.rulesets.rulesets (
description,
name,
kind,
phase,
rules,
zone_id
)
SELECT 
'{{ description }}',
'{{ name }}' /* required */,
'{{ kind }}' /* required */,
'{{ phase }}' /* required */,
'{{ rules }}',
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
- name: rulesets
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the rulesets resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the rulesets resource.
    - name: description
      value: "{{ description }}"
      description: |
        An informative description of the ruleset.
      default: 
    - name: name
      value: "{{ name }}"
      description: |
        The human-readable name of the ruleset.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the ruleset.
      valid_values: ['managed', 'custom', 'root', 'zone']
    - name: phase
      value: "{{ phase }}"
      description: |
        The phase of the ruleset.
      valid_values: ['ddos_l4', 'ddos_l7', 'http_config_settings', 'http_custom_errors', 'http_log_custom_fields', 'http_ratelimit', 'http_request_cache_settings', 'http_request_dynamic_redirect', 'http_request_firewall_custom', 'http_request_firewall_managed', 'http_request_late_transform', 'http_request_origin', 'http_request_redirect', 'http_request_sanitize', 'http_request_sbfm', 'http_request_transform', 'http_response_cache_settings', 'http_response_compression', 'http_response_firewall_managed', 'http_response_headers_transform', 'magic_transit', 'magic_transit_ids_managed', 'magic_transit_managed', 'magic_transit_ratelimit']
    - name: rules
      description: |
        The list of rules in the ruleset.
      value:
        - action: "{{ action }}"
          action_parameters:
            response:
              content: "{{ content }}"
              content_type: "{{ content_type }}"
              status_code: {{ status_code }}
          categories: "{{ categories }}"
          description: "{{ description }}"
          enabled: {{ enabled }}
          exposed_credential_check:
            password_expression: "{{ password_expression }}"
            username_expression: "{{ username_expression }}"
          expression: "{{ expression }}"
          id: "{{ id }}"
          last_updated: "{{ last_updated }}"
          logging:
            enabled: {{ enabled }}
          ratelimit:
            characteristics:
              - "{{ characteristics }}"
            counting_expression: "{{ counting_expression }}"
            mitigation_timeout: {{ mitigation_timeout }}
            period: {{ period }}
            requests_per_period: {{ requests_per_period }}
            requests_to_origin: {{ requests_to_origin }}
            score_per_period: {{ score_per_period }}
            score_response_header_name: "{{ score_response_header_name }}"
          ref: "{{ ref }}"
          version: "{{ version }}"
      default: 
`}</CodeBlock>

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

Updates an account or zone ruleset, creating a new version.

```sql
REPLACE cloudflare.rulesets.rulesets
SET 
description = '{{ description }}',
name = '{{ name }}',
kind = '{{ kind }}',
phase = '{{ phase }}',
rules = '{{ rules }}'
WHERE 
ruleset_id = '{{ ruleset_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates an account or zone ruleset, creating a new version.

```sql
REPLACE cloudflare.rulesets.rulesets
SET 
description = '{{ description }}',
name = '{{ name }}',
kind = '{{ kind }}',
phase = '{{ phase }}',
rules = '{{ rules }}'
WHERE 
ruleset_id = '{{ ruleset_id }}' --required
AND zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_account"
    values={[
        { label: 'delete_by_account', value: 'delete_by_account' },
        { label: 'delete_by_zone', value: 'delete_by_zone' }
    ]}
>
<TabItem value="delete_by_account">

Deletes all versions of an existing account or zone ruleset.

```sql
DELETE FROM cloudflare.rulesets.rulesets
WHERE ruleset_id = '{{ ruleset_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes all versions of an existing account or zone ruleset.

```sql
DELETE FROM cloudflare.rulesets.rulesets
WHERE ruleset_id = '{{ ruleset_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
