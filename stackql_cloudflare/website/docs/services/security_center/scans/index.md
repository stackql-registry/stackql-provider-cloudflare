--- 
title: scans
hide_title: false
hide_table_of_contents: false
keywords:
  - scans
  - security_center
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

Creates, updates, deletes, gets or lists a <code>scans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scans" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.security_center.scans" /></td></tr>
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

The request was successful.

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
    <td><CopyableCode code="scan_id" /></td>
    <td><code>string</code></td>
    <td>An opaque identifier for the scan. (example: d5e94e48-504f-4a7f-a8c4-e0dc2e05e5f2)</td>
</tr>
<tr>
    <td><CopyableCode code="started_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the scan was started, in RFC 3339 format. (example: 2026-04-13T23:59:59Z)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the scan. (in_progress, completed)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

The request was successful.

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
    <td><CopyableCode code="scan_id" /></td>
    <td><code>string</code></td>
    <td>An opaque identifier for the scan. (example: d5e94e48-504f-4a7f-a8c4-e0dc2e05e5f2)</td>
</tr>
<tr>
    <td><CopyableCode code="started_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the scan was started, in RFC 3339 format. (example: 2026-04-13T23:59:59Z)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the scan. (in_progress, completed)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Returns the most recent on-demand scans for the account or zone, up to a maximum of 5. Each scan includes its ID, start time, and current status. This includes both account or zone-wide and zone-scoped scans.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Returns the most recent on-demand scans for the account or zone, up to a maximum of 5. Each scan includes its ID, start time, and current status. This includes both account or zone-wide and zone-scoped scans.</td>
</tr>
<tr>
    <td><a href="#post_accounts_account_id_security_center_insights_scans"><CopyableCode code="post_accounts_account_id_security_center_insights_scans" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Initiates an on-demand security scan for the entire account or zone, scanning all zones associated with the account or zone. Rate limited to 5 scans per account or zone per 24-hour window.</td>
</tr>
<tr>
    <td><a href="#post_zones_zone_id_security_center_insights_scans"><CopyableCode code="post_zones_zone_id_security_center_insights_scans" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Initiates an on-demand security scan for the entire account or zone, scanning all zones associated with the account or zone. Rate limited to 5 scans per account or zone per 24-hour window.</td>
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

Returns the most recent on-demand scans for the account or zone, up to a maximum of 5. Each scan includes its ID, start time, and current status. This includes both account or zone-wide and zone-scoped scans.

```sql
SELECT
scan_id,
started_at,
status
FROM cloudflare.security_center.scans
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Returns the most recent on-demand scans for the account or zone, up to a maximum of 5. Each scan includes its ID, start time, and current status. This includes both account or zone-wide and zone-scoped scans.

```sql
SELECT
scan_id,
started_at,
status
FROM cloudflare.security_center.scans
WHERE zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_accounts_account_id_security_center_insights_scans"
    values={[
        { label: 'post_accounts_account_id_security_center_insights_scans', value: 'post_accounts_account_id_security_center_insights_scans' },
        { label: 'post_zones_zone_id_security_center_insights_scans', value: 'post_zones_zone_id_security_center_insights_scans' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_accounts_account_id_security_center_insights_scans">

Initiates an on-demand security scan for the entire account or zone, scanning all zones associated with the account or zone. Rate limited to 5 scans per account or zone per 24-hour window.

```sql
INSERT INTO cloudflare.security_center.scans (
issue_type,
issue_class,
account_id
)
SELECT 
'{{ issue_type }}',
'{{ issue_class }}',
'{{ account_id }}'
RETURNING
errors,
messages,
result,
success
;
```
</TabItem>
<TabItem value="post_zones_zone_id_security_center_insights_scans">

Initiates an on-demand security scan for the entire account or zone, scanning all zones associated with the account or zone. Rate limited to 5 scans per account or zone per 24-hour window.

```sql
INSERT INTO cloudflare.security_center.scans (
issue_type,
issue_class,
zone_id
)
SELECT 
'{{ issue_type }}',
'{{ issue_class }}',
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
- name: scans
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the scans resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the scans resource.
    - name: issue_type
      value: "{{ issue_type }}"
      valid_values: ['compliance_violation', 'email_security', 'exposed_infrastructure', 'insecure_configuration', 'weak_authentication', 'configuration_suggestion']
    - name: issue_class
      value: "{{ issue_class }}"
`}</CodeBlock>

</TabItem>
</Tabs>
