# SD-WAN Query Examples

## Getting Alarm Details

Instead of just asking for "alarms", try these more specific queries:

### 1. Get Raw Alarm Data
```
Get SD-WAN raw alarm data
```
This should call the `getRawAlarmData` operation which returns actual alarm details for the last 30 minutes.

### 2. Get Active Alarms
```
Get SD-WAN active alarms with details
```
This should call the `getActiveAlarms` operation which includes alarm details.

### 3. Get Non-Viewed Alarms
```
Show me SD-WAN alarms that haven't been viewed
```
This should call the `getNonViewedAlarms` operation.

### 4. Get Alarm Details by Type
```
Get SD-WAN alarm details
```
This should call the `getAlarmDetails` operation.

### 5. Query with Time Range
```
Get SD-WAN alarms from the last hour
Get SD-WAN alarms from today
```

## Other SD-WAN Queries

### Device Information

**Working Queries:**
```
Get SD-WAN connected devices
Execute listAllDevices for SD-WAN
Get SD-WAN device key value list
```

**Why Previous Queries Failed:**
- "List all SD-WAN devices" → picks `getAllDeviceStatus` which uses `device_state.get()` but that method doesn't exist
- "Show all SD-WAN devices" → same issue
- The `device_state` endpoint has specific methods like `get_device_wan_interfaces`, not a generic `get()`

**Better Approach:**
```
Run SD-WAN listAllDevices operation
Get SD-WAN devices using listAllDevices
Execute the listAllDevices function for SD-WAN
```

### Users and Administration
```
Get SD-WAN user list with details
Show all SD-WAN admin users
Get SD-WAN user groups
```

### Network Status
```
Get SD-WAN site health
Show SD-WAN WAN edge health
Get SD-WAN control connections
```

### Templates and Policies
```
Get SD-WAN device templates
Show SD-WAN policy list
Get SD-WAN feature templates
```

## Tips for Better Results

1. **Be specific**: Instead of "get alarms", say "get raw alarm data" or "get active alarms with details"
2. **Include "details" or "raw data"**: This helps the AI understand you want full information
3. **Specify time ranges**: Add "from last hour", "today", etc. for time-bounded queries
4. **Use operation names**: If you know the operation name like "getRawAlarmData", use it directly

## Understanding the Response

If you're getting just counts:
- The query might be too generic
- Try adding "with details", "raw data", or "full information"
- The AI might be summarizing; ask for "complete alarm data without summarization"