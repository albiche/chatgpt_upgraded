from openai import OpenAI
from config import OPENAI_API_KEY

# Initialiser le client OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(prompt, context):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Vous êtes un assistant utile."},
            {"role": "user", "content": f"Contexte : {context}\n\nQuestion : {prompt}"}
        ],
        max_tokens=2000
    )
    message = response.choices[0].message.content.strip()
    return message
