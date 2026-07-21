--- 
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.logpush.jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Get Logpush job details response.

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
<TabItem value="get_by_zone">

Get Logpush job details response.

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
    <td><a href="#get_by_account"><CopyableCode code="get_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets the details of a Logpush job.</td>
</tr>
<tr>
    <td><a href="#get_by_zone"><CopyableCode code="get_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Gets the details of a Logpush job.</td>
</tr>
<tr>
    <td><a href="#create_by_account"><CopyableCode code="create_by_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Creates a new Logpush job for an account or zone.</td>
</tr>
<tr>
    <td><a href="#create_by_zone"><CopyableCode code="create_by_zone" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Creates a new Logpush job for an account or zone.</td>
</tr>
<tr>
    <td><a href="#update_by_account"><CopyableCode code="update_by_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Updates a Logpush job.</td>
</tr>
<tr>
    <td><a href="#update_by_zone"><CopyableCode code="update_by_zone" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Updates a Logpush job.</td>
</tr>
<tr>
    <td><a href="#delete_by_account"><CopyableCode code="delete_by_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Deletes a Logpush job.</td>
</tr>
<tr>
    <td><a href="#delete_by_zone"><CopyableCode code="delete_by_zone" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes a Logpush job.</td>
</tr>
<tr>
    <td><a href="#get_ownership_challenge_by_account"><CopyableCode code="get_ownership_challenge_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Gets a new ownership challenge sent to your destination.</td>
</tr>
<tr>
    <td><a href="#get_ownership_challenge_by_zone"><CopyableCode code="get_ownership_challenge_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Gets a new ownership challenge sent to your destination.</td>
</tr>
<tr>
    <td><a href="#validate_ownership_challenge_by_account"><CopyableCode code="validate_ownership_challenge_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a>, <a href="#parameter-ownership_challenge"><code>ownership_challenge</code></a></td>
    <td></td>
    <td>Validates ownership challenge of the destination.</td>
</tr>
<tr>
    <td><a href="#validate_ownership_challenge_by_zone"><CopyableCode code="validate_ownership_challenge_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a>, <a href="#parameter-ownership_challenge"><code>ownership_challenge</code></a></td>
    <td></td>
    <td>Validates ownership challenge of the destination.</td>
</tr>
<tr>
    <td><a href="#validate_destination_by_account"><CopyableCode code="validate_destination_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Validates destination.</td>
</tr>
<tr>
    <td><a href="#validate_destination_by_zone"><CopyableCode code="validate_destination_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Validates destination.</td>
</tr>
<tr>
    <td><a href="#destination_exists_by_account"><CopyableCode code="destination_exists_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Checks if there is an existing job with a destination.</td>
</tr>
<tr>
    <td><a href="#destination_exists_by_zone"><CopyableCode code="destination_exists_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-destination_conf"><code>destination_conf</code></a></td>
    <td></td>
    <td>Checks if there is an existing job with a destination.</td>
</tr>
<tr>
    <td><a href="#validate_origin_by_account"><CopyableCode code="validate_origin_by_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-logpull_options"><code>logpull_options</code></a></td>
    <td></td>
    <td>Validates logpull origin with logpull_options.</td>
</tr>
<tr>
    <td><a href="#validate_origin_by_zone"><CopyableCode code="validate_origin_by_zone" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-logpull_options"><code>logpull_options</code></a></td>
    <td></td>
    <td>Validates logpull origin with logpull_options.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The job ID.</td>
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
    defaultValue="get_by_account"
    values={[
        { label: 'get_by_account', value: 'get_by_account' },
        { label: 'get_by_zone', value: 'get_by_zone' }
    ]}
>
<TabItem value="get_by_account">

Gets the details of a Logpush job.

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
FROM cloudflare.logpush.jobs
WHERE job_id = '{{ job_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="get_by_zone">

Gets the details of a Logpush job.

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
FROM cloudflare.logpush.jobs
WHERE job_id = '{{ job_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
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

Creates a new Logpush job for an account or zone.

