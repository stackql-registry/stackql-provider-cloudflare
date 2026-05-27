--- 
title: domain_search
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_search
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

Creates, updates, deletes, gets or lists a <code>domain_search</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domain_search" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.registrar.domain_search" /></td></tr>
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

Successfully returned domain search results.

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The fully qualified domain name (FQDN) in punycode format for internationalized domain names (IDNs). (example: example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="pricing" /></td>
    <td><code>object</code></td>
    <td>Annual pricing information for a registrable domain. This object is only present when `registrable` is `true`. All prices are per year and returned as strings to preserve decimal precision. `registration_cost` and `renewal_cost` are frequently the same value, but may differ — especially for premium domains where registries set different rates for initial registration vs. renewal. For a multi-year registration (e.g., 4 years), the first year is charged at `registration_cost` and each subsequent year at `renewal_cost`. Registry pricing may change over time; the values returned here reflect the current registry rate. Premium pricing may be surfaced by Search and Check, but premium registration is not currently supported by this API.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>Present only when `registrable` is `false` on search results. Explains why the domain does not appear registrable through this API. These values are advisory; use POST /domain-check for authoritative status. - `extension_not_supported_via_api`: Cloudflare Registrar supports this extension in the dashboard but it is not yet available for programmatic registration via this API. - `extension_not_supported`: This extension is not supported by Cloudflare Registrar at all. - `extension_disallows_registration`: The extension's registry has temporarily or permanently frozen new registrations. - `domain_premium`: The domain is premium priced. Premium registration is not currently supported by this API. - `domain_unavailable`: The domain appears unavailable. (extension_not_supported_via_api, extension_not_supported, extension_disallows_registration, domain_premium, domain_unavailable) (example: domain_unavailable)</td>
</tr>
<tr>
    <td><CopyableCode code="registrable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this domain appears available based on search data. Search results are non-authoritative and may be stale. - `true`: The domain appears available. Use POST /domain-check to confirm before registration. - `false`: The domain does not appear available in search results.</td>
</tr>
<tr>
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>The pricing tier for this domain. Always present when `registrable` is `true`; defaults to `standard` for most domains. May be absent when `registrable` is `false`. - `standard`: Standard registry pricing - `premium`: Premium domain with higher pricing set by the registry (standard, premium) (example: standard)</td>
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
    <td><a href="#parameter-q"><code>q</code></a>, <a href="#parameter-extensions"><code>extensions</code></a>, <a href="#parameter-limit"><code>limit</code></a></td>
    <td>Searches for domain name suggestions based on a keyword, phrase, or partial domain name. Returns a list of potentially available domains with pricing information. **Important:** Results are non-authoritative and based on cached data. Always use the `/domain-check` endpoint to verify real-time availability before attempting registration. Suggestions are scoped to extensions supported for programmatic registration via this API (`POST /registrations`). Domains on unsupported extensions will not appear in results, even if they are available at the registry level. **Use cases:** - Brand name discovery (e.g., "acme corp" → acmecorp.com, acmecorp.dev) - Keyword-based suggestions (e.g., "coffee shop" → coffeeshop.com, mycoffeeshop.net) - Alternative extension discovery (e.g., "example.com" → example.com, example.app, example.xyz) **Workflow:** 1. Call this endpoint with a keyword or domain name. 2. Present suggestions to the user. 3. Call `/domain-check` with the user's chosen domains to confirm real-time availability and pricing. 4. Proceed to `POST /registrations` only for supported non-premium domains where the Check response returns `registrable: true`. **Note:** Searching with just a domain extension (e.g., "com" or ".app") is not supported. Provide a keyword or domain name.</td>
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
<tr id="parameter-extensions">
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>Limits results to specific domain extensions from the supported set. If not specified, returns results across all supported extensions. Extensions not in the supported set are silently ignored.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of domain suggestions to return. Defaults to 20 if not specified.</td>
</tr>
<tr id="parameter-q">
    <td><CopyableCode code="q" /></td>
    <td><code>string</code></td>
    <td>The search term to find domain suggestions. Accepts keywords, phrases, or full domain names. - Phrases: "coffee shop" returns coffeeshop.com, mycoffeeshop.net, etc. - Domain names: "example.com" returns example.com and variations across extensions</td>
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

Searches for domain name suggestions based on a keyword, phrase, or partial domain name. Returns a list of potentially available domains with pricing information. **Important:** Results are non-authoritative and based on cached data. Always use the `/domain-check` endpoint to verify real-time availability before attempting registration. Suggestions are scoped to extensions supported for programmatic registration via this API (`POST /registrations`). Domains on unsupported extensions will not appear in results, even if they are available at the registry level. **Use cases:** - Brand name discovery (e.g., "acme corp" → acmecorp.com, acmecorp.dev) - Keyword-based suggestions (e.g., "coffee shop" → coffeeshop.com, mycoffeeshop.net) - Alternative extension discovery (e.g., "example.com" → example.com, example.app, example.xyz) **Workflow:** 1. Call this endpoint with a keyword or domain name. 2. Present suggestions to the user. 3. Call `/domain-check` with the user's chosen domains to confirm real-time availability and pricing. 4. Proceed to `POST /registrations` only for supported non-premium domains where the Check response returns `registrable: true`. **Note:** Searching with just a domain extension (e.g., "com" or ".app") is not supported. Provide a keyword or domain name.

```sql
SELECT
name,
pricing,
reason,
registrable,
tier
FROM cloudflare.registrar.domain_search
WHERE account_id = '{{ account_id }}' -- required
AND q = '{{ q }}'
AND extensions = '{{ extensions }}'
AND limit = '{{ limit }}'
;
```
</TabItem>
</Tabs>
