import pandas as pd
import mysql.connector

# Load cleaned data
df = pd.read_csv("superstore_cleaned.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="retailiq"
)
cursor = conn.cursor()

# Insert query
insert_query = """
INSERT INTO superstore_sales 
(row_id, order_id, order_date, ship_date, ship_mode, customer_id, customer_name,
 segment, country, city, state, postal_code, region, product_id, category,
 sub_category, product_name, sales, quantity, discount, profit)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = df.values.tolist()
cursor.executemany(insert_query, data)
conn.commit()

print(f"{cursor.rowcount} rows inserted successfully")

cursor.close()
conn.close()




