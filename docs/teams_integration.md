Below is a complete, step-by-step implementation guide for integrating your FastAPI-based AI agent with Microsoft Teams using the Bot Framework and Microsoft Entra ID (formerly Azure AD). 

########################################################################################################################
DISCLAIMER: USE AT YOUR OWN RISK

This software is provided "as is", without any express or implied warranties, including, but not limited to,
the implied warranties of merchantability and fitness for a particular purpose. In no event shall the authors or
contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits;
or business interruption) however caused and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of the use of this software.

This script is provided for demonstration and development purposes only and is not intended for use in production
environments. You are solely responsible for any modifications or adaptations made for your specific use case.

By using this code, you agree that you have read, understood, and accept these terms.
#######################################################################################################################


This guide covers:

* Bot registration (personal vs. corporate)
* Entra ID configuration
* Deployment
* Testing strategies
* Auth requirements
* Common pitfalls

---

# 🧭 OVERVIEW: Microsoft Teams Bot Integration

The integration uses the Microsoft Bot Framework + Microsoft Teams APIs via a webhook endpoint in your FastAPI app. Microsoft sends bot messages to your endpoint and expects responses via their Bot Connector API.

---

# 🧱 COMPONENTS

| Layer                    | Role                                        |
| ------------------------ | ------------------------------------------- |
| FastAPI `/teams/webhook` | Receives POST Activity from Teams           |
| Bot Framework API        | Sends messages via token-authenticated HTTP |
| Entra ID (Azure AD)      | Provides OAuth2 token (App Registration)    |
| Microsoft Teams          | UI front-end where the bot lives            |

---

# 🧪 STEP 1: Decide Account Type

## ✅ OPTION 1: Microsoft Personal Account (e.g. Outlook.com)

✔️ Good for local testing and personal use
❌ Cannot access Teams in a corporate tenant
❌ Limited deployment scope

**Use when:** You don’t have corporate Entra admin access, but want to experiment

## ✅ OPTION 2: Work/School Account (Entra/Azure AD)

✔️ Required for org-wide Teams access
✔️ Can publish bots across channels or users
❗ Requires Admin Consent for some permissions (ask your IT team)

---

# 🧷 STEP 2: Create the Bot Registration

## ✅ 2.1 Create Azure Account (if needed)

