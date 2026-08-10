# 📧 AI Gmail Assistant

<img width="1908" height="920" alt="Screenshot 2026-08-10 122227" src="https://github.com/user-attachments/assets/52ec3ed7-a69d-416a-be09-d29ba02d424e" />

### 🤖 An Agentic AI-powered Gmail Assistant for intelligent email search, summarization, and analysis

The **AI Gmail Assistant** is a Generative AI application that allows users to interact with their Gmail inbox using **natural language**.

Instead of manually searching, opening, reading, and analyzing emails, users can simply ask questions and let the AI assistant retrieve and analyze the required information.

The application combines **Python, OpenAI GPT-4o-mini, LangChain, LangGraph, Gmail API, MCP, Google OAuth 2.0, and Streamlit** to build a tool-enabled Agentic AI system.

---

## ✨ Key Features

| Feature                    | Description                                      |
| -------------------------- | ------------------------------------------------ |
| 📬 Unread Email Count      | Get the number of unread emails                  |
| 📩 Recent Emails           | Retrieve the latest emails from Gmail            |
| 🔍 Gmail Search            | Search emails using Gmail search operators       |
| 🧠 Email Summarization     | Generate concise summaries of emails             |
| 📋 Action Item Extraction  | Identify tasks that may require user action      |
| ⏰ Deadline Detection       | Identify deadlines and time-sensitive activities |
| 📅 Meeting Detection       | Identify meetings mentioned in emails            |
| ⭐ Priority Analysis        | Identify high-priority actions                   |
| 💬 Conversation Memory     | Maintain context across conversations            |
| 🔐 Gmail OAuth             | Authenticate securely with Gmail                 |
| 🤖 Tool Calling            | Automatically select the appropriate Gmail tool  |
| 🔄 LangGraph Workflow      | Orchestrate agent and tool execution             |
| 🖥️ Streamlit UI           | Interactive chat-based user interface            |
| 🆕 New Conversation        | Start a fresh conversation with a new thread     |
| 🔎 Natural-Language Search | Search Gmail using natural-language requests     |

---

## 🚀 Project Overview

Traditional email applications require users to manually perform multiple steps:

```text
Search Email
     ↓
Open Email
     ↓
Read Content
     ↓
Understand Information
     ↓
Identify Important Actions
     ↓
Make a Decision
```

The **AI Gmail Assistant** simplifies this process by providing an AI-powered interface over Gmail.

The user communicates with the assistant using natural language.

For example:

```text
User:
Find unread emails from HDFC Bank.
```

The AI agent understands the request, determines which Gmail operation is required, invokes the appropriate tool, retrieves the relevant emails, analyzes the results, and generates a natural-language response.

---

## 🧠 How the AI Gmail Assistant Works

```text
                         👤 User
                           │
                           │ Natural Language Query
                           ▼
                  ┌──────────────────┐
                  │   Streamlit UI   │
                  └─────────┬────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │    LangGraph     │
                  │  Agent Workflow  │
                  └─────────┬────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │   GPT-4o-mini    │
                  │   AI Agent / LLM │
                  └─────────┬────────┘
                            │
                     Tool Selection
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
       Gmail Search     Summarizer    Action Analyzer
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                  ┌──────────────────┐
                  │    Gmail API     │
                  └─────────┬────────┘
                            │
                            ▼
                     📧 Gmail Inbox
                            │
                            ▼
                    Retrieved Emails
                            │
                            ▼
                     GPT-4o-mini
                            │
                            ▼
                      🤖 AI Response
                            │
                            ▼
                         👤 User
```

---

## 🤖 Agentic AI Architecture

The application follows a **tool-enabled Agentic AI architecture**.

The LLM does not directly access Gmail. Gmail operations are exposed through controlled tools that the LangGraph agent can invoke.

