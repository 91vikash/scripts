'''
README
@Vikash

This script will give the Instance Name with the given Instance Id

Usage : python getInstanceName.py instance_id
'''


import boto
import sys
from boto import ec2
connection=ec2.connect_to_region("us-east-1")
	
def getTagByName(instanceid):
	 reservations=connection.get_all_instances(filters={'instance_id':sys.argv[1]})
	 for r in reservations:
 		for i in r.instances:
			 print i.tags['Name']


getTagByName(sys.argv[1])
