--- 
title: prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - prefixes
  - addressing
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

Creates, updates, deletes, gets or lists a <code>prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="prefixes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.addressing.prefixes" /></td></tr>
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

Prefix Details response

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
    <td>Identifier of an IP Prefix. (example: 2af39739cc4e3b5910c918468bb89828)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of a Cloudflare account. (example: 258def64c72dae45f3e4c8516e2111f2)</td>
</tr>
<tr>
    <td><CopyableCode code="loa_document_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for the uploaded LOA document. (example: d933b1530bc56c9953cf8ce166da8004)</td>
</tr>
<tr>
    <td><CopyableCode code="advertised" /></td>
    <td><code>boolean</code></td>
    <td>Prefix advertisement status to the Internet. This field is only not 'null' if on demand is enabled. (x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="advertised_modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the advertisement status was changed. This field is only not 'null' if on demand is enabled. (example: 2014-01-01T05:20:00.12345Z, x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="approved" /></td>
    <td><code>string</code></td>
    <td>Approval state of the prefix (P = pending, V = active). (example: P)</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Autonomous System Number (ASN) the prefix will be advertised under.</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="delegate_loa_creation" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cloudflare is allowed to generate the LOA document on behalf of the prefix owner.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the prefix. (example: Internal test prefix)</td>
</tr>
<tr>
    <td><CopyableCode code="irr_validation_state" /></td>
    <td><code>string</code></td>
    <td>State of one kind of validation for an IP prefix. (example: pending)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="on_demand_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether advertisement of the prefix to the Internet may be dynamically enabled or disabled. (x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="on_demand_locked" /></td>
    <td><code>boolean</code></td>
    <td>Whether advertisement status of the prefix is locked, meaning it cannot be changed. (x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_validation_state" /></td>
    <td><code>string</code></td>
    <td>State of one kind of validation for an IP prefix. (example: pending)</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_validation_token" /></td>
    <td><code>string</code></td>
    <td>Token provided to demonstrate ownership of the prefix. (example: 1234a5b6-1234-1abc-12a3-1234a5b6789c)</td>
</tr>
<tr>
    <td><CopyableCode code="rpki_validation_state" /></td>
    <td><code>string</code></td>
    <td>State of one kind of validation for an IP prefix. (example: pending)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List Prefixes response

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
    <td>Identifier of an IP Prefix. (example: 2af39739cc4e3b5910c918468bb89828)</td>
</tr>
<tr>
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of a Cloudflare account. (example: 258def64c72dae45f3e4c8516e2111f2)</td>
</tr>
<tr>
    <td><CopyableCode code="loa_document_id" /></td>
    <td><code>string</code></td>
    <td>Identifier for the uploaded LOA document. (example: d933b1530bc56c9953cf8ce166da8004)</td>
</tr>
<tr>
    <td><CopyableCode code="advertised" /></td>
    <td><code>boolean</code></td>
    <td>Prefix advertisement status to the Internet. This field is only not 'null' if on demand is enabled. (x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="advertised_modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the advertisement status was changed. This field is only not 'null' if on demand is enabled. (example: 2014-01-01T05:20:00.12345Z, x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="approved" /></td>
    <td><code>string</code></td>
    <td>Approval state of the prefix (P = pending, V = active). (example: P)</td>
</tr>
<tr>
    <td><CopyableCode code="asn" /></td>
    <td><code>integer</code></td>
    <td>Autonomous System Number (ASN) the prefix will be advertised under.</td>
</tr>
<tr>
    <td><CopyableCode code="cidr" /></td>
    <td><code>string</code></td>
    <td>IP Prefix in Classless Inter-Domain Routing format. (example: 192.0.2.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="delegate_loa_creation" /></td>
    <td><code>boolean</code></td>
    <td>Whether Cloudflare is allowed to generate the LOA document on behalf of the prefix owner.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the prefix. (example: Internal test prefix)</td>
</tr>
<tr>
    <td><CopyableCode code="irr_validation_state" /></td>
    <td><code>string</code></td>
    <td>State of one kind of validation for an IP prefix. (example: pending)</td>
</tr>
<tr>
    <td><CopyableCode code="modified_at" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="on_demand_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether advertisement of the prefix to the Internet may be dynamically enabled or disabled. (x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="on_demand_locked" /></td>
    <td><code>boolean</code></td>
    <td>Whether advertisement status of the prefix is locked, meaning it cannot be changed. (x-stainless-deprecation-message: Prefer the [BGP Prefixes API](https://developers.cloudflare.com/api/resources/addressing/subresources/prefixes/subresources/bgp_prefixes/) instead, which allows for advertising multiple BGP routes within a single IP Prefix.)</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_validation_state" /></td>
    <td><code>string</code></td>
    <td>State of one kind of validation for an IP prefix. (example: pending)</td>
</tr>
<tr>
    <td><CopyableCode code="ownership_validation_token" /></td>
    <td><code>string</code></td>
    <td>Token provided to demonstrate ownership of the prefix. (example: 1234a5b6-1234-1abc-12a3-1234a5b6789c)</td>
</tr>
<tr>
    <td><CopyableCode code="rpki_validation_state" /></td>
    <td><code>string</code></td>
    <td>State of one kind of validation for an IP prefix. (example: pending)</td>
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
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List a particular prefix owned by the account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>List all prefixes owned by the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-cidr"><code>cidr</code></a>, <a href="#parameter-asn"><code>asn</code></a></td>
    <td></td>
    <td>Add a new prefix under the account.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-description"><code>description</code></a></td>
    <td></td>
    <td>Modify the description for a prefix owned by the account.</td>
</tr>
<tr>
    <td><a href="#ip_address_management_prefixes_delete_bgp_prefix"><CopyableCode code="ip_address_management_prefixes_delete_bgp_prefix" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-bgp_prefix_id"><code>bgp_prefix_id</code></a></td>
    <td></td>
    <td>Delete a BGP Prefix associated with the specified IP Prefix. A BGP Prefix must be withdrawn before it can be deleted.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Delete an unapproved prefix owned by the account.</td>
</tr>
<tr>
    <td><a href="#validate_prefix"><CopyableCode code="validate_prefix" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-prefix_id"><code>prefix_id</code></a>, <a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Triggers a new prefix validation. The checks are run asynchronously and include IRR, RPKI, and prefix ownership.</td>
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
<tr id="parameter-bgp_prefix_id">
    <td><CopyableCode code="bgp_prefix_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-prefix_id">
    <td><CopyableCode code="prefix_id" /></td>
    <td><code>string</code></td>
    <td>The IP prefix ID.</td>
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

List a particular prefix owned by the account.

```sql
SELECT
id,
account_id,
loa_document_id,
advertised,
advertised_modified_at,
approved,
asn,
cidr,
created_at,
delegate_loa_creation,
description,
irr_validation_state,
modified_at,
on_demand_enabled,
on_demand_locked,
ownership_validation_state,
ownership_validation_token,
rpki_validation_state
FROM cloudflare.addressing.prefixes
WHERE prefix_id = '{{ prefix_id }}' -- required
AND account_id = '{{ account_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all prefixes owned by the account.

```sql
SELECT
id,
account_id,
loa_document_id,
advertised,
advertised_modified_at,
approved,
asn,
cidr,
created_at,
delegate_loa_creation,
description,
irr_validation_state,
modified_at,
on_demand_enabled,
on_demand_locked,
ownership_validation_state,
ownership_validation_token,
rpki_validation_state
FROM cloudflare.addressing.prefixes
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

Add a new prefix under the account.

```sql
INSERT INTO cloudflare.addressing.prefixes (
asn,
cidr,
delegate_loa_creation,
description,
loa_document_id,
account_id
)
SELECT 
{{ asn }} /* required */,
'{{ cidr }}' /* required */,
{{ delegate_loa_creation }},
'{{ description }}',
'{{ loa_document_id }}',
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
- name: prefixes
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the prefixes resource.
    - name: asn
      value: {{ asn }}
      description: |
        Autonomous System Number (ASN) the prefix will be advertised under.
    - name: cidr
      value: "{{ cidr }}"
      description: |
        IP Prefix in Classless Inter-Domain Routing format.
    - name: delegate_loa_creation
      value: {{ delegate_loa_creation }}
      description: |
        Whether Cloudflare is allowed to generate the LOA document on behalf of the prefix owner.
      default: false
    - name: description
      value: "{{ description }}"
      description: |
        Description of the prefix.
    - name: loa_document_id
      value: "{{ loa_document_id }}"
      description: |
        Identifier for the uploaded LOA document.
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

Modify the description for a prefix owned by the account.

```sql
UPDATE cloudflare.addressing.prefixes
SET 
description = '{{ description }}'
WHERE 
prefix_id = '{{ prefix_id }}' --required
AND account_id = '{{ account_id }}' --required
AND description = '{{ description }}' --required
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
    defaultValue="ip_address_management_prefixes_delete_bgp_prefix"
    values={[
        { label: 'ip_address_management_prefixes_delete_bgp_prefix', value: 'ip_address_management_prefixes_delete_bgp_prefix' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="ip_address_management_prefixes_delete_bgp_prefix">

Delete a BGP Prefix associated with the specified IP Prefix. A BGP Prefix must be withdrawn before it can be deleted.

```sql
DELETE FROM cloudflare.addressing.prefixes
WHERE account_id = '{{ account_id }}' --required
AND prefix_id = '{{ prefix_id }}' --required
AND bgp_prefix_id = '{{ bgp_prefix_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete an unapproved prefix owned by the account.

```sql
DELETE FROM cloudflare.addressing.prefixes
WHERE prefix_id = '{{ prefix_id }}' --required
AND account_id = '{{ account_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_prefix"
    values={[
        { label: 'validate_prefix', value: 'validate_prefix' }
    ]}
>
<TabItem value="validate_prefix">

Triggers a new prefix validation. The checks are run asynchronously and include IRR, RPKI, and prefix ownership.

```sql
EXEC cloudflare.addressing.prefixes.validate_prefix 
@prefix_id='{{ prefix_id }}' --required, 
@account_id='{{ account_id }}' --required
;
```
</TabItem>
</Tabs>
