from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def print_demo():
    return 'Data CICD demo!'


dag = DAG('demo_july', description='Simple demo DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 7, 15), catchup=False)

dummy_operator = DummyOperator(task_id='first_task', retries=3, dag=dag)

demo_operator = PythonOperator(
    task_id='demo_task', python_callable=print_demo, dag=dag)

dummy_operator >> demo_operator
