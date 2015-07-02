'''
README
@Vikash


This script will generate RDS Snapshot


'''

from boto import rds
from boto import vpc
import datetime



connection=rds.connect_to_region('us-east-1',aws_access_key_id='',aws_secret_access_key='')
dbInstances=connection.get_all_dbinstances()

for instance in dbInstances:
	print "%s\t%s\t %s" %(instance.status,instance.endpoint,instance.id)

_date=(datetime.date.today().strftime("%d-%B-%Y"))

for instance in dbInstances:
	instance.snapshot(instance.id+_date)

