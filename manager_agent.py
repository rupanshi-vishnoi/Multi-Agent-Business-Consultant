from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def manager_agent(question,
                  sales,
                  marketing,
                  finance,
                  customer):

    prompt = f"""
You are the CEO of a company.

Below are reports from different AI experts.

Sales Report:
{sales}

Marketing Report:
{marketing}

Finance Report:
{finance}

Customer Report:
{customer}

Using all reports, prepare:

1. Executive Summary
2. Top 5 Problems
3. Priority Action Plan
4. Short-Term Strategy
5. Long-Term Strategy
6. Final Recommendation

Original Business Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content