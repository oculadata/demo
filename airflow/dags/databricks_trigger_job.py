import airflow
from airflow import DAG
from airflow.contrib.operators.databricks_operator import DatabricksRunNowOperator

args = {
    'owner': 'airflow',
    'email': ['dev@oculadata.com'],
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1)
}

dag = DAG(
    dag_id='databricks_trigger_job', default_args=args,
    schedule_interval='None')

job_run = DatabricksRunNowOperator(
    task_id='job_task',
    dag=dag,
    job_id=17160)

job_run
