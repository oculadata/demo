DAGS_DIR=airflow/dags
test -d $DAGS_DIR || echo "Can't find folder for DAGs" >&2

for f in $DAGS_DIR/*.py ; do
    scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/AigiosAlphaServer.pem $f airflow@airflow.oculadata.com:airflow/dags/
done


