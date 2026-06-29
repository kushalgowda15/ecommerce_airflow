import pandas as pd
import sqlite3
import os

def load_data():
    print("Starting loading process...")

    IN_CSV = "/opt/airflow/data/processed/cleaned_sales.csv"
    DB_PATH = "/opt/airflow/data/ecommerce.db"

    if not os.path.exists(IN_CSV):
        print(f"File not found: {IN_CSV}")
        return

    df = pd.read_csv(IN_CSV)
    print(f"Loaded {len(df)} rows for loading")

    #  Select only the main columns
    cols = [
        "order_id", "product_id", "product_desc", "quantity",
        "invoice_date", "unit_price", "customer_id", "country", "total_price"
    ]
    df = df[[c for c in cols if c in df.columns]]

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    # Check if the existing DB is corrupted, delete and recreate if needed
    if os.path.exists(DB_PATH):
        try:
            conn = sqlite3.connect(DB_PATH)
            conn.execute("SELECT name FROM sqlite_master LIMIT 1;")
            conn.close()
        except sqlite3.DatabaseError:
            print(" Detected invalid database file. Recreating it...")
            os.remove(DB_PATH)

    #  Create new DB connection and insert data
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    #  Print final status
    db_size_kb = os.path.getsize(DB_PATH) / 1024
    print(f" Data successfully loaded into database: {DB_PATH}")
    print(f" Total rows inserted: {len(df)}")
    print(f" Database size: {db_size_kb:.2f} KB")

if __name__ == "__main__":
       load_data()
