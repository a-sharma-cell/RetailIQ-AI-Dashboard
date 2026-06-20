import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

# Gemini connect karo
llm = LiteLLM(model="gemini/gemini-2.5-flash", api_key="AQ.Ab8RN6L7gynsgEzNH7LWn4LXIZ4UYCYCIbMxi_d5hv_nWQ4BKw")
# Configure
pai.config.set({"llm": llm})

# Cleaned data load karo
df = pai.read_csv("superstore_cleaned.csv")

# Test sawal poocho
response = df.chat("Which region had the highest profit?")
print(response)

response1 = df.chat("Which category has the most sales?")
print(response1)

response2 = df.chat("What is the average discount given in Furniture category?")
print(response2)