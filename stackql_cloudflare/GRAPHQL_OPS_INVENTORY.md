# Cloudflare GraphQL Operations - Candidate Inventory

Source: introspected GraphQL schema mirror at https://pages.johnspurlock.com/graphql-schema-docs/cloudflare.html
(third-party introspection; for canonical use, run live introspection against `https://api.cloudflare.com/client/v4/graphql`).

All operations are SELECT-only - Cloudflare GraphQL API supports no mutations.
Pagination is filter-comparator keyset-based (not cursor / not offset); the any-sdk GraphQL reader GitHub-style `after:` cursor mechanism does not apply, so initial operations should run single-page.

**Totals:** 53 zone-scoped + 198 account-scoped = 251 candidate operations.

Tick the boxes next to the operations you want to ship in this PR. The "suggested service" column shows where each would land in the existing stackql provider service tree - adjust if needed.

## Zone-scoped (queried under `viewer.zones[*]`)

Required path-param: `zone_tag` (the Cloudflare zone ID).

### `cloudflare.api_gateway` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `apiGatewayGraphqlQueryAnalyticsGroups` | GraphQL query attributes and trends | `cloudflare.api_gateway.zone_api_gateway_graphql_query_analytics_groups` |
| [ ] | `apiGatewayMatchedSessionIDsAdaptiveGroups` | Beta. Aggregated count of Session Identifier matches | `cloudflare.api_gateway.zone_api_gateway_matched_session_i_ds_adaptive_groups` |
| [ ] | `apiGatewayMatchedSessionIDsPerEndpointAdaptiveGroups` | Beta. Aggregated count of Session Identifier matches per endpoint | `cloudflare.api_gateway.zone_api_gateway_matched_session_i_ds_per_endpoint_adaptive_groups` |
| [ ] | `apiGatewayMatchedSessionIDsPerEndpointFlattenedAdaptiveGroups` | Beta. Aggregated count of Session Identifier matches | `cloudflare.api_gateway.zone_api_gateway_matched_session_i_ds_per_endpoint_flattened_adaptive_groups` |
| [ ] | `apiRequestSequencesGroups` | Sequences of API endpoint operations. Sequences are learned by grouping requests by AuthID. Correlat... | `cloudflare.api_gateway.zone_api_request_sequences_groups` |

### `cloudflare.cache` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `cacheReserveOperationsAdaptiveGroups` | Beta. Cache Reserve operations with adaptive sampling | `cloudflare.cache.zone_cache_reserve_operations_adaptive_groups` |
| [ ] | `cacheReserveRequestsAdaptiveGroups` | Cache Reserve HTTP requests data with adaptive sampling | `cloudflare.cache.zone_cache_reserve_requests_adaptive_groups` |
| [ ] | `cacheReserveStorageAdaptiveGroups` | Beta. Cache Reserve storage with adaptive sampling | `cloudflare.cache.zone_cache_reserve_storage_adaptive_groups` |

### `cloudflare.dns` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `dnsAnalyticsAdaptive` | Analytics data for DNS queries | `cloudflare.dns.zone_dns_analytics_adaptive` |
| [ ] | `dnsAnalyticsAdaptiveGroups` | Analytics data for DNS queries | `cloudflare.dns.zone_dns_analytics_adaptive_groups` |

### `cloudflare.email_routing` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `emailRoutingAdaptive` | Beta. Raw email routing logs with adaptive sampling | `cloudflare.email_routing.zone_email_routing_adaptive` |
| [ ] | `emailRoutingAdaptiveGroups` | Beta. Aggregated email routing logs with adaptive sampling | `cloudflare.email_routing.zone_email_routing_adaptive_groups` |

### `cloudflare.email_security` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `dmarcReportsAdaptive` | Dmarc report records with adaptive sampling | `cloudflare.email_security.zone_dmarc_reports_adaptive` |
| [ ] | `dmarcReportsSourcesAdaptiveGroups` | Aggregated dmarc reports by sources logs with adaptive sampling | `cloudflare.email_security.zone_dmarc_reports_sources_adaptive_groups` |

### `cloudflare.email_sending` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `emailSendingAdaptive` | Raw email sending logs with adaptive sampling | `cloudflare.email_sending.zone_email_sending_adaptive` |
| [ ] | `emailSendingAdaptiveGroups` | Aggregated email sending logs with adaptive sampling | `cloudflare.email_sending.zone_email_sending_adaptive_groups` |

### `cloudflare.firewall` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `firewallEventsAdaptive` | Raw Firewall events with adaptive sampling | `cloudflare.firewall.zone_firewall_events_adaptive` |
| [ ] | `firewallEventsAdaptiveByTimeGroups` | Aggregated Firewall events with adaptive sampling grouped by time | `cloudflare.firewall.zone_firewall_events_adaptive_by_time_groups` |
| [ ] | `firewallEventsAdaptiveGroups` | Aggregated Firewall events with adaptive sampling | `cloudflare.firewall.zone_firewall_events_adaptive_groups` |

### `cloudflare.healthchecks` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `healthCheckEventsAdaptive` | Raw Health Check events with adaptive sampling | `cloudflare.healthchecks.zone_health_check_events_adaptive` |
| [ ] | `healthCheckEventsAdaptiveGroups` | Aggregated Health Check events with adaptive sampling | `cloudflare.healthchecks.zone_health_check_events_adaptive_groups` |

### `cloudflare.images` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `imageResizingRequests1mGroups` | Minutely rollups of Image Resizing requests | `cloudflare.images.zone_image_resizing_requests1m_groups` |

### `cloudflare.load_balancers` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `loadBalancingRequestsAdaptive` | Raw Load Balancing origin requests with adaptive sampling | `cloudflare.load_balancers.zone_load_balancing_requests_adaptive` |
| [ ] | `loadBalancingRequestsAdaptiveGroups` | Aggregated Load Balancing origin requests with adaptive sampling | `cloudflare.load_balancers.zone_load_balancing_requests_adaptive_groups` |

### `cloudflare.logpush` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `logpushHealthAdaptiveGroups` | Beta. Logpush job health metrics | `cloudflare.logpush.zone_logpush_health_adaptive_groups` |
| [ ] | `logpushTransformersAdaptiveGroups` | Beta. Logpush transformer health metrics | `cloudflare.logpush.zone_logpush_transformers_adaptive_groups` |

### `cloudflare.page_shield` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `pageShieldReportsAdaptiveGroups` | Page Shield CSP reports | `cloudflare.page_shield.zone_page_shield_reports_adaptive_groups` |

