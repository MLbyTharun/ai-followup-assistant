# ai-followup-assistant

**An AI‑powered follow‑up assistant for small businesses.**

Helps track customers, identify overdue follow‑ups, and generate personalized outreach messages using a modern LLM.

---

## Live Demo
**[Streamlit App](https://your-app-name.replit.app)**

## Demo Video
**[Watch Demo](https://youtu.be/your-demo-video)**

---

## What it solves
- Businesses forget to follow up with leads, lose deals, and miss opportunities.
- Sales teams waste time drafting similar messages again and again.

This app:
- Stores customer data (name, contact, company, status, notes).
- Shows a “Follow up today” dashboard.
- Generates polished, personalized follow‑up messages using Llama 3.1 8B Instruct.

---

## How it works

1. **Add a customer**  
   - Name, contact, company, status, notes, and interaction history.

2. **View the dashboard**  
   - See which customers are due for follow‑up today, overdue, or upcoming.

3. **Generate an AI message**  
   - Click “Generate Follow‑up”, pick a tone.
   - The app uses your notes to write a short, polite, persuasive message.

4. **Copy and send**  
   - Paste the message into WhatsApp, email, or your CRM.

---

## Tech stack

- **Frontend:** Streamlit (Python).
- **Backend:** Python + SQLAlchemy.
- **Database:** SQLite (local MVP storage).
- **AI:** Llama 3.1 8B Instruct via Hugging Face InferenceClient.
- **Deployment:** Replit.

---

## Who this is for

- **Small businesses** that want to never miss a follow‑up.
- **Sales teams** that want to scale personalized outreach.
- **Founders** and **early‑stage startups** that want a lightweight, no‑code‑style AI assistant.

---

## How to run it locally

```bash
git clone https://github.com/MLbyTharun/ai-followup-assistant.git
cd ai-followup-assistant
pip install -r requirements.txt
HUGGINGFACE_API_TOKEN=your_token_here streamlit run app.py
```

> 🔐 Keep your `HUGGINGFACE_API_TOKEN` safe. Do not commit it to GitHub.

---

## Why this is great for a startup

- **Real‑world workflow:** You’re not just “showing off AI”; you’re integrating it into a sales/crm‑style workflow.
- **From idea → shipped app:** You built a small but working product that demonstrates business understanding, frontend, backend, and AI in one place.
- **Extensible:**  
  - Add PostgreSQL, auth, and multi‑user support when you need a proper SaaS.
  - Add more AI features (e.g., next‑step suggestions, priority scoring, or email auto‑drafting).

---

## Future roadmap

- Add user authentication (login).
- Replace SQLite with PostgreSQL for multi‑user apps.
- Add tags and segmentation (cold/warm/hot leads).
- Add “Send via email” integration (SMTP or API).
- Add analytics (conversion rate per follow‑up).

---

## How to contribute

- Bug reports?
- Extra features?
- Better UI?

Open an issue or pull request.  
This is a beginner‑friendly project, and all contributions are welcome.

---

## Credits

Built by **Tharun K** for startup and AI‑internship practice.  
For hiring, reach out on **LinkedIn / GitHub** or via email: `your‑email‑here@example.com`.

---

> **“A tool that doesn’t just handle data, but speaks to customers.”**
