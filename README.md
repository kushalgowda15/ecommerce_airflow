# ecommerce_airflow

A minimal Airflow-friendly ETL project for the OnlineRetail dataset. This repository contains
a small extract → transform → load pipeline implemented as standalone Python scripts and
an Airflow DAG that calls them.

## Repository layout

- `dags/` — Airflow DAG(s). Contains `ecommerce_etl_dag.py`.
- `scripts/` — ETL scripts used by the DAG:
	- `extract_data.py` — reads raw CSV and writes `extracted_sales.csv`.
	- `transform_data.py` — cleans, deduplicates and enriches; writes `cleaned_sales.csv`.
	- `load_data.py` — loads cleaned CSV into SQLite `data/ecommerce.db`.
- `data/raw/` — put the original `OnlineRetail.csv` here (not included in repo).
- `data/processed/` — intermediate CSVs created by the ETL.
- `data/ecommerce.db` — output SQLite database created by the loader.
- `docker-compose.yaml` — minimal template for running Airflow + Postgres (edit before use).
- `requirements.txt` — Python dependencies for running the scripts locally.

## What this project does

- Extract: select the key columns from the raw CSV and write them to `data/processed/extracted_sales.csv`.
- Transform: rename and normalize columns, remove duplicates and rows with missing values, filter out non-positive quantities, convert dates, and add a `total_price` column (`quantity * unit_price`). Output is `data/processed/cleaned_sales.csv`.
- Load: persist the cleaned table into SQLite (`data/ecommerce.db`) under table `sales`.

## Prerequisites

- Python 3.8+ installed on Windows.
- PowerShell (instructions use PowerShell commands).
- The original `OnlineRetail.csv` dataset (Kaggle). Place it at `data/raw/OnlineRetail.csv`.

## Setup (recommended: use a virtual environment)

Open PowerShell in the project root (`C:\Users\gowda\Downloads\FDEPROJECT\ecommerce_airflow`) and run:

```powershell
# create and activate venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt
```

Notes:
- `requirements.txt` contains `pandas`, `sqlalchemy`, and a pinned `apache-airflow` version used only if you plan to run the included `docker-compose`/Airflow setup. If you only want to run the ETL scripts locally, `pandas` and `sqlalchemy` (and `psycopg2-binary` only if you plan to connect Postgres) are sufficient.

## Running the ETL locally (no Airflow)

1. Place the dataset file `OnlineRetail.csv` into `data/raw/`.

2. Run the scripts in order from PowerShell (with the venv activated):

```powershell
python .\scripts\extract_data.py
python .\scripts\transform_data.py
python .\scripts\load_data.py
```

Each script prints progress and output paths. After successful run:
- `data/processed/extracted_sales.csv` — result of extract
- `data/processed/cleaned_sales.csv` — result of transform
- `data/ecommerce.db` — SQLite DB with table `sales`

## Running with Airflow (Docker)

The included `docker-compose.yaml` is a minimal template. It is not a production-ready Airflow configuration — it is a starting point.

Quick steps (high level):

1. Ensure Docker Desktop is installed and running.
2. Optionally set `AIRFLOW_UID`/`AIRFLOW_GID` in `.env` (already present as placeholders).
3. Edit `docker-compose.yaml` if required (paths, versions) and mount the project directory into the container so Airflow can see the `dags/`, `scripts/`, and `data/` folders.
4. Start the stack (from project root):

```powershell
docker compose up -d
# then follow the Airflow webserver at http://localhost:8080
```

For a fully working Airflow + Docker development environment use the official Airflow Docker Compose example (recommended) and adapt the DAG and scripts into that environment.

## Verifying results

- To inspect the cleaned CSV: open `data/processed/cleaned_sales.csv` in Excel or a text editor.
- To inspect the SQLite DB:

```powershell
# (Windows) using sqlite3 if installed
sqlite3 data\ecommerce.db
```

Or open `data/ecommerce.db` with a GUI tool like DB Browser for SQLite.

## Metrics you can collect

From the scripts' logic you can collect the following metrics before/after transformation:
- Total records before transformation = rows in `data/processed/extracted_sales.csv` (the extractor preserves all rows from the raw CSV).
- Total records after transformation = rows in `data/processed/cleaned_sales.csv` (after drop_duplicates, dropna, and quantity>0 filters).
- Duplicates removed: `transform_data.py` calls `drop_duplicates()` but the script prints only a combined "removed X invalid rows" that includes duplicates, NA rows and quantity<=0 rows. To get per-category counts run a small pandas script.
- Columns before: `InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country` (if present in the raw file).
- Columns after: `order_id, product_id, product_desc, quantity, invoice_date, unit_price, customer_id, country, total_price` (the `total_price` column is newly added).

If you want an exact numeric metrics report I can provide a tiny script (`scripts/metrics_from_files.py`) that reads both CSVs and prints the counts; tell me if you'd like that added and I will include it.

## Troubleshooting

- If `extract_data.py` reports the raw CSV file missing, confirm the file is at `data/raw/OnlineRetail.csv` and that the path is readable by your user.
- If `transform_data.py` raises KeyError for columns, check the extracted CSV header to confirm the expected column names are present; the transformer normalizes column names and expects the 8 standard columns.
- If `load_data.py` reports a corrupted DB, it will try to recreate `data/ecommerce.db`; check file permissions if this fails.

## Notes / Next steps

- The included `docker-compose.yaml` is intentionally minimal. For production-like usage, prefer the official Airflow Docker Compose setup and adapt the DAG and scripts.
- If you want I can add a `scripts/metrics_from_files.py` to compute the exact numbers you requested (total rows, duplicates removed, missing values before/after, column lists, whether `total_price` was added). Reply and I'll add it and run it for you.

---

If anything in these instructions doesn't match your environment, tell me what OS/versions you prefer and I'll adapt the commands.