### `cloudflare.rum` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `nelReportsAdaptiveGroups` | Data to visualize network error logs | `cloudflare.rum.zone_nel_reports_adaptive_groups` |
| [ ] | `userProfilesAdaptiveGroups` | User ID profiles for login and sign up attempts | `cloudflare.rum.zone_user_profiles_adaptive_groups` |
| [ ] | `userProfilesRawEventsGroups` | Historical login and signup events per user. | `cloudflare.rum.zone_user_profiles_raw_events_groups` |

### `cloudflare.waiting_rooms` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `waitingRoomAnalyticsAdaptive` | Raw Waiting Room analytics logs | `cloudflare.waiting_rooms.zone_waiting_room_analytics_adaptive` |
| [ ] | `waitingRoomAnalyticsAdaptiveGroups` | Aggregated Waiting Room analytics logs with adaptive sampling | `cloudflare.waiting_rooms.zone_waiting_room_analytics_adaptive_groups` |

### `cloudflare.workers` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `workersZoneInvocationsAdaptiveGroups` | Workers invocations with adaptive sampling | `cloudflare.workers.zone_workers_zone_invocations_adaptive_groups` |
| [ ] | `workersZoneSubrequestsAdaptiveGroups` | Workers subrequests with adaptive sampling | `cloudflare.workers.zone_workers_zone_subrequests_adaptive_groups` |

### `cloudflare.zaraz` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `zarazActionsAdaptiveGroups` | Zaraz Actions Analytics | `cloudflare.zaraz.zone_zaraz_actions_adaptive_groups` |
| [ ] | `zarazAnalyticsIdentitiesAdaptiveGroups` | Zaraz Analytics Identities - zaraz.identify calls | `cloudflare.zaraz.zone_zaraz_analytics_identities_adaptive_groups` |
| [ ] | `zarazAnalyticsOrderedTrackAdaptive` | Zaraz Analytics Tracks ordered per session | `cloudflare.zaraz.zone_zaraz_analytics_ordered_track_adaptive` |
| [ ] | `zarazAnalyticsOrderedTrackAdaptiveGroups` | Zaraz Analytics Tracks ordered per session | `cloudflare.zaraz.zone_zaraz_analytics_ordered_track_adaptive_groups` |
| [ ] | `zarazAnalyticsTrackAdaptiveGroups` | Zaraz Analytics Track - counts zaraz.track calls | `cloudflare.zaraz.zone_zaraz_analytics_track_adaptive_groups` |
| [ ] | `zarazAnalyticsTrackTrafficSourcesAdaptiveGroups` | Zaraz Analytics Track Traffic Sources | `cloudflare.zaraz.zone_zaraz_analytics_track_traffic_sources_adaptive_groups` |
| [ ] | `zarazAnalyticsTriggersAdaptiveGroups` | Zaraz Analytics Triggers (a trigger is a set of rules that can trigger a zaraz action) | `cloudflare.zaraz.zone_zaraz_analytics_triggers_adaptive_groups` |
| [ ] | `zarazAnalyticsTriggersTrafficSourcesAdaptiveGroups` | Zaraz Analytics Triggers Traffic Sources | `cloudflare.zaraz.zone_zaraz_analytics_triggers_traffic_sources_adaptive_groups` |
| [ ] | `zarazFetchAdaptiveGroups` | Aggregated Zaraz External Fetch Logs | `cloudflare.zaraz.zone_zaraz_fetch_adaptive_groups` |
| [ ] | `zarazTrackAdaptiveGroups` | Zaraz Track Analytics - counts zaraz.track calls | `cloudflare.zaraz.zone_zaraz_track_adaptive_groups` |
| [ ] | `zarazTriggersAdaptiveGroups` | Zaraz Triggers Analytics (a trigger is a set of rules that can trigger a zaraz action) | `cloudflare.zaraz.zone_zaraz_triggers_adaptive_groups` |

### `cloudflare.zones` (zone-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `httpRequests1dByColoGroups` |  | `cloudflare.zones.zone_http_requests1d_by_colo_groups` |
| [ ] | `httpRequests1dGroups` | Daily rollups of request data | `cloudflare.zones.zone_http_requests1d_groups` |
| [ ] | `httpRequests1hGroups` | Hourly rollups of request data | `cloudflare.zones.zone_http_requests1h_groups` |
| [ ] | `httpRequests1mByColoGroups` |  | `cloudflare.zones.zone_http_requests1m_by_colo_groups` |
| [ ] | `httpRequests1mGroups` | Minutely rollups of request data | `cloudflare.zones.zone_http_requests1m_groups` |
| [ ] | `httpRequestsAdaptive` | Raw HTTP requests with adaptive sampling | `cloudflare.zones.zone_http_requests_adaptive` |
| [ ] | `httpRequestsAdaptiveGroups` | Aggregated HTTP requests data with adaptive sampling | `cloudflare.zones.zone_http_requests_adaptive_groups` |
| [ ] | `httpRequestsOverviewAdaptiveGroups` | A high-level summary of HTTP requests made by end users. | `cloudflare.zones.zone_http_requests_overview_adaptive_groups` |

## Account-scoped (queried under `viewer.accounts[*]`)

Required path-param: `account_tag` (the Cloudflare account ID).

### `cloudflare.addressing` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `aegisIpUtilizationAdaptiveGroups` | Beta. Aegis IP utilization metrics | `cloudflare.addressing.account_aegis_ip_utilization_adaptive_groups` |

### `cloudflare.ai` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `aiInferenceAdaptive` | AI Inference logs with adaptive sampling | `cloudflare.ai.account_ai_inference_adaptive` |
| [ ] | `aiInferenceAdaptiveGroups` | Aggregated AI Inference logs with adaptive sampling | `cloudflare.ai.account_ai_inference_adaptive_groups` |
| [ ] | `autoRAGConfigAPIAdaptiveGroups` | AutoRAG Config API Search Analytics | `cloudflare.ai.account_auto_r_a_g_config_a_p_i_adaptive_groups` |
| [ ] | `autoRAGEngineAdaptiveGroups` | AutoRAG Engine Ingestion Analytics | `cloudflare.ai.account_auto_r_a_g_engine_adaptive_groups` |
| [ ] | `toMarkdownConversionAdaptive` | Markdown Conversion Metrics | `cloudflare.ai.account_to_markdown_conversion_adaptive` |
| [ ] | `toMarkdownConversionAdaptiveGroups` | Markdown Conversion Metrics | `cloudflare.ai.account_to_markdown_conversion_adaptive_groups` |

