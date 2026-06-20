"""
RetailIQ - Data Cleaning
Cleans raw Sample Superstore CSV 
"""

import pandas as pd

# 1. Load raw data
df = pd.read_csv("superstore_raw.csv")
print("Raw shape:", df.shape)

# 2. Drop junk rows (rows with no Order Date = corrupted rows from bad export)
df = df[df["Order Date"].notnull()].copy()
print("After dropping junk rows:", df.shape)

# 3. Drop exact duplicate rows (safety check, should be 0)
df = df.drop_duplicates()
print("After dropping duplicates:", df.shape)

# 4. Rename columns to snake_case
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)
print("New columns:", list(df.columns))

# 5. Fix data types
df["order_date"] = pd.to_datetime(df["order_date"], format="%m/%d/%Y")
df["ship_date"] = pd.to_datetime(df["ship_date"], format="%m/%d/%Y")
df["quantity"] = df["quantity"].astype(int)

# Burlington, VT rows are missing postal_code in source data; real ZIP is 05401
df.loc[df["postal_code"].isnull() & (df["city"] == "Burlington"), "postal_code"] = 5401
df["postal_code"] = df["postal_code"].astype(int)
df["sales"] = df["sales"].astype(float)
df["discount"] = df["discount"].astype(float)
df["profit"] = df["profit"].astype(float)

# 6. Quick sanity checks (negative profit is a real insight, NOT an error - keep it)
print("\nNulls remaining:\n", df.isnull().sum().sum())
print("Negative profit rows (kept intentionally):", (df["profit"] < 0).sum())

# 7. Save cleaned file
df.to_csv("superstore_cleaned.csv", index=False)
print("\nSaved: superstore_cleaned.csv | Final shape:", df.shape)