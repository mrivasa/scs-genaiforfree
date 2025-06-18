import os
from openai import OpenAI

token = os.getenv("GH_MODELS_TOKEN", "")

client = OpenAI(base_url="https://models.github.ai/inference", api_key=token)

with open("customer_service_prompt.txt", "r") as f:
    customer_service_prompt = "".join(f.readlines())

system_message = {"role": "system", "content": customer_service_prompt}

user_message = {
    "role": "user",
    "content": "I was charged twice for the same item. What do I do?",
}

response = client.chat.completions.create(
    messages=[system_message, user_message],
    temperature=0.3,
    top_p=0.7,
    model="openai/gpt-4.1-mini",
)

print(response.choices[0].message.content)
