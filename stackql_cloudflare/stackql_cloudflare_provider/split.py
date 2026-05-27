"""Split the upstream Cloudflare OpenAPI spec into per-service yaml files
following the Python SDK service hierarchy.

Each output file is a self-contained OpenAPI 3.0 document that includes only
the paths assigned to that service and only the component schemas that are
transitively referenced by those paths.
"""
from __future__ import annotations

import copy
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from .sdk_index import SdkOperation, build_path_to_service_index


_VERBS = ("get", "put", "post", "delete", "patch", "options", "head", "trace")


def _ref_name(ref: str) -> Optional[str]:
    prefix = "#/components/schemas/"
    return ref[len(prefix):] if ref.startswith(prefix) else None


def _collect_refs(obj: Any, into: Set[str]) -> None:
    if isinstance(obj, dict):
        ref = obj.get("$ref")
        if isinstance(ref, str):
            n = _ref_name(ref)
            if n:
                into.add(n)
        for v in obj.values():
            _collect_refs(v, into)
    elif isinstance(obj, list):
        for v in obj:
            _collect_refs(v, into)


def _transitive_refs(seed: Set[str], schemas: Dict[str, Any]) -> Set[str]:
    """Return the set of schema names reachable from `seed` through $ref edges."""
    seen: Set[str] = set()
    stack = list(seed)
    while stack:
        name = stack.pop()
        if name in seen or name not in schemas:
            continue
        seen.add(name)
        children: Set[str] = set()
        _collect_refs(schemas[name], children)
        for c in children:
            if c not in seen:
                stack.append(c)
    return seen


