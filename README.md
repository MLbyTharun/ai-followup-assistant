# 🚀 AI Follow-Up Assistant

An AI-powered follow-up system designed to help small businesses and sales teams never miss a lead — and never write the same message twice.

## 🔗 Live Demo
- 🌐 Streamlit App: [Try it here](https://followup-ai-assistant--tharunabc.replit.app)
- 🎥 Demo Video: [Watch here](#)

---

## 💡 Problem

In fast-moving sals environments:

- Leads go cold due to missed follow-ups  
- Valuable deals slip through the cracks  
- Teams spend repetitive effort drafting similar messages  

Most small businesses don’t have sophisticated CRM automation — and even when they do, personalization doesn’t scale.

---

## ✅ Solution

**AI Follow-Up Assistant** acts as a lightweight, intelligent CRM layer that:

- Tracks customer intractions  
- Identifies overdue and upcoming follow-ups  
- Generates **context-aware, personalized messages using LLMs**  

This is not just an AI demo — it's a **usable workflow tool**.

---

## 🧠 Core Features

### 📌 Customer Management
- Store customer details: name, contact, company  
- Track status, notes, and interaction history  

### 📊 Smart Dashboard
- View:
  - Follow-ups due today  
  - Overdue leads  
  - Upcoming follow-ups  

### ✍️ AI Message Generation
- Generate tailored follow-up messages in one click  
- Choose tone (professional, friendly, persuasive)  
- Uses stored context to produce relevant outreach  

### ⚡ Fast Execution
- Copy generated message  
- Send via WhatsApp, email, or CRM  

---

## ⚙️ Tech Stack

| Layer       | Technology |
|------------|-----------|
| Frontend   | Streamlit |
| Backend    | Python |
| ORM        | SQLAlchemy |
| Database   | SQLite (MVP) |
| LLM        | Llama 3.1 8B Instruct (via Hugging Face) |
| Deployment | Replit |

---

## 🧩 System Flow

1. User adds customer data  
2. System tracks follow-up timelines  
3. Dashboard surfaces actionable leads  
4. LLM generates personalized message using notes + context  
5. User sends message externally  

---

## 🎯 Target Users

- Small businesses without CRM automation  
- Sales teams scaling outreach  
- Early-stage startups needing a lightweight AI assistant  

---
## Limitations

- Uses **local SQLite** for demo purposes; not designed for multi‑user production.
- No user authentication; all data is stored in one shared database.
- FOllow‑up scheduling is based on `last_interaction` and a simple “days from today” rule.
- LLM is called live on each request; no caching or rate‑limiting yet.

## Future Improvements

- Add **user authentication** and per‑user data isolation.
- Replacing SQLite with **PostgreSQL** for a scalable SaaS.
- Add **tags and status labels** (e.g., cold / warm / hot / converted).
- Integrate **email/WhatsApp notifications** (e.g., via SMTP or WhatsApp API).
- Add **analytics dashboard** (e.g., conversion rate, reply rate per follow‑up).
- Implement **tone/style presets** (formal, friendly, sales‑focused, etc.).

## Why This Design?

- **SQLite** – Simple, file‑based, no server needed for MVP.
- **Streamlit** – Fast prototyping with clean UI for non‑frontend‑heavy devs.
- **Llama 3.1 8B** – Good balance of quality and cost for small‑scale demos.

## How the AI Message Works

- The app uses your **customer notes** as context.
- A **prompt template** instructs the model to:
  - be polite and concise,
  - avoid making up facts,
  - adapt tone based on the selected style (polite / persuasive / reminder).
- You can tweak the prompt in `llm.py` to change the style or length.

## Simple Evaluation

- **Success criteria**:
  - Messages are clear, polite, and relevant to the notes.
  - Messages do not invent fake dates, names, or prices.
- In practice:
  - Over 80% of sample messages were usable as first‑draft messages.
  - For a real product, I’d track:
    - Reply rate.
    - Manual edits needed per message.

## Why I Built This

- To practice:
  - Connecting an LLM to a real workflow.
  - Building a simple but usable product UX.
  - Deploying a Python app on Replit.
- This is a stepping stone toward:
  - Full‑fledged AI‑assisted CRM tools.
  - Multi‑user SaaS‑style applications.
 
## FAQ

**Q: Can I use this for real business customers?**  
A: Yes, but ensure you store no sensitive or regulated data without extra precautions.

**Q: Why not use a hosted backend?**  
A: This is intentionally kept simple for demo; for production, I’d move to a proper backend service and DB.

**Q: Can I customize the message tone?**  
A: Yes, you can edit the prompt in `llm.py` to change the style.



## 🚀 Getting Started

```bash
git clone https://github.com/MLbyTharun/ai-followup-assistant.git
cd ai-followup-assistant
pip install -r requirements.txt
