## AI Building Blocks – Environment-Variable Guide

> **DISCLAIMER – USE AT YOUR OWN RISK**
> This software is provided “as is”, without any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software.
> This project is for **demonstration/development** only and is not intended for production.

---

## 0. Cheat-sheet

| Action                       | Variables                                                            | Typical Values                                |
| ---------------------------- | -------------------------------------------------------------------- | --------------------------------------------- |
| Toggle Cisco platform ON/OFF | `ENABLE_*` (global)                                                  | `true`, `false`                               |
| Choose vector backend        | `<LAYER>_VECTOR_BACKEND`                                             | `chroma`, `azure`, `elastic`                  |
| Choose embedder              | `<LAYER>_EMBEDDING_PROVIDER`, `<LAYER>_HUGGINGFACE_MODEL` (optional) | `huggingface`, `azure`                        |
| Chroma collection handling   | `<LAYER>_CHROMA_RECREATE_INDEX`                                      | `true`, `false`, **blank = prompt**           |
| Keyword & summarization      | `<LAYER>_CHROMA_KEYWORD_TYPE`, `<LAYER>_CHROMA_SUMMARIZER_TYPE`      | `yake`, `keybert`, `sumy`, `transformer`      |
| CPU/threading control        | `<LAYER>_<BACKEND>_OMP_NUM_THREADS`, etc.                            | `1` (process-based), ≥ cores (single-process) |

---

## 1. Global Settings

| Variable                   | Purpose                       | Default                              |
| -------------------------- | ----------------------------- | ------------------------------------ |
| `DEBUG_MODE`               | Verbose logging               | `true`                               |
| `ENABLE_*`                 | Cisco platform toggles        | `ENABLE_MERAKI=true`, others `false` |
| `MERAKI_DASHBOARD_API_KEY` | Meraki API Key                | *(required)*                         |
| Cisco Credentials          | Platform-specific credentials | *(placeholders)*                     |

---

## 2. Layer Configuration

Each layer (`AGENTIC`, `FASTAPI`, `DOMAIN`, `EVENTS`) contains 7 sections:

1. **Feature Flags**: `*_VECTOR_ENABLED`, `*_LLM_ENABLED`
2. **Core Providers**: Embedding, vector DB, LLM providers
3. **LLM Details**: Model parameters
4. **Backend Settings**: Storage, search configurations
5. **Embedding/Chunking**: Chunk sizes, batch sizes, embedding models
6. **Concurrency**: Threading and CPU usage
7. **Post-Retrieval Options**: Keyword extraction and summarization

### Example – FASTAPI Layer

```ini
FASTAPI_VECTOR_ENABLED=true
FASTAPI_LLM_ENABLED=true

FASTAPI_VECTOR_BACKEND=chroma
FASTAPI_EMBEDDING_PROVIDER=huggingface
FASTAPI_LLM_PROVIDER=azure

FASTAPI_AZURE_OPENAI_MODEL=gpt-4o
FASTAPI_AZURE_LLM_TEMPERATURE=0.5

FASTAPI_CHROMA_DB_PATH=./chroma_dbs/fastapi
FASTAPI_CHROMA_COLLECTION_PLATFORM=function-definitions-index
FASTAPI_CHROMA_RECREATE_INDEX=

FASTAPI_HUGGINGFACE_MODEL=sentence-transformers/all-MiniLM-L6-v2
FASTAPI_CHUNK_SIZE=2000
FASTAPI_EMBED_BATCH_SIZE=64

FASTAPI_CHROMA_OMP_NUM_THREADS=1
FASTAPI_NUM_CPUS=8

FASTAPI_CHROMA_ENABLE_KEYWORDS=true
FASTAPI_CHROMA_KEYWORD_TYPE=keybert
FASTAPI_CHROMA_ENABLE_SUMMARIZATION=true
FASTAPI_CHROMA_SUMMARIZER_TYPE=transformer
```

---

## 3. Keyword & Summary Options

| Variable                         | Choices                                                        | Recommended Use                     |
| -------------------------------- | -------------------------------------------------------------- | ----------------------------------- |
| `<LAYER>_CHROMA_KEYWORD_TYPE`    | `yake` (fast), `keybert` (semantic)                            | CPU: `yake`, Quality: `keybert`     |
| `<LAYER>_CHROMA_SUMMARIZER_TYPE` | `sumy` (light, extractive), `transformer` (heavy, abstractive) | CPU: `sumy`, Quality: `transformer` |

---

## 4. Chroma Configuration

* **DB Paths**: Defined per layer (`./chroma_dbs/<layer>`)
* **Index Creation**:

  * `true`: recreate silently
  * `false`: append
  * blank: interactive prompt

Include in `.gitignore`:

```gitignore
/chroma_dbs/
```

---

## 5. HuggingFace Embeddings

* Default: `sentence-transformers/all-MiniLM-L6-v2` (22MB, fast)
* Larger option: `sentence-transformers/all-mpnet-base-v2` (more accurate, higher resource use)

---

## 6. Concurrency Guidelines

| Scenario           | Threads | CPUs                    |
| ------------------ | ------- | ----------------------- |
| Multiple Processes | `1`     | logical cores available |
| Single Process     | `cores` | all available cores     |

---

## 7. Stable Document IDs

* Deterministic IDs used by default
* Automatic `upsert()` behavior for reruns

---

## Quick Start

```bash
cp example.env .env
# Configure keys and settings

# Build indexes
python -m scripts.process_docs      # FASTAPI
python -m scripts.process_domain    # DOMAIN
python -m scripts.process_events    # EVENTS
```

This standardized and updated guide aligns fully with your current `.env` configuration and recommended best practices.
