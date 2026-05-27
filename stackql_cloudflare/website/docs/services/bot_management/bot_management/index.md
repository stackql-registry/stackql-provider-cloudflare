--- 
title: bot_management
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_management
  - bot_management
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

Creates, updates, deletes, gets or lists a <code>bot_management</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="bot_management" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.bot_management.bot_management" /></td></tr>
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

Bot Management config response

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
    <td><CopyableCode code="ai_bots_protection" /></td>
    <td><code>string</code></td>
    <td>Enable rule to block AI Scrapers and Crawlers. Please note the value `only_on_ad_pages` is currently not available for Enterprise customers. (block, disabled, only_on_ad_pages) (example: block, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_update_model" /></td>
    <td><code>boolean</code></td>
    <td>Automatically update to the newest bot detection models created by Cloudflare as they are released. [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes) (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="bm_cookie_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates that the bot management cookie can be placed on end user devices accessing the site. Defaults to true (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="cf_robots_variant" /></td>
    <td><code>string</code></td>
    <td>Specifies the Robots Access Control License variant to use. (off, policy_only) (example: policy_only, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="content_bots_protection" /></td>
    <td><code>string</code></td>
    <td>Enable rule to block content bots. When enabled, blocks automated traffic with low bot scores, excluding safe verified bot categories. Exceptions should be managed via skip rules. (block, disabled) (example: disabled, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="crawler_protection" /></td>
    <td><code>string</code></td>
    <td>Enable rule to punish AI Scrapers and Crawlers via a link maze. (enabled, disabled) (example: enabled, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="enable_js" /></td>
    <td><code>boolean</code></td>
    <td>Use lightweight, invisible JavaScript detections to improve Bot Management. [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/). (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="fight_mode" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable Bot Fight Mode. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="is_robots_txt_managed" /></td>
    <td><code>boolean</code></td>
    <td>Enable cloudflare managed robots.txt. If an existing robots.txt is detected, then managed robots.txt will be prepended to the existing robots.txt. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="optimize_wordpress" /></td>
    <td><code>boolean</code></td>
    <td>Whether to optimize Super Bot Fight Mode protections for Wordpress. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="sbfm_definitely_automated" /></td>
    <td><code>string</code></td>
    <td>Super Bot Fight Mode (SBFM) action to take on definitely automated requests. (allow, block, managed_challenge) (example: allow, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="sbfm_likely_automated" /></td>
    <td><code>string</code></td>
    <td>Super Bot Fight Mode (SBFM) action to take on likely automated requests. (allow, block, managed_challenge) (example: allow, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="sbfm_static_resource_protection" /></td>
    <td><code>boolean</code></td>
    <td>Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if static resources on your application need bot protection. Note: Static resource protection can also result in legitimate traffic being blocked. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="sbfm_verified_bots" /></td>
    <td><code>string</code></td>
    <td>Super Bot Fight Mode (SBFM) action to take on verified bots requests. (allow, block) (example: allow, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="stale_zone_configuration" /></td>
    <td><code>object</code></td>
    <td>A read-only field that shows which unauthorized settings are currently active on the zone. These settings typically result from upgrades or downgrades. (title: stale_zone_configuration)</td>
</tr>
<tr>
    <td><CopyableCode code="suppress_session_score" /></td>
    <td><code>boolean</code></td>
    <td>Whether to disable tracking the highest bot score for a session in the Bot Management cookie. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="using_latest_model" /></td>
    <td><code>boolean</code></td>
    <td>A read-only field that indicates whether the zone currently is running the latest ML model. (x-stainless-terraform-configurability: computed_optional)</td>
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
    <td>Retrieve a zone's Bot Management Config</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates the Bot Management configuration for a zone. This API is used to update: - **Bot Fight Mode** - **Super Bot Fight Mode** - **Bot Management for Enterprise** See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more information on the different plans \ If you recently upgraded or downgraded your plan, refer to the following examples to clean up old configurations. Copy and paste the example body to remove old zone configurations based on your current plan. **Clean up configuration for Bot Fight Mode plan:** ```json &#123; "sbfm_likely_automated": "allow", "sbfm_definitely_automated": "allow", "sbfm_verified_bots": "allow", "sbfm_static_resource_protection": false, "optimize_wordpress": false, "suppress_session_score": false &#125; ``` **Clean up configuration for SBFM Pro plan:** ```json &#123; "sbfm_likely_automated": "allow", "fight_mode": false &#125; ``` **Clean up configuration for SBFM Biz plan:** ```json &#123; "fight_mode": false &#125; ``` **Clean up configuration for BM Enterprise Subscription plan:** It is strongly recommended that you ensure you have [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to protect your zone before disabling the SBFM rules. Without these protections, your zone is vulnerable to attacks. ```json &#123; "sbfm_likely_automated": "allow", "sbfm_definitely_automated": "allow", "sbfm_verified_bots": "allow", "sbfm_static_resource_protection": false, "optimize_wordpress": false, "fight_mode": false &#125; ```</td>
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

Retrieve a zone's Bot Management Config

```sql
SELECT
ai_bots_protection,
auto_update_model,
bm_cookie_enabled,
cf_robots_variant,
content_bots_protection,
crawler_protection,
enable_js,
fight_mode,
is_robots_txt_managed,
optimize_wordpress,
sbfm_definitely_automated,
sbfm_likely_automated,
sbfm_static_resource_protection,
sbfm_verified_bots,
stale_zone_configuration,
suppress_session_score,
using_latest_model
FROM cloudflare.bot_management.bot_management
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

Updates the Bot Management configuration for a zone. This API is used to update: - **Bot Fight Mode** - **Super Bot Fight Mode** - **Bot Management for Enterprise** See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more information on the different plans \ If you recently upgraded or downgraded your plan, refer to the following examples to clean up old configurations. Copy and paste the example body to remove old zone configurations based on your current plan. **Clean up configuration for Bot Fight Mode plan:** ```json &#123; "sbfm_likely_automated": "allow", "sbfm_definitely_automated": "allow", "sbfm_verified_bots": "allow", "sbfm_static_resource_protection": false, "optimize_wordpress": false, "suppress_session_score": false &#125; ``` **Clean up configuration for SBFM Pro plan:** ```json &#123; "sbfm_likely_automated": "allow", "fight_mode": false &#125; ``` **Clean up configuration for SBFM Biz plan:** ```json &#123; "fight_mode": false &#125; ``` **Clean up configuration for BM Enterprise Subscription plan:** It is strongly recommended that you ensure you have [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to protect your zone before disabling the SBFM rules. Without these protections, your zone is vulnerable to attacks. ```json &#123; "sbfm_likely_automated": "allow", "sbfm_definitely_automated": "allow", "sbfm_verified_bots": "allow", "sbfm_static_resource_protection": false, "optimize_wordpress": false, "fight_mode": false &#125; ```

```sql
REPLACE cloudflare.bot_management.bot_management
SET 
ai_bots_protection = '{{ ai_bots_protection }}',
cf_robots_variant = '{{ cf_robots_variant }}',
content_bots_protection = '{{ content_bots_protection }}',
crawler_protection = '{{ crawler_protection }}',
enable_js = {{ enable_js }},
is_robots_txt_managed = {{ is_robots_txt_managed }},
fight_mode = {{ fight_mode }},
optimize_wordpress = {{ optimize_wordpress }},
sbfm_definitely_automated = '{{ sbfm_definitely_automated }}',
sbfm_static_resource_protection = {{ sbfm_static_resource_protection }},
sbfm_verified_bots = '{{ sbfm_verified_bots }}',
sbfm_likely_automated = '{{ sbfm_likely_automated }}',
auto_update_model = {{ auto_update_model }},
bm_cookie_enabled = {{ bm_cookie_enabled }},
suppress_session_score = {{ suppress_session_score }}
WHERE 
zone_id = '{{ zone_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
