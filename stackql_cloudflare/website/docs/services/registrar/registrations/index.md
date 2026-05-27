--- 
title: registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations
  - registrar
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

Creates, updates, deletes, gets or lists a <code>registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.registrar.registrations" /></td></tr>
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

Registration details.

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
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name (FQDN) including the extension (e.g., `example.com`, `mybrand.app`). The domain name uniquely identifies a registration — the same domain cannot be registered twice, making it a natural idempotency key for registration requests. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_renew" /></td>
    <td><code>boolean</code></td>
    <td>Whether the domain will be automatically renewed before expiration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the domain was registered. Present when the registration resource exists. (example: 2025-01-15T10:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the domain registration expires. Present when the registration is ready; may be null only while `status` is `registration_pending`. (example: 2026-01-15T10:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="locked" /></td>
    <td><code>boolean</code></td>
    <td>Whether the domain is locked for transfer.</td>
</tr>
<tr>
    <td><CopyableCode code="privacy_mode" /></td>
    <td><code>string</code></td>
    <td>Current WHOIS privacy mode for the registration. (false, redaction) (example: redaction)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current registration status. - `active`: Domain is registered and operational - `registration_pending`: Registration is in progress - `expired`: Domain has expired - `suspended`: Domain is suspended by the registry - `redemption_period`: Domain is in the redemption grace period - `pending_delete`: Domain is pending deletion by the registry (active, registration_pending, expired, suspended, redemption_period, pending_delete) (example: active)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

List of registrations for the account.

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
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>Fully qualified domain name (FQDN) including the extension (e.g., `example.com`, `mybrand.app`). The domain name uniquely identifies a registration — the same domain cannot be registered twice, making it a natural idempotency key for registration requests. (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="auto_renew" /></td>
    <td><code>boolean</code></td>
    <td>Whether the domain will be automatically renewed before expiration.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the domain was registered. Present when the registration resource exists. (example: 2025-01-15T10:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the domain registration expires. Present when the registration is ready; may be null only while `status` is `registration_pending`. (example: 2026-01-15T10:00:00Z)</td>
</tr>
<tr>
    <td><CopyableCode code="locked" /></td>
    <td><code>boolean</code></td>
    <td>Whether the domain is locked for transfer.</td>
</tr>
<tr>
    <td><CopyableCode code="privacy_mode" /></td>
    <td><code>string</code></td>
    <td>Current WHOIS privacy mode for the registration. (false, redaction) (example: redaction)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current registration status. - `active`: Domain is registered and operational - `registration_pending`: Registration is in progress - `expired`: Domain has expired - `suspended`: Domain is suspended by the registry - `redemption_period`: Domain is in the redemption grace period - `pending_delete`: Domain is pending deletion by the registry (active, registration_pending, expired, suspended, redemption_period, pending_delete) (example: active)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a></td>
    <td></td>
    <td>Returns the current state of a domain registration. This is the canonical read endpoint for a domain you own. It returns the full registration resource including current settings and expiration. When the registration resource is ready, both `created_at` and `expires_at` are present in the response.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-cursor"><code>cursor</code></a>, <a href="#parameter-per_page"><code>per_page</code></a>, <a href="#parameter-direction"><code>direction</code></a>, <a href="#parameter-sort_by"><code>sort_by</code></a></td>
    <td>Returns a paginated list of domain registrations owned by the account. This endpoint uses cursor-based pagination. Results are ordered by registration date by default. To fetch the next page, pass the `cursor` value from the `result_info` object in the response as the `cursor` query parameter in your next request. An empty `cursor` string indicates there are no more pages.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a></td>
    <td><a href="#parameter-Prefer"><code>Prefer</code></a></td>
    <td>Starts a domain registration workflow. This is a billable operation — successful registration charges the account's default payment method. All successful domain registrations are non-refundable — once the workflow completes with `state: succeeded`, the charge cannot be reversed. **Prerequisites:** - The account must have a billing profile with a valid default payment method. Set this up at `https://dash.cloudflare.com/&#123;account_id&#125;/billing/payment-info`. - The account must not already be at the maximum supported domain limit. A single account may own up to 100 domains in total across registrations created through either the dashboard or this API. - The domain must be on a supported extension for programmatic registration. - Use `POST /domain-check` immediately before calling this endpoint to confirm real-time availability and pricing. **Supported extensions:** In this API, "extension" means the full registrable suffix after the domain label. For example, in `example.co.uk`, the extension is `co.uk`. Programmatic registration is currently supported for: `com`, `org`, `net`, `app`, `dev`, `cc`, `xyz`, `info`, `cloud`, `studio`, `live`, `link`, `pro`, `tech`, `fyi`, `shop`, `online`, `tools`, `run`, `games`, `build`, `systems`, `world`, `news`, `site`, `network`, `chat`, `space`, `family`, `page`, `life`, `group`, `email`, `solutions`, `day`, `blog`, `ing`, `icu`, `academy`, `today` Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions not listed above can still be registered at `https://dash.cloudflare.com/&#123;account_id&#125;/domains/registrations`. **Express mode:** The only required field is `domain_name`. If `contacts` is omitted, the system uses the account's default address book entry as the registrant. If no default exists and no contact is provided, the request fails. Set up a default address book entry and accept the required agreement at `https://dash.cloudflare.com/&#123;account_id&#125;/domains/registrations`. **Defaults:** - `years`: defaults to the extension's minimum registration period (1 year for most extensions, but varies — for example, `.ai` (if supported) requires a minimum of 2 years). - `auto_renew`: defaults to `false`. Setting it to `true` is an explicit opt-in authorizing Cloudflare to charge the account's default payment method up to 30 days before domain expiry to renew the registration. Renewal pricing may change over time based on registry pricing. - `privacy_mode`: defaults to `redaction`. **Premium domains:** Premium domain registration is not currently supported by this API. If `POST /domain-check` returns `tier: premium`, do not call this endpoint for that domain. **Response behavior:** By default, the server holds the connection for a bounded, server-defined amount of time while the registration completes. Most registrations finish within this window and return `201 Created` with a completed workflow status. If the registration is still processing after this synchronous wait window, the server returns `202 Accepted`. Poll the URL in `links.self` to track progress. To skip the wait and receive an immediate `202`, send `Prefer: respond-async`.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a></td>
    <td><a href="#parameter-Prefer"><code>Prefer</code></a></td>
    <td>Updates an existing domain registration. By default, the server holds the connection for a bounded, server-defined amount of time while the update completes. Most updates finish within this window and return `200 OK` with a completed workflow status. If the update is still processing after this synchronous wait window, the server returns `202 Accepted`. Poll the URL in `links.self` to track progress. To skip the wait and receive an immediate `202`, send `Prefer: respond-async`. This endpoint currently supports updating `auto_renew` only.</td>
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
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>Domain name to update.</td>
</tr>
<tr id="parameter-Prefer">
    <td><CopyableCode code="Prefer" /></td>
    <td><code>string</code></td>
    <td>Set to `respond-async` to receive an immediate `202 Accepted` without waiting for the operation to complete (RFC 7240).</td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td>Opaque token from a previous response's `result_info.cursor`. Pass this value to fetch the next page of results. Omit (or pass an empty string) for the first page.</td>
</tr>
<tr id="parameter-direction">
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Sort direction for results. Defaults to ascending order.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>integer</code></td>
    <td>Number of items to return per page.</td>
</tr>
<tr id="parameter-sort_by">
    <td><CopyableCode code="sort_by" /></td>
    <td><code>string</code></td>
    <td>Column to sort results by. Defaults to registration date (`registry_created_at`) when omitted.</td>
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

Returns the current state of a domain registration. This is the canonical read endpoint for a domain you own. It returns the full registration resource including current settings and expiration. When the registration resource is ready, both `created_at` and `expires_at` are present in the response.

```sql
SELECT
domain_name,
auto_renew,
created_at,
expires_at,
locked,
privacy_mode,
status
FROM cloudflare.registrar.registrations
WHERE account_id = '{{ account_id }}' -- required
AND domain_name = '{{ domain_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of domain registrations owned by the account. This endpoint uses cursor-based pagination. Results are ordered by registration date by default. To fetch the next page, pass the `cursor` value from the `result_info` object in the response as the `cursor` query parameter in your next request. An empty `cursor` string indicates there are no more pages.

```sql
SELECT
domain_name,
auto_renew,
created_at,
expires_at,
locked,
privacy_mode,
status
FROM cloudflare.registrar.registrations
WHERE account_id = '{{ account_id }}' -- required
AND cursor = '{{ cursor }}'
AND per_page = '{{ per_page }}'
AND direction = '{{ direction }}'
AND sort_by = '{{ sort_by }}'
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

Starts a domain registration workflow. This is a billable operation — successful registration charges the account's default payment method. All successful domain registrations are non-refundable — once the workflow completes with `state: succeeded`, the charge cannot be reversed. **Prerequisites:** - The account must have a billing profile with a valid default payment method. Set this up at `https://dash.cloudflare.com/&#123;account_id&#125;/billing/payment-info`. - The account must not already be at the maximum supported domain limit. A single account may own up to 100 domains in total across registrations created through either the dashboard or this API. - The domain must be on a supported extension for programmatic registration. - Use `POST /domain-check` immediately before calling this endpoint to confirm real-time availability and pricing. **Supported extensions:** In this API, "extension" means the full registrable suffix after the domain label. For example, in `example.co.uk`, the extension is `co.uk`. Programmatic registration is currently supported for: `com`, `org`, `net`, `app`, `dev`, `cc`, `xyz`, `info`, `cloud`, `studio`, `live`, `link`, `pro`, `tech`, `fyi`, `shop`, `online`, `tools`, `run`, `games`, `build`, `systems`, `world`, `news`, `site`, `network`, `chat`, `space`, `family`, `page`, `life`, `group`, `email`, `solutions`, `day`, `blog`, `ing`, `icu`, `academy`, `today` Cloudflare Registrar supports 400+ extensions in the dashboard. Extensions not listed above can still be registered at `https://dash.cloudflare.com/&#123;account_id&#125;/domains/registrations`. **Express mode:** The only required field is `domain_name`. If `contacts` is omitted, the system uses the account's default address book entry as the registrant. If no default exists and no contact is provided, the request fails. Set up a default address book entry and accept the required agreement at `https://dash.cloudflare.com/&#123;account_id&#125;/domains/registrations`. **Defaults:** - `years`: defaults to the extension's minimum registration period (1 year for most extensions, but varies — for example, `.ai` (if supported) requires a minimum of 2 years). - `auto_renew`: defaults to `false`. Setting it to `true` is an explicit opt-in authorizing Cloudflare to charge the account's default payment method up to 30 days before domain expiry to renew the registration. Renewal pricing may change over time based on registry pricing. - `privacy_mode`: defaults to `redaction`. **Premium domains:** Premium domain registration is not currently supported by this API. If `POST /domain-check` returns `tier: premium`, do not call this endpoint for that domain. **Response behavior:** By default, the server holds the connection for a bounded, server-defined amount of time while the registration completes. Most registrations finish within this window and return `201 Created` with a completed workflow status. If the registration is still processing after this synchronous wait window, the server returns `202 Accepted`. Poll the URL in `links.self` to track progress. To skip the wait and receive an immediate `202`, send `Prefer: respond-async`.

```sql
INSERT INTO cloudflare.registrar.registrations (
auto_renew,
contacts,
domain_name,
privacy_mode,
years,
account_id,
Prefer
)
SELECT 
{{ auto_renew }},
'{{ contacts }}',
'{{ domain_name }}' /* required */,
'{{ privacy_mode }}',
{{ years }},
'{{ account_id }}',
'{{ Prefer }}'
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
- name: registrations
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the registrations resource.
    - name: auto_renew
      value: {{ auto_renew }}
      description: |
        Enable or disable automatic renewal. Defaults to \`false\` if omitted. Setting this field to \`true\` is an explicit opt-in authorizing Cloudflare to charge the account's default payment method up to 30 days before domain expiry to renew the domain automatically. Renewal pricing may change over time based on registry pricing.
      default: false
    - name: contacts
      description: |
        Contact data for the registration request. If the \`contacts\` object is omitted entirely from the request, or if \`contacts.registrant\` is not provided, the system will use the account's default address book entry as the registrant contact. This default must be pre-configured by the account owner at \`https://dash.cloudflare.com/{account_id}/domains/registrations\`, where they can create or update the address book entry and accept the required agreement. No API exists for managing address book entries at this time. If no default address book entry exists and no registrant contact is provided, the registration request will fail with a validation error.
      value:
        registrant:
          email: "{{ email }}"
          fax: "{{ fax }}"
          phone: "{{ phone }}"
          postal_info:
            address:
              city: "{{ city }}"
              country_code: "{{ country_code }}"
              postal_code: "{{ postal_code }}"
              state: "{{ state }}"
              street: "{{ street }}"
            name: "{{ name }}"
            organization: "{{ organization }}"
    - name: domain_name
      value: "{{ domain_name }}"
      description: |
        Fully qualified domain name (FQDN) including the extension (e.g., \`example.com\`, \`mybrand.app\`). The domain name uniquely identifies a registration — the same domain cannot be registered twice, making it a natural idempotency key for registration requests.
    - name: privacy_mode
      value: "{{ privacy_mode }}"
      description: |
        WHOIS privacy mode for the registration. Defaults to \`redaction\`. - \`off\`: Do not request WHOIS privacy. - \`redaction\`: Request WHOIS redaction where supported by the extension. Some extensions do not support privacy/redaction.
      valid_values: ['false', 'redaction']
      default: redaction
    - name: years
      value: {{ years }}
      description: |
        Number of years to register (1–10). If omitted, defaults to the minimum registration period required by the registry for this extension. For most extensions this is 1 year, but some extensions require longer minimum terms (e.g., \`.ai\` requires a minimum of 2 years). The registry for each extension may also enforce its own maximum registration term. If the requested value exceeds the registry's maximum, the registration will be rejected. When in doubt, use the default by omitting this field.
    - name: Prefer
      value: "{{ Prefer }}"
      description: Set to \`respond-async\` to receive an immediate \`202 Accepted\` without waiting for the operation to complete (RFC 7240). The header may be combined with other preferences using standard comma-separated syntax.
      description: Set to \`respond-async\` to receive an immediate \`202 Accepted\` without waiting for the operation to complete (RFC 7240). The header may be combined with other preferences using standard comma-separated syntax.
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

Updates an existing domain registration. By default, the server holds the connection for a bounded, server-defined amount of time while the update completes. Most updates finish within this window and return `200 OK` with a completed workflow status. If the update is still processing after this synchronous wait window, the server returns `202 Accepted`. Poll the URL in `links.self` to track progress. To skip the wait and receive an immediate `202`, send `Prefer: respond-async`. This endpoint currently supports updating `auto_renew` only.

```sql
UPDATE cloudflare.registrar.registrations
SET 
auto_renew = {{ auto_renew }}
WHERE 
account_id = '{{ account_id }}' --required
AND domain_name = '{{ domain_name }}' --required
AND Prefer = '{{ Prefer}}'
RETURNING
errors,
messages,
result,
success;
```
</TabItem>
</Tabs>