### `cloudflare.ai_gateway` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `aiGatewayCacheAdaptiveGroups` | AI Gateway Cache | `cloudflare.ai_gateway.account_ai_gateway_cache_adaptive_groups` |
| [ ] | `aiGatewayErrorsAdaptiveGroups` | AI Gateway Errors | `cloudflare.ai_gateway.account_ai_gateway_errors_adaptive_groups` |
| [ ] | `aiGatewayRequestsAdaptiveGroups` | AI Gateway Requests | `cloudflare.ai_gateway.account_ai_gateway_requests_adaptive_groups` |
| [ ] | `aiGatewaySizeAdaptiveGroups` | AI Gateway Stored Rows | `cloudflare.ai_gateway.account_ai_gateway_size_adaptive_groups` |

### `cloudflare.aisearch` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `aiSearchAPIAdaptiveGroups` | AI Search API Search Analytics | `cloudflare.aisearch.account_ai_search_a_p_i_adaptive_groups` |
| [ ] | `aiSearchIngestedItemsAdaptiveGroups` | AI Search Ingested Items Analytics | `cloudflare.aisearch.account_ai_search_ingested_items_adaptive_groups` |

### `cloudflare.browser_rendering` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `browserRenderingApiAdaptive` | Browser Rendering API events with adaptive sampling | `cloudflare.browser_rendering.account_browser_rendering_api_adaptive` |
| [ ] | `browserRenderingApiAdaptiveGroups` | Aggregated Browser Rendering API events with adaptive sampling | `cloudflare.browser_rendering.account_browser_rendering_api_adaptive_groups` |
| [ ] | `browserRenderingBindingSessionsAdaptiveGroups` | Aggregated Browser Rendering worker binding sessions with adaptive sampling | `cloudflare.browser_rendering.account_browser_rendering_binding_sessions_adaptive_groups` |
| [ ] | `browserRenderingBrowserTimeUsageAdaptiveGroups` | Aggregated Browser Rendering and Browser Rendering REST API browser sessions with adaptive sampling | `cloudflare.browser_rendering.account_browser_rendering_browser_time_usage_adaptive_groups` |
| [ ] | `browserRenderingEventsAdaptive` | Browser Rendering events with adaptive sampling | `cloudflare.browser_rendering.account_browser_rendering_events_adaptive` |
| [ ] | `browserRenderingEventsAdaptiveGroups` | Aggregated Browser Rendering events with adaptive sampling | `cloudflare.browser_rendering.account_browser_rendering_events_adaptive_groups` |

### `cloudflare.cache` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `cdnNetworkAnalyticsAdaptiveGroups` | Network analytics data for Cloudflare CDN traffic | `cloudflare.cache.account_cdn_network_analytics_adaptive_groups` |

### `cloudflare.calls` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `callsStatusAdaptive` | (TESTING ONLY, NOT FOR PRODUCTION) Raw Calls events with adaptive sampling | `cloudflare.calls.account_calls_status_adaptive` |
| [ ] | `callsTurnUsageAdaptiveGroups` | Aggregated Calls TURN bandwidth usage with adaptive sampling" | `cloudflare.calls.account_calls_turn_usage_adaptive_groups` |
| [ ] | `callsUsageAdaptiveGroups` | Beta. Aggregated Calls SFU bandwidth usage with adaptive sampling | `cloudflare.calls.account_calls_usage_adaptive_groups` |

### `cloudflare.cloudforce_one` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `cloudforceOneDetectionsAdaptiveGroups` | Cloudforce One detection events for Workers for Platforms scripts with adaptive sampling. Each row r... | `cloudflare.cloudforce_one.account_cloudforce_one_detections_adaptive_groups` |
| [ ] | `cloudforceOneDetectionsStagingAdaptiveGroups` | Cloudforce One detection events for Workers for Platforms scripts with adaptive sampling (staging). ... | `cloudflare.cloudforce_one.account_cloudforce_one_detections_staging_adaptive_groups` |

### `cloudflare.connectivity` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `cloudflareTunnelsAnalyticsAdaptiveGroups` | Cloudflare tunnel Device Analytics | `cloudflare.connectivity.account_cloudflare_tunnels_analytics_adaptive_groups` |

### `cloudflare.d1` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `d1AnalyticsAdaptiveGroups` | Aggregated D1 analytics with adaptive sampling | `cloudflare.d1.account_d1_analytics_adaptive_groups` |
| [ ] | `d1QueriesAdaptiveGroups` | D1 query metrics with adaptive sampling | `cloudflare.d1.account_d1_queries_adaptive_groups` |
| [ ] | `d1StorageAdaptiveGroups` | D1 storage with adaptive sampling | `cloudflare.d1.account_d1_storage_adaptive_groups` |

### `cloudflare.ddos_protection` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `advancedDnsProtectionNetworkAnalyticsAdaptiveGroups` | Network analytics data for Advanced DNS Protection | `cloudflare.ddos_protection.account_advanced_dns_protection_network_analytics_adaptive_groups` |
| [ ] | `advancedTcpProtectionNetworkAnalyticsAdaptiveGroups` |  | `cloudflare.ddos_protection.account_advanced_tcp_protection_network_analytics_adaptive_groups` |
| [ ] | `dosdAttackAnalyticsGroups` | Attack analytics metadata for attacks detected by dosd | `cloudflare.ddos_protection.account_dosd_attack_analytics_groups` |
| [ ] | `dosdNetworkAnalyticsAdaptiveGroups` | Network analytics data for dosd | `cloudflare.ddos_protection.account_dosd_network_analytics_adaptive_groups` |
| [ ] | `fbmAttackAnalyticsGroups` | FBM analytics metadata for attacks detected by dosd | `cloudflare.ddos_protection.account_fbm_attack_analytics_groups` |
| [ ] | `flowtrackdNetworkAnalyticsAdaptiveGroups` |  | `cloudflare.ddos_protection.account_flowtrackd_network_analytics_adaptive_groups` |
| [ ] | `programmableFlowProtectionNetworkAnalyticsAdaptiveGroups` | Network analytics data for Programmable Flow Protection | `cloudflare.ddos_protection.account_programmable_flow_protection_network_analytics_adaptive_groups` |
| [ ] | `sinkholeRequestLogsAdaptive` | Sinkhole Request Logs | `cloudflare.ddos_protection.account_sinkhole_request_logs_adaptive` |
| [ ] | `sinkholeRequestLogsAdaptiveGroups` | Sinkhole Request Logs | `cloudflare.ddos_protection.account_sinkhole_request_logs_adaptive_groups` |

### `cloudflare.dns` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `dnsAnalyticsAdaptive` | Analytics data for DNS queries | `cloudflare.dns.account_dns_analytics_adaptive` |
| [ ] | `dnsAnalyticsAdaptiveGroups` | Analytics data for DNS queries | `cloudflare.dns.account_dns_analytics_adaptive_groups` |

