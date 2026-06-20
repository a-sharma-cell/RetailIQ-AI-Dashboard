import pandas as pd
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini via LiteLLM
llm = LiteLLM(model="gemini/gemini-2.5-flash", api_key=api_key)

# Configure
pai.config.set({"llm": llm})

# Load cleaned data
df = pai.read_csv("superstore_cleaned.csv")

# Test questions
response = df.chat("Which region had the highest profit?")
print(response)