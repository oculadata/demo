test -d airflow/dags || echo "Can't find folder for DAGs" >&2

cp airflow/dags/* ~/airflow/dags/