```text
User
 │
 ▼
Streamlit Application
 │
 ▼
LangGraph Agent
 │
 ▼
GPT-4o-mini
 │
 │ Determines required operation
 ▼
Tool Selection
 │
 ├── get_unread_email_count
 ├── get_recent_emails
 ├── summarize_latest_email
 ├── summarize_unread_emails
 ├── search_gmail
 ├── extract_action_items
 └── extract_deadlines_and_meetings
 │
 ▼
Gmail Service
 │
 ▼
Gmail API
 │
 ▼
Email Data
 │
 ▼
GPT-4o-mini
 │
 ▼
Final AI Response
 │
 ▼
Streamlit UI
```

This architecture separates:

* User interface
* Agent reasoning
* Tool execution
* Gmail service logic
* Gmail API communication
* Email analysis
* Response generation
* Conversation state

---

## 🔄 End-to-End Workflow

```text
1. User enters a natural-language question
                    ↓
2. Streamlit receives the request
                    ↓
3. LangGraph starts the agent workflow
                    ↓
4. GPT-4o-mini analyzes the user's intent
                    ↓
5. Agent selects the appropriate Gmail tool
                    ↓
6. Selected tool calls Gmail Service
                    ↓
7. Gmail Service communicates with Gmail API
                    ↓
8. Gmail data is retrieved
                    ↓
9. Tool returns the retrieved information
                    ↓
10. GPT-4o-mini analyzes the result
                    ↓
11. Final response is generated
                    ↓
12. Streamlit displays the response
```

---

## 🔍 Natural-Language Gmail Search

One of the important capabilities of the application is **AI-powered Gmail search**.

Users do not need to manually remember Gmail search operators.

For example:

```text
User:
Find unread emails from Google.
```

The agent can translate the intent into a Gmail search query such as:

```text
from:google is:unread
```

The workflow becomes:

```text
User Query
    ↓
GPT-4o-mini
    ↓
Understand User Intent
    ↓
Generate Gmail Search Query
    ↓
search_gmail Tool
    ↓
Gmail API
    ↓
Retrieve Matching Emails
    ↓
GPT-4o-mini
    ↓
Natural-Language Response
```

The search capability can work with Gmail operators such as:

```text
from:google
from:hdfcbank
subject:invoice
has:attachment
is:unread
newer_than:1d
```

---

## 💬 Example User Queries

### 📬 Email Management

```text
How many unread emails do I have?
```

```text
Show my latest 5 emails.
```

```text
Show me my recent emails.
```

### 🔍 Email Search

```text
Find emails from Google.
```

```text
Find emails from HDFC Bank.
```

```text
Find unread emails.
```

```text
Find emails containing invoices.
```

```text
Find emails with attachments.
```

```text
Find emails from Google received recently.
```

### 📝 Email Analysis

```text
Summarize my latest email.
```

```text
Summarize my unread emails.
```

```text
What action items are present in my emails?
```

```text
What are the high-priority actions?
```

```text
Are there any upcoming deadlines?
```

```text
Are there any meetings mentioned in my emails?
```

---

## 📋 Action Item Extraction

The assistant can analyze retrieved emails and identify tasks that may require user action.

For example:

```text
User:
What action items are present in my emails?
```

The system retrieves relevant emails and analyzes them using GPT-4o-mini.

The resulting information can contain:

```text
Action
Sender
Subject
Deadline
Priority
```

Example:

```text
1. Action: Complete a short form to indicate job preferences
   Sender: IBM Talent Acquisition
   Subject: Stay Matched to the Right Opportunities at IBM
   Deadline: Not mentioned
   Priority: Medium
```

The assistant is designed to distinguish potential actions from general promotional or informational emails.

---

## ⏰ Deadline and Meeting Detection

The application can analyze email content to identify:

* Upcoming deadlines
* Important dates
* Meetings
* Scheduled events
* Time-sensitive activities

Example:

```text
Are there any upcoming deadlines or meetings?
```

The assistant analyzes the relevant email content and returns detected information when available.

---

## 📝 Email Summarization

The application uses GPT-4o-mini to summarize email content.

The summarization process considers:

* Sender
* Subject
* Main purpose
* Important dates
* Important action items

Example:

```text
User:
Summarize my latest email.
```

The assistant retrieves the latest email, extracts the email body, and sends the relevant content to GPT-4o-mini for summarization.

---

