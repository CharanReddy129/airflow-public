from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="example_git_dag",
    default_args=default_args,
    description="Simple DAG from GitSync",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    task1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    task2 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello from GitSync DAG!'",
    )

    task1 >> task2
