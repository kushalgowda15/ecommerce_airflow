from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default settings for all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    dag_id='ecommerce_etl',
    default_args=default_args,
    description='E-commerce ETL Pipeline: Extract → Transform → Load',
    schedule_interval='@daily',   # Runs every day at midnight
    start_date=datetime(2025, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=['ETL', 'Ecommerce'],
) as dag:

    # 1️ Extract task
    extract_task = BashOperator(
        task_id='extract_data',
        bash_command='python /opt/airflow/scripts/extract_data.py'
    )

    # 2️ Transform task
    transform_task = BashOperator(
        task_id='transform_data',
        bash_command='python /opt/airflow/scripts/transform_data.py'
    )

    # 3️ Load task
    load_task = BashOperator(
        task_id='load_data',
        bash_command='python /opt/airflow/scripts/load_data.py'
    )

    # Define execution order
    extract_task >> transform_task >> load_task
