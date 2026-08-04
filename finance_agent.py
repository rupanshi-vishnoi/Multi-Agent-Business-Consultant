from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def finance_agent(question):
    prompt = f"""
You are an expert Financial Consultant.

Analyze the business and provide:
1. Financial Problems
2. Profit Improvement Ideas
3. Cost Reduction Suggestions
4. Investment Advice

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content