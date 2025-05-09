# -*- coding: utf-8 -*-
"""app file.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SfXvA-4unBUOI2YTiSHmpKEx05XE_dLh
"""

import streamlit as st
from langflow.load import run_flow_from_json

# Langflow TWEAKS - replace keys as per your Langflow component IDs
TWEAKS = {
    "Agent-rtMVt": {},
    "ChatInput-PbWyM": {},
    "ChatOutput-qp39q": {},
    "URL-zYBte": {},
    "CalculatorComponent-cAJeb": {},
    "ScrapeGraphSmartScraperApi-YOAJI": {},
    "Serp-QyoDu": {}
}

st.set_page_config(page_title="💸 Price Comparison Agent")
st.title("🧠 Langflow AI: Price Comparison Agent")
st.write("Ask your AI agent to compare prices or fetch info!")

user_input = st.text_input("🔍 Ask your question:")

if st.button("Run Agent") and user_input:
    with st.spinner("Running Langflow agent..."):
        try:
            result = run_flow_from_json(
                flow="Price Comparison Agent.json",
                input_value=user_input,
                session_id="",
                fallback_to_env_vars=True,
                tweaks=TWEAKS
            )
            st.success("✅ Agent responded:")
            st.write(result)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")