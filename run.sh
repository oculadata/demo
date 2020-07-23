DAEMON="${1:-DemoDaemon}.sh"
shift
PARAMS="$*"
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/AigiosAlphaServer.pem airflow@airflow.oculadata.com bash -c "~/bin/$DAEMON $PARAMS"
