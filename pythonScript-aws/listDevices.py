'''
README

@Vikash

This script will generate the list of all running/stopped Instances and associated IP Address.

You can also get the Instance's other information like attached securityGroup, KeyPairs, Volume etc

'''

import boto 
from boto import ec2

connection=ec2.connect_to_region("us-east-1")

reservations=connection.get_all_instances();


def getTag(instanceId):
	for r in reservations:
		for i in r.instances:
			return i.tags['Name']
	
	
for reservation in reservations:
	for instances in reservation.instances:
		print "%s \t\t\t  %s"  % (instances.tags['Name'], instances.ip_address)


