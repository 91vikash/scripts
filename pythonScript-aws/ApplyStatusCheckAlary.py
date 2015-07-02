'''
README
@Vikash


This script will create status check alarm for all Instances:


'''


import boto
import boto.ec2.cloudwatch
import sys
from boto import ec2
connection=ec2.connect_to_region("us-east-1")
cloudwatchConn=boto.ec2.cloudwatch.connect_to_region("us-east-1")	
reservations=connection.get_all_instances();
for r in reservations:
	for i in r.instances:
		alarm=boto.ec2.cloudwatch.alarm.MetricAlarm(connection = cloudwatchConn,
        name = i.tags['Name'] + "-status-alarm",
        metric = 'StatusCheckFailed',
        namespace = 'AWS/EC2',
        statistic = 'Maximum',
        comparison = '>=',
        description = 'status check for %s %s' % (i.id, i.tags['Name']),
        threshold = 1.0,
        period = 60,
        evaluation_periods = 2,
        dimensions = {'InstanceId':i.id},
        alarm_actions = 'arn:aws:sns:us-east-1:XXXXXXXXXXXXXX:boto-script-execution')
        
        
        cloudwatchConn.put_metric_alarm(alarm)
        
        

