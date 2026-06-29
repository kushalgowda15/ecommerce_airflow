import pandas as pd
import os

def transform_data():
    print("Starting transformation...")

    IN_CSV = "/opt/airflow/data/processed/extracted_sales.csv"
    OUT_CSV = "/opt/airflow/data/processed/cleaned_sales.csv"

    if not os.path.exists(IN_CSV):
        print(f"File not found: {IN_CSV}")
        return

    df = pd.read_csv(IN_CSV)
    print(f"Loaded {len(df)} rows")

    # Standardize and rename columns
    df.columns = df.columns.str.strip().str.replace(" ", "").str.replace("-", "_")
    df = df.rename(columns={
        'InvoiceNo': 'order_id',
        'StockCode': 'product_id',
        'Description': 'product_desc',
        'Quantity': 'quantity',
        'UnitPrice': 'unit_price',
        'InvoiceDate': 'invoice_date',
        'CustomerID': 'customer_id',
        'Country': 'country'
    })

    # Remove duplicates and missing values
    before_rows = len(df)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df = df[df['quantity'] > 0]
    print(f"Removed {before_rows - len(df)} invalid rows")

    # Convert date and add total price
    if 'invoice_date' in df.columns:
        df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    if 'quantity' in df.columns and 'unit_price' in df.columns:
        df['total_price'] = df['quantity'] * df['unit_price']

    # Save cleaned data
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    df.to_csv(OUT_CSV, index=False)
    print(f"Transformation complete — saved to {OUT_CSV}")

if __name__ == "__main__":
    transform_data()
