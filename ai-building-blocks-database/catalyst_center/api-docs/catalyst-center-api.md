# Cisco Catalyst Center Documentation

## Overview

Cisco Catalyst Center is a powerful platform at the core of Cisco’s intent-based networking architecture. Formerly known as **DNA Center**, Catalyst Center offers:

- **Intent-based APIs** that express business outcomes rather than specific device configurations.
- **Automation** for network tasks like zero-touch provisioning, device onboarding, and software image management.
- **Analytics & Assurance** features for end-to-end visibility into network devices, topology, issues, and recommended remediations.

Users and developers can **extend** Catalyst Center with applications leveraging the **northbound REST APIs** (Intent API, Integration APIs), as well as receiving **events** (webhooks) from the **Event Management** domain.

> **Note**: Cisco DNA Center has been rebranded as **Catalyst Center**. You may still see references to “DNA Center” in some documents; these refer to the same product.

---

## Key API Domains

Catalyst Center organizes its APIs into **domains** and **subdomains** that reflect enterprise networking workflows:

1. **Authentication**  
   - Obtain a token (`POST /dna/system/api/v1/auth/token`) for secure, token-based access.

2. **Know Your Network**  
   - **Sites**: Create, manage hierarchical sites (areas/buildings/floors).  
   - **Devices**: Import, retrieve, and manage network devices.  
   - **Clients**: Get client health info, connectivity details.  
   - **Issues**: Retrieve existing issues, recommended mitigations.  
   - **Topology**: Access site, physical, and logical (L2/L3) topologies.

3. **Site Management**  
   - **Site Design**: Provision network parameters for each site, e.g., IP pools, AAA, NTP.  
   - **Network Settings**: Assign shared services (DNS, DHCP, Telemetry) at the site level.

4. **Software Image Management (SWIM)**  
   - Upload OS images, distribute to devices, and activate images seamlessly.

5. **Device Onboarding (PnP)**  
   - Zero-touch deployment for new or replaced (RMA) devices.  
   - Manage device onboarding projects, settings, workflows, and virtual accounts.

6. **Configuration Templates**  
   - CLI-based templates that let you standardize and automate network configurations.

7. **Connectivity**  
   - **Fabric Wired**: Manage wired fabric devices (e.g., edge, border), authentication profiles.  
   - **Non-Fabric Wireless**: Manage enterprise SSIDs, wireless profiles, AP provisioning, etc.

8. **Operational Tasks**  
   - **Command Runner**: Execute read-only CLI commands across devices for troubleshooting.  
   - **Network Discovery**: Discover existing devices via SNMP, CDP, IP ranges.  
   - **Path Trace**: Analyze traffic flow between two endpoints, identify ACL/QoS issues.  
   - **File Services**: Manage and download logs, config archives.  
   - **Task**: Track asynchronous operations (e.g., image distribution, PnP discovery).

9. **Policy**  
   - **Application Policy**: Abstract business intent into application QoS/policies.  

10. **Event Management**  
   - Subscribe to events (e.g., device unreachable), send webhooks or emails on triggers.

11. **Integration (Westbound) APIs**  
   - IT Service Management (ITSM) integration to minimize manual handoffs or duplications.  
   - External IPAM or external analytics tools integration.

---

## Authentication & Token API

- **Endpoint**: `POST /dna/system/api/v1/auth/token`
- **Method**: `POST` (HTTP Basic Auth)
- **Response**: A JSON body containing a `Token` attribute.
  
**Python Example**:
```python
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://<CLUSTER-IP>"
AUTH_URL = "/dna/system/api/v1/auth/token"
USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

def get_token():
    response = requests.post(
       f"{BASE_URL}{AUTH_URL}",
       auth=HTTPBasicAuth(USERNAME, PASSWORD),
       headers={'content-type': 'application/json'},
       verify=False
    )
    data = response.json()
    return data['Token']
```

- **Usage**: Include `X-Auth-Token` header in subsequent calls:
```http
X-Auth-Token: <token-string>
```

---

## Know Your Network (Devices, Sites, Clients, Issues, Topology)

### Devices
- **Get All Devices**: `GET /dna/intent/api/v1/network-device`
- **Add Device**: `POST /dna/intent/api/v1/network-device`
- **Get Device by IP**: `GET /dna/intent/api/v1/network-device/ip-address/{ip}`
- **Filtering**: By hostname, platform ID, etc.

**Example**:
```python
import requests

def get_device_by_ip(ip_address, token):
    url = f"{BASE_URL}/dna/intent/api/v1/network-device/ip-address/{ip_address}"
    headers = {
       "X-Auth-Token": token,
       "Content-type": "application/json"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.json()
```

### Sites
- **Create Site**: `POST /dna/intent/api/v1/site`  
  - Supports `type=area`, `type=building`, `type=floor`.
- **Get Sites**: `GET /dna/intent/api/v1/site`
- **Site Count**: `GET /dna/intent/api/v1/site/count`
- **Assign Devices**: `POST /dna/intent/api/v1/site/{site_id}/device`

