import os
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    """
    List three pros and three cons of the following topic: 
    
    Topic: {topic}

    Format as:
    Pros:
    - ...
    Cons:
    - ...

    Restrict the length of each pro and con to 20 words or less.
    """
)

# llm = ChatGroq(
#     api_key=os.getenv("GROQ_API_KEY"),
#     model="llama-3.3-70b-versatile",
#     temperature=0,
# )

llm = ChatOpenAI(
    openai_api_key=os.getenv("GH_MODELS_TOKEN"),
    openai_api_base="https://models.github.ai/inference",
    model_name="openai/gpt-4.1-mini",
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({"topic": "artificial intelligence"})
print(response)
