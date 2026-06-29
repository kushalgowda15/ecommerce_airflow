import pandas as pd
import os

def extract_data():
    print("Starting extraction...")

    RAW_CSV = "/opt/airflow/data/raw/OnlineRetail.csv"
    OUT_CSV = "/opt/airflow/data/processed/extracted_sales.csv"

    if not os.path.exists(RAW_CSV):
        print(f"File not found: {RAW_CSV}")
        return

    df = pd.read_csv(RAW_CSV, encoding="latin1")
    print(f"Loaded {len(df)} rows")

    # Select important columns
    cols = ["InvoiceNo", "StockCode", "Description", "Quantity", 
            "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
    df = df[[c for c in cols if c in df.columns]]

    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    df.to_csv(OUT_CSV, index=False)
    print(f"Extraction complete — saved to {OUT_CSV}")

if __name__ == "__main__":
    extract_data()