## 💬 Conversation Memory

The application supports **conversation memory** using LangGraph checkpointing and thread-based conversations.

Each conversation is associated with a unique `thread_id`.

```text
Conversation
     │
     ▼
thread_id
     │
     ├── User Question 1
     ├── AI Response 1
     ├── User Question 2
     ├── AI Response 2
     ├── User Question 3
     └── AI Response 3
```

This allows the assistant to maintain context across multiple questions within the same conversation.

The application also provides a **New Conversation** option that creates a new thread and clears the visible conversation history.

---

## 🧰 Gmail Tools

The LangGraph agent currently exposes Gmail-related tools including:

```text
get_unread_email_count
get_recent_emails
summarize_latest_email
summarize_unread_emails
search_gmail
extract_action_items
extract_deadlines_and_meetings
```

The LLM decides which tool is appropriate based on the user's request.

For example:

```text
User:
How many unread emails do I have?

        ↓

GPT-4o-mini

        ↓

get_unread_email_count

        ↓

Gmail API

        ↓

Unread Email Count

        ↓

AI Response
```

---

## 🔐 Gmail Authentication

The application uses **Google OAuth 2.0** to authenticate with Gmail.

The authentication flow is:

```text
User
  ↓
Google OAuth
  ↓
Permission / Consent
  ↓
Gmail Authorization
  ↓
Access Token / Refresh Token
  ↓
Gmail API
```

OAuth credentials are stored locally and are excluded from version control through `.gitignore`.

Sensitive files such as:

```text
credentials/
credentials.json
token.json
token.pickle
```

should not be committed to GitHub.

---

## 🧩 Core Technologies

### 🐍 Python

Used as the primary programming language for the application.

### 🧠 OpenAI GPT-4o-mini

Used for:

* Natural-language understanding
* Tool selection
* Email summarization
* Action-item extraction
* Deadline detection
* Meeting detection
* Response generation

### 🔗 LangChain

Used for:

* LLM integration
* Tool creation
* Tool binding
* Message handling

### 🔄 LangGraph

Used for:

* Agent orchestration
* Workflow management
* Tool execution
* Conditional routing
* Conversation state
* Memory/checkpointing

### 📧 Gmail API

Used for:

* Reading Gmail profile information
* Retrieving emails
* Searching emails
* Reading email content
* Accessing Gmail metadata

### 🔐 Google OAuth 2.0

Used for secure authentication and authorization with Gmail.

### 🖥️ Streamlit

Used to build the interactive web-based chat interface.

### 🔌 MCP

Model Context Protocol is included in the project architecture as an extensible mechanism for connecting AI models with tools and external context.

---

## 🗂️ Project Structure

The project follows a modular architecture:

