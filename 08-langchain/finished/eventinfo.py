import datetime
import os
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq


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
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
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
