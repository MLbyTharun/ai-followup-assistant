import os
from huggingface_hub import InferenceClient

HF_API_TOKEN = os.environ.get("HF_API_TOKEN")
MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"

client = InferenceClient(
    model=MODEL_NAME,
    token=HF_API_TOKEN
)

def generate_followup(customer, tone="professional"):
    if not HF_API_TOKEN:
        return "Hugging Face API token not found. Please add HF_API_TOKEN in Replit Secrets."

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant for a small business. Write short, professional customer follow-up messages."
        },
        {
            "role": "user",
            "content": f"""
Write one {tone} follow-up message for this customer.

Customer name: {customer['name']}
Contact: {customer['contact']}
Company: {customer['company']}
Last interaction date: {customer['last_interaction']}
Next follow-up date: {customer['next_followup']}
Status: {customer['status']}
Interest level: {customer['interest_level']}
Notes: {customer['notes']}

Requirements:
- Be polite and professional
- Keep it under 120 words
- Personalize using the notes
- Do not invent facts
- End with a clear next step
"""
        }
    ]

    try:
        output = client.chat_completion(
            messages=messages,
            max_tokens=180,
            temperature=0.7
        )
        return output.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating message: {str(e)}"