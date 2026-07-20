# Non-selectable resource analysis and remap plan

Working document. At the time of the initial analysis, 220 of 1,267
resources (17%) had no working SELECT. This analysis groups them by root
cause and proposes a disposition for each, with the goal of reducing
genuinely non-selectable resources to true action-only endpoints
(target: under 5%).

**Status 2026-07-20: Phases 1, 2 and 3 are IMPLEMENTED.** The count is
now **73 of 1,171 resources (6.2%)**, down from 221/1,267 (17.4%),
confirmed by the meta-route gate (no signature collisions). The 5
octet-input AI models are folded into `ai.run` as exec methods, and
`tomarkdown`/`to_markdown` are unified (converter + supported-formats
resources). What landed:

- Phase 1.1: AI task-family collapse (`ai_task_families.py` +
  `provider-dev/config/ai_task_families.yaml`) - 93 per-model resources
  -> 9 family SELECT resources, verified live.
- Phase 1.2: the F-group schema fixes (`select_response_fixes.py` +
  `provider-dev/config/select_response_fixes.yaml`) - typed item schemas
  for ai.models/tasks (verified live: `SELECT name, task FROM
  cloudflare.ai.models`), scalar-array-to-rows for resource_tagging and
  ai.authors, contents wraps for the dynamic/raw responses. Note:
  response transforms that access `.result` must use
  `golang_template_json_v0.3.0` (parsed input); the text transform type
  receives the raw body string and only suits `{{ toJson . }}` wraps.
- Phase 2: read-like POSTs remapped to SELECT via `all_services.csv`
  verb edits - d1.database_query, autorag ai-search/search, aisearch
  searches, vectorize v2 query, diagnostics traceroute, registrar
  domain-check, billing pay-per-crawl query, ssl analyze, logs explorer
  SQL, and browser_rendering split into per-render select resources
  (content, links, markdown, json_extract, scrape, snapshot, pdf,
  screenshot).
- Phase 3: 24 CSV fold rows - addressing validate + address-map
  membership -> prefixes/address_maps, logpush validators -> jobs,
  email_security move -> investigate, queue acks -> queues, autorag
  sync -> jobs, vectorize v1 index update -> indexes.

The remaining 81 are the REVIEW group (below) - predominantly genuine
action/write-only endpoints (purge, revoke, send, apply, bulk writes,
octet-stream inputs). Phase 4 (owner sweep of those rows) is the only
open item.

## Proven mechanics (validated live, 2026-07-20)

The pivotal question was whether stackql can map SELECT to a POST operation
with request-body parameters. Answer: **yes**, proven against the live API:

```sql
SELECT contents FROM cloudflare.ai.llama_3_2_1b_instruct
WHERE account_id = '...' AND prompt = 'Reply with exactly the word: pong';
-- -> POST /accounts/{account_id}/ai/run/@cf/meta/llama-3.2-1b-instruct
-- -> body {"prompt": "Reply with exactly the word: pong"}  (built by request.transform)
-- -> one row: contents = '{"result":{"response":"Pong","usage":{...}},...}'
```

Mechanics established:

1. **WHERE params bind to request-body properties with UNPREFIXED names.**
   `WHERE prompt = '...'` works; `WHERE data__prompt = '...'` fails with
   `could not locate symbol data__prompt`. The `data__` prefix is an
   INSERT/UPDATE/REPLACE concept only.
2. The existing `request.transform` blocks (from `request_body_transforms.py`)
   build the POST body from the WHERE params with no changes needed.
3. Untyped responses (`{type: object}`) can be made projectable with the
   `binary_responses.py` contents-wrap pattern (`overrideMediaType` +
   `[{"contents": {{ toJson . }}}]`). Typed responses are better long-term:
   set `objectKey` + a typed schema so DESCRIBE shows real columns.
4. **The generic upstream path `/ai/run/{model_name}` works through stackql
   with slash-containing model names**, proven live:
   `SELECT contents FROM cloudflare.ai.run WHERE account_id = '...' AND
   model_name = '@cf/meta/llama-3.2-1b-instruct' AND prompt = '...'`
   substitutes the value literally into the URL (no encoding issue,
   Cloudflare returns 200). This makes model-collapsed resources viable
   with `model_name` as the discriminator.

## Collapsing the AI model resources