# --------------------------------------------------------------------------
# Static capability map: the second static segment after the scope
# (accounts/{id} or zones/{id}) usually identifies the SDK service the path
# belongs to. This is more reliable than the SDK longest-prefix matcher,
# which can over-match short prefixes like `/accounts/{account_id}` and
# accidentally dump a thousand specialised paths under the `accounts`
# service.
#
# The map is keyed by the capability segment as it appears in the upstream
# OpenAPI path. Values are the canonical SDK service name (matches a folder
# under src/cloudflare/resources/).
#
# When a capability isn't here we fall through to SDK longest-prefix and
# then to the URL-prefix heuristic.
# --------------------------------------------------------------------------
_CAPABILITY_TO_SERVICE: Dict[str, str] = {
    # Account/zone-scoped capabilities. Order doesn't matter, but the keys
    # are matched literally against the second-after-scope segment.
    "abuse-reports":                  "abuse_reports",
    "access":                         "zero_trust",
    "acm":                            "acm",
    "addressing":                     "addressing",
    "ai":                             "ai",
    "ai-gateway":                     "ai_gateway",
    "ai-security":                    "ai_security",
    "ai-search":                      "aisearch",
    "aisearch":                       "aisearch",
    "alerting":                       "alerting",
    "api_gateway":                    "api_gateway",
    "api-gateway":                    "api_gateway",
    "argo":                           "argo",
    "audit_logs":                     "audit_logs",
    "audit-logs":                     "audit_logs",
    "audit":                          "audit_logs",
    "autorag":                        "ai",  # AutoRAG is part of the AI capability
    "billing":                        "billing",
    "bot_management":                 "bot_management",
    "botnet-feed":                    "botnet_feed",
    "brand-protection":               "brand_protection",
    "browser-rendering":              "browser_rendering",
    "builds":                         "workers",  # Workers Builds
    "cache":                          "cache",
    "calls":                          "calls",
    "certificate_authorities":        "certificate_authorities",
    "cfd_tunnel":                     "zero_trust",  # Cloudflare Tunnel
    "challenges":                     "turnstile",
    "client_certificates":            "client_certificates",
    "cloud-connector":                "cloud_connector",
    "cloudforce-one":                 "cloudforce_one",
    "connectivity":                   "connectivity",
    "constellation":                  "ai",
    "containers":                     "workers",
    "content-scanning":               "content_scanning",
    "custom_certificates":            "custom_certificates",
    "custom_hostnames":               "custom_hostnames",
    "custom_nameservers":             "custom_nameservers",
    "custom_pages":                   "custom_pages",
    "d1":                             "d1",
    "dcv_delegation":                 "dcv_delegation",
    "ddos_protection":                "ddos_protection",
    "devices":                        "zero_trust",  # Zero Trust device posture
    "dex":                            "zero_trust",
    "diagnostics":                    "diagnostics",
    "dlp":                            "zero_trust",  # Data Loss Prevention
    "dns_firewall":                   "dns_firewall",
    "dns_records":                    "dns",
    "dns_settings":                   "dns",
    "dns":                            "dns",
    "dnssec":                         "dns",
    "durable_objects":                "durable_objects",
    "email-routing":                  "email_routing",
    "email_routing":                  "email_routing",
    "email-security":                 "email_security",
    "email-sending":                  "email_sending",
    "event-notifications":            "queues",
    "filters":                        "filters",
    "firewall":                       "firewall",
    "fraud":                          "fraud",
    "gateway":                        "zero_trust",
    "google-tag-gateway":             "google_tag_gateway",
    "healthchecks":                   "healthchecks",
    "hostnames":                      "hostnames",
    "hyperdrive":                     "hyperdrive",
    "iam":                            "iam",
    "identity_providers":             "zero_trust",
    "images":                         "images",
    "intel":                          "intel",
    "interconnects":                  "network_interconnects",
    "ips":                            "ips",
    "keyless_certificates":           "keyless_certificates",
    "load_balancers":                 "load_balancers",
    "logpush":                        "logpush",
    "logs":                           "logs",
    "magic":                          "magic_transit",
    "magic-cloud-networking":         "magic_cloud_networking",
    "magic-network-monitoring":       "magic_network_monitoring",
    "magic-transit":                  "magic_transit",
    "managed_headers":                "managed_transforms",
    "managed_transforms":             "managed_transforms",
    "members":                        "memberships",
    "memberships":                    "memberships",
    "moq":                            "realtime_kit",
    "mtls_certificates":              "mtls_certificates",
    "network-interconnects":          "network_interconnects",
    "networks":                       "zero_trust",
    "cni":                            "network_interconnects",
    "notifications":                  "alerting",
    "organizations":                  "organizations",
    "origin_ca_certificates":         "origin_ca_certificates",
    "origin_post_quantum_encryption": "origin_post_quantum_encryption",
    "origin_tls_client_auth":         "origin_tls_client_auth",
    "page_shield":                    "page_shield",
    "pagerules":                      "page_rules",
    "pages":                          "pages",
    "pay-per-crawl":                  "billing",
    "pcaps":                          "magic_transit",
    "pipelines":                      "pipelines",
    "profile":                        "iam",
    "queues":                         "queues",
    "r2":                             "r2",
    "r2-data-catalog":                "r2_data_catalog",
    "radar":                          "radar",
    "rate_plans":                     "billing",
    "rate-limits":                    "rate_limits",
    "rate_limits":                    "rate_limits",
    "realtime":                       "realtime_kit",
    "registrar":                      "registrar",
    "request_tracers":                "request_tracers",
    "resource-library":               "zero_trust",
    "resource-sharing":               "resource_sharing",
    "resource-tagging":               "resource_tagging",
    "roles":                          "iam",
    "routing-suppression":            "email_routing",
    "rules":                          "rules",
    "rulesets":                       "rulesets",
    "rum":                            "rum",
    "scim":                           "iam",
    "schema-validation":              "schema_validation",
    "secrets":                        "secrets_store",
    "secrets-store":                  "secrets_store",
    "secrets_store":                  "secrets_store",
    "security_center":                "security_center",
    "secondary_dns":                  "dns",
    "snippets":                       "snippets",
    "spectrum":                       "spectrum",
    "speed_api":                      "speed",
    "speed":                          "speed",
    "ssl":                            "ssl",
    "subscriptions":                  "billing",
    "teamnet":                        "zero_trust",
    "tokens":                         "iam",
    "tunnels":                        "zero_trust",
    "turnstile":                      "turnstile",
    "url-normalization":              "url_normalization",
    "url_normalization":              "url_normalization",
    "urlscanner":                     "url_scanner",
    "vectorize":                      "vectorize",
    "vulnerability-scanner":          "vulnerability_scanner",
    "waf":                            "rulesets",
    "waiting_rooms":                  "waiting_rooms",
    "warp_connector":                 "zero_trust",
    "web3":                           "web3",
    "websites":                       "brand_protection",
    "workers":                        "workers",
    "workers-for-platforms":          "workers_for_platforms",
    "workflows":                      "workflows",
    "zaraz":                          "zaraz",
    "zerotrust":                      "zero_trust",
    "zerotrust-iam":                  "zero_trust",
}


def _static_capability_match(path: str) -> Optional[str]:
    """Look at the second-after-scope segment in `path` and return the
    canonical service per `_CAPABILITY_TO_SERVICE`. Returns None if no
    capability is recognised.

    Examples:
      /accounts/{account_id}/ai/run/@cf/.../model  -> 'ai'
      /accounts/{account_id}/builds/builds         -> 'workers'
      /zones/{zone_id}/dns_records/{id}            -> 'dns'
      /accounts/{account_id}/scim/v2/Users         -> 'iam'
    """
    segs = path.strip("/").split("/")
    if not segs:
        return None
    # First static segment after the leading scope (accounts/zones/user/etc.)
    scope = segs[0]
    if scope in ("accounts", "zones", "user", "memberships", "organizations"):
        # Skip the scope segment and its templated ID (e.g. {account_id}).
        for s in segs[1:]:
            if s.startswith("{") and s.endswith("}"):
                continue
            return _CAPABILITY_TO_SERVICE.get(s)
        return None
    # No leading scope: the first segment is itself the capability.
    return _CAPABILITY_TO_SERVICE.get(scope)


