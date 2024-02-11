from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st

import pandas as pd

from pandasai import SmartDataframe
from pandasai.llm import OpenAI


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
llm = OpenAI(api_token=OPENAI_API_KEY)

st.title("CSV Analysis with PandasAI")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))
    df = SmartDataframe(df, config={"llm": llm})
    
    prompt = st.text_area("Enter your prompt:")

    submit = st.button("Generate")

    if submit:
        if prompt:
            with st.spinner("Generating response, please wait..."):
                st.write(df.chat(prompt))
        else:
            st.warning("Please enter a prompt.")