* [https://portal.azure.com](https://portal.azure.com)
* Sign in with your corporate or personal Microsoft account

## ✅ 2.2 Register Bot App

Go to:
🔗 [https://portal.azure.com](https://portal.azure.com) > Search: “Azure Active Directory” → “App registrations”

1. Click **"New registration"**
2. Fill in:

   * **Name**: Platform-AI-Chat
   * **Supported account types**: Choose:

     * Single tenant = only your org (e.g. Cisco)
     * Multitenant = allow cross-tenant installs
   * **Redirect URI**: Leave blank for now (not needed)
3. Click "Register"

You will get:

| Field                   | Use For           |
| ----------------------- | ----------------- |
| Application (client) ID | `TEAMS_APP_ID`    |
| Directory (tenant) ID   | `TEAMS_TENANT_ID` |

---

## ✅ 2.3 Add Bot Framework Channel

Go to:
🔗 [https://portal.azure.com](https://portal.azure.com) → Search “Bot Services” → “+ Create”

* Bot handle: `askapo-bot`
* Microsoft App ID: **paste App ID from registration**
* Hosting: Choose “Other”
* Messaging endpoint:
  `https://<your-domain>/chat/teams/webhook` (must be HTTPS + reachable)
* Enable Microsoft Teams channel

---

## ✅ 2.4 Generate Client Secret

Back in App Registration:

1. Go to "Certificates & secrets"
2. Click "New client secret"
3. Set expiration (e.g. 6 or 12 months)
4. Copy secret and store it — this is your:

```
TEAMS_APP_PASSWORD
```

---

## ✅ 2.5 Set Required API Permissions

1. Go to App → “API Permissions”
2. Click “Add permission” → "APIs my organization uses"
3. Search: `Bot Framework`
4. Add:

   * `Bot Framework` → Application → `.default` scope
5. Click **“Grant admin consent”** (if you have access)

⚠️ If not, ask an Entra admin to do this later — your bot won’t reply otherwise.

---

# 📦 STEP 3: Update Your FastAPI App

## ✅ Add `teams_routes.py`

Save the scaffold you already have to:

```
app/routers/teams_routes.py
```

## ✅ Add to app.main.py

```python
from app.routers.teams_routes import router as teams_router
app.include_router(teams_router)
```

## ✅ Add `.env` entries:

```
TEAMS_APP_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
TEAMS_APP_PASSWORD=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

(Optionally: `TEAMS_TENANT_ID`)

---

# 🌐 STEP 4: Deploy Secure Endpoint

Your bot must be reachable at HTTPS:

```
https://yourdomain.com/chat/teams/webhook
```

✔️ DNS must point to your VM
✔️ NGINX must route `/chat/teams/webhook` to `localhost:8000/chat/teams/webhook`
✔️ Let’s Encrypt cert should be valid (you already have this from Webex)

---

# 🧪 STEP 5: Local Testing with Bot Framework Emulator

Download:
🔗 [https://github.com/microsoft/BotFramework-Emulator](https://github.com/microsoft/BotFramework-Emulator)

1. Run Uvicorn:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
2. Open Emulator
3. Connect to:

   ```
   http://localhost:8000/chat/teams/webhook
   ```
4. Paste in your App ID / Password
5. Send `"ping"` and verify `"You said: ping"` returns

---

# 🧪 STEP 6: Sideload to Microsoft Teams

## ✅ Build `manifest.zip` file

Contains:

* manifest.json
* bot icon 32x32
* bot icon 192x192

🧱 Sample manifest.json:

```json
{
  "$schema": "https://developer.microsoft.com/en-us/json-schemas/teams/v1.11/MicrosoftTeams.schema.json",
  "manifestVersion": "1.11",
  "version": "1.0.0",
  "id": "<APP-ID>",
  "packageName": "com.platformaichat.bot",
  "name": { "short": "PlatformAIChat", "full": "Platform AI Chat" },
  "description": { "short": "Chat with Cisco AI Assistant", "full": "Ask questions about Cisco platforms..." },
  "developer": {
    "name": "Cisco",
    "websiteUrl": "https://yourdomain.com",
    "privacyUrl": "https://yourdomain.com/privacy",
    "termsOfUseUrl": "https://yourdomain.com/terms"
  },
  "bots": [{
    "botId": "<APP-ID>",
    "scopes": [ "personal" ],
    "supportsFiles": false,
    "isNotificationOnly": false
  }],
  "permissions": [ "identity", "messageTeamMembers" ],
  "validDomains": [ "yourdomain.com" ]
}
```

## ✅ Upload to Teams

1. Open Teams
2. Click "Apps" → “Upload a custom app” → "Upload for me or my teams"
3. Select your `manifest.zip`
4. Start chatting with your bot

---

# 🧪 STEP 7: Test Message Roundtrip

* Type `ping`
* Bot replies `"You said: ping"`
* Check logs on VM to verify request + response cycle

---

# 🧩 Optional: Production Enhancements

| Feature                      | How to Implement                         |
| ---------------------------- | ---------------------------------------- |
| 💬 LLM responses             | Use `get_llm()` like in `chat_routes.py` |
| 🧠 Message history/threading | Store in Redis, SQLite, or memory        |
| 🧪 Span-level tracing        | Already present via OpenTelemetry        |
| 🔐 Token refresh daemon      | Add caching or TTL-check to token logic  |
| 📈 Analytics                 | Log `from.id`, `timestamp`, `text`       |

---

# ✅ Summary Checklist

| Task                              | Done? |
| --------------------------------- | ----- |
| Azure app registration            |       |
| Bot handle + Teams channel added  |       |
| Client secret generated           |       |
| BotFramework API permission added |       |
| `/teams/webhook` route working    |       |
| Test with Emulator                |       |
| Sideload to Teams                 |       |
| Message received + reply sent     |       |

---
 