### `cloudflare.dns_firewall` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `dnsFirewallAnalyticsAdaptive` | Analytics data for DNS Firewall queries | `cloudflare.dns_firewall.account_dns_firewall_analytics_adaptive` |
| [ ] | `dnsFirewallAnalyticsAdaptiveGroups` | Analytics data for DNS Firewall queries | `cloudflare.dns_firewall.account_dns_firewall_analytics_adaptive_groups` |

### `cloudflare.durable_objects` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `durableObjectsInvocationsAdaptiveGroups` | Durable Objects invocations with adaptive sampling | `cloudflare.durable_objects.account_durable_objects_invocations_adaptive_groups` |
| [ ] | `durableObjectsPeriodicGroups` | Durable Objects periodic metrics | `cloudflare.durable_objects.account_durable_objects_periodic_groups` |
| [ ] | `durableObjectsSqlStorageGroups` | Storage metrics for SQL-backed Durable Objects. | `cloudflare.durable_objects.account_durable_objects_sql_storage_groups` |
| [ ] | `durableObjectsStorageGroups` | Durable Objects storage metrics | `cloudflare.durable_objects.account_durable_objects_storage_groups` |
| [ ] | `durableObjectsSubrequestsAdaptiveGroups` | Durable Objects subrequests with adaptive sampling | `cloudflare.durable_objects.account_durable_objects_subrequests_adaptive_groups` |

### `cloudflare.firewall` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `firewallEventsAdaptive` | Raw Firewall events with adaptive sampling | `cloudflare.firewall.account_firewall_events_adaptive` |
| [ ] | `firewallEventsAdaptiveGroups` | Aggregated Firewall events with adaptive sampling | `cloudflare.firewall.account_firewall_events_adaptive_groups` |

### `cloudflare.hyperdrive` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `hyperdrivePoolSizesAdaptiveGroups` | Hyperdrive connection pool size snapshots with adaptive sampling. | `cloudflare.hyperdrive.account_hyperdrive_pool_sizes_adaptive_groups` |
| [ ] | `hyperdriveQueriesAdaptiveGroups` | Hyperdrive query events with adaptive sampling. | `cloudflare.hyperdrive.account_hyperdrive_queries_adaptive_groups` |

### `cloudflare.images` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `imagesRequestsAdaptiveGroups` | A high-level summary of Cloudflare Images served to end users. | `cloudflare.images.account_images_requests_adaptive_groups` |
| [ ] | `imagesUniqueTransformations` | Image unique transfromations per day | `cloudflare.images.account_images_unique_transformations` |
| [ ] | `imagesUniqueTransformationsAccumulatedSinceStartOfMonth` | Image unique transformations accumulated since start of month | `cloudflare.images.account_images_unique_transformations_accumulated_since_start_of_month` |

### `cloudflare.kv` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `kvOperationsAdaptiveGroups` | KV operations data with adaptive sampling | `cloudflare.kv.account_kv_operations_adaptive_groups` |
| [ ] | `kvStorageAdaptiveGroups` | KV stored data with adaptive sampling | `cloudflare.kv.account_kv_storage_adaptive_groups` |

### `cloudflare.logpush` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `logpushHealthAdaptiveGroups` | Beta. Logpush job health metrics | `cloudflare.logpush.account_logpush_health_adaptive_groups` |
| [ ] | `logpushTransformersAdaptiveGroups` | Beta. Logpush transformer health metrics | `cloudflare.logpush.account_logpush_transformers_adaptive_groups` |

### `cloudflare.logs` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `artifactsEventsAdaptiveGroups` | Artifacts events with adaptive sampling | `cloudflare.logs.account_artifacts_events_adaptive_groups` |
| [ ] | `logExplorerIngestionAdaptiveGroups` | Ingestion metrics for Log Explorer | `cloudflare.logs.account_log_explorer_ingestion_adaptive_groups` |
| [ ] | `storageTraces` | Storage Tracing Information | `cloudflare.logs.account_storage_traces` |

### `cloudflare.magic_cloud_networking` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `mconnTelemetryEventsAdaptiveGroups` | Aggregated Magic WAN Connector events with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_events_adaptive_groups` |
| [ ] | `mconnTelemetryEventsStagingAdaptiveGroups` | Aggregated Magic WAN Connector events with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_events_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotDhcpLeasesAdaptiveGroups` | Aggregated Magic WAN Connector snapshots of DHCP leases with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_dhcp_leases_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotDhcpLeasesStagingAdaptiveGroups` | Aggregated Magic WAN Connector snapshots of DHCP leases with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_dhcp_leases_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotDisksAdaptiveGroups` | Aggregated Magic WAN Connector disk snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_disks_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotDisksStagingAdaptiveGroups` | Aggregated Magic WAN Connector disk snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_disks_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotInterfaceAddressesAdaptiveGroups` | Aggregated Magic WAN Connector interface address snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_interface_addresses_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotInterfaceAddressesStagingAdaptiveGroups` | Aggregated Magic WAN Connector interface address snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_interface_addresses_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotInterfacesAdaptiveGroups` | Aggregated Magic WAN Connector interface snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_interfaces_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotInterfacesStagingAdaptiveGroups` | Aggregated Magic WAN Connector interface snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_interfaces_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotMountsAdaptiveGroups` | Aggregated Magic WAN Connector mount snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_mounts_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotMountsStagingAdaptiveGroups` | Aggregated Magic WAN Connector mount snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_mounts_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotNetdevsAdaptiveGroups` | Aggregated Magic WAN Connector netdev snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_netdevs_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotNetdevsStagingAdaptiveGroups` | Aggregated Magic WAN Connector netdev snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_netdevs_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotThermalsAdaptiveGroups` | Aggregated Magic WAN Connector thermal snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_thermals_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotThermalsStagingAdaptiveGroups` | Aggregated Magic WAN Connector thermal snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_thermals_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotTunnelsAdaptiveGroups` | Aggregated Magic WAN Connector tunnel snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_tunnels_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotTunnelsStagingAdaptiveGroups` | Aggregated Magic WAN Connector tunnel snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshot_tunnels_staging_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotsAdaptiveGroups` | Aggregated Magic WAN Connector system snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshots_adaptive_groups` |
| [ ] | `mconnTelemetrySnapshotsStagingAdaptiveGroups` | Aggregated Magic WAN Connector system snapshots with adaptive sampling | `cloudflare.magic_cloud_networking.account_mconn_telemetry_snapshots_staging_adaptive_groups` |