The 99 per-model resources overwhelm the `ai` service. Three collapse
options were evaluated against the actual request/response signatures of
all 98 `/ai/run/@{ns}/{vendor}/{model}` operations:

**Option 1 - collapse by vendor** (`cloudflare.ai.black_forest_labs` with
`{model}` as discriminator). Rejected by the data: 98 models spread across
38 vendor groups, 20 of which contain exactly one model (no gain), and the
large vendors are NOT signature-homogeneous - vendors ship mixed task
types. meta = chat + guard (required: messages) + translation; openai =
LLM + whisper STT (octet-stream input); deepgram = TTS (mpeg output) +
STT + streaming; baai = embeddings + reranker (required: query+contexts);
black-forest-labs itself = flux-1-schnell (required: prompt) vs flux-2-*
(required: multipart). The "same required body args" assumption holds for
only 17 of 38 vendor groups, almost all single-model.

**Option 2 - collapse by task family** with `model_name` as the
discriminator, riding the generic `/ai/run/{model_name}` op (proven above).
This is where the homogeneity actually lives - the signature clusters cut
across vendors and match Cloudflare's own model-catalog task taxonomy
(which `/ai/models/search` returns per model):

| Family resource | Models | Input | Output | Select shape |
|---|---|---|---|---|
| `ai.text_generation` | ~55 (llama, qwen, gemma, mistral, gpt-oss, phi, deepseek, ...) | json (prompt / messages) | json + event-stream | typed: response, usage (or contents) |
| `ai.text_embeddings` | ~10 (bge, embeddinggemma, plamo, qwen3-embedding) | json (text) | json | typed: shape, data |
| `ai.text_to_image` | ~9 (stable-diffusion, flux, dreamshaper, leonardo) | json (prompt) | json / png | contents (base64/binary) |
| `ai.speech_to_text` | ~5 (whisper x3, nova-3) | octet-stream or json (audio) | json | typed: text, words |
| `ai.text_to_speech` | ~4 (aura x3, melotts) | json (text/prompt) | mpeg / json | contents |
| `ai.text_classification` | ~2 (distilbert x2) | json (text) | json | typed array |
| `ai.image_classification` | ~3 (resnet x2, detr) | octet-stream | json | typed array |
| `ai.translation` | ~3 (m2m100, indictrans2 x2) | json (text, target_language) | json | typed: translated_text |
| `ai.summarization` | ~2 (bart x2) | json (input_text) | json | typed: summary |
| `ai.reranking` | ~1 (bge-reranker-base) | json (query, contexts) | json | typed |

