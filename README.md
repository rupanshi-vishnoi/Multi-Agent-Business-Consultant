# Multi-Agent Business Consultant 🤖

## Overview
Multi-Agent Business Consultant is an AI-powered business analysis application that helps users understand business data and generate actionable insights. The project uses Generative AI, Large Language Models (LLMs), Retrieval Augmented Generation (RAG), and a multi-agent architecture to analyze information, retrieve relevant knowledge, and provide intelligent business recommendations.

## Features
- AI-based business consulting and decision support
- Multi-agent architecture for specialized tasks
- RAG-based knowledge retrieval system
- Sales data analysis and business insights generation
- Automated recommendations for improving business performance
- Interactive user interface built with Streamlit

## Technologies Used
- Python
- Streamlit
- Generative AI (LLM)
- RAG (Retrieval Augmented Generation)
- LangChain
- Vector Database
- Pandas
- Machine Learning Concepts

## Project Structure
Multi-Agent-Business-Consultant
│
├── agents
│ └── AI agents for business analysis
│
├── data
│ ├── sales.csv
│ └── create_vector.py
│
├── rag
│ └── RAG pipeline implementation
│
├── knowledge_base
│ └── Business knowledge documents
│
├── app.py
│ └── Streamlit application
│
└── README.md

## How to Run the Project

### 1. Create Virtual Environment
python -m venv venv


### 2. Activate Environment
Windows:
venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Create Vector Database
python data/create_vector.py


### 5. Run Application
streamlit run app.py


## Use Cases
- Business performance analysis
- Sales trend identification
- Customer and market insights
- Data-driven decision making
- AI-powered business recommendations

## Future Improvements
- Integration with real-time business data
- Advanced analytics dashboard
- More specialized AI agents
- Improved recommendation system

## Author
Rupanshi Vishnoi