#!/usr/bin/env bash

PROJECT=$1

LOG=~/log/DemoDaemon.log

date | tee $LOG

echo
echo "Workload dispatched to 1 pod" | tee -a $LOG

echo
echo "Checking Data Source..." | tee -a $LOG
ls /efs > /dev/null 2>&1 || echo "Unable to find data source" | tee -a $LOG

[ ! -d workspace ] && mkdir workspace
cd workspace
rm -rf *

echo | tee -a $LOG
echo "Retrieving Data..." | tee -a $LOG
for f in /efs/${PROJECT}
do
    cp $f .
done

echo | tee -a $LOG
echo "Uploading to Landing Bucket..."  | tee -a $LOG
for f in *
do
    aws s3 cp $f s3://oculadatalanding/${PROJECT}/  | tee -a $LOG
done

echo | tee -a $LOG
echo "Job completed!" | tee -a $LOG

