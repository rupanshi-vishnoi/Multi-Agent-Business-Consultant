from utils.data_analysis import get_summary
from dotenv import load_dotenv 
import os
from langchain_groq import ChatGroq
from utils.data_analysis import get_summary

load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def sales_agent(question):

    summary = get_summary()

    prompt = f"""
You are an expert Sales Consultant.

Business Data:

Total Sales: {summary['Total Sales']}
Total Profit: {summary['Total Profit']}
Total Orders: {summary['Total Orders']}
Top Product: {summary['Top Product']}
Top City: {summary['Top City']}

User Question:
{question}

Analyze the business and provide:
1. Sales Analysis
2. Problems
3. Recommendations
4. Growth Strategy
"""

    response = llm.invoke(prompt)

    return response.content