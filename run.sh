DAEMON="${1:-DemoDaemon}.sh"
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/AigiosAlphaServer.pem ec2-user@3.133.134.32 bash -c "~/bin/$DAEMON"