### Clients
- **Get Client Health**: `GET /dna/intent/api/v1/client-health`
- **Get Detailed Client Info**: `GET /dna/intent/api/v1/client-detail?macAddress=xx:xx:xx:xx:xx:xx`

### Issues
- **Get Issues**: `GET /dna/intent/api/v1/issue`
- **Get Issue Enrichment Details**: `GET /dna/intent/api/v1/issue-enrichment-details`  
  Useful for retrieving suggested actions, impacted hosts, etc.

### Topology
- **Site Topology**: `GET /dna/intent/api/v1/topology/site-topology`
- **Physical Topology**: `GET /dna/intent/api/v1/topology/physical-topology`
- **Layer 2**: `GET /dna/intent/api/v1/topology/l2/{vlanId}`
- **Layer 3**: `GET /dna/intent/api/v1/topology/l3/{ipv4Network?}` (if supported in your release)

---

## Site Management & Network Settings

### Site Design
- **Create NFV device** (Day-N provisioning)
- **Site-Level AAA, DNS, NTP**: `GET`/`POST` calls to `/dna/intent/api/v1/site/{site_id}/settings`
- **Banner, Telemetry** config at site level

### Network Settings
- **Global IP Pools**: `POST /dna/intent/api/v1/global-pool` / `GET /dna/intent/api/v1/global-pool`
- **DHCP / DNS**:
  - Assign DNS Servers, DHCP Relay at a site or global level.

---

## Software Image Management (SWIM)

1. **Image Import**:  
   - `POST /dna/intent/api/v1/image/importation/source/url`  
   - Upload via URL (HTTP, FTP, etc.).

2. **List Imported Images**:  
   - `GET /dna/intent/api/v1/image/importation`

3. **Distribute Image**:  
   - `POST /dna/intent/api/v1/image/distribution`  
   - Provide device UUID and image UUID.

4. **Activate Image**:  
   - `POST /dna/intent/api/v1/image/activation/device`  
   - Reboot device if needed.

5. **Asynchronous**: Use `GET /dna/intent/api/v1/task/{taskId}` to track progress.

---

## Device Onboarding (PnP)

**PnP** (Plug and Play) automates zero-touch deployment:
- **Import Device**: `POST /dna/intent/api/v1/onboarding/pnp-device/import`
- **Claim Device**: `POST /dna/intent/api/v1/onboarding/pnp-device/site-claim`
- **Get All PnP Devices**: `GET /dna/intent/api/v1/onboarding/pnp-device`
- **Get Workflows**: `GET /dna/intent/api/v1/onboarding/pnp-workflow`

**Example**: Marking a device for RMA, or replacing device in a PnP flow.

---

## Configuration Templates

- **Projects**: Organize templates.  
  - `POST /dna/intent/api/v1/template-programmer/project`
- **Templates**:  
  - `POST /dna/intent/api/v1/template-programmer/project/{projectId}/template`
  - Commit/Version a template: `POST /dna/intent/api/v1/template-programmer/template/version`
- **Deploy Template**: `POST /dna/intent/api/v1/template-programmer/template/deploy`  
  Provide `templateId`, device parameters, etc.

---

## Connectivity (SDA & Wireless)

### Fabric Wired (SDA)
- **Create Fabric**: `POST /dna/intent/api/v1/business/sda/fabric`
- **Assign Site to Fabric**: `POST /dna/intent/api/v1/business/sda/fabric-site`
- **Control Plane Device**: `POST /dna/intent/api/v1/business/sda/control-plane-device`
- **Border / Edge**: `POST /dna/intent/api/v1/business/sda/border-device` / `edge-device`
- **Authentication Profile**: `POST /dna/intent/api/v1/business/sda/authentication-profile`
- **Virtual Network**: `POST /dna/intent/api/v1/business/sda/virtual-network`
- **IP Pool**: `POST /dna/intent/api/v1/business/sda/virtualnetwork/ippool`

### Non-Fabric Wireless
- **Enterprise SSIDs**: Assign or configure SSID on WLC.  
- **Access Point Provisioning**: `POST /dna/intent/api/v1/network-device` with wireless profiles.

---

## Operational Tasks

### Command Runner
- **Run CLI Commands**: `POST /dna/intent/api/v1/network-device-poller/cli/read-request`
- **Get Task**: Check results with `GET /dna/intent/api/v1/task/{taskId}`

### Network Discovery
- **Discover**: `POST /dna/intent/api/v1/discovery`
- **Retrieve**: `GET /dna/intent/api/v1/discovery/{discoveryId}/network-device`

### Path Trace
- **Create**: `POST /dna/intent/api/v1/flow-analysis` (source IP, dest IP, protocol)
- **Get Results**: `GET /dna/intent/api/v1/flow-analysis/{flowAnalysisId}`
- **Delete**: `DELETE /dna/intent/api/v1/flow-analysis/{flowAnalysisId}`

### Tag / Task Management
- **Tag**: Create, retrieve, or assign tags to devices, etc.
- **Task**: Retrieve the status of asynchronous tasks (`GET /dna/intent/api/v1/task/{taskId}`).

---

## Policy (Application Policy)

