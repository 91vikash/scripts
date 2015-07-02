'''
README
@Vikash


This script will delete all the snapshot which is 30 days old


'''



import boto 
import datetime
import dateutil
from dateutil import parser
from boto import ec2

connection=ec2.connect_to_region("us-east-1")

#Get All Snapshot associated with your account

allSnapshots=connection.get_all_snapshots(owner='AWSAccountNumber')

#Define the time limit
timeLimit=datetime.datetime.now() - datetime.timedelta(days=30)

for snapshot in allSnapshots:
	if parser.parse(snapshot.start_time).date() <= timeLimit.date():
		print "Deleting Snapshot %s " %(snapshot.id)
		connection.delete_snapshot(snapshot.id)
	    
	else:    
		print "No Snapshots Found before 30 days"
		    
		    
	
    


