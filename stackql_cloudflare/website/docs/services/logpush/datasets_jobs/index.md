--- 
title: datasets_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets_jobs
  - logpush
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

Creates, updates, deletes, gets or lists a <code>datasets_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="datasets_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logpush.datasets_jobs" /></td></tr>
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

List Logpush jobs for a dataset response.

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
    <td><code>integer</code></td>
    <td>Unique id of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Optional human readable job name. Not unique. Cloudflare suggests. that you set this to a meaningful string, like the domain name, to make it easier to identify your job. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>string</code></td>
    <td>Name of the dataset. A list of supported datasets can be found on the [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/). (access_requests, audit_logs, audit_logs_v2, biso_user_actions, casb_findings, device_posture_results, dex_application_tests, dex_device_state_events, dlp_forensic_copies, dns_firewall_logs, dns_logs, email_security_alerts, email_security_post_delivery_events, firewall_events, gateway_dns, gateway_http, gateway_network, http_requests, ipsec_logs, magic_ids_detections, mcp_portal_logs, nel_reports, network_analytics_logs, page_shield_events, sinkhole_http_logs, spectrum_events, ssh_logs, warp_config_changes, warp_toggle_changes, workers_trace_events, zaraz_events, zero_trust_network_sessions) (default: http_requests, example: http_requests)</td>
