--- 
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - alerting
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.alerting.policies" /></td></tr>
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

Get a Notification policy response

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
    <td>The unique identifier of a notification policy (example: 0da2b59ef118439d8097bdfb215203c9)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the policy. (example: SSL Notification Event Policy)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_interval" /></td>
    <td><code>string</code></td>
    <td>Optional specification of how often to re-alert from the same incident, not support on all alert types. (example: 30m)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_type" /></td>
    <td><code>string</code></td>
    <td>Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which then will give you a list of possible values. (abuse_report_alert, access_custom_certificate_expiration_type, advanced_ddos_attack_l4_alert, advanced_ddos_attack_l7_alert, advanced_http_alert_error, bgp_hijack_notification, billing_usage_alert, block_notification_block_removed, block_notification_new_block, block_notification_review_rejected, bot_traffic_basic_alert, brand_protection_alert, brand_protection_digest, clickhouse_alert_fw_anomaly, clickhouse_alert_fw_ent_anomaly, cloudforce_one_request_notification, cni_maintenance_notification, custom_analytics, custom_bot_detection_alert, custom_ssl_certificate_event_type, dedicated_ssl_certificate_event_type, device_connectivity_anomaly_alert, dos_attack_l4, dos_attack_l7, expiring_service_token_alert, failing_logpush_job_disabled_alert, fbm_auto_advertisement, fbm_dosd_attack, fbm_volumetric_attack, health_check_status_notification, hostname_aop_custom_certificate_expiration_type, http_alert_edge_error, http_alert_origin_error, image_notification, image_resizing_notification, incident_alert, load_balancing_health_alert, load_balancing_pool_enablement_alert, logo_match_alert, magic_tunnel_health_check_event, magic_wan_tunnel_health, maintenance_event_notification, mtls_certificate_store_certificate_expiration_type, pages_event_alert, radar_notification, real_origin_monitoring, scriptmonitor_alert_new_code_change_detections, scriptmonitor_alert_new_hosts, scriptmonitor_alert_new_malicious_hosts, scriptmonitor_alert_new_malicious_scripts, scriptmonitor_alert_new_malicious_url, scriptmonitor_alert_new_max_length_resource_url, scriptmonitor_alert_new_resources, secondary_dns_all_primaries_failing, secondary_dns_primaries_failing, secondary_dns_warning, secondary_dns_zone_successfully_updated, secondary_dns_zone_validation_warning, security_insights_alert, sentinel_alert, stream_live_notifications, synthetic_test_latency_alert, synthetic_test_low_availability_alert, traffic_anomalies_alert, tunnel_health_event, tunnel_update_event, universal_ssl_event_type, web_analytics_metrics_update, zone_aop_custom_certificate_expiration_type) (example: universal_ssl_event_type)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Optional description for the Notification policy. (example: Something describing the policy.)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the Notification policy is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria. This is only available for select alert types. See alert type documentation for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="mechanisms" /></td>
    <td><code>object</code></td>
    <td>List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Notification policies response

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
    <td>The unique identifier of a notification policy (example: 0da2b59ef118439d8097bdfb215203c9)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the policy. (example: SSL Notification Event Policy)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_interval" /></td>
    <td><code>string</code></td>
    <td>Optional specification of how often to re-alert from the same incident, not support on all alert types. (example: 30m)</td>
</tr>
<tr>
    <td><CopyableCode code="alert_type" /></td>
    <td><code>string</code></td>
    <td>Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which then will give you a list of possible values. (abuse_report_alert, access_custom_certificate_expiration_type, advanced_ddos_attack_l4_alert, advanced_ddos_attack_l7_alert, advanced_http_alert_error, bgp_hijack_notification, billing_usage_alert, block_notification_block_removed, block_notification_new_block, block_notification_review_rejected, bot_traffic_basic_alert, brand_protection_alert, brand_protection_digest, clickhouse_alert_fw_anomaly, clickhouse_alert_fw_ent_anomaly, cloudforce_one_request_notification, cni_maintenance_notification, custom_analytics, custom_bot_detection_alert, custom_ssl_certificate_event_type, dedicated_ssl_certificate_event_type, device_connectivity_anomaly_alert, dos_attack_l4, dos_attack_l7, expiring_service_token_alert, failing_logpush_job_disabled_alert, fbm_auto_advertisement, fbm_dosd_attack, fbm_volumetric_attack, health_check_status_notification, hostname_aop_custom_certificate_expiration_type, http_alert_edge_error, http_alert_origin_error, image_notification, image_resizing_notification, incident_alert, load_balancing_health_alert, load_balancing_pool_enablement_alert, logo_match_alert, magic_tunnel_health_check_event, magic_wan_tunnel_health, maintenance_event_notification, mtls_certificate_store_certificate_expiration_type, pages_event_alert, radar_notification, real_origin_monitoring, scriptmonitor_alert_new_code_change_detections, scriptmonitor_alert_new_hosts, scriptmonitor_alert_new_malicious_hosts, scriptmonitor_alert_new_malicious_scripts, scriptmonitor_alert_new_malicious_url, scriptmonitor_alert_new_max_length_resource_url, scriptmonitor_alert_new_resources, secondary_dns_all_primaries_failing, secondary_dns_primaries_failing, secondary_dns_warning, secondary_dns_zone_successfully_updated, secondary_dns_zone_validation_warning, security_insights_alert, sentinel_alert, stream_live_notifications, synthetic_test_latency_alert, synthetic_test_low_availability_alert, traffic_anomalies_alert, tunnel_health_event, tunnel_update_event, universal_ssl_event_type, web_analytics_metrics_update, zone_aop_custom_certificate_expiration_type) (example: universal_ssl_event_type)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Optional description for the Notification policy. (example: Something describing the policy.)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the Notification policy is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="filters" /></td>
    <td><code>object</code></td>
    <td>Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria. This is only available for select alert types. See alert type documentation for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="mechanisms" /></td>
    <td><code>object</code></td>
    <td>List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.</td>
