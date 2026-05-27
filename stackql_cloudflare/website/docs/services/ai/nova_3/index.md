--- 
title: nova_3
hide_title: false
hide_table_of_contents: false
keywords:
  - nova_3
  - ai
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

Creates, updates, deletes, gets or lists a <code>nova_3</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="nova_3" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.ai.nova_3" /></td></tr>
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
    <td><a href="#workers_ai_post_run_cf_deepgram_nova_3"><CopyableCode code="workers_ai_post_run_cf_deepgram_nova_3" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-audio"><code>audio</code></a></td>
    <td><a href="#parameter-queueRequest"><code>queueRequest</code></a>, <a href="#parameter-tags"><code>tags</code></a></td>
    <td>Runs inference on the @cf/deepgram/nova-3 model.</td>
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
<tr id="parameter-queueRequest">
    <td><CopyableCode code="queueRequest" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-tags">
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="workers_ai_post_run_cf_deepgram_nova_3"
    values={[
        { label: 'workers_ai_post_run_cf_deepgram_nova_3', value: 'workers_ai_post_run_cf_deepgram_nova_3' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="workers_ai_post_run_cf_deepgram_nova_3">

Runs inference on the @cf/deepgram/nova-3 model.

```sql
INSERT INTO cloudflare.ai.nova_3 (
audio,
channels,
custom_intent,
custom_intent_mode,
custom_topic,
custom_topic_mode,
detect_entities,
detect_language,
diarize,
dictation,
encoding,
endpointing,
extra,
filler_words,
interim_results,
keyterm,
keywords,
language,
measurements,
mip_opt_out,
mode,
multichannel,
numerals,
paragraphs,
profanity_filter,
punctuate,
redact,
replace,
search,
sentiment,
smart_format,
topics,
utt_split,
utterance_end_ms,
utterances,
vad_events,
account_id,
queueRequest,
tags
)
SELECT 
'{{ audio }}' /* required */,
{{ channels }},
'{{ custom_intent }}',
'{{ custom_intent_mode }}',
'{{ custom_topic }}',
'{{ custom_topic_mode }}',
{{ detect_entities }},
{{ detect_language }},
{{ diarize }},
{{ dictation }},
'{{ encoding }}',
'{{ endpointing }}',
'{{ extra }}',
{{ filler_words }},
{{ interim_results }},
'{{ keyterm }}',
'{{ keywords }}',
'{{ language }}',
{{ measurements }},
{{ mip_opt_out }},
'{{ mode }}',
{{ multichannel }},
{{ numerals }},
{{ paragraphs }},
{{ profanity_filter }},
{{ punctuate }},
'{{ redact }}',
'{{ replace }}',
'{{ search }}',
{{ sentiment }},
{{ smart_format }},
{{ topics }},
{{ utt_split }},
{{ utterance_end_ms }},
{{ utterances }},
{{ vad_events }},
'{{ account_id }}',
'{{ queueRequest }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: nova_3
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the nova_3 resource.
    - name: audio
      value:
        body: "{{ body }}"
        contentType: "{{ contentType }}"
    - name: channels
      value: {{ channels }}
      description: |
        The number of channels in the submitted audio
    - name: custom_intent
      value: "{{ custom_intent }}"
      description: |
        Custom intents you want the model to detect within your input audio if present
    - name: custom_intent_mode
      value: "{{ custom_intent_mode }}"
      description: |
        Sets how the model will interpret intents submitted to the custom_intent param. When strict, the model will only return intents submitted using the custom_intent param. When extended, the model will return its own detected intents in addition those submitted using the custom_intents param
      valid_values: ['extended', 'strict']
    - name: custom_topic
      value: "{{ custom_topic }}"
      description: |
        Custom topics you want the model to detect within your input audio or text if present Submit up to 100
    - name: custom_topic_mode
      value: "{{ custom_topic_mode }}"
      description: |
        Sets how the model will interpret strings submitted to the custom_topic param. When strict, the model will only return topics submitted using the custom_topic param. When extended, the model will return its own detected topics in addition to those submitted using the custom_topic param.
      valid_values: ['extended', 'strict']
    - name: detect_entities
      value: {{ detect_entities }}
      description: |
        Identifies and extracts key entities from content in submitted audio
    - name: detect_language
      value: {{ detect_language }}
      description: |
        Identifies the dominant language spoken in submitted audio
    - name: diarize
      value: {{ diarize }}
      description: |
        Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0
    - name: dictation
      value: {{ dictation }}
      description: |
        Identify and extract key entities from content in submitted audio
    - name: encoding
      value: "{{ encoding }}"
      description: |
        Specify the expected encoding of your submitted audio
      valid_values: ['linear16', 'flac', 'mulaw', 'amr-nb', 'amr-wb', 'opus', 'speex', 'g729']
    - name: endpointing
      value: "{{ endpointing }}"
      description: |
        Indicates how long model will wait to detect whether a speaker has finished speaking or pauses for a significant period of time. When set to a value, the streaming endpoint immediately finalizes the transcription for the processed time range and returns the transcript with a speech_final parameter set to true. Can also be set to false to disable endpointing
    - name: extra
      value: "{{ extra }}"
      description: |
        Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
    - name: filler_words
      value: {{ filler_words }}
      description: |
        Filler Words can help transcribe interruptions in your audio, like 'uh' and 'um'
    - name: interim_results
      value: {{ interim_results }}
      description: |
        Specifies whether the streaming endpoint should provide ongoing transcription updates as more audio is received. When set to true, the endpoint sends continuous updates, meaning transcription results may evolve over time. Note: Supported only for webosockets.
    - name: keyterm
      value: "{{ keyterm }}"
      description: |
        Key term prompting can boost or suppress specialized terminology and brands.
    - name: keywords
      value: "{{ keywords }}"
      description: |
        Keywords can boost or suppress specialized terminology and brands.
    - name: language
      value: "{{ language }}"
      description: |
        The BCP-47 language tag that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available.
    - name: measurements
      value: {{ measurements }}
      description: |
        Spoken measurements will be converted to their corresponding abbreviations.
    - name: mip_opt_out
      value: {{ mip_opt_out }}
      description: |
        Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip.
    - name: mode
      value: "{{ mode }}"
      description: |
        Mode of operation for the model representing broad area of topic that will be talked about in the supplied audio
      valid_values: ['general', 'medical', 'finance']
    - name: multichannel
      value: {{ multichannel }}
      description: |
        Transcribe each audio channel independently.
    - name: numerals
      value: {{ numerals }}
      description: |
        Numerals converts numbers from written format to numerical format.
    - name: paragraphs
      value: {{ paragraphs }}
      description: |
        Splits audio into paragraphs to improve transcript readability.
    - name: profanity_filter
      value: {{ profanity_filter }}
      description: |
        Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely.
    - name: punctuate
      value: {{ punctuate }}
      description: |
        Add punctuation and capitalization to the transcript.
    - name: redact
      value: "{{ redact }}"
      description: |
        Redaction removes sensitive information from your transcripts.
    - name: replace
      value: "{{ replace }}"
      description: |
        Search for terms or phrases in submitted audio and replaces them.
    - name: search
      value: "{{ search }}"
      description: |
        Search for terms or phrases in submitted audio.
    - name: sentiment
      value: {{ sentiment }}
      description: |
        Recognizes the sentiment throughout a transcript or text.
    - name: smart_format
      value: {{ smart_format }}
      description: |
        Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability.
    - name: topics
      value: {{ topics }}
      description: |
        Detect topics throughout a transcript or text.
    - name: utt_split
      value: {{ utt_split }}
      description: |
        Seconds to wait before detecting a pause between words in submitted audio.
    - name: utterance_end_ms
      value: {{ utterance_end_ms }}
      description: |
        Indicates how long model will wait to send an UtteranceEnd message after a word has been transcribed. Use with interim_results. Note: Supported only for webosockets.
    - name: utterances
      value: {{ utterances }}
      description: |
        Segments speech into meaningful semantic units.
    - name: vad_events
      value: {{ vad_events }}
      description: |
        Indicates that speech has started. You'll begin receiving Speech Started messages upon speech starting. Note: Supported only for webosockets.
    - name: queueRequest
      value: "{{ queueRequest }}"
    - name: tags
      value: "{{ tags }}"
`}</CodeBlock>

</TabItem>
</Tabs>
