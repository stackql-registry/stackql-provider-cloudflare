--- 
title: waiting_rooms
hide_title: false
hide_table_of_contents: false
keywords:
  - waiting_rooms
  - waiting_rooms
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

Creates, updates, deletes, gets or lists a <code>waiting_rooms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="waiting_rooms" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.waiting_rooms.waiting_rooms" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_zone', value: 'list_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get">

Waiting room details response

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
    <td><CopyableCode code="result" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_zone">

List waiting rooms for account or zone response

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
    <td> (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A unique name to identify the waiting room. Only alphanumeric characters, hyphens and underscores are allowed. (example: production_webinar)</td>
</tr>
<tr>
    <td><CopyableCode code="additional_routes" /></td>
    <td><code>array</code></td>
    <td>Only available for the Waiting Room Advanced subscription. Additional hostname and path combinations to which this waiting room will be applied. There is an implied wildcard at the end of the path. The hostname and path combination must be unique to this and all other waiting rooms.</td>
</tr>
<tr>
    <td><CopyableCode code="cookie_attributes" /></td>
    <td><code>object</code></td>
    <td>Configures cookie attributes for the waiting room cookie. This encrypted cookie stores a user's status in the waiting room, such as queue position.</td>
</tr>
<tr>
    <td><CopyableCode code="cookie_suffix" /></td>
    <td><code>string</code></td>
    <td>Appends a '_' + a custom suffix to the end of Cloudflare Waiting Room's cookie name(__cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be `__cf_waitingroom_abcd`. This field is required if using `additional_routes`. (default: , example: abcd)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_page_html" /></td>
    <td><code>string</code></td>
    <td>Only available for the Waiting Room Advanced subscription. This is a template html file that will be rendered at the edge. If no custom_page_html is provided, the default waiting room will be used. The template is based on mustache ( https://mustache.github.io/ ). There are several variables that are evaluated by the Cloudflare edge: 1. &#123;&#123;`waitTimeKnown`&#125;&#125; Acts like a boolean value that indicates the behavior to take when wait time is not available, for instance when queue_all is **true**. 2. &#123;&#123;`waitTimeFormatted`&#125;&#125; Estimated wait time for the user. For example, five minutes. Alternatively, you can use: 3. &#123;&#123;`waitTime`&#125;&#125; Number of minutes of estimated wait for a user. 4. &#123;&#123;`waitTimeHours`&#125;&#125; Number of hours of estimated wait for a user (`Math.floor(waitTime/60)`). 5. &#123;&#123;`waitTimeHourMinutes`&#125;&#125; Number of minutes above the `waitTimeHours` value (`waitTime%60`). 6. &#123;&#123;`queueIsFull`&#125;&#125; Changes to **true** when no more people can be added to the queue. To view the full list of variables, look at the `cfWaitingRoom` object described under the `json_response_enabled` property in other Waiting Room API calls. (default: , example: &#123;&#123;#waitTimeKnown&#125;&#125; &#123;&#123;waitTime&#125;&#125; mins &#123;&#123;/waitTimeKnown&#125;&#125; &#123;&#123;^waitTimeKnown&#125;&#125; Queue all enabled &#123;&#123;/waitTimeKnown&#125;&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="default_template_language" /></td>
    <td><code>string</code></td>
    <td>The language of the default page template. If no default_template_language is provided, then `en-US` (English) will be used. (en-US, es-ES, de-DE, fr-FR, it-IT, ja-JP, ko-KR, pt-BR, zh-CN, zh-TW, nl-NL, pl-PL, id-ID, tr-TR, ar-EG, ru-RU, fa-IR, bg-BG, hr-HR, cs-CZ, da-DK, fi-FI, lt-LT, ms-MY, nb-NO, ro-RO, el-GR, he-IL, hi-IN, hu-HU, sr-BA, sk-SK, sl-SI, sv-SE, tl-PH, th-TH, uk-UA, vi-VN) (default: en-US, example: es-ES)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A note that you can use to add more details about the waiting room. (default: , example: Production - DO NOT MODIFY)</td>
</tr>
<tr>
    <td><CopyableCode code="disable_session_renewal" /></td>
    <td><code>boolean</code></td>
    <td>Only available for the Waiting Room Advanced subscription. Disables automatic renewal of session cookies. If `true`, an accepted user will have session_duration minutes to browse the site. After that, they will have to go through the waiting room again. If `false`, a user's session cookie will be automatically renewed on every request.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled_origin_commands" /></td>
    <td><code>array</code></td>
    <td>A list of enabled origin commands.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td>The host name to which the waiting room will be applied (no wildcards). Please do not include the scheme (http:// or https://). The host and path combination must be unique. (example: shop.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="json_response_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Only available for the Waiting Room Advanced subscription. If `true`, requests to the waiting room with the header `Accept: application/json` will receive a JSON response object with information on the user's status in the waiting room as opposed to the configured static HTML page. This JSON response object has one property `cfWaitingRoom` which is an object containing the following fields: 1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room (always **true**). 2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are accurate. If **false**, they are not available. 3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating the current estimated time in minutes the user will wait in the waiting room. When `queueingMethod` is **random**, this is set to `waitTime50Percentile`. 4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and `waitTimeKnown` is **true**. Integer indicating the current estimated maximum wait time for the 25% of users that gain entry the fastest (25th percentile). 5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and `waitTimeKnown` is **true**. Integer indicating the current estimated maximum wait time for the 50% of users that gain entry the fastest (50th percentile). In other words, half of the queued users are expected to let into the origin website before `waitTime50Percentile` and half are expected to be let in after it. 6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and `waitTimeKnown` is **true**. Integer indicating the current estimated maximum wait time for the 75% of users that gain entry the fastest (75th percentile). 7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display **unavailable**. 8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently full and not accepting new users at the moment. 9. `queueAll`: Boolean indicating if all users will be queued in the waiting room and no one will be let into the origin website. 10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the user's last attempt to leave the waiting room and be let into the origin website. The user is able to make another attempt after `refreshIntervalSeconds` past this time. If the user makes a request too soon, it will be ignored and `lastUpdated` will not change. 11. `refreshIntervalSeconds`: Integer indicating the number of seconds after `lastUpdated` until the user is able to make another attempt to leave the waiting room and be let into the origin website. When the `queueingMethod` is `reject`, there is no specified refresh time —\_it will always be **zero**. 12. `queueingMethod`: The queueing method currently used by the waiting room. It is either **fifo**, **random**, **passthrough**, or **reject**. 13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO (First-In-First-Out) queue. 14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue where users gain access randomly. 15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a passthrough queue. Keep in mind that when passthrough is enabled, this JSON response will only exist when `queueAll` is **true** or `isEventPrequeueing` is **true** because in all other cases requests will go directly to the origin. 16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue. 17. `isEventActive`: Boolean indicating if an event is currently occurring. Events are able to change a waiting room's behavior during a specified period of time. For additional information, look at the event properties `prequeue_start_time`, `event_start_time`, and `event_end_time` in the documentation for creating waiting room events. Events are considered active between these start and end times, as well as during the prequeueing period if it exists. 18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean indicating if an event is currently prequeueing users before it starts. 19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**. Integer indicating the number of minutes until the event starts. 20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart` formatted in English for users. If `isEventPrequeueing` is **false**, `timeUntilEventStartFormatted` will display **unavailable**. 21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer indicating the number of minutes until the event ends. 22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd` formatted in English for users. If `isEventActive` is **false**, `timeUntilEventEndFormatted` will display **unavailable**. 23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean indicating if the users in the prequeue are shuffled randomly when the event starts. 24. `turnstile`: Empty when turnstile isn't enabled. String displaying an html tag to display the Turnstile widget. Please add the `&#123;&#123;&#123;turnstile&#125;&#125;&#125;` tag to the `custom_html` template to ensure the Turnstile widget appears. 25. `infiniteQueue`: Boolean indicating whether the response is for a user in the infinite queue. An example cURL to a waiting room could be: curl -X GET "https://example.com/waitingroom" \ -H "Accept: application/json" If `json_response_enabled` is **true** and the request hits the waiting room, an example JSON response when `queueingMethod` is **fifo** and no event is active could be: &#123; "cfWaitingRoom": &#123; "inWaitingRoom": true, "waitTimeKnown": true, "waitTime": 10, "waitTime25Percentile": 0, "waitTime50Percentile": 0, "waitTime75Percentile": 0, "waitTimeFormatted": "10 minutes", "queueIsFull": false, "queueAll": false, "lastUpdated": "2020-08-03T23:46:00.000Z", "refreshIntervalSeconds": 20, "queueingMethod": "fifo", "isFIFOQueue": true, "isRandomQueue": false, "isPassthroughQueue": false, "isRejectQueue": false, "isEventActive": false, "isEventPrequeueing": false, "timeUntilEventStart": 0, "timeUntilEventStartFormatted": "unavailable", "timeUntilEventEnd": 0, "timeUntilEventEndFormatted": "unavailable", "shuffleAtEventStart": false &#125; &#125; If `json_response_enabled` is **true** and the request hits the waiting room, an example JSON response when `queueingMethod` is **random** and an event is active could be: &#123; "cfWaitingRoom": &#123; "inWaitingRoom": true, "waitTimeKnown": true, "waitTime": 10, "waitTime25Percentile": 5, "waitTime50Percentile": 10, "waitTime75Percentile": 15, "waitTimeFormatted": "5 minutes to 15 minutes", "queueIsFull": false, "queueAll": false, "lastUpdated": "2020-08-03T23:46:00.000Z", "refreshIntervalSeconds": 20, "queueingMethod": "random", "isFIFOQueue": false, "isRandomQueue": true, "isPassthroughQueue": false, "isRejectQueue": false, "isEventActive": true, "isEventPrequeueing": false, "timeUntilEventStart": 0, "timeUntilEventStartFormatted": "unavailable", "timeUntilEventEnd": 15, "timeUntilEventEndFormatted": "15 minutes", "shuffleAtEventStart": true &#125; &#125;</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="new_users_per_minute" /></td>
    <td><code>integer</code></td>
    <td>Sets the number of new users that will be let into the route every minute. This value is used as baseline for the number of users that are let in per minute. So it is possible that there is a little more or little less traffic coming to the route based on the traffic patterns at that time around the world.</td>
</tr>
<tr>
    <td><CopyableCode code="next_event_prequeue_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks when the next event will begin queueing. (example: 2021-09-28T15:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="next_event_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks when the next event will start. (example: 2021-09-28T15:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Sets the path within the host to enable the waiting room on. The waiting room will be enabled for all subpaths as well. If there are two waiting rooms on the same subpath, the waiting room for the most specific path will be chosen. Wildcards and query parameters are not supported. (default: /, example: /shop/checkout)</td>
</tr>
<tr>
    <td><CopyableCode code="queue_all" /></td>
    <td><code>boolean</code></td>
    <td>If queue_all is `true`, all the traffic that is coming to a route will be sent to the waiting room. No new traffic can get to the route once this field is set and estimated time will become unavailable.</td>
</tr>
<tr>
    <td><CopyableCode code="queueing_method" /></td>
    <td><code>string</code></td>
    <td>Sets the queueing method used by the waiting room. Changing this parameter from the **default** queueing method is only available for the Waiting Room Advanced subscription. Regardless of the queueing method, if `queue_all` is enabled or an event is prequeueing, users in the waiting room will not be accepted to the origin. These users will always see a waiting room page that refreshes automatically. The valid queueing methods are: 1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in the order they arrived. 2. `random`: Random queue where customers gain access randomly, regardless of arrival time. 3. `passthrough`: Users will pass directly through the waiting room and into the origin website. As a result, any configured limits will not be respected while this is enabled. This method can be used as an alternative to disabling a waiting room (with `suspended`) so that analytics are still reported. This can be used if you wish to allow all traffic normally, but want to restrict traffic during a waiting room event, or vice versa. 4. `reject`: Users will be immediately rejected from the waiting room. As a result, no users will reach the origin website while this is enabled. This can be used if you wish to reject all traffic while performing maintenance, block traffic during a specified period of time (an event), or block traffic while events are not occurring. Consider a waiting room used for vaccine distribution that only allows traffic during sign-up events, and otherwise blocks all traffic. For this case, the waiting room uses `reject`, and its events override this with `fifo`, `random`, or `passthrough`. When this queueing method is enabled and neither `queueAll` is enabled nor an event is prequeueing, the waiting room page **will not refresh automatically**. (fifo, random, passthrough, reject) (default: fifo, example: fifo)</td>
</tr>
<tr>
    <td><CopyableCode code="queueing_status_code" /></td>
    <td><code>integer</code></td>
    <td>HTTP status code returned to a user while in the queue. (200, 202, 429)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>integer</code></td>
    <td>Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. If a user is not seen by Cloudflare again in that time period, they will be treated as a new user that visits the route.</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>Suspends or allows traffic going to the waiting room. If set to `true`, the traffic will not go to the waiting room.</td>
</tr>
<tr>
    <td><CopyableCode code="total_active_users" /></td>
    <td><code>integer</code></td>
    <td>Sets the total number of active user sessions on the route at a point in time. A route is a combination of host and path on which a waiting room is available. This value is used as a baseline for the total number of active user sessions on the route. It is possible to have a situation where there are more or less active users sessions on the route based on the traffic patterns at that time around the world.</td>
</tr>
<tr>
    <td><CopyableCode code="turnstile_action" /></td>
    <td><code>string</code></td>
    <td>Which action to take when a bot is detected using Turnstile. `log` will have no impact on queueing behavior, simply keeping track of how many bots are detected in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing state, where they will never reach your origin. `infinite_queue` requires Advanced Waiting Room. (log, infinite_queue) (default: log)</td>
</tr>
<tr>
    <td><CopyableCode code="turnstile_mode" /></td>
    <td><code>string</code></td>
    <td>Which Turnstile widget type to use for detecting bot traffic. See [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types) for the definitions of these widget types. Set to `off` to disable the Turnstile integration entirely. Setting this to anything other than `off` or `invisible` requires Advanced Waiting Room. (off, invisible, visible_non_interactive, visible_managed) (default: invisible)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_account">

List waiting rooms for account or zone response

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
    <td> (example: 699d98642c564d2e855e9661899b7252)</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>A unique name to identify the waiting room. Only alphanumeric characters, hyphens and underscores are allowed. (example: production_webinar)</td>
</tr>
<tr>
    <td><CopyableCode code="additional_routes" /></td>
    <td><code>array</code></td>
    <td>Only available for the Waiting Room Advanced subscription. Additional hostname and path combinations to which this waiting room will be applied. There is an implied wildcard at the end of the path. The hostname and path combination must be unique to this and all other waiting rooms.</td>
</tr>
<tr>
    <td><CopyableCode code="cookie_attributes" /></td>
    <td><code>object</code></td>
    <td>Configures cookie attributes for the waiting room cookie. This encrypted cookie stores a user's status in the waiting room, such as queue position.</td>
</tr>
<tr>
    <td><CopyableCode code="cookie_suffix" /></td>
    <td><code>string</code></td>
    <td>Appends a '_' + a custom suffix to the end of Cloudflare Waiting Room's cookie name(__cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be `__cf_waitingroom_abcd`. This field is required if using `additional_routes`. (default: , example: abcd)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="custom_page_html" /></td>
    <td><code>string</code></td>
    <td>Only available for the Waiting Room Advanced subscription. This is a template html file that will be rendered at the edge. If no custom_page_html is provided, the default waiting room will be used. The template is based on mustache ( https://mustache.github.io/ ). There are several variables that are evaluated by the Cloudflare edge: 1. &#123;&#123;`waitTimeKnown`&#125;&#125; Acts like a boolean value that indicates the behavior to take when wait time is not available, for instance when queue_all is **true**. 2. &#123;&#123;`waitTimeFormatted`&#125;&#125; Estimated wait time for the user. For example, five minutes. Alternatively, you can use: 3. &#123;&#123;`waitTime`&#125;&#125; Number of minutes of estimated wait for a user. 4. &#123;&#123;`waitTimeHours`&#125;&#125; Number of hours of estimated wait for a user (`Math.floor(waitTime/60)`). 5. &#123;&#123;`waitTimeHourMinutes`&#125;&#125; Number of minutes above the `waitTimeHours` value (`waitTime%60`). 6. &#123;&#123;`queueIsFull`&#125;&#125; Changes to **true** when no more people can be added to the queue. To view the full list of variables, look at the `cfWaitingRoom` object described under the `json_response_enabled` property in other Waiting Room API calls. (default: , example: &#123;&#123;#waitTimeKnown&#125;&#125; &#123;&#123;waitTime&#125;&#125; mins &#123;&#123;/waitTimeKnown&#125;&#125; &#123;&#123;^waitTimeKnown&#125;&#125; Queue all enabled &#123;&#123;/waitTimeKnown&#125;&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="default_template_language" /></td>
    <td><code>string</code></td>
    <td>The language of the default page template. If no default_template_language is provided, then `en-US` (English) will be used. (en-US, es-ES, de-DE, fr-FR, it-IT, ja-JP, ko-KR, pt-BR, zh-CN, zh-TW, nl-NL, pl-PL, id-ID, tr-TR, ar-EG, ru-RU, fa-IR, bg-BG, hr-HR, cs-CZ, da-DK, fi-FI, lt-LT, ms-MY, nb-NO, ro-RO, el-GR, he-IL, hi-IN, hu-HU, sr-BA, sk-SK, sl-SI, sv-SE, tl-PH, th-TH, uk-UA, vi-VN) (default: en-US, example: es-ES)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A note that you can use to add more details about the waiting room. (default: , example: Production - DO NOT MODIFY)</td>
</tr>
<tr>
    <td><CopyableCode code="disable_session_renewal" /></td>
    <td><code>boolean</code></td>
    <td>Only available for the Waiting Room Advanced subscription. Disables automatic renewal of session cookies. If `true`, an accepted user will have session_duration minutes to browse the site. After that, they will have to go through the waiting room again. If `false`, a user's session cookie will be automatically renewed on every request.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled_origin_commands" /></td>
    <td><code>array</code></td>
    <td>A list of enabled origin commands.</td>
</tr>
<tr>
    <td><CopyableCode code="host" /></td>
    <td><code>string</code></td>
    <td>The host name to which the waiting room will be applied (no wildcards). Please do not include the scheme (http:// or https://). The host and path combination must be unique. (example: shop.example.com)</td>
</tr>
<tr>
    <td><CopyableCode code="json_response_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Only available for the Waiting Room Advanced subscription. If `true`, requests to the waiting room with the header `Accept: application/json` will receive a JSON response object with information on the user's status in the waiting room as opposed to the configured static HTML page. This JSON response object has one property `cfWaitingRoom` which is an object containing the following fields: 1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room (always **true**). 2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are accurate. If **false**, they are not available. 3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating the current estimated time in minutes the user will wait in the waiting room. When `queueingMethod` is **random**, this is set to `waitTime50Percentile`. 4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and `waitTimeKnown` is **true**. Integer indicating the current estimated maximum wait time for the 25% of users that gain entry the fastest (25th percentile). 5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and `waitTimeKnown` is **true**. Integer indicating the current estimated maximum wait time for the 50% of users that gain entry the fastest (50th percentile). In other words, half of the queued users are expected to let into the origin website before `waitTime50Percentile` and half are expected to be let in after it. 6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and `waitTimeKnown` is **true**. Integer indicating the current estimated maximum wait time for the 75% of users that gain entry the fastest (75th percentile). 7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display **unavailable**. 8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently full and not accepting new users at the moment. 9. `queueAll`: Boolean indicating if all users will be queued in the waiting room and no one will be let into the origin website. 10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the user's last attempt to leave the waiting room and be let into the origin website. The user is able to make another attempt after `refreshIntervalSeconds` past this time. If the user makes a request too soon, it will be ignored and `lastUpdated` will not change. 11. `refreshIntervalSeconds`: Integer indicating the number of seconds after `lastUpdated` until the user is able to make another attempt to leave the waiting room and be let into the origin website. When the `queueingMethod` is `reject`, there is no specified refresh time —\_it will always be **zero**. 12. `queueingMethod`: The queueing method currently used by the waiting room. It is either **fifo**, **random**, **passthrough**, or **reject**. 13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO (First-In-First-Out) queue. 14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue where users gain access randomly. 15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a passthrough queue. Keep in mind that when passthrough is enabled, this JSON response will only exist when `queueAll` is **true** or `isEventPrequeueing` is **true** because in all other cases requests will go directly to the origin. 16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue. 17. `isEventActive`: Boolean indicating if an event is currently occurring. Events are able to change a waiting room's behavior during a specified period of time. For additional information, look at the event properties `prequeue_start_time`, `event_start_time`, and `event_end_time` in the documentation for creating waiting room events. Events are considered active between these start and end times, as well as during the prequeueing period if it exists. 18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean indicating if an event is currently prequeueing users before it starts. 19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**. Integer indicating the number of minutes until the event starts. 20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart` formatted in English for users. If `isEventPrequeueing` is **false**, `timeUntilEventStartFormatted` will display **unavailable**. 21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer indicating the number of minutes until the event ends. 22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd` formatted in English for users. If `isEventActive` is **false**, `timeUntilEventEndFormatted` will display **unavailable**. 23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean indicating if the users in the prequeue are shuffled randomly when the event starts. 24. `turnstile`: Empty when turnstile isn't enabled. String displaying an html tag to display the Turnstile widget. Please add the `&#123;&#123;&#123;turnstile&#125;&#125;&#125;` tag to the `custom_html` template to ensure the Turnstile widget appears. 25. `infiniteQueue`: Boolean indicating whether the response is for a user in the infinite queue. An example cURL to a waiting room could be: curl -X GET "https://example.com/waitingroom" \ -H "Accept: application/json" If `json_response_enabled` is **true** and the request hits the waiting room, an example JSON response when `queueingMethod` is **fifo** and no event is active could be: &#123; "cfWaitingRoom": &#123; "inWaitingRoom": true, "waitTimeKnown": true, "waitTime": 10, "waitTime25Percentile": 0, "waitTime50Percentile": 0, "waitTime75Percentile": 0, "waitTimeFormatted": "10 minutes", "queueIsFull": false, "queueAll": false, "lastUpdated": "2020-08-03T23:46:00.000Z", "refreshIntervalSeconds": 20, "queueingMethod": "fifo", "isFIFOQueue": true, "isRandomQueue": false, "isPassthroughQueue": false, "isRejectQueue": false, "isEventActive": false, "isEventPrequeueing": false, "timeUntilEventStart": 0, "timeUntilEventStartFormatted": "unavailable", "timeUntilEventEnd": 0, "timeUntilEventEndFormatted": "unavailable", "shuffleAtEventStart": false &#125; &#125; If `json_response_enabled` is **true** and the request hits the waiting room, an example JSON response when `queueingMethod` is **random** and an event is active could be: &#123; "cfWaitingRoom": &#123; "inWaitingRoom": true, "waitTimeKnown": true, "waitTime": 10, "waitTime25Percentile": 5, "waitTime50Percentile": 10, "waitTime75Percentile": 15, "waitTimeFormatted": "5 minutes to 15 minutes", "queueIsFull": false, "queueAll": false, "lastUpdated": "2020-08-03T23:46:00.000Z", "refreshIntervalSeconds": 20, "queueingMethod": "random", "isFIFOQueue": false, "isRandomQueue": true, "isPassthroughQueue": false, "isRejectQueue": false, "isEventActive": true, "isEventPrequeueing": false, "timeUntilEventStart": 0, "timeUntilEventStartFormatted": "unavailable", "timeUntilEventEnd": 15, "timeUntilEventEndFormatted": "15 minutes", "shuffleAtEventStart": true &#125; &#125;</td>
</tr>
<tr>
    <td><CopyableCode code="modified_on" /></td>
    <td><code>string (date-time)</code></td>
    <td> (example: 2014-01-01T05:20:00.12345Z)</td>
</tr>
<tr>
    <td><CopyableCode code="new_users_per_minute" /></td>
    <td><code>integer</code></td>
    <td>Sets the number of new users that will be let into the route every minute. This value is used as baseline for the number of users that are let in per minute. So it is possible that there is a little more or little less traffic coming to the route based on the traffic patterns at that time around the world.</td>
</tr>
<tr>
    <td><CopyableCode code="next_event_prequeue_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks when the next event will begin queueing. (example: 2021-09-28T15:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="next_event_start_time" /></td>
    <td><code>string</code></td>
    <td>An ISO 8601 timestamp that marks when the next event will start. (example: 2021-09-28T15:00:00.000Z)</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Sets the path within the host to enable the waiting room on. The waiting room will be enabled for all subpaths as well. If there are two waiting rooms on the same subpath, the waiting room for the most specific path will be chosen. Wildcards and query parameters are not supported. (default: /, example: /shop/checkout)</td>
</tr>
<tr>
    <td><CopyableCode code="queue_all" /></td>
    <td><code>boolean</code></td>
    <td>If queue_all is `true`, all the traffic that is coming to a route will be sent to the waiting room. No new traffic can get to the route once this field is set and estimated time will become unavailable.</td>
</tr>
<tr>
    <td><CopyableCode code="queueing_method" /></td>
    <td><code>string</code></td>
    <td>Sets the queueing method used by the waiting room. Changing this parameter from the **default** queueing method is only available for the Waiting Room Advanced subscription. Regardless of the queueing method, if `queue_all` is enabled or an event is prequeueing, users in the waiting room will not be accepted to the origin. These users will always see a waiting room page that refreshes automatically. The valid queueing methods are: 1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in the order they arrived. 2. `random`: Random queue where customers gain access randomly, regardless of arrival time. 3. `passthrough`: Users will pass directly through the waiting room and into the origin website. As a result, any configured limits will not be respected while this is enabled. This method can be used as an alternative to disabling a waiting room (with `suspended`) so that analytics are still reported. This can be used if you wish to allow all traffic normally, but want to restrict traffic during a waiting room event, or vice versa. 4. `reject`: Users will be immediately rejected from the waiting room. As a result, no users will reach the origin website while this is enabled. This can be used if you wish to reject all traffic while performing maintenance, block traffic during a specified period of time (an event), or block traffic while events are not occurring. Consider a waiting room used for vaccine distribution that only allows traffic during sign-up events, and otherwise blocks all traffic. For this case, the waiting room uses `reject`, and its events override this with `fifo`, `random`, or `passthrough`. When this queueing method is enabled and neither `queueAll` is enabled nor an event is prequeueing, the waiting room page **will not refresh automatically**. (fifo, random, passthrough, reject) (default: fifo, example: fifo)</td>
</tr>
<tr>
    <td><CopyableCode code="queueing_status_code" /></td>
    <td><code>integer</code></td>
    <td>HTTP status code returned to a user while in the queue. (200, 202, 429)</td>
</tr>
<tr>
    <td><CopyableCode code="session_duration" /></td>
    <td><code>integer</code></td>
    <td>Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the route. If a user is not seen by Cloudflare again in that time period, they will be treated as a new user that visits the route.</td>
</tr>
<tr>
    <td><CopyableCode code="suspended" /></td>
    <td><code>boolean</code></td>
    <td>Suspends or allows traffic going to the waiting room. If set to `true`, the traffic will not go to the waiting room.</td>
</tr>
<tr>
    <td><CopyableCode code="total_active_users" /></td>
    <td><code>integer</code></td>
    <td>Sets the total number of active user sessions on the route at a point in time. A route is a combination of host and path on which a waiting room is available. This value is used as a baseline for the total number of active user sessions on the route. It is possible to have a situation where there are more or less active users sessions on the route based on the traffic patterns at that time around the world.</td>
</tr>
<tr>
    <td><CopyableCode code="turnstile_action" /></td>
    <td><code>string</code></td>
    <td>Which action to take when a bot is detected using Turnstile. `log` will have no impact on queueing behavior, simply keeping track of how many bots are detected in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing state, where they will never reach your origin. `infinite_queue` requires Advanced Waiting Room. (log, infinite_queue) (default: log)</td>
</tr>
<tr>
    <td><CopyableCode code="turnstile_mode" /></td>
    <td><code>string</code></td>
    <td>Which Turnstile widget type to use for detecting bot traffic. See [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types) for the definitions of these widget types. Set to `off` to disable the Turnstile integration entirely. Setting this to anything other than `off` or `invisible` requires Advanced Waiting Room. (off, invisible, visible_non_interactive, visible_managed) (default: invisible)</td>
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
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Fetches a single configured waiting room.</td>
</tr>
<tr>
    <td><a href="#list_by_zone"><CopyableCode code="list_by_zone" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists waiting rooms for account or zone.</td>
</tr>
<tr>
    <td><a href="#list_by_account"><CopyableCode code="list_by_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-per_page"><code>per_page</code></a></td>
    <td>Lists waiting rooms for account or zone.</td>
</tr>
<tr>
    <td><a href="#edit"><CopyableCode code="edit" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-new_users_per_minute"><code>new_users_per_minute</code></a>, <a href="#parameter-total_active_users"><code>total_active_users</code></a></td>
    <td></td>
    <td>Patches a configured waiting room.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-host"><code>host</code></a>, <a href="#parameter-new_users_per_minute"><code>new_users_per_minute</code></a>, <a href="#parameter-total_active_users"><code>total_active_users</code></a></td>
    <td></td>
    <td>Updates a configured waiting room.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-waiting_room_id"><code>waiting_room_id</code></a>, <a href="#parameter-zone_id"><code>zone_id</code></a></td>
    <td></td>
    <td>Deletes a waiting room.</td>
</tr>
<tr>
    <td><a href="#preview"><CopyableCode code="preview" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-zone_id"><code>zone_id</code></a>, <a href="#parameter-custom_html"><code>custom_html</code></a></td>
    <td></td>
    <td>Creates a waiting room page preview. Upload a custom waiting room page for preview. You will receive a preview URL in the form `http://waitingrooms.dev/preview/<uuid>`. You can use the following query parameters to change the state of the preview: 1. `force_queue`: Boolean indicating if all users will be queued in the waiting room and no one will be let into the origin website (also known as queueAll). 2. `queue_is_full`: Boolean indicating if the waiting room's queue is currently full and not accepting new users at the moment. 3. `queueing_method`: The queueing method currently used by the waiting room. - **fifo** indicates a FIFO queue. - **random** indicates a Random queue. - **passthrough** indicates a Passthrough queue. Keep in mind that the waiting room page will only be displayed if `force_queue=true` or `event=prequeueing` — for other cases the request will pass through to the origin. For our preview, this will be a fake origin website returning \"Welcome\". - **reject** indicates a Reject queue. 4. `event`: Used to preview a waiting room event. - **none** indicates no event is occurring. - **prequeueing** indicates that an event is prequeueing (between `prequeue_start_time` and `event_start_time`). - **started** indicates that an event has started (between `event_start_time` and `event_end_time`). 5. `shuffle_at_event_start`: Boolean indicating if the event will shuffle users in the prequeue when it starts. This can only be set to **true** if an event is active (`event` is not **none**). For example, you can make a request to `http://waitingrooms.dev/preview/<uuid>?force_queue=false&queue_is_full=false&queueing_method=random&event=started&shuffle_at_event_start=true` 6. `waitTime`: Non-zero, positive integer indicating the estimated wait time in minutes. The default value is 10 minutes. For example, you can make a request to `http://waitingrooms.dev/preview/<uuid>?waitTime=50` to configure the estimated wait time as 50 minutes.</td>
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
<tr id="parameter-waiting_room_id">
    <td><CopyableCode code="waiting_room_id" /></td>
    <td><code>string</code></td>
    <td>The Waiting Room ID.</td>
</tr>
<tr id="parameter-zone_id">
    <td><CopyableCode code="zone_id" /></td>
    <td><code>string</code></td>
    <td>The Cloudflare zone ID.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>number</code></td>
    <td>Page number of paginated results.</td>
</tr>
<tr id="parameter-per_page">
    <td><CopyableCode code="per_page" /></td>
    <td><code>number</code></td>
    <td>Maximum number of results per page. Must be a multiple of 5.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_zone', value: 'list_by_zone' },
        { label: 'list_by_account', value: 'list_by_account' }
    ]}
>
<TabItem value="get">

Fetches a single configured waiting room.

```sql
SELECT
result
FROM cloudflare.waiting_rooms.waiting_rooms
WHERE waiting_room_id = '{{ waiting_room_id }}' -- required
AND zone_id = '{{ zone_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_zone">

Lists waiting rooms for account or zone.

```sql
SELECT
id,
name,
additional_routes,
cookie_attributes,
cookie_suffix,
created_on,
custom_page_html,
default_template_language,
description,
disable_session_renewal,
enabled_origin_commands,
host,
json_response_enabled,
modified_on,
new_users_per_minute,
next_event_prequeue_start_time,
next_event_start_time,
path,
queue_all,
queueing_method,
queueing_status_code,
session_duration,
suspended,
total_active_users,
turnstile_action,
turnstile_mode
FROM cloudflare.waiting_rooms.waiting_rooms
WHERE zone_id = '{{ zone_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
;
```
</TabItem>
<TabItem value="list_by_account">

Lists waiting rooms for account or zone.

```sql
SELECT
id,
name,
additional_routes,
cookie_attributes,
cookie_suffix,
created_on,
custom_page_html,
default_template_language,
description,
disable_session_renewal,
enabled_origin_commands,
host,
json_response_enabled,
modified_on,
new_users_per_minute,
next_event_prequeue_start_time,
next_event_start_time,
path,
queue_all,
queueing_method,
queueing_status_code,
session_duration,
suspended,
total_active_users,
turnstile_action,
turnstile_mode
FROM cloudflare.waiting_rooms.waiting_rooms
WHERE account_id = '{{ account_id }}' -- required
AND page = '{{ page }}'
AND per_page = '{{ per_page }}'
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

Patches a configured waiting room.

```sql
UPDATE cloudflare.waiting_rooms.waiting_rooms
SET 
additional_routes = '{{ additional_routes }}',
cookie_attributes = '{{ cookie_attributes }}',
cookie_suffix = '{{ cookie_suffix }}',
custom_page_html = '{{ custom_page_html }}',
default_template_language = '{{ default_template_language }}',
description = '{{ description }}',
disable_session_renewal = {{ disable_session_renewal }},
enabled_origin_commands = '{{ enabled_origin_commands }}',
host = '{{ host }}',
json_response_enabled = {{ json_response_enabled }},
name = '{{ name }}',
new_users_per_minute = {{ new_users_per_minute }},
path = '{{ path }}',
queue_all = {{ queue_all }},
queueing_method = '{{ queueing_method }}',
queueing_status_code = {{ queueing_status_code }},
session_duration = {{ session_duration }},
suspended = {{ suspended }},
total_active_users = {{ total_active_users }},
turnstile_action = '{{ turnstile_action }}',
turnstile_mode = '{{ turnstile_mode }}'
WHERE 
waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND host = '{{ host }}' --required
AND new_users_per_minute = '{{ new_users_per_minute }}' --required
AND total_active_users = '{{ total_active_users }}' --required
RETURNING
result;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Updates a configured waiting room.

```sql
REPLACE cloudflare.waiting_rooms.waiting_rooms
SET 
additional_routes = '{{ additional_routes }}',
cookie_attributes = '{{ cookie_attributes }}',
cookie_suffix = '{{ cookie_suffix }}',
custom_page_html = '{{ custom_page_html }}',
default_template_language = '{{ default_template_language }}',
description = '{{ description }}',
disable_session_renewal = {{ disable_session_renewal }},
enabled_origin_commands = '{{ enabled_origin_commands }}',
host = '{{ host }}',
json_response_enabled = {{ json_response_enabled }},
name = '{{ name }}',
new_users_per_minute = {{ new_users_per_minute }},
path = '{{ path }}',
queue_all = {{ queue_all }},
queueing_method = '{{ queueing_method }}',
queueing_status_code = {{ queueing_status_code }},
session_duration = {{ session_duration }},
suspended = {{ suspended }},
total_active_users = {{ total_active_users }},
turnstile_action = '{{ turnstile_action }}',
turnstile_mode = '{{ turnstile_mode }}'
WHERE 
waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
AND name = '{{ name }}' --required
AND host = '{{ host }}' --required
AND new_users_per_minute = '{{ new_users_per_minute }}' --required
AND total_active_users = '{{ total_active_users }}' --required
RETURNING
result;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a waiting room.

```sql
DELETE FROM cloudflare.waiting_rooms.waiting_rooms
WHERE waiting_room_id = '{{ waiting_room_id }}' --required
AND zone_id = '{{ zone_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="preview"
    values={[
        { label: 'preview', value: 'preview' }
    ]}
>
<TabItem value="preview">

Creates a waiting room page preview. Upload a custom waiting room page for preview. You will receive a preview URL in the form `http://waitingrooms.dev/preview/<uuid>`. You can use the following query parameters to change the state of the preview: 1. `force_queue`: Boolean indicating if all users will be queued in the waiting room and no one will be let into the origin website (also known as queueAll). 2. `queue_is_full`: Boolean indicating if the waiting room's queue is currently full and not accepting new users at the moment. 3. `queueing_method`: The queueing method currently used by the waiting room. - **fifo** indicates a FIFO queue. - **random** indicates a Random queue. - **passthrough** indicates a Passthrough queue. Keep in mind that the waiting room page will only be displayed if `force_queue=true` or `event=prequeueing` — for other cases the request will pass through to the origin. For our preview, this will be a fake origin website returning \"Welcome\". - **reject** indicates a Reject queue. 4. `event`: Used to preview a waiting room event. - **none** indicates no event is occurring. - **prequeueing** indicates that an event is prequeueing (between `prequeue_start_time` and `event_start_time`). - **started** indicates that an event has started (between `event_start_time` and `event_end_time`). 5. `shuffle_at_event_start`: Boolean indicating if the event will shuffle users in the prequeue when it starts. This can only be set to **true** if an event is active (`event` is not **none**). For example, you can make a request to `http://waitingrooms.dev/preview/<uuid>?force_queue=false&queue_is_full=false&queueing_method=random&event=started&shuffle_at_event_start=true` 6. `waitTime`: Non-zero, positive integer indicating the estimated wait time in minutes. The default value is 10 minutes. For example, you can make a request to `http://waitingrooms.dev/preview/<uuid>?waitTime=50` to configure the estimated wait time as 50 minutes.

```sql
EXEC cloudflare.waiting_rooms.waiting_rooms.preview 
@zone_id='{{ zone_id }}' --required 
@@json=
'{
"custom_html": "{{ custom_html }}"
}'
;
```
</TabItem>
</Tabs>
