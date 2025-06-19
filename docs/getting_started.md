# Getting Started with Cisco Platform AI Agent

Welcome to the Cisco Platform AI Agent, a modular toolkit for building retrieval-augmented generative AI solutions that integrate seamlessly with Cisco platforms such as Meraki, Catalyst Center, Webex, and others.

---

## 1. Prerequisites

Before you begin, ensure you have:

* **Git** ([Download Git](https://git-scm.com/downloads))
* **Python 3.9+** ([Download Python](https://www.python.org/downloads/))
* **Pip** (included with Python) or **Poetry** ([Poetry Installation](https://python-poetry.org/docs/#installation))
* **Azure Subscription** ([Create Azure Account](https://azure.microsoft.com/free))
* **Docker** (optional) ([Download Docker](https://docs.docker.com/get-docker/))

---

## 2. Clone the Repository

Clone the Cisco Platform AI Agent repository:

```bash
git clone https://github.com/APO-SRE/suite-cisco-ai-building-blocks.git
cd suite-cisco-ai-building-blocks
```

---

## 3. Set Up Environment Variables

Copy and edit the environment sample file:

```bash
# Copy the sample and edit `.env` for your setup
cp env.sample .env
# Edit .env to configure VECTOR_BACKEND, FEATURE flags, credentials, etc.
```

---

## 4. Install Dependencies

Create and activate a Python virtual environment and install dependencies from `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then, install the project in editable mode from the root directory:

```bash
pip install -e .
```

---

## 5. Initial Data Indexing (Optional)

You can optionally build initial vector indexes:

```bash
python -m db_scripts.process_domain  # For API docs
python -m db_scripts.process_events  # For enriching events and injecting back into vector database
```

---
## 6. Interactive CLI

After installation, these CLI tools are available:

* `menu`: Interactive CLI menu
* `start-cisco-platform-ai`: Run FastAPI (hot-reload)
* `stop-cisco-platform-ai`: Terminate FastAPI server
* `start-telemetry-stack`: Bring up Tempo/Prometheus/Grafana via Docker Compose
* `stop-telemetry-stack`: Tear down Tempo/Prometheus/Grafana via Docker Compose
* `status-application`: Show FastAPI & telemetry stack status
* `create-platform`: Scaffold a new platform
* `reset-platform`: Delete platform artifacts
* `create-sdk`: Generate an OpenAPI-based SDK
* `delete-sdk`: Remove a generated SDK
* `create-platform-index`: Index platform functions
* `create-domain-demo-index`: Create demo domain-specific indexes
* `create-events-index`: Index sample telemetry/events data
* `create-platform-route`: Add new FastAPI platform routes
* `delete-platform-routes`: Remove FastAPI routes for a platform
* `list-platform-registry`: Show Platform Registry
* `update-platform-registry`: Add / edit platform entries
* `sync-registry-with-scaffold`: Reconcile registry with files
* `convert-swagger`: Convert Swagger v2 spec → OpenAPI 3
* `manage-env`: Edit environment variables
* `cisco`: Cisco API Docs

Run the interactive menu with:

```bash
menu
```

---

## 8. Cisco Integrations

To integrate Cisco platforms:

* Place your OpenAPI spec in `src/source_open_api`
* Use the provided commands (`create-platform`, `create-sdk`) to scaffold integrations

### Preloaded Cisco Platforms

* Catalyst Center
* Meraki
* SD-WAN
* Intersight
* Nexus Dashboard
* Nexus Hyperfabric
* AI Defense
* Cloud Control Firewall Manager
* Cloudlock
* Secure Access
* Umbrella
* Webex
* Spaces location

### Enabling a New Cisco Platform

1. **Upload the OpenAPI file** – copy the JSON or YAML spec to `src/source_open_api/`.
2. **Install the SDK** – if a Python SDK exists, install it in your environment.
3. **Update the registry** – edit `src/app/llm/platform_registry.json` with the platform's short name, associated `openapi_name`, and `sdk_module` (if any).
4. **Create a SDK if none exists** – run `create-sdk` to generate one; this automatically installs it and updates the registry.
5. **Create the platform** – run `create-platform` to scaffold clients, services, and dispatchers.
6. **Add the platform route** – run `create-platform-route` to expose FastAPI endpoints.
7. **Create-platform-index** - run 'create-platform-index' to embed the platform's functions for retrieval.
8. Start chatting through [index.html](http://127.0.0.1:8000/static) or via Webex if configured.

 
---

## 8. Testing the AI Agent

Verify basic functionality:

* Visit [http://127.0.0.1:8000/static](http://127.0.0.1:8000/static) to access the sample UI.
* Run sample queries to test Azure OpenAI connectivity and Cisco integrations.

---

## 9. Troubleshooting

Check the logs in your terminal for any errors or issues related to environment variables or integrations.

---

## 10. Additional Resources

* [Azure OpenAI Docs](https://learn.microsoft.com/azure/cognitive-services/openai/)
* [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
* [Docker Documentation](https://docs.docker.com/get-started/)

---

**Congratulations!** Your Cisco Platform AI Agent setup is complete. You can now explore advanced features, integrate more Cisco platforms, and customize the agent for your needs.
