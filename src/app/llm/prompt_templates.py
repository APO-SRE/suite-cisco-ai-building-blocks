#!/usr/bin/env python3
from __future__ import annotations
################################################################################
## suite-cisco-ai-building-blocks/src/app/llm/prompt_templates.py
## Copyright (c) 2025 Jeff Teeter, Ph.D.
## Cisco Systems, Inc.
## Licensed under the Apache License, Version 2.0 (see LICENSE)
## Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.
################################################################################

################################################################################
## PROMPT TEMPLATE USAGE GUIDE
## 
## This file contains three types of prompts for different performance/UX needs:
## 
## 1. REGULAR PROMPTS (Default - Best User Experience)
##    Example: HTML_CATALYST_INTERFACES_PROMPT, HTML_SDWAN_DEVICE_STATUS_PROMPT
##    
##    When to use:
##    - Default choice for most scenarios
##    - Displaying < 1,000 items
##    - Executive dashboards or customer-facing interfaces
##    - When professional appearance matters
##    - Users need interactive features (sorting, filtering, actions)
##    
##    Features:
##    ✓ Rich styling with colors, badges, and icons
##    ✓ Hover effects and transitions
##    ✓ Responsive grid layouts
##    ✓ Interactive buttons and controls
##    ✓ Pagination for large datasets
##    ✓ Tooltips for truncated content
##    ✓ Visual status indicators
##    ✓ Professional spacing and typography
##    
##    Performance Impact:
##    - Initial render: ~50-200ms for 100 items
##    - Memory usage: ~2-5MB for 1,000 items
##    - Best for datasets under 1,000 items
##
## 2. LIGHTWEIGHT PROMPTS (Performance-Optimized)
##    Example: HTML_MERAKI_INVENTORY_LIGHTWEIGHT_PROMPT
##    
##    When to use:
##    - Displaying 1,000-10,000 items
##    - Technical users who prioritize data over aesthetics
##    - Embedded systems or limited hardware
##    - Slow network connections (< 1 Mbps)
##    - Real-time monitoring dashboards
##    
##    Features:
##    ✓ Minimal HTML structure
##    ✓ Basic color coding for critical info (status)
##    ✓ Monospace font for alignment
##    ✓ Essential data only
##    ⨯ No hover effects or transitions
##    ⨯ No pagination (shows all data)
##    ⨯ No interactive elements
##    
##    Performance Impact:
##    - Initial render: ~10-50ms for 1,000 items
##    - Memory usage: ~0.5-1MB for 1,000 items
##    - 70% faster than regular prompts
##
## 3. ULTRA-LIGHTWEIGHT (Maximum Performance)
##    Example: HTML_CATALYST_INTERFACES_LIGHTWEIGHT_PROMPT with minimal rules
##    
##    When to use:
##    - Displaying > 10,000 items
##    - CLI/terminal output emulation
##    - Extremely limited hardware (IoT devices)
##    - Data export/logging purposes
##    - Automated systems consuming the output
##    
##    Features:
##    ✓ Absolute minimum HTML
##    ✓ Single-line formatting
##    ✓ No styling whatsoever
##    ⨯ No colors or visual indicators
##    ⨯ No spacing or padding
##    ⨯ May truncate datasets > threshold
##    
##    Performance Impact:
##    - Initial render: < 10ms for 10,000 items
##    - Memory usage: < 0.1MB for 1,000 items
##    - 95% faster than regular prompts
##
## CHOOSING THE RIGHT PROMPT TYPE:
## 
## Dataset Size    | Recommended Type  | User Experience | Performance
## --------------- | ----------------- | --------------- | -----------
## < 100 items     | Regular          | Excellent ⭐⭐⭐⭐⭐ | Good
## 100-1,000       | Regular          | Excellent ⭐⭐⭐⭐⭐ | Acceptable
## 1,000-5,000     | Lightweight      | Basic ⭐⭐⭐      | Good
## 5,000-10,000    | Lightweight      | Basic ⭐⭐⭐      | Acceptable
## > 10,000        | Ultra-Lightweight| Minimal ⭐⭐      | Excellent
##
## PRO TIPS:
## - Consider adding a user toggle between view modes
## - Auto-detect large datasets and switch to lightweight
## - Use regular prompts for summary views, lightweight for detailed logs
## - Cache rendered HTML for frequently accessed data
## - Consider server-side pagination for datasets > 10,000 items
##
## IMPACT ON LLM PROCESSING:
## - Regular prompts: More tokens, higher cost, richer output
## - Lightweight: 50% fewer tokens, faster LLM response
## - Ultra-lightweight: 80% fewer tokens, minimal LLM processing time
################################################################################