</tr>
<tr>
    <td><CopyableCode code="destination_conf" /></td>
    <td><code>string (uri)</code></td>
    <td>Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included. (example: s3://mybucket/logs?region=us-west-2)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag that indicates if the job is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="error_message" /></td>
    <td><code>string</code></td>
    <td>If not null, the job is currently failing. Failures are usually. repetitive (example: no permissions to write to destination bucket). Only the last failure is recorded. On successful execution of a job the error_message and last_error are set to null.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>This field is deprecated. Please use `max_upload_*` parameters instead. . The frequency at which Cloudflare sends batches of logs to your destination. Setting frequency to high sends your logs in larger quantities of smaller files. Setting frequency to low sends logs in smaller quantities of larger files. (high, low) (default: high, example: high)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind parameter (optional) is used to differentiate between Logpush and Edge Log Delivery jobs (when supported by the dataset). (, edge) (default: , example: , x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="last_complete" /></td>
    <td><code>string (date-time)</code></td>
    <td>Records the last time for which logs have been successfully pushed. If the last successful push was for logs range 2018-07-23T10:00:00Z to 2018-07-23T10:01:00Z then the value of this field will be 2018-07-23T10:01:00Z. If the job has never run or has just been enabled and hasn't run yet then the field will be empty.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>string (date-time)</code></td>
    <td>Records the last time the job failed. If not null, the job is currently. failing. If null, the job has either never failed or has run successfully at least once since last failure. See also the error_message field.</td>
</tr>
<tr>
    <td><CopyableCode code="logpull_options" /></td>
    <td><code>string (uri-reference)</code></td>
    <td>This field is deprecated. Use `output_options` instead. Configuration string. It specifies things like requested fields and timestamp formats. If migrating from the logpull api, copy the url (full url or just the query string) of your call here, and logpush will keep on making this call for you, setting start and end times appropriately. (example: fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339)</td>
</tr>
<tr>
    <td><CopyableCode code="max_upload_bytes" /></td>
    <td><code>integer</code></td>
    <td>The maximum uncompressed file size of a batch of logs. This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size. (0)</td>
</tr>
<tr>
    <td><CopyableCode code="max_upload_interval_seconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum interval in seconds for log batches. This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify a minimum interval for log batches; this means that log files may be sent in shorter intervals than this. (0)</td>
</tr>
<tr>
    <td><CopyableCode code="max_upload_records" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of log lines per batch. This setting must be between 1000 and 1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this. (0)</td>
</tr>
<tr>
    <td><CopyableCode code="output_options" /></td>
    <td><code>object</code></td>
    <td>The structured replacement for `logpull_options`. When including this field, the `logpull_option` field will be ignored.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List Logpush jobs for a dataset response.

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
    <td><code>integer</code></td>
    <td>Unique id of the job.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Optional human readable job name. Not unique. Cloudflare suggests. that you set this to a meaningful string, like the domain name, to make it easier to identify your job. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>string</code></td>
    <td>Name of the dataset. A list of supported datasets can be found on the [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/). (access_requests, audit_logs, audit_logs_v2, biso_user_actions, casb_findings, device_posture_results, dex_application_tests, dex_device_state_events, dlp_forensic_copies, dns_firewall_logs, dns_logs, email_security_alerts, email_security_post_delivery_events, firewall_events, gateway_dns, gateway_http, gateway_network, http_requests, ipsec_logs, magic_ids_detections, mcp_portal_logs, nel_reports, network_analytics_logs, page_shield_events, sinkhole_http_logs, spectrum_events, ssh_logs, warp_config_changes, warp_toggle_changes, workers_trace_events, zaraz_events, zero_trust_network_sessions) (default: http_requests, example: http_requests)</td>
</tr>
<tr>
    <td><CopyableCode code="destination_conf" /></td>
    <td><code>string (uri)</code></td>
    <td>Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included. (example: s3://mybucket/logs?region=us-west-2)</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag that indicates if the job is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="error_message" /></td>
    <td><code>string</code></td>
    <td>If not null, the job is currently failing. Failures are usually. repetitive (example: no permissions to write to destination bucket). Only the last failure is recorded. On successful execution of a job the error_message and last_error are set to null.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>This field is deprecated. Please use `max_upload_*` parameters instead. . The frequency at which Cloudflare sends batches of logs to your destination. Setting frequency to high sends your logs in larger quantities of smaller files. Setting frequency to low sends logs in smaller quantities of larger files. (high, low) (default: high, example: high)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind parameter (optional) is used to differentiate between Logpush and Edge Log Delivery jobs (when supported by the dataset). (, edge) (default: , example: , x-stainless-terraform-configurability: computed_optional)</td>
</tr>
<tr>
    <td><CopyableCode code="last_complete" /></td>
    <td><code>string (date-time)</code></td>
    <td>Records the last time for which logs have been successfully pushed. If the last successful push was for logs range 2018-07-23T10:00:00Z to 2018-07-23T10:01:00Z then the value of this field will be 2018-07-23T10:01:00Z. If the job has never run or has just been enabled and hasn't run yet then the field will be empty.</td>
</tr>
<tr>
    <td><CopyableCode code="last_error" /></td>
    <td><code>string (date-time)</code></td>
    <td>Records the last time the job failed. If not null, the job is currently. failing. If null, the job has either never failed or has run successfully at least once since last failure. See also the error_message field.</td>
</tr>
<tr>
    <td><CopyableCode code="logpull_options" /></td>
    <td><code>string (uri-reference)</code></td>
    <td>This field is deprecated. Use `output_options` instead. Configuration string. It specifies things like requested fields and timestamp formats. If migrating from the logpull api, copy the url (full url or just the query string) of your call here, and logpush will keep on making this call for you, setting start and end times appropriately. (example: fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339)</td>
</tr>
<tr>
    <td><CopyableCode code="max_upload_bytes" /></td>
    <td><code>integer</code></td>
    <td>The maximum uncompressed file size of a batch of logs. This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size. (0)</td>
</tr>
<tr>
    <td><CopyableCode code="max_upload_interval_seconds" /></td>
    <td><code>integer</code></td>
    <td>The maximum interval in seconds for log batches. This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify a minimum interval for log batches; this means that log files may be sent in shorter intervals than this. (0)</td>
</tr>
<tr>
    <td><CopyableCode code="max_upload_records" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of log lines per batch. This setting must be between 1000 and 1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this. (0)</td>
</tr>
<tr>
    <td><CopyableCode code="output_options" /></td>
    <td><code>object</code></td>
    <td>The structured replacement for `logpull_options`. When including this field, the `logpull_option` field will be ignored.</td>
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
    <td><a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Lists Logpush jobs for an account or zone for a dataset.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-dataset_id"><code>dataset_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Lists Logpush jobs for an account or zone for a dataset.</td>
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
<tr id="parameter-dataset_id">
    <td><CopyableCode code="dataset_id" /></td>
    <td><code>string</code></td>
    <td>The dataset ID.</td>
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

Lists Logpush jobs for an account or zone for a dataset.

```sql
SELECT
id,
name,
dataset,
destination_conf,
enabled,
error_message,
frequency,
kind,
last_complete,
last_error,
logpull_options,
max_upload_bytes,
max_upload_interval_seconds,
max_upload_records,
output_options
FROM cloudflare.logpush.datasets_jobs
WHERE dataset_id = '{{ dataset_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Lists Logpush jobs for an account or zone for a dataset.

```sql
SELECT
id,
name,
dataset,
destination_conf,
enabled,
error_message,
frequency,
kind,
last_complete,
last_error,
logpull_options,
max_upload_bytes,
max_upload_interval_seconds,
max_upload_records,
output_options
FROM cloudflare.logpush.datasets_jobs
WHERE dataset_id = '{{ dataset_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
</Tabs>