- **Application**: `GET /dna/intent/api/v1/applications`
- **Application Sets**: Group multiple applications.
- **Policy**: Translate business rules into device configurations.

---

## Event Management (Notifications)

- **Get Events**: `GET /dna/intent/api/v1/events`
- **Create Subscription**: `POST /dna/intent/api/v1/event/subscription`
  - Provide event IDs, choose `REST` or `EMAIL` notifications, set the URL/email.
- **Get Subscriptions**: `GET /dna/intent/api/v1/event/subscription`
- **Delete Subscription**: `DELETE /dna/intent/api/v1/event/subscription/{id}`
- **Synchronous Query**: `GET /dna/intent/api/v1/event/event-series` to retrieve past occurrences.

---

## Integration (Westbound APIs)

- **IT Service Management (ITSM)**:  
  - Automate incident creation, change requests upon certain events.  
  - E.g., `GET /dna/intent/api/v1/integrations/itsm`
- **External IPAM**: Configure or sync IP pools with an external IPAM.

---

## RMA (Device Replacement)

- **Mark Device**: `POST /dna/intent/api/v1/device-replacement`
- **Workflow**: `POST /dna/intent/api/v1/device-replacement/workflow`
  - Provide `faultyDeviceSerialNumber` and `replacementDeviceSerialNumber`.

---

## Asynchronous Operations (Tasks)

Many Catalyst Center operations (e.g., discovery, image distribution, template deployments) are **async**. The API response often includes:
```json
{
  "response": {
    "taskId": "6f5a724b-f922-4cec-96c3-dc5f52693934",
    "url": "/api/v1/task/6f5a724b-f922-4cec-96c3-dc5f52693934"
  },
  "version": "1.0"
}
```
You then check the status with:
```http
GET /dna/intent/api/v1/task/{taskId}
```
The resulting JSON shows **isError**, **progress**, and possibly **data** keys to indicate success or failure.

---

## Additional Resources

- **Developer Toolkit**:  
  Access via Catalyst Center GUI: *Platform > Developer Toolkit* to browse interactive docs.
- **cisco-data-bridge-domain-index**:  
  If you’re integrating multiple Cisco platforms (Catalyst, Meraki, etc.), ensure consistent environment variables and code structure.
- **dnacentersdk** (Python SDK)**:
  - [dnacentersdk GitHub](https://github.com/cisco-en-programmability/dnacentersdk)
  - `pip install dnacentersdk`
- **Cisco DevNet**:  
  Tutorials, sandboxes, and example code: <https://developer.cisco.com/dnacenter/>

---

## Example Script Snippets

### Authenticate & List Devices
```python
import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()

BASE_URL = "https://<YOUR-CLUSTER-IP>"
USERNAME = "admin"
PASSWORD = "Cisco123!"
AUTH_ENDPOINT = "/dna/system/api/v1/auth/token"

def get_auth_token():
    resp = requests.post(
        f"{BASE_URL}{AUTH_ENDPOINT}",
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=False
    )
    return resp.json()["Token"]

def list_devices():
    token = get_auth_token()
    headers = {"X-Auth-Token": token}
    devices_url = f"{BASE_URL}/dna/intent/api/v1/network-device"
    resp = requests.get(devices_url, headers=headers, verify=False)
    return resp.json()

if __name__ == "__main__":
    devices = list_devices()
    print(devices)
```

### Command Runner (Read-Only CLI)
```python
def run_cli_command(device_id, command):
    """
    device_id: ID from /network-device
    command: single command or list of commands
    """
    token = get_auth_token()
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    url = f"{BASE_URL}/dna/intent/api/v1/network-device-poller/cli/read-request"

    payload = {
      "commands": [command] if isinstance(command, str) else command,
      "deviceUuids": [device_id],
      "timeout": 0
    }

    resp = requests.post(url, json=payload, headers=headers, verify=False)
    task_id = resp.json()["response"]["taskId"]

    # Wait, then check task outcome
    task_url = f"{BASE_URL}/dna/intent/api/v1/task/{task_id}"
    # ... poll or sleep, get results from "fileId", then /dna/intent/api/v1/file/<fileId>
    return task_id
```

---

## Conclusion

Cisco Catalyst Center (formerly DNA Center) provides a **comprehensive** set of **REST APIs** to automate enterprise networks:

- **Sites & Devices**: Onboarding, topologies, health checks
- **Software Images**: Upload, distribute, and activate OS
- **Zero-Touch**: PnP, device replacement (RMA)
- **SDA**: Fabric creation, border/edge assignments
- **Wireless**: SSIDs, AP provisioning
- **Templates & Policies**: Day-N configuration, business intent
- **Event Subscriptions**: Email, webhook notifications for issues

Leverage these APIs to build end-to-end automation, integrate with ITSM systems, or develop custom monitoring dashboards. For deeper references, consult the [Catalyst Center Platform User Guide](https://www.cisco.com/c/en/us/support/cloud-systems-management/cisco-dna-center/series.html) and the [Cisco Developer](https://developer.cisco.com/dnacenter/) portal.
```