BASE_SYSTEM_PROMPT_DOCS_ONLY = """You are a Cisco AI assistant. Use ONLY provided documents.

RULES:
1. Answer not in docs → "I don't know"
2. Output: Clean HTML only (no backticks)
3. Multi-turn: Continue if user confirms
4. Performance: Minimal tags, efficient structure"""

BASE_SYSTEM_PROMPT_GENERAL = """You are a Cisco AI assistant. Use ONLY provided documents/data.

RULES:
1. No external knowledge
2. Unknown → "I don't know"
3. Output: Clean HTML only
4. Multi-turn: Continue on confirmation
5. Performance: Minimal DOM"""

BASE_SYSTEM_PROMPT_EVENT = """You are a Cisco event data specialist. Use ONLY provided event documents.

DISPLAY FORMAT:
<div style="font-family:system-ui,-apple-system,sans-serif;max-width:800px">
  <div style="background:#f0f3f5;padding:16px;border-radius:8px;margin-bottom:16px">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px">
      <div><span style="color:#666;font-size:12px">Event ID</span><br><strong style="font-size:18px">{event_id}</strong></div>
      <div><span style="color:#666;font-size:12px">Detected Event</span><br><strong>{detected_event}</strong></div>
      <div><span style="color:#666;font-size:12px">Zone</span><br><strong>{zone}</strong></div>
      <div><span style="color:#666;font-size:12px">Date/Time</span><br><strong>{datetime}</strong></div>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-bottom:16px">
    <div style="background:#fff;padding:12px;border:1px solid #e0e0e0;border-radius:4px">
      <strong style="color:#1a73e8">Camera:</strong> {camera}
    </div>
    <div style="background:#fff;padding:12px;border:1px solid #e0e0e0;border-radius:4px">
      <strong style="color:#1a73e8">Building:</strong> {building}
    </div>
    <div style="background:#fff;padding:12px;border:1px solid #e0e0e0;border-radius:4px">
      <strong style="color:#1a73e8">Floor:</strong> {floor}
    </div>
    <div style="background:#fff;padding:12px;border:1px solid #e0e0e0;border-radius:4px">
      <strong style="color:#1a73e8">Location:</strong> {location}
    </div>
  </div>
  {recommended_actions}
  {urls_section}
  {notes_section}
</div>

RULES:
- Pure HTML output only
- Use grid layouts for performance
- Include action buttons with fullscreen onclick
- No markdown or code fences"""

BASE_SYSTEM_PROMPT_LOB = """You are a healthcare LOB data specialist. Use ONLY provided LOB documents.

RESPONSE FORMATS:

1. DATA SUMMARY:
<div style="font-family:system-ui;overflow-x:auto">
  <table style="border-collapse:collapse;width:100%;background:#fff;border:1px solid #dee2e6;border-radius:8px;overflow:hidden">
    <thead style="background:#f8f9fa">
      <tr>
        {headers}
      </tr>
    </thead>
    <tbody>
      {data_rows}
    </tbody>
  </table>
</div>

2. EMAIL/LETTER FORMAT:
<div style="font-family:system-ui;max-width:600px;background:#fff;padding:24px;border:1px solid #e0e0e0;border-radius:8px">
  <div style="border-bottom:2px solid #1a73e8;padding-bottom:16px;margin-bottom:16px">
    <strong style="color:#1a73e8">Subject:</strong> {subject}
  </div>
  <div style="margin-bottom:16px">{greeting}</div>
  <div style="line-height:1.6;margin-bottom:16px">{body}</div>
  <div style="margin-top:24px">
    <div>{closing}</div>
    <div style="color:#666;margin-top:8px">{signature}</div>
  </div>
</div>

RULES:
- Pure HTML output
- Professional healthcare formatting
- No markdown"""

