import streamlit as st
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = api_key

# Page configuration
st.set_page_config(page_title="RetailIQ AI Dashboard", layout="wide")
st.title("RetailIQ - AI Powered Sales Assistant")
st.write("Ask anything about your sales data in plain English.")

# Connect to Gemini via LiteLLM
llm = LiteLLM(model="gemini/gemini-2.5-flash")
pai.config.set({"llm": llm})

# Load cleaned dataset
df = pai.read_csv("superstore_cleaned.csv")

# Initialize session state to hold the current question text
if "question_text" not in st.session_state:
    st.session_state.question_text = ""

# Sidebar - sample questions for quick demo
st.sidebar.title("Sample Questions")
sample_questions = [
    "Which region had the highest profit?",
    "Which category has the most sales?",
    "What is the average discount in the Furniture category?",
    "Top 5 customers by profit?",
    "Which month had the highest sales?"
]

for q in sample_questions:
    if st.sidebar.button(q):
        st.session_state.question_text = q

# Main input area - bound directly to session state
user_question = st.text_input(
    "Type your question here:",
    key="question_text"
)

if st.button("Ask") and user_question:
    with st.spinner("Thinking..."):
        try:
            response = df.chat(user_question)
            st.success("Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"Something went wrong: {e}")