def _service_for_path(
    path: str,
    sdk_idx: Dict[Tuple[str, str], SdkOperation],
    sdk_ops: List[SdkOperation],
) -> Optional[str]:
    """Return the top-level SDK service for an OpenAPI path.

    Resolution order:
      1. Exact (verb, path) match against the SDK index.
      2. Static capability map (path's first capability segment) - this
         catches the common case where the upstream literal path doesn't
         line up with the SDK's template (e.g. /ai/run/@cf/foo/bar vs
         /ai/run/{model_name}) but the capability segment is identical.
      3. SDK longest-prefix match, *requiring* that the prefix go at least
         past the scope's templated ID segment (so a bare `/accounts/{id}`
         prefix doesn't drag everything into the `accounts` bucket).
    """
    for verb in _VERBS:
        hit = sdk_idx.get((verb, path))
        if hit:
            return hit.service

    static_hit = _static_capability_match(path)
    if static_hit:
        return static_hit

    # SDK longest-prefix - only accept matches that go past the scope ID.
    best: Tuple[int, Optional[str]] = (0, None)
    for op in sdk_ops:
        sdk_path = op.path.rstrip("/")
        # Require at least 3 segments to count (so '/accounts/{id}' alone
        # doesn't win - it has only 2 segments, not enough specificity).
        sdk_segs = [s for s in sdk_path.split("/") if s]
        if len(sdk_segs) < 3:
            continue
        if path.startswith(sdk_path + "/") or path == sdk_path:
            score = len(sdk_path)
            if score > best[0]:
                best = (score, op.service)
    return best[1]


_PATH_TO_SLUG_RE = re.compile(r"[^a-z0-9]+")


# Buckets we collapse the fallback heuristic into so the final service list
# stays close to the SDK's resources/ layout. Maps `derived_name -> canonical`.
# Verified by inspecting upstream tags on the affected paths.
_SERVICE_ALIASES: Dict[str, str] = {
    # /users/tenants is the multi-tenant account portion of the user API
    "users": "user",
    # /live, /ready, /internal/submit, /signed-url all carry brand_protection
    # tags upstream
    "live": "brand_protection",
    "ready": "brand_protection",
    "internal": "brand_protection",
    "signed_url": "brand_protection",
    # /system/accounts/{tag}/stores tag is "Secrets Store" upstream
    "system": "secrets_store",
    # `stream` is a reserved word in StackQL's SQL parser - pluralise it
    # so it can appear unquoted in FROM clauses.
    "stream": "streams",
}


def _path_to_service_fallback(path: str) -> str:
    """When no SDK mapping exists, derive a service name from the first
    static path segment.

    /accounts/... -> accounts
    /zones/...    -> zones
    /radar/...    -> radar
    /ips          -> ips

    Paths that begin with a templated segment (e.g. /{accounts_or_zones}/...)
    are mapped using the first static segment that comes after the
    templated portion (e.g. /access/... -> access).
    """
    p = path.strip("/")
    if not p:
        return "root"
    for seg in p.split("/"):
        if seg.startswith("{") and seg.endswith("}"):
            continue
        slug = _PATH_TO_SLUG_RE.sub("_", seg.lower()).strip("_")
        if slug:
            return slug
    return "root"


def _service_filename(service: str) -> str:
    """File-safe service yaml name."""
    safe = re.sub(r"[^a-z0-9]+", "_", service.lower()).strip("_")
    return f"{safe}.yaml"


def _path_seed_refs(path_item: Dict[str, Any]) -> Set[str]:
    """Collect every $ref reachable from a PathItem (operations, parameters,
    request bodies, responses)."""
    seeds: Set[str] = set()
    _collect_refs(path_item, seeds)
    return seeds


def _strip_unused_examples(node: Any) -> Any:
    """Remove `examples` and component-level examples - they bloat each file
    and stackql doesn't consume them."""
    if isinstance(node, dict):
        node.pop("examples", None)
        node.pop("example", None)
        for k, v in list(node.items()):
            node[k] = _strip_unused_examples(v)
        return node
    if isinstance(node, list):
        return [_strip_unused_examples(v) for v in node]
    return node