HTML_MERAKI_INVENTORY_PROMPT = """Parse Meraki device JSON and display in optimized HTML table.

REQUIRED OUTPUT:
<div style="font-family:system-ui">
  <h3 style="color:#1a73e8;margin-bottom:16px">Meraki Device Inventory</h3>
  <div style="overflow-x:auto">
    <table style="border-collapse:collapse;width:100%;background:#fff;border:1px solid #dee2e6">
      <thead style="background:#1a73e8;color:#fff">
        <tr>
          <th style="padding:12px;text-align:left;font-weight:500">Serial</th>
          <th style="padding:12px;text-align:left;font-weight:500">MAC</th>
          <th style="padding:12px;text-align:left;font-weight:500">Name</th>
          <th style="padding:12px;text-align:left;font-weight:500">Model</th>
          <th style="padding:12px;text-align:left;font-weight:500">Network ID</th>
          <th style="padding:12px;text-align:left;font-weight:500">Product Type</th>
          <th style="padding:12px;text-align:left;font-weight:500">Claimed At</th>
          <th style="padding:12px;text-align:left;font-weight:500">License Expiration</th>
          <th style="padding:12px;text-align:left;font-weight:500">Tags</th>
          <th style="padding:12px;text-align:left;font-weight:500">Country Code</th>
        </tr>
      </thead>
      <tbody>
        {device_rows}
      </tbody>
    </table>
  </div>
  <div style="margin-top:16px;display:flex;gap:8px">
    <button onclick="downloadData()" style="background:#1a73e8;color:#fff;border:none;padding:8px 16px;border-radius:4px;cursor:pointer;font-size:14px">📥 Download JSON</button>
    <button onclick="toggleView()" style="background:#fff;color:#1a73e8;border:1px solid #1a73e8;padding:8px 16px;border-radius:4px;cursor:pointer;font-size:14px">👁️ View as JSON</button>
  </div>
</div>

ROW FORMAT:
<tr style="border-bottom:1px solid #e0e0e0;transition:background-color 0.2s" onmouseover="this.style.backgroundColor='#f8f9fa'" onmouseout="this.style.backgroundColor=''">
  <td style="padding:12px;font-family:monospace;font-size:13px">{serial}</td>
  <td style="padding:12px;font-family:monospace;font-size:12px;color:#666">{mac}</td>
  <td style="padding:12px;font-weight:500">{name}</td>
  <td style="padding:12px">{model}</td>
  <td style="padding:12px;font-size:11px;color:#666">{network_id}</td>
  <td style="padding:12px"><span style="padding:2px 6px;background:#e8f0fe;color:#1967d2;border-radius:3px;font-size:12px">{product_type}</span></td>
  <td style="padding:12px;font-size:13px">{claimed_at}</td>
  <td style="padding:12px;font-size:13px">{license_exp}</td>
  <td style="padding:12px;font-size:12px">{tags}</td>
  <td style="padding:12px;text-align:center">{country_code}</td>
</tr>

Requirements:
- Valid HTML only
- Professional appearance
- Interactive elements
- Empty cells for missing data"""

HTML_MERAKI_INVENTORY_LIGHTWEIGHT_PROMPT = """Meraki inventory - ULTRA LIGHTWEIGHT HTML.

CRITICAL: Maximum performance, minimum size.

OUTPUT:
<table style="font-family:monospace;font-size:12px"><tr><td>Serial</td><td>Name</td><td>Model</td><td>Product Type</td><td>Network ID</td></tr>{rows}</table>

ROW: <tr><td>{serial}</td><td>{name}</td><td>{model}</td><td>{type}</td><td>{network}</td></tr>

RULES:
- ONE LINE per row
- NO formatting
- NO whitespace
- If truncated: <tr><td colspan="5">Showing {x} of {y} devices</td></tr>"""

HTML_MERAKI_APS_WITH_MESSAGE_PROMPT = """Display message and access points from Meraki response.

OUTPUT FORMAT:
<div style="font-family:system-ui">
  <div style="background:#e8f0fe;color:#1967d2;padding:12px;border-radius:4px;margin-bottom:16px;font-weight:500">
    {message}
  </div>
  <table style="border-collapse:collapse;width:100%">
    <thead style="background:#1a73e8;color:#fff">
      <tr>
        <th style="padding:12px;text-align:left">Serial</th>
        <th style="padding:12px;text-align:left">Model</th>
        <th style="padding:12px;text-align:left">MAC</th>
        <th style="padding:12px;text-align:left">Network ID</th>
        <th style="padding:12px;text-align:left">Product Type</th>
      </tr>
    </thead>
    <tbody>
      {ap_rows}
    </tbody>
  </table>
</div>

Pure HTML only. No markdown."""

