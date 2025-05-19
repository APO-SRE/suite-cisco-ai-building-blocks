
# Getting Started Guide

## 1. Prerequisites

1. **Git**  
   - Git is a version control tool used to download (“clone”) projects from GitHub.  
   - [Download Git here](https://git-scm.com/downloads) if you don’t already have it.  
   - During installation, you can mostly accept the defaults.

2. **Python 3.9+ (Recommended)**  
   - The AI Agent’s code is written in Python. You need Python installed to run it locally.  
   - [Download Python here](https://www.python.org/downloads/).

3. **Pip or Poetry (for installing Python dependencies)**  
   - If you have Python 3.9+, Pip should already be installed.  
   - Alternatively, some developers prefer [Poetry](https://python-poetry.org/) as a more modern package manager (optional).

4. **Azure Subscription**  
   - You need a Microsoft Azure account to create an Azure OpenAI resource.  
   - If you don’t have one, you can sign up for a free or pay-as-you-go Azure account:
     - [Create an Azure free account](https://azure.microsoft.com/free)

5. (**Optional**) **Docker**  
   - You can containerize and run the AI Agent inside Docker if you prefer.  
   - [Download Docker here](https://docs.docker.com/get-docker/).  
   - If you’re completely new, you can skip Docker for now and run directly on your local machine.

---

## 2. Download (Clone) the Repository

1. **Open a Terminal or Command Prompt**  
   - On Windows, search for “Command Prompt” or open Git Bash.  
   - On Mac/Linux, open Terminal.

2. **Navigate to a Folder Where You Want to Download the Code**  
   ```bash
   cd Documents
   ```

3. **Clone the Repository**  
   ```bash
   git clone https://github.com/APO-SRE/cisco-data-bridge-ai-agent.git
   ```
   - This creates a new folder named `cisco-data-bridge-ai-agent` in your current directory.

4. **Enter the Project Folder**  
   ```bash
   cd cisco-data-bridge-ai-agent
   ```

Now you’ve successfully downloaded (“cloned”) the AI agent code to your local machine.

---

## 3. Install Dependencies

There are two ways to install the necessary Python libraries:

### Option A: Using `requirements.txt` + pip

1. **Ensure you’re inside the project folder**  
   ```bash
   cd cisco-data-bridge-ai-agent
   ```
2. **Install using pip**  
   ```bash
   pip install -r requirements.txt
   ```
   - This downloads and installs all dependencies listed in `requirements.txt`.

### Option B: Using Poetry

1. **Install Poetry (if you haven’t already)**  
   - [Poetry Installation Guide](https://python-poetry.org/docs/#installation).
2. **Install dependencies**  
   ```bash
   poetry install
   ```
3. **(Optional) Activate the virtual environment**  
   ```bash
   poetry shell
   ```

Either approach is fine. If you’re new to Python, Option A with pip is typically simpler.

---

## 4. Setting Up Azure OpenAI (General LLM)

> **Important:** You must be approved to use Azure OpenAI before you can deploy GPT-3.5 or GPT-4 in your own Azure tenant. If you haven’t requested access yet, visit **[Azure OpenAI Access Request](https://aka.ms/oai/access)** and fill out the required form. You’ll receive an email once your request is approved.

### 4.1 Request (or Confirm) Access to Azure OpenAI

- **Request Access:**  
  - Submit your info at [Azure OpenAI Access Request](https://aka.ms/oai/access).  
  - Microsoft reviews your tenant and use case.  
  - Once approved, you can create an Azure OpenAI resource.

- **Verify Approval:**  
  - You’ll get an email from Microsoft confirming your approval.  
  - If you haven’t received approval yet, you won’t be able to deploy GPT models.

### 4.2 Create an Azure OpenAI Resource

1. **Create or Log into Your Azure Account**  
   - Go to the [Azure Portal](https://portal.azure.com) and log in.  
   - If you don’t have an account, create one ([Free Trial or Pay-as-you-go](https://azure.microsoft.com/free)).

2. **Create an Azure OpenAI Resource**  
   - In the Azure Portal, click “Create a Resource” → search for “Azure OpenAI” → click “Create.”  
   - Choose a **resource group**, **region**, and **pricing tier** that meets your needs.  
   - Note the **endpoint URL**—it will look something like:  
     ```
     https://<your-deployment-name>.openai.azure.com/
     ```

3. **Deploy a Model (e.g., GPT-4 or GPT-3.5)**  
   - Go to your newly created Azure OpenAI resource → “Model deployments.”  
   - Deploy or manage the model version you want (e.g., GPT-4).  
   - You will provide a **deployment name** (e.g., `gpt-4o`).

4. **Get Your Azure OpenAI Key**  
   - In your Azure OpenAI resource, go to **“Keys and Endpoint.”**  
   - Copy your **Key** (e.g., `pIAy6...`).

5. **Copy the Endpoint & Key**  
   - You’ll need these values to fill your `.env` file.

---

## 5. Understand & Create the `.env` File

1. **What Is a `.env` File?**  
   - A `.env` file stores configuration secrets/settings (like API keys, service URLs, or usernames/passwords).  
   - This helps you avoid committing sensitive data to GitHub.

2. **Find `ENV_TEMPLATE` in the Project Folder**  
   - Inside `cisco-data-bridge-ai-agent`, there’s a file named `ENV_TEMPLATE`.

3. **Copy `ENV_TEMPLATE` to `.env`**  
   - Mac/Linux:
     ```bash
     cp ENV_TEMPLATE .env
     ```
   - Windows Command Prompt:
     ```bat
     copy ENV_TEMPLATE .env
     ```
   - Or rename manually in your file explorer from `ENV_TEMPLATE` to `.env`.

4. **Open `.env` in a Text Editor**  
   - Fill in the variables for your environment. Each variable uses the format:
     ```
     VARIABLE_NAME=value
     ```

### 5.1 Configuring for Azure OpenAI (General Queries)

In the `.env` file, look for the section:

```bash
##################################
# LLM Selection
#  - "azure_openai" or "ollama" (or more if you add them)
##################################
LLM_TYPE=azure_openai

##################################
# RAG Selection
#  - "azure_search", "chroma", "elastic", or "none"
##################################
RAG_TYPE=azure_search

##################################
# Azure OpenAI Settings for General Queries
##################################
AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
AZURE_OPENAI_KEY=<your-azure-openai-key>
AZURE_OPENAI_MODEL=gpt-4o

# Optional parameters
AZURE_OPENAI_TEMPERATURE=0
AZURE_OPENAI_TOP_P=1.0
AZURE_OPENAI_MAX_TOKENS=4096
AZURE_OPENAI_PRESENCE_PENALTY=0.0
AZURE_OPENAI_FREQUENCY_PENALTY=0.0
AZURE_OPENAI_STREAM=True
AZURE_OPENAI_SYSTEM_MESSAGE="You are a helpful AI assistant. You must use the provided documents to answer questions when available. If the answer is not in the documents, you can use your own knowledge to provide an answer."
```

- **`LLM_TYPE=azure_openai`**: This tells the AI Agent to use Azure OpenAI for general queries.  
- **`AZURE_OPENAI_ENDPOINT`**: Paste your endpoint from the Azure Portal. Example:  
  ```
  https://my-openai-resource.openai.azure.com/
  ```
- **`AZURE_OPENAI_KEY`**: Paste the key from your Azure OpenAI resource.  
- **`AZURE_OPENAI_MODEL`**: Use the **deployment name** (e.g., `gpt-4o`) that you created.  

> **Note**: You can ignore the “Event Queries” section if you’re not doing RAG with an “events” index. Focus on the “Azure OpenAI Settings for General Queries” section.

---

## 6. (Optional) Setting Up Cisco Sandboxes

If you only want to run the AI Agent with minimal functionality (and just test the LLM), you can **skip** the Cisco integrations. If you **do** want to demo how the AI Agent interacts with Cisco platforms, set up one or more sandboxes:

- **Meraki**  
- **Catalyst Center**  
- (Optional) Cisco Spaces, Webex, etc.

See the [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/) site for details and follow the instructions in the sandbox sections of the guide for environment variables like `CISCO_MERAKI_API_KEY`, etc.

---

## 7. Run the AI Agent

### Option A: Directly with Python

1. **Ensure you’ve installed all dependencies** (`pip install -r requirements.txt` or `poetry install`).  
2. **Make sure your `.env` file is properly configured** (especially for Azure OpenAI).  
3. **Run the FastAPI server**:
   ```bash
   cd cisco-data-bridge-ai-agent
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   - This starts a server on [http://localhost:8000](http://localhost:8000).

4. **Open the Static Front-End** (if provided)  
   - Check [http://localhost:8000/docs](http://localhost:8000/docs) for FastAPI’s built-in docs.  
   - You might also find a sample UI at [http://localhost:8000/static/](http://localhost:8000/static/).

### Option B: Using Docker

1. **Build the Docker Image**  
   ```bash
   docker build -t cisco-data-bridge:latest .
   ```
2. **Run the Docker Container**  
   ```bash
   docker run -p 8000:8000 --env-file .env cisco-data-bridge:latest
   ```
   - `--env-file .env` tells Docker to use your local `.env` for environment variables.  
   - The application should be accessible at [http://localhost:8000](http://localhost:8000).

---

## 8. Testing the Agent

1. **Open the Application in Your Browser**  
   - Navigate to `http://localhost:8000/static/` (or another path depending on your config).  
   - You can test chat features, ask the LLM questions, etc.  

2. **Verify Azure OpenAI Connectivity**  
   - Try a simple query: “Hello, can you give me some fun facts about AI?”  
   - If configured correctly, the agent will use your **Azure OpenAI** endpoint and key to respond.

3. **Verify Any Cisco Integrations** (Optional)  
   - If you’ve enabled Meraki or Catalyst in your `.env`, try a query like:  
     “Retrieve information about my Meraki networks.”  
   - Watch the logs to confirm the AI agent is calling the Meraki or Catalyst APIs.

4. **Check Logs & Debug**  
   - Return to your Terminal to view logs.  
   - Look for any error messages about missing environment variables or connectivity problems.

---

## 9. Summary & Next Steps

- **You now have the Cisco Data Bridge AI Agent running locally** (or in a Docker container) with **Azure OpenAI** as the general LLM.  
- You can **enable or disable** various Cisco integrations using the `.env` file.  
- If you want more advanced features, such as retrieval-augmented generation (RAG) with Azure Cognitive Search or other vector databases (Chroma, Elastic), **set `RAG_TYPE`** accordingly and fill out the associated environment variables.

### Key Points to Remember

- **`.env` file**: Stores credentials and toggles for integrations—keep it private.  
- **Azure OpenAI**: Ensure you have a valid subscription, have requested/received access, and provided your endpoint, key, and model deployment name.  
- **Cisco Sandboxes**: Only configure if you want to demo actual Cisco platform integrations.  
- **Containerization**: Use the provided `Dockerfile` if you prefer Docker.

---

## 10. Additional Help

1. **Azure Portal**  
   - [Azure OpenAI Docs](https://learn.microsoft.com/azure/cognitive-services/openai/)  
   - [Azure Free Account](https://azure.microsoft.com/free)  

2. **Git & GitHub**  
   - [Beginner Tutorials on GitHub](https://docs.github.com/en/get-started)

3. **Python Basics**  
   - [Official Python Docs](https://docs.python.org/3/tutorial/)

4. **Docker**  
   - [Docker Documentation](https://docs.docker.com/get-started/)

5. **Cisco DevNet**  
   - [Sandbox Documentation](https://developer.cisco.com/site/sandbox/)

---

**Congratulations!** Your AI Agent is now ready with **Azure OpenAI** as its LLM—assuming you have requested and received approval to deploy GPT models in your Azure tenant. Feel free to explore additional capabilities, integrate other Cisco platforms, or customize the front-end for your specific use cases.