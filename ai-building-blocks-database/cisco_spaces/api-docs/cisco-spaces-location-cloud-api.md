# Cisco Spaces Location Cloud API

## Overview
Cisco Spaces offers multiple APIs, including a **Firehose** API and a **REST** API. For this application, **only** the **REST API**—referred to as the **Cisco Spaces Location Cloud API**—is used. This API provides **endpoints** to retrieve, update, and manage:
- **Devices** (including active devices, their locations, and usage history)
- **Maps** (including campus, building, floor, and zone hierarchies)

This API is served by `ApiServer` to handle device, history, and map requests. It also offers instructions on **authentication**, **authorization**, **request/response** examples (using `cURL`), and developer support.

## Use Cases
1. **Search & Display Location Devices**  
   - Query and filter devices by **location hierarchy** (campus, building, floor, zone).
   - Retrieve and manage device data (e.g., APs, tags, rogue devices, etc.).

2. **Location Hierarchy & Maps**  
   - Navigate hierarchical maps: **Campus -> Building -> Floor -> Zone**.
   - Validate location data and visualize device placements.

3. **Device History**  
   - Access historical data for a single device or multiple devices.
   - Filter by time range, location, or device type.

---
## Authentication
1. **Authorization Header**  
   - Every request must include:  
     ```http
     Authorization: Bearer {BEARER_TOKEN}
     ```
   - Supported **Bearer** token format (JWT or other).  
   - Regions have different Base URIs:
     - **US**: `https://dnaspaces.io`
     - **EU**: `https://dnaspaces.eu`
     - **Singapore**: `https://ciscospaces.sg`

2. **Obtaining the Bearer Token**  
   - Generate an **API Key** in the Detect & Locate app (`Notifications -> API Keys -> Add`).  
   - The key is displayed only at creation time and must be stored **securely**.
   - Each user can have up to **10 keys**, with a max of **5 active** at once.
   - Key expiration is **configurable** (7–365 days).  
   - Example usage:
     ```bash
     curl --location --request GET 'https://dnaspaces.io/api/location/v2/devices' \
       --header 'Authorization: Bearer {BEARER_TOKEN}'
     ```

---
## Base URIs
Use the region-specific base URI before each path:
- **US**: `https://dnaspaces.io`
- **EU**: `https://dnaspaces.eu`
- **Singapore**: `https://ciscospaces.sg`

**Example** (devices retrieval):
```bash
curl --location --request GET '{base-uri}/api/location/v2/devices' \
  --header 'Authorization: Bearer {BEARER_TOKEN}'
```
Replace `{base-uri}` with the appropriate regional domain.

---
## Resources

### 1. Maps
- **Hierarchy**: Campus -> Building -> Floor -> Zone
- **API**: Retrieve map elements, location hierarchy, and details.  
- **Use**: Validate workspace map data (i.e., confirm devices on the correct floor/zone).

### 2. Active Devices
- **Description**: Get device information (e.g., type, last seen, location).
- **Filtering**: By location level (building, floor, etc.) or device type (AP, interferer, tag, rogue AP).
- **Use**: Quickly see how many devices are on a particular floor or building.

### 3. Device History
- **Description**: Access historical data for a single device or multiple devices.
- **Use**: Track movement, usage, or signals over time.

---
## Sample API Workflow

1. **Request**: List all active devices  
   ```bash
   curl --location --request GET '{base-uri}/api/location/v2/devices' \
     --header 'Authorization: Bearer {BEARER_TOKEN}'
   ```
2. **Response** (Example):
   ```json
   {
     "success": true,
     "results": [
       {
         "tenantId": "200",
         "macAddress": "00:12:b8:0a:c6:20",
         "deviceType": "TAG",
         "campusId": "...",
         "hierarchy": "San Jose->SJC-17->1st Floor",
         "coordinates": [33.401928, 101.87378],
         "lastLocatedAt": "2018-05-27T21:14:44.005Z",
         "manufacturer": "Aeroscout Ltd.",
         "numDetectingAps": 3,
         "apList": [...]
         ...
       }
     ]
   }
   ```

3. **Request**: Retrieve details of a specific floor  
   ```bash
   curl --location --request GET '{base-uri}/api/location/v2/map/floor/{FLOOR_ID}' \
     --header 'Authorization: Bearer {BEARER_TOKEN}'
   ```
4. **Response** (Example):
   ```json
   {
     "locationHierarchy": [
       { "id": "a8b98eac-8aef-42dd-a24d-3ea6839efa3c", "name": "dnshirsa_acc1", "type": "root" },
       { "id": "b975b84b-1cad-43a4-9da2-80946ebf1d61", "name": "System Campus", "type": "campus" },
       { "id": "7bcd2f92-abab-4fee-853d-d16c71cddf52", "name": "ewlc173building 20", "type": "network" },
       { "id": "28946415-f998-4183-948c-c49fd2268b3a", "name": "floor2", "type": "floor" }
     ],
     "accessPoints": [...],
     "maps": [...],
     "details": { ... },
     ...
   }
   ```

---
## Key Notes & Reminders
- **REST API Only**: While Cisco Spaces also has a **Firehose** API, for this particular application **only** the Cisco Spaces Location Cloud (REST) API is utilized.
- **Multiple Regions**: Use the correct domain (`dnaspaces.io`, `dnaspaces.eu`, or `ciscospaces.sg`) for your region.
- **Bearer Token**: Must be included in **every** request via the `Authorization` header.
- **API Key Storage**: Once generated, the key is **not** shown again; store it securely.
- **Role & Scope**: By default, direct API users have admin-level access to all locations.

---
*This guide is intended for **developers** integrating with Cisco Spaces to manage devices and maps through a RESTful approach. Use the above methods to query location data, handle device states, and maintain accurate workspace information across your organization.*
```