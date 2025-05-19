# Meraki Dashboard & Camera Intelligence APIs

## Overview
Meraki provides multiple APIs to integrate with the Meraki Cloud and its features:

1. **Meraki Dashboard API**  
   - The **main** API for interacting with Meraki cloud-managed devices and networks.

2. **MV Camera Intelligence API**  
   - Focuses on smart camera analytics—people detection, vehicle detection, light levels, occupancy, etc.
   - Available through both **REST-based** and **MQTT-based** endpoints.

This document covers both the **Dashboard API** and **Camera Intelligence** capabilities, emphasizing how to retrieve data and manage Meraki devices for application development.

---

## MV Camera Intelligence API

### Introduction
Meraki **MV cameras** provide real-time and historical intelligence such as:
- **People Detection** (counts, dwell time, occupancy)
- **Vehicle Detection** (cars, bikes, trucks)
- **Light Level Readings**

You can use **REST** endpoints to fetch near real-time or historical data and **MQTT** to receive a live feed.  
- **REST-based**: On-demand client-server communication (slight delay).
- **MQTT-based**: Publish-subscribe model, real-time data feed.

### Types of Endpoints

#### 1. Camera Intelligence REST APIs
Allows you to query analytics configured on the Meraki Dashboard, such as:
- **People Counting**
- **Line Crossing**
- **Area Occupancy**

##### Examples:
- **MV Camera Intelligence REST API**  
  Retrieve historical or near real-time object detection data from a camera.

- **MV Sense & MQTT**  
  Real-time feed of object detection, bounding boxes, and light levels. Requires a **paid license** (MV Sense license).

#### 2. MQTT-Based (MV Sense)
- Real-time push of data from the camera (sub-second latency).
- Object detection, bounding boxes, occupant location, light levels.
- Typically for advanced analytics or immediate event-driven use cases.

---

## Cameras & APIs (High-Level)

1. **Camera Intelligence REST APIs**  
   - **People Counting, Line Crossing, Area Occupancy** analytics.
   - Use the **MV Camera Intelligence REST endpoints**.

2. **MV Sense & MQTT**  
   - Enables data ingestion via MQTT streams.
   - Also powers Custom Computer Vision (e.g., user-trained ML models on the camera).

3. **Live Link API**  
   - A **REST** API returning links for the Meraki Dashboard or Vision Portal.
   - Optionally time-based: if a timestamp is provided, links directly to that video segment.

4. **Snapshot API**  
   - **REST** endpoint generating a snapshot image from the camera’s field of view at a specified time.
   - For 2nd/3rd gen cameras, resolution can be configured or requested in full frame.

---

## Meraki Dashboard API

### Introduction
The **Meraki Dashboard API** is a **REST** service for:
- Managing organizations, admins, networks, devices, VLANs.
- Automating network configurations.
- Building custom UIs for store managers, field techs, etc.

### Key Features
- Add or remove devices, networks, VLANs programmatically.
- Onboard/offboard users automatically.
- Python library/SDK and other OpenAPI-based resources available.
- Postman collections, interactive docs, code generation.

#### Python SDK Quickstart

1. **Install** the Meraki Python library:
   ```bash
   pip install meraki
   ```
2. **Set your API key**:
   ```python
   import meraki
   API_KEY = "YOUR_API_KEY"
   dashboard = meraki.DashboardAPI(API_KEY)
   ```
3. **Test** with a simple call:
   ```python
   response = dashboard.organizations.getOrganizations()
   print(response)
   ```
   This returns a list of organizations accessible to the given API key.

---

## Sample Use Cases

### 1. Build a Captive Portal
- **Goal**: Provide a custom authentication or landing page for Wi-Fi users.
- **How**:  
  1. Set up a Python/Flask web server.  
  2. Use the Meraki **Splash** page integration (Dashboard > Wireless > Configure > Splash).  
  3. On connecting to the SSID, users see your custom portal served by your local or cloud server.  

### 2. Build Wi-Fi & BLE Location Apps
- **Goal**: Real-time or historical location data for Wi-Fi and BLE devices.  
- **How**:  
  1. Enable **Location Scanning API** in the Dashboard.  
  2. Provide an endpoint (Flask, Node, etc.) to receive JSON data from Meraki on connected and non-connected devices.  
  3. Visualize or store the location data in your systems.

---

## MV Sense & Camera Analytics

### What is MV Sense?
A set of **APIs** giving access to **edge-computed** data for people detection, classification, and tracking on Meraki cameras:
- **Historical Aggregate**: People count at time t  
- **Current Snapshot**: People count now  
- **Real-time Feed**: Sub-second data feed via MQTT

#### Additional APIs
- **Live Link API**: Link to the specific video feed or timestamp.  
- **Snapshot API**: Timestamped or live snapshot from the camera.

---

## Deep Dive: Camera Intelligence

### Areas & Lines
- Configurable in the Meraki Dashboard’s **Analytics** tab:
  1. Create or move an **Area** box or **Line**.  
  2. Save the name.  
  3. Use the MV Camera Intelligence APIs to query crossing events or occupancy within that area.

### MQTT Details
- Meraki cameras can publish messages to a configured MQTT broker.
- Topics typically follow the format `/merakimv/XXXX-XXXX-XXXX/...` (where `XXXX-XXXX-XXXX` is the camera serial).
- Data examples:
  - **Counts**: Current people or vehicle counts in the frame.
  - **Raw Detections**: A list of bounding boxes, object IDs, confidence scores.
  - **Line Crossing**: Published each time an object crosses a defined line.
  - **Area Occupancy**: Summaries of objects entering or leaving an area over a 60-second window.

---

## Generating a Meraki Dashboard API Key

1. **Login** to Meraki Dashboard.
2. Navigate: **Organization > Configure > API & Webhooks**.
3. Select **API Keys and Access** tab, click **Generate API Key**.
4. **Save** the key securely (it will not be shown again).
5. If you need **MV Sense**:
   - Enable under **Cameras > Monitor > [Select Camera] > Settings > Sense**.

---

## REST API Endpoints for MV Camera Intelligence

1. **Areas by Device**  
   - `GET /organizations/{organizationId}/camera/boundaries/areas/byDevice`  
   - Lists all configured area boundaries for the cameras in an org.
2. **Lines by Device**  
   - `GET /organizations/{organizationId}/camera/boundaries/lines/byDevice`
3. **Detections by Interval**  
   - `GET /organizations/{organizationId}/camera/detections/history/byBoundary/byInterval`
   - Retrieve data for multiple boundaries, with custom intervals, over a specified time range.

### Custom CV / MV Sense Endpoints
- **GET/PUT** custom analytics (model artifacts, thresholds, etc.).
- **Enable/disable** MV Sense, assign MQTT brokers, etc.

### Snapshot API
- `POST /devices/{serial}/camera/generateSnapshot`
- Returns a URL linking to an image at a specified time (or live).

---

## Deprecated Endpoints
- **Zones**: Replaced by “Areas & Lines”.
- **GET** `/devices/{serial}/camera/analytics/zones`  
- **GET** `/devices/{serial}/camera/analytics/overview`  
- **GET** `/devices/{serial}/camera/analytics/zones/{zoneId}/history`

Use the new endpoints in **MV Camera Intelligence** for areas/lines and historical data.

---

## Summary
- **Meraki Dashboard API**: Central place for network-level management, device config, and integration (Captive portal, location scanning, etc.).
- **MV Camera Intelligence**: Specific to camera analytics (people/vehicle detection, occupancy, line crossing, etc.).  
  - Access through **REST** or **MQTT**.  
  - Possibly enable **Custom CV** for advanced models.

