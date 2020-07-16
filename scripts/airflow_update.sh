test -d airflow/dags || echo "Can't find folder for DAGs" >&2

scp -i ~/.ssh/AigiosAlphaServer.pem airflow/dags/* airflow@airflow.oculadata.com:airflow/dags/


