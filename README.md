# 🤖 Coded Agent Chatbot

An intelligent Agentic AI Chatbot built with Python and deployed on the **UiPath Cloud** platform. The agent can reason, plan, and take actions autonomously using LangGraph workflows.
The AI uses question answer format to answer the queries or give output to queries.

---

## 🚀 Features

- 🧠 Agentic AI that reasons and takes actions step by step
- ☁️ Integrated with UiPath Cloud system
- 🔄 Built using LangGraph for agent workflow management
- 🐍 Python-based with a clean modular structure
- ❓ You ask anything for topic and it answers in Question Answer format.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangGraph | Agent workflow & state management |
| UiPath Cloud | Cloud deployment & automation |
| LLM APIs | AI reasoning & responses |

---

## 📁 Project Structure

```
Agentic-AI-Chatbot/
├── main.py              # Main entry point
├── .agent/              # Agent configuration files
├── .uipath/             # UiPath integration files
├── langgraph.json       # LangGraph configuration
├── pyproject.toml       # Python project dependencies
├── .gitignore           # Files excluded from Git
└── README.md            # You are here!
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Dustbinturbo/Agentic-AI-Chatbot.git
cd Agentic-AI-Chatbot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_key_here
UIPATH_API_KEY=your_key_here
```

### 5. Run the chatbot
```bash
python main.py
```

---

## 🔐 Security Note

Never commit your `.env` file. It contains secret API keys. This project uses `.gitignore` to keep it safe.

---

## 👤 Author

**Dustbinturbo**
- GitHub: [@Dustbinturbo](https://github.com/Dustbinturbo)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).\


The porject is currently under maintenance with issues resolving to API tokens in UI cloud path system. 
The issues will be resolved quickly .
Thank you for waiting.
