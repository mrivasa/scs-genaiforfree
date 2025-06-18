import json
import os

from lab_prompts import prompts
from openai import OpenAI

token = os.getenv("GH_MODELS_TOKEN", "")

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=token,
)

system_message = {
    "role": "system",
    "content": prompts["SYSTEM"],
}
user_message = {
    "role": "user",
    "content": prompts["USER"],
}
assistant_message = {
    "role": "assistant",
    "content": prompts["ASSISTANT"],
}

for ticket in prompts["SAMPLES"]:
    messages = [
        system_message,
        user_message,
        assistant_message,
    ]
    messages.append({"role": "user", "content": ticket})
    response = client.chat.completions.create(
        messages=messages,
        temperature=0.7,
        max_tokens=750,
        model="openai/gpt-4.1-mini",
    )
    content = response.choices[0].message.content.strip()
    content = content[content.index("{") : content.rindex("}") + 1]
    summary = json.loads(content)
    print("Category: ", summary["category"])
    print("Summary: ", summary["summary"])
    print("-" * 60)
