#/bin/bash


# This script will set CPU Utilization Alarm for Staging EC2 Server

_Project="project-name"

_arnAWS="arnAWS"


# Retrive Instance Id for all Staging Server 

_instanceId=`aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[0].Value]' --output text |grep -i stag | awk '{print $1}'`



for instanceId in $_instanceId

do 
		# Retrive Tag Name associated with each Instance id

		_instanceName=`aws ec2 describe-tags --filters "Name=resource-id,Values=$instanceId" --query Tags[*].Value --output text`

			echo "Setting Alarm for $_instanceName"

				aws cloudwatch put-metric-alarm --alarm-name $_Project-$_instanceName-60-PERCENT-CPU-UTILIZATION --alarm-description "Alarm when CPU exceeds 60%" --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 60 --threshold 60 --comparison-operator GreaterThanThreshold  --dimensions  Name=InstanceId,Value=$instanceId  --evaluation-periods 5 --alarm-actions $_arnAWS --unit Percent

					
			done

echo "All the Alarms for CPU Utilization has been Set."

