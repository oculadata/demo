import airflow
from airflow import DAG
from airflow.contrib.operators.databricks_operator import DatabricksSubmitRunOperator

args = {
    'owner': 'airflow',
    'email': ['dev@oculadata.com'],
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1)
}

dag = DAG(
    dag_id='databricks_create_job',
    default_args=args,
    schedule_interval=None)

test_cluster = {
    'spark_version': '6.5 (includes Apache Spark 2.4.5, Scala 2.11)',
    'node_type_id': 'm5.large',
    'aws_attributes': {'availability': 'ON_DEMAND'},
    'num_workers': 1}

notebook_task_params = {'airlfow_cluster': test_cluster, 'notebook_task': {
    'notebook_path': '/Users/yuantai.du@gmail.com/Data Lake PoC', }, }

notebook_task = DatabricksSubmitRunOperator(
    task_id='notebook_task', dag=dag, json=notebook_task_params)

notebook_task