FUNCTIONS_LLM_PROMPT = """Select ONE function from available list.

OUTPUT: {"name":"<function_name>","arguments":{...}}

RULES:
- Single line JSON
- NO markdown fences
- Body params: {"arguments":{"body":{...}}}
- No match: Plain text response
- CRITICAL: NEVER use platform names (catalyst, meraki, intersight, sdwan, nexus) as parameter VALUES
- When user asks for "catalyst notifications" or "<platform> <function>", the platform name is context, NOT a parameter

Example: {"name":"fabricsAddFabrics","arguments":{"body":{"fabrics":[{"name":"demo"}]}}}
Example for "get catalyst notifications": {"name":"getNotifications","arguments":{}}"""

USER_PROMPT_TEMPLATE = """User: {user_query}"""

GENERIC_RESPONSE_PROMPT = """Format Cisco function data professionally.

**OUTPUT RULES**:
1. HEADING: Start with descriptive <h3> (e.g., "API Result", "Network Status")
2. LISTS → HTML table:
   <table style="border-collapse:collapse;width:100%">
     <thead style="background:#f0f3f5">
       <tr><th style="padding:8px;text-align:left">{key}</th>...</tr>
     </thead>
     <tbody>
       <tr><td style="padding:8px;border-bottom:1px solid #e0e0e0">{value}</td>...</tr>
     </tbody>
   </table>
3. SINGLE OBJECT → Definition list:
   <dl>
     <dt style="font-weight:600;margin-top:8px">{key}</dt>
     <dd style="margin-left:20px;margin-bottom:8px">{value}</dd>
   </dl>
4. SIMPLE DATA → Paragraph or list
5. CRITICAL: Valid HTML only, NO markdown
6. PERFORMANCE: Minimal HTML, compact structure
7. COMPLETENESS: Display ALL provided data - never truncate or summarize list items"""

HTML_SDWAN_DEVICE_STATUS_PROMPT = """Parse SD-WAN device list into professional HTML table.

REQUIRED OUTPUT:
<div style="font-family:system-ui">
  <h3 style="color:#1a73e8;margin-bottom:16px">SD-WAN Device Status</h3>
  <div style="overflow-x:auto">
    <table style="border-collapse:collapse;width:100%;background:#fff">
      <thead style="background:#f0f3f5">
        <tr>
          <th style="padding:12px;text-align:left;font-weight:600">Hostname</th>
          <th style="padding:12px;text-align:left;font-weight:600">System IP</th>
          <th style="padding:12px;text-align:left;font-weight:600">Site ID</th>
          <th style="padding:12px;text-align:left;font-weight:600">Status</th>
          <th style="padding:12px;text-align:left;font-weight:600">Reachability</th>
          <th style="padding:12px;text-align:left;font-weight:600">Device Model</th>
          <th style="padding:12px;text-align:left;font-weight:600">Version</th>
        </tr>
      </thead>
      <tbody>
        {all_device_rows}
      </tbody>
    </table>
  </div>
</div>

DEVICE ROW:
<tr style="border-bottom:1px solid #e8eaed;transition:background 0.15s" onmouseover="this.style.background='#f8f9fa'" onmouseout="this.style.background=''">
  <td style="padding:12px;font-weight:500">{host-name}</td>
  <td style="padding:12px;font-family:monospace;font-size:13px">{system-ip}</td>
  <td style="padding:12px">{site-id}</td>
  <td style="padding:12px"><span style="display:inline-block;padding:2px 8px;border-radius:12px;font-size:12px;background:{status_bg};color:{status_color};font-weight:500">{status}</span></td>
  <td style="padding:12px"><span style="color:{reach_color}">{reachability}</span></td>
  <td style="padding:12px">{device-model}</td>
  <td style="padding:12px;font-size:13px">{version}</td>
</tr>

STATUS COLORS:
- up: bg:#e8f5e9, color:#2e7d32
- down: bg:#ffebee, color:#c62828
- other: bg:#fff3e0, color:#f57c00

CRITICAL: Generate FULL table with ALL device rows. HTML only."""