### `cloudflare.magic_network_monitoring` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `mnmAWSVPCFlowDataAdaptiveGroups` | AWS VPC Flow data collected through Magic Network Monitoring | `cloudflare.magic_network_monitoring.account_mnm_a_w_s_v_p_c_flow_data_adaptive_groups` |
| [ ] | `mnmFlowDataAdaptiveGroups` | Flow data collected through Magic Network Monitoring | `cloudflare.magic_network_monitoring.account_mnm_flow_data_adaptive_groups` |

### `cloudflare.magic_transit` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `MagicWANConnectorMetricsAdaptiveGroups` |  | `cloudflare.magic_transit.account_magic_w_a_n_connector_metrics_adaptive_groups` |
| [ ] | `magicEndpointHealthCheckAdaptiveGroups` | Magic Endpoint Healthcheck events with adaptive sampling. | `cloudflare.magic_transit.account_magic_endpoint_health_check_adaptive_groups` |
| [ ] | `magicFirewallNetworkAnalyticsAdaptiveGroups` | Network analytics data for Magic Firewall | `cloudflare.magic_transit.account_magic_firewall_network_analytics_adaptive_groups` |
| [ ] | `magicFirewallRateLimitNetworkAnalyticsAdaptiveGroups` | Network analytics data for Magic Firewall Ratelimiting | `cloudflare.magic_transit.account_magic_firewall_rate_limit_network_analytics_adaptive_groups` |
| [ ] | `magicFirewallSamplesAdaptiveGroups` | Data to visualize traffic allowed and blocked by Magic Firewall rules | `cloudflare.magic_transit.account_magic_firewall_samples_adaptive_groups` |
| [ ] | `magicIDPSNetworkAnalyticsAdaptiveGroups` | Network analytics data for Magic IDS | `cloudflare.magic_transit.account_magic_i_d_p_s_network_analytics_adaptive_groups` |
| [ ] | `magicTransitNetworkAnalyticsAdaptiveGroups` | Network analytics data for Magic Transit traffic | `cloudflare.magic_transit.account_magic_transit_network_analytics_adaptive_groups` |
| [ ] | `magicTransitTunnelHealthCheckSLOsAdaptiveGroups` | Magic Transit Tunnel Health Check SLO events with adaptive sampling. | `cloudflare.magic_transit.account_magic_transit_tunnel_health_check_s_l_os_adaptive_groups` |
| [ ] | `magicTransitTunnelHealthChecksAdaptiveGroups` | Beta. Magic Transit Health check results for customer GRE Tunnels with adaptive sampling (ABR). | `cloudflare.magic_transit.account_magic_transit_tunnel_health_checks_adaptive_groups` |
| [ ] | `magicTransitTunnelTrafficAdaptiveGroups` | Bandwidth usage metric of a Magic Transit tunnel. | `cloudflare.magic_transit.account_magic_transit_tunnel_traffic_adaptive_groups` |

### `cloudflare.page_shield` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `pageShieldReportsAdaptiveGroups` | Page Shield CSP reports | `cloudflare.page_shield.account_page_shield_reports_adaptive_groups` |

### `cloudflare.pages` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `pagesFunctionsInvocationsAdaptiveGroups` | Pages Functions invocations with adaptive sampling | `cloudflare.pages.account_pages_functions_invocations_adaptive_groups` |

### `cloudflare.pipelines` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `pipelinesDeliveryAdaptiveGroups` | Beta. Data delivered via Workers Pipelines | `cloudflare.pipelines.account_pipelines_delivery_adaptive_groups` |
| [ ] | `pipelinesIngestionAdaptiveGroups` | Beta. Data ingested via Workers Pipelines | `cloudflare.pipelines.account_pipelines_ingestion_adaptive_groups` |
| [ ] | `pipelinesOperatorAdaptiveGroups` | Aggregated Pipelines source metrics with adaptive sampling | `cloudflare.pipelines.account_pipelines_operator_adaptive_groups` |
| [ ] | `pipelinesOperatorStagingAdaptiveGroups` | Aggregated Pipelines source metrics with adaptive sampling | `cloudflare.pipelines.account_pipelines_operator_staging_adaptive_groups` |
| [ ] | `pipelinesSinkAdaptiveGroups` | Aggregated Pipelines sink metrics with adaptive sampling | `cloudflare.pipelines.account_pipelines_sink_adaptive_groups` |
| [ ] | `pipelinesSinkStagingAdaptiveGroups` | Aggregated Pipelines sink metrics with adaptive sampling | `cloudflare.pipelines.account_pipelines_sink_staging_adaptive_groups` |
| [ ] | `pipelinesUserErrorsAdaptive` | Raw user errors from Workers Pipelines | `cloudflare.pipelines.account_pipelines_user_errors_adaptive` |
| [ ] | `pipelinesUserErrorsAdaptiveGroups` | User errors from Workers Pipelines | `cloudflare.pipelines.account_pipelines_user_errors_adaptive_groups` |
| [ ] | `pipelinesUserErrorsStagingAdaptive` | Raw user errors from Workers Pipelines (staging) | `cloudflare.pipelines.account_pipelines_user_errors_staging_adaptive` |
| [ ] | `pipelinesUserErrorsStagingAdaptiveGroups` | User errors from Workers Pipelines (staging) | `cloudflare.pipelines.account_pipelines_user_errors_staging_adaptive_groups` |

### `cloudflare.queues` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `queueBacklogAdaptiveGroups` | Beta. Queue backlog data with adaptive sampling. Queues that are not being written to, or read from,... | `cloudflare.queues.account_queue_backlog_adaptive_groups` |
| [ ] | `queueConsumerMetricsAdaptiveGroups` | Beta. Queue consumer metrics with adaptive sampling. Inactive queues will not return data. | `cloudflare.queues.account_queue_consumer_metrics_adaptive_groups` |
| [ ] | `queueDelayedBacklogAdaptiveGroups` | Beta. Queue delayed backlog data with adaptive sampling. Queues that are not being written to, or re... | `cloudflare.queues.account_queue_delayed_backlog_adaptive_groups` |
| [ ] | `queueMessageOperationsAdaptiveGroups` | Beta. Queue message operation data with adaptive sampling | `cloudflare.queues.account_queue_message_operations_adaptive_groups` |

### `cloudflare.r2` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `r2OperationsAdaptiveGroups` | Beta. R2 operations with adaptive sampling | `cloudflare.r2.account_r2_operations_adaptive_groups` |
| [ ] | `r2StorageAdaptiveGroups` | Beta. R2 storage with adaptive sampling | `cloudflare.r2.account_r2_storage_adaptive_groups` |
| [ ] | `sippyOperationsAdaptiveGroups` | Sippy operations with adaptive sampling | `cloudflare.r2.account_sippy_operations_adaptive_groups` |

