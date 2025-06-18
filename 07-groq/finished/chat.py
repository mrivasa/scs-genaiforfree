import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    model="llama-3.3-70b-versatile",
)

print(response.choices[0].message.content)
