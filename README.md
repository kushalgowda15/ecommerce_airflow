# 🛒 E-Commerce ETL Pipeline using Apache Airflow & Docker

## 📌 Project Overview

This project implements an automated **Extract–Transform–Load (ETL)** pipeline for e-commerce transaction data using **Apache Airflow**, **Docker**, and **Python**. The workflow automates data extraction, cleaning, transformation, and loading into a SQLite database, providing a reliable and reproducible data engineering solution. :contentReference[oaicite:0]{index=0}

The pipeline is orchestrated using Apache Airflow DAGs, containerized with Docker for portability, and designed following modern data engineering best practices.

---

## 🚀 Features

- Automated ETL workflow using Apache Airflow
- Docker-based deployment for reproducibility
- Data cleaning and preprocessing
- Scheduled workflow execution
- Task dependency management
- Processed data stored in SQLite database
- Modular and scalable pipeline architecture
- Ready for Business Intelligence and Analytics

---

# 🏗️ Architecture

```
                Raw CSV Dataset
                      │
                      ▼
            Extract Data Task
                      │
                      ▼
           Transform Data Task
        (Cleaning & Preprocessing)
                      │
                      ▼
              Load Data Task
              (SQLite Database)
                      │
                      ▼
          Analytics / Power BI / Tableau
```

Apache Airflow orchestrates the complete ETL workflow while Docker ensures a consistent execution environment.

---

# 📂 Project Structure

```
ecommerce_airflow/
│
├── dags/
│   └── ecommerce_etl_dag.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── database/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

**Dataset:** Online Retail Dataset

**Source:** UCI Machine Learning Repository

The dataset contains real-world online retail transactions, including:

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

The ETL pipeline transforms raw transactional data into a clean, analytics-ready format. :contentReference[oaicite:1]{index=1}

---

# ⚙️ Technologies Used

## Programming

- Python 3.x

## Data Processing

- Pandas
- NumPy

## Workflow Orchestration

- Apache Airflow

## Containerization

- Docker
- Docker Compose

## Database

- SQLite

## Development

- Jupyter Notebook
- Visual Studio Code

---

# 🔄 ETL Workflow

## 1. Extract

- Reads raw sales data
- Validates file availability
- Loads data into memory

---

## 2. Transform

- Removes duplicate records
- Handles missing values
- Cleans inconsistent entries
- Formats date columns
- Generates processed dataset

---

## 3. Load

- Stores cleaned data into SQLite
- Creates analytics-ready tables
- Enables downstream reporting

---

# 📈 Apache Airflow DAG

The pipeline is orchestrated through Apache Airflow using three dependent tasks:

```
Extract Data
      │
      ▼
Transform Data
      │
      ▼
Load Data
```

The DAG ensures:

- Sequential execution
- Automatic scheduling
- Retry handling
- Execution monitoring
- Dependency management

---

# 🐳 Docker Integration

Docker is used to:

- Eliminate dependency conflicts
- Ensure reproducible execution
- Simplify deployment
- Package Airflow and project components together

---

# 📊 Output

The pipeline generates:

- Cleaned CSV dataset
- Processed sales dataset
- SQLite database
- Airflow execution logs
- Analytics-ready data

---

# ▶️ Getting Started

## Clone Repository

```bash
git clone https://github.com/kushalgowda15/ecommerce_airflow.git
```

## Navigate to Project

```bash
cd ecommerce_airflow
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Docker Containers

```bash
docker-compose up -d
```

## Launch Apache Airflow

```bash
http://localhost:8080
```

Enable the DAG and trigger the workflow from the Airflow UI.

---

# 📊 Results

The implemented ETL pipeline successfully:

- Automated the complete ETL process
- Improved data quality through cleaning and transformation
- Reduced manual intervention
- Produced structured data for business intelligence
- Demonstrated reliable execution using Apache Airflow and Docker :contentReference[oaicite:2]{index=2}

---

# 🔮 Future Enhancements

- Integrate PostgreSQL or MySQL
- Deploy to AWS or Azure
- Add Apache Kafka for real-time streaming
- Connect with Snowflake, BigQuery, or Amazon Redshift
- Build Power BI/Tableau dashboards
- Add monitoring and alerting
- Implement CI/CD with GitHub Actions :contentReference[oaicite:3]{index=3}

---

# 💼 Skills Demonstrated

- Data Engineering
- ETL Pipeline Development
- Apache Airflow
- Docker
- Python
- Pandas
- SQLite
- Workflow Automation
- Data Cleaning
- Data Processing

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

**Kushal Gowda**

- GitHub: https://github.com/kushalgowda15