</tr>
<tr>
    <td><CopyableCode code="modified" /></td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Get details for a single policy.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Get a list of all Notification policies.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-alert_type"><code>alert_type</code></a>, <a href="#parameter-enabled"><code>enabled</code></a>, <a href="#parameter-mechanisms"><code>mechanisms</code></a></td>
    <td></td>
    <td>Creates a new Notification policy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Update a Notification policy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-policy_id"><code>policy_id</code></a></td>
    <td></td>
    <td>Delete a Notification policy.</td>
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
<tr id="parameter-policy_id">
    <td><CopyableCode code="policy_id" /></td>
    <td><code>string</code></td>
    <td>The Access policy ID.</td>
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

Get details for a single policy.

```sql
SELECT
id,
name,
alert_interval,
alert_type,
created,
description,
enabled,
filters,
mechanisms,
modified
FROM cloudflare.alerting.policies
WHERE account_id = '{{ account_id }}' -- required
AND policy_id = '{{ policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all Notification policies.

```sql
SELECT
id,
name,
alert_interval,
alert_type,
created,
description,
enabled,
filters,
mechanisms,
modified
FROM cloudflare.alerting.policies
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

Creates a new Notification policy.

```sql
INSERT INTO cloudflare.alerting.policies (
alert_interval,
alert_type,
description,
enabled,
filters,
mechanisms,
name,
account_id
)
SELECT 
'{{ alert_interval }}',
'{{ alert_type }}' /* required */,
'{{ description }}',
{{ enabled }} /* required */,
'{{ filters }}',
'{{ mechanisms }}' /* required */,
'{{ name }}' /* required */,
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
- name: policies
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the policies resource.
    - name: alert_interval
      value: "{{ alert_interval }}"
      description: |
        Optional specification of how often to re-alert from the same incident, not support on all alert types.
    - name: alert_type
      value: "{{ alert_type }}"
      description: |
        Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which then will give you a list of possible values.
      valid_values: ['abuse_report_alert', 'access_custom_certificate_expiration_type', 'advanced_ddos_attack_l4_alert', 'advanced_ddos_attack_l7_alert', 'advanced_http_alert_error', 'bgp_hijack_notification', 'billing_usage_alert', 'block_notification_block_removed', 'block_notification_new_block', 'block_notification_review_rejected', 'bot_traffic_basic_alert', 'brand_protection_alert', 'brand_protection_digest', 'clickhouse_alert_fw_anomaly', 'clickhouse_alert_fw_ent_anomaly', 'cloudforce_one_request_notification', 'cni_maintenance_notification', 'custom_analytics', 'custom_bot_detection_alert', 'custom_ssl_certificate_event_type', 'dedicated_ssl_certificate_event_type', 'device_connectivity_anomaly_alert', 'dos_attack_l4', 'dos_attack_l7', 'expiring_service_token_alert', 'failing_logpush_job_disabled_alert', 'fbm_auto_advertisement', 'fbm_dosd_attack', 'fbm_volumetric_attack', 'health_check_status_notification', 'hostname_aop_custom_certificate_expiration_type', 'http_alert_edge_error', 'http_alert_origin_error', 'image_notification', 'image_resizing_notification', 'incident_alert', 'load_balancing_health_alert', 'load_balancing_pool_enablement_alert', 'logo_match_alert', 'magic_tunnel_health_check_event', 'magic_wan_tunnel_health', 'maintenance_event_notification', 'mtls_certificate_store_certificate_expiration_type', 'pages_event_alert', 'radar_notification', 'real_origin_monitoring', 'scriptmonitor_alert_new_code_change_detections', 'scriptmonitor_alert_new_hosts', 'scriptmonitor_alert_new_malicious_hosts', 'scriptmonitor_alert_new_malicious_scripts', 'scriptmonitor_alert_new_malicious_url', 'scriptmonitor_alert_new_max_length_resource_url', 'scriptmonitor_alert_new_resources', 'secondary_dns_all_primaries_failing', 'secondary_dns_primaries_failing', 'secondary_dns_warning', 'secondary_dns_zone_successfully_updated', 'secondary_dns_zone_validation_warning', 'security_insights_alert', 'sentinel_alert', 'stream_live_notifications', 'synthetic_test_latency_alert', 'synthetic_test_low_availability_alert', 'traffic_anomalies_alert', 'tunnel_health_event', 'tunnel_update_event', 'universal_ssl_event_type', 'web_analytics_metrics_update', 'zone_aop_custom_certificate_expiration_type']
    - name: description
      value: "{{ description }}"
      description: |
        Optional description for the Notification policy.
    - name: enabled
      value: {{ enabled }}
      description: |
        Whether or not the Notification policy is enabled.
      default: true
    - name: filters
      description: |
        Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria. This is only available for select alert types. See alert type documentation for more details.
      value:
        actions:
          - "{{ actions }}"
        affected_asns:
          - "{{ affected_asns }}"
        affected_components:
          - "{{ affected_components }}"
        affected_locations:
          - "{{ affected_locations }}"
        airport_code:
          - "{{ airport_code }}"
        alert_trigger_preferences:
          - "{{ alert_trigger_preferences }}"
        alert_trigger_preferences_value:
          - "{{ alert_trigger_preferences_value }}"
        enabled:
          - "{{ enabled }}"
        environment:
          - "{{ environment }}"
        event:
          - "{{ event }}"
        event_source:
          - "{{ event_source }}"
        event_type:
          - "{{ event_type }}"
        group_by:
          - "{{ group_by }}"
        health_check_id:
          - "{{ health_check_id }}"
        incident_impact:
          - "{{ incident_impact }}"
        input_id:
          - "{{ input_id }}"
        insight_class:
          - "{{ insight_class }}"
        limit:
          - "{{ limit }}"
        logo_tag:
          - "{{ logo_tag }}"
        megabits_per_second:
          - "{{ megabits_per_second }}"
        new_health:
          - "{{ new_health }}"
        new_status:
          - "{{ new_status }}"
        packets_per_second:
          - "{{ packets_per_second }}"
        pool_id:
          - "{{ pool_id }}"
        pop_names:
          - "{{ pop_names }}"
        product:
          - "{{ product }}"
        project_id:
          - "{{ project_id }}"
        protocol:
          - "{{ protocol }}"
        query_tag:
          - "{{ query_tag }}"
        requests_per_second:
          - "{{ requests_per_second }}"
        selectors:
          - "{{ selectors }}"
        services:
          - "{{ services }}"
        slo:
          - "{{ slo }}"
        status:
          - "{{ status }}"
        target_hostname:
          - "{{ target_hostname }}"
        target_ip:
          - "{{ target_ip }}"
        target_zone_name:
          - "{{ target_zone_name }}"
        traffic_exclusions:
          - "{{ traffic_exclusions }}"
        tunnel_id:
          - "{{ tunnel_id }}"
        tunnel_name:
          - "{{ tunnel_name }}"
        type:
          - "{{ type }}"
        where:
          - "{{ where }}"
        zones:
          - "{{ zones }}"
    - name: mechanisms
      description: |
        List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
      value:
        email:
          - id: "{{ id }}"
        pagerduty:
          - id: "{{ id }}"
        webhooks:
          - id: "{{ id }}"
    - name: name
      value: "{{ name }}"
      description: |
        Name of the policy.
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

Update a Notification policy.

```sql
REPLACE cloudflare.alerting.policies
SET 
alert_interval = '{{ alert_interval }}',
alert_type = '{{ alert_type }}',
description = '{{ description }}',
enabled = {{ enabled }},
filters = '{{ filters }}',
mechanisms = '{{ mechanisms }}',
name = '{{ name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND policy_id = '{{ policy_id }}' --required
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

Delete a Notification policy.

```sql
DELETE FROM cloudflare.alerting.policies
WHERE account_id = '{{ account_id }}' --required
AND policy_id = '{{ policy_id }}' --required
;
```
</TabItem>
</Tabs>
