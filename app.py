import streamlit as st
from dotenv import load_dotenv

from agents.sales_agent import sales_agent
from agents.marketing_agent import marketing_agent
from agents.finance_agent import finance_agent
from agents.customer_agent import customer_agent
from agents.manager_agent import manager_agent

# Load Environment Variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="Multi-Agent Business Consultant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Multi-Agent Business Consultant")
st.markdown("### Get Business Advice from Multiple AI Experts")

# User Input
question = st.text_area(
    "Enter Your Business Question",
    placeholder="Example: My sales have dropped by 20%. What should I do?"
)

# Button
if st.button("Analyze Business"):

    if question.strip() == "":
        st.warning("Please enter a business question.")
    else:

        with st.spinner("Analyzing your business..."):

            # Agents
            sales_response = sales_agent(question)

            marketing_response = marketing_agent(question)

            finance_response = finance_agent(question)

            customer_response = customer_agent(question)

            manager_response = manager_agent(
                question,
                sales_response,
                marketing_response,
                finance_response,
                customer_response
            )

        st.success("Analysis Completed Successfully ✅")

        st.divider()

        st.subheader("📊 Sales Agent")
        st.write(sales_response)

        st.divider()

        st.subheader("📢 Marketing Agent")
        st.write(marketing_response)

        st.divider()

        st.subheader("💰 Finance Agent")
        st.write(finance_response)

        st.divider()

        st.subheader("👥 Customer Support Agent")
        st.write(customer_response)

        st.divider()

        st.subheader("🧠 Manager Agent")
        st.write(manager_response)