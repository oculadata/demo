from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.contrib.hooks.ssh_hook import SSHHook


sshHook = SSHHook(ssh_conn_id='kafka_ssh_connection')


dag = DAG('etf_retrieval', description='Simple demo DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 7, 15), catchup=False)

etf_retrieval = SSHOperator(
    task_id="retrieval",
    command='python3 retriever.py',
    ssh_hook=sshHook,
    #ssh_conn_id='kafka_ssh_connection',
    dag=dag)

etf_send = SSHOperator(
    task_id="send",
    command='bash send_file_to_topic.sh mytopic df_all.csv',
    ssh_hook=sshHook,
    dag=dag)

etf_check_recv = SSHOperator(
    task_id="recv",
    command='bash check_received.sh',
    ssh_hook=sshHook,
    dag=dag)

etf_upload = SSHOperator(
    task_id="upload",
    command='bash upload_aws',
    ssh_hook=sshHook,
    dag=dag)

etf_retrieval >> etf_send >> etf_check_recv >> etf_upload

