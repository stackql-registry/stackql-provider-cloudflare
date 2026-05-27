--- 
title: posture
hide_title: false
hide_table_of_contents: false
keywords:
  - posture
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

Creates, updates, deletes, gets or lists a <code>posture</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="posture" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.zero_trust.posture" /></td></tr>
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

Get device posture rule details response.

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
    <td>API UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the device posture rule. (example: Admin Serial Numbers)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the device posture rule. (example: The rule for admin serial numbers)</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client. (example: 1h)</td>
</tr>
<tr>
    <td><CopyableCode code="input" /></td>
    <td><code>object</code></td>
    <td>The value to be checked against. (title: File Check)</td>
</tr>
<tr>
    <td><CopyableCode code="match" /></td>
    <td><code>array</code></td>
    <td>The conditions that the client must match to run the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>string</code></td>
    <td>Polling frequency for the WARP client posture check. Default: `5m` (poll every five minutes). Minimum: `1m`. (example: 1h)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of device posture rule. (file, application, tanium, gateway, warp, disk_encryption, serial_number, sentinelone, carbonblack, firewall, os_version, domain_joined, client_certificate, client_certificate_v2, antivirus, unique_client_id, kolide, tanium_s2s, crowdstrike_s2s, intune, workspace_one, sentinelone_s2s, custom_s2s) (example: file)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List device posture rules response.

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
    <td>API UUID. (example: f174e90a-fafe-4643-bbbc-4a0ed4fc8415)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the device posture rule. (example: Admin Serial Numbers)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the device posture rule. (example: The rule for admin serial numbers)</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code>string</code></td>
    <td>Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client. (example: 1h)</td>
</tr>
<tr>
    <td><CopyableCode code="input" /></td>
    <td><code>object</code></td>
    <td>The value to be checked against. (title: File Check)</td>
</tr>
<tr>
    <td><CopyableCode code="match" /></td>
    <td><code>array</code></td>
    <td>The conditions that the client must match to run the rule.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>string</code></td>
    <td>Polling frequency for the WARP client posture check. Default: `5m` (poll every five minutes). Minimum: `1m`. (example: 1h)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of device posture rule. (file, application, tanium, gateway, warp, disk_encryption, serial_number, sentinelone, carbonblack, firewall, os_version, domain_joined, client_certificate, client_certificate_v2, antivirus, unique_client_id, kolide, tanium_s2s, crowdstrike_s2s, intune, workspace_one, sentinelone_s2s, custom_s2s) (example: file)</td>
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
    <td>Fetches a single device posture rule.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Fetches device posture rules for a Zero Trust account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Creates a new device posture rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Updates a device posture rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a device posture rule.</td>
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

Fetches a single device posture rule.

```sql
SELECT
id,
name,
description,
expiration,
input,
match,
schedule,
type
FROM cloudflare.zero_trust.posture
WHERE rule_id = '{{ rule_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Fetches device posture rules for a Zero Trust account.

```sql
SELECT
id,
name,
description,
expiration,
input,
match,
schedule,
type
FROM cloudflare.zero_trust.posture
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

Creates a new device posture rule.

```sql
INSERT INTO cloudflare.zero_trust.posture (
description,
expiration,
input,
match,
name,
schedule,
type,
account_id
)
SELECT 
'{{ description }}',
'{{ expiration }}',
'{{ input }}',
'{{ match }}',
'{{ name }}' /* required */,
'{{ schedule }}',
'{{ type }}' /* required */,
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
- name: posture
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the posture resource.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the device posture rule.
    - name: expiration
      value: "{{ expiration }}"
      description: |
        Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client.
    - name: input
      description: |
        The value to be checked against.
      value:
        exists: {{ exists }}
        operating_system: "{{ operating_system }}"
        path: "{{ path }}"
        sha256: "{{ sha256 }}"
        thumbprint: "{{ thumbprint }}"
        id: "{{ id }}"
        domain: "{{ domain }}"
        operator: "{{ operator }}"
        os_distro_name: "{{ os_distro_name }}"
        os_distro_revision: "{{ os_distro_revision }}"
        os_version_extra: "{{ os_version_extra }}"
        version: "{{ version }}"
        enabled: {{ enabled }}
        checkDisks:
          - "{{ checkDisks }}"
        requireAll: {{ requireAll }}
        certificate_id: "{{ certificate_id }}"
        cn: "{{ cn }}"
        check_private_key: {{ check_private_key }}
        extended_key_usage:
          - "{{ extended_key_usage }}"
        locations:
          paths:
            - "{{ paths }}"
          trust_stores:
            - "{{ trust_stores }}"
        subject_alternative_names:
          - "{{ subject_alternative_names }}"
        update_window_days: {{ update_window_days }}
        compliance_status: "{{ compliance_status }}"
        connection_id: "{{ connection_id }}"
        last_seen: "{{ last_seen }}"
        os: "{{ os }}"
        overall: "{{ overall }}"
        sensor_config: "{{ sensor_config }}"
        state: "{{ state }}"
        versionOperator: "{{ versionOperator }}"
        countOperator: "{{ countOperator }}"
        issue_count: "{{ issue_count }}"
        eid_last_seen: "{{ eid_last_seen }}"
        risk_level: "{{ risk_level }}"
        scoreOperator: "{{ scoreOperator }}"
        total_score: {{ total_score }}
        active_threats: {{ active_threats }}
        infected: {{ infected }}
        is_active: {{ is_active }}
        network_status: "{{ network_status }}"
        operational_state: "{{ operational_state }}"
        score: {{ score }}
    - name: match
      description: |
        The conditions that the client must match to run the rule.
      value:
        - platform: "{{ platform }}"
    - name: name
      value: "{{ name }}"
      description: |
        The name of the device posture rule.
    - name: schedule
      value: "{{ schedule }}"
      description: |
        Polling frequency for the WARP client posture check. Default: \`5m\` (poll every five minutes). Minimum: \`1m\`.
    - name: type
      value: "{{ type }}"
      description: |
        The type of device posture rule.
      valid_values: ['file', 'application', 'tanium', 'gateway', 'warp', 'disk_encryption', 'serial_number', 'sentinelone', 'carbonblack', 'firewall', 'os_version', 'domain_joined', 'client_certificate', 'client_certificate_v2', 'antivirus', 'unique_client_id', 'kolide', 'tanium_s2s', 'crowdstrike_s2s', 'intune', 'workspace_one', 'sentinelone_s2s', 'custom_s2s']
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

Updates a device posture rule.

```sql
REPLACE cloudflare.zero_trust.posture
SET 
description = '{{ description }}',
expiration = '{{ expiration }}',
input = '{{ input }}',
match = '{{ match }}',
name = '{{ name }}',
schedule = '{{ schedule }}',
type = '{{ type }}'
WHERE 
rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
AND name = '{{ name }}' --required
AND type = '{{ type }}' --required
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

Deletes a device posture rule.

```sql
DELETE FROM cloudflare.zero_trust.posture
WHERE rule_id = '{{ rule_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