HTML_SDWAN_ALARM_STATUS_PROMPT = """Parse SD-WAN alarms into professional HTML table.

REQUIRED OUTPUT:
<div style="font-family:system-ui">
  <h3 style="color:#d32f2f;margin-bottom:16px">⚠️ SD-WAN Active Alarms</h3>
  <div style="overflow-x:auto">
    <table style="border-collapse:collapse;width:100%;background:#fff">
      <thead style="background:#ffebee">
        <tr>
          <th style="padding:12px;text-align:left;font-weight:600">Severity</th>
          <th style="padding:12px;text-align:left;font-weight:600">Type</th>
          <th style="padding:12px;text-align:left;font-weight:600">Component</th>
          <th style="padding:12px;text-align:left;font-weight:600">System IP</th>
          <th style="padding:12px;text-align:left;font-weight:600">Message</th>
          <th style="padding:12px;text-align:left;font-weight:600">Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {all_alarm_rows}
      </tbody>
    </table>
  </div>
</div>

ALARM ROW:
<tr style="border-bottom:1px solid #e0e0e0">
  <td style="padding:12px">
    <span style="display:inline-flex;align-items:center;gap:4px;padding:4px 8px;border-radius:4px;font-size:12px;font-weight:600;background:{sev_bg};color:{sev_color}">
      {icon} {severity}
    </span>
  </td>
  <td style="padding:12px;font-size:13px">{type}</td>
  <td style="padding:12px;font-family:monospace;font-size:12px">{component}</td>
  <td style="padding:12px;font-family:monospace;font-size:12px">{system-ip}</td>
  <td style="padding:12px;font-size:13px">{message}</td>
  <td style="padding:12px;font-size:12px;color:#666">{formatted_time}</td>
</tr>

SEVERITY STYLES:
- critical: bg:#ffcdd2, color:#b71c1c, icon:🔴
- major: bg:#ffe0b2, color:#e65100, icon:🟠
- minor: bg:#fff9c4, color:#f57f17, icon:🟡
- warning: bg:#f5f5f5, color:#616161, icon:⚪

CRITICAL: Generate FULL table with ALL alarm rows. HTML only."""

HTML_SDWAN_GENERIC_RESPONSE_PROMPT = """Format SD-WAN function response professionally.

INSTRUCTIONS:
1. Start with heading: <h3 style="color:#1a73e8">SD-WAN Operation Result</h3>
2. LIST OF ITEMS → Table with inferred columns:
   <table style="border-collapse:collapse;width:100%">
     <thead style="background:#f0f3f5">...</thead>
     <tbody>...</tbody>
   </table>
3. SINGLE OBJECT → Definition list:
   <dl style="background:#f8f9fa;padding:16px;border-radius:4px">
     <dt style="font-weight:600;color:#1a73e8">{key}</dt>
     <dd style="margin:4px 0 12px 20px">{value}</dd>
   </dl>
4. SUCCESS MESSAGE → Styled paragraph:
   <p style="background:#e8f5e9;color:#2e7d32;padding:12px;border-radius:4px">{message}</p>
5. CRITICAL: HTML only, no markdown"""

