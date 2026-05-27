--- 
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - billing
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.billing.profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Billing Profile Details response

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
    <td>Billing item identifier tag. (example: b69a9f3492637782896352daae219e7d)</td>
</tr>
<tr>
    <td><CopyableCode code="first_name" /></td>
    <td><code>string</code></td>
    <td> (example: John)</td>
</tr>
<tr>
    <td><CopyableCode code="last_name" /></td>
    <td><code>string</code></td>
    <td> (example: Doe)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_first_name" /></td>
    <td><code>string</code></td>
    <td> (example: John)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_last_name" /></td>
    <td><code>string</code></td>
    <td> (example: Doe)</td>
</tr>
<tr>
    <td><CopyableCode code="account_type" /></td>
    <td><code>string</code></td>
    <td> (example: type)</td>
</tr>
<tr>
    <td><CopyableCode code="address" /></td>
    <td><code>string</code></td>
    <td> (example: 123 Main Street)</td>
</tr>
<tr>
    <td><CopyableCode code="address2" /></td>
    <td><code>string</code></td>
    <td> (example: Apt 1)</td>
</tr>
<tr>
    <td><CopyableCode code="balance" /></td>
    <td><code>string</code></td>
    <td> (example: 0)</td>
</tr>
<tr>
    <td><CopyableCode code="card_expiry_month" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="card_expiry_year" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="card_number" /></td>
    <td><code>string</code></td>
    <td> (example: 4242424242424242)</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td> (example: Anytown)</td>
</tr>
<tr>
    <td><CopyableCode code="company" /></td>
    <td><code>string</code></td>
    <td> (example: Company)</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td> (example: Anycountry)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-03-01T12:21:59.3456Z)</td>
</tr>
<tr>
    <td><CopyableCode code="device_data" /></td>
    <td><code>string</code></td>
    <td> (example: sample_data)</td>
</tr>
<tr>
    <td><CopyableCode code="edited_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-03-01T12:21:59.3456Z)</td>
</tr>
<tr>
    <td><CopyableCode code="enterprise_billing_email" /></td>
    <td><code>string</code></td>
    <td> (example: johndoe@gmail.com)</td>
</tr>
<tr>
    <td><CopyableCode code="enterprise_primary_email" /></td>
    <td><code>string</code></td>
    <td> (example: johndoe@gmail.com)</td>
</tr>
<tr>
    <td><CopyableCode code="is_partner" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="next_bill_date" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-03-01T12:21:59.3456Z)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_address" /></td>
    <td><code>string</code></td>
    <td> (example: 123 Main Street)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_address2" /></td>
    <td><code>string</code></td>
    <td> (example: Apt 1)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_city" /></td>
    <td><code>string</code></td>
    <td> (example: Anytown)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_country" /></td>
    <td><code>string</code></td>
    <td> (example: Anycountry)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_email" /></td>
    <td><code>string</code></td>
    <td> (example: johndoe@gmail.com)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_gateway" /></td>
    <td><code>string</code></td>
    <td> (example: gateway)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_nonce" /></td>
    <td><code>string</code></td>
    <td> (example: abc123)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_state" /></td>
    <td><code>string</code></td>
    <td> (example: state)</td>
</tr>
<tr>
    <td><CopyableCode code="payment_zipcode" /></td>
    <td><code>string</code></td>
    <td> (example: 12345)</td>
</tr>
<tr>
    <td><CopyableCode code="primary_email" /></td>
    <td><code>string</code></td>
    <td> (example: johndoe@gmail.com)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td> (example: AnyState)</td>
</tr>
<tr>
    <td><CopyableCode code="tax_id_type" /></td>
    <td><code>string</code></td>
    <td> (example: type)</td>
</tr>
<tr>
    <td><CopyableCode code="telephone" /></td>
    <td><code>string</code></td>
    <td> (example: 1234567899)</td>
</tr>
<tr>
    <td><CopyableCode code="use_legacy" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="validation_code" /></td>
    <td><code>string</code></td>
    <td> (example: 1111)</td>
</tr>
<tr>
    <td><CopyableCode code="vat" /></td>
    <td><code>string</code></td>
    <td> (example: GB123456789)</td>
</tr>
<tr>
    <td><CopyableCode code="zipcode" /></td>
    <td><code>string</code></td>
    <td> (example: 12345)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td></td>
    <td>Gets the current billing profile for the account.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets the current billing profile for the account.

```sql
SELECT
id,
first_name,
last_name,
payment_first_name,
payment_last_name,
account_type,
address,
address2,
balance,
card_expiry_month,
card_expiry_year,
card_number,
city,
company,
country,
created_on,
device_data,
edited_on,
enterprise_billing_email,
enterprise_primary_email,
is_partner,
next_bill_date,
payment_address,
payment_address2,
payment_city,
payment_country,
payment_email,
payment_gateway,
payment_nonce,
payment_state,
payment_zipcode,
primary_email,
state,
tax_id_type,
telephone,
use_legacy,
validation_code,
vat,
zipcode
FROM cloudflare.billing.profiles
WHERE account_id = '{{ account_id }}' -- required
;
```
</TabItem>
</Tabs>
