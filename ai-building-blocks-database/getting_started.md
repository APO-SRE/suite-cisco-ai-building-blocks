# Getting Started with the AI-Building-Blocks-Database

This guide walks through:

1. Standing up an Ubuntu-based VM (e.g., Azure VM)
2. Installing system dependencies (Python, Rust, etc.)
3. Configuring a Python environment for ChromaDB and optional NLP tasks
4. Setting up environment variables for the different AI “layers” (DOMAIN, EVENTS, FASTAPI, AGENTIC)

## 1. VM & Ubuntu Baseline

If you’re spinning up a new Azure VM or similar Ubuntu environment:

* **Operating System**: Ubuntu 24.04 (x64)
* **VM Size**: Standard D8as v5 (8 vCPUs / 32 GiB RAM) recommended for moderate workloads
* **Disk**:

  * Premium SSD LRS
  * \~128 GiB or more. Expand disk space if needed ([Microsoft Docs Reference](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/expand-disks?tabs=ubuntu))

Make sure you have sufficient disk space before you begin installing dependencies. For example:

```bash
df -h
```

If space is low, consider resizing or adding a new disk.

---

## 2. System Dependencies & Python Environment

### 2.1. Create or Clean a Python Virtual Environment

```bash
# (Optional) rename existing env if it exists
mv env env_old

# Create a fresh virtual environment
python3 -m venv env
source env/bin/activate

# Upgrade pip
pip install --upgrade pip
```

### 2.2. Install PyTorch for CPU (Nightly Build, Python 3.12)

```bash
pip install --no-cache-dir --pre torch torchvision \
  --index-url https://download.pytorch.org/whl/nightly/cpu
```

**Verify**:

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

You should see a version number for PyTorch (e.g. `2.8.0.dev...`) and `False` for CUDA availability (CPU only).

---

## 3. NLP & Embedding Libraries

### 3.1. Install Sentence Transformers

```bash
pip install --no-cache-dir sentence-transformers
```

**Verify**:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("Test embedding")
print(len(embedding))  # Should output 384
```

### 3.2. Keyword Extraction & Summarization

* **Keyword Extraction**:

  ```bash
  pip install keybert
  ```

* **Text Summarization**:

  ```bash
  pip install nltk transformers
  ```

**Verify**:

```python
from keybert import KeyBERT
kw_model = KeyBERT()
keywords = kw_model.extract_keywords("This is a test sentence to extract keywords from.")
print(keywords)

from transformers import pipeline
summarizer = pipeline("summarization")
summary = summarizer("Longer text to be summarized goes here.")
print(summary)
```

---

## 4. NLTK Data on a Headless Ubuntu Server

For local text processing without interactive downloads, you can manually install NLTK packages (stopwords, wordnet, etc.):

1. **Configure Local Data Directory**:

   ```bash
   export NLTK_DATA="$HOME/nltk_data"
   mkdir -p "$NLTK_DATA"/{corpora,tokenizers}
   ```

   (Add the `export` line to `~/.bashrc` or `~/.zshrc` for persistence.)

2. **Install `unzip`**:

   ```bash
   sudo apt-get install unzip
   ```

3. **Download Required NLTK Zip Packages**:

   ```bash
   cd "$NLTK_DATA"/corpora
   for pkg in wordnet omw-1.4 stopwords; do
     wget https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/${pkg}.zip
   done

   cd "$NLTK_DATA"/tokenizers
   wget https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip
   ```

4. **Unpack ZIPs via Python**:

   ```bash
   python3 - <<EOF
   import zipfile, os
   base = os.path.expanduser("~/nltk_data")

   # corpora
   corp = os.path.join(base, "corpora")
   for pkg in ("wordnet", "omw-1.4", "stopwords"):
       with zipfile.ZipFile(f"{corp}/{pkg}.zip") as z:
           z.extractall(corp)

   # tokenizers
   tok = os.path.join(base, "tokenizers")
   with zipfile.ZipFile(f"{tok}/punkt.zip") as z:
       z.extractall(tok)
   EOF
   ```

5. **Verify**:

   ```bash
   python3 - <<EOF
   import nltk
   from nltk.corpus import wordnet, stopwords

   print(wordnet.synsets("test")[0].definition())
   print(stopwords.words("english")[:5])
   EOF
   ```

   You should see the WordNet definition for “test” and the first few English stopwords.

---

## 5. Install Rust & Cargo (Needed by ChromaDB)

ChromaDB relies on some Rust-based dependencies (e.g., for vector indexing). Install Rust and Cargo:

```bash
sudo apt-get update
sudo apt-get install -y curl protobuf-compiler
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

