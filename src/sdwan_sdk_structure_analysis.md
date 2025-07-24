# SD-WAN SDK Structure Analysis

Based on the official documentation and SDK examples, here's the actual structure:

## Key Findings:

### 1. API Path Structure
- **Base Path**: All API endpoints are relative to `/dataservice`
- **Full URL**: `https://<vmanage-server>/dataservice/<endpoint>`
- **Examples**:
  - `/admin/user` → `https://vmanage/dataservice/admin/user`
  - `/device` → `https://vmanage/dataservice/device`

### 2. SDK Access Pattern
From the SDK documentation examples:
```python
# Get devices
devices = session.api.devices.get()

# Get alarms
alarms = session.api.alarms.get()

# Get users
users = session.api.users.get()
```

### 3. SDK Endpoint Classes (from the documentation)
- `AdministrationUserAndGroup` - for user/group operations
- `MonitoringDeviceDetails` - for device operations
- `ConfigurationDeviceInventory` - for device inventory
- And many more...

### 4. Our Current Mapping Issues

**Current mappings**:
- `/admin/user` → `administration.users` ❌
- Should be: `/admin/user` → `users` ✅

**The SDK structure is**:
- `session.api.users` - NOT `session.api.administration.users`
- `session.api.devices` - NOT `session.api.monitoring.devices`
- `session.api.alarms` - correct as is

### 5. Why Our Queries Are Failing

When we map to `administration.users`, the SDK client tries:
1. `endpoint = self._api` (the api container)
2. `endpoint = endpoint.administration` (doesn't exist!)
3. Fails with "SDK endpoint administration not found"

### 6. The Fix

We need to update our mappings to use the direct endpoint names:
- `users` instead of `administration.users`
- `devices` instead of `monitoring.devices`
- Keep `alarms` as is

The SDK internally handles the routing to the appropriate class methods.