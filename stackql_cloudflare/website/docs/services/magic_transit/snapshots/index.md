--- 
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - magic_transit
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="cloudflare.magic_transit.snapshots" /></td></tr>
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
    <td><CopyableCode code="bonds" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="count_reclaim_failures" /></td>
    <td><code>number</code></td>
    <td>Count of failures to reclaim space</td>
</tr>
<tr>
    <td><CopyableCode code="count_reclaimed_paths" /></td>
    <td><code>number</code></td>
    <td>Count of reclaimed paths</td>
</tr>
<tr>
    <td><CopyableCode code="count_record_failed" /></td>
    <td><code>number</code></td>
    <td>Count of failed snapshot recordings</td>
</tr>
<tr>
    <td><CopyableCode code="count_transmit_failures" /></td>
    <td><code>number</code></td>
    <td>Count of failed snapshot transmissions</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_count" /></td>
    <td><code>number</code></td>
    <td>Count of processors/cores</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_pressure_10s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 10 second window that tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_pressure_300s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 5 minute window that tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_pressure_60s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 1 minute window that tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_pressure_total_us" /></td>
    <td><code>number</code></td>
    <td>Total stall time (microseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_guest_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent running a virtual CPU or guest OS (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_guest_nice_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent running a niced guest (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_idle_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent in idle state (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_iowait_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent wait for I/O to complete (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_irq_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent servicing interrupts (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_nice_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent in low-priority user mode (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_softirq_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent servicing softirqs (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_steal_ms" /></td>
    <td><code>number</code></td>
    <td>Time stolen (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_system_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent in system mode (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu_time_user_ms" /></td>
    <td><code>number</code></td>
    <td>Time spent in user mode (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="delta" /></td>
    <td><code>number</code></td>
    <td>Number of network operations applied during state transition</td>
</tr>
<tr>
    <td><CopyableCode code="dhcp_leases" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="epsilon" /></td>
    <td><code>number</code></td>
    <td>Simulated number of network operations applied during state transition</td>
</tr>
<tr>
    <td><CopyableCode code="ha_state" /></td>
    <td><code>string</code></td>
    <td>Name of high availability state</td>
</tr>
<tr>
    <td><CopyableCode code="ha_value" /></td>
    <td><code>number</code></td>
    <td>Numeric value associated with high availability state (0 = disabled, 1 = active, 2 = standby, 3 = stopped, 4 = fault)</td>
</tr>
<tr>
    <td><CopyableCode code="interfaces" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_full_10s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 10 second window that all tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_full_300s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 5 minute window that all tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_full_60s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 1 minute window that all tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_full_total_us" /></td>
    <td><code>number</code></td>
    <td>Total stall time (microseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_some_10s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 10 second window that some tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_some_300s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 3 minute window that some tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_some_60s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 1 minute window that some tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="io_pressure_some_total_us" /></td>
    <td><code>number</code></td>
    <td>Total stall time (microseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="kernel_btime" /></td>
    <td><code>number</code></td>
    <td>Boot time (seconds since Unix epoch)</td>
</tr>
<tr>
    <td><CopyableCode code="kernel_ctxt" /></td>
    <td><code>number</code></td>
    <td>Number of context switches that the system underwent</td>
</tr>
<tr>
    <td><CopyableCode code="kernel_processes" /></td>
    <td><code>number</code></td>
    <td>Number of forks since boot</td>
</tr>
<tr>
    <td><CopyableCode code="kernel_processes_blocked" /></td>
    <td><code>number</code></td>
    <td>Number of processes blocked waiting for I/O</td>
</tr>
<tr>
    <td><CopyableCode code="kernel_processes_running" /></td>
    <td><code>number</code></td>
    <td>Number of processes in runnable state</td>
</tr>
<tr>
    <td><CopyableCode code="load_average_15m" /></td>
    <td><code>number</code></td>
    <td>The fifteen-minute load average</td>
</tr>
<tr>
    <td><CopyableCode code="load_average_1m" /></td>
    <td><code>number</code></td>
    <td>The one-minute load average</td>
</tr>
<tr>
    <td><CopyableCode code="load_average_5m" /></td>
    <td><code>number</code></td>
    <td>The five-minute load average</td>
</tr>
<tr>
    <td><CopyableCode code="load_average_cur" /></td>
    <td><code>number</code></td>
    <td>Number of currently runnable kernel scheduling entities</td>
</tr>
<tr>
    <td><CopyableCode code="load_average_max" /></td>
    <td><code>number</code></td>
    <td>Number of kernel scheduling entities that currently exist on the system</td>
</tr>
<tr>
    <td><CopyableCode code="memory_active_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory that has been used more recently</td>
</tr>
<tr>
    <td><CopyableCode code="memory_anon_hugepages_bytes" /></td>
    <td><code>number</code></td>
    <td>Non-file backed huge pages mapped into user-space page tables</td>
</tr>
<tr>
    <td><CopyableCode code="memory_anon_pages_bytes" /></td>
    <td><code>number</code></td>
    <td>Non-file backed pages mapped into user-space page tables</td>
</tr>
<tr>
    <td><CopyableCode code="memory_available_bytes" /></td>
    <td><code>number</code></td>
    <td>Estimate of how much memory is available for starting new applications</td>
</tr>
<tr>
    <td><CopyableCode code="memory_bounce_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory used for block device bounce buffers</td>
</tr>
<tr>
    <td><CopyableCode code="memory_buffers_bytes" /></td>
    <td><code>number</code></td>
    <td>Relatively temporary storage for raw disk blocks</td>
</tr>
<tr>
    <td><CopyableCode code="memory_cached_bytes" /></td>
    <td><code>number</code></td>
    <td>In-memory cache for files read from the disk</td>
</tr>
<tr>
    <td><CopyableCode code="memory_cma_free_bytes" /></td>
    <td><code>number</code></td>
    <td>Free CMA (Contiguous Memory Allocator) pages</td>
</tr>
<tr>
    <td><CopyableCode code="memory_cma_total_bytes" /></td>
    <td><code>number</code></td>
    <td>Total CMA (Contiguous Memory Allocator) pages</td>
</tr>
<tr>
    <td><CopyableCode code="memory_commit_limit_bytes" /></td>
    <td><code>number</code></td>
    <td>Total amount of memory currently available to be allocated on the system</td>
</tr>
<tr>
    <td><CopyableCode code="memory_committed_as_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of memory presently allocated on the system</td>
</tr>
<tr>
    <td><CopyableCode code="memory_dirty_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory which is waiting to get written back to the disk</td>
</tr>
<tr>
    <td><CopyableCode code="memory_free_bytes" /></td>
    <td><code>number</code></td>
    <td>The sum of LowFree and HighFree</td>
</tr>
<tr>
    <td><CopyableCode code="memory_high_free_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of free highmem</td>
</tr>
<tr>
    <td><CopyableCode code="memory_high_total_bytes" /></td>
    <td><code>number</code></td>
    <td>Total amount of highmem</td>
</tr>
<tr>
    <td><CopyableCode code="memory_hugepages_free" /></td>
    <td><code>number</code></td>
    <td>The number of huge pages in the pool that are not yet allocated</td>
</tr>
<tr>
    <td><CopyableCode code="memory_hugepages_rsvd" /></td>
    <td><code>number</code></td>
    <td>Number of huge pages for which a commitment has been made, but no allocation has yet been made</td>
</tr>
<tr>
    <td><CopyableCode code="memory_hugepages_surp" /></td>
    <td><code>number</code></td>
    <td>Number of huge pages in the pool above the threshold</td>
</tr>
<tr>
    <td><CopyableCode code="memory_hugepages_total" /></td>
    <td><code>number</code></td>
    <td>The size of the pool of huge pages</td>
</tr>
<tr>
    <td><CopyableCode code="memory_hugepagesize_bytes" /></td>
    <td><code>number</code></td>
    <td>The size of huge pages</td>
</tr>
<tr>
    <td><CopyableCode code="memory_inactive_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory which has been less recently used</td>
</tr>
<tr>
    <td><CopyableCode code="memory_k_reclaimable_bytes" /></td>
    <td><code>number</code></td>
    <td>Kernel allocations that the kernel will attempt to reclaim under memory pressure</td>
</tr>
<tr>
    <td><CopyableCode code="memory_kernel_stack_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of memory allocated to kernel stacks</td>
</tr>
<tr>
    <td><CopyableCode code="memory_low_free_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of free lowmem</td>
</tr>
<tr>
    <td><CopyableCode code="memory_low_total_bytes" /></td>
    <td><code>number</code></td>
    <td>Total amount of lowmem</td>
</tr>
<tr>
    <td><CopyableCode code="memory_mapped_bytes" /></td>
    <td><code>number</code></td>
    <td>Files which have been mapped into memory</td>
</tr>
<tr>
    <td><CopyableCode code="memory_page_tables_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of memory dedicated to the lowest level of page tables</td>
</tr>
<tr>
    <td><CopyableCode code="memory_per_cpu_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory allocated to the per-cpu alloctor used to back per-cpu allocations</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_full_10s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 10 second window that all tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_full_300s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 5 minute window that all tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_full_60s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 1 minute window that all tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_full_total_us" /></td>
    <td><code>number</code></td>
    <td>Total stall time (microseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_some_10s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 10 second window that some tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_some_300s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 5 minute window that some tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_some_60s" /></td>
    <td><code>number</code></td>
    <td>Percentage of time over a 1 minute window that some tasks were stalled</td>
</tr>
<tr>
    <td><CopyableCode code="memory_pressure_some_total_us" /></td>
    <td><code>number</code></td>
    <td>Total stall time (microseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="memory_s_reclaimable_bytes" /></td>
    <td><code>number</code></td>
    <td>Part of slab that can be reclaimed on memory pressure</td>
</tr>
<tr>
    <td><CopyableCode code="memory_s_unreclaim_bytes" /></td>
    <td><code>number</code></td>
    <td>Part of slab that cannot be reclaimed on memory pressure</td>
</tr>
<tr>
    <td><CopyableCode code="memory_secondary_page_tables_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of memory dedicated to the lowest level of page tables</td>
</tr>
<tr>
    <td><CopyableCode code="memory_shmem_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of memory consumed by tmpfs</td>
</tr>
<tr>
    <td><CopyableCode code="memory_shmem_hugepages_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory used by shmem and tmpfs, allocated with huge pages</td>
</tr>
<tr>
    <td><CopyableCode code="memory_shmem_pmd_mapped_bytes" /></td>
    <td><code>number</code></td>
    <td>Shared memory mapped into user space with huge pages</td>
</tr>
<tr>
    <td><CopyableCode code="memory_slab_bytes" /></td>
    <td><code>number</code></td>
    <td>In-kernel data structures cache</td>
</tr>
<tr>
    <td><CopyableCode code="memory_swap_cached_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory swapped out and back in while still in swap file</td>
</tr>
<tr>
    <td><CopyableCode code="memory_swap_free_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of swap space that is currently unused</td>
</tr>
<tr>
    <td><CopyableCode code="memory_swap_total_bytes" /></td>
    <td><code>number</code></td>
    <td>Total amount of swap space available</td>
</tr>
<tr>
    <td><CopyableCode code="memory_total_bytes" /></td>
    <td><code>number</code></td>
    <td>Total usable RAM</td>
</tr>
<tr>
    <td><CopyableCode code="memory_vmalloc_chunk_bytes" /></td>
    <td><code>number</code></td>
    <td>Largest contiguous block of vmalloc area which is free</td>
</tr>
<tr>
    <td><CopyableCode code="memory_vmalloc_total_bytes" /></td>
    <td><code>number</code></td>
    <td>Total size of vmalloc memory area</td>
</tr>
<tr>
    <td><CopyableCode code="memory_vmalloc_used_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of vmalloc area which is used</td>
</tr>
<tr>
    <td><CopyableCode code="memory_writeback_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory which is actively being written back to the disk</td>
</tr>
<tr>
    <td><CopyableCode code="memory_writeback_tmp_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory used by FUSE for temporary writeback buffers</td>
</tr>
<tr>
    <td><CopyableCode code="memory_z_swap_bytes" /></td>
    <td><code>number</code></td>
    <td>Memory consumed by the zswap backend, compressed</td>
</tr>
<tr>
    <td><CopyableCode code="memory_z_swapped_bytes" /></td>
    <td><code>number</code></td>
    <td>Amount of anonymous memory stored in zswap, uncompressed</td>
</tr>
<tr>
    <td><CopyableCode code="mounts" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="netdevs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>Platform identifier</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_addr_mask_reps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Address Mask Reply messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_addr_masks" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Address Mask Request messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_csum_errors" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP messages received with bad checksums</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_dest_unreachs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Destination Unreachable messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_echo_reps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Echo Reply messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_echos" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Echo (request) messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_errors" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP messages received with ICMP-specific errors</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_msgs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_parm_probs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Parameter Problem messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_redirects" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Redirect messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_src_quenchs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Source Quench messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_time_excds" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Time Exceeded messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_timestamp_reps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Address Mask Request messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_in_timestamps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Timestamp (request) messages received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_addr_mask_reps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Address Mask Reply messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_addr_masks" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Address Mask Request messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_dest_unreachs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Destination Unreachable messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_echo_reps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Echo Reply messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_echos" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Echo (request) messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_errors" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP messages which this entity did not send due to ICMP-specific errors</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_msgs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP messages attempted to send</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_parm_probs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Parameter Problem messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_redirects" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Redirect messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_src_quenchs" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Source Quench messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_time_excds" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Time Exceeded messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_timestamp_reps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Timestamp Reply messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_icmp_out_timestamps" /></td>
    <td><code>number</code></td>
    <td>Number of ICMP Timestamp (request) messages sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_default_ttl" /></td>
    <td><code>number</code></td>
    <td>Default value of the Time-To-Live field of the IP header</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_forw_datagrams" /></td>
    <td><code>number</code></td>
    <td>Number of datagrams forwarded to their final destination</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_forwarding_enabled" /></td>
    <td><code>boolean</code></td>
    <td>Set when acting as an IP gateway</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_frag_creates" /></td>
    <td><code>number</code></td>
    <td>Number of datagrams generated by fragmentation</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_frag_fails" /></td>
    <td><code>number</code></td>
    <td>Number of datagrams discarded because fragmentation failed</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_frag_oks" /></td>
    <td><code>number</code></td>
    <td>Number of datagrams successfully fragmented</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_in_addr_errors" /></td>
    <td><code>number</code></td>
    <td>Number of input datagrams discarded due to errors in the IP address</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_in_delivers" /></td>
    <td><code>number</code></td>
    <td>Number of input datagrams successfully delivered to IP user-protocols</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_in_discards" /></td>
    <td><code>number</code></td>
    <td>Number of input datagrams otherwise discarded</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_in_hdr_errors" /></td>
    <td><code>number</code></td>
    <td>Number of input datagrams discarded due to errors in the IP header</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_in_receives" /></td>
    <td><code>number</code></td>
    <td>Number of input datagrams received from interfaces</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_in_unknown_protos" /></td>
    <td><code>number</code></td>
    <td>Number of input datagrams discarded due unknown or unsupported protocol</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_out_discards" /></td>
    <td><code>number</code></td>
    <td>Number of output datagrams otherwise discarded</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_out_no_routes" /></td>
    <td><code>number</code></td>
    <td>Number of output datagrams discarded because no route matched</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_out_requests" /></td>
    <td><code>number</code></td>
    <td>Number of datagrams supplied for transmission</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_reasm_fails" /></td>
    <td><code>number</code></td>
    <td>Number of failures detected by the reassembly algorithm</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_reasm_oks" /></td>
    <td><code>number</code></td>
    <td>Number of datagrams successfully reassembled</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_reasm_reqds" /></td>
    <td><code>number</code></td>
    <td>Number of fragments received which needed to be reassembled</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_ip_reasm_timeout" /></td>
    <td><code>number</code></td>
    <td>Number of seconds fragments are held while awaiting reassembly</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_active_opens" /></td>
    <td><code>number</code></td>
    <td>Number of times TCP transitions to SYN-SENT from CLOSED</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_attempt_fails" /></td>
    <td><code>number</code></td>
    <td>Number of times TCP transitions to CLOSED from SYN-SENT or SYN-RCVD, plus transitions to LISTEN from SYN-RCVD</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_curr_estab" /></td>
    <td><code>number</code></td>
    <td>Number of TCP connections in ESTABLISHED or CLOSE-WAIT</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_estab_resets" /></td>
    <td><code>number</code></td>
    <td>Number of times TCP transitions to CLOSED from ESTABLISHED or CLOSE-WAIT</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_in_csum_errors" /></td>
    <td><code>number</code></td>
    <td>Number of TCP segments received with checksum errors</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_in_errs" /></td>
    <td><code>number</code></td>
    <td>Number of TCP segments received in error</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_in_segs" /></td>
    <td><code>number</code></td>
    <td>Number of TCP segments received</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_max_conn" /></td>
    <td><code>number</code></td>
    <td>Limit on the total number of TCP connections</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_out_rsts" /></td>
    <td><code>number</code></td>
    <td>Number of TCP segments sent with RST flag</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_out_segs" /></td>
    <td><code>number</code></td>
    <td>Number of TCP segments sent</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_passive_opens" /></td>
    <td><code>number</code></td>
    <td>Number of times TCP transitions to SYN-RCVD from LISTEN</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_retrans_segs" /></td>
    <td><code>number</code></td>
    <td>Number of TCP segments retransmitted</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_rto_max" /></td>
    <td><code>number</code></td>
    <td>Maximum value permitted by a TCP implementation for the retransmission timeout (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_tcp_rto_min" /></td>
    <td><code>number</code></td>
    <td>Minimum value permitted by a TCP implementation for the retransmission timeout (milliseconds)</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_udp_in_datagrams" /></td>
    <td><code>number</code></td>
    <td>Number of UDP datagrams delivered to UDP applications</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_udp_in_errors" /></td>
    <td><code>number</code></td>
    <td>Number of UDP datagrams failed to be delivered for reasons other than lack of application at the destination port</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_udp_no_ports" /></td>
    <td><code>number</code></td>
    <td>Number of UDP datagrams received for which there was not application at the destination port</td>
</tr>
<tr>
    <td><CopyableCode code="snmp_udp_out_datagrams" /></td>
    <td><code>number</code></td>
    <td>Number of UDP datagrams sent</td>
</tr>
<tr>
    <td><CopyableCode code="system_boot_time_s" /></td>
    <td><code>number</code></td>
    <td>Boottime of the system (seconds since the Unix epoch)</td>
</tr>
<tr>
    <td><CopyableCode code="t" /></td>
    <td><code>number</code></td>
    <td>Time the Snapshot was recorded (seconds since the Unix epoch)</td>
</tr>
<tr>
    <td><CopyableCode code="thermals" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tunnels" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uptime_idle_ms" /></td>
    <td><code>number</code></td>
    <td>Sum of how much time each core has spent idle</td>
</tr>
<tr>
    <td><CopyableCode code="uptime_total_ms" /></td>
    <td><code>number</code></td>
    <td>Uptime of the system, including time spent in suspend</td>
</tr>
<tr>
    <td><CopyableCode code="v" /></td>
    <td><code>string</code></td>
    <td>Version</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td><CopyableCode code="a" /></td>
    <td><code>number</code></td>
    <td>Time the Snapshot was collected (seconds since the Unix epoch)</td>
</tr>
<tr>
    <td><CopyableCode code="t" /></td>
    <td><code>number</code></td>
    <td>Time the Snapshot was recorded (seconds since the Unix epoch)</td>
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a>, <a href="#parameter-snapshot_t"><code>snapshot_t</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-connector_id"><code>connector_id</code></a></td>
    <td><a href="#parameter-from"><code>from</code></a>, <a href="#parameter-to"><code>to</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-cursor"><code>cursor</code></a></td>
    <td></td>
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
<tr id="parameter-connector_id">
    <td><CopyableCode code="connector_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-snapshot_t">
    <td><CopyableCode code="snapshot_t" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-cursor">
    <td><CopyableCode code="cursor" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-from">
    <td><CopyableCode code="from" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>number</code></td>
    <td></td>
</tr>
<tr id="parameter-to">
    <td><CopyableCode code="to" /></td>
    <td><code>number</code></td>
    <td></td>
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

OK

```sql
SELECT
bonds,
count_reclaim_failures,
count_reclaimed_paths,
count_record_failed,
count_transmit_failures,
cpu_count,
cpu_pressure_10s,
cpu_pressure_300s,
cpu_pressure_60s,
cpu_pressure_total_us,
cpu_time_guest_ms,
cpu_time_guest_nice_ms,
cpu_time_idle_ms,
cpu_time_iowait_ms,
cpu_time_irq_ms,
cpu_time_nice_ms,
cpu_time_softirq_ms,
cpu_time_steal_ms,
cpu_time_system_ms,
cpu_time_user_ms,
delta,
dhcp_leases,
disks,
epsilon,
ha_state,
ha_value,
interfaces,
io_pressure_full_10s,
io_pressure_full_300s,
io_pressure_full_60s,
io_pressure_full_total_us,
io_pressure_some_10s,
io_pressure_some_300s,
io_pressure_some_60s,
io_pressure_some_total_us,
kernel_btime,
kernel_ctxt,
kernel_processes,
kernel_processes_blocked,
kernel_processes_running,
load_average_15m,
load_average_1m,
load_average_5m,
load_average_cur,
load_average_max,
memory_active_bytes,
memory_anon_hugepages_bytes,
memory_anon_pages_bytes,
memory_available_bytes,
memory_bounce_bytes,
memory_buffers_bytes,
memory_cached_bytes,
memory_cma_free_bytes,
memory_cma_total_bytes,
memory_commit_limit_bytes,
memory_committed_as_bytes,
memory_dirty_bytes,
memory_free_bytes,
memory_high_free_bytes,
memory_high_total_bytes,
memory_hugepages_free,
memory_hugepages_rsvd,
memory_hugepages_surp,
memory_hugepages_total,
memory_hugepagesize_bytes,
memory_inactive_bytes,
memory_k_reclaimable_bytes,
memory_kernel_stack_bytes,
memory_low_free_bytes,
memory_low_total_bytes,
memory_mapped_bytes,
memory_page_tables_bytes,
memory_per_cpu_bytes,
memory_pressure_full_10s,
memory_pressure_full_300s,
memory_pressure_full_60s,
memory_pressure_full_total_us,
memory_pressure_some_10s,
memory_pressure_some_300s,
memory_pressure_some_60s,
memory_pressure_some_total_us,
memory_s_reclaimable_bytes,
memory_s_unreclaim_bytes,
memory_secondary_page_tables_bytes,
memory_shmem_bytes,
memory_shmem_hugepages_bytes,
memory_shmem_pmd_mapped_bytes,
memory_slab_bytes,
memory_swap_cached_bytes,
memory_swap_free_bytes,
memory_swap_total_bytes,
memory_total_bytes,
memory_vmalloc_chunk_bytes,
memory_vmalloc_total_bytes,
memory_vmalloc_used_bytes,
memory_writeback_bytes,
memory_writeback_tmp_bytes,
memory_z_swap_bytes,
memory_z_swapped_bytes,
mounts,
netdevs,
platform,
snmp_icmp_in_addr_mask_reps,
snmp_icmp_in_addr_masks,
snmp_icmp_in_csum_errors,
snmp_icmp_in_dest_unreachs,
snmp_icmp_in_echo_reps,
snmp_icmp_in_echos,
snmp_icmp_in_errors,
snmp_icmp_in_msgs,
snmp_icmp_in_parm_probs,
snmp_icmp_in_redirects,
snmp_icmp_in_src_quenchs,
snmp_icmp_in_time_excds,
snmp_icmp_in_timestamp_reps,
snmp_icmp_in_timestamps,
snmp_icmp_out_addr_mask_reps,
snmp_icmp_out_addr_masks,
snmp_icmp_out_dest_unreachs,
snmp_icmp_out_echo_reps,
snmp_icmp_out_echos,
snmp_icmp_out_errors,
snmp_icmp_out_msgs,
snmp_icmp_out_parm_probs,
snmp_icmp_out_redirects,
snmp_icmp_out_src_quenchs,
snmp_icmp_out_time_excds,
snmp_icmp_out_timestamp_reps,
snmp_icmp_out_timestamps,
snmp_ip_default_ttl,
snmp_ip_forw_datagrams,
snmp_ip_forwarding_enabled,
snmp_ip_frag_creates,
snmp_ip_frag_fails,
snmp_ip_frag_oks,
snmp_ip_in_addr_errors,
snmp_ip_in_delivers,
snmp_ip_in_discards,
snmp_ip_in_hdr_errors,
snmp_ip_in_receives,
snmp_ip_in_unknown_protos,
snmp_ip_out_discards,
snmp_ip_out_no_routes,
snmp_ip_out_requests,
snmp_ip_reasm_fails,
snmp_ip_reasm_oks,
snmp_ip_reasm_reqds,
snmp_ip_reasm_timeout,
snmp_tcp_active_opens,
snmp_tcp_attempt_fails,
snmp_tcp_curr_estab,
snmp_tcp_estab_resets,
snmp_tcp_in_csum_errors,
snmp_tcp_in_errs,
snmp_tcp_in_segs,
snmp_tcp_max_conn,
snmp_tcp_out_rsts,
snmp_tcp_out_segs,
snmp_tcp_passive_opens,
snmp_tcp_retrans_segs,
snmp_tcp_rto_max,
snmp_tcp_rto_min,
snmp_udp_in_datagrams,
snmp_udp_in_errors,
snmp_udp_no_ports,
snmp_udp_out_datagrams,
system_boot_time_s,
t,
thermals,
tunnels,
uptime_idle_ms,
uptime_total_ms,
v
FROM cloudflare.magic_transit.snapshots
WHERE account_id = '{{ account_id }}' -- required
AND connector_id = '{{ connector_id }}' -- required
AND snapshot_t = '{{ snapshot_t }}' -- required
;
```
</TabItem>
<TabItem value="list">

OK

```sql
SELECT
a,
t
FROM cloudflare.magic_transit.snapshots
WHERE account_id = '{{ account_id }}' -- required
AND connector_id = '{{ connector_id }}' -- required
AND from = '{{ from }}'
AND to = '{{ to }}'
AND limit = '{{ limit }}'
AND cursor = '{{ cursor }}'
;
```
</TabItem>
</Tabs>