Verify:

```bash
rustc --version
cargo --version
protoc --version
```

---

## 6. Install or Upgrade ChromaDB

Chroma provides a local persistent store for embeddings. Uninstall old versions if needed, then do a fresh install from GitHub:

```bash
pip uninstall chromadb
pip install --force-reinstall git+https://github.com/chroma-core/chroma.git@main
```

Check:

```bash
pip show chromadb
```

Optionally, test a simple PersistentClient usage:

```python
from chromadb import PersistentClient
client = PersistentClient(path="/tmp/chroma_db")
print("PersistentClient created successfully!", client)
```

---

## 7. Resolve Possible Dependency Conflicts

Some packages (like LangChain) may require specific older versions of `numpy`, `tenacity`, etc.:

```bash
pip install "numpy<2.0.0"
pip install "tenacity<9.0.0"
pip install "packaging<25.0"
```

Finally:

```bash
pip list
```

to confirm your installed packages.

---

## 8. Configure Environment Variables

Each “layer” (DOMAIN, EVENTS, FASTAPI, AGENTIC) has a dedicated block of environment variables. Copy `example.env` → `.env`, then customize:

* **Enable or disable each layer**: e.g. `FASTAPI_VECTOR_ENABLED=true`
* **Choose a backend**: `FASTAPI_VECTOR_BACKEND=azure` (or `chroma`, etc.)
* **Set concurrency** (`OMP_NUM_THREADS`, etc.) and credentials (Azure or Hugging Face model names).

For details, see the [Environment Variables Guide](example_environment_variables_guide.MD) or the relevant documentation sections in the main README.

---

## 9. Run the Layer Scripts

Once your `.env` is in place, run the indexing script(s) you want:

* **Domain Data**:

  ```bash
  python scripts/process_domain.py
  ```

  Pulls data from `domain_samples/<folder_name>` (set `DOMAIN_SAMPLES_INDEX_FOLDER_NAME` in `.env`).

* **Events**:

  ```bash
  python scripts/process_events.py
  ```

  Uses `events/sample_events.json`.

* **Docs (FASTAPI)**:

  ```bash
  python scripts/process_docs.py
  ```

  Reads from `platform_summaries/` plus various `api-docs/` folders.

* (If you add an **AGENTIC** layer, you’d do something similar.)

Each script will embed, chunk, and store documents in your chosen vector store (Azure, Chroma, or Elastic).

---

## After Setup: Check Disk Usage

```bash
df -h
```

Look for remaining disk space. Chroma can grow quickly if you index large datasets.

Example usage:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       123G   57G   67G  47% /
...
```

Here, we have \~67GB free.

---

## Project Goals & Refactoring Notes

The overarching goal of this repository is to provide a **modular AI-building-blocks database** for Cisco’s AI suite. Each “layer” (FASTAPI, EVENTS, DOMAIN, AGENTIC) can ingest data into a vector store of your choice. Scripts are refactored so that:

1. Each script explicitly sets which layer it is operating on (`LAYER="FASTAPI"` or `LAYER="EVENTS"`, etc.).
2. Environment variables in the `.env` file drive embedding provider selection, concurrency, chunking, and more.
3. The pipeline\_utils and indexer modules handle all the heavy lifting for embedding and vector indexing.
4. Variables like `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, and `NUM_CPUS` are properly set based on the chosen `(LAYER)_...` prefix.

---

## Next Steps

* **Automate**: Incorporate these scripts into a CI/CD process or cron job to re-index data when files change.
* **Validate**: Confirm data in your chosen vector backend (e.g., Azure Search Explorer, local Chroma folder, or Elasticsearch `_cat/indices`).
* **Integrate**: Combine with the [Cisco AI Building Blocks Agent](https://github.com/APO-SRE/ai-building-blocks-agent) for question-answering or domain-specific retrieval-augmented generation (RAG).

---

**Enjoy building out your multi-layer AI indexing pipelines!** For more details on advanced usage, environment variable structure, or troubleshooting, see the [README.md](README.md) and [Example Environment Variables Guide](example_environment_variables_guide.MD).

---

*Last updated: May 2025 by Jeff Teeter, Ph.D.*
