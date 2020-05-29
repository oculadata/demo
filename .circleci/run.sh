
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/AigiosAlphaServer.pem ec2-user@18.222.18.219 bash -c '~/bin/DemoDaemon.sh'