### `cloudflare.r2_data_catalog` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `r2CatalogDataOperationsAdaptiveGroups` | R2 Data Catalog data plane operations (Iceberg REST API requests) with adaptive sampling | `cloudflare.r2_data_catalog.account_r2_catalog_data_operations_adaptive_groups` |
| [ ] | `r2CatalogTableMaintenanceAdaptiveGroups` | R2 Data Catalog table maintenance job metrics (compaction, snapshot expiration) with adaptive sampli... | `cloudflare.r2_data_catalog.account_r2_catalog_table_maintenance_adaptive_groups` |

### `cloudflare.realtime_kit` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `realtimeKitUsageAdaptiveGroups` | RealtimeKit usage metrics | `cloudflare.realtime_kit.account_realtime_kit_usage_adaptive_groups` |

### `cloudflare.rum` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `nelReportsAdaptiveGroups` | Data to visualize network error logs | `cloudflare.rum.account_nel_reports_adaptive_groups` |
| [ ] | `rumPageloadEventsAdaptiveGroups` | Beta. Aggregated RUM pageload event metrics with adaptive sampling | `cloudflare.rum.account_rum_pageload_events_adaptive_groups` |
| [ ] | `rumPerformanceEventsAdaptiveGroups` | Beta. Aggregated RUM performance event metrics with adaptive sampling | `cloudflare.rum.account_rum_performance_events_adaptive_groups` |
| [ ] | `rumWebVitalsEventsAdaptive` | Beta. RUM Web Vitals event metrics with adaptive sampling | `cloudflare.rum.account_rum_web_vitals_events_adaptive` |
| [ ] | `rumWebVitalsEventsAdaptiveGroups` | Beta. Aggregated RUM Web Vitals event metrics with adaptive sampling | `cloudflare.rum.account_rum_web_vitals_events_adaptive_groups` |

### `cloudflare.spectrum` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `spectrumNetworkAnalyticsAdaptiveGroups` | Network analytics data for Spectrum traffic | `cloudflare.spectrum.account_spectrum_network_analytics_adaptive_groups` |

### `cloudflare.streams` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `liveInputEventsAdaptive` | Live input events with adaptive sampling | `cloudflare.streams.account_live_input_events_adaptive` |
| [ ] | `liveInputEventsAdaptiveGroups` | Aggregated live input events with adaptive sampling | `cloudflare.streams.account_live_input_events_adaptive_groups` |
| [ ] | `mediaUniqueTransformations` | Media unique transfromations per day | `cloudflare.streams.account_media_unique_transformations` |
| [ ] | `mediaUniqueTransformationsAccumulatedSinceStartOfMonth` | Media unique transformations accumulated since start of month | `cloudflare.streams.account_media_unique_transformations_accumulated_since_start_of_month` |
| [ ] | `streamCMCDAdaptiveGroups` | Stream CMCD data | `cloudflare.streams.account_stream_c_m_c_d_adaptive_groups` |
| [ ] | `streamMinutesViewedAdaptiveGroups` | A high-level summary of Cloudflare Stream minutes viewed. | `cloudflare.streams.account_stream_minutes_viewed_adaptive_groups` |
| [ ] | `videoBufferEventsAdaptiveGroups` | Beta. Aggregated video streaming buffer event metrics with adaptive sampling | `cloudflare.streams.account_video_buffer_events_adaptive_groups` |
| [ ] | `videoPlaybackEventsAdaptiveGroups` | Beta. Aggregated video streaming playback event metrics with adaptive sampling | `cloudflare.streams.account_video_playback_events_adaptive_groups` |
| [ ] | `videoQualityEventsAdaptiveGroups` | Beta. Aggregated video streaming quality change event metrics with adaptive sampling | `cloudflare.streams.account_video_quality_events_adaptive_groups` |

### `cloudflare.turnstile` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `turnstileAdaptiveGroups` | Beta. Cloudflare Turnstile aggregated events with adaptive sampling | `cloudflare.turnstile.account_turnstile_adaptive_groups` |

### `cloudflare.uncategorized` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `flagshipFlagEvaluationsAdaptive` | Flagship feature flag evaluations with adaptive sampling. Each row represents an individual flag eva... | `cloudflare.uncategorized.account_flagship_flag_evaluations_adaptive` |
| [ ] | `flagshipFlagEvaluationsAdaptiveGroups` | Aggregated Flagship feature flag evaluations with adaptive sampling. Use this to build dashboards ov... | `cloudflare.uncategorized.account_flagship_flag_evaluations_adaptive_groups` |

### `cloudflare.vectorize` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `vectorizeQueriesAdaptiveGroups` | Beta. Vectorize usage with adaptive sampling | `cloudflare.vectorize.account_vectorize_queries_adaptive_groups` |
| [ ] | `vectorizeStorageAdaptiveGroups` | Beta. Vectorize storage with adaptive sampling | `cloudflare.vectorize.account_vectorize_storage_adaptive_groups` |
| [ ] | `vectorizeV2OperationsAdaptiveGroups` | Vectorize operations with adaptive sampling | `cloudflare.vectorize.account_vectorize_v2_operations_adaptive_groups` |
| [ ] | `vectorizeV2QueriesAdaptiveGroups` | Vectorize queries with adaptive sampling | `cloudflare.vectorize.account_vectorize_v2_queries_adaptive_groups` |
| [ ] | `vectorizeV2StorageAdaptiveGroups` | Vectorize storage with adaptive sampling | `cloudflare.vectorize.account_vectorize_v2_storage_adaptive_groups` |
| [ ] | `vectorizeV2WritesAdaptiveGroups` | Vectorize writes with adaptive sampling | `cloudflare.vectorize.account_vectorize_v2_writes_adaptive_groups` |

