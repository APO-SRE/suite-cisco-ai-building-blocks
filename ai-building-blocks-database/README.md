Thought for 5 seconds


![Cisco AI Building Blocks Database Banner](assets/cisco_ai%20building_blocks_domain_project.png)

# Cisco AI Building Blocks — Database Project

*Vector-index pipelines for every AI layer*

> **DISCLAIMER — USE AT YOUR OWN RISK**
> The software in this repository is provided **“as is”** without warranty of any kind, either express or implied.
> It is intended for demonstration and development. **Do not** deploy in production until you have reviewed, tested, and hardened the code for your own requirements. By using this project you acknowledge that you have read and accepted these terms.

---

## 1  What this repo does

This repository houses the **data-engineering side** of the Cisco AI Building Blocks Suite.
It contains the scripts and utilities that:

| 🏗️ Task                                                                                     | 📁 Where / How                    |
| -------------------------------------------------------------------------------------------- | --------------------------------- |
| Chunk raw files into manageable text chunks                                                  | `scripts/utils/chunking.py`       |
| Embed each chunk with your choice of encoder (Azure OpenAI, Hugging Face, etc.)              | `scripts/utils/pipeline_utils.py` |
| Write the embeddings to your chosen vector backend (Azure Cognitive Search, Chroma, Elastic) | `scripts/indexers/*`              |
| Do all of the above per **layer** (FASTAPI, EVENTS, DOMAIN, AGENTIC)                         | `scripts/process_*.py`            |

The resulting vector indices are then consumed by the runtime agent in the companion project: **[Cisco AI Building Blocks Agent](https://github.com/APO-SRE/ai-building-blocks-agent)**.

---

## 2  Layer-specific processors

| Layer                  | Script                       | Typical content                                 |
| ---------------------- | ---------------------------- | ----------------------------------------------- |
| **FASTAPI**            | `scripts/process_docs.py`    | API docs & platform-level references            |
| **EVENTS**             | `scripts/process_events.py`  | High-volume telemetry / event blobs             |
| **DOMAIN**             | `scripts/process_domain.py`  | Domain-specific or industry data                |
| **AGENTIC** (optional) | `scripts/process_agentic.py` | Long-form knowledge for chain-of-thought agents |

Each script hard-codes its `LAYER` value and automatically reads the matching section in your **`.env`**.

---

## 3  Environment-variable driven

All configuration lives in **`.env`** (copy `example.env` to get started).
Variables are grouped by layer:

```
# FASTAPI ───────────────────────────────────────────
FASTAPI_VECTOR_ENABLED=true
FASTAPI_VECTOR_BACKEND=chroma
FASTAPI_EMBEDDING_PROVIDER=huggingface
FASTAPI_CHROMA_RECREATE_INDEX=false
…

# DOMAIN ────────────────────────────────────────────
DOMAIN_VECTOR_ENABLED=true
DOMAIN_VECTOR_BACKEND=azure
DOMAIN_AZURE_SEARCH_INDEX_NAME=domain-index
…
```

A full cheat-sheet is available in [here](example_environment_variables_guide.MD)
---

## 4  Project layout

```
ai-building-blocks-database/
├── assets/                         # banners & diagrams
├── chroma_dbs/                     # local Chroma storage (git-ignored)
├── domain_samples/                 # sample JSON for DOMAIN layer
├── events/                         # raw event docs
├── platform_summaries/             # FASTAPI layer docs
├── scripts/
│   ├── process_docs.py             # FASTAPI
│   ├── process_events.py           # EVENTS
│   ├── process_domain.py           # DOMAIN
│   ├── process_agentic.py          # AGENTIC (optional)
│   ├── indexers/                   # Azure / Chroma / Elastic drivers
│   └── utils/                      # chunking, NLP, pipeline helpers
└── .env / example.env              # configuration
```

---

## 5  Quick start

```bash
# 1  Clone & create your .env
git clone https://github.com/APO-SRE/AI-Building-Blocks-Database.git
cp example.env .env
# edit keys, backend choices, and layer flags

# 2  Create the indices you need
python scripts/process_domain.py      # DOMAIN layer
python scripts/process_events.py      # EVENTS layer
python scripts/process_docs.py        # FASTAPI layer
# (optional) python scripts/process_agentic.py
```

You’ll see progress logs for chunking, embedding, and upsert operations.
Validate the output in your vector backend’s UI or via the test queries provided in the Agent project.

---

## 6  How it works (nutshell)

1. **Pipeline factory** decides which encoder & vector DB to spin up (driven by `.env`).
2. **Chunker** splits source text (size tunable per layer).
3. **Embedder** converts chunks to vectors in mini-batches (CPU/OMP threads also tunable).
4. **Indexer** upserts to the target backend.

   * Chroma collections live under `./chroma_dbs/<layer>/…`
   * Azure & Elastic indices use the names in `.env`.

All heavy-lifting happens inside `pipeline_utils.embed_and_index()` so each `process_*.py` stays tiny (< 100 LOC).

---

## 7  Extending & automating

* **Add a backend**: write a new class in `scripts/indexers/`, expose the env-vars, done.
* **Add a layer**: copy an existing script, change `LAYER` and source paths.
* **CI/CD**: hook the scripts into your pipeline to auto-refresh indices on doc updates.

---

## 8  License

Licensed under the **Apache 2.0** license. See [`LICENSE`](LICENSE) for the full text.

---

*Last updated — May 2025*
