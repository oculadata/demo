#!/usr/bin/env bash

LOG=~/log/DemoDaemon.log

date | tee $LOG

echo "Starting Demo Daemon..."

sleep 3

echo
echo "Initializing Kubernetes Environment..." | tee -a $LOG
sleep 30

echo
echo "Dispatch workload..." | tee -a $LOG
sleep 2

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
for f in /efs/*
do
    cp $f .
done

echo | tee -a $LOG
echo "Uploading to Landing Bucket..."  | tee -a $LOG
for f in *
do
    aws s3 cp $f s3://oculadatalanding/raw/  | tee -a $LOG
done

echo | tee -a $LOG
echo "Checking sibiling job status..." | tee -a $LOG
sleep 5

echo | tee -a $LOG
echo "Job completed!" | tee -a $LOG

echo | tee -a $LOG
echo "Exit Daemon? (y/n): y"

echo | tee -a $LOG
echo "Gracefully shutting down Daemon... "
sleep 5