```text
AI_Gmail_Assistant/
│
├── agents/
│   ├── agent.py
│   ├── graph.py
│   ├── nodes.py
│   └── state.py
│
├── config/
│
├── credentials/
│   ├── credentials.json
│   └── token.json
│
├── mcp_server/
│
├── models/
│   └── llm.py
│
├── services/
│   ├── auth_service.py
│   ├── gmail_service.py
│   └── summary_service.py
│
├── tools/
│   └── gmail_tools.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> **Note:** The `images/`, `utils/`, `schemas/`, and `prompts/` folders were removed because they were empty and were not required by the current implementation.

### Main Components

| Component                     | Responsibility                                                |
| ----------------------------- | ------------------------------------------------------------- |
| `app.py`                      | Streamlit application and chat interface                      |
| `agents/agent.py`             | Creates the LLM agent and binds tools                         |
| `agents/graph.py`             | Defines and compiles LangGraph workflow                       |
| `agents/nodes.py`             | Defines chatbot and tool nodes                                |
| `agents/state.py`             | Defines agent state                                           |
| `models/llm.py`               | Configures GPT-4o-mini                                        |
| `services/gmail_service.py`   | Handles Gmail API operations                                  |
| `services/auth_service.py`    | Handles Gmail OAuth authentication                            |
| `services/summary_service.py` | Handles email summarization                                   |
| `tools/gmail_tools.py`        | Exposes Gmail operations as LangChain tools                   |
| `mcp_server/`                 | MCP-related project components                                |
| `credentials/`                | Local Gmail OAuth credentials                                 |
| `requirements.txt`            | Python dependencies                                           |
| `.gitignore`                  | Prevents sensitive and unnecessary files from being committed |

---

## 🏗️ Application Architecture

```text
┌──────────────────────────────────────────────┐
│                 User / Browser               │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                Streamlit UI                  │
│                                              │
│  • Chat Interface                            │
│  • Quick Actions                             │
│  • Gmail Statistics                          │
│  • Conversation Management                  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│               LangGraph Agent                │
│                                              │
│  • Agent State                               │
│  • Conditional Routing                       │
│  • Tool Execution                            │
│  • Conversation Memory                       │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                GPT-4o-mini                   │
│                                              │
│  • Intent Understanding                      │
│  • Tool Selection                            │
│  • Reasoning                                 │
│  • Response Generation                       │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│               Gmail Tools                    │
│                                              │
│  • Search                                    │
│  • Recent Emails                             │
│  • Unread Count                              │
│  • Summarization                             │
│  • Action Extraction                         │
│  • Deadline Detection                        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              Gmail Service                   │
│                                              │
│  Authentication                              │
│  Email Retrieval                             │
│  Search                                      │
│  Header Extraction                           │
│  Body Extraction                             │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                 Gmail API                    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
                📧 Gmail Inbox
```

---

## 🧪 Testing

The project includes multiple test scripts for validating individual components and the complete agent workflow.

Examples include:

```text
test_auth.py
test_search.py
test_search_tool.py
test_search_full.py
test_agent_search.py
test_agent_search_loop.py
test_graph_search.py
test_action_items.py
test_action_tool.py
test_deadlines.py
test_deadlines_tool.py
test_email_analysis.py
test_memory.py
test_graph_memory_action.py
test_multi_tool.py
```

The testing approach validates functionality progressively:

```text
Individual Service
       ↓
Individual Tool
       ↓
Agent Tool Calling
       ↓
LangGraph Workflow
       ↓
Memory / Checkpointing
       ↓
Streamlit Application
```

---

## 📊 Example Agent Execution

### User Query

```text
Find emails from Google.
```

### Agent Decision

```text
Intent:
Search Gmail

Tool:
search_gmail

Query:
from:google
```

### Gmail API

The Gmail API returns matching messages.

### Agent Response

```text
I found the following emails from Google:

1. Security Alert
2. Google Account Notification
3. Account Update
```

---

## 🎯 Project Goals

The main goals of this project are:

* Build a practical Agentic AI application
* Integrate an LLM with external APIs
* Implement Gmail tool calling
* Enable natural-language email search
* Automate email analysis
* Extract actionable information from emails
* Detect important deadlines and meetings
* Maintain conversation context
* Build a modular and extensible AI architecture
* Provide an intuitive Streamlit interface

---

## 📌 Current Capabilities

```text
✅ Gmail OAuth Authentication
✅ Gmail Profile Information
✅ Unread Email Count
✅ Recent Email Retrieval
✅ Full Email Retrieval
✅ Gmail Search
✅ Natural-Language Gmail Search
✅ Email Summarization
✅ Unread Email Summarization
✅ Action Item Extraction
✅ Deadline Detection
✅ Meeting Detection
✅ Priority Analysis
✅ LangChain Tools
✅ LangGraph Agent
✅ Tool Calling
✅ Conversation Memory
✅ Thread-Based Conversations
✅ Streamlit Chat UI
✅ Quick Actions
✅ New Conversation Support
```

---

## 🚀 Future Enhancements

The following capabilities can be added in future versions:

```text
📤 Send Emails
↩️ Generate Email Replies
📝 Create Draft Emails
📎 Attachment Analysis
📄 PDF / Document Analysis
📅 Google Calendar Integration
🏷️ Gmail Label Management
🗄️ Email Archiving
🗑️ Email Deletion with Confirmation
⚡ Async Processing
🚀 Production Deployment
📊 LLM Evaluation
📈 Observability and Monitoring
🔐 Enterprise Authentication
```

---

## 💡 Why This Project?

The project demonstrates how **Generative AI and Agentic AI can be integrated with real-world APIs and applications**.

Instead of building a chatbot that only generates text, this project demonstrates an AI agent that can:

```text
Understand
   ↓
