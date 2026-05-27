--- 
title: rules_tenant
hide_title: false
hide_table_of_contents: false
keywords:
  - rules_tenant
  - zero_trust
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

Creates, updates, deletes, gets or lists a <code>rules_tenant</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="rules_tenant" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.rules_tenant" /></td></tr>
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

List Zero Trust Gateway rules response.

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
    <td>Identify the API resource with a UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Specify the rule name. (example: block bad websites)</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>Specify the action to perform when the associated traffic, identity, and device posture expressions either absent or evaluate to `true`. (on, off, allow, block, scan, noscan, safesearch, ytrestricted, isolate, noisolate, override, l4_override, egress, resolve, quarantine, redirect) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="deleted_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicate the date of deletion, if any. (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Specify the rule description. (example: Block bad websites based on their host name.)</td>
</tr>
<tr>
    <td><CopyableCode code="device_posture" /></td>
    <td><code>string</code></td>
    <td>Specify the wirefilter expression used for device posture check. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response. (default: , example: any(device_posture.checks.passed[*] in &#123;"1308749e-fcfb-4ebc-b051-fe022b632644"&#125;), x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Specify whether the rule is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>object</code></td>
    <td>Defines the expiration time stamp and default duration of a DNS policy. Takes precedence over the policy's `schedule` configuration, if any. This does not apply to HTTP or network policies. Settable only for `dns` rules. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>array</code></td>
    <td>Specify the protocol or layer to evaluate the traffic, identity, and device posture expressions. Can only contain a single value.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>string</code></td>
    <td>Specify the wirefilter expression used for identity matching. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response. (default: , example: any(identity.groups.name[*] in &#123;"finance"&#125;), x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>Set the order of your rules. Lower values indicate higher precedence. At each processing phase, evaluate applicable rules in ascending order of this value. Refer to [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform) to manage precedence via Terraform. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="read_only" /></td>
    <td><code>boolean</code></td>
    <td>Indicate that this rule is shared via the Orgs API and read only. (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="rule_settings" /></td>
    <td><code>object</code></td>
    <td>Defines settings for this rule. Settings apply only to specific rule types and must use compatible selectors. If Terraform detects drift, confirm the setting supports your rule type and check whether the API modifies the value. Use API-returned values in your configuration to prevent drift. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Defines the schedule for activating DNS policies. Settable only for `dns` and `dns_resolver` rules. (x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="sharable" /></td>
    <td><code>boolean</code></td>
    <td>Indicate that this rule is sharable via the Orgs API. (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="source_account" /></td>
    <td><code>string</code></td>
    <td>Provide the account tag of the account that created the rule. (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="traffic" /></td>
    <td><code>string</code></td>
    <td>Specify the wirefilter expression used for traffic matching. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response. (default: , example: http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10, x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>integer</code></td>
    <td>Indicate the version number of the rule(read-only). (x-stainless-terraform-configurability: computed)</td>
</tr>
<tr>
    <td><CopyableCode code="warning_status" /></td>
    <td><code>string</code></td>
    <td>Indicate a warning for a misconfigured rule, if any. (x-stainless-terraform-configurability: computed)</td>
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
    <td>List Zero Trust Gateway rules for the parent account of an account in the MSP configuration.</td>
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

List Zero Trust Gateway rules for the parent account of an account in the MSP configuration.

```sql
SELECT
id,
name,
action,
created_at,
deleted_at,
description,
device_posture,
enabled,
expiration,
filters,
identity,
precedence,
read_only,
rule_settings,
schedule,
sharable,
source_account,
traffic,
updated_at,
version,
warning_status
FROM cloudflare.zero_trust.rules_tenant
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
