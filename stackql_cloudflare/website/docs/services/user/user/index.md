--- 
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - user
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

Creates, updates, deletes, gets or lists a <code>user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.user.user" /></td></tr>
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

User Details response

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
    <td>Identifier of the user. (example: 6d7f2f5f5b1d4a0e9081fdc98d432fd1)</td>
</tr>
<tr>
    <td><CopyableCode code="first_name" /></td>
    <td><code>string</code></td>
    <td>User's first name (example: John)</td>
</tr>
<tr>
    <td><CopyableCode code="last_name" /></td>
    <td><code>string</code></td>
    <td>User's last name (example: Appleseed)</td>
</tr>
<tr>
    <td><CopyableCode code="betas" /></td>
    <td><code>array</code></td>
    <td>Lists the betas that the user is participating in.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country in which the user lives. (example: US)</td>
</tr>
<tr>
    <td><CopyableCode code="has_business_zones" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user has any business zones</td>
</tr>
<tr>
    <td><CopyableCode code="has_enterprise_zones" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user has any enterprise zones</td>
</tr>
<tr>
    <td><CopyableCode code="has_pro_zones" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user has any pro zones</td>
</tr>
<tr>
    <td><CopyableCode code="organizations" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user has been suspended</td>
</tr>
<tr>
    <td><CopyableCode code="telephone" /></td>
    <td><code>string</code></td>
    <td>User's telephone number (example: +1 123-123-1234)</td>
</tr>
<tr>
    <td><CopyableCode code="two_factor_authentication_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether two-factor authentication is enabled for the user account. Does not apply to API authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="two_factor_authentication_locked" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether two-factor authentication is required by one of the accounts that the user is a member of.</td>
</tr>
<tr>
    <td><CopyableCode code="zipcode" /></td>
    <td><code>string</code></td>
    <td>The zipcode or postal code where the user lives. (example: 12345)</td>
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
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Edit part of your user details.</td>
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

User Details response

```sql
SELECT
id,
first_name,
last_name,
betas,
country,
has_business_zones,
has_enterprise_zones,
has_pro_zones,
organizations,
suspended,
telephone,
two_factor_authentication_enabled,
two_factor_authentication_locked,
zipcode
FROM cloudflare.user.user
;
```
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

Edit part of your user details.

```sql
UPDATE cloudflare.user.user
SET 
country = '{{ country }}',
first_name = '{{ first_name }}',
last_name = '{{ last_name }}',
telephone = '{{ telephone }}',
zipcode = '{{ zipcode }}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
