from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def marketing_agent(question):
    prompt = f"""
You are a Marketing Consultant.

Analyze the user's business and provide:
1. Marketing Strategy
2. Social Media Ideas
3. Advertising Suggestions
4. Customer Growth Ideas

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content