--- 
title: apps_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_policies
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

Creates, updates, deletes, gets or lists an <code>apps_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.apps_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get an Access policy response.

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
    <td>The UUID of the policy (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access policy. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_groups" /></td>
    <td><code>array</code></td>
    <td>Administrators who can approve a temporary authentication request. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_required" /></td>
    <td><code>boolean</code></td>
    <td>Requires the user to request access from an administrator at the start of each session.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_rules" /></td>
    <td><code>object</code></td>
    <td>The rules that define how users may connect to targets secured by your application. (title: Connection Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action. (allow, deny, non_identity, bypass) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_required" /></td>
    <td><code>boolean</code></td>
    <td>Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>The order of execution for this policy. Must be unique for each policy within an app.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_prompt" /></td>
    <td><code>string</code></td>
    <td>A custom message that will appear on the purpose justification screen. (example: Please enter a justification for entering this protected domain.)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_required" /></td>
    <td><code>boolean</code></td>
    <td>Require users to enter a justification when they log in to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_zone">

Get an Access policy response.

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
    <td>The UUID of the policy (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access policy. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_groups" /></td>
    <td><code>array</code></td>
    <td>Administrators who can approve a temporary authentication request. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_required" /></td>
    <td><code>boolean</code></td>
    <td>Requires the user to request access from an administrator at the start of each session.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_rules" /></td>
    <td><code>object</code></td>
    <td>The rules that define how users may connect to targets secured by your application. (title: Connection Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action. (allow, deny, non_identity, bypass) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_required" /></td>
    <td><code>boolean</code></td>
    <td>Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>The order of execution for this policy. Must be unique for each policy within an app.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_prompt" /></td>
    <td><code>string</code></td>
    <td>A custom message that will appear on the purpose justification screen. (example: Please enter a justification for entering this protected domain.)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_required" /></td>
    <td><code>boolean</code></td>
    <td>Require users to enter a justification when they log in to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List Access application policies response

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
    <td>The UUID of the policy (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access policy. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_groups" /></td>
    <td><code>array</code></td>
    <td>Administrators who can approve a temporary authentication request. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_required" /></td>
    <td><code>boolean</code></td>
    <td>Requires the user to request access from an administrator at the start of each session.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_rules" /></td>
    <td><code>object</code></td>
    <td>The rules that define how users may connect to targets secured by your application. (title: Connection Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action. (allow, deny, non_identity, bypass) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_required" /></td>
    <td><code>boolean</code></td>
    <td>Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>The order of execution for this policy. Must be unique for each policy within an app.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_prompt" /></td>
    <td><code>string</code></td>
    <td>A custom message that will appear on the purpose justification screen. (example: Please enter a justification for entering this protected domain.)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_required" /></td>
    <td><code>boolean</code></td>
    <td>Require users to enter a justification when they log in to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List Access application policies response

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
    <td>The UUID of the policy (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the Access policy. (example: Allow devs)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_groups" /></td>
    <td><code>array</code></td>
    <td>Administrators who can approve a temporary authentication request. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="approval_required" /></td>
    <td><code>boolean</code></td>
    <td>Requires the user to request access from an administrator at the start of each session.</td>
</tr>
<tr>
    <td><CopyableCode code="connection_rules" /></td>
    <td><code>object</code></td>
    <td>The rules that define how users may connect to targets secured by your application. (title: Connection Rules)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>The action Access will take if a user matches this policy. Infrastructure application policies can only use the Allow action. (allow, deny, non_identity, bypass) (example: allow)</td>
</tr>
<tr>
    <td><CopyableCode code="exclude" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="include" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="isolation_required" /></td>
    <td><code>boolean</code></td>
    <td>Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.</td>
</tr>
<tr>
    <td><CopyableCode code="mfa_config" /></td>
    <td><code>object</code></td>
    <td>Configures multi-factor authentication (MFA) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="precedence" /></td>
    <td><code>integer</code></td>
    <td>The order of execution for this policy. Must be unique for each policy within an app.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_prompt" /></td>
    <td><code>string</code></td>
    <td>A custom message that will appear on the purpose justification screen. (example: Please enter a justification for entering this protected domain.)</td>
</tr>
<tr>
    <td><CopyableCode code="purpose_justification_required" /></td>
    <td><code>boolean</code></td>
    <td>Require users to enter a justification when they log in to the application.</td>
</tr>
<tr>
    <td><CopyableCode code="require" /></td>
    <td><code>array</code></td>
    <td>Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules. (x-stainless-collection-type: set)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>string</code></td>
    <td>The amount of time that tokens issued for the application will be valid. Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. (default: 24h, example: 24h)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
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
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches a single Access policy configured for an application. Returns both exclusively owned and reusable policies used by the application.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches a single Access policy configured for an application. Returns both exclusively owned and reusable policies used by the application.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists Access policies configured for an application. Returns both exclusively scoped and reusable policies used by the application.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists Access policies configured for an application. Returns both exclusively scoped and reusable policies used by the application.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Creates a policy applying exclusive to a single application that defines the users or groups who can reach it. We recommend creating a reusable policy instead and subsequently referencing its ID in the application's 'policies' array.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Creates a policy applying exclusive to a single application that defines the users or groups who can reach it. We recommend creating a reusable policy instead and subsequently referencing its ID in the application's 'policies' array.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates an Access policy specific to an application. To update a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates an Access policy specific to an application. To update a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes an Access policy specific to an application. To delete a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes an Access policy specific to an application. To delete a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>The Access application ID.</td>
</tr>
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' },
        { label: 'list_by_zone', value: 'list_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Fetches a single Access policy configured for an application. Returns both exclusively owned and reusable policies used by the application.

```sql
SELECT
id,
name,
approval_groups,
approval_required,
connection_rules,
created_at,
decision,
exclude,
include,
isolation_required,
mfa_config,
precedence,
purpose_justification_prompt,
purpose_justification_required,
require,
session_duration,
updated_at
FROM cloudflare.zero_trust.apps_policies
WHERE app_id = '{{ app_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Fetches a single Access policy configured for an application. Returns both exclusively owned and reusable policies used by the application.

```sql
SELECT
id,
name,
approval_groups,
approval_required,
connection_rules,
created_at,
decision,
exclude,
include,
isolation_required,
mfa_config,
precedence,
purpose_justification_prompt,
purpose_justification_required,
require,
session_duration,
updated_at
FROM cloudflare.zero_trust.apps_policies
WHERE app_id = '{{ app_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_account">

Lists Access policies configured for an application. Returns both exclusively scoped and reusable policies used by the application.

```sql
SELECT
id,
name,
approval_groups,
approval_required,
connection_rules,
created_at,
decision,
exclude,
include,
isolation_required,
mfa_config,
precedence,
purpose_justification_prompt,
purpose_justification_required,
require,
session_duration,
updated_at
FROM cloudflare.zero_trust.apps_policies
WHERE app_id = '{{ app_id }}' -- required
AND account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_zone">

Lists Access policies configured for an application. Returns both exclusively scoped and reusable policies used by the application.

```sql
SELECT
id,
name,
approval_groups,
approval_required,
connection_rules,
created_at,
decision,
exclude,
include,
isolation_required,
mfa_config,
precedence,
purpose_justification_prompt,
purpose_justification_required,
require,
session_duration,
updated_at
FROM cloudflare.zero_trust.apps_policies
WHERE app_id = '{{ app_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
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

Creates a policy applying exclusive to a single application that defines the users or groups who can reach it. We recommend creating a reusable policy instead and subsequently referencing its ID in the application's 'policies' array.

```sql
INSERT INTO cloudflare.zero_trust.apps_policies (
precedence,
approval_groups,
approval_required,
connection_rules,
isolation_required,
mfa_config,
purpose_justification_prompt,
purpose_justification_required,
session_duration,
app_id,
account_id
)
SELECT 
{{ precedence }},
'{{ approval_groups }}',
{{ approval_required }},
'{{ connection_rules }}',
{{ isolation_required }},
'{{ mfa_config }}',
'{{ purpose_justification_prompt }}',
{{ purpose_justification_required }},
'{{ session_duration }}',
'{{ app_id }}',
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

Creates a policy applying exclusive to a single application that defines the users or groups who can reach it. We recommend creating a reusable policy instead and subsequently referencing its ID in the application's 'policies' array.

```sql
INSERT INTO cloudflare.zero_trust.apps_policies (
precedence,
approval_groups,
approval_required,
connection_rules,
isolation_required,
mfa_config,
purpose_justification_prompt,
purpose_justification_required,
session_duration,
app_id,
zone_id
)
SELECT 
{{ precedence }},
'{{ approval_groups }}',
{{ approval_required }},
'{{ connection_rules }}',
{{ isolation_required }},
'{{ mfa_config }}',
'{{ purpose_justification_prompt }}',
{{ purpose_justification_required }},
'{{ session_duration }}',
'{{ app_id }}',
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
- name: apps_policies
  props:
    - name: app_id
      value: "{{ app_id }}"
      description: Required parameter for the apps_policies resource.
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the apps_policies resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the apps_policies resource.
    - name: precedence
      value: {{ precedence }}
      description: |
        The order of execution for this policy. Must be unique for each policy within an app.
    - name: approval_groups
      description: |
        Administrators who can approve a temporary authentication request.
      value:
        - approvals_needed: {{ approvals_needed }}
          email_addresses: "{{ email_addresses }}"
          email_list_uuid: "{{ email_list_uuid }}"
    - name: approval_required
      value: {{ approval_required }}
      description: |
        Requires the user to request access from an administrator at the start of each session.
    - name: connection_rules
      description: |
        The rules that define how users may connect to targets secured by your application.
      value:
        rdp:
          allowed_clipboard_local_to_remote_formats:
            - "{{ allowed_clipboard_local_to_remote_formats }}"
          allowed_clipboard_remote_to_local_formats:
            - "{{ allowed_clipboard_remote_to_local_formats }}"
    - name: isolation_required
      value: {{ isolation_required }}
      description: |
        Require this application to be served in an isolated browser for users matching this policy. 'Client Web Isolation' must be on for the account in order to use this feature.
    - name: mfa_config
      description: |
        Configures multi-factor authentication (MFA) settings.
      value:
        allowed_authenticators:
          - "{{ allowed_authenticators }}"
        mfa_disabled: {{ mfa_disabled }}
        session_duration: "{{ session_duration }}"
    - name: purpose_justification_prompt
      value: "{{ purpose_justification_prompt }}"
      description: |
        A custom message that will appear on the purpose justification screen.
    - name: purpose_justification_required
      value: {{ purpose_justification_required }}
      description: |
        Require users to enter a justification when they log in to the application.
    - name: session_duration
      value: "{{ session_duration }}"
      description: |
        The amount of time that tokens issued for the application will be valid. Must be in the format \`300ms\` or \`2h45m\`. Valid time units are: ns, us (or µs), ms, s, m, h.
      default: 24h
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

Updates an Access policy specific to an application. To update a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.

```sql
REPLACE cloudflare.zero_trust.apps_policies
SET 
precedence = {{ precedence }},
approval_groups = '{{ approval_groups }}',
approval_required = {{ approval_required }},
connection_rules = '{{ connection_rules }}',
isolation_required = {{ isolation_required }},
mfa_config = '{{ mfa_config }}',
purpose_justification_prompt = '{{ purpose_justification_prompt }}',
purpose_justification_required = {{ purpose_justification_required }},
session_duration = '{{ session_duration }}'
WHERE 
app_id = '{{ app_id }}' --required
AND policy_id = '{{ policy_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates an Access policy specific to an application. To update a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.

```sql
REPLACE cloudflare.zero_trust.apps_policies
SET 
precedence = {{ precedence }},
approval_groups = '{{ approval_groups }}',
approval_required = {{ approval_required }},
connection_rules = '{{ connection_rules }}',
isolation_required = {{ isolation_required }},
mfa_config = '{{ mfa_config }}',
purpose_justification_prompt = '{{ purpose_justification_prompt }}',
purpose_justification_required = {{ purpose_justification_required }},
session_duration = '{{ session_duration }}'
WHERE 
app_id = '{{ app_id }}' --required
AND policy_id = '{{ policy_id }}' --required
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

Deletes an Access policy specific to an application. To delete a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.

```sql
DELETE FROM cloudflare.zero_trust.apps_policies
WHERE app_id = '{{ app_id }}' --required
AND policy_id = '{{ policy_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes an Access policy specific to an application. To delete a reusable policy, use the /account or zones/&#123;account or zone_id&#125;/policies/&#123;uid&#125; endpoint.

```sql
DELETE FROM cloudflare.zero_trust.apps_policies
WHERE app_id = '{{ app_id }}' --required
AND policy_id = '{{ policy_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
