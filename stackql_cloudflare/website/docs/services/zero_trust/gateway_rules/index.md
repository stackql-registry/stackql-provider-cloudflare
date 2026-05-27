--- 
title: gateway_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_rules
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

Creates, updates, deletes, gets or lists a <code>gateway_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gateway_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.gateway_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get Zero Trust Gateway rule details response.

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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get a single Zero Trust Gateway rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List Zero Trust Gateway rules for an account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Create a new Zero Trust Gateway rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-action"><code>action</code></a></td>
    <td></td>
    <td>Update a configured Zero Trust Gateway rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete a Zero Trust Gateway rule.</td>
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
<tr id="parameter-rule_id">
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td>The rule ID.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a single Zero Trust Gateway rule.

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
FROM cloudflare.zero_trust.gateway_rules
WHERE rule_id = '{{ rule_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Zero Trust Gateway rules for an account.

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
FROM cloudflare.zero_trust.gateway_rules
WHERE account_id = '{{ account_id }}' -- required
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

Create a new Zero Trust Gateway rule.

```sql
INSERT INTO cloudflare.zero_trust.gateway_rules (
action,
description,
device_posture,
enabled,
expiration,
filters,
identity,
name,
precedence,
rule_settings,
schedule,
traffic,
account_id
)
SELECT 
'{{ action }}' /* required */,
'{{ description }}',
'{{ device_posture }}',
{{ enabled }},
'{{ expiration }}',
'{{ filters }}',
'{{ identity }}',
'{{ name }}' /* required */,
{{ precedence }},
'{{ rule_settings }}',
'{{ schedule }}',
'{{ traffic }}',
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
- name: gateway_rules
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the gateway_rules resource.
    - name: action
      value: "{{ action }}"
      description: |
        Specify the action to perform when the associated traffic, identity, and device posture expressions either absent or evaluate to \`true\`.
      valid_values: ['on', 'off', 'allow', 'block', 'scan', 'noscan', 'safesearch', 'ytrestricted', 'isolate', 'noisolate', 'override', 'l4_override', 'egress', 'resolve', 'quarantine', 'redirect']
    - name: description
      value: "{{ description }}"
      description: |
        Specify the rule description.
    - name: device_posture
      value: "{{ device_posture }}"
      description: |
        Specify the wirefilter expression used for device posture check. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response.
      default: 
    - name: enabled
      value: {{ enabled }}
      description: |
        Specify whether the rule is enabled.
      default: false
    - name: expiration
      description: |
        Defines the expiration time stamp and default duration of a DNS policy. Takes precedence over the policy's \`schedule\` configuration, if any. This does not apply to HTTP or network policies. Settable only for \`dns\` rules.
      value:
        duration: {{ duration }}
        expired: {{ expired }}
        expires_at: "{{ expires_at }}"
    - name: filters
      value:
        - "{{ filters }}"
      description: |
        Specify the protocol or layer to evaluate the traffic, identity, and device posture expressions. Can only contain a single value.
    - name: identity
      value: "{{ identity }}"
      description: |
        Specify the wirefilter expression used for identity matching. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response.
      default: 
    - name: name
      value: "{{ name }}"
      description: |
        Specify the rule name.
    - name: precedence
      value: {{ precedence }}
      description: |
        Set the order of your rules. Lower values indicate higher precedence. At each processing phase, evaluate applicable rules in ascending order of this value. Refer to [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform) to manage precedence via Terraform.
    - name: rule_settings
      description: |
        Defines settings for this rule. Settings apply only to specific rule types and must use compatible selectors. If Terraform detects drift, confirm the setting supports your rule type and check whether the API modifies the value. Use API-returned values in your configuration to prevent drift.
      value:
        add_headers: "{{ add_headers }}"
        allow_child_bypass: {{ allow_child_bypass }}
        audit_ssh:
          command_logging: {{ command_logging }}
        biso_admin_controls:
          copy: "{{ copy }}"
          dcp: {{ dcp }}
          dd: {{ dd }}
          dk: {{ dk }}
          download: "{{ download }}"
          dp: {{ dp }}
          du: {{ du }}
          keyboard: "{{ keyboard }}"
          paste: "{{ paste }}"
          printing: "{{ printing }}"
          upload: "{{ upload }}"
          version: "{{ version }}"
          wm_id: "{{ wm_id }}"
        block_page:
          include_context: {{ include_context }}
          target_uri: "{{ target_uri }}"
        block_page_enabled: {{ block_page_enabled }}
        block_reason: "{{ block_reason }}"
        bypass_parent_rule: {{ bypass_parent_rule }}
        check_session:
          duration: "{{ duration }}"
          enforce: {{ enforce }}
        dns_resolvers:
          ipv4:
            - ip: "{{ ip }}"
              port: {{ port }}
              route_through_private_network: {{ route_through_private_network }}
              vnet_id: "{{ vnet_id }}"
          ipv6:
            - ip: "{{ ip }}"
              port: {{ port }}
              route_through_private_network: {{ route_through_private_network }}
              vnet_id: "{{ vnet_id }}"
        egress:
          ipv4: "{{ ipv4 }}"
          ipv4_fallback: "{{ ipv4_fallback }}"
          ipv6: "{{ ipv6 }}"
        forensic_copy:
          enabled: {{ enabled }}
        ignore_cname_category_matches: {{ ignore_cname_category_matches }}
        insecure_disable_dnssec_validation: {{ insecure_disable_dnssec_validation }}
        ip_categories: {{ ip_categories }}
        ip_indicator_feeds: {{ ip_indicator_feeds }}
        l4override:
          ip: "{{ ip }}"
          port: {{ port }}
        notification_settings:
          enabled: {{ enabled }}
          include_context: {{ include_context }}
          msg: "{{ msg }}"
          support_url: "{{ support_url }}"
        override_host: "{{ override_host }}"
        override_ips:
          - "{{ override_ips }}"
        payload_log:
          enabled: {{ enabled }}
        quarantine:
          file_types:
            - "{{ file_types }}"
        redirect:
          include_context: {{ include_context }}
          preserve_path_and_query: {{ preserve_path_and_query }}
          target_uri: "{{ target_uri }}"
        resolve_dns_internally:
          fallback: "{{ fallback }}"
          view_id: "{{ view_id }}"
        resolve_dns_through_cloudflare: {{ resolve_dns_through_cloudflare }}
        untrusted_cert:
          action: "{{ action }}"
    - name: schedule
      description: |
        Defines the schedule for activating DNS policies. Settable only for \`dns\` and \`dns_resolver\` rules.
      value:
        fri: "{{ fri }}"
        mon: "{{ mon }}"
        sat: "{{ sat }}"
        sun: "{{ sun }}"
        thu: "{{ thu }}"
        time_zone: "{{ time_zone }}"
        tue: "{{ tue }}"
        wed: "{{ wed }}"
    - name: traffic
      value: "{{ traffic }}"
      description: |
        Specify the wirefilter expression used for traffic matching. The API automatically formats and sanitizes expressions before storing them. To prevent Terraform state drift, use the formatted expression returned in the API response.
      default: 
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

Update a configured Zero Trust Gateway rule.

```sql
REPLACE cloudflare.zero_trust.gateway_rules
SET 
action = '{{ action }}',
description = '{{ description }}',
device_posture = '{{ device_posture }}',
enabled = {{ enabled }},
expiration = '{{ expiration }}',
filters = '{{ filters }}',
identity = '{{ identity }}',
name = '{{ name }}',
precedence = {{ precedence }},
rule_settings = '{{ rule_settings }}',
schedule = '{{ schedule }}',
traffic = '{{ traffic }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND action = '{{ action }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a Zero Trust Gateway rule.

```sql
DELETE FROM cloudflare.zero_trust.gateway_rules
WHERE rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
