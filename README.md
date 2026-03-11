# 🔍 Deep Research Agent

An AI-powered multi-agent research assistant that takes any topic, searches the web, synthesizes findings, and delivers a detailed report — straight to your inbox.

**Live Demo:** [https://deep-research-agent-production-0885.up.railway.app/](https://deep-research-agent-production-0885.up.railway.app/)

---

## 🚀 What It Does

Type any research topic and the agent will:
1. **Plan** a set of targeted web searches
2. **Search** the web in parallel across multiple queries
3. **Write** a detailed 5-10 page markdown report
4. **Email** the report directly to you via Resend

---

## 🧠 Agent Architecture

This project uses a multi-agent pipeline built with the OpenAI Agents SDK:

```
User Query
    │
    ▼
┌─────────────────┐
│  Planner Agent  │  → Plans 5 targeted web searches
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Search Agent   │  → Runs all searches in parallel
│  (x5 parallel)  │     using OpenAI WebSearchTool
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Writer Agent   │  → Synthesizes a detailed markdown report
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Email Agent    │  → Sends formatted HTML email via Resend
└─────────────────┘
```

| Agent | Model | Role |
|-------|-------|------|
| Planner | gpt-4o-mini | Breaks query into search terms |
| Search | gpt-4o-mini | Web search + summarization |
| Writer | gpt-4o-mini | Full report generation |
| Email | gpt-4o-mini | HTML email formatting + sending |

---

## 🛠️ Tech Stack

- **Frontend:** Gradio
- **AI Agents:** OpenAI Agents SDK
- **Web Search:** OpenAI WebSearchTool
- **Email:** Resend API
- **Deployment:** Railway
- **Language:** Python 3.11+

---

## 📦 Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/iqrai1/deep-research-agent.git
cd deep-research-agent
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your keys:
```
OPENAI_API_KEY=sk-...
RESEND_API_KEY=re_...
```

**4. Run**
```bash
python deep_research.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | ✅ | OpenAI API key for all agents |
| `RESEND_API_KEY` | ✅ | Resend API key for email delivery |
| `PORT` | Auto | Set automatically by Railway |

---

## 📁 Project Structure

```
deep_research/
├── deep_research.py       # Gradio UI + entry point
├── research_manager.py    # Orchestrates the full pipeline
├── planner_agent.py       # Search planning agent
├── search_agent.py        # Web search agent
├── writer_agent.py        # Report writing agent
├── email_agent.py         # Email delivery agent
├── requirements.txt       # Python dependencies
├── railway.json           # Railway deployment config
└── .env.example           # Environment variable template
```

---

## 🌐 Deployment

This app is deployed on [Railway](https://railway.app). Every push to `main` triggers an automatic redeploy.

---

*Built as a portfolio project to explore multi-agent AI architectures.*
