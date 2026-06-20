# E-Commerce Cloud Data Analytics Pipeline (Automated)

An end-to-end cloud data engineering pipeline that automates data generation, cloud warehousing, and live BI visualization.

## 📊 Live Dashboard
* **Tableau Public:** [View the Interactive Dashboard Here](https://public.tableau.com/app/profile/satya.prakash.singh5812/viz/E-CommerceCloudDataAnalyticsPipelineAutomated/Sheet1?publish=yes)

## 🚀 Tech Stack & Architecture
* **Language:** Python 3.x (Data generation & pipeline engine using Pandas)
* **Cloud Data Warehouse:** Snowflake (Secure data storage & SQL querying)
* **Automation:** Windows Task Scheduler (Daily production pipeline trigger)
* **Business Intelligence:** Tableau (Interactive sales performance dashboard)
* **Security:** Environment variables (`.env`) used for secure credential management.

## ⚙️ How it Works
1. A Python script (`load_data.py`) generates dummy e-commerce sales records.
2. The script securely connects to a Snowflake database using `snowflake-connector-python`.
3. The data is automatically uploaded and appended to the Snowflake table.
4. The process is scheduled to run daily, ensuring the database is always up-to-date.
5. The Tableau dashboard visualizes the processed data to track category-wise sales performance.

## 🔒 Security Note
To run this project locally, you must create a `.env` file in the root directory with your own Snowflake credentials:
SF_USER=your_username
SF_PASSWORD=your_password
SF_ACCOUNT=your_account_identifier