```sql
INSERT INTO cloudflare.logpush.jobs (
dataset,
destination_conf,
enabled,
filter,
frequency,
kind,
logpull_options,
max_upload_bytes,
max_upload_interval_seconds,
max_upload_records,
name,
output_options,
ownership_challenge,
account_id
)
SELECT 
'{{ dataset }}',
'{{ destination_conf }}' /* required */,
{{ enabled }},
'{{ filter }}',
'{{ frequency }}',
'{{ kind }}',
'{{ logpull_options }}',
{{ max_upload_bytes }},
{{ max_upload_interval_seconds }},
{{ max_upload_records }},
'{{ name }}',
'{{ output_options }}',
'{{ ownership_challenge }}',
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

Creates a new Logpush job for an account or zone.

```sql
INSERT INTO cloudflare.logpush.jobs (
dataset,
destination_conf,
enabled,
filter,
frequency,
kind,
logpull_options,
max_upload_bytes,
max_upload_interval_seconds,
max_upload_records,
name,
output_options,
ownership_challenge,
zone_id
)
SELECT 
'{{ dataset }}',
'{{ destination_conf }}' /* required */,
{{ enabled }},
'{{ filter }}',
'{{ frequency }}',
'{{ kind }}',
'{{ logpull_options }}',
{{ max_upload_bytes }},
{{ max_upload_interval_seconds }},
{{ max_upload_records }},
'{{ name }}',
'{{ output_options }}',
'{{ ownership_challenge }}',
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
- name: jobs
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the jobs resource.
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the jobs resource.
    - name: dataset
      value: "{{ dataset }}"
      description: |
        Name of the dataset. A list of supported datasets can be found on the [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/).
      valid_values: ['access_requests', 'audit_logs', 'audit_logs_v2', 'biso_user_actions', 'casb_findings', 'device_posture_results', 'dex_application_tests', 'dex_device_state_events', 'dlp_forensic_copies', 'dns_firewall_logs', 'dns_logs', 'email_security_alerts', 'email_security_post_delivery_events', 'firewall_events', 'gateway_dns', 'gateway_http', 'gateway_network', 'http_requests', 'ipsec_logs', 'magic_ids_detections', 'mcp_portal_logs', 'nel_reports', 'network_analytics_logs', 'page_shield_events', 'sinkhole_http_logs', 'spectrum_events', 'ssh_logs', 'warp_config_changes', 'warp_toggle_changes', 'workers_trace_events', 'zaraz_events', 'zero_trust_network_sessions']
      default: http_requests
    - name: destination_conf
      value: "{{ destination_conf }}"
      description: |
        Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.
    - name: enabled
      value: {{ enabled }}
      description: |
        Flag that indicates if the job is enabled.
      default: false
    - name: filter
      value: "{{ filter }}"
      description: |
        The filters to select the events to include and/or remove from your logs. For more information, refer to [Filters](https://developers.cloudflare.com/logs/reference/filters/).
    - name: frequency
      value: "{{ frequency }}"
      description: |
        This field is deprecated. Please use \`max_upload_*\` parameters instead. . The frequency at which Cloudflare sends batches of logs to your destination. Setting frequency to high sends your logs in larger quantities of smaller files. Setting frequency to low sends logs in smaller quantities of larger files.
      valid_values: ['high', 'low']
      default: high
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind parameter (optional) is used to differentiate between Logpush and Edge Log Delivery jobs (when supported by the dataset).
      valid_values: ['', 'edge']
      default: 
    - name: logpull_options
      value: "{{ logpull_options }}"
      description: |
        This field is deprecated. Use \`output_options\` instead. Configuration string. It specifies things like requested fields and timestamp formats. If migrating from the logpull api, copy the url (full url or just the query string) of your call here, and logpush will keep on making this call for you, setting start and end times appropriately.
    - name: max_upload_bytes
      value: {{ max_upload_bytes }}
      description: |
        The maximum uncompressed file size of a batch of logs. This setting value must be between \`5 MB\` and \`1 GB\`, or \`0\` to disable it. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size.
      valid_values: ['0']
    - name: max_upload_interval_seconds
      value: {{ max_upload_interval_seconds }}
      description: |
        The maximum interval in seconds for log batches. This setting must be between 30 and 300 seconds (5 minutes), or \`0\` to disable it. Note that you cannot specify a minimum interval for log batches; this means that log files may be sent in shorter intervals than this.
      valid_values: ['0']
    - name: max_upload_records
      value: {{ max_upload_records }}
      description: |
        The maximum number of log lines per batch. This setting must be between 1000 and 1,000,000 lines, or \`0\` to disable it. Note that you cannot specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this.
      valid_values: ['0']
    - name: name
      value: "{{ name }}"
      description: |
        Optional human readable job name. Not unique. Cloudflare suggests. that you set this to a meaningful string, like the domain name, to make it easier to identify your job.
    - name: output_options
      description: |
        The structured replacement for \`logpull_options\`. When including this field, the \`logpull_option\` field will be ignored.
      value:
        CVE-2021-44228: {{ CVE-2021-44228 }}
        batch_prefix: "{{ batch_prefix }}"
        batch_suffix: "{{ batch_suffix }}"
        field_delimiter: "{{ field_delimiter }}"
        field_names:
          - "{{ field_names }}"
        merge_subrequests: {{ merge_subrequests }}
        output_type: "{{ output_type }}"
        record_delimiter: "{{ record_delimiter }}"
        record_prefix: "{{ record_prefix }}"
        record_suffix: "{{ record_suffix }}"
        record_template: "{{ record_template }}"
        sample_rate: {{ sample_rate }}
        timestamp_format: "{{ timestamp_format }}"
    - name: ownership_challenge
      value: "{{ ownership_challenge }}"
      description: |
        Ownership challenge token to prove destination ownership.
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

Updates a Logpush job.

```sql
REPLACE cloudflare.logpush.jobs
SET 
destination_conf = '{{ destination_conf }}',
enabled = {{ enabled }},
filter = '{{ filter }}',
frequency = '{{ frequency }}',
kind = '{{ kind }}',
logpull_options = '{{ logpull_options }}',
max_upload_bytes = {{ max_upload_bytes }},
max_upload_interval_seconds = {{ max_upload_interval_seconds }},
max_upload_records = {{ max_upload_records }},
name = '{{ name }}',
output_options = '{{ output_options }}',
ownership_challenge = '{{ ownership_challenge }}'
WHERE 
job_id = '{{ job_id }}' --required
AND account_id = '{{ account_id }}' --required
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
<TabItem value="update_by_zone">

Updates a Logpush job.

```sql
REPLACE cloudflare.logpush.jobs
SET 
destination_conf = '{{ destination_conf }}',
enabled = {{ enabled }},
filter = '{{ filter }}',
frequency = '{{ frequency }}',
kind = '{{ kind }}',
logpull_options = '{{ logpull_options }}',
max_upload_bytes = {{ max_upload_bytes }},
max_upload_interval_seconds = {{ max_upload_interval_seconds }},
max_upload_records = {{ max_upload_records }},
name = '{{ name }}',
output_options = '{{ output_options }}',
ownership_challenge = '{{ ownership_challenge }}'
WHERE 
job_id = '{{ job_id }}' --required
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

Deletes a Logpush job.

```sql
DELETE FROM cloudflare.logpush.jobs
WHERE job_id = '{{ job_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
<TabItem value="delete_by_zone">

Deletes a Logpush job.

```sql
DELETE FROM cloudflare.logpush.jobs
WHERE job_id = '{{ job_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_ownership_challenge_by_account"
    values={[
        { label: 'get_ownership_challenge_by_account', value: 'get_ownership_challenge_by_account' },
        { label: 'get_ownership_challenge_by_zone', value: 'get_ownership_challenge_by_zone' },
        { label: 'validate_ownership_challenge_by_account', value: 'validate_ownership_challenge_by_account' },
        { label: 'validate_ownership_challenge_by_zone', value: 'validate_ownership_challenge_by_zone' },
        { label: 'validate_destination_by_account', value: 'validate_destination_by_account' },
        { label: 'validate_destination_by_zone', value: 'validate_destination_by_zone' },
        { label: 'destination_exists_by_account', value: 'destination_exists_by_account' },
        { label: 'destination_exists_by_zone', value: 'destination_exists_by_zone' },
        { label: 'validate_origin_by_account', value: 'validate_origin_by_account' },
        { label: 'validate_origin_by_zone', value: 'validate_origin_by_zone' }
    ]}
>
<TabItem value="get_ownership_challenge_by_account">

Gets a new ownership challenge sent to your destination.

```sql
EXEC cloudflare.logpush.jobs.get_ownership_challenge_by_account 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="get_ownership_challenge_by_zone">

Gets a new ownership challenge sent to your destination.

```sql
EXEC cloudflare.logpush.jobs.get_ownership_challenge_by_zone 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="validate_ownership_challenge_by_account">

Validates ownership challenge of the destination.

```sql
EXEC cloudflare.logpush.jobs.validate_ownership_challenge_by_account 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}", 
"ownership_challenge": "{{ ownership_challenge }}"
}'
;
```
</TabItem>
<TabItem value="validate_ownership_challenge_by_zone">

Validates ownership challenge of the destination.

```sql
EXEC cloudflare.logpush.jobs.validate_ownership_challenge_by_zone 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}", 
"ownership_challenge": "{{ ownership_challenge }}"
}'
;
```
</TabItem>
<TabItem value="validate_destination_by_account">

Validates destination.

```sql
EXEC cloudflare.logpush.jobs.validate_destination_by_account 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="validate_destination_by_zone">

Validates destination.

```sql
EXEC cloudflare.logpush.jobs.validate_destination_by_zone 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="destination_exists_by_account">

Checks if there is an existing job with a destination.

```sql
EXEC cloudflare.logpush.jobs.destination_exists_by_account 
@account_id='{{ account_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="destination_exists_by_zone">

Checks if there is an existing job with a destination.

```sql
EXEC cloudflare.logpush.jobs.destination_exists_by_zone 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"destination_conf": "{{ destination_conf }}"
}'
;
```
</TabItem>
<TabItem value="validate_origin_by_account">

Validates logpull origin with logpull_options.

```sql
EXEC cloudflare.logpush.jobs.validate_origin_by_account 
@account_id='{{ account_id }}' --required 
@@json=
'{
"logpull_options": "{{ logpull_options }}"
}'
;
```
</TabItem>
<TabItem value="validate_origin_by_zone">

Validates logpull origin with logpull_options.

```sql
EXEC cloudflare.logpush.jobs.validate_origin_by_zone 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"logpull_options": "{{ logpull_options }}"
}'
;
```
</TabItem>
</Tabs>
