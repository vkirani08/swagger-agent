# 🧠 Swagger Agent (Local AI Assistant for OpenAPI)

A local, lightweight, and privacy-friendly assistant that helps you interact with and explore OpenAPI (Swagger) specifications using a Small Language Model (SLM) via [Ollama](https://ollama.com/).

---

## ✨ Features

- 📝 Accepts any OpenAPI (Swagger) JSON file
- 🤖 Uses an LLM (like `phi` via Ollama) to answer questions about API endpoints
- 🔒 Fully offline and privacy-friendly — no data sent to cloud
- 🔍 Understands endpoints, request/response formats, and parameter details
- 💬 Chat-like interface via terminal

---

## 📁 Folder Structure
```
swagger-agent/
├── main.py # Entry point for the assistant
├── api_parser.py # Swagger file loading & parsing logic
├── requirements.txt # Python dependencies
├── petstore.json # Sample Swagger spec (Petstore)
├── github-api.json # Swagger spec for GitHub APIs
├── openapi.json # Default spec loaded on startup
├── .gitignore
├── README.md
```

---

## ⚙️ Prerequisites

- ✅ Python 3.9+
- ✅ [Ollama](https://ollama.com) installed and running
- ✅ A pulled local model (e.g. `phi`)

---

## 🧪 Setup Instructions

### 1️⃣ Clone the Repo

```
git clone git@github.com:vkirani08/swagger-agent.git
cd swagger-agent
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Start Ollama in a separate terminal
bash
Copy
Edit
ollama serve
ollama pull phi  # Only needed once
```

## 🚀 Run the Agent
python main.py
You will be prompted to ask questions about the API in the loaded Swagger file (openapi.json by default).

## 💬 Example Prompts
What endpoint allows me to get a pet by ID?

How can I add a new pet?

What parameters does the updateUser endpoint take?

Give me an example POST request for /user/login

## 📦 Supported Specs
You can replace the default openapi.json with any OpenAPI spec, like:

bash
Copy
Edit
curl -o github-api.json https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
cp github-api.json openapi.json
Then re-run:

bash
Copy
Edit
python main.py

## 🔒 Security Notes
✅ No external API calls — LLM runs locally using Ollama

✅ Swagger specs are parsed safely using prance and validated

