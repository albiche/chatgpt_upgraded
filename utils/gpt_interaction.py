from openai import OpenAI
from config import OPENAI_API_KEY

# Initialiser le client OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt, context, model, max_tokens, role):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": f"Tu es {role}."},
            {"role": "user", "content": f"Contexte : {context}\n\nQuestion : {prompt}"}
        ],
        max_tokens=max_tokens
    )
    message = response.choices[0].message.content.strip()
    return message
