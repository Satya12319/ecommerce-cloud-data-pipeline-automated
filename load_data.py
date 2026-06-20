import os
import random
import pandas as pd
import snowflake.connector
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

print("🔄 Data Pipeline starting...")

# 1. Mock Data Generator (Generates dummy e-commerce sales data)
products = {
    'Electronics': ['Laptop', 'Smartphone', 'Wireless Earbuds'],
    'Clothing': ['T-Shirt', 'Jeans', 'Hoodie'],
    'Home Decor': ['Desk Lamp', 'Scented Candle', 'Wall Art']
}

data = []
for i in range(10): # Generates 10 new sales records on every run
    cat = random.choice(list(products.keys()))
    prod = random.choice(products[cat])
    data.append([
        random.randint(10000, 99999),
        prod, cat,
        random.randint(1, 3),
        round(random.uniform(10.0, 500.0), 2),
        datetime.today().strftime('%Y-%m-%d'),
        random.choice(['US', 'UK', 'India', 'Germany'])
    ])

df = pd.DataFrame(data, columns=['ORDER_ID', 'PRODUCT_NAME', 'CATEGORY', 'QUANTITY', 'PRICE', 'ORDER_DATE', 'COUNTRY'])
print("✅ 10 Dummy Sales Records generated successfully!")

# 2. Hardcoded Credentials (Temporary setup for local testing)
# ⚠️ Update these values after creating your Snowflake account
SF_USER = os.getenv('SF_USER')
SF_PASSWORD = os.getenv('SF_PASSWORD')
SF_ACCOUNT = os.getenv('SF_ACCOUNT') 

print("🔗 Connecting to Snowflake Cloud Data Warehouse...")
try:
    conn = snowflake.connector.connect(
        user=SF_USER,
        password=SF_PASSWORD,
        account=SF_ACCOUNT,
        warehouse='COMPUTE_WH',
        database='ECOMMERCE_DB',
        schema='SALES_SCHEMA'
    )
    cursor = conn.cursor()

# # 3. Insert Data into Snowflake
    print("📥 Uploading data to Snowflake using Pandas Tools...")

    from snowflake.connector.pandas_tools import write_pandas

    # Loop chalane ki jagah ye direct poori table ko ek baar mein bhej dega
    success, nchunks, nrows, _ = write_pandas(
    conn=conn, 
    df=df, 
    table_name='DAILY_SALES', # Snowflake mein table ka naam upper-case mein hona chahiye
    database='ECOMMERCE_DB', 
    schema='SALES_SCHEMA',
    overwrite=True # Yeh line purane data ko automatic clear (truncate) kar degi!
)

    conn.commit()
    cursor.close()
    conn.close()
    print("🎉 SUCCESS: Data fully automated to Snowflake!")
    df.to_csv('C:/Users/ssaty/OneDrive/Desktop/minor-project-2/Live_Sales.csv', index=False)
except Exception as e:
    print("❌ ERROR OCCURRED:", e)