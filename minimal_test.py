import streamlit as st
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = api_key

llm = LiteLLM(model="gemini/gemini-2.5-flash")
pai.config.set({"llm": llm})

df = pai.read_csv("superstore_cleaned.csv")

if st.button("Test"):
    response = df.chat("Which region had the highest profit?")
    st.write(response)
    