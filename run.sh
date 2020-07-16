DAEMON="${1:-DemoDaemon}.sh"
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/AigiosAlphaServer.pem airflow@airflow.oculadata.com bash -c "~/bin/$DAEMON"
