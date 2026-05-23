import os
import random
import pandas as pd
import snowflake.connector
from datetime import datetime

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
SF_USER = 'SatyaSingh12'
SF_PASSWORD = 'Satyasingh@0987'
SF_ACCOUNT = 'upc13072.us-east-1' 

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

    # 3. Insert Data into Snowflake
    print("📤 Uploading data to Snowflake...")
    for index, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO daily_sales (order_id, product_name, category, quantity, price, order_date, country)
            VALUES ({row['ORDER_ID']}, '{row['PRODUCT_NAME']}', '{row['CATEGORY']}', {row['QUANTITY']}, {row['PRICE']}, '{row['ORDER_DATE']}', '{row['COUNTRY']}')
        """)

    conn.commit()
    cursor.close()
    conn.close()
    print("🎉 SUCCESS: Data successfully loaded to Snowflake Cloud!")

except Exception as e:
    print("❌ ERROR OCCURRED:", e)