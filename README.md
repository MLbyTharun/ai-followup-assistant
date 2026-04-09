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

## 🚀 Getting Started

```bash
git clone https://github.com/MLbyTharun/ai-followup-assistant.git
cd ai-followup-assistant
pip install -r requirements.txt