Reason
   ↓
Select a Tool
   ↓
Interact with an External System
   ↓
Retrieve Data
   ↓
Analyze Data
   ↓
Generate an Intelligent Response
```

This makes the application closer to a real-world **Agentic AI system** rather than a simple LLM chatbot.

---

## 📈 Learning Outcomes

This project provides practical experience with:

* Generative AI application development
* LLM integration
* Prompt engineering
* LangChain tool development
* LangGraph agent orchestration
* Agent state management
* Conversation memory
* Gmail API integration
* Google OAuth authentication
* Natural-language search
* Structured email analysis
* Streamlit application development
* Modular Python architecture
* Agentic AI design patterns

---

## 🛡️ Security Considerations

Sensitive credentials should never be committed to the repository.

The project uses `.gitignore` rules for sensitive files such as:

```text
credentials/
credentials.json
token.json
token.pickle
.env
*.key
*.pem
```

Before pushing the project to GitHub, verify that no OAuth tokens, API keys, or other secrets are included in the repository.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd AI_Gmail_Assistant
```

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv gmail_ai_agent
```

Activate it:

```powershell
gmail_ai_agent\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Set the OpenAI API key in your environment.

For example, on Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

Do not commit API keys to GitHub.

### 5. Configure Gmail OAuth

Place the required Gmail OAuth configuration inside the local `credentials/` directory.

The application uses Google OAuth to authenticate the Gmail account.

### 6. Run the Application

Start Streamlit using:

```powershell
streamlit run app.py
```

The application will open in the browser.

---

## 🖥️ Streamlit Application

The Streamlit interface provides:

* Gmail account information
* Connection status
* Unread email count
* Total email count
* Gmail thread count
* Quick actions
* Natural-language chat
* Conversation memory
* New conversation functionality

Example interface flow:

```text
┌────────────────────────────────────────────┐
│ 📧 AI Gmail Assistant                     │
├────────────────────────────────────────────┤
│                                            │
│ 👤 Find unread emails from Google.         │
│                                            │
│ 🤖 I found the following emails...         │
│                                            │
│                                            │
│ Ask about your emails...                   │
└────────────────────────────────────────────┘
```

---

## 🏆 Project Summary

The **AI Gmail Assistant** is an end-to-end Agentic AI application that combines:

```text
Python
   +
OpenAI GPT-4o-mini
   +
LangChain
   +
LangGraph
   +
Gmail API
   +
Google OAuth
   +
MCP
   +
Streamlit
```

The application demonstrates how an LLM can understand natural-language requests, select appropriate tools, interact with Gmail, retrieve email information, analyze the retrieved data, maintain conversation context, and provide intelligent responses.

### 🔥 Final Architecture

```text
                👤 USER
                  │
                  ▼
          ┌───────────────┐
          │  Streamlit UI │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │   LangGraph   │
          │     Agent     │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │  GPT-4o-mini  │
          └───────┬───────┘
                  │
             Tool Calling
                  │
                  ▼
          ┌───────────────┐
          │ Gmail Tools   │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ Gmail Service │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │   Gmail API   │
          └───────┬───────┘
                  │
                  ▼
             📧 Gmail
                  │
                  ▼
          Email Data / Results
                  │
                  ▼
             GPT-4o-mini
                  │
                  ▼
          🤖 AI Response
                  │
                  ▼
             👤 USER
```

---

## 🛠️ Built With

**Python • OpenAI GPT-4o-mini • LangChain • LangGraph • Gmail API • Google OAuth 2.0 • MCP • Streamlit**

---

## 👨‍💻 Author

**Nagaraj Kamale**

Generative AI Engineer | Python | LLMs | RAG | Agentic AI | LangChain | LangGraph

---

⭐ If you find this project useful, consider giving the repository a star.
