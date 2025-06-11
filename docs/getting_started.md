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

Copy and edit the example environment file:

```bash
cp example.env .env
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
python -m db_scripts.process_events  # For telemetry
```

---

## 6. Launch the AI Agent Service

Navigate to the agent service directory and launch the service:

```bash
cd src/app
uvicorn main:app --reload --log-level debug
```

Your AI Agent will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 7. Interactive CLI

After installation, these CLI tools are available:

* `menu`: Interactive CLI menu
* `create-platform`: Scaffold new Cisco platform integration
* `create-sdk`: Generate Python SDK from OpenAPI spec
* `create-platform-index`: Index platform API functions
* `create-domain-demo-index`: Create demo domain-specific indexes
* `create-events-index`: Index sample telemetry/events data

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
* Webex
* Nexus Dashboard
* SD-WAN
* Intersight

---

## 9. Testing the AI Agent

Verify basic functionality:

* Visit [http://127.0.0.1:8000/static](http://127.0.0.1:8000/static) to access the sample UI.
* Run sample queries to test Azure OpenAI connectivity and Cisco integrations.

---

## 10. Troubleshooting

Check the logs in your terminal for any errors or issues related to environment variables or integrations.

---

## 11. Additional Resources

* [Azure OpenAI Docs](https://learn.microsoft.com/azure/cognitive-services/openai/)
* [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
* [Docker Documentation](https://docs.docker.com/get-started/)

---

**Congratulations!** Your Cisco Platform AI Agent setup is complete. You can now explore advanced features, integrate more Cisco platforms, and customize the agent for your needs.
