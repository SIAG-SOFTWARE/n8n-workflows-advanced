# n8n Workflows — Advanced Automation Suite

Production-grade automation examples powered by **n8n**, **Python**, and modern cloud services.  
This repository contains real-world, business-ready workflows used across SIAG Software projects.

Includes:
- Lead intake pipelines  
- Scraping & monitoring flows  
- Customer notification systems  
- Helper scripts for Python-node integration  

This suite is designed to show how SIAG Software builds **scalable**, **transparent**, and **robust** automations.

---

## 📁 Repository Structure

```
n8n-workflows-advanced/
│
├── workflows/
│   ├── lead_pipeline.json
│   ├── scraping_pipeline.json
│   └── notifications_pipeline.json
│
├── scripts/
│   └── python_helper.py
│
├── docs/
│   ├── architecture.png
│   ├── diagram_leads.png
│   ├── diagram_scraping.png
│   └── diagram_notifications.png
│
├── README.md
└── LICENSE
```

---

# 🚀 Workflows Included

## 1. 📩 Lead Pipeline (Webhook → CRM → Telegram)
**Purpose:** Capture leads, sanitize them, enrich data, and notify your CRM + Telegram channel.

**Key components:**
- Webhook trigger  
- Email/phone sanitizer  
- CRM integration (HubSpot, Airtable, Notion or custom API)  
- Telegram/WhatsApp notifications  
- Branching logic for multi-form input  

File: `workflows/lead_pipeline.json`

---

## 2. 🕷 Web Scraping Pipeline (Cron → Python → API → Email Report)
**Purpose:** Run scheduled (cron) extractions, process data through Python, and send summary reports.

**Key components:**
- Cron trigger  
- Python function node  
- HTTP Request node (API submission)  
- Email/SMS notification  
- Error-handling fallback path  

File: `workflows/scraping_pipeline.json`

---

## 3. 🔔 Customer Notification System  
**Purpose:** Notify customers automatically depending on rules (status changes, delays, payments).

**Key components:**
- Webhook/API trigger  
- Conditional branches  
- Multi-channel notification: Email / WhatsApp / SMS  
- Logging with Google Sheets / DB  

File: `workflows/notifications_pipeline.json`

---

# 🧩 Helper Script (Python)

Located in `scripts/python_helper.py`

Example usage:  
- data cleaning  
- scraping  
- classification  
- API enrichment  

Compatible with the **n8n Python Function node**.

---

# 🔧 Requirements

No global installs needed.  
Just import the JSON workflows into your n8n instance.

Python helper uses:
- `requests`
- `beautifulsoup4`
- `pydantic`
- `lxml`

---

# 📘 License — MIT

This project is open-source under the MIT License.  
Feel free to modify and use in your own automations.

---

# 🌐 About SIAG Software

SIAG Software builds AI-driven tools, automation workflows, chatbots, and full-stack solutions for modern businesses.

**Contact:** siag.software@protonmail.com
