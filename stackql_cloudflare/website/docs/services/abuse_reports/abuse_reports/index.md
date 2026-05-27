--- 
title: abuse_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - abuse_reports
  - abuse_reports
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

Creates, updates, deletes, gets or lists an <code>abuse_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="abuse_reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.abuse_reports.abuse_reports" /></td></tr>
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

Report submitted successfully

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
    <td>Public facing ID of abuse report, aka abuse_rand.</td>
</tr>
<tr>
    <td><CopyableCode code="cdate" /></td>
    <td><code>string</code></td>
    <td>Creation date of report. Time in RFC 3339 format (https://www.rfc-editor.org/rfc/rfc3339.html) (example: 2009-11-10T23:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain that relates to the report.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for the report.</td>
</tr>
<tr>
    <td><CopyableCode code="mitigation_summary" /></td>
    <td><code>object</code></td>
    <td>A summary of the mitigations related to this report.</td>
</tr>
<tr>
    <td><CopyableCode code="original_work" /></td>
    <td><code>string</code></td>
    <td>Original work / Targeted brand in the alleged abuse.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>An enum value that represents the status of an abuse record (accepted, in_review)</td>
</tr>
<tr>
    <td><CopyableCode code="submitter" /></td>
    <td><code>object</code></td>
    <td>Information about the submitter of the report.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The abuse report type (PHISH, GEN, THREAT, DMCA, EMER, TM, REG_WHO, NCSEI, NETWORK)</td>
</tr>
<tr>
    <td><CopyableCode code="urls" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Abuse report list successful

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
    <td>Public facing ID of abuse report, aka abuse_rand.</td>
</tr>
<tr>
    <td><CopyableCode code="cdate" /></td>
    <td><code>string</code></td>
    <td>Creation date of report. Time in RFC 3339 format (https://www.rfc-editor.org/rfc/rfc3339.html) (example: 2009-11-10T23:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Domain that relates to the report.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification for the report.</td>
</tr>
<tr>
    <td><CopyableCode code="mitigation_summary" /></td>
    <td><code>object</code></td>
    <td>A summary of the mitigations related to this report.</td>
</tr>
<tr>
    <td><CopyableCode code="original_work" /></td>
    <td><code>string</code></td>
    <td>Original work / Targeted brand in the alleged abuse.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>An enum value that represents the status of an abuse record (accepted, in_review)</td>
</tr>
<tr>
    <td><CopyableCode code="submitter" /></td>
    <td><code>object</code></td>
    <td>Information about the submitter of the report.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The abuse report type (PHISH, GEN, THREAT, DMCA, EMER, TM, REG_WHO, NCSEI, NETWORK)</td>
</tr>
<tr>
    <td><CopyableCode code="urls" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-report_param"><code>report_param</code></a></td>
    <td></td>
    <td>Retrieve the details of an abuse report.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-sort"><code>sort</code></a>, <a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-created_before"><code>created_before</code></a>, <a href="#parameter-created_after"><code>created_after</code></a>, <a href="#parameter-status"><code>status</code></a>, <a href="#parameter-type"><code>type</code></a>, <a href="#parameter-mitigation_status"><code>mitigation_status</code></a></td>
    <td>List the abuse reports for a given account</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-report_param"><code>report_param</code></a>, <a href="#parameter-act"><code>act</code></a>, <a href="#parameter-email"><code>email</code></a>, <a href="#parameter-email2"><code>email2</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-owner_notification"><code>owner_notification</code></a>, <a href="#parameter-urls"><code>urls</code></a></td>
    <td></td>
    <td>Submit the Abuse Report of a particular type</td>
</tr>
<tr>
    <td><a href="#request_review"><CopyableCode code="request_review" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-report_id"><code>report_id</code></a>, <a href="#parameter-appeals"><code>appeals</code></a></td>
    <td></td>
    <td>Request a review for mitigations on an account.</td>
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
<tr id="parameter-report_id">
    <td><CopyableCode code="report_id" /></td>
    <td><code>string</code></td>
    <td>Abuse Report ID</td>
</tr>
<tr id="parameter-report_param">
    <td><CopyableCode code="report_param" /></td>
    <td><code>string</code></td>
    <td>The report type to be submitted. Example: abuse_general</td>
</tr>
<tr id="parameter-created_after">
    <td><CopyableCode code="created_after" /></td>
    <td><code>string</code></td>
    <td>Returns reports created after the specified date</td>
</tr>
<tr id="parameter-created_before">
    <td><CopyableCode code="created_before" /></td>
    <td><code>string</code></td>
    <td>Returns reports created before the specified date</td>
</tr>
<tr id="parameter-domain">
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>Filter by domain name related to the abuse report</td>
</tr>
<tr id="parameter-mitigation_status">
    <td><CopyableCode code="mitigation_status" /></td>
    <td><code>string</code></td>
    <td>Filter reports that have any mitigations in the given status.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>Where in pagination to start listing abuse reports</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>How many abuse reports per page to list</td>
</tr>
<tr id="parameter-sort">
    <td><CopyableCode code="sort" /></td>
    <td><code>string</code></td>
    <td>A property to sort by, followed by the order (id, cdate, domain, type, status)</td>
</tr>
<tr id="parameter-status">
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Filter by the status of the report.</td>
</tr>
<tr id="parameter-type">
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Filter by the type of the report.</td>
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

Retrieve the details of an abuse report.

```sql
SELECT
id,
cdate,
domain,
justification,
mitigation_summary,
original_work,
status,
submitter,
type,
urls
FROM cloudflare.abuse_reports.abuse_reports
WHERE account_id = '{{ account_id }}' -- required
AND report_param = '{{ report_param }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the abuse reports for a given account

```sql
SELECT
id,
cdate,
domain,
justification,
mitigation_summary,
original_work,
status,
submitter,
type,
urls
FROM cloudflare.abuse_reports.abuse_reports
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
AND sort = '{{ sort }}'
AND domain = '{{ domain }}'
AND created_before = '{{ created_before }}'
AND created_after = '{{ created_after }}'
AND status = '{{ status }}'
AND type = '{{ type }}'
AND mitigation_status = '{{ mitigation_status }}'
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

Submit the Abuse Report of a particular type

```sql
INSERT INTO cloudflare.abuse_reports.abuse_reports (
act,
comments,
company,
email,
email2,
name,
reported_country,
reported_user_agent,
tele,
title,
urls,
address1,
agent_name,
agree,
city,
country,
host_notification,
original_work,
owner_notification,
signature,
state,
justification,
trademark_number,
trademark_office,
trademark_symbol,
destination_ips,
ports_protocols,
source_ips,
ncmec_notification,
reg_who_request,
ncsei_subject_representation,
account_id,
report_param
)
SELECT 
'{{ act }}' /* required */,
'{{ comments }}',
'{{ company }}',
'{{ email }}' /* required */,
'{{ email2 }}' /* required */,
'{{ name }}' /* required */,
'{{ reported_country }}',
'{{ reported_user_agent }}',
'{{ tele }}',
'{{ title }}',
'{{ urls }}' /* required */,
'{{ address1 }}',
'{{ agent_name }}',
{{ agree }},
'{{ city }}',
'{{ country }}',
'{{ host_notification }}',
'{{ original_work }}',
'{{ owner_notification }}' /* required */,
'{{ signature }}',
'{{ state }}',
'{{ justification }}',
'{{ trademark_number }}',
'{{ trademark_office }}',
'{{ trademark_symbol }}',
'{{ destination_ips }}',
'{{ ports_protocols }}',
'{{ source_ips }}',
'{{ ncmec_notification }}',
'{{ reg_who_request }}',
{{ ncsei_subject_representation }},
'{{ account_id }}',
'{{ report_param }}'
RETURNING
abuse_rand,
request,
result
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: abuse_reports
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the abuse_reports resource.
    - name: report_param
      value: "{{ report_param }}"
      description: Required parameter for the abuse_reports resource.
    - name: act
      value: "{{ act }}"
      description: |
        The report type for submitted reports.
      valid_values: ['abuse_dmca']
    - name: comments
      value: "{{ comments }}"
      description: |
        Any additional comments about the infringement not exceeding 2000 characters
    - name: company
      value: "{{ company }}"
      description: |
        Text not exceeding 100 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: email
      value: "{{ email }}"
      description: |
        A valid email of the abuse reporter. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: email2
      value: "{{ email2 }}"
      description: |
        Should match the value provided in \`email\`
    - name: name
      value: "{{ name }}"
      description: |
        Text not exceeding 255 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: reported_country
      value: "{{ reported_country }}"
      description: |
        Text containing 2 characters
    - name: reported_user_agent
      value: "{{ reported_user_agent }}"
      description: |
        Text not exceeding 255 characters
    - name: tele
      value: "{{ tele }}"
      description: |
        Text not exceeding 20 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: title
      value: "{{ title }}"
      description: |
        Text not exceeding 255 characters
    - name: urls
      value: "{{ urls }}"
      description: |
        A list of valid URLs separated by ‘\n’ (new line character). The list of the URLs should not exceed 250 URLs. All URLs should have the same hostname. Each URL should be unique. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: address1
      value: "{{ address1 }}"
      description: |
        Text not exceeding 100 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: agent_name
      value: "{{ agent_name }}"
      description: |
        The name of the copyright holder. Text not exceeding 60 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: agree
      value: {{ agree }}
      description: |
        Can be \`0\` for false or \`1\` for true. Must be value: 1 for DMCA reports
      valid_values: ['1']
    - name: city
      value: "{{ city }}"
      description: |
        Text not exceeding 255 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: country
      value: "{{ country }}"
      description: |
        Text not exceeding 255 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: host_notification
      value: "{{ host_notification }}"
      description: |
        Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
      valid_values: ['send']
    - name: original_work
      value: "{{ original_work }}"
      description: |
        Text not exceeding 255 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: owner_notification
      value: "{{ owner_notification }}"
      description: |
        Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
      valid_values: ['send']
    - name: signature
      value: "{{ signature }}"
      description: |
        Required for DMCA reports, should be same as Name. An affirmation that all information in the report is true and accurate while agreeing to the policies of Cloudflare's abuse reports
    - name: state
      value: "{{ state }}"
      description: |
        Text not exceeding 255 characters. This field may be released by Cloudflare to third parties such as the Lumen Database (https://lumendatabase.org/).
    - name: justification
      value: "{{ justification }}"
      description: |
        A detailed description of the infringement, including any necessary access details and the exact steps needed to view the content, not exceeding 5000 characters.
    - name: trademark_number
      value: "{{ trademark_number }}"
      description: |
        Text not exceeding 1000 characters
    - name: trademark_office
      value: "{{ trademark_office }}"
      description: |
        Text not exceeding 1000 characters
    - name: trademark_symbol
      value: "{{ trademark_symbol }}"
      description: |
        Text not exceeding 1000 characters
    - name: destination_ips
      value: "{{ destination_ips }}"
      description: |
        A list of IP addresses separated by ‘\n’ (new line character). The list of destination IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be unique.
    - name: ports_protocols
      value: "{{ ports_protocols }}"
      description: |
        A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total size of the field should not exceed 2000 characters. Each individual port/protocol should not exceed 100 characters. The list should not have more than 30 unique ports and protocols.
    - name: source_ips
      value: "{{ source_ips }}"
      description: |
        A list of IP addresses separated by ‘\n’ (new line character). The list of source IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be unique.
    - name: ncmec_notification
      value: "{{ ncmec_notification }}"
      description: |
        Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
      valid_values: ['send', 'send-anon']
    - name: reg_who_request
      description: |
        RDP-mandated fields for registrar WHOIS data disclosure requests.
      value:
        reg_who_authorization_statement: "{{ reg_who_authorization_statement }}"
        reg_who_good_faith_affirmation: {{ reg_who_good_faith_affirmation }}
        reg_who_lawful_processing_agreement: {{ reg_who_lawful_processing_agreement }}
        reg_who_legal_basis: "{{ reg_who_legal_basis }}"
        reg_who_request_type: "{{ reg_who_request_type }}"
        reg_who_requested_data_elements:
          - "{{ reg_who_requested_data_elements }}"
        reg_who_requestor_type: "{{ reg_who_requestor_type }}"
    - name: ncsei_subject_representation
      value: {{ ncsei_subject_representation }}
      description: |
        If the submitter is the target of NCSEI in the URLs of the abuse report.
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="request_review"
    values={[
        { label: 'request_review', value: 'request_review' }
    ]}
>
<TabItem value="request_review">

Request a review for mitigations on an account.

```sql
EXEC cloudflare.abuse_reports.abuse_reports.request_review 
@account_id='{{ account_id }}' --required, 
@report_id='{{ report_id }}' --required 
@@json=
'{
"appeals": "{{ appeals }}"
}'
;
```
</TabItem>
</Tabs>
