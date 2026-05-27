--- 
title: healthchecks
hide_title: false
hide_table_of_contents: false
keywords:
  - healthchecks
  - healthchecks
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

Creates, updates, deletes, gets or lists a <code>healthchecks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="healthchecks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.healthchecks.healthchecks" /></td></tr>
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

Health Check Details response.

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed. (example: server-1)</td>
</tr>
<tr>
    <td><CopyableCode code="address" /></td>
    <td><code>string</code></td>
    <td>The hostname or IP address of the origin server to run health checks on. (example: www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="check_regions" /></td>
    <td><code>array</code></td>
    <td>A list of regions from which to run health checks. Null means Cloudflare will pick a default region.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_fails" /></td>
    <td><code>integer</code></td>
    <td>The number of consecutive fails required from a health check before changing the health to unhealthy.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_successes" /></td>
    <td><code>integer</code></td>
    <td>The number of consecutive successes required from a health check before changing the health to healthy.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the health check. (example: Health check for www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="failure_reason" /></td>
    <td><code>string</code></td>
    <td>The current failure reason if status is unhealthy. (example: )</td>
</tr>
<tr>
    <td><CopyableCode code="http_config" /></td>
    <td><code>object</code></td>
    <td>Parameters specific to an HTTP or HTTPS health check.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>integer</code></td>
    <td>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the origin server according to the health check. (unknown, healthy, unhealthy, suspended) (example: healthy)</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>If suspended, no health checks are sent to the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="tcp_config" /></td>
    <td><code>object</code></td>
    <td>Parameters specific to TCP health check.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout (in seconds) before marking the health check as failed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The protocol to use for the health check. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. (default: HTTP, example: HTTPS)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Health Checks response

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
    <td>Identifier (example: 023e105f4ecef8ad9ca31a8372d0c353)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed. (example: server-1)</td>
</tr>
<tr>
    <td><CopyableCode code="address" /></td>
    <td><code>string</code></td>
    <td>The hostname or IP address of the origin server to run health checks on. (example: www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="check_regions" /></td>
    <td><code>array</code></td>
    <td>A list of regions from which to run health checks. Null means Cloudflare will pick a default region.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_fails" /></td>
    <td><code>integer</code></td>
    <td>The number of consecutive fails required from a health check before changing the health to unhealthy.</td>
</tr>
<tr>
    <td><CopyableCode code="consecutive_successes" /></td>
    <td><code>integer</code></td>
    <td>The number of consecutive successes required from a health check before changing the health to healthy.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the health check. (example: Health check for www.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="failure_reason" /></td>
    <td><code>string</code></td>
    <td>The current failure reason if status is unhealthy. (example: )</td>
</tr>
<tr>
    <td><CopyableCode code="http_config" /></td>
    <td><code>object</code></td>
    <td>Parameters specific to an HTTP or HTTPS health check.</td>
</tr>
<tr>
    <td><CopyableCode code="interval" /></td>
    <td><code>integer</code></td>
    <td>The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="retries" /></td>
    <td><code>integer</code></td>
    <td>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the origin server according to the health check. (unknown, healthy, unhealthy, suspended) (example: healthy)</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>If suspended, no health checks are sent to the origin.</td>
</tr>
<tr>
    <td><CopyableCode code="tcp_config" /></td>
    <td><code>object</code></td>
    <td>Parameters specific to TCP health check.</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>The timeout (in seconds) before marking the health check as failed.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The protocol to use for the health check. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. (default: HTTP, example: HTTPS)</td>
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
    <td><a href="#parameter-healthcheck_id"><code>healthcheck_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetch a single configured health check.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>List configured health checks.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-address"><code>address</code></a></td>
    <td></td>
    <td>Create a new health check.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-healthcheck_id"><code>healthcheck_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-address"><code>address</code></a></td>
    <td></td>
    <td>Patch a configured health check.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-healthcheck_id"><code>healthcheck_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-address"><code>address</code></a></td>
    <td></td>
    <td>Update a configured health check.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-healthcheck_id"><code>healthcheck_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Delete a health check.</td>
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
<tr id="parameter-healthcheck_id">
    <td><CopyableCode code="healthcheck_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td>Page number of paginated results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Maximum number of results per page. Must be a multiple of 5.</td>
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

Fetch a single configured health check.

```sql
SELECT
id,
name,
address,
check_regions,
consecutive_fails,
consecutive_successes,
created_on,
description,
failure_reason,
http_config,
interval,
modified_on,
retries,
status,
suspended,
tcp_config,
timeout,
type
FROM cloudflare.healthchecks.healthchecks
WHERE healthcheck_id = '{{ healthcheck_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List configured health checks.

```sql
SELECT
id,
name,
address,
check_regions,
consecutive_fails,
consecutive_successes,
created_on,
description,
failure_reason,
http_config,
interval,
modified_on,
retries,
status,
suspended,
tcp_config,
timeout,
type
FROM cloudflare.healthchecks.healthchecks
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Create a new health check.

```sql
INSERT INTO cloudflare.healthchecks.healthchecks (
address,
check_regions,
consecutive_fails,
consecutive_successes,
description,
http_config,
interval,
name,
retries,
suspended,
tcp_config,
timeout,
type,
zone_id
)
SELECT 
'{{ address }}' /* required */,
'{{ check_regions }}',
{{ consecutive_fails }},
{{ consecutive_successes }},
'{{ description }}',
'{{ http_config }}',
{{ interval }},
'{{ name }}' /* required */,
{{ retries }},
{{ suspended }},
'{{ tcp_config }}',
{{ timeout }},
'{{ type }}',
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
- name: healthchecks
  props:
    - name: zone_id
      value: "{{ zone_id }}"
      description: Required parameter for the healthchecks resource.
    - name: address
      value: "{{ address }}"
      description: |
        The hostname or IP address of the origin server to run health checks on.
    - name: check_regions
      value:
        - "{{ check_regions }}"
      description: |
        A list of regions from which to run health checks. Null means Cloudflare will pick a default region.
    - name: consecutive_fails
      value: {{ consecutive_fails }}
      description: |
        The number of consecutive fails required from a health check before changing the health to unhealthy.
      default: 1
    - name: consecutive_successes
      value: {{ consecutive_successes }}
      description: |
        The number of consecutive successes required from a health check before changing the health to healthy.
      default: 1
    - name: description
      value: "{{ description }}"
      description: |
        A human-readable description of the health check.
    - name: http_config
      description: |
        Parameters specific to an HTTP or HTTPS health check.
      value:
        allow_insecure: {{ allow_insecure }}
        expected_body: "{{ expected_body }}"
        expected_codes:
          - "{{ expected_codes }}"
        follow_redirects: {{ follow_redirects }}
        header: "{{ header }}"
        method: "{{ method }}"
        path: "{{ path }}"
        port: {{ port }}
    - name: interval
      value: {{ interval }}
      description: |
        The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations.
      default: 60
    - name: name
      value: "{{ name }}"
      description: |
        A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.
    - name: retries
      value: {{ retries }}
      description: |
        The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately.
      default: 2
    - name: suspended
      value: {{ suspended }}
      description: |
        If suspended, no health checks are sent to the origin.
      default: false
    - name: tcp_config
      description: |
        Parameters specific to TCP health check.
      value:
        method: "{{ method }}"
        port: {{ port }}
    - name: timeout
      value: {{ timeout }}
      description: |
        The timeout (in seconds) before marking the health check as failed.
      default: 5
    - name: type
      value: "{{ type }}"
      description: |
        The protocol to use for the health check. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'.
      default: HTTP
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="edit"
    values={[
        { label: 'edit', value: 'edit' }
    ]}
>
<TabItem value="edit">

Patch a configured health check.

```sql
UPDATE cloudflare.healthchecks.healthchecks
SET 
address = '{{ address }}',
check_regions = '{{ check_regions }}',
consecutive_fails = {{ consecutive_fails }},
consecutive_successes = {{ consecutive_successes }},
description = '{{ description }}',
http_config = '{{ http_config }}',
interval = {{ interval }},
name = '{{ name }}',
retries = {{ retries }},
suspended = {{ suspended }},
tcp_config = '{{ tcp_config }}',
timeout = {{ timeout }},
type = '{{ type }}'
WHERE 
healthcheck_id = '{{ healthcheck_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND address = '{{ address }}' --required
RETURNING
errors,
messages,
result,
success;
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

Update a configured health check.

```sql
REPLACE cloudflare.healthchecks.healthchecks
SET 
address = '{{ address }}',
check_regions = '{{ check_regions }}',
consecutive_fails = {{ consecutive_fails }},
consecutive_successes = {{ consecutive_successes }},
description = '{{ description }}',
http_config = '{{ http_config }}',
interval = {{ interval }},
name = '{{ name }}',
retries = {{ retries }},
suspended = {{ suspended }},
tcp_config = '{{ tcp_config }}',
timeout = {{ timeout }},
type = '{{ type }}'
WHERE 
healthcheck_id = '{{ healthcheck_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND address = '{{ address }}' --required
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

Delete a health check.

```sql
DELETE FROM cloudflare.healthchecks.healthchecks
WHERE healthcheck_id = '{{ healthcheck_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>
