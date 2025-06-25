import datetime
import os
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama


class EventInfo(BaseModel):
    title: str = Field(..., description="Name of the event")
    date: datetime.date = Field(..., description="Date of the event (YYYY-MM-DD)")
    location: str = Field(..., description="Where it takes place")


prompt = PromptTemplate.from_template(
    """
    Extract the event information from this text:

    {text}

    Format:
    {format_instructions}
    """
)

# Configure Ollama LLM
llm = ChatOllama(
    model="llama3.2",  # or whatever model you have installed
    base_url="http://your-server-ip:11434",  # Replace with your server's IP
    temperature=0,
)

parser = PydanticOutputParser(pydantic_object=EventInfo)
fmt = parser.get_format_instructions()

chain = prompt | llm | parser
print(fmt)

response: EventInfo = chain.invoke(
    {
        "text": "Join us at Scenic City Summit on June 19, 2025 in Chattanooga, TN for three days of workshops, sessions and a hackathon.",
        "format_instructions": fmt,
    }
)

print(f"Title: {response.title}")
print(f"Location: {response.location}")
print(f"Date: {response.date.strftime('%x')}")