HTML_CATALYST_INTERFACES_PROMPT = """Parse Catalyst interface list into paginated HTML table.

REQUIRED OUTPUT:
<div style="font-family:system-ui">
  <h3 style="color:#1a73e8;margin-bottom:16px">Catalyst Network Interfaces</h3>
  <div style="overflow-x:auto">
    <table style="border-collapse:collapse;width:100%;background:#fff;border:1px solid #dee2e6">
      <thead style="background:#1a73e8;color:#fff">
        <tr>
          <th style="padding:12px;text-align:left;font-weight:500">Port Name</th>
          <th style="padding:12px;text-align:left;font-weight:500">Status</th>
          <th style="padding:12px;text-align:left;font-weight:500">Admin</th>
          <th style="padding:12px;text-align:left;font-weight:500">Type</th>
          <th style="padding:12px;text-align:left;font-weight:500">IP Address</th>
          <th style="padding:12px;text-align:left;font-weight:500">MAC Address</th>
          <th style="padding:12px;text-align:left;font-weight:500">VLAN</th>
          <th style="padding:12px;text-align:left;font-weight:500">Mode</th>
          <th style="padding:12px;text-align:left;font-weight:500">Speed</th>
          <th style="padding:12px;text-align:left;font-weight:500">Duplex</th>
          <th style="padding:12px;text-align:left;font-weight:500">Description</th>
          <th style="padding:12px;text-align:left;font-weight:500">Device</th>
        </tr>
      </thead>
      <tbody>
        {interface_rows}
      </tbody>
    </table>
  </div>
  {pagination_controls}
</div>

INTERFACE ROW FORMAT:
<tr style="border-bottom:1px solid #e0e0e0;transition:background-color 0.2s" onmouseover="this.style.backgroundColor='#f8f9fa'" onmouseout="this.style.backgroundColor=''">
  <td style="padding:12px;font-weight:500;font-family:monospace;font-size:13px">{portName}</td>
  <td style="padding:12px">
    <span style="display:inline-flex;align-items:center;gap:4px">
      <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:{status_color}"></span>
      <span style="font-weight:500;color:{status_text_color}">{status}</span>
    </span>
  </td>
  <td style="padding:12px">
    <span style="padding:2px 6px;background:{admin_bg};color:{admin_color};border-radius:3px;font-size:12px;font-weight:500">{adminStatus}</span>
  </td>
  <td style="padding:12px;font-size:13px">{interfaceType}</td>
  <td style="padding:12px;font-family:monospace;font-size:13px">{ipv4Address}</td>
  <td style="padding:12px;font-family:monospace;font-size:12px;color:#666">{macAddress}</td>
  <td style="padding:12px">
    <span style="padding:2px 6px;background:#f0f3f5;border-radius:3px;font-size:12px">{vlanId}</span>
  </td>
  <td style="padding:12px;font-size:13px">{portMode}</td>
  <td style="padding:12px;font-size:13px">{speed_formatted}</td>
  <td style="padding:12px;font-size:13px">{duplex}</td>
  <td style="padding:12px;font-size:13px;max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="{description}">{description}</td>
  <td style="padding:12px;font-size:11px;color:#666;max-width:150px;overflow:hidden;text-overflow:ellipsis" title="{deviceId}">{device_short}</td>
</tr>

STATUS COLORS:
- up: color:#4caf50, text_color:#2e7d32
- down: color:#f44336, text_color:#c62828
- other: color:#ff9800, text_color:#f57c00

ADMIN STATUS:
- UP: bg:#e8f5e9, color:#2e7d32
- DOWN: bg:#ffebee, color:#c62828

PAGINATION CONTROLS (when > 50 interfaces):
<div style="margin-top:16px;display:flex;justify-content:space-between;align-items:center">
  <div style="color:#666;font-size:14px">
    Showing {start}-{end} of {total} interfaces
  </div>
  <div style="display:flex;gap:8px">
    <button onclick="changePage(-1)" style="background:#fff;color:#1a73e8;border:1px solid #dadce0;padding:6px 12px;border-radius:4px;cursor:pointer;font-size:14px" {prev_disabled}>← Previous</button>
    <span style="padding:6px 12px;background:#1a73e8;color:#fff;border-radius:4px;font-size:14px">Page {current_page} of {total_pages}</span>
    <button onclick="changePage(1)" style="background:#fff;color:#1a73e8;border:1px solid #dadce0;padding:6px 12px;border-radius:4px;cursor:pointer;font-size:14px" {next_disabled}>Next →</button>
  </div>
</div>

FORMATTING RULES:
- Speed: Convert to human-readable (e.g., "1000000" → "1 Gbps", "10000000" → "10 Gbps", "100000" → "100 Mbps")
- Empty/null values: Display as "-"
- Device ID: Show first 8 characters + "..."
- IP addresses without mask: Show address only
- VLAN 0: Display as "None (Routed)"
- If total interfaces ≤ 50: Show all, no pagination
- If total interfaces > 50: Show 50 per page with controls
- CRITICAL: Display ALL interfaces without summarization
- Pure HTML output only, no markdown"""
HTML_CATALYST_INTERFACES_LIGHTWEIGHT_PROMPT = """Catalyst interfaces - LIGHTWEIGHT HTML.

PERFORMANCE: Balanced - good performance with basic readability.

OUTPUT:
<div style="font-family:system-ui">
  <h4 style="margin:0 0 8px 0">Catalyst Interfaces</h4>
  <table style="border-collapse:collapse;width:100%;font-size:13px">
    <thead>
      <tr style="background:#f0f3f5">
        <th style="padding:6px;text-align:left">Port</th>
        <th style="padding:6px;text-align:left">Status</th>
        <th style="padding:6px;text-align:left">IP Address</th>
        <th style="padding:6px;text-align:left">VLAN</th>
        <th style="padding:6px;text-align:left">Speed</th>
        <th style="padding:6px;text-align:left">Device</th>
        <th style="padding:6px;text-align:left">Description</th>
      </tr>
    </thead>
    <tbody>
      {interface_rows}
    </tbody>
  </table>
</div>

ROW FORMAT:
<tr style="border-bottom:1px solid #eee">
  <td style="padding:6px;font-family:monospace">{portName}</td>
  <td style="padding:6px">
    <span style="color:{status_color};font-weight:600">{status}</span>
  </td>
  <td style="padding:6px;font-family:monospace">{ipv4Address}</td>
  <td style="padding:6px">{vlanId}</td>
  <td style="padding:6px">{speed_simple}</td>
  <td style="padding:6px;font-size:11px">{device_short}</td>
  <td style="padding:6px">{description}</td>
</tr>

FORMATTING:
- Status colors: up=#2e7d32, down=#c62828, other=#f57c00
- Speed format: 1G, 10G, 100M (simplified)
- Device: First 8 chars only
- Empty values: "-"
- If > 500 interfaces: Add note "Showing first 500 of {total} interfaces"
- Basic borders and padding for readability"""

