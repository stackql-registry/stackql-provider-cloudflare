--- 
title: registrar
hide_title: false
hide_table_of_contents: false
keywords:
  - registrar
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

Creates, updates, deletes, gets or lists a <code>registrar</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registrar" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.registrar.registrar" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#create_domain_check"><CopyableCode code="create_domain_check" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-domains"><code>domains</code></a></td>
    <td></td>
    <td>Performs real-time, authoritative availability checks directly against domain registries. Use this endpoint to verify a domain is available before attempting registration via `POST /registrations`. **Important:** Unlike the Search endpoint, these results are authoritative and reflect current registry status. Always check availability immediately before registration as domain status can change rapidly. **Note:** This endpoint uses POST to accept a list of domains in the request body. It is a read-only operation — it does not create, modify, or reserve any domains. **Extension support:** Only domains on extensions supported for programmatic registration by this API can be registered. If you check a domain on an unsupported extension, the response will include `registrable: false` with a `reason` field explaining why: - `extension_not_supported_via_api` — Cloudflare Registrar supports this extension in the dashboard, but it is not yet available for programmatic registration via this API. Register via `https://dash.cloudflare.com/&#123;account_id&#125;/domains/registrations` instead. - `extension_not_supported` — This extension is not supported by Cloudflare Registrar. - `extension_disallows_registration` — The extension's registry has temporarily or permanently frozen new registrations. No registrar can register domains on this extension at this time. - `domain_premium` — The domain is premium priced. Premium registration is not currently supported by this API. - `domain_unavailable` — The domain is already registered, reserved, or otherwise not available for registration on a supported extension. The `reason` field is only present when `registrable` is `false`. **Behavior:** - Maximum 20 domains per request - Pricing is only returned for domains where `registrable: true` - Results are not cached; each request queries the registry **Workflow:** 1. Call this endpoint with domains the user wants to register. 2. For each domain where `registrable: true`, present pricing to the user. 3. If `tier: premium`, note that premium registration is not currently supported by this API and do not proceed to `POST /registrations`. 4. Proceed to `POST /registrations` only for supported non-premium domains.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="create_domain_check"
    values={[
        { label: 'create_domain_check', value: 'create_domain_check' }
    ]}
>
<TabItem value="create_domain_check">

Performs real-time, authoritative availability checks directly against domain registries. Use this endpoint to verify a domain is available before attempting registration via `POST /registrations`. **Important:** Unlike the Search endpoint, these results are authoritative and reflect current registry status. Always check availability immediately before registration as domain status can change rapidly. **Note:** This endpoint uses POST to accept a list of domains in the request body. It is a read-only operation — it does not create, modify, or reserve any domains. **Extension support:** Only domains on extensions supported for programmatic registration by this API can be registered. If you check a domain on an unsupported extension, the response will include `registrable: false` with a `reason` field explaining why: - `extension_not_supported_via_api` — Cloudflare Registrar supports this extension in the dashboard, but it is not yet available for programmatic registration via this API. Register via `https://dash.cloudflare.com/&#123;account_id&#125;/domains/registrations` instead. - `extension_not_supported` — This extension is not supported by Cloudflare Registrar. - `extension_disallows_registration` — The extension's registry has temporarily or permanently frozen new registrations. No registrar can register domains on this extension at this time. - `domain_premium` — The domain is premium priced. Premium registration is not currently supported by this API. - `domain_unavailable` — The domain is already registered, reserved, or otherwise not available for registration on a supported extension. The `reason` field is only present when `registrable` is `false`. **Behavior:** - Maximum 20 domains per request - Pricing is only returned for domains where `registrable: true` - Results are not cached; each request queries the registry **Workflow:** 1. Call this endpoint with domains the user wants to register. 2. For each domain where `registrable: true`, present pricing to the user. 3. If `tier: premium`, note that premium registration is not currently supported by this API and do not proceed to `POST /registrations`. 4. Proceed to `POST /registrations` only for supported non-premium domains.

```sql
EXEC cloudflare.registrar.registrar.create_domain_check 
@account_id='{{ account_id }}' --required 
@@json=
'{
"domains": "{{ domains }}"
}'
;
```
</TabItem>
</Tabs>
