## AI Building Blocks – Environment-Variable Guide


> **DISCLAIMER – USE AT YOUR OWN RISK**  
> This software is provided “as is”, without any express or implied warranties,
> including, but not limited to, the implied warranties of merchantability and
> fitness for a particular purpose. In no event shall the authors or
> contributors be liable for any direct, indirect, incidental, special,
> exemplary, or consequential damages (including, but not limited to,
> procurement of substitute goods or services; loss of use, data, or profits;
> or business interruption) however caused and on any theory of liability,
> whether in contract, strict liability, or tort (including negligence or
> otherwise) arising in any way out of the use of this software.  
> This project is for **demonstration / development** only and is not intended
> for production. By using the code you acknowledge that you have read,
> understood, and accepted these terms.

---

## 0.  Cheat-sheet

| Want to                                | Touch these vars                                                    | Typical value                                     |
| -------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| Turn a Cisco platform ON/OFF           | `ENABLE_*` (global)                                                 | `true` / `false`                                  |
| Pick your vector backend               | `<LAYER>_VECTOR_BACKEND`                                            | `chroma`, `azure`, `elastic`                      |
| Pick your embedder                     | `<LAYER>_EMBEDDING_PROVIDER` + optional `<LAYER>_HUGGINGFACE_MODEL` | `huggingface` / `azure`                           |
| Recreate or append a Chroma collection | `<LAYER>_CHROMA_RECREATE_INDEX`                                     | `true`, `false`, **blank = prompt**               |
| Keyword & summary tuning               | `<LAYER>_CHROMA_KEYWORD_TYPE`, `<LAYER>_CHROMA_SUMMARIZER_TYPE`     | `yake` vs `keybert`, `sumy` vs `transformer`      |
| CPU limits                             | `<LAYER>_<BACKEND>_OMP_NUM_THREADS` etc.                            | `1` for process-based, ≥ cores for single-process |

---

## 1. Global block

| Variable                      | Purpose                                        | Default in `example.env`                  |
| ----------------------------- | ---------------------------------------------- | ----------------------------------------- |
| `DEBUG_MODE`                  | Verbose logging toggle                         | `false`                                   |
| `ENABLE_*`                    | One flag per Cisco SaaS (Meraki, Spaces, etc.) | all **false** except `ENABLE_MERAKI=true` |
| Cisco creds (`CISCO_*`, etc.) | Demo keys for DevNet sandboxes                 | *place-holders*                           |

---

## 2. Layer anatomy

Every layer (`AGENTIC`, `FASTAPI`, `DOMAIN`, `EVENTS`) repeats the same 7 mini-sections:

1. **Feature flags** – `*_VECTOR_ENABLED`, `*_LLM_ENABLED`
2. **Core providers** – which embedder / vector DB / LLM to use
3. **LLM details** – model name, temperature, etc.
4. **Backend-specific search settings** – index names, API versions
5. **Embedding / chunking** – chunk size, batch size, HF model override
6. **Concurrency** – per-backend thread & CPU caps
7. **Post-retrieval** – keyword & summarisation switches

### 2.1 Example – FASTAPI layer

```ini
# ❶ enable vector + LLM
FASTAPI_VECTOR_ENABLED=true
FASTAPI_LLM_ENABLED=true

# ❷ use Chroma DB + HF embeddings + Azure-hosted GPT-4o
FASTAPI_VECTOR_BACKEND=chroma
FASTAPI_EMBEDDING_PROVIDER=huggingface      # default HF model below
FASTAPI_LLM_PROVIDER=azure

# ❸ Azure LLM tuning
FASTAPI_AZURE_LLM_MODEL=gpt-4o
FASTAPI_AZURE_LLM_TEMPERATURE=0.5
...

# ❹ Chroma storage
FASTAPI_CHROMA_DB_PATH=./chroma_dbs/fastapi
FASTAPI_CHROMA_COLLECTION_DOCS=api-docs-index
FASTAPI_CHROMA_COLLECTION_PLATFORM=platform-summaries-index
FASTAPI_CHROMA_RECREATE_INDEX=      # ← blank → CLI prompt

# ❺ Embeddings
FASTAPI_HUGGINGFACE_MODEL=sentence-transformers/all-MiniLM-L6-v2
FASTAPI_CHUNK_SIZE=2000
FASTAPI_EMBED_BATCH_SIZE=64

# ❻ Concurrency
FASTAPI_CHROMA_OMP_NUM_THREADS=1
FASTAPI_NUM_CPUS=8                  # used by pipeline_utils

# ❼ After retrieval
FASTAPI_CHROMA_ENABLE_KEYWORDS=true
FASTAPI_CHROMA_KEYWORD_TYPE=keybert       # yake is faster, keybert more accurate
FASTAPI_CHROMA_ENABLE_SUMMARIZATION=true
FASTAPI_CHROMA_SUMMARIZER_TYPE=transformer # sumy is lighter
```

---

## 3. Keyword & Summary knobs

| Variable                         | Options                                                  | Notes                          |
| -------------------------------- | -------------------------------------------------------- | ------------------------------ |
| `<LAYER>_CHROMA_KEYWORD_TYPE`    | `yake` (fast) / `keybert` (semantic)                     |                                |
| `<LAYER>_CHROMA_SUMMARIZER_TYPE` | `sumy` (extractive, light) / `transformer` (abstractive) | transformer needs more CPU/RAM |

Recommended mixes:

* **Lean CPU:** `sumy` + `yake`
* **Best quality:** `transformer` + `keybert`

---

## 4. Chroma (local vector DB)

* **Path** – one folder per layer, eg. `./chroma_dbs/fastapi`.
* **(Re)create logic**

  * `..._CHROMA_RECREATE_INDEX=true` → wipe silently
  * `false` → always append
  * **blank** → interactive prompt (“(R)ecreate or (A)ppend?”)

If you don’t want the DB in Git, keep `.gitignore` stanza:

```gitignore
/chroma_dbs/
```

---

## 5. Hugging Face models

* Leaving `<LAYER>_HUGGINGFACE_MODEL` **blank** falls back to
  `sentence-transformers/all-MiniLM-L6-v2` (≈22 MB, 384-dim).
* Want a beefier encoder?  Set e.g.

  ```ini
  DOMAIN_HUGGINGFACE_MODEL=sentence-transformers/all-mpnet-base-v2
  ```

  Expect \~4× RAM & \~2× latency on CPU.

---

## 6. Concurrency tips

| Scenario                              | OMP/MKL threads | `NUM_CPUS`              | Comment                    |
| ------------------------------------- | --------------- | ----------------------- | -------------------------- |
| Many *processes* (default in scripts) | **1**           | number of logical cores | prevents oversubscription  |
| Single long-running service           | ≈ cores         | ≈ cores                 | okay if no other CPU users |

---

## 7. Stable document IDs (Chroma & Azure)

* By default `process_*` scripts hash each text chunk → deterministic IDs.
* **Chroma** now uses `collection.upsert()` so reruns overwrite, not duplicate.
* **Azure AI Search** upserts automatically when `id` repeats.

No extra env-vars needed.

---

### Quick start

```bash
cp example.env .env
# fill in your Azure + Cisco keys

# build indexes
python -m scripts.process_docs      # FASTAPI layer
python -m scripts.process_domain    # DOMAIN layer
python -m scripts.process_events    # EVENTS layer
```