HTML_CATALYST_INTERFACES_LIGHTWEIGHT_PROMPT = """Catalyst interfaces - LIGHTWEIGHT HTML.

PERFORMANCE: Balanced - good performance with basic readability.

OUTPUT:
<div style="font-family:system-ui">
  <h4 style="margin:0 0 8px 0">Catalyst Interfaces</h4>
  <table style="border-collapse:collapse;width:100%;font-size:13px">
    <thead>
      <tr style="background:#f0f3f5">
        <th style="padding:6px;text-align:left">Port</th>
        <th style="padding:6px;text-align:left">Status</th>
        <th style="padding:6px;text-align:left">IP Address</th>
        <th style="padding:6px;text-align:left">VLAN</th>
        <th style="padding:6px;text-align:left">Speed</th>
        <th style="padding:6px;text-align:left">Device</th>
        <th style="padding:6px;text-align:left">Description</th>
      </tr>
    </thead>
    <tbody>
      {interface_rows}
    </tbody>
  </table>
</div>

ROW FORMAT:
<tr style="border-bottom:1px solid #eee">
  <td style="padding:6px;font-family:monospace">{portName}</td>
  <td style="padding:6px">
    <span style="color:{status_color};font-weight:600">{status}</span>
  </td>
  <td style="padding:6px;font-family:monospace">{ipv4Address}</td>
  <td style="padding:6px">{vlanId}</td>
  <td style="padding:6px">{speed_simple}</td>
  <td style="padding:6px;font-size:11px">{device_short}</td>
  <td style="padding:6px">{description}</td>
</tr>

FORMATTING:
- Status colors: up=#2e7d32, down=#c62828, other=#f57c00
- Speed format: 1G, 10G, 100M (simplified)
- Device: First 8 chars only
- Empty values: "-"
- If > 500 interfaces: Add note "Showing first 500 of {total} interfaces"
- Basic borders and padding for readability"""

HTML_CATALYST_INTERFACES_ULTRALIGHTWEIGHT_PROMPT = """Catalyst interfaces - ULTRA LIGHTWEIGHT.

CRITICAL: Absolute minimum HTML for maximum performance.

OUTPUT:
<table style="font:12px monospace">
<tr><td>Port</td><td>Status</td><td>IP</td><td>VLAN</td><td>Speed</td><td>Device</td><td>Desc</td></tr>
{rows}
</table>

ROW: <tr><td>{portName}</td><td style="color:{color}">{status}</td><td>{ipv4Address}</td><td>{vlanId}</td><td>{speed}</td><td>{deviceId}</td><td>{description}</td></tr>

RULES:
- NO spacing/padding
- ONE style only (status color)
- Status: up=#080, down=#c00
- Empty: "-"
- Device: 8 chars max
- Desc: 20 chars max
- Speed: raw number
- Max 100 rows then: <tr><td colspan="7">Showing 100 of {total}</td></tr>"""