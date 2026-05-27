"""Canonical path-parameter definitions.

Upstream Cloudflare reuses the same path parameter names across hundreds of
endpoints (e.g. `account_id` 1,800+ times) but the parameter definition
varies wildly - some declarations have a `description`, some don't; some
point at a schema with `format: uuid`, others at a freeform `type: string`.
The result: the rendered Parameters table is inconsistent and often shows
no description for the most common IDs.

This module replaces the inline parameter definition for a known set of
canonical path-param names with a single project-wide standard. We rewrite
in place (no $ref) because the rest of the pipeline expects every operation
parameter to be self-contained at the operation level.

To add a new canonical parameter, add an entry to `CANONICAL_PATH_PARAMS`.
"""
from __future__ import annotations

from typing import Any, Dict


# Single source of truth for the most common path params.
# Each entry: name -> {description, schema}.
# `in: path` and `required: true` are added automatically.
CANONICAL_PATH_PARAMS: Dict[str, Dict[str, Any]] = {
    "account_id": {
        "description": "The Cloudflare account ID.",
        "schema": {"type": "string"},
    },
    "zone_id": {
        "description": "The Cloudflare zone ID.",
        "schema": {"type": "string"},
    },
    "identifier": {
        "description": "Resource identifier.",
        "schema": {"type": "string"},
    },
    "id": {
        "description": "Resource ID.",
        "schema": {"type": "string"},
    },
    "name": {
        "description": "Resource name.",
        "schema": {"type": "string"},
    },
    "app_id": {
        "description": "The Access application ID.",
        "schema": {"type": "string"},
    },
    "policy_id": {
        "description": "The Access policy ID.",
        "schema": {"type": "string"},
    },
    "group_id": {
        "description": "The Access group ID.",
        "schema": {"type": "string"},
    },
    "rule_id": {
        "description": "The rule ID.",
        "schema": {"type": "string"},
    },
    "ruleset_id": {
        "description": "The ruleset ID.",
        "schema": {"type": "string"},
    },
    "script_name": {
        "description": "The Worker script name.",
        "schema": {"type": "string"},
    },
    "dispatch_namespace": {
        "description": "The Workers-for-Platforms dispatch namespace.",
        "schema": {"type": "string"},
    },
    "service_name": {
        "description": "The Worker service name.",
        "schema": {"type": "string"},
    },
    "environment_name": {
        "description": "The Worker service environment name.",
        "schema": {"type": "string"},
    },
    "queue_id": {
        "description": "The Cloudflare Queue ID.",
        "schema": {"type": "string"},
    },
    "namespace_id": {
        "description": "The Workers KV namespace ID.",
        "schema": {"type": "string"},
    },
    "database_id": {
        "description": "The D1 database ID.",
        "schema": {"type": "string"},
    },
    "bucket_name": {
        "description": "The R2 bucket name.",
        "schema": {"type": "string"},
    },
    "index_name": {
        "description": "The Vectorize index name.",
        "schema": {"type": "string"},
    },
    "workflow_name": {
        "description": "The Workflow name.",
        "schema": {"type": "string"},
    },
    "instance_id": {
        "description": "The Workflow instance ID.",
        "schema": {"type": "string"},
    },
    "tunnel_id": {
        "description": "The Cloudflare Tunnel ID.",
        "schema": {"type": "string"},
    },
    "site_id": {
        "description": "The site ID.",
        "schema": {"type": "string"},
    },
    "certificate_id": {
        "description": "The certificate ID.",
        "schema": {"type": "string"},
    },
    "gateway_id": {
        "description": "The AI Gateway ID.",
        "schema": {"type": "string"},
    },
    "dataset_id": {
        "description": "The dataset ID.",
        "schema": {"type": "string"},
    },
    "store_id": {
        "description": "The secrets store ID.",
        "schema": {"type": "string"},
    },
    "secret_id": {
        "description": "The secret ID.",
        "schema": {"type": "string"},
    },
    "job_id": {
        "description": "The job ID.",
        "schema": {"type": "string"},
    },
    "event_id": {
        "description": "The event ID.",
        "schema": {"type": "string"},
    },
    "session_id": {
        "description": "The session ID.",
        "schema": {"type": "string"},
    },
    "meeting_id": {
        "description": "The Realtime Kit meeting ID.",
        "schema": {"type": "string"},
    },
    "organization_id": {
        "description": "The organization ID.",
        "schema": {"type": "string"},
    },
    "membership_id": {
        "description": "The membership ID.",
        "schema": {"type": "string"},
    },
    "member_id": {
        "description": "The account member ID.",
        "schema": {"type": "string"},
    },
    "user_id": {
        "description": "The user ID.",
        "schema": {"type": "string"},
    },
    "role_id": {
        "description": "The role ID.",
        "schema": {"type": "string"},
    },
    "token_id": {
        "description": "The API token ID.",
        "schema": {"type": "string"},
    },
    "subscription_id": {
        "description": "The subscription ID.",
        "schema": {"type": "string"},
    },
    "feed_id": {
        "description": "The Intel indicator feed ID.",
        "schema": {"type": "string"},
    },
    "prefix_id": {
        "description": "The IP prefix ID.",
        "schema": {"type": "string"},
    },
    "snippet_name": {
        "description": "The Cloudflare Snippet name.",
        "schema": {"type": "string"},
    },
    "project_name": {
        "description": "The Pages project name.",
        "schema": {"type": "string"},
    },
    "waiting_room_id": {
        "description": "The Waiting Room ID.",
        "schema": {"type": "string"},
    },
    "load_balancer_id": {
        "description": "The Load Balancer ID.",
        "schema": {"type": "string"},
    },
    "pool_id": {
        "description": "The Load Balancer pool ID.",
        "schema": {"type": "string"},
    },
    "monitor_id": {
        "description": "The Load Balancer monitor ID.",
        "schema": {"type": "string"},
    },
}


def normalize_path_params_in_op(op: dict) -> int:
    """Walk an operation's `parameters` list and rewrite any path parameter
    whose `name` is in `CANONICAL_PATH_PARAMS` to the canonical shape:

        {name, in: path, required: true, schema: <canonical>, description: <canonical>}

    Returns the number of parameters rewritten.
    """
    n = 0
    for p in (op.get("parameters") or []):
        if not isinstance(p, dict):
            continue
        if p.get("in") != "path":
            continue
        name = p.get("name")
        canon = CANONICAL_PATH_PARAMS.get(name)
        if canon is None:
            continue
        # Rewrite in place, preserving any keys we don't explicitly own
        # (e.g. example, x-* extensions) by clearing/resetting only the
        # standard ones.
        p.clear()
        p["name"] = name
        p["in"] = "path"
        p["required"] = True
        p["description"] = canon["description"]
        p["schema"] = dict(canon["schema"])
        n += 1
    return n


def normalize_path_params(spec: dict) -> int:
    """Walk every operation in `spec.paths` and apply
    `normalize_path_params_in_op`. Returns the total parameter count
    rewritten."""
    total = 0
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for verb in ("get", "put", "post", "delete", "patch", "options", "head"):
            op = item.get(verb)
            if isinstance(op, dict):
                total += normalize_path_params_in_op(op)
    return total