### `cloudflare.workers` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `cloudchamberMetricsAdaptiveGroups` | Metrics for Cloudchamber applications and deployments | `cloudflare.workers.account_cloudchamber_metrics_adaptive_groups` |
| [ ] | `containersMetricsAdaptiveGroups` | Metrics for Cloudchamber applications and deployments | `cloudflare.workers.account_containers_metrics_adaptive_groups` |
| [ ] | `containersUsageAdaptiveGroups` | Used to compute usage queries for billing estimates in Dash | `cloudflare.workers.account_containers_usage_adaptive_groups` |
| [ ] | `workerPlacementAdaptiveGroups` | Worker placement metrics | `cloudflare.workers.account_worker_placement_adaptive_groups` |
| [ ] | `workersAnalyticsEngineAdaptiveGroups` | Beta. Custom Events with adaptive sampling | `cloudflare.workers.account_workers_analytics_engine_adaptive_groups` |
| [ ] | `workersBuildsBuildMinutesAdaptiveGroups` | Workers Builds build minute overview data with adaptive sampling | `cloudflare.workers.account_workers_builds_build_minutes_adaptive_groups` |
| [ ] | `workersInvocationsAdaptive` | Beta. Workers invocations with adaptive sampling | `cloudflare.workers.account_workers_invocations_adaptive` |
| [ ] | `workersInvocationsScheduled` | Workers scheduled invocations | `cloudflare.workers.account_workers_invocations_scheduled` |
| [ ] | `workersOverviewDataAdaptiveGroups` | Beta. Workers account overview invocation data with adaptive sampling | `cloudflare.workers.account_workers_overview_data_adaptive_groups` |
| [ ] | `workersOverviewRequestsAdaptiveGroups` | Beta. Workers account overview invocation count with adaptive sampling | `cloudflare.workers.account_workers_overview_requests_adaptive_groups` |
| [ ] | `workersSubrequestsAdaptiveGroups` | Beta. Workers subrequests with adaptive sampling | `cloudflare.workers.account_workers_subrequests_adaptive_groups` |
| [ ] | `workersVpcConnectionAdaptiveGroups` | Workers VPC connections with adaptive sampling. | `cloudflare.workers.account_workers_vpc_connection_adaptive_groups` |

### `cloudflare.workflows` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `workflowsAdaptive` | Workflows analytics | `cloudflare.workflows.account_workflows_adaptive` |
| [ ] | `workflowsAdaptiveGroups` | Workflows analytics | `cloudflare.workflows.account_workflows_adaptive_groups` |

### `cloudflare.zaraz` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `zarazTrackAdaptiveGroups` | Zaraz Track Analytics - counts zaraz.track calls | `cloudflare.zaraz.account_zaraz_track_adaptive_groups` |
| [ ] | `zarazTriggersAdaptiveGroups` | Zaraz Triggers Analytics (a trigger is a set of rules that can trigger a zaraz action) | `cloudflare.zaraz.account_zaraz_triggers_adaptive_groups` |

