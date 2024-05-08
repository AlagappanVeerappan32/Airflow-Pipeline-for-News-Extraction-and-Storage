from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from datetime import timedelta
from NY_Times_ETL import my_function

default_args = {
    "owner": "alex_airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 5, 8),
    "email": ["xyz@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "NY_TIMES_Dag",
    default_args=default_args,
    description=" My NY_TIMES AIRFLOW EXTRACTION",
)

run_job = PythonOperator(
    task_id="NY_Times_ETL_JOB",
    callable=my_function,
    dag=dag,
)

run_job
