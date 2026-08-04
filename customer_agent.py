from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def customer_agent(question):
    prompt = f"""
You are an expert Customer Support Consultant.

Analyze the business problem and provide:

1. Customer Issues
2. Customer Satisfaction Tips
3. Customer Retention Ideas
4. Loyalty Program Suggestions

Business Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content