### `cloudflare.zero_trust` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `accessLoginRequestsAdaptiveGroups` | Access login requests | `cloudflare.zero_trust.account_access_login_requests_adaptive_groups` |
| [ ] | `browserIsolationSessionsAdaptiveGroups` | Aggregated count of Browser Isolation sessions | `cloudflare.zero_trust.account_browser_isolation_sessions_adaptive_groups` |
| [ ] | `browserIsolationUserActionsAdaptiveGroups` | Aggregated count of Browser Isolation User Actions matches | `cloudflare.zero_trust.account_browser_isolation_user_actions_adaptive_groups` |
| [ ] | `cf1AccessLogins1dGroups` | CF1 Access login analytics - 1 day rollup (up to 90d window, 365d back) | `cloudflare.zero_trust.account_cf1_access_logins1d_groups` |
| [ ] | `cf1AccessLogins1hGroups` | CF1 Access login analytics - 1 hour rollup (up to 31d window, 62d back). Use cf1AccessLogins1dGroups... | `cloudflare.zero_trust.account_cf1_access_logins1h_groups` |
| [ ] | `cf1AccessLoginsRawGroups` | CF1 Access login analytics - raw data (max 3h window, up to 31d back). Supports unique user counts. ... | `cloudflare.zero_trust.account_cf1_access_logins_raw_groups` |
| [ ] | `cf1GatewayDns1dGroups` | CF1 Gateway DNS analytics - 1 day rollup | `cloudflare.zero_trust.account_cf1_gateway_dns1d_groups` |
| [ ] | `cf1GatewayDns1hGroups` | CF1 Gateway DNS analytics - 1 hour rollup | `cloudflare.zero_trust.account_cf1_gateway_dns1h_groups` |
| [ ] | `cf1GatewayDnsRawGroups` | CF1 Gateway DNS analytics - raw data (max 3h query window). Use cf1GatewayDns1hGroups for longer ran... | `cloudflare.zero_trust.account_cf1_gateway_dns_raw_groups` |
| [ ] | `cf1GatewayHttp1dGroups` | CF1 Gateway HTTP analytics - 1 day rollup (up to 90d window, 365d back) | `cloudflare.zero_trust.account_cf1_gateway_http1d_groups` |
| [ ] | `cf1GatewayHttp1hGroups` | CF1 Gateway HTTP analytics - 1 hour rollup (up to 31d window, 62d back) | `cloudflare.zero_trust.account_cf1_gateway_http1h_groups` |
| [ ] | `cf1GatewayHttpRawGroups` | CF1 Gateway HTTP analytics - raw data (max 3h query window, 4d lookback). Use cf1GatewayHttp1hGroups... | `cloudflare.zero_trust.account_cf1_gateway_http_raw_groups` |
| [ ] | `cf1GatewayNetwork1dGroups` | CF1 Gateway Network analytics (L4 firewall events) - 1 day rollup (up to 90d window, 365d back) | `cloudflare.zero_trust.account_cf1_gateway_network1d_groups` |
| [ ] | `cf1GatewayNetwork1hGroups` | CF1 Gateway Network analytics (L4 firewall events) - 1 hour rollup (up to 31d window, 62d back) | `cloudflare.zero_trust.account_cf1_gateway_network1h_groups` |
| [ ] | `cf1GatewayNetworkRawGroups` | CF1 Gateway Network analytics (L4 firewall events) - raw data (max 3h query window, 4d lookback). Us... | `cloudflare.zero_trust.account_cf1_gateway_network_raw_groups` |
| [ ] | `cf1GatewayNetworkSession1dGroups` | CF1 Gateway Network Session Log analytics - 1 day rollup (up to 90d window, 365d back) | `cloudflare.zero_trust.account_cf1_gateway_network_session1d_groups` |
| [ ] | `cf1GatewayNetworkSession1hGroups` | CF1 Gateway Network Session Log analytics - 1 hour rollup (up to 31d window, 62d back) | `cloudflare.zero_trust.account_cf1_gateway_network_session1h_groups` |
| [ ] | `cf1GatewayNetworkSessionRawGroups` | CF1 Gateway Network Session Log (L4 sessions with bandwidth) - raw data (max 3h query window, 4d loo... | `cloudflare.zero_trust.account_cf1_gateway_network_session_raw_groups` |
| [ ] | `gatewayL4DownstreamSessionsAdaptiveGroups` | Aggregated metrics about downstream (client to edge) L4 Gateway Sessions. Metrics are reported on TC... | `cloudflare.zero_trust.account_gateway_l4_downstream_sessions_adaptive_groups` |
| [ ] | `gatewayL4SessionsAdaptiveGroups` | BETA - Aggregate counts of Gateway L4 sessions with adaptive sampling | `cloudflare.zero_trust.account_gateway_l4_sessions_adaptive_groups` |
| [ ] | `gatewayL4UpstreamSessionsAdaptiveGroups` | Aggregated metrics about upstream (edge to client) L4 Gateway Sessions. Metrics are reported on TCP,... | `cloudflare.zero_trust.account_gateway_l4_upstream_sessions_adaptive_groups` |
| [ ] | `gatewayL7RequestsAdaptiveGroups` | BETA - Aggregate counts of Gateway L7 requests with adaptive sampling | `cloudflare.zero_trust.account_gateway_l7_requests_adaptive_groups` |
| [ ] | `gatewayResolverByCategoryAdaptiveGroups` | BETA - Aggregate counts of Gateway Resolver queries by category with adaptive sampling | `cloudflare.zero_trust.account_gateway_resolver_by_category_adaptive_groups` |
| [ ] | `gatewayResolverByCustomResolverGroups` | Stats on dns custom resolvers | `cloudflare.zero_trust.account_gateway_resolver_by_custom_resolver_groups` |
| [ ] | `gatewayResolverByRuleExecutionPerformanceAdaptiveGroups` | Total time spent on executing firewall rules at the edge | `cloudflare.zero_trust.account_gateway_resolver_by_rule_execution_performance_adaptive_groups` |
| [ ] | `gatewayResolverQueriesAdaptiveGroups` | BETA - Aggregate counts of Gateway Resolver queries with adaptive sampling | `cloudflare.zero_trust.account_gateway_resolver_queries_adaptive_groups` |
| [ ] | `ohttpMetricsAdaptive` | oHTTP request metrics with adaptive sampling | `cloudflare.zero_trust.account_ohttp_metrics_adaptive` |
| [ ] | `ohttpMetricsAdaptiveGroups` | Aggregated oHTTP request metrics with adaptive sampling | `cloudflare.zero_trust.account_ohttp_metrics_adaptive_groups` |
| [ ] | `ohttpRelayEgressConnMetricsAdaptiveGroups` | Aggregated OHTTP relay egress (relay-to-gateway) connection metrics with adaptive sampling | `cloudflare.zero_trust.account_ohttp_relay_egress_conn_metrics_adaptive_groups` |
| [ ] | `ohttpRelayIngressConnMetricsAdaptiveGroups` | Aggregated OHTTP relay ingress (client-to-relay) connection metrics with adaptive sampling | `cloudflare.zero_trust.account_ohttp_relay_ingress_conn_metrics_adaptive_groups` |
| [ ] | `ohttpRelayRequestMetricsAdaptiveGroups` | Aggregated OHTTP relay request metrics with adaptive sampling | `cloudflare.zero_trust.account_ohttp_relay_request_metrics_adaptive_groups` |
| [ ] | `privacyProxyAuthMetricsAdaptiveGroups` | Aggregated Privacy Proxy authentication metrics with adaptive sampling | `cloudflare.zero_trust.account_privacy_proxy_auth_metrics_adaptive_groups` |
| [ ] | `privacyProxyEgressConnMetricsAdaptiveGroups` | Aggregated Privacy Proxy egress (proxy-to-origin) connection metrics with adaptive sampling | `cloudflare.zero_trust.account_privacy_proxy_egress_conn_metrics_adaptive_groups` |
| [ ] | `privacyProxyIngressConnMetricsAdaptiveGroups` | Aggregated Privacy Proxy ingress (client-to-proxy) connection metrics with adaptive sampling | `cloudflare.zero_trust.account_privacy_proxy_ingress_conn_metrics_adaptive_groups` |
| [ ] | `privacyProxyRequestMetricsAdaptiveGroups` | Aggregated Privacy Proxy request metrics with adaptive sampling | `cloudflare.zero_trust.account_privacy_proxy_request_metrics_adaptive_groups` |
| [ ] | `warpDeviceAdaptiveGroups` | Beta. Warp device health events with adaptive sampling | `cloudflare.zero_trust.account_warp_device_adaptive_groups` |
| [ ] | `zeroTrustPrivateNetworkDiscoveryGroups` | Beta - Unique origins, applications, and users discovered for Zero Trust private networks | `cloudflare.zero_trust.account_zero_trust_private_network_discovery_groups` |

### `cloudflare.zones` (account-scoped)

| Pick | GraphQL field | Description | Suggested stackql resource |
|---|---|---|---|
| [ ] | `httpRequests1dGroups` | Daily rollups of request data | `cloudflare.zones.account_http_requests1d_groups` |
| [ ] | `httpRequests1hGroups` | Hourly rollups of request data | `cloudflare.zones.account_http_requests1h_groups` |
| [ ] | `httpRequests1mGroups` | Minutely rollups of request data | `cloudflare.zones.account_http_requests1m_groups` |
| [ ] | `httpRequestsAdaptive` | Raw HTTP requests with adaptive sampling | `cloudflare.zones.account_http_requests_adaptive` |
| [ ] | `httpRequestsAdaptiveGroups` | Aggregated HTTP requests data with adaptive sampling | `cloudflare.zones.account_http_requests_adaptive_groups` |
| [ ] | `httpRequestsOverviewAdaptiveGroups` | A high-level summary of HTTP requests made by end users. | `cloudflare.zones.account_http_requests_overview_adaptive_groups` |

## Notes

- **Audit logs.** Not in this schema mirror. Cloudflare exposes a separate `auditlogs` GraphQL endpoint that needs its own discovery pass.
- **Deprecated REST endpoints superseded by GraphQL** (with hard EOL 2026-12-01 per Cloudflare deprecations page):
  - `GET /zones/{zone_id}/analytics/dashboard` -> `zone.httpRequestsAdaptiveGroups` (already sunset, code 1015)
  - `GET /zones/{zone_id}/analytics/colos` -> `zone.httpRequestsAdaptiveGroups` with `coloCode` dimension
  - `GET /zones/{zone_id}/dns_analytics/*` -> `zone.dnsAnalyticsAdaptive` / `zone.dnsAnalyticsAdaptiveGroups`
  - `GET /accounts/{account_id}/dns_firewall/{id}/dns_analytics/report` -> `account.dnsFirewallAnalyticsAdaptive` / `account.dnsFirewallAnalyticsAdaptiveGroups`
- **Token scope.** GraphQL Analytics requires an API token with `Account -> Analytics -> Read` permission. Document this clearly in user-facing docs to prevent cryptic 403s.
- **Resource-name suggestions** are mechanical. They are *suggestions* - feel free to rename for clarity. e.g. `zone.httpRequestsAdaptiveGroups` could be `http_requests_adaptive` rather than the full `zone_http_requests_adaptive_groups`.