Each family resource carries a single `run` method that `$ref`s the SAME
generic operation, with a per-family `request.schema_override` (the union
of the family's body schemas - homogeneous by construction) and a
per-family typed response schema or contents wrap. The `schema_override` +
`request.transform` machinery already exists (built for the octet-stream
work). The 98 per-model paths and resources are then DROPPED from the
provider: the ai service goes from 100+ inference resources to ~10, the
spec shrinks, and every family is selectable. Models with octet-stream
input (whisper, resnet) stay reachable in the same family resource via an
`insert`/`exec` method rather than select (binary WHERE values are
impractical).

Model discovery composes nicely once `ai.models` is schema-fixed
(F group): `SELECT name FROM cloudflare.ai.models WHERE search_task =
'Text Generation'` tells you what to put in `model_name`.

**Option 3 - single generic `ai.run` resource only.** Simplest (already
proven live), but one union body schema across ALL task types and a
contents-only response. Fine as a fallback or stepping stone; Option 2 is
strictly better UX for the same machinery.

**Recommendation: Option 2**, with Option 3's generic `ai.run` kept as the
escape hatch for new/unlisted models.

## Groups

| Group | Count | Root cause | Disposition |
|---|---|---|---|
| A - AI model inference | 99 | Each Workers AI model is a resource with a single `insert` POST `/ai/run/...` | **Collapse into ~10 task-family SELECT resources** (see "Collapsing the AI model resources" above) riding the generic `/ai/run/{model_name}` op with `model_name` as the discriminator. 99 resources -> ~10, all selectable. |
| F - select exists, no columns | 19 | Upstream response schema is untyped (`result: {items: {type: object}}`), a scalar array, a dynamic-keyed object, or missing entirely | **Schema fix per resource**: inject typed item schemas where the shape is known (ai.models search), wrap scalars/raw text as contents, or transform scalar arrays to single-column rows. |
| C - insert-only action POSTs | 24 | Validation / query / conversion POSTs mapped to `insert` | Split: **read-like -> SELECT** (d1 query, autorag search, aisearch, tomarkdown), **validators -> FOLD as exec into their noun parent** (addressing.validate -> prefixes, logpush validate/ownership -> jobs), true uploads stay. |
| D - write-only mixed | 15 | Resources with insert/update/delete but no list/get upstream | Case-by-case: fold methods into the selectable sibling resource where one exists (rulesets.rules, zero_trust entries), else accept. |
| E - other | 63 | Exec-only verb-resources (purge, revoke, send, ack, apply) and write-only membership subresources (address map members, split-tunnel lists) | Split: **read-like -> SELECT** (browser_rendering renders, traceroute, domain-check, ssl analyze, logs SQL, vectorize query), **membership -> FOLD into parent**, true actions -> ACCEPT as exec-only. |

Disposition counts across all 220 (see appendix for per-resource detail):

| Action | Count | Meaning |
|---|---|---|
| SELECT | 113 | Remap the existing POST/GET to a select method (contents wrap or typed schema) |
| SELECT+ | 4 | Resource keeps write verbs; its read-like methods additionally map to select |
| SCHEMA-FIX | 19 | Select mapping already correct; fix the response schema/objectKey/wrap |
| FOLD | 14 | Move method(s) into the selectable parent resource as exec, delete this resource |
| ACCEPT | 3 | Genuinely non-selectable (uploads, browser session lifecycle, purge) |
| REVIEW | 67 | Group-default disposition assigned; needs an owner call per resource |

Projected outcome if all SELECT/SCHEMA-FIX/FOLD land: 220 -> 70 flagged, and
most of the remaining 67 REVIEW rows are genuine exec-only actions (purge,
revoke, ack, send) that would end as ACCEPT. Realistic end state: roughly
40-60 non-selectable resources (3-5%), all true actions.

## Implementation plan

Phase 1 - mechanical, high-volume (kills ~120 of 220):

1. **AI model collapse -> ~10 task-family SELECT resources** (per the
   "Collapsing the AI model resources" section): build a task-family map
   from the model catalog, generate per-family union body schemas +
   `request.schema_override` entries against the generic
   `/ai/run/{model_name}` op, drop the 98 per-model paths and resources,
   keep generic `ai.run` as the escape hatch. Body-required properties
   (prompt, messages, text, etc.) surface as WHERE params with unprefixed
   names. Octet-stream-input models (whisper, resnet) stay as insert/exec
   methods within their family resource (binary WHERE values are
   impractical).
2. **Schema fixes for the 19 F-group resources**: extend `binary_responses.py`
   (or a new `select_schema_fixes.py` post-pass) with: contents wrap for
   raw/dynamic responses, scalar-array-to-rows transforms, and injected
   typed item schemas for ai.models/authors/tasks and the cloudforce_one
   list endpoints.

Phase 2 - read-like POSTs -> SELECT (~15 resources): d1.database_query,
autorag/aisearch searches, vectorize query/get_by_ids, browser_rendering
renders, diagnostics traceroute, registrar domain-check, ssl analyze,
logs explorer SQL, billing pay-per-crawl query, cloudforce_one search_v2.
Each needs an objectKey (typed result) or contents wrap. CSV `stackql_verb`
edits + regeneration.

Phase 3 - folds (~14 resources + REVIEW outcomes): extend the
`fold_singletons.py` approach (or CSV resource renames) to move validators
and membership writes into their noun parents:
addressing.validate -> prefixes; addressing address-map members ->
address_maps; logpush validators -> jobs; queue acks -> messages; email
move -> messages; vectorize.vectorize -> indexes; ai.sync -> rags.

Phase 4 - REVIEW sweep: walk the 67 REVIEW rows with the maintainer, decide
fold vs accept per resource, then re-run `make all` and the meta-route gate
to confirm the non-selectable count.

Notes and constraints:

- SELECT-on-POST executes the operation on every query. For inference and
  renders that is the point, but document it (each SELECT bills an inference
  call). Same caveat as the GraphQL analytics resources.
- The meta-test counts a resource non-selectable when DESCRIBE yields no
  columns even if sqlVerbs.select exists - so SCHEMA-FIX items must change
  schemas, not just mappings.
- All remaps flow through `all_services.csv` (stackql_verb) plus post-pass
  transforms, so `make all` remains the single path to a rebuilt provider.

## Appendix - per-resource dispositions

### A-ai-model-inference

Superseded by the task-family collapse (see "Collapsing the AI model
resources"): every resource below is absorbed into one of ~10 family
resources and its per-model path is dropped from the provider. The
per-row SELECT action stands only if the collapse is rejected.

| Resource | Current verbs | Action | Notes |
|---|---|---|---|
| `ai.aura_1` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.aura_2_en` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.aura_2_es` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.bart_large_cnn` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.bge_base_en_v1_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.bge_large_en_v1_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.bge_m3` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.bge_reranker_base` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.bge_small_en_v1_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.deepseek_coder_6_7b_base_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.deepseek_coder_6_7b_instruct_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.deepseek_math_7b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.deepseek_r1_distill_qwen_32b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.discolm_german_7b_v1_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.distilbert_sst_2_int8` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.dreamshaper_8_lcm` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.embeddinggemma_300m` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.falcon_7b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.flux` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.flux_1_schnell` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.flux_2_dev` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.flux_2_klein_4b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.flux_2_klein_9b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gemma_2b_it_lora` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gemma_3_12b_it` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gemma_7b_it` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gemma_7b_it_lora` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gemma_sea_lion_v4_27b_it` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.glm_4_7_flash` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gpt_oss_120b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.gpt_oss_20b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.granite_4_0_h_micro` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.hermes_2_pro_mistral_7b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.indictrans2_en_indic_1_b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.kimi_k2_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_2_13b_chat_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_2_7b_chat_fp16` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_2_7b_chat_hf_lora` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_2_7b_chat_int8` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_1_70b_instruct_fp8_fast` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_1_8b_instruct_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_1_8b_instruct_fp8` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_1_8b_instruct_fp8_fast` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_2_11b_vision_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_2_1b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_2_3b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_3_70b_instruct_fp8_fast` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_8b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_3_8b_instruct_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_4_scout_17b_16e_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.llama_guard_3_8b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.lucid_origin` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.m2m100_1_2b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.melotts` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.mistral_7b_instruct_v0_1` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.mistral_7b_instruct_v0_1_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.mistral_7b_instruct_v0_2` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.mistral_7b_instruct_v0_2_lora` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.mistral_small_3_1_24b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nemotron_3_120b_a12b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.neural_chat_7b_v3_1_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_bart_large_cnn` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_bge_base_en_v1_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_bge_large_en_v1_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_bge_m3` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_bge_small_en_v1_5` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_detr_resnet_50` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_distilbert_sst_2_int8` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_embeddinggemma_300m` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_indictrans2_en_indic_1b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nonomni_resnet_50` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.nova_3` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.openchat_3_5_0106` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.openhermes_2_5_mistral_7b_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.phi_2` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.phoenix_1_0` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.plamo_embedding_1b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen1_5_0_5b_chat` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen1_5_14b_chat_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen1_5_1_8b_chat` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen1_5_7b_chat_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen2_5_coder_32b_instruct` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen3_30b_a3b_fp8` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwen3_embedding_0_6b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.qwq_32b` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.resnet_50` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.run` | insert | **SELECT** | generic model runner: WHERE model_name + body params, contents wrap |
| `ai.sqlcoder_7b_2` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.stable_diffusion_v1_5_img2img` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.stable_diffusion_v1_5_inpainting` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.stable_diffusion_xl_base_1_0` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.stable_diffusion_xl_lightning` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.starling_lm_7b_beta` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.tinyllama_1_1b_chat_v1_0` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.una_cybertron_7b_v2_bf16` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.whisper` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.whisper_large_v3_turbo` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.whisper_tiny_en` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |
| `ai.zephyr_7b_beta_awq` | insert | **SELECT** | insert -> select; contents wrap v1, per-family typed schema v2; WHERE binds body props (proven live) |

### C-insert-only

| Resource | Current verbs | Action | Notes |
|---|---|---|---|
| `addressing.validate` | insert | **FOLD** | exec into addressing.prefixes (prefix validation action) |
| `ai.ai_search` | insert | **SELECT** | autorag ai-search: objectKey $.result.data (typed) |
| `ai.assets` | insert | **ACCEPT** | finetune asset upload - genuine write-only |
| `ai.search` | insert | **SELECT** | autorag search: objectKey $.result.data (typed: file_id, filename, score, content) |
| `ai.tomarkdown` | insert | **SELECT** | doc conversion returns markdown - contents/typed wrap |
| `aisearch.chat_completions` | insert | **SELECT** | returns completion data - contents wrap (or keep insert; decide) |
| `aisearch.instances_search` | insert | **SELECT** | search results - objectKey $.result.data |
| `aisearch.namespace_instance_chat_completions` | insert | **SELECT** | as chat_completions |
| `aisearch.namespaces_instance_search` | insert | **SELECT** | search results |
| `aisearch.namespaces_search` | insert | **SELECT** | search results |
| `api_gateway.fallthrough` | insert | **REVIEW** | action POST - fold into parent or keep insert |
| `api_gateway.operations_item` | insert | **REVIEW** | action POST - fold into parent or keep insert |
| `cloudforce_one.binary_storage` | insert | **REVIEW** | action POST - fold into parent or keep insert |
| `cloudforce_one.events_categories_create` | insert | **REVIEW** | action POST - fold into parent or keep insert |
| `d1.database_query` | insert | **SELECT** | objectKey $.result (typed d1QueryResultResponse rows) |
| `email_security.move` | insert | **FOLD** | exec into email_security investigate/messages resource |
| `logpush.destination_exists` | insert | **FOLD** | exec into logpush.jobs (validation action) |
| `logpush.logpush_ownership` | insert | **FOLD** | exec into logpush.jobs (ownership challenge) |
| `logpush.ownership_validate` | insert | **FOLD** | exec into logpush.jobs (validation action) |
| `logpush.validate_destination` | insert | **FOLD** | exec into logpush.jobs (validation action) |
| `logpush.validate_origin` | insert | **FOLD** | exec into logpush.jobs (validation action) |
| `realtime_kit.livestreams` | insert | **REVIEW** | action POST - fold into parent or keep insert |
| `workflows.workflows_instances` | insert | **REVIEW** | action POST - fold into parent or keep insert |
| `zero_trust.upload` | insert | **REVIEW** | action POST - fold into parent or keep insert |

### D-write-only-mixed

| Resource | Current verbs | Action | Notes |
|---|---|---|---|
| `brand_protection.brand_protection_logos` | insert,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `brand_protection.logo_queries` | insert,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `browser_rendering.browser` | insert,delete | **ACCEPT** | browser session create/delete - lifecycle |
| `cloudforce_one.bulk` | insert,update | **REVIEW** | fold methods into selectable sibling or accept |
| `cloudforce_one.dataset` | insert,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `cloudforce_one.event_tags` | insert,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `cloudforce_one.tags` | insert,update,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `firewall.rules` | insert,update,delete,replace | **REVIEW** | fold methods into selectable sibling or accept |
| `realtime_kit.meetings` | insert,update,delete,replace | **REVIEW** | fold methods into selectable sibling or accept |
| `rulesets.rules` | insert,update,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `token_validation.bulk` | insert,update | **REVIEW** | fold methods into selectable sibling or accept |
| `zero_trust.cas` | insert,delete | **REVIEW** | fold methods into selectable sibling or accept |
| `zero_trust.entries` | insert,replace | **REVIEW** | fold methods into selectable sibling or accept |
| `zero_trust.entries_predefined` | insert,delete,replace | **REVIEW** | fold methods into selectable sibling or accept |
| `zero_trust.integration` | insert,delete,replace | **REVIEW** | fold methods into selectable sibling or accept |

### E-other

| Resource | Current verbs | Action | Notes |
|---|---|---|---|
| `addressing.accounts` | delete,replace | **FOLD** | exec into addressing.address_maps (membership add/remove) |
| `addressing.ips` | delete,replace | **FOLD** | exec into addressing.address_maps (membership add/remove) |
| `addressing.zones` | delete,replace | **FOLD** | exec into addressing.address_maps (membership add/remove) |
| `ai.sync` | update | **FOLD** | exec into ai.rags (autorag sync action) |
| `api_gateway.managed_resources_operation` | replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `api_gateway.user_resources_operation` | replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `billing.accounts` | exec-only | **SELECT+** | query_pay_per_crawl_zones -> select; set_ stays exec |
| `brand_protection.brand_protection` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `browser_rendering.browser_rendering` | exec-only | **SELECT+** | content/links/markdown/json/scrape -> select (result string/typed); pdf/screenshot -> select via contents |
| `cache.batch` | update,delete | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cache.cache_reserve` | update | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cache.zones` | exec-only | **ACCEPT** | purge_cache - genuine action (already folded verb-resource) |
| `cloudforce_one.cloudforce_one` | exec-only | **SELECT+** | search_v2 -> select candidate; create_requests/generate_v2 stay |
| `cloudforce_one.events_create` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cloudforce_one.message` | delete,replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cloudforce_one.message_new` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cloudforce_one.relate_create` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cloudforce_one.requests_new` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `cloudforce_one.tags_categories_create` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `content_scanning.content_upload_scan` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `custom_hostnames.certificates` | delete,replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `diagnostics.diagnostics` | exec-only | **SELECT** | traceroute returns hops - objectKey $.result |
| `dns.secondary_dns` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `email_sending.email` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `images.images` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `intel.intel` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `logs.accounts_logs_explorer_query_sql` | exec-only | **SELECT** | SQL query over logs - rows |
| `logs.zones_logs_explorer_query_sql` | exec-only | **SELECT** | SQL query over logs - rows |
| `magic_cloud_networking.magic` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `magic_network_monitoring.mnm` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `pipelines.pipelines` | delete,replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `queues.messages_ack` | exec-only | **FOLD** | exec into queues.messages |
| `queues.preview_ack` | exec-only | **FOLD** | exec into queues.subscriptions_preview or messages |
| `r2.r2` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `r2.source_connectivity_precheck` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `r2.target_connectivity_precheck` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `registrar.registrar` | exec-only | **SELECT** | domain-check: objectKey $.result.domains (typed availability rows) |
| `request_tracers.request_tracer` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `rulesets.versions` | delete | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `rum.rum` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `security_center.classification` | update | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `ssl.ssl` | exec-only | **SELECT** | analyze returns cert analysis - contents wrap (untyped upstream) |
| `token_validation.token_validation` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `url_scanner.urlscanner` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `vectorize.indexes` | exec-only | **SELECT+** | query/get_by_ids -> select; insert/upsert/delete_by_ids stay exec |
| `vectorize.vectorize` | exec-only | **FOLD** | update_indexes replace into vectorize indexes resource |
| `workers.connections` | delete,replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `workers.content` | replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `workers.settings` | update | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `workflows.instances_events` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zaraz.settings` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.access` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.cfd_tunnel` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.devices` | delete | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.devices_revoke` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.dlp` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.exclude` | replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.fallback_domains` | replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.include` | replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.infrastructure` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.integrations` | update,replace | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.physical_devices_revoke` | exec-only | **REVIEW** | exec-only action or membership subresource - fold or accept |
| `zero_trust.rules` | update | **REVIEW** | exec-only action or membership subresource - fold or accept |

### F-select-empty-schema

| Resource | Current verbs | Action | Notes |
|---|---|---|---|
| `ai.authors` | select | **SCHEMA-FIX** | type result items (upstream {type: object}); else contents wrap |
| `ai.models` | select | **SCHEMA-FIX** | type result items (name, description, task, properties known from API) |
| `ai.tasks` | select | **SCHEMA-FIX** | type result items |
| `ai_gateway.dynamic_routing` | select,insert,update,delete | **SCHEMA-FIX** | type the response items or wrap as contents |
| `alerting.available_alerts` | select | **SCHEMA-FIX** | dynamic-keyed object - contents wrap |
| `browser_rendering.targets` | select,replace | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.attackers` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.countries` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.datasets` | select,insert,update | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.events_categories` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.events_target_industries` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.indicator_types_indicator_types` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
| `cloudforce_one.indicators_tags` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
| `logs.rayids` | select | **SCHEMA-FIX** | raw log line - contents wrap |
| `logs.received` | select | **SCHEMA-FIX** | raw log lines - contents wrap |
| `network_interconnects.loas` | select | **SCHEMA-FIX** | no 200 content in spec - LOA document; contents wrap like other loa_documents |
| `resource_tagging.keys` | select | **SCHEMA-FIX** | result is array of strings - wrap to [{key: ...}] via transform |
| `resource_tagging.values` | select | **SCHEMA-FIX** | array of strings - wrap to [{value: ...}] |
| `zero_trust.devices_override_codes` | select | **SCHEMA-FIX** | type the response items or wrap as contents |
