from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

# Define default arguments
default_args = {
    'owner': 'student',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Create the DAG
dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(days=1)
)

# Define tasks
extract_task = DummyOperator(
    task_id='extract_task',
    dag=dag
)

transform_task = DummyOperator(
    task_id='transform_task',
    dag=dag
)

load_task = DummyOperator(
    task_id='load_task',
    dag=dag
)

# Set task dependencies
extract_task >> transform_task >> load_task