def assign_paths_to_services(
    spec: Dict[str, Any],
    sdk_ops: List[SdkOperation],
) -> Tuple[Dict[str, Dict[str, Dict[str, Any]]], List[str]]:
    """Return ({service_name: {path: path_item}}, unmatched_paths).

    Each path is assigned to exactly one service. Paths missing from the SDK
    fall back to a URL-prefix heuristic, then through _SERVICE_ALIASES to
    keep the service list close to the SDK's resources/ layout.
    """
    sdk_idx = build_path_to_service_index(sdk_ops)
    by_service: Dict[str, Dict[str, Dict[str, Any]]] = defaultdict(dict)
    unmatched: List[str] = []

    for path, item in spec.get("paths", {}).items():
        svc = _service_for_path(path, sdk_idx, sdk_ops)
        if svc is None:
            svc = _path_to_service_fallback(path)
            unmatched.append(path)
        svc = _SERVICE_ALIASES.get(svc, svc)
        by_service[svc][path] = item

    return dict(by_service), unmatched


def build_service_spec(
    service: str,
    paths: Dict[str, Dict[str, Any]],
    schemas: Dict[str, Any],
    base_info: Dict[str, Any],
    servers: List[Dict[str, Any]],
    security_schemes: Dict[str, Any],
    sdk_idx: Dict[Tuple[str, str], SdkOperation],
) -> Dict[str, Any]:
    """Assemble a self-contained OpenAPI 3.0 document for one service."""
    # Collect every schema this service references, transitively.
    seed: Set[str] = set()
    for path_item in paths.values():
        seed |= _path_seed_refs(path_item)
    needed = _transitive_refs(seed, schemas)

    # Build the components.schemas slice.
    schema_slice = {name: copy.deepcopy(schemas[name]) for name in sorted(needed)}

    # Drop response/request examples to keep specs tight, then drop any
    # operation that has no 2xx response (typically WebSocket-upgrade
    # endpoints with only 101 - StackQL can't model those).
    paths_out: Dict[str, Dict[str, Any]] = {}
    for path, item in paths.items():
        new_item = _strip_unused_examples(copy.deepcopy(item))
        for verb in list(new_item.keys()):
            if verb not in _VERBS:
                continue
            op = new_item.get(verb)
            if not isinstance(op, dict):
                continue
            responses = op.get("responses") or {}
            if not any(str(code).startswith("2") for code in responses.keys()):
                del new_item[verb]
        # Only keep paths that still have at least one operation.
        if any(v in new_item for v in _VERBS):
            paths_out[path] = new_item

    # Force `required: true` on every path parameter. Per the OpenAPI 3.0
    # spec all path parameters must be required, but the upstream Cloudflare
    # spec frequently omits the flag. Downstream tooling (and StackQL's
    # SHOW METHODS introspection) treats absent `required` as "optional",
    # which makes two GETs on /foo and /foo/{bar} look like they have the
    # same parameter signature - an ambiguous route. Forcing the flag
    # disambiguates them.
    for path, item in paths_out.items():
        if not isinstance(item, dict):
            continue
        for verb in _VERBS:
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            for param in (op.get("parameters") or []):
                if isinstance(param, dict) and param.get("in") == "path":
                    param["required"] = True

    # Annotate each operation with the SDK mapping when we have one (so the
    # assign_resource_names step has stable defaults), and synthesize a
    # snake-cased operationId for any operation upstream left blank.
    for path, item in paths_out.items():
        if not isinstance(item, dict):
            continue
        for verb in _VERBS:
            op = item.get(verb)
            if not isinstance(op, dict):
                continue
            sdk_op = sdk_idx.get((verb, path))
            if sdk_op:
                xs = op.setdefault("x-stackql-sdk", {})
                xs["service"] = sdk_op.service
                xs["resource_chain"] = list(sdk_op.resource_chain)
                xs["method"] = sdk_op.sdk_method
            if not op.get("operationId"):
                segs = [s.strip("{}") for s in path.strip("/").split("/") if s]
                synthesized = "_".join([verb] + segs).lower()
                synthesized = re.sub(r"[^a-z0-9]+", "_", synthesized).strip("_")
                op["operationId"] = synthesized

    return {
        "openapi": "3.0.3",
        "info": {
            "title": f"{service} API",
            "description": base_info.get("description", "Cloudflare API"),
            "version": base_info.get("version", "4.0.0"),
            "contact": base_info.get("contact", {"name": "Cloudflare", "url": "https://www.cloudflare.com"}),
        },
        "servers": copy.deepcopy(servers),
        "security": [{"api_token": []}],
        "paths": paths_out,
        "components": {
            "schemas": schema_slice,
            "securitySchemes": copy.deepcopy(security_schemes),
        },
    }
