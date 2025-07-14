# Getting Started with Cisco Platform AI Agent

Welcome to the Cisco Platform AI Agent, a modular toolkit for building retrieval-augmented generative AI solutions that integrate seamlessly with Cisco platforms such as Meraki, Catalyst Center, Webex, and others.

---

## 1. Prerequisites

Before you begin, ensure you have:

* **Git** ([Download Git](https://git-scm.com/downloads))
* **Python ≥ 3.12**

  * If you’re on Ubuntu 22.04 or earlier, install via the Deadsnakes PPA (see next section).
* **Build Tools** for native extensions

  * A C/C++ compiler (`build-essential`) and Python headers (`python3.12-dev`) are required to compile ChromaDB's HNSW backend.
* **Pip** (included with Python) or **Poetry** ([Poetry Installation](https://python-poetry.org/docs/#installation))
* **Azure Subscription** ([Create Azure Account](https://azure.microsoft.com/free))
* **Docker** (optional) ([Download Docker](https://docs.docker.com/get-docker/))

---

## 2. Install Python 3.12 on Ubuntu

If your system Python is older than 3.12, add Deadsnakes and install:

```bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install \
  python3.12 \
  python3.12-venv \
  python3.12-dev \
  build-essential -y
```

> **Note:** The `python3.12-dev` package provides the C-API headers; `build-essential` brings in `gcc`, `g++`, and `make`, enabling C++11 support for packages like `chroma-hnswlib`.

---

## 3. Clone the Repository

```bash
git clone https://github.com/APO-SRE/suite-cisco-ai-building-blocks.git
cd suite-cisco-ai-building-blocks
```

---

## 4. Set Up Environment Variables

Copy and edit the environment sample file:

```bash
cp env.sample .env
# Open .env and configure VECTOR_BACKEND, feature flags, API keys, etc.
```

---

## 5. Create & Activate a Virtual Environment

```bash
python3.12 -m venv .venv      # Use the installed Python 3.12
source .venv/bin/activate
```

---

## 6. Install Python Dependencies

Upgrade pip and install from `requirements.txt`, then install the project in editable mode:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

---

## 7. Initial Data Indexing (Optional)

Optionally build initial vector indexes:

```bash
python -m db_scripts.process_domain    # For API docs
python -m db_scripts.process_events    # For events enrichment
```

--- 



## 8. Configure Docker & Enable Compose

To get the telemetry stack working, you must install and configure Docker and Docker Compose, and grant your user permission to talk to the Docker daemon:

1. **Install Docker Engine**

   ```bash
   sudo apt-get update
   sudo apt-get install -y docker.io
   sudo systemctl enable --now docker
   ```
2. **Install the Docker Compose v2 CLI plugin**

   ```bash
   sudo mkdir -p /usr/lib/docker/cli-plugins
   sudo curl -SL \
      "https://github.com/docker/compose/releases/download/v2.36.2/docker-compose-linux-$(uname -m)" \
      -o ~/.docker/cli-plugins/docker-compose
 
   sudo chmod +x /usr/lib/docker/cli-plugins/docker-compose
   ```

   > Alternatively install legacy via `sudo apt-get install docker-compose`, but v2 is recommended.
3. **Add your user to the Docker group**

   ```bash
   sudo groupadd docker   # only if the group doesn’t already exist
   sudo usermod -aG docker $USER
   newgrp docker          # apply changes to this session
   ```
4. **Verify installation**

   ```bash
   docker --version         # e.g. Docker version 20.10.x
   docker compose version   # e.g. Docker Compose v2.x.x
   ```

Once Docker and Compose are configured, the `start-telemetry-stack` command will successfully bring up Tempo, Prometheus, and Grafana.

---

## 9. Interactive CLI Tools

After installation, the following CLI commands are available:

* `menu`                      – Interactive menu
* `start-cisco-platform-ai`   – Run FastAPI (hot-reload)
* `stop-cisco-platform-ai`    – Terminate FastAPI server
* `start-telemetry-stack`     – Launch Tempo/Prometheus/Grafana
* `stop-telemetry-stack`      – Tear down telemetry stack
* `status-application`        – Show FastAPI & telemetry status
* `create-platform`           – Scaffold a new platform
* `reset-platform`            – Delete platform artifacts
* `create-sdk`                – Generate an OpenAPI-based SDK
* `delete-sdk`                – Remove a generated SDK
* `create-platform-index`     – Embed platform functions
* `create-domain-demo-index`  – Create demo domain indices
* `create-events-index`       – Index sample telemetry/events
* `create-platform-route`     – Expose FastAPI endpoints
* `delete-platform-routes`    – Remove FastAPI routes
* `list-platform-registry`    – Show Platform Registry
* `update-platform-registry`  – Add / edit registry entries
* `sync-registry-with-scaffold` – Reconcile registry with files
* `convert-swagger`           – Swagger v2 → OpenAPI 3
* `manage-env`                – Edit environment variables
* `cisco`                     – Cisco API Docs viewer

Run the interactive menu with:

```bash
menu
```

---

## 10. Cisco Integrations

To integrate Cisco platforms:

1. Place your OpenAPI spec in `src/source_open_api/`.
2. If a Python SDK exists, install it or run `create-sdk` to generate and install one.
3. Update `src/app/llm/platform_registry.json` with the platform’s short name, `openapi_name`, and `sdk_module`.
4. Run `create-platform` to scaffold clients, services, and dispatchers.
5. Run `create-platform-route` to add FastAPI endpoints.
6. Run `create-platform-index` to embed platform functions.
7. Start chatting via [http://127.0.0.1:8000/static](http://127.0.0.1:8000/static) or through Webex.

---

## 11. Testing the AI Agent

* Visit [http://127.0.0.1:8000/static](http://127.0.0.1:8000/static) for the sample UI.
* Run sample queries to verify AI & Cisco integrations.

---

## 12. Troubleshooting

* **Docker socket permission**: If you see “permission denied” on `/var/run/docker.sock`, ensure you’ve added your user to the `docker` group and run `newgrp docker`.
* **Compose command not found**: Double‑check the CLI‑plugins folder and executable name (`docker-compose`) in `/usr/lib/docker/cli-plugins`.
* **Python version mismatch**: Ensure your venv uses Python 3.12 per `pyproject.toml` (`>=3.12`).
* **C++ build errors** (e.g. `Unsupported compiler`): Install `build-essential` and `python3.12-dev`.
* **ChromaDB native backend fails**: Either install the toolchain or remove `chroma-hnswlib` from dependencies to fall back to the pure‑Python parser.
* **Permission or SSH issues**: If using VS Code Remote – SSH, confirm your SSH `authorized_keys` and `IdentityFile` settings (see the VS Code Remote SSH guide).

---

## 13. Additional Resources

* [Azure OpenAI Docs](https://learn.microsoft.com/azure/cognitive-services/openai/)
* [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/)
* [Docker Documentation](https://docs.docker.com/get-started/)

---

**Congratulations!** Your Cisco Platform AI Agent setup is complete. You can now explore advanced features, integrate more Cisco platforms, and customize the agent for your needs.
